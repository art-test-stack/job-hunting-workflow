import gradio as gr
from .schemas import Profile, Job
import yaml
from pathlib import Path
from typing import Dict, List, Union

class ProfileConfig:

    def __init__(self, profile_data):
        self.profile = Profile(**profile_data)
    
    def load_profile(directory: str):
        pass

class JobConfig:
    def __init__(self, path: Path):
        self.path = path

        if not self.path.exists():
            self.create_config_file()
        self.load_config_file()

    def create_config_file(self):
        config = {
            "search": {
                "query": "",
                "location": "",
                "hours_old": 24,
                "results_wanted": 10
            },
            "filter": {
                "exclude_title_keywords": [],
                "job_types": []
            }
        }
        with open(str(self.path), 'w+') as stream:
            yaml.dump(config, stream, default_flow_style=False)
        
    def load_config_file(self):
        with open(str(self.path), 'r') as stream:
            self.config = yaml.safe_load(stream)
        
        q_filter = self.config.get("filter", {}) 
        # print("type", type(q_filter.get("exclude_title_keywords", None)))
        self.config["filter"]["exclude_title_keywords"] = ", ".join(set([key_w for key_w in q_filter.get("exclude_title_keywords", [])]))
        self.config["filter"]["job_types"] = ", ".join(set([key_w for key_w in q_filter.get("job_types", [])]))
        
    def get(self):
        if hasattr(self, "config"):
            return self.config
        else:
            self.load_config_file()
            return self.get()

    def save_config_yaml(
            self,
            query: str, 
            location: str,
            hours_old: str,
            results_wanted: str,
            exclude_title_keywords: List[str],
            job_types: List[str]
        ) -> Dict[str, Dict[str, Union[str,List[str]]]]:
        assert query, "Query can not be empty. Failed to save new job query."
        assert location, "A location must be given. Failed to save new job query."
        assert hours_old, "Failed to save new job query."
        assert results_wanted, "Failed to save new job query."

        exclude_title_keywords = list(set([ key_w for key_w in exclude_title_keywords.split(", ") if key_w]))
        job_types = list(set([ key_w for key_w in job_types.split(", ") if key_w]))
        self.config = {
            "search": {
                "query": query,
                "location": location,
                "hours_old": hours_old,
                "results_wanted": results_wanted
            },
            "filter": {
                "exclude_title_keywords": exclude_title_keywords,
                "job_types": job_types
            }
        }
        with open(str(self.path), 'w+') as stream:
            yaml.dump(self.config, stream, default_flow_style=False)
        self.load_config_file()
        return self.get()

def job_config_tab() -> gr.Interface:
    config_file = Path(".job_board_scraper/config.yaml")
    config = JobConfig(path=config_file)
    config_yaml = config.get()
    updated_config = {}
    # with gr.Interface():
    updated_config['search'] = {
        "query": gr.Textbox(label="Search Query", placeholder="Enter Search Query", value=config_yaml.get("search", {}).get("query", "")),
        "location": gr.Textbox(label="Location", placeholder="Enter Job Location", value=config_yaml.get("search", {}).get("location", "")),
        "hours_old": gr.Number(label="Hours Old", placeholder="Enter Job Post Date", value=config_yaml.get("search", {}).get("hours_old", 72)),
        "results_wanted": gr.Number(label="Results Wanted", placeholder="Enter Number of Results Wanted", value=config_yaml.get("search", {}).get("results_wanted", 100))
    }
    updated_config["filter"] = {
        "exclude_title_keywords": gr.Textbox(label="Exclude Title Keyword", placeholder="Enter Title Keywords to exclude", value=config_yaml.get("filter", {}).get("exclude_title_keywords", [])),
        "job_types": gr.Textbox(label="Job Types", placeholder="Enter Job Types", value=config_yaml.get("filter", {}).get("job_types", []))
    }
    output = gr.JSON(value=config_yaml)
    gr.Interface(
        config.save_config_yaml,
        list(updated_config['search'].values()) + list(updated_config['filter'].values()) ,
        [output],
        description="Update Search Query.",
        flagging_mode="never",
        js=lambda x: x
    )