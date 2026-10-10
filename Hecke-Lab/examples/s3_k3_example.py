"""Classical worked example: S3/H and the triangle K3.

Let G=S3 and H=< (12) >.  There are two double cosets: H itself and the
remaining four elements.  The nontrivial Hecke operator T acts on G/H, a
three-point set, as adjacency in K3.
"""

from hecke_lab.finite_operator import FiniteOperator
from hecke_lab.toy_systems import s3_stabilizer_algebra


states = ("1", "2", "3")
T = FiniteOperator.from_edges(
    "T",
    states,
    [(src, dst) for src in states for dst in states if src != dst],
)

T2 = T @ T
expected = FiniteOperator(
    name="T + 2I",
    states=states,
    transitions={
        (src, dst): (2.0 if src == dst else 1.0)
        for src in states
        for dst in states
    },
)

print("K3 adjacency operator T")
print(T.pretty())
print("\nTwo-step composition T @ T")
print(T2.pretty())
print("\nIdentity checked: T^2 = T + 2I ->", T2.is_same_as(expected))

alg = s3_stabilizer_algebra()
print("Symbolically: T*T =", alg.format_linear_combo(alg.product("T", "T")))
print("Associative?", alg.is_associative())
