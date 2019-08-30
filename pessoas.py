import random as rm
import numpy as np

class pessoas:
    def __init__(self, n):
        self.tamanho=int(n)
        self.individuo=self.pessoas(self.tamanho)

    def pessoas(self, n):
        lista = np.chararray((int(n), 16), itemsize=15)
        for i in range(int(n)):

            #  1 atributo: rendimento mensal domiciliar 5.1.1.1
            if rm.random() <= np.random.normal(14908, 1.3)/157626:
                lista[i,0]='até 1 S.M.'
            elif rm.random() <= np.random.normal(45027, 0.8)/157626:
                lista[i,0]='1 a 2 S.M.'
            elif rm.random() <= np.random.normal(73020, 0.8)/157626:
                lista[i,0]='2 a 3 S.M.'
            elif rm.random() <= np.random.normal(109111, 0.7)/157626:
                lista[i,0]='3 a 5 S.M."'
            elif rm.random() <= np.random.normal(138220, 0.9)/157626:
                lista[i,0]='5 a 10 S.M.'
            elif rm.random() <= np.random.normal(147771, 1.9)/157626:
                lista[i,0]='10 a 20 S.M.'
            elif rm.random() <= np.random.normal(151181, 3.7)/157626:
                lista[i,0]='Mais de 20 S.M.'
            else:
                lista[i,0]='Sem declaração'


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

        # 13 atributo: Cor

        # 14 atributo: Grupo de idade

        # 15 atributo: Anos de estudo

        # 16 atributo: Regiões
