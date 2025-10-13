# Job Hunting Workflow

This application is an end-to-end web app which permits the user to simply follow and manage its job applications. 

Its include a table to have an overview of the current job applications, a page for each job application with the possibility to give the job description in order to generate a tailored resume, and profile manager.

## Prerequirements 

The workflow is dependent on [this repository](https://github.com/art-test-stack/cv_generator). First clone it in a directory (eg: /path/to/cv_generator). Then add it to your python environment:
```bash
pip install -e /path/to/cv_generator  
```

## To run manually the web application
To run manually the application:
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open an other terminal:
```bash
cd job-tracker-web
npm install
npx @hey-api/openapi-ts -i http://localhost:8000/openapi.json -o src/client
npm run dev
```

## To run the gradio application (demo)
```bash
pip install -r requirements.txt
python main.py
# or
gradio main.py --demo-name=app     
```

## Features in coming

- Dashboard: the user can track its own main statistics.
- Autofill profile: the user can submit his resume/CV to auto-fill its profile.
- Todo page: the user can see and prioritize the following tasks for its job application/interview management. 
- Future: include HR environment which permits HR from a company to get top-$k$ profile based on the job description. 