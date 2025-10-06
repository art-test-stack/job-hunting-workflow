import os, tempfile, io, yaml
from pathlib import Path
from typing import List
import gradio as gr
from gradio_pdf import PDF

from job_board_scraper import get_jobs, get_job_by_url, JobData
from job_board_scraper.support import ScraperSource
from cv_generator import CVPipeline, CVStyle


import gradio as gr

def cv_tab() -> gr.Interface:

    with gr.Blocks():
        cv_style = gr.Radio(
            choices=[c.value.capitalize() for c in CVStyle],
            label="CV Style",
            value=CVStyle.MODERN.value.capitalize()
        )
        input_type = gr.Radio(
            choices=["Job URL", "Offer ID"],
            label="Input Type",
            value="Job URL"
        )
        top_margin = gr.Slider(
            -1, 0,
            value=-0.5,
            step=0.05,
            interactive=True,
            label="Adapt Top Margin (in)",
        )

        def generate_cv_dynamic(cv_style: str, input_type: str, input_value: str, top_margin: float):
            cv_style = cv_style.lower()
            if input_type == "Offer ID":
                offer_file = f"/Users/arthurtestard/job-board-scraper/data/desc/li-{input_value}.txt"
                cv_pipeline = CVPipeline(offer_file=offer_file, params={"cv_style": cv_style, "top_margin": top_margin})
            elif input_type == "Job URL":
                job_data = get_job_by_url(input_value)
                offer_dict = job_data
                cv_pipeline = CVPipeline(offer_dict=offer_dict, params={"cv_style": cv_style, "top_margin": top_margin})
            else:
                raise ValueError("Invalid input type")

            cv_pipeline.make_cv()

            pdf_bytes = cv_pipeline.get_pdf_bytes()

            tmp_path = os.path.join(tempfile.gettempdir(), "cv_arthur_testard_2025.pdf")
            with open(tmp_path, "wb") as f:
                f.write(pdf_bytes)
            return tmp_path, tmp_path


        input_value = gr.Textbox(label="Input Value", placeholder="Enter Offer ID or Job URL")
        preview = PDF(label="CV Preview", height=400)
        download = gr.File(label="Download CV")

        gr.Interface(
            generate_cv_dynamic,
            [cv_style, input_type, input_value, top_margin],
            [preview, download],
            description="Generate CV based on Offer ID or Job URL.",
            flagging_mode="never"
        )