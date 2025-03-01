from langchain_community.chat_models import ChatOllama

class Model:
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters
        self.model = ChatOllama(model=name, temperature=parameters["temperature"])

    def query(self, prompt):
        self.model.invoke(prompt)
