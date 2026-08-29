# Workflow Protocol

## Purpose

This document describes the integrated GitHub–Zenodo–ORCID workflow evaluated in the study.

The objective of the workflow is to improve reproducibility, traceability, transparency, discoverability and long-term preservation of computational research outputs.

---

# Workflow Overview

The workflow consists of three complementary infrastructure layers:

1. GitHub
   - Version control
   - Collaborative development
   - Documentation
   - Release management

2. Zenodo
   - Archival preservation
   - DOI assignment
   - Citation support
   - Long-term accessibility

3. ORCID
   - Persistent researcher identification
   - Attribution
   - Research output linkage

---

# Workflow Steps

## Step 1. Project Creation

Create a GitHub repository containing:

- README.md
- LICENSE
- CITATION.cff
- Source code
- Documentation
- Data
- Results
- Reproduction instructions

Expected output:

- Public version-controlled repository.

---

## Step 2. Repository Documentation

Document:

- Project purpose
- Input data
- Software requirements
- Dependencies
- Execution instructions

Expected output:

- Complete README.md

---

## Step 3. Version Control

Record development activities using Git commits.

Requirements:

- Meaningful commit messages
- Traceable modifications
- Tagged release versions

Expected output:

- Traceable repository history

---

## Step 4. Release Creation

Create a formal GitHub release.

Example:

v1.0.0

Expected output:

- Stable version identifier

---

## Step 5. Zenodo Archiving

Connect GitHub and Zenodo.

Archive the release.

Expected output:

- Archived record
- DOI assignment
- Permanent citation

---

## Step 6. ORCID Attribution

Associate:

- Repository
- DOI
- Publication

with the researcher ORCID profile.

Expected output:

- Persistent author identification

---

## Step 7. Publication

Include in the manuscript:

- GitHub repository URL
- Zenodo DOI
- ORCID identifier

Expected output:

- Traceable linkage between article and research artefacts

---

# Reproduction Procedure

An independent researcher should:

1. Locate the paper.
2. Access GitHub.
3. Identify the correct release.
4. Access the Zenodo archive.
5. Download materials.
6. Install dependencies.
7. Follow reproduction instructions.
8. Generate outputs.
9. Compare outputs with expected results.

---

# Success Criteria

The workflow is considered reproducible when:

- The correct version is identifiable.
- Required materials are accessible.
- Dependencies are documented.
- Instructions are available.
- Outputs can be regenerated.