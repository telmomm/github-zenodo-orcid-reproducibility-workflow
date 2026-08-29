reproducible-open-science-workflow/
│
├── README.md
├── LICENSE
├── CITATION.cff
├── codemeta.json
├── .zenodo.json
├── CONTRIBUTING.md
├── CHANGELOG.md
│
├── manuscript/
│   ├── paper.docx
│   └── figures/
│       ├── figure1_study_design.png
│       ├── figure2_requirement_framework.png
│       └── figure3_integrated_workflow.png
│
├── literature/
│   ├── search_strategy.md
│   ├── included_studies.csv
│   ├── extraction_template.csv
│   └── screening_notes.md
│
├── data/
│   ├── reproducibility_requirements.csv
│   ├── infrastructure_mapping.csv
│   └── baseline_vs_workflow_scores.csv
│
├── analysis/
│   ├── calculate_scores.R
│   └── calculate_scores.py
│
├── results/
│   ├── reproducibility_scores.csv
│   ├── requirement_coverage.csv
│   └── reproduction_task_results.csv
│
├── docs/
│   ├── workflow_protocol.md
│   ├── reproduction_protocol.md
│   └── scoring_criteria.md
│
├── tests/
│   └── test_score_calculation.py
│
└── .github/
    └── workflows/
        └── reproducibility-check.yml
``