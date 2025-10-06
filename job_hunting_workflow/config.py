import gradio as gr
from .schemas import Profile, Job
import yaml, json, pandas as pd
from pathlib import Path
from typing import Dict, List, Union

from cv_generator import Activity, Contact, Education, Experience, Header, Language, Project, Skill, Summary


class ProfileConfig:
    def __init__(self, path, language):
        # self.profile = Profile()
        if isinstance(path, str):
            path = Path(path)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
        self.path = path
        self.language = language
        self.load_profile()
    
    def load_profile(self):
        act_path = self.path / "activities.json"
        if act_path.exists():
            activities = json.loads(act_path.read_text())
            activities = [ Activity(**activity) for activity in activities ] 
        else:
            activities = []
        
        contact_path = self.path / "contact.json"
        if contact_path.exists():
            contact = json.loads(contact_path.read_text())
            contact = Contact(**contact) if contact else None
        else:
            contact = None
        
        edu_path = self.path / "education.json"
        if edu_path.exists():
            education = json.loads(edu_path.read_text())
            education = [ Education(**edu) for edu in education ]
        else:
            education = []

        exp_path = self.path / "experiences.json"
        if exp_path.exists():
            experiences = json.loads(exp_path.read_text())
            experiences = [ Experience(**exp) for exp in experiences ] 
        else:
            experiences = []
        
        hdr_path = self.path / "header.json"
        if hdr_path.exists():
            header = json.loads(hdr_path.read_text())
            header = [ Header(**hdr) for hdr in header ]
        else:
            header = None

        lng_path = self.path / "languages.json"
        if lng_path.exists():
            languages = json.loads(lng_path.read_text())
            languages = [ Language(**language) for language in languages ]
        else:
            languages = []

        prj_path = self.path / "projects.json"
        if prj_path.exists():
            projects = json.loads(prj_path.read_text())
            projects = [ Project(**project) for project in projects ]
        else:
            projects = []

        skl_path = self.path / "skills.json"
        if skl_path.exists():
            skills = json.loads(skl_path.read_text())
            skills = [ Skill(**skill) for skill in skills ]
        else:
            skills = []
        
        smr_path = self.path / "summary.json"
        if smr_path.exists():
            summary = json.loads(smr_path.read_text())
            summary = [ Summary(**smr) for smr in summary ]
        else:
            summary = []

        pic_path = self.path / "pic.jpg"
        
        self.profile = Profile(
            activities=activities, 
            contact=contact, 
            education=education, 
            experiences=experiences,
            header=header,
            languages=languages,
            projects=projects,
            skills=skills,
            summary=summary,
            pic=str(pic_path)
        )

    def save_profile(self):
        print("self.profile.__dict__", self.profile.__dict__)
        for key, item in self.profile.__dict__.items():
            print("key", key)
            cur_path = self.path / f"{key}.json"
            if not cur_path.exists():
                cur_path.touch()
            if key == "pic":
                item = { "path": item }
            if type(item) == list:
                item = [ it.__dict__ for it in item ]
            else:
                if item:
                    
                    item = item if type(item) == dict else item.__dict__
                else:
                    item = {}
            with open(str(self.path / f"{key}.json"), "w+") as stream:
                json.dump(item, stream)

    def add_activity(self, name, text, emoji):
        self.profile.activities.append(
            Activity(
                name=name,
                text=text,
                emoji=emoji
            )
        )
        return self.get('activities')
    
    def add_contact(self, phone, email, github, linkedin):
        self.profile.contact = { "email": email, "phone": phone, "github": github, "linkedin": linkedin }
        self.profile.contact = Contact(email=email, phone=phone, github=github, linkedin=linkedin)
        return gr.JSON(self.profile.contact)
    
    def create_education(self):

        idx = len(self.profile.education)
        self.profile.education.append(
            Education(
                id=idx,
                title=f"Edu {idx+1}",
                # institution="",
                # location="",
                # dates=dates,
                # highlights=highlights,
                # url=url,
                # logo=logo
            ))
        print('self.profile.edu', self.profile.education[idx].__dict__)
        return self.profile.education
    
    def modify_education(
            self, 
            idx = 0,
            title = "Education Title", 
            institution = "Institution", 
            location = "Location", 
            dates = "Dates", 
            highlights = [ "highlight 1" ], 
            url = "",
            logo = ""
        ):
        
        for edu in self.profile.education:
            if edu.id == idx:
                edu.title = title
                edu.institution = institution
                edu.location = location
                edu.dates = dates
                edu.highlights = highlights
                edu.url = url
                edu.logo = logo
            break
        return gr.JSON(edu).__dict__
    

    def add_experiences(self, title, company, location, dates, highlights, supplemental_info, logo, url):
        idx = len(self.profile.experiences)
        self.profile.experiences.append(
            Experience(
                id=idx,
                title=title,
                company=company,
                location=location,
                dates=dates,
                highlights=highlights,
                supplemental_info=supplemental_info,
                logo=logo
            )
        )
        return self.get("experiences")
    
    def create_experience(self):

        idx = len(self.profile.experiences)
        self.profile.education.append(
            Experience(
                id=idx,
                title=f"Exp {idx+1}",
                company="Company",
                location="Location",
                dates="dates",

                # institution="",
                # location="",
                # dates=dates,
                # highlights=highlights,
                # url=url,
                # logo=logo
            ))
        return self.profile.experiences
        # self.profile.education
    
    def modify_education(
            self, 
            idx = 0,
            title = "Education Title", 
            company = "Institution", 
            location = "Location", 
            dates = "Dates", 
            highlights = [ "highlight 1" ], 
            url = "",
            logo = "",
            supplemental_info = ""
        ):

