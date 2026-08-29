# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-08-29

This release completes the analysis so that every calculation runs over the full
sample space described in the manuscript (25 included studies, twelve
reproducibility requirements) instead of the partial placeholder data shipped in
1.0.0.

### Added

- `literature/extraction_template.csv`: full 12-requirement coding matrix for the
  25 included studies.
- `literature/screening_notes.md`: coding note stating that the analytical fields
  are a working coding subject to author validation.
- `data/reproducibility_requirements.csv`: requirements R4–R12 (definitions and
  source examples); the file previously stopped at R3.
- `data/infraestructure_mapping.csv`: GitHub / Zenodo / ORCID / integrated support
  scores and justifications for requirements R4–R12.
- `analysis/calculate_scores.py`: RQ1 requirement-coverage analysis over the
  literature and RQ2 infrastructure-coverage analysis over the mapping table.
- `results/requirement_coverage.csv` and `results/infrastructure_coverage.csv`:
  generated outputs for RQ1 and RQ2.
- `results/reproduction_task_results.csv`: outcomes of the controlled reproduction
  task for both scenarios.
- `analysis/calculate_scores.R`: R port of the scoring script.
- `codemeta.json`: machine-readable software metadata.
- `docs/scoring_criteria.md`: rubrics for the two new criteria (Traceability,
  Discoverability).
- `tests/test_score_calculation.py`: tests for the 12-criterion matrix, the
  requirement-coverage matrix and the infrastructure mapping.

### Changed

- `data/baseline_vs_workflow_scores.csv`: scoring matrix expanded from 10 to 12
  criteria (added Traceability and Discoverability). `Dependencies specified` now
  scores 1 (not 2) for the integrated workflow, because neither scenario
  guarantees a complete executable environment.
- `literature/included_studies.csv`: expanded from 4 to 25 studies using the full
  24-column extraction schema; bibliographic fields taken from the reference
  export in `state of the art/`.
- Reproducibility scores updated to run over 24 points:
  - Conventional workflow: 30.0 % (6/20) -> **29.2 % (7/24)**.
  - Integrated workflow: 100.0 % (20/20) -> **95.8 % (23/24)**.
- `manuscript/paper.docx`: abstract, Section 2.6, Section 3 results paragraph,
  Section 4 discussion and Table 1 updated to the 12-criterion scoring and the new
  percentages. Backup kept as `manuscript/paper.docx.bak`.
- `docs/scoring_criteria.md`: maximum score 20 -> 24; "Ten criteria" -> "Twelve
  criteria"; evaluation results updated.
- `00_files.md`: file tree aligned with the actual repository contents.

## [1.0.0] - 2026-08-29

### Added

- Initial archived release (Zenodo DOI 10.5281/zenodo.22164247).
- Manuscript and figures under `manuscript/`.
- Literature search strategy and initial extraction data under `literature/`.
- Reproducibility requirement matrix and workflow scoring data under `data/`.
- `analysis/calculate_scores.py` with a 10-criterion reproducibility assessment
  (conventional 30.0 %, integrated 100.0 %).
- Workflow and reproduction protocols under `docs/`.
- Continuous integration check under `.github/workflows/`.

[1.1.0]: https://github.com/telmomm/github-zenodo-orcid-reproducibility-workflow/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/telmomm/github-zenodo-orcid-reproducibility-workflow/releases/tag/v1.0.0
