#variaveis para o sistema de pontacao
pontosX = 0
pontosO = 0
contadorJogos = 1
contadorEmpates = 0


def Jogo_Da_Velha():
  tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  QuadradoMagico = [4, 9, 2, 3, 5, 7, 8, 1, 6]

  #metodo que cria o tabuleiro
  def Tabuleiro():
    print()
    print("┌───┬───┬───┐")
    print("|", tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8],"|")
    print("├───┼───┼───┤")
    print("|", tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5],"|")
    print("├───┼───┼───┤")
    print("|", tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2],"|")
    print("└───┴───┴───┘")
    print()

  #metodo que verifica se o numero digitado é valido no tabuleiro
  def PegarNumero():
    while True:
      numero = input()
      try:
        numero  = int(numero)
        if numero in range(1, 10):
          return numero
        else:
          print("\nO número não existe no tabuleiro.")
      except ValueError:
        print("\nIsso não é um número. Tente novamente.")
        continue

  #metodo que exibe o numero de partidas jogadas, vitorias do jogador X e O e empates
  def Pontuacaoo():
    print("\nPartidas jogadas:", contadorJogos, "Jogador \'X\' ganhou:", pontosX, "Jogador \'O\' ganhou:", pontosO, "Empates:", contadorEmpates)

  #metodo que verifica se o jogador preencheu todos os quadrados em uma linha, coluna ou diagonal
  def ChecaVitoria(jogador):
    global pontosX
    global pontosO
    global contadorEmpates

    jogadas = 0

    #no metodo de checagem de vitoria, é usado o metodo do quadrado magico, onde se a soma de x, y e z é igual a um numero n, o vencedor é definido
    for x in range(9):
      for y in range(9):
        for z in range(9):
          if x != y and y != z and z != x:
            if tabuleiro[x] == jogador and tabuleiro[y] == jogador and tabuleiro[z] == jogador:
              if QuadradoMagico[x] + QuadradoMagico[y] + QuadradoMagico[z] == 15:
                if jogador == "X":
                  pontosX += 1
                elif jogador == "O":
                  pontosO += 1
                print("O jogador", jogador ,"ganhou!!!\n")
                Pontuacaoo()
                return True

  #metodo para definir se ha um empate 
    for a in range(9):
      if tabuleiro[a] == "X" or tabuleiro[a] == "O":
        jogadas += 1
      if jogadas == 9:
        print("EMPATE!!!\n")
        contadorEmpates += 1
        Pontuacaoo()
        return True
  
  #metodo que define os turnos jogada apos jogada
  def Turno(jogador):
    espaco_colocado = PegarNumero() - 1
    if tabuleiro[espaco_colocado] == "X" or tabuleiro[espaco_colocado] == "O":
      print("\nEste espaço ja foi ocupado, por favor coloque em outro lugar")
      Turno(jogador)
    else:
      tabuleiro[espaco_colocado] = jogador

    
  
  acabou = False
 #loop que alterna as jogadas e chama o metodo de checagem de vitoria para definir um vencedor
  while not acabou:
    Tabuleiro()
    acabou = ChecaVitoria("O")
    if acabou == True:
      break
    print("Jogador X faça sua jogada")
    Turno("X")
    
    Tabuleiro()
    acabou = ChecaVitoria("X")
    if acabou == True:
      break
    print("Jogador O faça sua jogada")
    Turno("O")
  
  if input("Deseja jogar Novamente? (sim/nao)\n") == "sim":
    print()
    Jogo_Da_Velha()

Jogo_Da_Velha()