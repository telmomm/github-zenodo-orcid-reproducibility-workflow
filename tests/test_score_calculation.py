import pandas as pd


def test_scores():

    df = pd.read_csv("../data/baseline_vs_workflow_scores.csv")

    baseline = df["baseline_score"].sum()
    integrated = df["integrated_score"].sum()
    maximum = df["max_score"].sum()

    assert baseline == 7
    assert integrated == 23
    assert maximum == 24

    assert round(baseline / maximum, 3) == 0.292
    assert round(integrated / maximum, 3) == 0.958


def test_twelve_criteria():

    df = pd.read_csv("../data/baseline_vs_workflow_scores.csv")

    assert len(df) == 12
    assert (df["max_score"] == 2).all()


def test_requirement_coverage():

    extraction = pd.read_csv("../literature/extraction_template.csv")
    requirement_cols = [c for c in extraction.columns if c not in ("paper_id", "notes")]

    assert len(extraction) == 25
    assert len(requirement_cols) == 12
    assert extraction[requirement_cols].isin([0, 1]).all().all()


def test_infrastructure_mapping():

    mapping = pd.read_csv("../data/infraestructure_mapping.csv")

    assert len(mapping) == 12
    assert mapping["integrated_score"].sum() == 23
    for col in ("github_score", "zenodo_score", "orcid_score", "integrated_score"):
        assert mapping[col].between(0, 2).all()