# class Experience(BaseModel):
#     id: int
#     title: str
#     company: str
#     location: str
#     dates: str
#     highlights: Optional[List[Dict]] = None
#     url: Optional[str] = None
#     logo: str = ""
#     supplemental_info: Optional[str] = None
        
        for exp in self.profile.experiences:
            if exp.id == idx:
                exp.title = title
                exp.company = company
                exp.location = location
                exp.dates = dates
                exp.highlights = highlights
                exp.url = url
                exp.logo = logo
                exp.supplemental_info = supplemental_info
            break
        return gr.JSON(exp).__dict__
    
    def get(self, key: str):
        if key == "contact" and hasattr(self.profile, key):
            if self.profile.contact:
                return gr.JSON(self.profile.contact.__dict__)
            else:
                return gr.JSON({})
            
        if hasattr(self.profile, key):
            cls_val = getattr(self.profile, key)
            columns = {
                "activities": Activity,
                "education": Education,
                "experiences": Experience,
                "header": Header,
                "projects": Project,
                "skills": Skill,
                "summary": Summary
            }[key].__annotations__.keys()
            df = pd.DataFrame(data=[val.__dict__ for idx, val in enumerate(cls_val)], columns=list(columns))
            return gr.DataFrame(
                value=df,
                # value=[ val.__dict__ for val in cls_val ],
                headers=list(columns),
                interactive=True
            )
        else:
            raise ValueError(f"No attribute {key} in Profile class.")

        

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
        return gr.JSON(value=self.get())

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
        output,
        description="Update Search Query.",
        flagging_mode="never",
        js=lambda x: x
    )

