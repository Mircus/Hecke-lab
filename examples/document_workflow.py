"""A document/RFP workflow as finite composable operators."""

from hecke_lab.toy_systems import document_operators


def main() -> None:
    ops = document_operators()

    # Convention: A @ B means first B, then A.
    risk_then_brief = ops["brief_ceo"] @ ops["extract_risks"]
    summarize_then_risk = ops["extract_risks"] @ ops["summarize"]
    repair_pipeline = ops["rewrite"] @ ops["find_gaps"] @ ops["extract_risks"]

    print("=== extract risks, then brief CEO ===")
    print(risk_then_brief.pretty())
    print()

    print("=== summarize, then extract risks ===")
    print(summarize_then_risk.pretty())
    print()

    print("=== extract risks, find gaps, rewrite ===")
    print(repair_pipeline.pretty())


if __name__ == "__main__":
    main()
