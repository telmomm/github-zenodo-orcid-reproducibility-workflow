import pandas as pd

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

print(results)