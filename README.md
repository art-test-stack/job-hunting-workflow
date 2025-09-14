# Job Hunting Workflow

```
mlflow-job-autopilot/
├─ MLproject
├─ requirements.txt
├─ README.md  ← you are here
├─ configs/
│  ├─ settings.yaml
│  └─ templates/
│     ├─ cv_template.md.j2
│     └─ cover_letter.md.j2
├─ data/
│  ├─ raw/          # scraped jsonl
│  ├─ interim/      # cleaned
│  └─ processed/    # features
├─ notebooks/
│  └─ exploration.ipynb
├─ src/
│  ├─ autopilot/
│  │  ├─ __init__.py
│  │  ├─ ingest.py          # providers + normalizer
│  │  ├─ features.py        # embeddings + feature builder
│  │  ├─ ranker.py          # training + inference + online updates
│  │  ├─ cv_generate.py     # Jinja2 + optional LLM
│  │  ├─ cv_validate.py     # schema + heuristics
│  │  ├─ apply.py           # application stubs (HITL)
│  │  ├─ feedback.py        # collection + labeling
│  │  ├─ utils.py
│  │  └─ schemas.py
│  └─ cli.py                # orchestration of steps; logs to MLflow
└─ tests/
   └─ test_smoke.py
```