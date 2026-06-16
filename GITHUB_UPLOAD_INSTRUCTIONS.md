# GitHub Upload Instructions

## Option A — Upload through GitHub web interface

1. Create a new GitHub repository named:

   ```text
   neutral-zone-rotational-vector-manifold
   ```

2. Keep it private at first while the concept is being cleaned up.

3. Unzip this build pack.

4. Drag the full folder contents into the GitHub upload page.

5. Commit with:

   ```text
   Initial NZ-RVM + NRL-01 research scaffold
   ```

## Option B — Upload with Git command line

```bash
git init
git add .
git commit -m "Initial NZ-RVM + NRL-01 research scaffold"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/neutral-zone-rotational-vector-manifold.git
git push -u origin main
```

## Suggested branch names

```text
main
research/numeric-register-layer
research/neutral-zone-physics
feature/register-feature-builder
feature/anomaly-detection-model
```

## Suggested GitHub repo description

```text
Neutral-Zone Rotational Vector Manifold with Numeric Register Layer: a research scaffold for translating handwritten rotational-vector diagrams into symbolic registers, matrices, and testable neutral-zone stability equations.
```

## Suggested README badges later

Add badges only after tests and releases are active:

```md
![Status](https://img.shields.io/badge/status-research%20prototype-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
```

## Safety note

Keep claims technical and testable. Use words like **prototype**, **model**, **hypothesis**, **simulation**, and **bench-scale validation**. Avoid claiming verified propulsion performance until measured data exists.