import random
import numpy as np


class pessoas:
    def __init__(self, n):
        self.tamanho = int (n)
        self.individuo = self.pessoas (self.tamanho)

    def individuos(n):
        lista_comprimento = np.arange (10 * n)
        lista = lista_comprimento.reshape ((n, 10))
        lista = np.array (lista, dtype='object')

        hist = np.random.multinomial (int (n), [np.random.uniform (0.045, 0.081), np.random.uniform (0.135, 0.154),
                                                np.random.uniform (0.282, 0.296), np.random.uniform (0.271, 0.285),
                                                np.random.uniform (0.076, 0.102), np.random.uniform (0.036, 0.072),
                                                np.random.uniform (0.013, 0.067), np.random.uniform (0.015, 0.067)])
        for i in range (int (n)):
            # 1 atributo: rendimento mensal domiciliar per capita 5.1.1.1
            classes_c_valor = np.array (np.nonzero (hist))
            c = classes_c_valor.tolist ()
            d = c[0]
            escolha = d[random.randint (0, np.size (classes_c_valor) - 1)]
            if escolha == 0:
                lista[i, 0] = "0 _ 1/4 S.M."
                hist[escolha] -= 1
            elif escolha == 1:
                lista[i, 0] = "1/4 _ 1/2 S.M."
                hist[escolha] -= 1
            elif escolha == 2:
                lista[i, 0] = "1/2 _ 1 S.M"
                hist[escolha] -= 1
            elif escolha == 3:
                lista[i, 0] = "1 _ 2 S.M"
                hist[escolha] -= 1
            elif escolha == 4:
                lista[i, 0] = "2 _ 3 S.M"
                hist[escolha] -= 1
            elif escolha == 5:
                lista[i, 0] = "3 _ 5 S.M"
                hist[escolha] -= 1
            elif escolha == 6:
                lista[i, 0] = "5 _ + S.M"
                hist[escolha] -= 1
            elif escolha == 7:
                lista[i, 0] = "Sem declaração"
                hist[escolha] -= 1

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
        #     lista[i, 1] = 'Homem' if (rm.random() <= (np.random.normal(75403, 0.2) / 157967)) else 'Mulher'
        #
        # # 13 atributo: Cor
        #     lista[i, 2] = 'Branca' if (rm.random() <= (np.random.normal(48743,0.5) /80035)) else 'Preta ou Parda'

        # 14 atributo: Grupo de idade

        # 15 atributo: Anos de estudo

        # 16 atributo: Regiões
        #     if (rm.random() <= (np.random.normal(2770, 1.9) / 16871)):
        #         lista[i, 3] = 'Norte'
        #     elif (rm.random() <= (np.random.normal(5034, 1.5) / 16871)):
        #         lista[i, 3] = 'Nordeste'
        #     elif (rm.random() <= (np.random.normal(8901, 1.4) / 16871)):
        #         lista[i, 3] = 'Sudeste'
        #     elif (rm.random() <= (np.random.normal(12787, 1.4) / 16871)):
        #         lista[i, 3] = 'Sul'
        #     else:
        #         lista[i, 3] = 'Centro-Oeste'
        #
        print (lista)
        print(hist)


pessoas.individuos(10)
