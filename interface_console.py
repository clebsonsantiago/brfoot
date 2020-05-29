import os
from estatisticas import Estatisticas

class Interface:  
  def __loop_inserir_jogadores(self):
    pass

  def imprime_jogadores_da_equipe(self, equipe_a_imprimir):
    """
    equipe = [{n_da_camisa, nome_do_jogador, tipo_do_jogador}]
    Resultado:
    1: Cauã, goleiro
    """
    for key, valor in enumerate(equipe_a_imprimir):
      print("{}: {}, {}".format(
        valor["n_da_camisa"],
        valor["nome"],
        valor["tipo"]
        ))
  
  def imprime_cabecalho_do_time(self, equipe):
    pass
    
  def imprime_estastisticas_de_time(self, equipe):
    """
    Imprima a estatisticas de ataque, defesa, comportamento dos jogadores presentes na lista
    ---
    equipe = [{n_da_camisa, nome_do_jogador, tipo_do_jogador}]
    ---
    resultado:
    Estatistica: 
    Ataque:  7.041666666666667
    Defesa:  5.416666666666667
    Comportamento:  5.541666666666667
    """
    estatisticas = Estatisticas()
    print("Estatisticas: ")
    print("Ataque: ", estatisticas.resultado_media(equipe, "ataque"))
    
    print("Defesa: ", estatisticas.resultado_media(equipe, "defesa"))
    
    print("Comportamento: ", estatisticas.resultado_media(equipe, "comportamento"))
    

  def clear(self):
    limpa_tela_do_console = lambda: os.system("clear")
    return limpa_tela_do_console()