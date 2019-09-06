import random
import numpy as np


class pessoas:
    def __init__(self, n):
        self.tamanho = int (n)
        self.individuo = self.pessoas (self.tamanho)

    def individuos(n):
        lista_comprimento = np.arange(8 * n)
        lista = lista_comprimento.reshape((n, 8))
        lista = np.array(lista, dtype='object')

        #0 atributo
        hist0 = np.random.multinomial(int(n), [np.random.uniform(0.045, 0.081), np.random.uniform(0.135, 0.154),
                                                np.random.uniform(0.282, 0.296), np.random.uniform(0.271, 0.285),
                                                np.random.uniform(0.076, 0.102), np.random.uniform(0.036, 0.072),
                                                np.random.uniform(0.013, 0.067), np.random.uniform(0.015, 0.067)])
        #1 atributo
        hist1 = np.random.multinomial(int(n), [np.random.uniform(0.11,0.188), np.random.uniform(0.831,0.871)])

        #2 atributo
        hist2 = np.random.multinomial(int(n), [np.random.uniform(0.142, 0.180), np.random.uniform(0.122, 0.152),
                                                 np.random.uniform(0.215, 0.243), np.random.uniform(0.216, 0.244),
                                                 np.random.uniform(0.219, 0.265)])
        #3 atributo
        hist3 = np.random.multinomial(int(n), [np.random.uniform(0.43, 0.48), np.random.uniform(0.524, 0.566)])

        #4 atributo
        hist4 = np.random.multinomial(int(n), [np.random.uniform(0.42, 0.48), np.random.uniform(0.514, 0.558)])

        #5 atributo
        hist5 = np.random.multinomial(int(n), [np.random.uniform(0.154, 0.228), np.random.uniform(0.789, 0.829)])

        #6 atributo
        hist6 = np.random.multinomial(int(n), [np.random.uniform(0.927, 0.963), np.random.uniform(0.023, 0.087)])

        #7 atributo
        hist7 = np.random.multinomial(int(n), [np.random.uniform(0.199, 0.255), np.random.uniform(0.765, 0.781)])


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

        # 2 atributo: Dificuldade de acesso ao local do curso 5.1.3.1
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



        #6 atributo: Modalidade
            classes_c_valor6 = np.array(np.nonzero(hist6))
            c6 = classes_c_valor6.tolist()
            d6 = c6[0]
            escolha6 = d6[random.randint(0, np.size(classes_c_valor6) - 1)]
            if escolha6 == 0:
                lista[i, 6] = 'Presencial'
                hist6[escolha6] -= 1
            else:
                lista[i, 6] = 'A distancia'
                hist6[escolha6] -= 1

        #7 atributo: Frquentaram ou nao o curso de qualificacao profissional
            classes_c_valor7 = np.array(np.nonzero(hist7))
            c7 = classes_c_valor7.tolist()
            d7 = c7[0]
            escolha7 = d7[random.randint(0, np.size(classes_c_valor7) - 1)]
            if escolha7 == 0:
                lista[i, 7] = "Frequentou"
                hist7[escolha7] -= 1
            else:
                lista[i, 7] = "Não frequentou"
                hist7[escolha7] -= 1


        #3 atributo: Sexo
            classes_c_valor3 = np.array(np.nonzero(hist3))
            c3= classes_c_valor3.tolist()
            d3 = c3[0]
            escolha3 = d3[random.randint(0, np.size(classes_c_valor3) - 1)]
            if escolha3 == 0:
                lista[i, 3] = 'Homem'
                hist3[escolha3] -= 1
            else:
                lista[i, 3] = 'Mulher'
                hist3[escolha3] -= 1

        # 7 atributo: Rede de ensino (Curso de qualificação profissional)
            classes_c_valor5 = np.array(np.nonzero(hist5))
            c5 = classes_c_valor5.tolist()
            d5 = c5[0]
            escolha5 = d5[random.randint(0, np.size(classes_c_valor5) - 1)]
            if escolha5 == 0:
                lista[i, 5] = 'Pública'
                hist5[escolha5] -= 1
            else:
                lista[i, 5] = 'Particular'
                hist5[escolha5] -= 1



        #4 atributo: Cor
            classes_c_valor4 = np.array (np.nonzero (hist4))
            c4 = classes_c_valor4.tolist ()
            d4 = c4[0]
            escolha4 = d4[random.randint (0, np.size (classes_c_valor4) - 1)]
            if escolha4 == 0:
                lista[i, 4] = 'Branco'
                hist4[escolha4] -= 1
            else:
                lista[i, 4] = 'Preto ou pardo'
                hist4[escolha4] -= 1

        #2 atributo: Regiões
            classes_c_valor2 = np.array (np.nonzero (hist2))
            c2 = classes_c_valor2.tolist ()
            d2 = c2[0]
            escolha2 = d2[random.randint (0, np.size (classes_c_valor2) - 1)]
            if escolha2 == 0:
                lista[i, 2] = 'Norte'
                hist2[escolha2] -= 1
            elif escolha2 == 1:
                lista[i, 2] = 'Nordeste'
                hist2[escolha2] -= 1
            elif escolha2 == 2:
                lista[i, 2] = 'Sudeste'
                hist2[escolha2] -= 1
            elif escolha2 == 3:
                lista[i, 2] = 'Sul'
                hist2[escolha2] -= 1
            else:
                lista[i, 2] = 'Centro-Oeste'
                hist2[escolha2] -= 1

        return lista


