# Hecke Algebras for AI: From Similarity to Structured Moves

Most AI systems today are described in the language of representation. We take an object — a text, an image, a theorem, a code file, a customer ticket — and map it into some latent space. Once the object has a vector representation, we can compare it with other objects, retrieve nearest neighbors, cluster it, classify it, or feed it into another model.

This is powerful. But it is also incomplete.

Similarity answers one question:

> What is close to this object?

But many intelligent systems need to answer a different question:

> What can be done from here, and how do the possible moves compose?

That second question is where Hecke algebras become interesting — not as a fashionable buzzword, but as a useful mathematical metaphor and maybe eventually as a real design principle.

## The basic intuition

A group algebra remembers exact symmetries. A Hecke algebra appears when we blur exact symmetries into structured packets of transformations, then study how these packets compose.

In the classical picture, we have a group `G` and a subgroup `H`. Instead of tracking every individual element of `G`, we track double cosets:

```text
H g H
```

A double coset is a coarse move: a whole packet of transformations considered equivalent up to an allowed ambiguity. Multiplying two such packets does not usually produce a single packet. It produces a combination of packets, with coefficients that count how many ways the composition can happen.

The slogan is:

> Groups describe exact motion. Hecke algebras describe averaged motion through structured space.

For AI, the key word is **motion**.

AI does not only store objects. It transforms them. It summarizes, critiques, translates, verifies, formalizes, searches, compresses, retrieves, executes, refutes, and revises. These are not just labels. They are operators. They have domains, codomains, costs, risks, and order effects.

The order matters:

```text
summarize → critique ≠ critique → summarize
search → compress ≠ compress → search
generate → test ≠ test → generate
formalize → verify ≠ verify → formalize
```

A Hecke-like view says: do not only embed the objects. Build an algebra of admissible moves.

## Example 1: document intelligence

Consider a tender, an RFP, a legal contract, or a technical proposal. The usual embedding-based approach asks:

> Which documents are similar to this one?

That is useful for retrieval. But a serious document AI system must do more. It needs moves such as:

- summarize;
- extract requirements;
- classify obligations;
- identify risks;
- compare against a proposal;
- find gaps;
- rewrite the proposal;
- produce a CEO memo;
- generate an audit trail.

These moves compose. But not all compositions are equal.

For instance:

```text
summarize → extract risks
```

may miss details that were compressed away during summarization. By contrast:

```text
extract risks → summarize
```

can preserve risk-relevant details and then compress them for a human reader.

The two workflows use similar components, but their composition has different meaning. This is precisely the kind of thing an operator calculus can expose.

The Hecke-like question is:

> What are the admissible document moves, and what happens when we compose them?

A mature system would not only retrieve similar RFPs. It would know that `extract_risks` followed by `brief_ceo` is a different operator from `brief_ceo` followed by `extract_risks`.

## Example 2: theorem proving and counterexample search

Mathematical AI is often discussed in terms of proof generation. But proof generation is only one move among many.

A mathematical assistant may need to:

- translate an informal claim into a formal statement;
- search for known lemmas;
- generate a proof sketch;
- normalize definitions;
- attempt a Lean proof;
- construct a finite model;
- search for a counterexample;
- weaken or strengthen a hypothesis;
- explain why a proof attempt failed.

Again, the order matters.

```text
formalize → verify
```

is a certification path.

```text
formalize → search_counterexample
```

is a falsification path.

Both may start from the same informal claim. Both are legitimate. But they are different operators on the mathematical state.

This is especially important because much of mathematics is not merely proving. Mathematicians also test definitions, build examples, probe consistency, search for obstructions, and look for countermodels.

A Hecke-like workflow algebra for mathematical AI would treat proof generation, proof checking, model construction, and counterexample search as composable operators. The question becomes:

> Which operator path is appropriate for this claim, at this level of confidence, under these constraints?

That is very different from simply asking which theorem in the database is nearest in embedding space.

## Example 3: agentic AI

Agentic AI systems are often described as chains or graphs of tools. But many such systems still lack a strong algebra of actions.

A serious agent may have actions such as:

- search;
- read;
- compress;
- challenge;
- generate;
- test;
- execute;
- audit;
- produce an action item.

The Hecke-like point is that these actions should not be viewed as arbitrary nodes in a flowchart. They are transformations of information states.

For example:

```text
search → compress → generate → test → audit
```

is a very different workflow from:

```text
generate → search → patch → audit
```

The first begins from evidence and moves toward output. The second begins from a draft and uses search as repair. Both may be useful, but they have different risks and invariants.

