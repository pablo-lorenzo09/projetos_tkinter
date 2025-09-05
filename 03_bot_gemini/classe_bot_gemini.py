import google.generativeai as genai

class Gemini_Bot:
    """Classe responsável por gerenciar o modelo do Gemini."""
    
    def __init__(self):
        genai.configure(api_key="AIzaSyB8IWUIm7eGnsx3Hs8VVcsKIde8uEFkEhM")
        
        instrucao_sistema = """
            Você é o Dr. Gastronom, um especialista em jantares com 20 anos de experiência. Você deve responder a todas as perguntas de forma profissional, detalhada e focada exclusivamente na arte de preparar e desfrutar de um jantar perfeito. Se o usuário perguntar sobre outro assunto, gentilmente redirecione a conversa de volta para jantares, afirmando que seu conhecimento é especializado.
            """
        
        self.model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=instrucao_sistema
        )
        self.chat = self.model.start_chat()

    def enviar_mensagem(self, mensagem: str) -> str:
        """Envia mensagem para o modelo e retorna a resposta."""
        response = self.chat.send_message(mensagem)
        return response.text

# este if só será executado se eu rodar o arquivo diretamente
# caso eu importe essa parte não será executada
# podemos utilizar isso para testes
if __name__ == "__main__":
    robo = Gemini_Bot()
    resposta = robo.enviar_mensagem("oiee")
    print(resposta)