# Design Note: What Hecke-Lab Is Trying to Capture

The core intuition is not “AI should use textbook Hecke algebras tomorrow.” The core intuition is narrower and more operational:

1. AI systems manipulate structured objects: documents, proofs, plans, states, code, datasets.
2. The important thing is often not only similarity between objects, but admissible transformations between them.
3. These transformations compose.
4. Their composition is generally non-commutative.
5. Some compositions preserve invariants; others destroy information, increase risk, or produce certification.

This is Hecke-like because a Hecke algebra replaces exact symmetries by coarse classes of moves/correspondences and studies their multiplication by composition/counting.

## Immediate invariant

Hecke-Lab should preserve this invariant:

> Do not collapse the project into another embedding demo. Every example must expose operators and their composition.

## Minimal executable gate

```bash
pytest
```

The tests must include at least one demonstration that two workflows with the same primitive moves in different order produce different operators.
