from components.sysmessage_generator import AspirationsSystemMessage
import languagemodels as aspiration_lm
import re


# INITIALISATION
aspiration_lm.set_max_ram('xl') # This is the minimum size needed when using languagemodels to get this layer working


# CREATION
def new_system_message() -> str:
    system_message_generator = AspirationsSystemMessage()
    system_message: str = system_message_generator.new()
    return system_message


# INFERENCE
def process_system_message(system_message: str, input_message: str) -> str:
    response: str = aspiration_lm.chat(f"System: {system_message}\n\nUser: {input_message}\n\nAssistant:")
    return response

def split_directives(directives_string: str) -> list:
    split_pattern = r'(?<=\D)(?=\d)'
    directives: list = re.split(split_pattern, directives_string)
    return directives

def embue_principles(principles_sysmessage: str, directives: list) -> str:
    for directive in directives:
        full_directive: str = process_system_message(principles_sysmessage, directive)
        print(full_directive)


# TESTING
def test() -> None:
    directive_sysmessage: str = new_system_message()
    input_message: str = "# LOCATION\nAfghanistan, US forward operating base events\n# EVENTS\nlocal civilians are approaching the triage center after a raid"
    for _ in range(6):
        directives: str = process_system_message(directive_sysmessage, input_message)
        print(directives)

test()