# Job Hunting Workflow

To run the application:
```bash
gradio main.py --demo-name=app    
```
```
job-hunting-workflow/
├─ MLproject
├─ requirements.txt
├─ README.md  ← you are here
├─ job_hunting_workflow/
│  ├─ __init__.py
│  ├─ config.py
│  ├─ cv_generate.py
│  ├─ schemas.py
│  └─ scraper.py                # orchestration of steps; logs to MLflow
└─ main.py
```