An operator calculus could help an agent reason about its own workflow:

- Which moves are valid from the current state?
- Which moves commute, and which do not?
- Which compositions increase confidence?
- Which compositions destroy information?
- Which compositions produce externally checkable artifacts?

This gives a sharper version of “agent planning.” It is not just selecting the next tool. It is composing operators under constraints.

## Example 4: retrieval-augmented generation

RAG systems are usually built around retrieval plus generation. But a Hecke-like perspective suggests richer primitives.

A RAG pipeline might include:

```text
retrieve
rerank
compress
cite
challenge
generate
verify
```

Many current failures come from bad composition. A model may generate before retrieval, compress before retaining crucial evidence, cite after losing source alignment, or verify using the same weak context that caused the error.

The Hecke-like design principle would be:

> Treat pipeline steps as typed operators with explicit composition rules, not as loose prompt templates.

For example, `compress` should carry an invariant: it must preserve citation anchors or risk labels. `generate` should consume a context object with provenance. `verify` should operate on both the draft and the evidence graph, not just on the draft alone.

The result is a more algebraic view of AI pipelines: not merely a chain of prompts, but a calculus of admissible transformations.

## What would the algebra contain?

A practical Hecke-like AI algebra would need several layers.

First, it needs objects:

- documents;
- summaries;
- formal statements;
- proof sketches;
- search results;
- agent states;
- verified artifacts;
- counterexamples;
- action items.

Second, it needs operators:

- summarize;
- critique;
- formalize;
- verify;
- generate;
- test;
- search;
- compress;
- audit.

Third, it needs composition rules:

```text
T_a T_b = Σ_c N_ab^c T_c
```

In classical Hecke theory, the coefficients count geometric choices. In AI, the coefficients could initially be hand-designed and later learned from traces. They might represent frequency, confidence, cost, risk, or branching probability.

Fourth, it needs invariants:

- provenance preserved;
- claims verified;
- risks exposed;
- assumptions tracked;
- executable artifact produced;
- information loss bounded;
- contradiction found or excluded within a finite scope.

This is where the idea becomes operational.

## Why not just category theory?

One could say: this is just category theory. Objects, morphisms, composition.

That is partly true. Category theory gives the broad grammar. But Hecke algebras add a specific flavor: coarse-grained correspondences, averaging, multiplicities, and operator action on spaces of states or functions.

The Hecke intuition is not merely “there are arrows.” It is:

> There are classes of moves, and composing classes produces linear combinations of classes.

That is important for AI because many transformations are not deterministic. A move like `critique` or `search_counterexample` may branch into several possible outcomes. A move like `summarize` may compress many inputs into one coarse output. A move like `verify` may certify, fail, or expose a missing lemma.

So the Hecke-like layer is a bridge between categorical composition and linear/operator methods.

## A modest first implementation

The first version of Hecke-Lab is intentionally small.

It models a finite set of states and finite relational operators between them. Composition is path counting. This is enough to demonstrate the first invariant:

> Different compositions of the same primitive AI moves can produce different operators.

For example:

```text
generate → test
```

may take a question to a tested answer.

But:

```text
test → generate
```

may be invalid or produce a different state entirely.

This is trivial in one sense, but important in another: it makes explicit what many AI workflows currently hide inside prompt chains.

The goal is not to worship a metaphor. The goal is to create executable toys that force the distinction between objects, moves, compositions, and invariants.

## Where this could go

Several directions are natural.

1. **Weighted operators**: attach cost, confidence, or risk to transitions.
2. **Typed operators**: prevent invalid compositions by domain and codomain constraints.
3. **Learned structure constants**: estimate composition outcomes from real workflow traces.
4. **Operator-valued memory**: store not only facts, but successful transformation paths.
5. **Verification-aware agents**: distinguish generative moves from certifying moves.
6. **Mathematical discovery systems**: combine proof search and counterexample search in a single operator calculus.
7. **RAG with invariants**: require citation preservation, assumption tracking, and evidence coverage across transformations.

The larger hypothesis is simple:

> AI needs a mathematics of action, not only a mathematics of representation.

Embeddings tell us what is close. Operators tell us what can be done. Algebras tell us how actions compose.

That is why Hecke algebras, even as an analogy, are worth taking seriously.

## Closing slogan

The current AI stack is very good at asking:

> What is similar to this?

The next stack may need to ask:

> What are the admissible moves from here, how do they compose, and what survives the composition?

That is a Hecke-like question.

And it may be one of the missing mathematical languages for serious agentic AI.
