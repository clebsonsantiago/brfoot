from interface_console import Interface
from partida import Partida
from equipe import Equipe
from estatisticas import Estatisticas
import time
import random

tela_console = Interface()
partida = Partida()
tela_console.clear()

time_flamengo = Equipe("Flamengo")
time_flamengo.cria_equipe_aleatoria()
estatisticas = Estatisticas()

time_vasco_da_gama = Equipe("Vasco da Gama")
time_vasco_da_gama.cria_equipe_aleatoria()


gols_do_flamengo = 0
gols_do_vasco_da_gama = 0

print("Primeiro tempo: ")
for x in range(1, 46):
  
  vasco_ataque_randomico = time_vasco_da_gama.time
  #criar uma lista com os 5 melhores pontuados no calculo ataque * random
  partida.ordem_decrescente_dos_melhores(vasco_ataque_randomico, "ataque")

  flamengo_ataque_randomico = time_flamengo.time
  partida.ordem_decrescente_dos_melhores(flamengo_ataque_randomico, "ataque")

  vasco_melhores_ataques = sorted(vasco_ataque_randomico, key=lambda k: k["ataque"], reverse=True)
  flamengo_melhores_ataques = sorted(flamengo_ataque_randomico, key=lambda k: k["ataque"], reverse=True)

  jogador_flamengo = random.choice(flamengo_melhores_ataques[0:2])
  jogador_flamengo_ataque = estatisticas.resultado_media(jogador_flamengo, "ataque")

  jogador_vasco = random.choice(vasco_melhores_ataques[0:2])
  jogador_vasco_ataque = estatisticas.resultado_media(jogador_vasco, "ataque")
  vasco = time_vasco_da_gama.time
  goleiro_vasco = vasco[0]


  equipe_flamengo_ataque = estatisticas.resultado_media(time_flamengo.time, "ataque")
  equipe_flamengo_defesa = estatisticas.resultado_media(time_flamengo.time, "defesa")
  flamengo = time_flamengo.time
  goleiro_flamengo = flamengo[0]
  
  equipe_vasco_ataque = estatisticas.resultado_media(time_vasco_da_gama.time, "ataque")
  equipe_vasco_defesa = estatisticas.resultado_media(time_vasco_da_gama.time, "defesa")
  
  #gol Flamengo
  numeracao1 = int(jogador_flamengo_ataque/2 + equipe_flamengo_ataque/2 + random.random() * int(20 - goleiro_vasco["defesa"]) - equipe_vasco_defesa - gols_do_flamengo + gols_do_vasco_da_gama)
  
  gol_time1 = lambda: True if numeracao1 >= 20 else False

  #gol vasco da gama
  numeracao2 = int(jogador_vasco_ataque/2 + equipe_vasco_ataque/2 + random.random() * int(20 - goleiro_flamengo["defesa"]) - equipe_flamengo_defesa - gols_do_vasco_da_gama + gols_do_flamengo)

  gol_time2 = lambda: True if numeracao2 >= 20 else False

  if(gol_time1() == True):
    print(x, ": {} fez 1 goool para o Flamengo".format(jogador_flamengo["nome"]), sep="")
    gols_do_flamengo += 1
  
  if(gol_time2() == True):
    print(x, ": {} fez 1 goool para o Vasco da Gama".format(jogador_vasco["nome"]), sep="")
    gols_do_vasco_da_gama += 1
  else:
    print(x, ": ", sep="")

  time.sleep(0.0)
print("")
print("Gols do Flamengo: ", gols_do_flamengo)
print("Gols do Vasco da Gama: ", gols_do_vasco_da_gama)

print("----------------------")
print("   Time do Flamengo")
print("----------------------")
print("")

tela_console.imprime_jogadores_da_equipe(time_flamengo.time)
print("")
tela_console.imprime_estastisticas_de_time(time_flamengo.time)

print("")
print("")
ataque_do_flamengo = estatisticas.resultado_media(time_flamengo.time, "ataque")
defesa_do_flamengo = estatisticas.resultado_media(time_flamengo.time, "defesa")
comportamento_do_flamengo = estatisticas.resultado_media(time_flamengo.time, "comportamento")

print("")
tela_console.imprime_estastisticas_de_time(time_vasco_da_gama.time)

ataque_do_vasco_da_gama = estatisticas.resultado_media(time_vasco_da_gama.time, "ataque")
defesa_do_vasco_da_gama = estatisticas.resultado_media(time_vasco_da_gama.time, "defesa")
comportamento_do_vasco_da_gama = estatisticas.resultado_media(time_vasco_da_gama.time, "comportamento")
