def verifica_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-','')
    digito_um = False
    digito_dois = False
    if cpf.isdigit() and len(cpf) == 11:
        j = 10
        soma_um = 0
        for i in range(0, 9):
            soma_um += int(cpf[i]) * j
            j -= 1
        resto_um = soma_um % 11
        if resto_um < 2:
            if int(cpf[9]) == 0:
                digito_um = True
            else:
                digito_um = False
        else:
            if int(cpf[9]) == (11 - resto_um):
                digito_um = True
            else:
                digito_um = False
        # se o primeiro digito for valido, verifica o segundo digito
        if digito_um:
            soma_dois = 0
            m = 11
            for k in range(0, 10):
                soma_dois += int(cpf[k]) * m
                m -= 1
            resto_dois = soma_dois % 11
            if resto_dois < 2:
                if int(cpf[10]) == 0:
                    digito_dois = True
                else:
                    digito_dois = False
            else:
                if int(cpf[10]) == 11 - resto_dois:
                    digito_dois = True
                else:
                    digito_dois = False
    if digito_um and digito_dois and cpf.isdigit() and len(cpf) == 11:
        print('CPF válido!')
    else:
        print('CPF inválido!')

verifica_cpf('082.955.076-30')