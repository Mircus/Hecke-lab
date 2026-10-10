"""A theorem/proof workflow as finite composable operators."""

from hecke_lab.toy_systems import theorem_operators


def main() -> None:
    ops = theorem_operators()

    proof_path = ops["verify"] @ ops["try_lean"] @ ops["formalize"]
    refutation_path = ops["refute"] @ ops["search_counterexample"] @ ops["formalize"]

    print("=== formalize, try Lean, verify ===")
    print(proof_path.pretty())
    print()

    print("=== formalize, search counterexample, refute ===")
    print(refutation_path.pretty())
    print()

    print("These are two different operator paths from an informal claim:")
    print("- one attempts certification")
    print("- one attempts falsification")


if __name__ == "__main__":
    main()
