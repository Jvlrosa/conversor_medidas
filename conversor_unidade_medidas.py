
verde = "\033[32m"

reset = "\033[0m"

print('\nDIGITE APENAS O NUMERO DA CONVERSÃO QUE DESEJA SOLUCIONAR!!!')

opcao = input('\n- QUAL UNIDADE DE MEDIDA DESEJA TRANSFORMAR?\n1 - Metros para Quilômetros\n2 - Quilogramas para Gramas\n3 - L6itros para Mililitros\n4 - Horas para Minutos\n5 - Minutos para Segundos\n6 - Jardas para Metros\n7 - ilhas para Quilômetros\n8 - Pés para Metros\n9 - Polegadas para Centímetros\n10 - Celsius para Fahrenheit\n\nESCOLHA SUA OPÇÃO: ')

if opcao == '1':
    metros = int(input('DIGITE UM VALOR EM METROS: '))
    print(f'{verde}O valor em Quilômetros é: {metros / 1000}{reset}')
elif opcao == '2':
    quilos = int(input('DIGITE UM VALOR EM QUILÔMETROS: '))
    print(f'{verde}O valor em Gramas é: {quilos * 1000}{reset}')
elif opcao == '3':
    litros = int(input('DIGITE UM VALOR EM LITROS: '))
    print(f'{verde}O valor em Mililitros é: {litros * 1000}{reset}')
elif opcao == '4':
    horas = int(input('DIGITE UM VALOR EM HORAS: '))
    print(f'{verde}O valor em Minutos é: {horas * 60}{reset}')
elif opcao == '5':
    minutos = int(input('DIGITE UM VALOR EM MINUTOS: '))
    print(f'{verde}O valor em Segundos é: {minutos * 60}{reset}')
elif opcao == '6':
    jardas = int(input('DIGITE UM VALOR EM JARDAS: '))
    print(f'{verde}O valor em Metros é: {jardas * 0.91}{reset}')
elif opcao == '7':
    ilhas = int(input('DIGITE UM VALOR EM ILHAS: '))
    print(f'{verde}O valor em Quilômetros é: {ilhas * 10000}{reset}')
elif opcao == '8':
    pés = int(input('DIGITE UM VALOR EM PÉS: '))
    print(f'{verde}O valor em Metros é: {pés * 0.3048}{reset}')
elif opcao == '9': 
    polegadas = int(input('DIGITE UM VALOR EM POLEGADAS: '))
    print(f'{verde}O valor em Centímetros é: {polegadas * 2.54}{reset}')
else:
    celsius = int(input('DIGITE UM VALOR EM CELSIUS: '))
    print(f'{verde}O valor em Fahrenheit é: {celsius * 1.8 + 32}{reset}{reset}')
