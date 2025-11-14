#!/usr/bin/env bash
python app.py & PID=$!
sleep 2
curl -X POST http://localhost:8000/review \
  -H "Content-Type: application/json" \
  --data @demo/sample_pr.json
kill $PID
