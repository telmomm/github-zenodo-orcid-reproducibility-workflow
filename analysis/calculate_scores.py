import pandas as pd
import os

print("Directorio actual:", os.getcwd())
print("Archivos aquí:", os.listdir())

# ---------------------------------------------------------------------------
# RQ3 -- Comparative reproducibility assessment (conventional vs integrated)
# ---------------------------------------------------------------------------
df = pd.read_csv("../data/baseline_vs_workflow_scores.csv")

baseline = df["baseline_score"].sum()
integrated = df["integrated_score"].sum()
maximum = df["max_score"].sum()

results = pd.DataFrame({
    "scenario": ["Conventional workflow", "Integrated workflow"],
    "score": [baseline, integrated],
    "maximum": [maximum, maximum],
    "reproducibility_score": [baseline / maximum, integrated / maximum]
})

results.to_csv("../results/reproducibility_scores.csv", index=False)

# ---------------------------------------------------------------------------
# RQ1 -- Frequency of each reproducibility requirement across the literature
# ---------------------------------------------------------------------------
extraction = pd.read_csv("../literature/extraction_template.csv")
requirement_cols = [c for c in extraction.columns if c not in ("paper_id", "notes")]
n_total = len(extraction)

coverage = pd.DataFrame({
    "requirement": requirement_cols,
    "n_studies": [int(extraction[c].sum()) for c in requirement_cols],
    "n_total": n_total,
})
coverage["pct_studies"] = coverage["n_studies"] / n_total
coverage = coverage.sort_values("n_studies", ascending=False).reset_index(drop=True)
coverage.to_csv("../results/requirement_coverage.csv", index=False)

# ---------------------------------------------------------------------------
# RQ2 -- How far GitHub, Zenodo and ORCID cover the requirement framework
# ---------------------------------------------------------------------------
mapping = pd.read_csv("../data/infraestructure_mapping.csv")
n_requirements = len(mapping)
max_infra = n_requirements * 2

infrastructure = pd.DataFrame({
    "infrastructure": ["GitHub", "Zenodo", "ORCID", "Integrated"],
    "total_score": [
        mapping["github_score"].sum(),
        mapping["zenodo_score"].sum(),
        mapping["orcid_score"].sum(),
        mapping["integrated_score"].sum(),
    ],
    "max_score": max_infra,
})
infrastructure["coverage"] = infrastructure["total_score"] / max_infra
infrastructure.to_csv("../results/infrastructure_coverage.csv", index=False)

print()
print(results)
print()
print(coverage)
print()
print(infrastructure)
