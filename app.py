from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn, textwrap

app = FastAPI()

class PRPayload(BaseModel):
    title: str = ""
    body: str = ""
    diff: str = ""
    comments: int = 0

def generate_summary(title, body, diff, comments):
    summary = f"{title} — {textwrap.shorten(body, width=140)}"
    additions = diff.count("+")
    deletions = diff.count("-")
    changed = additions + deletions

    if changed > 300 or comments > 10:
        risk = "HIGH"
    elif changed > 100 or comments > 3:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    insight = "High churn — consider splitting." if risk == "HIGH" else \
              "Moderate diff — add one reviewer." if risk == "MEDIUM" else \
              "Low churn — straightforward merge."

    return {
        "summary": summary,
        "risk_tag": risk,
        "changed_lines": changed,
        "comments": comments,
        "insight": insight
    }

@app.post("/review")
async def review_pr(payload: PRPayload):
    return generate_summary(payload.title, payload.body, payload.diff, payload.comments)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
