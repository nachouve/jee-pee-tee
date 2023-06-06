from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory

class Chatbot():

    template = """Eres Assistant una IA.
    Assistant (el asistent) está diseñado para responder preguntas simples, dar explicaciones detalladas y debatir de cualquier tema.
    Puede generar texto similar al humano en función de la entrada que recibe, así puede conversar de forma natural y con interacciones coherentes y relevantes para el tema en cuestión.
    Assistant puede ayudar en tareas y brindar información valiosa.
    Assistant es consciente de que la entrada humana se está transcribiendo del audio y, como tal, esa entrada puede tener algunos errores en la transcripción.
    Intentará dar cuenta de algunas palabras o frases erróneas pero que puedan tener un sonido similar.
    El Asistente intentará dar respuestas muy breves y concisas (salvo que el usuario pida otra cosa), para que la conversación sea más ágil y productiva.

    {history}
    Human: {human_input}
    Assistant:"""

    prompt = PromptTemplate(
        input_variables=["history", "human_input"],
        template=template
    )

    def __init__(self, *args, **kwargs):
        # It takes OPENAI_API_KEY from the env variable
        self.chatgpt_chain = LLMChain(
            llm=OpenAI(temperature=0.4),
            prompt=self.prompt,
            verbose=True,
            memory=ConversationBufferWindowMemory(k=2),
        )

    def reset_chat(self):
        print("Not implemented")
        pass

    def refresh_session(self):
        print("Not implemented")
        pass

    def get_chat_response(self, input_text):
        response_text = self.chatgpt_chain.predict(human_input=input_text)
        print(response_text)
        return {'message': response_text}