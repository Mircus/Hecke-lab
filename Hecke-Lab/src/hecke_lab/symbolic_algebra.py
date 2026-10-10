"""Symbolic algebra of coarse move classes.

This module is closer to the algebra slogan::

    T_a T_b = sum_c N_ab^c T_c

It does not attempt to derive structure constants from geometry. Instead, it
stores a finite table and lets examples/tests compose symbolic moves. This is
useful for sketching AI workflows as coarse operator classes.

Unlike the original scaffold, this version also checks the most basic algebraic
sanity condition: associativity. A multiplication table is not automatically an
algebra merely because we can write down structure constants.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass, field
from itertools import product
from typing import Iterable, Mapping

CoeffDict = Mapping[str, int | float]
LinearCombo = Mapping[str, int | float]


@dataclass
class SymbolicHeckeAlgebra:
    """A finite symbolic multiplication table of coarse move classes.

    The name is historical to Hecke-Lab. Users should check associativity before
    treating an arbitrary table as an actual algebra.
    """

    basis: set[str]
    structure_constants: dict[tuple[str, str], Counter[str]] = field(default_factory=dict)

    @classmethod
    def with_identity(cls, basis: Iterable[str], identity: str = "I") -> "SymbolicHeckeAlgebra":
        basis_set = set(basis) | {identity}
        alg = cls(basis=basis_set)
        for b in basis_set:
            alg.set_product(identity, b, {b: 1})
            alg.set_product(b, identity, {b: 1})
        return alg

    def set_product(self, left: str, right: str, result: CoeffDict) -> None:
        """Set product ``left * right`` as a finite linear combination."""
        self._require_basis(left)
        self._require_basis(right)
        for key in result:
            self._require_basis(key)
        self.structure_constants[(left, right)] = Counter(result)

    def product(self, left: str, right: str) -> Counter[str]:
        """Return the symbolic product of two basis elements.

        Unspecified products are treated as zero. This is convenient for sparse
        experiments, but it also means associativity should be checked explicitly.
        """
        self._require_basis(left)
        self._require_basis(right)
        return Counter(self.structure_constants.get((left, right), {}))

    def multiply_linear(self, left: LinearCombo, right: LinearCombo) -> Counter[str]:
        """Multiply two finite linear combinations by bilinearity."""
        out: defaultdict[str, float] = defaultdict(float)
        for left_term, left_coeff in left.items():
            self._require_basis(left_term)
            for right_term, right_coeff in right.items():
                self._require_basis(right_term)
                for result_term, structure_coeff in self.product(left_term, right_term).items():
                    out[result_term] += left_coeff * right_coeff * structure_coeff
        return self._clean(out)

    def commutator(self, left: str, right: str) -> Counter[str]:
        """Return ``[left,right] = left*right - right*left``."""
        forward = self.product(left, right)
        backward = self.product(right, left)
        out: defaultdict[str, float] = defaultdict(float)
        for key, value in forward.items():
            out[key] += value
        for key, value in backward.items():
            out[key] -= value
        return self._clean(out)

    def associator(self, left: str, middle: str, right: str) -> Counter[str]:
        """Return ``(left*middle)*right - left*(middle*right)``."""
        lm = self.product(left, middle)
        mr = self.product(middle, right)
        left_assoc = self.multiply_linear(lm, {right: 1})
        right_assoc = self.multiply_linear({left: 1}, mr)

        out: defaultdict[str, float] = defaultdict(float)
        for key, value in left_assoc.items():
            out[key] += value
        for key, value in right_assoc.items():
            out[key] -= value
        return self._clean(out)

    def associativity_failures(self) -> list[tuple[str, str, str, Counter[str]]]:
        """Return all basis triples with a nonzero associator.

        For a finite basis it is enough to test basis triples because
        multiplication is bilinear.
        """
        failures: list[tuple[str, str, str, Counter[str]]] = []
        ordered_basis = sorted(self.basis)
        for left, middle, right in product(ordered_basis, repeat=3):
            diff = self.associator(left, middle, right)
            if diff:
                failures.append((left, middle, right, diff))
        return failures

    def is_associative(self) -> bool:
        """Whether the multiplication table is associative on all basis triples."""
        return not self.associativity_failures()

    def compose_word(self, word: Iterable[str]) -> Counter[str]:
        """Compose a word of basis names from left to right.

        Example: ``compose_word(["generate", "test", "audit"])`` computes
        ``((generate * test) * audit)`` using bilinearity. For a non-associative
        experimental table, the parenthesization matters; this method deliberately
        uses left association.
        """
        items = list(word)
        if not items:
            return Counter({"I": 1}) if "I" in self.basis else Counter()

        current: Counter[str] = Counter({items[0]: 1})
        for item in items[1:]:
            self._require_basis(item)
            current = self.multiply_linear(current, {item: 1})
        return current

    @staticmethod
    def format_linear_combo(combo: Mapping[str, int | float]) -> str:
        """Format a finite linear combination, including negative coefficients."""
        items = [(name, coeff) for name, coeff in sorted(combo.items()) if coeff != 0]
        if not items:
            return "0"

        parts: list[str] = []
        for index, (name, coeff) in enumerate(items):
            magnitude = abs(coeff)
            term = name if magnitude == 1 else f"{magnitude:g}·{name}"
            if index == 0:
                parts.append(term if coeff > 0 else f"-{term}")
            else:
                parts.append((" + " if coeff > 0 else " - ") + term)
        return "".join(parts)

    @staticmethod
    def _clean(combo: Mapping[str, float], tolerance: float = 1e-12) -> Counter[str]:
        """Drop numerical zeros from a linear combination."""
        cleaned: Counter[str] = Counter()
        for key, value in combo.items():
            if abs(value) > tolerance:
                cleaned[key] = value
        return cleaned

    def _require_basis(self, name: str) -> None:
        if name not in self.basis:
            raise KeyError(f"Unknown basis element: {name!r}")
