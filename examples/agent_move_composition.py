"""Show that order matters in a small agent workflow."""

from hecke_lab.toy_systems import agent_operators


def main() -> None:
    ops = agent_operators()
    generate_then_test = ops["test"] @ ops["generate"]
    test_then_generate = ops["generate"] @ ops["test"]

    print("=== generate then test ===")
    print(generate_then_test.pretty())
    print()
    print("=== test then generate ===")
    print(test_then_generate.pretty())
    print()
    print("Same operator?", generate_then_test.is_same_as(test_then_generate))


if __name__ == "__main__":
    main()
