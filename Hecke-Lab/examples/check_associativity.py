"""Check whether a symbolic multiplication table is actually associative."""

from hecke_lab.toy_systems import s3_stabilizer_algebra, tiny_symbolic_ai_algebra


classical = s3_stabilizer_algebra()
print("S3/H algebra associative?", classical.is_associative())

experimental = tiny_symbolic_ai_algebra()
failures = experimental.associativity_failures()
print("Toy AI table associative?", not failures)
print(f"Associativity failures: {len(failures)}")
for left, middle, right, diff in failures[:8]:
    print(
        f"  ({left}*{middle})*{right} - {left}*({middle}*{right}) = "
        f"{experimental.format_linear_combo(diff)}"
    )
if len(failures) > 8:
    print(f"  ... and {len(failures) - 8} more")
