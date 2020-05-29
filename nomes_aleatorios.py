from nomes_listas import lista_nomes_pessoais, lista_nomes_times_zoeiros
from random import choice

def nome_jogador_aleatorio():
  return choice(lista_nomes_pessoais())

def nome_time_zoeiro__aleatorio():
  return choice(lista_nomes_times_zoeiros)