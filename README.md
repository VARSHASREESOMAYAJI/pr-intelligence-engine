# PR Intelligence Engine

Lightweight Pull Request Intelligence MVP.  
Processes a PR JSON and generates:
- A concise summary  
- Estimated changed lines  
- A heuristic risk tag (LOW / MEDIUM / HIGH)  
- A short actionable insight  

This demo is fast, local, and ready for evaluation.

---

## Quick Start

**1. Install dependencies**
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
2. Start the server

bash
Copy code
python -m uvicorn app:app --host 127.0.0.1 --port 9000
3. Run a sample demo (new terminal)

powershell
Copy code
.\.venv\Scripts\Activate.ps1
Invoke-RestMethod -Uri http://127.0.0.1:9000/review -Method Post -ContentType 'application/json' -InFile '.\demo\sample_medium_change.json' | ConvertTo-Json
Interactive API Docs:
http://127.0.0.1:9000/docs

📂 Demo Suite
Inside demo/ you’ll find realistic PR scenarios:

sample_small_change.json

sample_medium_change.json

sample_large_change.json

sample_test_case.json

sample_security_fix.json

These provide multi-scenario coverage for quick evaluation.

📌 Scope of This MVP
FastAPI endpoint for PR analysis

Lightweight heuristics for summarization and risk scoring

Multi-case simulation suite

One-command local demo flow

Clean, review-friendly structure

🔮 Future Upgrade Paths
ML risk prediction (LightGBM or transformers)

GitHub webhook ingestion

PR feature store (Postgres)

SHAP-based explainability

Reviewer recommendation engine

📄 License
MIT License.

perl
Copy code

Say **“done”** when saved.
::contentReference[oaicite:0]{index=0}