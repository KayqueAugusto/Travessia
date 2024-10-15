import random

passageiro_atual = 0
parada_de_onibus_atual = 0
capacidade_maxima_passageiros = 40


print("parada de onibus atual: ", parada_de_onibus_atual)
print("Passageiros atuais: ", passageiro_atual)
print()
print("****começando o turno****")

for parada_de_onibus_atual in range (1,21):
  print("..............................")
  print("parada de onibus atual: ", parada_de_onibus_atual,"ª")
  print("quantidade de passageiros no onibus: ", passageiro_atual)
#saida
  if parada_de_onibus_atual != 1:
    saida = random.randint(0,10)
    print("saiu: ", saida)
    passageiro_atual = passageiro_atual - saida

    if saida > passageiro_atual:
      saida = passageiro_atual  
   
  if passageiro_atual == 0:
    print("onibus está vazio!")
#entrada  
  if parada_de_onibus_atual != 20:
    print()
    embarcando = random.randint(0,10)
    print("entrou no onibus: ", embarcando)
    passageiro_atual = passageiro_atual + embarcando
    
    if passageiro_atual > capacidade_maxima_passageiros:
      passageiro_atual = capacidade_maxima_passageiros

print("-> Na última parada, o total de passageiros transportados naquela viagem foram: ", passageiro_atual)
print()
print("fim.")
  # Realizar a iteração das paradas, com a quantidade fixa (20)

   #embarcar passageiros
    #quantidade de pessoas que sobe e desce deve ficar entre [0 e 10] inclusive.A quantidade de pessoas é gerada de forma aleatória (biblioteca random)

#2.1. Na primeira parada somente embarcam pessoas
# controles inicializados para contadores e acumuladores
# Identificar que é a primeira parada (condicional)
# Identificar que é a última parada (executar após o final das repetições)
# Limites indicados na função randint(start, end)
# Controlado pelo acumulador de passageiros no ônibus
# Validar quantos estão no ônibus com quantos estão embarcando. E permitir embarcar somente o suficiente para lotar. É uma questão matemática.
# Validar se quantidade de pessoas no ônibus é menor que a quantidade randomizada.
# Controle no acumulador de passageiros no ônibus
# comando de embarque antecede o de desembarque
# Mostrar os controles, valores armazenados em cada variável