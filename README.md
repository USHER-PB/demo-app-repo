# Demo App — Professional GitOps CI Repo

This is the **Application Source Code** repository. It handles the **CI (Continuous Integration)** part of the professional Two-Repo GitOps workflow.

---

## 📁 Repository Structure

```
demo-app-repo/
  src/main.py                        ← Application code (Python Flask)
  Dockerfile                         ← How to build the Docker image
  .github/workflows/deploy.yaml      ← CI Pipeline: builds/pushes image & updates GitOps repo
```

> [!NOTE]
> There are **NO Kubernetes manifests** in this repo. In a professional setup, manifests live in a dedicated **GitOps Repo** for security and clean separation of concerns.

---

## ⚙️ How It Works (The Professional Flow)

1.  **Code Push:** Developer pushes a change to this repository.
2.  **CI Run:** GitHub Actions builds a new Docker image with a unique SHA tag.
3.  **Image Push:** The image is pushed to **GitHub Container Registry (GHCR)**.
4.  **GitOps Trigger:** The pipeline then clones the **`demo-gitops-repo`**, updates its `deployment.yaml` with the new image tag, and pushes the change.
5.  **ArgoCD Sync:** ArgoCD (watching the GitOps repo) detects the change and automatically deploys the new version to the cluster.

---

## 🔧 Setup for Developers

### Step 1 — Push this repo to GitHub
```bash
cd /home/usherking/projects/demo-app-repo
git init
git add .
git commit -m "feat: initial app code and professional CI pipeline"
git remote add origin https://github.com/USHER-PB/demo-app-repo.git
git push -u origin main
```

### Step 2 — Configure Cross-Repo Access (CRITICAL)
For this repo to update the **GitOps Repo**, it needs a Personal Access Token (PAT):
1.  **Generate a PAT:** Go to GitHub Settings → Developer settings → PAT (classic) → Generate token with **`repo`** scope.
2.  **Add Secret:** Go to THIS repo's **Settings → Secrets and variables → Actions**.
3.  **Create Secret:** Name it **`GITOPS_REPO_PAT`** and paste your token.

---

## 🎯 Implementation Notes
- **Language:** Python 3.9 (Flask)
- **Container Registry:** GHCR (ghcr.io)
- **Deployment Strategy:** GitOps (Application/Infrastructure parity)
