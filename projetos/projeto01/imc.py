def calcula_imc(peso, altura):
     
    if isinstance(peso, str):
        peso_limpo = ''
        peso = peso.replace(',', '.')
        for i in peso:
            if i.isdigit() or i == '.':
                peso_limpo += i
        try:
            peso = float(peso_limpo)
        except ValueError:
            print('peso inválido!')
            exit()
    
    if isinstance(altura, str):
        altura_limpo = ''
        altura = altura.replace(',', '.')
        for i in altura:
            if i.isdigit() or i == '.':
                altura_limpo += i
        try:
            altura = float(altura_limpo)
        except ValueError:
            print('altura inválida!')
            exit()

    resultado = peso / altura ** 2
    print(f'{resultado:.2f}')