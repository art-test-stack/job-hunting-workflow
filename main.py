import gradio as gr
from gradio_pdf import PDF

from job_hunting_workflow.cv_generate import cv_tab
from job_hunting_workflow.scraper import scraper_tab
from job_hunting_workflow.config import job_config_tab

import pandas as pd



with gr.Blocks() as app:
    gr.Markdown("# Job Hunting Workflow")

    with gr.Tab("Scrape Jobs"):
        scraper_tab()
    
    with gr.Tab("Generate CV"):
        cv_tab()

    # with gr.Tab("Select Jobs for Recommendation Model"):
    #     jobs_input = gr.Textbox(label="Scraped Jobs", placeholder="List of scraped jobs will appear here")
    #     select_button = gr.Button("Select Interesting Jobs")
    #     select_output = gr.Textbox(label="Selected Jobs")
    #     select_button.click(select_jobs, inputs=jobs_input, outputs=select_output)
    with gr.Tab("Edit Job Config"):
        job_config_tab()


if __name__ == "__main__":
    app.launch()