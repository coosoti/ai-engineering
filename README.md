# 🚀 From SWE to AI Engineer: A 25-Week Mastery Roadmap

Welcome to my journey from Software Engineer to AI Engineer. This repository documents a 25-week, project-based curriculum focused on the modern AI stack: **Large Language Models (LLMs), MLOps, and Site Reliability Engineering (SRE).**

Rather than focusing purely on training models from scratch (Data Science), this portfolio demonstrates how to integrate, deploy, scale, and monitor AI in production environments.



## 🎯 Objective
To bridge the gap between traditional software engineering and artificial intelligence by treating ML models as production-grade software components. 

By the end of this roadmap, I will have built:
* Containerized NLP APIs
* End-to-End RAG (Retrieval-Augmented Generation) Systems
* Kubernetes-based Auto-Scaling Inference Servers
* Complete SRE Observability & Incident Response Pipelines

## 🛠️ Tech Stack
* **AI & NLP:** Hugging Face, LangChain, vLLM, OpenAI API
* **Backend:** Python, FastAPI, Pydantic
* **Infrastructure & CI/CD:** Docker, Terraform, AWS, GitHub Actions, ArgoCD
* **Orchestration:** Kubernetes (K8s), KEDA, Helm
* **SRE & Observability:** Prometheus, Grafana, Alertmanager, Chaos Mesh

---

## 🗺️ The 25-Week Curriculum

### Phase 1: AI Software Engineering (APIs & Telemetry)
*Focus: Building software wrappers around foundational models and containerizing them.*
* [ ] **Week 1:** [Text Summarization API](./week-01-summarization-api) - FastAPI & Hugging Face pipeline.
* [ ] **Week 2:** [Containerize the NLP API](./week-02-docker-api) - Multi-stage Dockerfiles for heavy ML weights.
* [ ] **Week 3:** [Automated LLM Testing](./week-03-api-testing) - PyTest and edge-case validation for NLP.
* [ ] **Week 4:** [Token & Latency Logging](./week-04-telemetry) - Prometheus metrics and structured logging.

### Phase 2: AI Infrastructure & CI/CD
*Focus: Automating deployments and managing GPU compute costs.*
* [ ] **Week 5:** [GPU Cloud Provisioning](./week-05-terraform-gpu) - Terraform IaC for AWS EC2 instances.
* [ ] **Week 6:** [AI Docker CI/CD Pipeline](./week-06-github-actions) - GitHub Actions to build and push heavy ML images.
* [ ] **Week 7:** [Serverless Embeddings](./week-07-serverless) - AWS Lambda functions for event-driven AI tasks.
* [ ] **Week 8:** [GPU FinOps & Alerting](./week-08-finops) - Boto3 scripts for cloud cost monitoring.

### Phase 3: Advanced NLP, LLMs & RAG
*Focus: Mastering context retrieval, vector search, and LLM evaluation.*
* [ ] **Week 9:** [End-to-End RAG System](./week-09-rag-chatbot) - LangChain and ChromaDB/Pinecone.
* [ ] **Week 10:** [LLM Observability](./week-10-llm-tracing) - Prompt tracing with LangSmith or Phoenix.
* [ ] **Week 11:** [RAG Evaluation Pipeline](./week-11-rag-eval) - Automated scoring for hallucinations and relevance.
* [ ] **Week 12:** [LLM Fine-Tuning (PEFT)](./week-12-fine-tuning) - LoRA fine-tuning on custom datasets.

### Phase 4: MLOps, Scaling & Kubernetes
*Focus: Orchestrating massive models for enterprise traffic.*
* [ ] **Week 13:** [AI on Kubernetes](./week-13-k8s-deploy) - K8s Deployments and Services for AI.
* [ ] **Week 14:** [Queue-Based Auto-Scaling](./week-14-keda-scaling) - KEDA for event-driven LLM scaling.
* [ ] **Week 15:** [High-Throughput Serving](./week-15-vllm-serving) - Deploying with vLLM for continuous batching.
* [ ] **Week 16:** [GitOps for AI Infra](./week-16-argocd) - Declarative cluster management using ArgoCD.

### Phase 5: Agents, Telemetry & Resilience
*Focus: Autonomous systems and SRE Golden Signals.*
* [ ] **Week 17:** [Multi-Agent System](./week-17-ai-agents) - LangGraph for collaborative AI workflows.
* [ ] **Week 18:** [LLM 'Golden Signals'](./week-18-grafana-dashboards) - PromQL dashboards for Time To First Token (TTFT).
* [ ] **Week 19:** [Canary Deployments](./week-19-istio-canary) - Istio Service Mesh for safe AI rollouts.
* [ ] **Week 20:** [Chaos Engineering](./week-20-chaos-mesh) - Resilience testing for AI architecture.

### Phase 6: Applied SRE & Reliability
*Focus: Protecting the system, automating incident response, and eliminating toil.*
* [ ] **Week 21:** [LLM SLOs & Error Budgets](./week-21-slos) - Defining mathematical reliability targets.
* [ ] **Week 22:** [Incident Routing](./week-22-alertmanager) - PagerDuty integrations for critical outages.
* [ ] **Week 23:** [LLM Gateway & Load Shedding](./week-23-api-gateway) - Rate limiting and OpenAI API fallbacks.
* [ ] **Week 24:** [GPU OOM Postmortems](./week-24-runbooks) - Root Cause Analysis and Markdown Runbooks.
* [ ] **Week 25:** [AI-Powered ChatOps](./week-25-slack-bot) - Slack bots for secure infrastructure execution.

---

## 📂 Repository Structure
Each week has its own dedicated directory containing the source code, infrastructure files, and a specific `README.md` detailing the setup instructions and lessons learned.

```text
├── week-01-summarization-api/
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
├── week-02-docker-api/
│   ├── Dockerfile
│   └── ...
└── README.md
```

### Getting Started
To run any of these projects locally, ensure you have Python 3.10+ and Docker installed. Navigate to the specific week's folder and follow its internal README.md instructions.

```bash
git clone [https://github.com/yourusername/ai-engineer-roadmap.git](https://github.com/yourusername/ai-engineer-roadmap.git)
cd ai-engineer-roadmap/week-01-summarization-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
