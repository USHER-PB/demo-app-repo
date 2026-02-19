# Demo App — GitOps CD Pipeline

A demo application showing how teams deploy apps automatically using GitHub Actions + ArgoCD.

---

## 📁 Repository Structure

```
demo-app-repo/
  src/main.py                        ← Application code (Python Flask)
  Dockerfile                         ← How to build the Docker image
  k8s/deployment.yaml                ← Kubernetes manifests (deployment + service)
  .github/workflows/deploy.yaml      ← CI Pipeline: builds & pushes Docker image on every push
```

---

## ⚙️ How It Works

```
Developer pushes code to GitHub
        ↓
GitHub Actions runs automatically:
  → Builds Docker image
  → Pushes image to GHCR (ghcr.io/USERNAME/demo-app:sha-xxxxx)
        ↓
ArgoCD (managed externally by DevOps) detects the new image
        ↓
ArgoCD deploys the new version to the Kubernetes cluster
        ↓
App is live. No manual steps.
```

---

## 🔧 Setup for Developers

### Step 1 — Push this repo to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/demo-app-repo.git
git push -u origin main
```

### Step 2 — Enable GitHub Actions write permissions
Go to: **Repo → Settings → Actions → General → Workflow permissions → Read and write** ✅

### Step 3 — Replace image reference
In `k8s/deployment.yaml`, replace `REPLACE_WITH_YOUR_GITHUB_USERNAME` with your actual GitHub username.

### Step 4 — Trigger the pipeline
Push any code change to `main`:
```bash
echo "# update" >> README.md
git add . && git commit -m "trigger pipeline" && git push
```

Watch GitHub Actions build and push the image automatically.

---

## 🎯 DevOps Setup (Done Once — Not by the Developer)

The DevOps engineer connects this repo to ArgoCD via the **ArgoCD UI**:

1. **Settings → Repositories → Connect Repo**
   - Type: HTTPS
   - URL: `https://github.com/USERNAME/demo-app-repo`
   - GitHub Token: (generate from GitHub → Settings → Developer settings → PAT)

2. **Applications → New Application**
   - Repo URL: same as above
   - Path: `k8s`
   - Cluster: target spoke cluster
   - Namespace: `demo-app`
   - Sync Policy: **Automatic** ✅

ArgoCD will now watch the repo and deploy every new image automatically.

---

## 🔄 Supported Manifest Formats

This demo uses plain k8s manifests. Teams can also use:
- **Kustomize** — add a `kustomization.yaml` file, ArgoCD detects it automatically
- **Helm** — add a `Chart.yaml` file, ArgoCD detects it automatically
