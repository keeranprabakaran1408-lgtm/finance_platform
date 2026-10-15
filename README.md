# Finance Insights Platform

A personal finance insights platform built on synthetic transaction data. Users upload bank-statement-style CSVs, a cloud pipeline cleans them into a database, a machine learning model flags likely fraud with explanations, a dashboard shows spending trends, and an AI assistant answers questions about spending in plain English.

> **Status:** in progress. All data in this project is synthetic; no real bank data is used.

## Architecture (planned)

```
React website  ──►  NodeJS (Express) back end  ──►  Oracle Database
                              │                         ▲
                              ▼                         │
                   Python (FastAPI) ML service ─────────┘
                   • fraud model (XGBoost + SHAP)
                   • AI assistant (LangChain, read-only SQL)

Raw CSV ──► AWS S3 ──► AWS Lambda (Python cleaning) ──► Oracle
```

## Repository layout

| Folder | Contents | Language |
| --- | --- | --- |
| `pipeline/` | Synthetic data generator, cleaning, S3 → Lambda pipeline | Python |
| `database/` | Schema (3NF), views, PL/SQL package | SQL, PL/SQL |
| `model/` | Fraud detection notebooks and training | Python |
| `agent/` | LangChain SQL agent, evaluation set and scorer | Python |
| `ml-service/` | FastAPI service hosting the model and agent | Python |
| `backend/` | Main API: uploads, summaries | NodeJS (Express) |
| `frontend/` | Dashboard: upload, charts, flagged payments, chat | React |
| `analysis/` | Spending analysis report | R |
| `tests/` | pytest tests | Python |
| `docs/` | ER diagram, architecture, retrospective | — |

## Getting started

1. Create a Python virtual environment in `.venv` and install `requirements.txt`.
2. Copy `.env.example` to `.env` and fill in your own values. Never commit `.env`.
3. Run Oracle Database Free locally in Docker.

## Way of working

- Work is tracked as GitHub issues grouped into weekly milestones (sprints).
- Every change goes through a branch and pull request; `main` is protected.
- CI runs the tests on every pull request (added in Week 2).

## Results

_To be added: fraud model PR-AUC and recall, agent evaluation score._

## Responsible AI and limitations

_To be added._
