from collections import Counter

from hecke_lab.symbolic_algebra import SymbolicHeckeAlgebra
from hecke_lab.toy_systems import tiny_symbolic_ai_algebra


def test_symbolic_product() -> None:
    alg = SymbolicHeckeAlgebra.with_identity(["A", "B"])
    alg.set_product("A", "B", {"A": 2, "B": 1})
    assert alg.product("A", "B") == Counter({"A": 2, "B": 1})


def test_symbolic_noncommutativity() -> None:
    alg = tiny_symbolic_ai_algebra()
    forward = alg.product("Generate", "Test")
    backward = alg.product("Test", "Generate")
    assert forward != backward


def test_compose_word() -> None:
    alg = tiny_symbolic_ai_algebra()
    result = alg.compose_word(["Generate", "Test", "Action"])
    assert result == Counter({"Action": 1})


def test_format_linear_combo() -> None:
    combo = Counter({"Audit": 2, "Action": 1})
    assert SymbolicHeckeAlgebra.format_linear_combo(combo) == "Action + 2·Audit"


def test_genuine_s3_example_is_associative() -> None:
    from hecke_lab.toy_systems import s3_stabilizer_algebra

    alg = s3_stabilizer_algebra()
    assert alg.product("T", "T") == Counter({"I": 2, "T": 1})
    assert alg.is_associative()
    assert alg.associativity_failures() == []


def test_experimental_ai_table_reports_associativity_failures() -> None:
    alg = tiny_symbolic_ai_algebra()
    failures = alg.associativity_failures()
    assert failures
    assert not alg.is_associative()
