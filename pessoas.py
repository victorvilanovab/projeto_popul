import random as rm
import numpy as np

class pessoas:
    def __init__(self, n):
        self.pessoa=[]
    for i in range(n):
        #  1 atributo: rendimento mensal domiciliar 5.1.1.1

        # 2 atributo: Vinculação ao PRONATEC 5.1.2.1

        # 3 atributo: Tempo de duração de qualificação profissional 5.1.2.1

        # 4 atributo: Modalidade 5.1.2.1

        # 5 atributo: Turno 5.1.2.1

        # 6 atributo: Dificuldade financeira 5.1.3.1

        # 7 atributo: Dificuldade de acesso ao local do curso 5.1.3.1

        # 8 atributo: Dificuldade de cumprir o horário do curso 5.1.3.1

        # 9 atributo: Falta de tempo para estudar 5.1.3.1

        # 10 atributo: Outras dificuldades para freguentar o curso de qualificação 5.1.3.1

        # 11 atributo: Não havia dificuldades para frequentar o curso de qualificação 5.1.3.1

        # 12 atributo: Sexo
        lista[i, 1] = 'Homem' if (rm.random() <= (np.random.normal(75403, 0.2) / 157967)) else 'Mulher'

        # 13 atributo: Cor
        lista[i, 2] = 'Branca' if (rm.random() <= (np.random.normal(48743,0.5) /80035)) else 'Preta ou Parda'

        # 14 atributo: Grupo de idade

        # 15 atributo: Anos de estudo

        # 16 atributo: Regiões
        if (rm.random() <= (np.random.normal(2770, 1.9) / 16871)):
            lista[i, 0] = 'Norte'
        elif (rm.random() <= (np.random.normal(5034, 1.5) / 16871)):
            lista[i, 0] = 'Nordeste'
        elif (rm.random() <= (np.random.normal(8901, 1.4) / 16871)):
            lista[i, 0] = 'Sudeste'
        elif (rm.random() <= (np.random.normal(12787, 1.4) / 16871)):
            lista[i, 0] = 'Sul'
        else:
            lista[i, 0] = 'Centro-Oeste'