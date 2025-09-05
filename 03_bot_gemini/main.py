from classe_bot_gemini import Gemini_Bot
from classe_chat import Janela

robo = Gemini_Bot()

resposta = robo.enviar_mensagem("quem descobriu o Brasil?")

print(resposta)

janela = Janela()
janela.run()

