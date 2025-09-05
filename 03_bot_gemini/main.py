from classe_bot_gemini import Gemini_Bot
from classe_chat import Janela
from classe_bot_mal import Gemini_Bot_mal
janela = Janela()
robo = Gemini_Bot()
robo_mal = Gemini_Bot_mal()

resposta = robo.enviar_mensagem("h")

resposta_ruim = robo_mal.enviar_mensagem("oi, me ensina a jantas")
print(resposta_ruim)


janela.run()

# scrolled text