# Architecture Decision Records

This directory defines the portfolio's Architecture Decision Record (ADR) baseline. Each ADR records one architecturally significant decision: the problem being solved, the decision that was made, the alternatives that were considered, and the consequences to expect.

The directory is named `decision-records` because the full name is more readable to contributors, reviewers, and auditors who may not already know the acronym.

At the portfolio root, this directory serves as the canonical baseline. The structure defined in [ADR-0001](0001-use-architecture-decision-records.md) is the shape that participating repositories should copy into their own `.github/docs/decision-records/` directory when they adopt this convention. Those repositories should reuse the structure, not this directory's prose verbatim.

ADRs may begin as `Proposed` while a decision is being discussed. Once accepted, an ADR becomes part of the repository's permanent historical record. Accepted ADRs are not substantively rewritten; later decisions supersede earlier ones through new ADRs. Post-acceptance edits are limited to status updates, supersession links, implementing-PR links, and editorial fixes that do not change the decision itself.

## What is an ADR?

An Architecture Decision Record is a short Markdown document that answers three questions about a single architectural choice:

1. **What is the problem?** What forces drove the decision?
2. **What was decided?** Concretely, what will we do?
3. **Why?** What alternatives were considered, and what trade-offs are we accepting?

A reader who knows nothing about the codebase should be able to open any ADR and understand why a particular design exists. A reviewer evaluating the repository should be able to reconstruct the project's architectural reasoning without a synchronous conversation. An auditor in a regulated environment should be able to trace important design choices to source-controlled artifacts.

The format used here is established by [ADR-0001](0001-use-architecture-decision-records.md). It is MADR 4.0-aligned, uses a visible Markdown metadata table instead of YAML front matter, and adds fields for reversibility, traceability, and conservative compliance mapping.

## Index

| #                                                      | Title                                                          | Status   | Date       | Summary                                                                                        |
| ------------------------------------------------------ | -------------------------------------------------------------- | -------- | ---------- | ---------------------------------------------------------------------------------------------- |
| [0001](0001-use-architecture-decision-records.md)      | Use Architecture Decision Records to Document Design Rationale | Accepted | 2026-04-22 | Adopt ADRs as the documentation format for architecturally significant decisions.              |
| [0002](0002-adopt-diataxis-documentation-framework.md) | Adopt Diátaxis as the Documentation Framework                  | Accepted | 2026-04-24 | Adopt the Diátaxis four-quadrant framework for non-ADR documentation in adopting repositories. |
| [0003](0003-use-deny-all-gitignore-strategy.md)        | Use a Deny-All `.gitignore` Strategy                           | Accepted | 2026-04-25 | Adopt deny-all `.gitignore` with explicit allowlist as the default tracking strategy for adopting repositories. |

## Status Lifecycle

An ADR moves through the following statuses. Every ADR in the Index above shows its current status.

- **Proposed.** The ADR has been drafted and is under discussion. The decision has not yet been made. A `Review-by` date should be set; if the ADR is not Accepted or Rejected by that date, it should be revisited or closed.
- **Accepted.** The ADR represents an active decision. The code in the repository should reflect it. This is the working state of most ADRs.
- **Rejected.** The ADR was considered and decided against. It remains in the repository as a historical record so future readers can see that the option was evaluated.
- **Superseded by ADR-NNNN.** The decision was valid at the time but has been replaced by a later ADR. Both ADRs remain in the repository. The superseded ADR points forward to the newer one in its `Superseded by` section, and the newer ADR points back in its `Supersedes` section.
- **Deprecated.** The ADR describes a decision that is no longer in force but has not been explicitly replaced. This status should be rare and should usually be followed by a superseding ADR that explains what changed.

An Accepted ADR may still receive non-substantive maintenance updates, but any change that alters the decision, its scope, or its rationale requires a superseding ADR.

## How to Contribute a New ADR

1. Decide whether the change is architecturally significant. The four tests are in [ADR-0001](0001-use-architecture-decision-records.md) under `Decision Outcome`. When in doubt, err toward writing the ADR; a short record is cheaper than reconstructing the reasoning later.
2. Copy [ADR-0001](0001-use-architecture-decision-records.md) to a new file at `.github/docs/decision-records/NNNN-short-kebab-title.md`, where `NNNN` is the next unused four-digit number in this directory. Numbers are allocated monotonically and never reused.
3. Strip the template-instruction HTML comment block at the top of the copied file. Exception: if you are seeding a repository's own `ADR-0001` per step 5, keep the block so it continues to serve as that repository's template.
4. Replace the metadata values and every section body with content specific to the new decision. Keep the section headings in the order shown. For sections that genuinely do not apply, write "None." or "N/A (reason)." rather than deleting the heading. A missing heading reads as "I forgot"; an explicit "None." reads as "I considered this and there is nothing to record."
5. If you are seeding a different repository with its initial `ADR-0001`, reuse the structure but rewrite repository-specific context, consequences, and compliance notes so the record is true for that repository.
6. Update this index file. Add a row for the new ADR with its Status (usually `Proposed` or `Accepted`), Date, and a one-sentence Summary.
7. Open a pull request in the repository where the ADR lives. The new ADR and the index update belong in the same PR.

## Conventions

- **Directory.** In any repository using this convention, ADRs live in `.github/docs/decision-records/` relative to the repository root, alongside other governance files under `.github/`.
- **Directory naming.** Use `decision-records` as the directory name so the purpose is obvious even to readers who do not know the acronym.
- **Filenames.** `NNNN-short-kebab-title.md`, where `NNNN` is a four-digit zero-padded number and the title is a present-tense verb phrase in kebab case. Example: `0004-pin-github-actions-by-commit-sha.md`.
- **Numbering.** Monotonic. Gaps are allowed. Numbers are never reused, even if a proposed ADR is later abandoned.
- **Titles.** Start with a present-tense imperative verb. Prefer `Pin GitHub Actions by Commit SHA` over `GitHub Actions Pinning Policy`. The title is also the H1 of the file, prefixed with `ADR-NNNN:`.
- **Metadata fields.** The table at the top of every ADR records `Status`, `Date`, `Authors`, `Decision-maker`, `Consulted`, `Informed`, `Reversibility`, and `Review-by`. `Consulted` and `Informed` follow RACI-style conventions: people whose input was actively sought versus people who were kept in the loop. `Reversibility` is an ease-of-change estimate: `Low` means hard to reverse (deeply committed), `Medium` means reversal is possible but involves meaningful migration or rework, and `High` means easy to reverse. `Review-by` is the date by which a `Proposed` ADR should be accepted or rejected; it is typically `N/A (Accepted)` once the ADR is Accepted.
- **Editing.** Accepted ADRs are append-only for substantive meaning. Allowed post-acceptance updates are Status changes, `Supersedes` and `Superseded by` links, `Implementing PRs`, and editorial corrections that do not alter the decision.

## Further Reading

Readers unfamiliar with ADRs as a genre may find the following useful. None of these is required; they are provided for context.

- **Michael Nygard, [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions.html) (2011).** The original post that introduced the ADR concept.
- **[MADR](https://adr.github.io/madr/) (Markdown Architectural Decision Records).** The community template that this baseline aligns with.
- **Joel Parker Henderson, [`architecture-decision-record`](https://github.com/joelparkerhenderson/architecture-decision-record).** A widely referenced collection of ADR formats and examples.
- **ThoughtWorks Technology Radar, [Lightweight Architecture Decision Records](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records) (Adopt, November 2017).** Recommends keeping ADRs in source control instead of a wiki or website.
