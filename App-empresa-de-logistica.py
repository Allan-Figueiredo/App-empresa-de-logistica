def rotaObjeto ():
    while True:
      rotaObjeto = input('⦁ Escolha a rota desejada:\nrs - De Rio de Janeiro até São Paulo\nsr - De São Paulo até Rio de Janeiro\nbs - De Brasília até São Paulo\nsb - De São Paulo até Brasília\nbr - De Brasília até Rio de Janeiro\nrb - Rio de Janeiro até Brasília\n >> ')
      if rotaObjeto == 'rs':
        return 1
      elif rotaObjeto =='sr':
        return 1
      elif rotaObjeto == 'bs':
        return 1.2
      elif rotaObjeto == 'sb':
        return 1.2
      elif rotaObjeto == 'br':
        return 1.5
      elif rotaObjeto == 'rb':
        return 1.5
      else:
          print('Por favor digite o valor corretamente')
      continue
def dimensoesObejto ():

    while True:
        try:
            altura = int(input('⦁ Qual a altura ? (em cm) '))
            comprimento = int(input('⦁ Qual o comprimento ? (em cm) '))
            largura = int(input('⦁ Qual a largura ? (em cm) '))
            dimensoesObejto = altura * largura * comprimento
            if dimensoesObejto < 1000:
                return 10
            elif (dimensoesObejto > 1001) and (dimensoesObejto <= 10000):
                return 20
            elif (dimensoesObejto > 10000) and (dimensoesObejto <= 30000):
                return 30
            elif (dimensoesObejto > 30000) and (dimensoesObejto <= 100000):
                return 50
            else:
                print('Dimensão não aceita')
            continue
        except ValueError:
            print('Pare de digitar valores não numéricos. tente novamente ')
            continue
def pesoObejto():
    while True:
        try:
            pesoObejto = float(input('Qual o peso do objeto ?'))
            if pesoObejto < 0.1:
                return 1
            elif (pesoObejto > 0.11) and (pesoObejto <= 1):
                return 1.5
            elif (pesoObejto > 1.10) and (pesoObejto <= 10):
                return 2
            elif (pesoObejto > 10.1) and (pesoObejto <= 30):
                return 3
            else:
                print (' Peso de objeto não aceito')
            continue
        except ValueError:
               print('Pare de digitar valores não numéricos. tente novamente ')



print('Bem-vindo a empresa de logística Allan Figueiredo')
rota = rotaObjeto()
dimensao = dimensoesObejto()
peso = pesoObejto()
total = rota * dimensao * peso
print(' O valor total do serviço foi de R${:.2f}'.format(total))
