# Hecke-Lab

**Hecke-Lab** is the executable companion to the short illustrated booklet
**_Hecke Algebras: How Symmetry Becomes Geometry, Counting, and Operators_**
by Mirco A. Mannucci and Robin Langer.

📘 **[Read the companion booklet](booklet/Hecke_Algebras_Guided_Tour.pdf)**

The booklet starts from ordinary symmetry, double cosets, relative position,
convolution, finite geometry, and Hecke operators, then asks whether the same
structural viewpoint can illuminate modern computational workflows.

Hecke-Lab keeps that last question deliberately small and testable:

> Can we represent structured moves as finite correspondences, compose them
> explicitly, and test which genuinely algebraic properties survive?

This repo does **not** claim that ordinary AI workflows literally form Hecke
algebras. It contains both orthodox finite examples and deliberately speculative
AI-flavored toys, with checks that keep the distinction visible.

## The core picture

A group algebra remembers exact motion. A Hecke algebra appears after some
symmetry has been deliberately forgotten. Exact elements are replaced by
relative-position classes or correspondences, and multiplication counts how
those coarse moves compose.

```text
exact symmetry
      ↓
quotient / tolerated ambiguity
      ↓
relative position
      ↓
correspondence
      ↓
composition by counting
      ↓
operators and spectra
```

For AI engineering, the analogy suggests moving beyond pure similarity:

```text
object -> vector -> nearest neighbors
```

asks **what is close?**

while

```text
object -> admissible moves -> composed workflows -> invariants / outcomes
```

asks **what can be done from here, and how do the moves compose?**

## What is new in 0.2

The original scaffold focused almost entirely on the speculative AI side. Version
0.2 adds a small classical spine matching the booklet:

- a complete `S3/H` worked example, realized as adjacency on the triangle `K3`;
- the genuine quadratic relation `T^2 = T + 2I`;
- a tiny `q=2` finite-geometry example using `P^1(F_2)`;
- an associativity checker for symbolic structure constants;
- an explicit demonstration that a hand-written multiplication table is **not**
  automatically an algebra;
- the companion booklet included directly in the repository.

These are intentionally small additions. Hecke-Lab remains a lab, not a general
computer-algebra package.

## Repo structure

```text
Hecke-Lab/
  README.md
  pyproject.toml
  booklet/
    Hecke_Algebras_Guided_Tour.pdf
  src/hecke_lab/
    __init__.py
    finite_operator.py
    symbolic_algebra.py
    toy_systems.py
  examples/
    s3_k3_example.py
    q2_projective_line.py
    check_associativity.py
    document_workflow.py
    theorem_workflow.py
    agent_move_composition.py
  tests/
    test_finite_operator.py
    test_symbolic_algebra.py
  articles/
    hecke_algebras_for_ai.md
  assets/
    hecke_algebras_and_ai_transformations.png
  docs/
    design_note.md
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest
```

Run the classical examples first:

```bash
python examples/s3_k3_example.py
python examples/q2_projective_line.py
python examples/check_associativity.py
```

Then the AI-flavored workflow toys:

```bash
python examples/agent_move_composition.py
python examples/document_workflow.py
python examples/theorem_workflow.py
```

## Example 1: the whole mechanism in `S3/H`

Take `G = S3` and `H = <(12)>`. There are only two double cosets: `H` and the
remaining four group elements. The coset space `G/H` has three points. The
nontrivial Hecke operator `T` is the adjacency operator of the complete graph
`K3`.

Two-step path counting gives

```text
T^2 = T + 2I.
```

There are two two-step paths from a vertex back to itself and one two-step path
to either other vertex. The group-theoretic convolution relation and the graph
identity are the same calculation.

Run:

```bash
python examples/s3_k3_example.py
```

## Example 2: where `q` comes from

For `q = 2`, the projective line `P^1(F_2)` consists of the one-dimensional
subspaces of `F_2^2`. There are

```text
q + 1 = 3
```

of them. The example is deliberately tiny because the conceptual point is the
important one: in finite-field Hecke theory, `q` is often not decorative notation;
it counts actual geometric choices.

Run:

```bash
python examples/q2_projective_line.py
```

## Example 3: is the multiplication really an algebra?

A symbolic table of structure constants

```text
T_a T_b = sum_c N_ab^c T_c
```

is not automatically associative. Version 0.2 therefore provides:

```python
alg.associator("A", "B", "C")
alg.associativity_failures()
alg.is_associative()
```

The genuine `S3/H` toy algebra passes. The older illustrative AI table does not,
which is useful information rather than a bug to hide. It tells us that the
chosen coarse move vocabulary or structure constants have not yet earned the
name "algebra."

Run:

```bash
python examples/check_associativity.py
```

## The AI experiment

The AI examples still use moves such as:

- `search`
- `compress`
- `generate`
- `test`
- `audit`
- `extract_action`

Order can matter:

```text
generate -> test != test -> generate
search -> compress != compress -> search
```

That noncommutativity is easy to model. The harder research question is stronger:

> Can we discover a quotient of real workflow states on which typed move
> composition becomes sparse, stable, predictive, and approximately algebraic?

That would require structure constants learned or counted from actual traces,
not invented by hand.

## Executable gates

The repository now has two distinct gates.

**Software gate**

```bash
pytest
```

must pass.

**Algebra gate**

Any proposed symbolic move system should be checked with
`associativity_failures()` before being described as an algebra. Approximate or
systematic failure can itself be diagnostic: perhaps the state quotient is too
coarse, hidden context matters, or the move types need refinement.

## Scope and next step

Hecke-Lab 0.2 is intentionally modest. A serious 0.3 would use real traces from
one bounded workflow to estimate empirical structure constants and then measure:

1. closure;
2. associativity error;
3. sparsity;
4. noncommutativity;
5. stability across datasets or tasks;
6. whether spectral or algebraic features predict outcomes better than the raw
   workflow graph alone.

If those tests fail, that is a result. If they succeed, the Hecke analogy becomes
substantive rather than metaphorical.

## License

MIT. See `LICENSE`.
