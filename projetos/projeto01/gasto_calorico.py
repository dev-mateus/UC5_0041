def calcula_gasto_calorico(atividade, tempo, peso):
    
    if atividade == 'caminhada':
        met = 3
    
    elif atividade == 'corrida': 
        met = 8.3
    
    elif atividade == 'ciclismo':
        met = 16
    
    else:
        print('atividade inválida')
        exit()
    
    gasto_calorico = met * peso * tempo / 60
    print(f'{gasto_calorico:.2f} cal')


