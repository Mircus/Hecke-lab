"""Reusable toy systems for Hecke-Lab examples."""

from __future__ import annotations

from .finite_operator import FiniteOperator
from .symbolic_algebra import SymbolicHeckeAlgebra


def agent_states() -> tuple[str, ...]:
    return (
        "question",
        "search_results",
        "compressed_context",
        "draft_answer",
        "tested_answer",
        "audited_answer",
        "action_item",
    )


def agent_operators() -> dict[str, FiniteOperator]:
    """A tiny operator system for agent workflows."""
    states = agent_states()
    return {
        "search": FiniteOperator.from_edges(
            "search",
            states,
            [("question", "search_results"), ("draft_answer", "search_results")],
        ),
        "compress": FiniteOperator.from_edges(
            "compress",
            states,
            [("search_results", "compressed_context"), ("draft_answer", "compressed_context")],
        ),
        "generate": FiniteOperator.from_edges(
            "generate",
            states,
            [("question", "draft_answer"), ("compressed_context", "draft_answer")],
        ),
        "test": FiniteOperator.from_edges(
            "test",
            states,
            [("draft_answer", "tested_answer"), ("compressed_context", "tested_answer")],
        ),
        "audit": FiniteOperator.from_edges(
            "audit",
            states,
            [("tested_answer", "audited_answer"), ("draft_answer", "audited_answer")],
        ),
        "extract_action": FiniteOperator.from_edges(
            "extract_action",
            states,
            [("audited_answer", "action_item"), ("tested_answer", "action_item")],
        ),
    }


def document_states() -> tuple[str, ...]:
    return (
        "raw_rfp",
        "proposal",
        "summary",
        "risk_table",
        "gap_list",
        "ceo_memo",
        "revised_proposal",
    )


def document_operators() -> dict[str, FiniteOperator]:
    """A tiny operator system for document/RFP workflows."""
    states = document_states()
    return {
        "summarize": FiniteOperator.from_edges(
            "summarize",
            states,
            [("raw_rfp", "summary"), ("proposal", "summary"), ("revised_proposal", "summary")],
        ),
        "extract_risks": FiniteOperator.from_edges(
            "extract_risks",
            states,
            [("raw_rfp", "risk_table"), ("proposal", "risk_table"), ("summary", "risk_table")],
        ),
        "find_gaps": FiniteOperator.from_edges(
            "find_gaps",
            states,
            [("risk_table", "gap_list"), ("proposal", "gap_list")],
        ),
        "rewrite": FiniteOperator.from_edges(
            "rewrite",
            states,
            [("gap_list", "revised_proposal"), ("risk_table", "revised_proposal")],
        ),
        "brief_ceo": FiniteOperator.from_edges(
            "brief_ceo",
            states,
            [("summary", "ceo_memo"), ("risk_table", "ceo_memo"), ("gap_list", "ceo_memo")],
        ),
    }


def theorem_states() -> tuple[str, ...]:
    return (
        "informal_claim",
        "formal_statement",
        "proof_sketch",
        "lean_attempt",
        "counterexample_search",
        "verified_theorem",
        "refuted_claim",
    )


def theorem_operators() -> dict[str, FiniteOperator]:
    """A tiny operator system for theorem/proof workflows."""
    states = theorem_states()
    return {
        "formalize": FiniteOperator.from_edges(
            "formalize",
            states,
            [("informal_claim", "formal_statement"), ("proof_sketch", "formal_statement")],
        ),
        "sketch": FiniteOperator.from_edges(
            "sketch",
            states,
            [("informal_claim", "proof_sketch"), ("formal_statement", "proof_sketch")],
        ),
        "try_lean": FiniteOperator.from_edges(
            "try_lean",
            states,
            [("formal_statement", "lean_attempt"), ("proof_sketch", "lean_attempt")],
        ),
        "verify": FiniteOperator.from_edges(
            "verify",
            states,
            [("lean_attempt", "verified_theorem")],
        ),
        "search_counterexample": FiniteOperator.from_edges(
            "search_counterexample",
            states,
            [("formal_statement", "counterexample_search"), ("informal_claim", "counterexample_search")],
        ),
        "refute": FiniteOperator.from_edges(
            "refute",
            states,
            [("counterexample_search", "refuted_claim")],
        ),
    }


def tiny_symbolic_ai_algebra() -> SymbolicHeckeAlgebra:
    """A toy symbolic algebra of coarse AI move classes.

    The coefficients are illustrative, not learned. They represent a hypothesis:
    composing coarse AI actions can branch into multiple outcome-classes.
    """
    alg = SymbolicHeckeAlgebra.with_identity(
        ["Search", "Compress", "Generate", "Test", "Audit", "Action"], identity="I"
    )
    alg.set_product("Search", "Compress", {"Generate": 1, "Audit": 1})
    alg.set_product("Compress", "Search", {"Compress": 2})
    alg.set_product("Generate", "Test", {"Audit": 1, "Action": 1})
    alg.set_product("Test", "Generate", {"Generate": 1, "Audit": 2})
    alg.set_product("Audit", "Action", {"Action": 1})
    alg.set_product("Action", "Audit", {"Audit": 1})
    return alg


def s3_stabilizer_algebra() -> SymbolicHeckeAlgebra:
    """The genuine two-dimensional Hecke algebra for S3 with H=<(12)>.

    With normalized convolution, the nontrivial double-coset operator T obeys

        T^2 = T + 2 I.

    This is the algebraic form of the K3 adjacency identity A^2 = A + 2I.
    """
    alg = SymbolicHeckeAlgebra.with_identity(["T"], identity="I")
    alg.set_product("T", "T", {"T": 1, "I": 2})
    return alg
