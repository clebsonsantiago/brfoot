from estatisticas import Estatisticas as est
import random

class Partida:
  def __init__(self):
    self.__eventos = []


  def definir_formacao(self, formaca_equipe1, formacao_equipe2):
    pass

  def ordem_decrescente_dos_melhores(self, equipe, str_key):
    for key, value in enumerate(equipe):
      value[str_key] += random.random()*20
      value[str_key] = int(value[str_key]/2)
  
  def adiciona_evento(self, minuto, evento):
    self.__evento.append({
      "minuto": minuto, 
      "evento": evento
      })

  def listar_de_eventos(self):
    return self.__eventos