# smart-healthcare-pipeline
Fine-grained micro-model MLOps demo (Acumos + Docker + Kubernetes)
# Smart Healthcare Pipeline — Fine-Grained Micro-Model MLOps

This repository contains a demo implementation of fine-grained intra-model modularity:
- **Preprocessor → Classifier → Evaluator** as separate micro-models
- Packaged with **Docker**
- Orchestrated with **Kubernetes (Minikube for local)**
- Ready for **CI/CD** via GitHub Actions (workflows folder)

Folders:
- `src/preprocessor`, `src/classifier`, `src/evaluator`, `src/aggregator`
- `k8s` — Kubernetes manifests
- `.github/workflows` — CI/CD pipelines
