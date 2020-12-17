"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    a = float(input('Informe o primeiro lado: '))
    b = float(input('Informe o segundo lado: '))
    c = float(input('Informe o terceiro lado: '))

  
    
    if a >= b + c or b >= a + c or c >= a + b:
      n = 0
    else: 
      n = 1
    if n == 0:
      print('Os valores informados não formam um triângulo.')
    else:
      if a == b == c:
        print(f'O triângulo é equilátero.')
      elif a == b or b == c or a == c:
        print(f'O triângulo é isósceles.')
      else:
        print(f'O triângulo é escaleno.')



if __name__ == '__main__':
    main()
