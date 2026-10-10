from hecke_lab.finite_operator import FiniteOperator
from hecke_lab.toy_systems import agent_operators


def test_identity_composition() -> None:
    states = ("a", "b")
    op = FiniteOperator.from_edges("move", states, [("a", "b")])
    identity = FiniteOperator.identity(states)

    assert (op @ identity).is_same_as(op)
    assert (identity @ op).is_same_as(op)


def test_order_matters_for_agent_moves() -> None:
    ops = agent_operators()
    generate_then_test = ops["test"] @ ops["generate"]
    test_then_generate = ops["generate"] @ ops["test"]

    assert not generate_then_test.is_same_as(test_then_generate)
    assert ("question", "tested_answer") in generate_then_test.support()
    assert ("question", "tested_answer") not in test_then_generate.support()


def test_apply_distribution() -> None:
    states = ("raw", "summary", "risk")
    summarize = FiniteOperator.from_edges("summarize", states, [("raw", "summary")])
    out = summarize.apply({"raw": 2.0})
    assert out == {"summary": 2.0}


def test_s3_k3_quadratic_relation() -> None:
    states = ("1", "2", "3")
    adjacency = FiniteOperator.from_edges(
        "T",
        states,
        [(src, dst) for src in states for dst in states if src != dst],
    )
    squared = adjacency @ adjacency
    expected = FiniteOperator(
        "T + 2I",
        states,
        {
            (src, dst): (2.0 if src == dst else 1.0)
            for src in states
            for dst in states
        },
    )
    assert squared.is_same_as(expected)
