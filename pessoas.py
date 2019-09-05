import random
import numpy as np


class pessoas:
    def __init__(self, n):
        self.tamanho = int (n)
        self.individuo = self.pessoas (self.tamanho)

    def individuos(n):
        lista_comprimento = np.arange(10 * n)
        lista = lista_comprimento.reshape((n, 10))
        lista = np.array(lista, dtype='object')

        #0 atributo
        hist0 = np.random.multinomial(int(n), [np.random.uniform(0.045, 0.081), np.random.uniform(0.135, 0.154),
                                                np.random.uniform(0.282, 0.296), np.random.uniform(0.271, 0.285),
                                                np.random.uniform(0.076, 0.102), np.random.uniform(0.036, 0.072),
                                                np.random.uniform(0.013, 0.067), np.random.uniform(0.015, 0.067)])
        #1 atributo
        hist1 = np.random.multinomial(int(n), [np.random.uniform(0.11,0.188), np.random.uniform(0.831,0.871)])

        #4 atributo
        hist4 = np.random.multinomial(int(n), [np.random.uniform(0.142, 0.180), np.random.uniform(0.122, 0.152),
                                                 np.random.uniform(0.215, 0.243), np.random.uniform(0.216, 0.244),
                                                 np.random.uniform(0.219, 0.265)])
        #5 atributo
        hist5 = np.random.multinomial(int(n), [np.random.uniform(0.43, 0.48), np.random.uniform(0.524, 0.566)])

        #6 atributo
        hist6 = np.random.multinomial(int(n), [np.random.uniform(0.42, 0.48), np.random.uniform(0.514, 0.558)])

        #7 atributo
        hist7 = np.random.multinomial(int(n), [np.random.uniform(0.154, 0.228), np.random.uniform(0.789, 0.829)])

        #8 atributo
        hist8 = np.random.multinomial(int(n), [np.random.uniform(0.927, 0.963), np.random.uniform(0.023, 0.087)])

        #9 atributo
        hist9 = np.random.multinomial(int(n), [np.random.uniform(0.199, 0.255), np.random.uniform(0.765, 0.781)])


        for i in range (int (n)):
            # 1 atributo: rendimento mensal domiciliar per capita 5.1.1.1
            classes_c_valor0 = np.array (np.nonzero (hist0))
            c0 = classes_c_valor0.tolist ()
            d0 = c0[0]
            escolha0 = d0[random.randint (0, np.size (classes_c_valor0) - 1)]
            if escolha0 == 0:
                lista[i, 0] = "0 - 1/4 S.M."
                hist0[escolha0] -= 1
            elif escolha0 == 1:
                lista[i, 0] = "1/4 - 1/2 S.M."
                hist0[escolha0] -= 1
            elif escolha0 == 2:
                lista[i, 0] = "1/2 - 1 S.M"
                hist0[escolha0] -= 1
            elif escolha0 == 3:
                lista[i, 0] = "1 - 2 S.M"
                hist0[escolha0] -= 1
            elif escolha0 == 4:
                lista[i, 0] = "2 - 3 S.M"
                hist0[escolha0] -= 1
            elif escolha0 == 5:
                lista[i, 0] = "3 - 5 S.M"
                hist0[escolha0] -= 1
            elif escolha0 == 6:
                lista[i, 0] = "5+ S.M"
                hist0[escolha0] -= 1
            elif escolha0 == 7:
                lista[i, 0] = "Sem declaração"
                hist0[escolha0] -= 1

        # 2 atributo: Vinculação ao PRONATEC 5.1.2.1

        # 3 atributo: Tempo de duração de qualificação profissional 5.1.2.1

        # 5 atributo: Turno 5.1.2.1

        # 6 atributo: Dificuldade financeira 5.1.3.1

        # 1 atributo: Dificuldade de acesso ao local do curso 5.1.3.1
            classes_c_valor1 = np.array(np.nonzero(hist1))
            c1 = classes_c_valor1.tolist ()
            d1 = c1[0]
            escolha1 = d1[random.randint (0, np.size (classes_c_valor1) - 1)]
            if escolha1 == 0:
                lista[i,1] = "Havia dificuldade $$"
                hist1[escolha1] -= 1
            else:
                lista[i,1] = "Não havia dificuldade $$"
                hist1[escolha1] -= 1



        # 8 atributo: Modalidade
            classes_c_valor8 = np.array(np.nonzero(hist8))
            c8 = classes_c_valor8.tolist()
            d8 = c8[0]
            escolha8 = d8[random.randint(0, np.size(classes_c_valor8) - 1)]
            if escolha8 == 0:
                lista[i, 8] = 'Presencial'
                hist8[escolha8] -= 1
            else:
                lista[i, 8] = 'A distancia'
                hist8[escolha8] -= 1

        # 9 atributo: Frquentaram ou nao o curso de qualificacao profissional
            classes_c_valor9 = np.array(np.nonzero(hist9))
            c9 = classes_c_valor9.tolist()
            d9 = c9[0]
            escolha9 = d9[random.randint(0, np.size(classes_c_valor9) - 1)]
            if escolha9 == 0:
                lista[i, 9] = "Frequentou"
                hist9[escolha9] -= 1
            else:
                lista[i, 9] = "Não frequentou"
                hist9[escolha9] -= 1


        # 10 atributo: Outras dificuldades para freguentar o curso de qualificação 5.1.3.1

        # 11 atributo: Não havia dificuldades para frequentar o curso de qualificação 5.1.3.1

        # 5 atributo: Sexo
            classes_c_valor5 = np.array(np.nonzero(hist5))
            c5= classes_c_valor5.tolist()
            d5 = c5[0]
            escolha5 = d5[random.randint(0, np.size(classes_c_valor5) - 1)]
            if escolha5 == 0:
                lista[i, 5] = 'Homem'
                hist5[escolha5] -= 1
            else:
                lista[i, 5] = 'Mulher'
                hist5[escolha5] -= 1

        # 7 atributo: Rede de ensino (Curso de qualificação profissional)
            classes_c_valor7 = np.array(np.nonzero(hist7))
            c7 = classes_c_valor7.tolist()
            d7 = c7[0]
            escolha7 = d7[random.randint(0, np.size(classes_c_valor7) - 1)]
            if escolha7 == 0:
                lista[i, 7] = 'Pública'
                hist7[escolha7] -= 1
            else:
                lista[i, 7] = 'Particular'
                hist7[escolha7] -= 1



        # # 13 atributo: Cor
            classes_c_valor6 = np.array (np.nonzero (hist6))
            c6 = classes_c_valor6.tolist ()
            d6 = c6[0]
            escolha6 = d6[random.randint (0, np.size (classes_c_valor6) - 1)]
            if escolha6 == 0:
                lista[i, 6] = 'Branco'
                hist6[escolha6] -= 1
            else:
                lista[i, 6] = 'Preto ou pardo'
                hist6[escolha6] -= 1

        # 14 atributo: Grupo de idade

        # 15 atributo: Anos de estudo

        # 4 atributo: Regiões
            classes_c_valor4 = np.array (np.nonzero (hist4))
            c4 = classes_c_valor4.tolist ()
            d4 = c4[0]
            escolha4 = d4[random.randint (0, np.size (classes_c_valor4) - 1)]


            if escolha4 == 0:
                lista[i, 4] = 'Norte'
                hist4[escolha4] -= 1
            elif escolha4 == 1:
                lista[i, 4] = 'Nordeste'
                hist4[escolha4] -= 1
            elif escolha4 == 2:
                lista[i, 4] = 'Sudeste'
                hist4[escolha4] -= 1
            elif escolha4 == 3:
                lista[i, 4] = 'Sul'
                hist4[escolha4] -= 1
            else:
                lista[i, 4] = 'Centro-Oeste'
                hist4[escolha4] -= 1
        #
        print(lista)
        print(hist0)
        print(hist1)
        print(hist4)
        print(hist5)
        print(hist6)
        print(hist7)
        print(hist8)
        print(hist9)

pessoas.individuos(10)
