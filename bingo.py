import random
from datetime import datetime

num = 0
cards = []
game = []
numbers_drawn = []
win = False
player_card = 0

#store cards from cartelas.txt in a usable format
with open('cartelas.txt','r') as file:
  for line in file:
    card = []
    card = line.rstrip().split(',')
    cards.append(card)

#select 4 cards for the game
def select_cards():
  for i in range(4):
    num_card = random.randint(1,len(cards)-1)
    game.append(cards[num_card])


#publish game layout
def publish_game(game):

  for i in range(len(game)):
    space1 = '    '
    space2 = '    '
    space3 = '    '
    space4 = '    '
    space5 = '    '

    if int(game[i][0]) in numbers_drawn:
        space1 = '----'
    if int(game[i][1]) in numbers_drawn:
        space2 = '----'
    if int(game[i][2]) in numbers_drawn:
        space3 = '----'
    if int(game[i][3]) in numbers_drawn:
        space4 = '----'
    if int(game[i][4]) in numbers_drawn:
        space5 = '----'
      
    if i == player_card:
      if win == True and winner == i:
        print (' ' + 9*'*' + '    **** **** **** **** ****')
        print(f' Cartela {i+1}: *  {str(game[i][0]).rjust(2)} * {str(game[i][1]).rjust(2)} * {str(game[i][2]).rjust(2)} * {str(game[i][3]).rjust(2)} * {str(game[i][4]).rjust(2)} * <<<<<<<<<<<<<<<<<<<<<<')
        print (' ' + 9*'*' + '    **** **** **** **** ****')

      else:
        print (13*' ' + f' {space1} {space2} {space3} {space4} {space5}')
        print(f' Cartela {i+1}:  | {str(game[i][0]).rjust(2)} | {str(game[i][1]).rjust(2)} | {str(game[i][2]).rjust(2)} | {str(game[i][3]).rjust(2)} | {str(game[i][4]).rjust(2)} | <<<<<<<<<<<<<<<<<<<<<<')
        print (13*' ' + f' {space1} {space2} {space3} {space4} {space5}')

      
    else:
      if win == True and winner == i:
        print (' ' + 9*'*' + '    **** **** **** **** ****')
        print(f' Cartela {i+1}: *  {str(game[i][0]).rjust(2)} * {str(game[i][1]).rjust(2)} * {str(game[i][2]).rjust(2)} * {str(game[i][3]).rjust(2)} * {str(game[i][4]).rjust(2)} *')
        print (' ' + 9*'*' + '    **** **** **** **** ****')

      else:
        print (13*' ' + f' {space1} {space2} {space3} {space4} {space5}')
        print(f' Cartela {i+1}:  | {str(game[i][0]).rjust(2)} | {str(game[i][1]).rjust(2)} | {str(game[i][2]).rjust(2)} | {str(game[i][3]).rjust(2)} | {str(game[i][4]).rjust(2)} |')
        print (13*' ' + f' {space1} {space2} {space3} {space4} {space5}')

#publishes winning message
def publish_win(winner):
  if winner == player_card:
    now = datetime.now()
    print('# PARABÉNS! VOCÊ VENCEU!!!')
    name = input('# Entre o seu nome para constar no rol de vencedores: _______________')
    with open('vencedores.txt','w') as vencedores:
      vencedores.write(name,now)
  else:
    print('\n# OUTRA CARTELA FOI COMPLETADA! \n# Melhor sorte na próxima vez!')

      
#draw next number
def draw_num():
  num = random.randint(1,50)
  print('\n'+68*'#')
  print(f'#                        NÚMERO SORTEADO: {num}                       #')
  print(68*'#'+'\n')
  return num

select_cards()
publish_game(game)
  
#ask player his option and check if any card wins
while not win:
  move = input('\n# SELECIONE OUTRA CARTELA (2, 3 ou 4) ou PRESSIONE ENTER PARA SORTEAR: ')
    
  if move == '2' or move == '3' or move == '4':
    player_card = (int(move) - 1)
    print('\n'+68*'#')
    print(f'#                 VOCÊ AGORA É DONO DA CARTELA {player_card + 1}                   #')
    print(68*'#'+'\n')
  else:
    num = draw_num()
    numbers_drawn.append(num)
    for i in range(len(game)):
      if int(game[i][0]) in numbers_drawn and int(game[i][1]) in numbers_drawn and int(game[i][2]) in numbers_drawn and int(game[i][3]) in numbers_drawn and int(game[i][4]) in numbers_drawn:
        winner = i
        win = True

  publish_game(game)

publish_win(winner)



  
  






