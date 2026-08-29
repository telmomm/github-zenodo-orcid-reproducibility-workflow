# Contributing to github-zenodo-orcid-reproducibility-workflow

Thank you for considering a contribution. The project is developed in the
open from its earliest stages

## Getting started

Use a virtual environment rather than installing into your system or base
conda Python -- it keeps this project's dependencies isolated and avoids the
wrong `python`/`pip` being picked up by your shell. It is never committed
(already in `.gitignore`) and can be deleted and recreated at any time.

```bash
git clone https://github.com/telmomm/github-zenodo-orcid-reproducibility-workflow.git
cd github-zenodo-orcid-reproducibility-workflow

python3 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate


```

## Before opening a pull request

1. Search existing issues to avoid duplicate work.
2. Explain the motivation, ideally by referencing or opening an issue.
3. Keep changes focused on a single concern.
4. Add or update tests 
5. Update documentation, including docstrings and relevant files under `docs/`.
6. Describe any scientific assumptions made.
7. Update `CHANGELOG.md` when the change is user-visible.

## Scientific contributions

A pull request implementing a scientific method (validation rule,
uncertainty model, propagation algorithm, etc.) should additionally
include:

- references to the method (standard, paper, or textbook);
- the mathematical definition;
- assumptions and limitations;
- a validation strategy (analytical reference, independently verified
  example, or comparison with an established implementation);
- comparison with existing implementations where possible.

Experimental or heuristic algorithms must be clearly labeled as such and
must not be presented as validated metrology methods without evidence.

## API changes

Public API changes should be discussed in an issue or discussion before
implementation. Breaking changes require explicit justification and
should be called out prominently in `CHANGELOG.md`.

## Code review

Reviewers assess correctness, tests, API clarity, documentation,
numerical stability, scientific validity, and maintainability.

## Code style

- Format and lint with `ruff`.
- Type-check with `mypy` where annotations are present.

## Reporting bugs and asking questions

Use the GitHub issue templates for bug reports, feature requests, and
scientific questions. A bug report should include a minimal reproducible
example whenever possible. Use GitHub Discussions for open-ended
architectural or scientific-direction questions.

## Attribution

Contributors receive appropriate credit. When a contribution is
substantial to the scientific software, authorship or formal
acknowledgement will be discussed transparently with the contributor.