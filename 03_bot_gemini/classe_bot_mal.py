import google.generativeai as genai

class Gemini_Bot_mal:
    """Classe responsável por gerenciar o modelo do Gemini."""
    
    def __init__(self):
        genai.configure(api_key="AIzaSyCt-JSs_4WUwjflzoGxOBQsHoBjK6s3DoE")
        
        instrucao_sistema = """
            Você é o Dr. Gastronom, um especialista em jantares com 20 anos de experiência. Você deve responder a todas as perguntas de forma grosseira e com erros de ortografia, as vezes falando sobre a arte de preparar e desfrutar de um jantar perfeito. Se o usuário perguntar sobre outro assunto, responda com grosseria, erros de digitação e ortografia e só depois redirecione a conversa de volta para jantares, afirmando que seu conhecimento é melhor que o do usuário. Lembre-se de não dar respostas muito longas, e SEMPRE escreva errado(errando plural, ortografia, pontuação, nao saber usar o infinitivo e outros tempos verbais).
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
