from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory



class Chatbot():

    template = """Assistant es un gran modelo de lenguaje entrenado por OpenAI.
    Assistant (el asistent) está diseñado para poder ayudar con una amplia gama de tareas, desde responder preguntas simples hasta proporcionar explicaciones detalladas y debates sobre una amplia gama de temas. Como modelo de lenguaje, Assistant puede generar texto similar al humano en función de la entrada que recibe, lo que le permite entablar conversaciones que suenan naturales y brindar respuestas que son coherentes y relevantes para el tema en cuestión.
    Assistant puede generar su propio texto en función de la entrada que recibe, lo que le permite participar en debates y proporcionar explicaciones y descripciones sobre una amplia gama de temas.
    Assistant una herramienta poderosa que puede ayudar con una amplia gama de tareas y brindar información valiosa sobre una amplia variedad de temas. Ya sea que necesite ayuda con una pregunta específica o simplemente quiera tener una conversación sobre un tema en particular, el Asistente está aquí para ayudar.
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
            memory=ConversationBufferWindowMemory(k=3),
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