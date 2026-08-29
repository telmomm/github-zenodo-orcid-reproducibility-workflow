# Reproducibility Scoring Criteria

## Purpose

This document defines the scoring system used to evaluate reproducibility support.

Maximum score: 24 points.

Twelve criteria are evaluated.

Each criterion is scored:

- 0 = not available
- 1 = partially available
- 2 = fully available

---

# Criterion 1. Code Availability

0:
No source code available.

1:
Partial code available.

2:
Complete source code publicly accessible.

---

# Criterion 2. Version Identification

0:
Version cannot be identified.

1:
Version mentioned but not formally managed.

2:
Version explicitly identified through Git tags or releases.

---

# Criterion 3. Persistent Identifier

0:
No persistent identifier.

1:
Temporary or unstable link.

2:
DOI assigned.

---

# Criterion 4. Documentation

0:
No documentation.

1:
Limited documentation.

2:
Comprehensive documentation available.

---

# Criterion 5. Dependency Specification

0:
Dependencies not documented.

1:
Dependencies partially documented.

2:
Complete dependency specification available.

---

# Criterion 6. Researcher Identification

0:
Researcher identity unclear.

1:
Researcher name available.

2:
Persistent ORCID identifier available.

---

# Criterion 7. Release Identification

0:
No release mechanism.

1:
Version indicated informally.

2:
Formal release available.

---

# Criterion 8. Citation Mechanism

0:
No citation guidance.

1:
Citation suggested informally.

2:
Structured citation metadata available (DOI, CITATION.cff).

---

# Criterion 9. Long-Term Archive

0:
No archival preservation.

1:
Repository only.

2:
Permanent archive available through Zenodo.

---

# Criterion 10. Reproduction Instructions

0:
No instructions.

1:
Partial instructions.

2:
Complete step-by-step instructions.

---

# Criterion 11. Traceability

0:
Outputs cannot be linked to a specific version or contributor.

1:
Partial link between outputs and version or contributor.

2:
Outputs linked to the exact version and to accountable contributors.

---

# Criterion 12. Discoverability

0:
Artifacts cannot be found through indexing or identifiers.

1:
Artifacts findable only through a single non-indexed location.

2:
Artifacts indexed and resolvable through persistent identifiers.

---

# Reproducibility Score

The reproducibility score is calculated as:

RS = Total Score / Maximum Score

where:

- Total Score = sum of obtained criterion scores
- Maximum Score = 24

---

# Evaluation Results

## Conventional Workflow

Total score: 7

Maximum score: 24

Reproducibility score:

RS = 7 / 24 = 0.292

29.2%

---

## Integrated GitHub–Zenodo–ORCID Workflow

Total score: 23

Maximum score: 24

Reproducibility score:

RS = 23 / 24 = 0.958

95.8%

Note: dependency specification scores 1 (not 2) for the integrated workflow,
because neither scenario guarantees a complete executable environment. This is
the single criterion the integrated workflow does not fully satisfy.