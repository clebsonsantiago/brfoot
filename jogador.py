from random import random
class Jogador:
  def __init__(self) :
      self.__nome = "" 
      self.__tipo = ""
      self.__defesa = 0
      self.__ataque = 0
      self.__comportamento = 0

  def criar_jogador(self, nome, tipo):
    self.__nome = nome
    self.__tipo = tipo["tipo"]
    self.__defesa = tipo["defesa"] + int(random()*10)
    self.__ataque = tipo["ataque"] + int(random()*10)
    self.__comportamento = int(random()*10) 

  def dados_do_jogador(self):
    dados_do_jogador = {
      "nome": self.__nome,
      "tipo": self.__tipo,
      "defesa": self.__defesa,
      "ataque": self.__ataque,
      "comportamento": self.__comportamento
     }

    return dados_do_jogador

  #get and set: Nome
  @property
  def nome(self):
    return self.__nome
  @nome.setter
  def nome(self, nome):
    self.__nome = nome

  #get and set: Tipo
  @property
  def tipo(self):
    return self.__tipo
  @tipo.setter
  def tipo(self, tipo):
    self.__tipo = tipo

  #get and set: Defesa
  @property
  def defesa(self):
    return self.__defesa
  @defesa.setter
  def defesa(self, defesa):
    self.__defesa = defesa
  
  #get and set: Ataque
  @property
  def ataque(self):
    return self.__ataque
  @ataque.setter
  def ataque(self, ataque):
    self.__ataque = ataque
  
  #get and set: Comportamento
  @property
  def comportamento(self):
    return self.__comportamento
  @comportamento.setter
  def comportamento(self, comportamento):
    self.__comportamento = comportamento