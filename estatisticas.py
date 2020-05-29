class Estatisticas:
  def resultado_media(self, lista_equipe, chave_numerica_do_jogador_ou_time):
    if type(lista_equipe) == type(dict()):
      return float(lista_equipe[chave_numerica_do_jogador_ou_time])

    somatorio = 0
    for key, value in enumerate(lista_equipe):
      somatorio += value[chave_numerica_do_jogador_ou_time]
    return float(somatorio / len(lista_equipe))