def profile_config_tab() -> None:
    languages = ["en", "fr"]
    languages_dict = {
        "en": "English",
        "fr": "French"
    }
    profiles: Dict[str, ProfileConfig] = { 
        language: ProfileConfig(path=Path(f".cv_generator/data/{language}"), language=language) 
        for language in languages 
    }
    for language in languages:
        with gr.Tab(f"{languages_dict.get(language, 'None')} Profile"):
            save_btn = gr.Button("Save")
            save_btn.click(profiles[language].save_profile)
            with gr.Tab("Activities"):
                # config = ProfileConfig(path=Path(".cv_generator/data"))
                new_activity_name = gr.Textbox(label="Add an activity name")
                new_activity_text = gr.TextArea(label="Activity Description")
                new_activity_emoji = gr.Textbox(label="Add an emoji for the activity")

                activities = profiles[language].get('activities'),
                
                gr.Interface(
                    profiles[language].add_activity,
                    [new_activity_name, new_activity_text, new_activity_emoji],
                    activities
                )

            with gr.Tab("Contact"):
                if profiles[language].profile.contact:
                    contact_phone = profiles[language].profile.contact.phone
                    contact_email = profiles[language].profile.contact.email
                    contact_github = profiles[language].profile.contact.github
                    contact_linkedin = profiles[language].profile.contact.linkedin
                else:
                    contact_phone = ""
                    contact_email = ""
                    contact_github = ""
                    contact_linkedin = ""

                new_contact_phone = gr.Textbox(value=contact_phone, label="New Phone number")
                new_contact_email = gr.Textbox(value=contact_email, label="New email address")
                new_contact_github = gr.Textbox(value=contact_github, label="New Github")
                new_contact_linkedin = gr.Textbox(value=contact_linkedin, label="New LinkedIn")
                contact = profiles[language].get('contact')

                gr.Interface(
                    profiles[language].add_contact,
                    [new_contact_phone, new_contact_email, new_contact_github, new_contact_linkedin],
                    contact
                )


            # with gr.Tab("Education"):
            #     add_edu_btn = gr.Button("Add Education")
            #     education = gr.State(value=profiles[language].profile.education)

            #     def update_education():
            #         profiles[language].create_education()
            #         return profiles[language].profile.education

            #     add_edu_btn.click(
            #         fn=update_education,
            #         inputs=None,
            #         outputs=education
            #     )

            #     def render_education_tabs(education_list):
            #         print("education_list")
            #         for edu in education_list:
            #             # with gr.Tab(f"{edu.title}"):
            #             #     edu_json = gr.JSON(edu.__dict__)
            #             #     edu_id = gr.Number(value=edu.id, label="ID", interactive=False)
            #             #     edu_title = gr.Textbox(value=edu.title, label="Education Title")
            #             #     edu_institution = gr.Textbox(value=edu.institution, label="Institution")
            #             #     edu_location = gr.Textbox(value=edu.location, label="Location")
            #             #     edu_dates = gr.Textbox(value=edu.dates, label="Dates")
            #             #     edu_highlights = gr.JSON(value=edu.highlights, label="Highlights")
            #             #     edu_url = gr.Textbox(value=edu.url, label="Institution URL")
            #             #     edu_logo = gr.Textbox(value=edu.logo, label="Institution Logo")
            #             #     gr.Interface(
            #             #         profiles[language].modify_education,
            #             #         [edu_id, edu_title, edu_institution, edu_location, edu_dates, edu_highlights, edu_url, edu_logo],
            #             #         edu_json
            #             #     )
            #             with gr.Tab(f"{edu.title}"):
            #                 edu_json = gr.JSON(edu.__dict__)
            #                 edu_id = gr.Number(value=edu.id, label="ID", interactive=False)
            #                 edu_title = gr.Textbox(value=edu.title, label="Education Title")
            #                 edu_institution = gr.Textbox(value=edu.institution, label="Institution")
            #                 edu_location = gr.Textbox(value=edu.location, label="Location")
            #                 edu_dates = gr.Textbox(value=edu.dates, label="Dates")
            #                 edu_highlights = gr.JSON(value=edu.highlights, label="Highlights")
            #                 edu_url = gr.Textbox(value=edu.url, label="Institution URL")
            #                 edu_logo = gr.Textbox(value=edu.logo, label="Institution Logo")

            #                 update_btn = gr.Button("Update")

            #                 update_btn.click(
            #                     fn=profiles[language].modify_education,
            #                     inputs=[edu_id, edu_title, edu_institution, edu_location, edu_dates, edu_highlights, edu_url, edu_logo],
            #                     outputs=edu_json
            #                 )

            #     education.change(
            #         fn=render_education_tabs,
            #         inputs=education,
            #         outputs=education
            #     )
            with gr.Tab("Education"):
                add_edu_btn = gr.Button("Add Education")
                education_state = gr.State(value=profiles[language].profile.education)
                education_display = gr.JSON(label="Education List")

                def update_education():
                    profiles[language].create_education()
                    return profiles[language].profile.education

                add_edu_btn.click(
                    fn=update_education,
                    inputs=None,
                    outputs=education_state
                )

                def render_education_tabs(education_list):
                    return [edu.__dict__ for edu in education_list]

                education_state.change(
                    fn=render_education_tabs,
                    inputs=education_state,
                    outputs=education_display
                )


            with gr.Tab("Experiences"):
                add_exp_btn = gr.Button("Add Experience")
                experiences_state = gr.State(value=profiles[language].profile.experiences)
                experiences_display = gr.JSON(label="Experience List")

                def update_experiences():
                    profiles[language].create_experience()
                    return profiles[language].profile.experiences

                add_exp_btn.click(
                    fn=update_experiences,
                    inputs=None,
                    outputs=experiences_state
                )

                def render_experiences_tabs(experiences_list):
                    return [exp.__dict__ for exp in experiences_list]

                experiences_state.change(
                    fn=render_experiences_tabs,
                    inputs=experiences_state,
                    outputs=experiences_display
                )
            
            with gr.Tab("Header"):
                pass
            with gr.Tab("Languages"):
                pass
            with gr.Tab("Projects"):
                pass
            with gr.Tab("Skills"):
                pass
            with gr.Tab("Summary"):
                pass