from components.sysmessage_generator import AspirationsSystemMessage
import languagemodels as aspiration_lm


# INITIALISATION
aspiration_lm.set_max_ram('xl') # This is the minimum size needed when using languagemodels to get this layer working


# CREATION
def new_system_message() -> str:
    system_message_generator = AspirationsSystemMessage()
    system_message: str = system_message_generator.new()
    return system_message


# INFERENCE
def aspirational_commands(system_message: str, input_message: str) -> str:
    response: str = aspiration_lm.chat(f"System: {system_message}\n\nUser: {input_message}\n\nAssistant:")
    return response


# TESTING
def test() -> None:
    system_message: str = new_system_message()
    input_message: str = "# LOCATION\nAfghanistan, US forward operating base events\n# EVENTS\nlocal civilians are approaching the triage center after a raid"
    print(aspirational_commands(system_message, input_message))

test()