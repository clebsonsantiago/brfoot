#import random as random
class Eventos:
  def __init__(self):
    self.__eventos = []

  def falta(self, comportamento):
    pass
  
  def cartao_amarelo(self, comportamento):
    pass
  
  def cartao_vermelho(self, comportamento):
    pass

  def contundido(self, comportamento):
    pass

  def gol(self, minuto, n_camisa_do_jogador, time):
    jogador = time.exibe_jogador(n_camisa_do_jogador)["nome"]
    frase = "Goool do {} para o {}".format(jogador, time.nome)
    self.__eventos.append({
      "minuto": minuto,
      "evento": "gol",
      "frase": frase
    })
  
  @property
  def eventos(self):
    return self.__eventos
