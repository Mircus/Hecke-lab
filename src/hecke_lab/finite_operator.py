"""Finite relational operators.

This module gives a tiny executable model of the core Hecke-Lab intuition:

- states are finite objects;
- an operator is a weighted relation between states;
- operator composition is path counting;
- non-commutativity is visible by direct comparison.

The convention is the usual linear-algebra convention:

    A @ B

means "first apply B, then apply A".
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Iterable, Mapping

State = str
Transition = tuple[State, State]


@dataclass(frozen=True)
class FiniteOperator:
    """A finite weighted relation on a finite state set.

    Parameters
    ----------
    name:
        Human-readable operator name, e.g. "summarize".
    states:
        Finite universe on which the operator acts.
    transitions:
        Mapping from ``(source, target)`` to multiplicity/weight.

    Notes
    -----
    A Hecke operator can be viewed as an averaging/counting operator over a
    structured relation. This class is intentionally minimal: it stores only
    finite relations and composes them by counting length-two paths.
    """

    name: str
    states: tuple[State, ...]
    transitions: Mapping[Transition, float]

    @classmethod
    def from_edges(
        cls,
        name: str,
        states: Iterable[State],
        edges: Iterable[Transition],
    ) -> "FiniteOperator":
        """Create an operator from unweighted edges."""
        counts: Counter[Transition] = Counter(edges)
        return cls(name=name, states=tuple(states), transitions=dict(counts))

    @classmethod
    def identity(cls, states: Iterable[State], name: str = "I") -> "FiniteOperator":
        """Identity operator on the given finite state set."""
        state_tuple = tuple(states)
        return cls(name=name, states=state_tuple, transitions={(s, s): 1.0 for s in state_tuple})

    def apply(self, distribution: Mapping[State, float]) -> dict[State, float]:
        """Apply the operator to a finite distribution over states."""
        out: defaultdict[State, float] = defaultdict(float)
        for (src, dst), weight in self.transitions.items():
            if src in distribution:
                out[dst] += distribution[src] * weight
        return dict(out)

    def __matmul__(self, other: "FiniteOperator") -> "FiniteOperator":
        """Compose operators: ``self @ other`` means self after other."""
        if set(self.states) != set(other.states):
            raise ValueError("Cannot compose operators on different state universes.")

        composed: defaultdict[Transition, float] = defaultdict(float)
        for (src, mid), w1 in other.transitions.items():
            for (mid2, dst), w2 in self.transitions.items():
                if mid == mid2:
                    composed[(src, dst)] += w1 * w2

        return FiniteOperator(
            name=f"{self.name}∘{other.name}",
            states=self.states,
            transitions=dict(composed),
        )

    def support(self) -> frozenset[Transition]:
        """Return the unweighted support of the operator."""
        return frozenset(edge for edge, weight in self.transitions.items() if weight != 0)

    def total_weight(self) -> float:
        """Total transition weight."""
        return sum(self.transitions.values())

    def is_same_as(self, other: "FiniteOperator") -> bool:
        """Exact comparison of state universe and weighted transitions."""
        return set(self.states) == set(other.states) and dict(self.transitions) == dict(other.transitions)

    def pretty(self) -> str:
        """Human-readable transition list."""
        if not self.transitions:
            return f"{self.name}: <empty>"
        rows = [f"{src} --{self.name}:{weight:g}--> {dst}" for (src, dst), weight in sorted(self.transitions.items())]
        return "\n".join(rows)
