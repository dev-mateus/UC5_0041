def calcula_frequencia_cardiaca(idade):
    max_frequencia_cardiaca = 220 - idade
    max_q_gordura = max_frequencia_cardiaca * 0.7
    min_q_gordura = max_frequencia_cardiaca * 0.5
    max_cardio = max_frequencia_cardiaca * 0.85
    min_cardio = max_frequencia_cardiaca * 0.7
    print(f'zona de queima de gordura: min {min_q_gordura:.0f} bpm - max {max_q_gordura:.0f} bpm')
    print(f'zona de cardio: min {min_cardio:.0f} bpm - max {max_cardio:.0f} bpm')