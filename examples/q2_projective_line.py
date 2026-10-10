"""A minimal finite-geometry example over F_2.

The projective line P^1(F_2) consists of the one-dimensional subspaces of F_2^2.
There are q+1 = 3 of them.  The example makes the parameter q concrete: it is
literally counting finite-field choices.
"""

from itertools import product


def span(v: tuple[int, int]) -> frozenset[tuple[int, int]]:
    # Over F_2 the only scalars are 0 and 1.
    return frozenset({(0, 0), v})


vectors = [v for v in product((0, 1), repeat=2) if v != (0, 0)]
lines = sorted({span(v) for v in vectors}, key=lambda line: sorted(line))

print("Nonzero vectors in F_2^2:", vectors)
print("One-dimensional subspaces (points of P^1(F_2)):")
for i, line in enumerate(lines, start=1):
    print(f"  L{i} = {sorted(line)}")

q = 2
print(f"\nCount = {len(lines)} = q + 1 = {q + 1}")

# Every pair of distinct projective points is in the nontrivial relative position.
# The adjacency graph is therefore K3, giving the same rank-one Hecke relation.
for i, line in enumerate(lines):
    others = [j + 1 for j in range(len(lines)) if j != i]
    print(f"L{i + 1} has {len(others)} distinct neighbors: {others}")
