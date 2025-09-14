import gradio as gr
import pandas as pd
from typing import List
import yaml

from job_board_scraper import get_jobs
from job_board_scraper.support import ScraperSource

def scraper_tab() -> gr.Interface:


    sites_names = gr.Dropdown(
        choices=[source.value.capitalize() for source in ScraperSource],
        value=ScraperSource.LINKEDIN.value.capitalize(),
        label="Job Sites",
        info="Enter the names of the job recruitment websites (e.g., Indeed, LinkedIn)", 
        multiselect=True
    )
    scrape_button = gr.Button("Scrape Jobs (may takes a while)")
    scrape_output = gr.DataFrame(label="Scraped Jobs")
    
    def scrape_jobs(site_names: List[str] = ["linkedin"]):

        config_path = ".job_board_scraper/config.yaml"
        if len(site_names) == 0:
            return ValueError('You must select at least one site name in the dropdown menu.')
        site_names = [ site.lower() for site in site_names ]
        with open(config_path, "r") as file:
            CFG = yaml.safe_load(file)

        df: pd.DataFrame = get_jobs(site_names, CFG)

        df = df[['id', 'title', 'company', 'job_url']]
        output = gr.DataFrame(
            value=df,
            headers=list(df.columns),
            interactive=True
        )
        return output
    

    scrape_button.click(scrape_jobs, inputs=sites_names, outputs=scrape_output)
    