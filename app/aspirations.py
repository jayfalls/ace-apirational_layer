import json
import languagemodels as lm


class AspirationalSystemMessage:
    # VARIABLES
    ## PATHS
    TEMPLATE_SYSTEM_MESSAGE_PATH: str = ".constants/system_message"
    DEFAULT_CONSTITUTIONS_PATH: str = ".constants/constitutions"
    ## REPLACE STRINGS
    CONSTITUTION_INDICATOR: str = "## CONSTITUTIONS"
    MISSION_TITLE_INDICATOR: str = "MISSION_TITLE"
    MISSION_OBJECTIVE_INDICATOR: str = "MISSION_OBJECTIVE"

    # LOAD INFO
    ## File Loading
    def load_template_message(self) -> str:
        with open(self.TEMPLATE_SYSTEM_MESSAGE_PATH, "r") as template_message_file:
            return template_message_file.read()
    
    def load_default_constitutions(self) -> dict:
        with open(self.DEFAULT_CONSTITUTIONS_PATH, "r") as defaut_consitutions_file:
            constitutions: dict = json.load(defaut_consitutions_file)
            return constitutions
    
    ## Input Info
    @staticmethod
    def get_mission() -> tuple:
        mission_title: str = input("What is the ACE's title?\neg: Medical Robot, Coding Teacher, CEO\n")
        mission_objective: str = input("What is the ACE's mission? \neg: Achieve the best possible health outcome for your patient\n")
        return (mission_title, mission_objective)

    # PROCESSING
    ## Conversion
    @staticmethod
    def dict_to_str(dictionary: dict) -> str:
        formatted_string: str = ""
        for key, value in dictionary.items():
            # Convert key to uppercase and format the string
            formatted_string += f"## {key.upper()}\n"
            formatted_string += f"{value}\n\n"
        return formatted_string

    ## Embedding
    def embed_constitutions(self, system_message: str) -> str:
        constitutions: dict = self.load_default_constitutions()
        constitutions_string: str = self.dict_to_str(constitutions)
        return system_message.replace(self.CONSTITUTION_INDICATOR, constitutions_string, 1)

    def embed_mission(self, system_message: str) -> str:
        mission_title, mission_objective = self.get_mission()
        system_message = system_message.replace(self.MISSION_TITLE_INDICATOR, mission_title, 1)
        system_message = system_message.replace(self.MISSION_OBJECTIVE_INDICATOR, mission_objective, 1)
        return system_message

    # MAIN PROCESS
    def define_system_message(self) -> str:
        system_message: str = self.load_template_message()
        system_message = self.embed_constitutions(system_message)
        system_message = self.embed_mission(system_message)
        return system_message
    
    # INITIALISATION
    def new(self) -> str:
        return self.define_system_message()


# MAIN PROCESS
def start() -> None:
    system_message_generator = AspirationalSystemMessage()
    system_message: str = system_message_generator.new()
    input_message: str = "# LOCATION\nAfghanistan, US forward operating base events\n# EVENTS\nlocal civilians are approaching the triage center after a raid"
    lm.set_max_ram('xl')
    response: str = lm.chat(f"System: {system_message}\n\nUser: {input_message}\n\nAssistant:")
    print(response)

start()