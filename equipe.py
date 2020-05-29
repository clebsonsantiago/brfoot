from nomes_aleatorios import nome_jogador_aleatorio
from jogador import Jogador
from tipos_de_jogadores import tipo_goleiro, tipo_zagueiro, tipo_centro_avante, tipo_atacante

class Equipe:
  def __init__(self, nome):
    self.__nome = nome
    self.__formacao = ""
    self.__time = []
    self.__ataque = []
    self.__centro_avante = []
    self.__defesa = []
    self.__goleiros = []

  def adiciona_jogador(self, nome, n_da_camisa, tipo):
    """
    Nome: 'Nome do Jogador'
    Camisa: 'Numero da camisa do Jogador'
    tipo: importe tipos_de_jogadores e coloque a função referente a funçao
    exemplo: adiciona_jogadores("Clebson Santiago", "1", goleiro())
    """
    jogador = Jogador() 
    jogador.criar_jogador(nome, tipo)
    jogador_dados = jogador.dados_do_jogador()
    jogador_dados["n_da_camisa"] = n_da_camisa
    self.__time.append(jogador_dados)
  
  def remove_jogador(self, n_da_camisa):
    """
    Camisa: 'Numero da camisa do Jogador'
    exemplo: remove_jogador("1")
    """
    for key, value in enumerate(self.__time):
      if value["n_da_camisa"] == n_da_camisa:
        self.__time.pop(key)
        return True
    
  def cria_equipe_aleatoria(self):
    
    for i in range(0,24):
      if i <= 2:
        tipo = tipo_goleiro()
      elif i <= 10:
        tipo = tipo_zagueiro()
      elif i <= 18:
        tipo = tipo_centro_avante()
      elif i <= 24:
        tipo = tipo_atacante()

      self.adiciona_jogador(nome_jogador_aleatorio(), i+1, tipo)
      
  @property
  def time(self):
    return self.__time

  @property
  def time_formacao(self):
    return self.__time_formacao
  @time_formacao.setter
  def __time_formacao(self, str_formacao):
    self.__time_formacao = str_formacao

  @property
  def ataque(self):
    self.__ataque = self.__lista_jogadores_por_chave("atacante")
    return self.__ataque
  @property
  def meio_de_campo(self):
    self.__centro_avante = self.__lista_jogadores_por_chave("centro_avante")
    return self.__centro_avante
  
  @property
  def defesa(self):
    self.__defesa = self.__lista_jogadores_por_chave("zagueiro")
    return self.__defesa
  
  @property
  def goleiros(self):
    self.__goleiros = self.__lista_jogadores_por_chave("goleiro")
    return self.__goleiros

  def __lista_jogadores_por_chave(self, chave_do_tipo_de_posicao):
    lista_jogadores_da_posicao = []
    for key, value in enumerate(self.__time):
      if value["tipo"] == chave_do_tipo_de_posicao:
        lista_jogadores_da_posicao.append(self.__time[key])
    
    return lista_jogadores_da_posicao