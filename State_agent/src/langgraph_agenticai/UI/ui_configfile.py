from configparser import ConfigParser
from pathlib import Path


# config_file = Path("D:/Gen-ai/State_agent/src/langgrapg_agenticai/UI/Streamlit_UI/ui_config.ini")

class config:
    def __init__(self, config_file = r"D:\Gen-ai\State_agent\src\langgrapg_agenticai\UI\Streamlit_UI\ui_config.ini"):
        self.config=ConfigParser()
        self.config.read(config_file)
    
    def get_llm_options(self):
       return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("AGENT_ARCHETYPE").split(", ")
    def get_groq_model_options(self):
         return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")    