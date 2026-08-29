# Reproducibility scoring -- R port of calculate_scores.py
# Run from the analysis/ directory:  Rscript calculate_scores.R

cat("Working directory:", getwd(), "\n")
cat("Files here:", paste(list.files(), collapse = ", "), "\n")

# ---------------------------------------------------------------------------
# RQ3 -- Comparative reproducibility assessment (conventional vs integrated)
# ---------------------------------------------------------------------------
df <- read.csv("../data/baseline_vs_workflow_scores.csv", stringsAsFactors = FALSE)

baseline   <- sum(df$baseline_score)
integrated <- sum(df$integrated_score)
maximum    <- sum(df$max_score)

results <- data.frame(
  scenario = c("Conventional workflow", "Integrated workflow"),
  score = c(baseline, integrated),
  maximum = c(maximum, maximum),
  reproducibility_score = c(baseline / maximum, integrated / maximum),
  stringsAsFactors = FALSE
)

write.csv(results, "../results/reproducibility_scores.csv", row.names = FALSE)

# ---------------------------------------------------------------------------
# RQ1 -- Frequency of each reproducibility requirement across the literature
# ---------------------------------------------------------------------------
extraction <- read.csv("../literature/extraction_template.csv", stringsAsFactors = FALSE)
requirement_cols <- setdiff(names(extraction), c("paper_id", "notes"))
n_total <- nrow(extraction)

coverage <- data.frame(
  requirement = requirement_cols,
  n_studies = as.integer(colSums(extraction[requirement_cols])),
  n_total = n_total,
  stringsAsFactors = FALSE
)
coverage$pct_studies <- coverage$n_studies / n_total
coverage <- coverage[order(-coverage$n_studies), ]
rownames(coverage) <- NULL

write.csv(coverage, "../results/requirement_coverage.csv", row.names = FALSE)

# ---------------------------------------------------------------------------
# RQ2 -- How far GitHub, Zenodo and ORCID cover the requirement framework
# ---------------------------------------------------------------------------
mapping <- read.csv("../data/infraestructure_mapping.csv", stringsAsFactors = FALSE)
max_infra <- nrow(mapping) * 2

infrastructure <- data.frame(
  infrastructure = c("GitHub", "Zenodo", "ORCID", "Integrated"),
  total_score = c(
    sum(mapping$github_score),
    sum(mapping$zenodo_score),
    sum(mapping$orcid_score),
    sum(mapping$integrated_score)
  ),
  max_score = max_infra,
  stringsAsFactors = FALSE
)
infrastructure$coverage <- infrastructure$total_score / max_infra

write.csv(infrastructure, "../results/infrastructure_coverage.csv", row.names = FALSE)

cat("\n"); print(results, row.names = FALSE)
cat("\n"); print(coverage, row.names = FALSE)
cat("\n"); print(infrastructure, row.names = FALSE)
