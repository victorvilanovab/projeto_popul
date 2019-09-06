import random
import numpy as np

class Pessoas:
    def __init__(self):
        #0 atributo (renda_per_capta_em_SM)
        escolha0 = np.nonzero(np.random.multinomial(1, [np.random.uniform(0.045, 0.081), np.random.uniform(0.135, 0.154),
                                                np.random.uniform(0.282, 0.296), np.random.uniform(0.271, 0.285),
                                                np.random.uniform(0.076, 0.102), np.random.uniform(0.036, 0.072),
                                                np.random.uniform(0.013, 0.067), np.random.uniform(0.015, 0.067)]))
        if escolha0 == 0:
            self.renda_per_capta_em_SM = "0-1/4"
        elif escolha0 == 1:
            self.renda_per_capta_em_SM = "1/4-1/2"
        elif escolha0 == 2:
            self.renda_per_capta_em_SM = "1/2-1"
        elif escolha0 == 3:
            self.renda_per_capta_em_SM = "1-2"
        elif escolha0 == 4:
            self.renda_per_capta_em_SM = "2-3"
        elif escolha0 == 5:
            self.renda_per_capta_em_SM = "3-5"
        elif escolha0 == 6:
            self.renda_per_capta_em_SM = "5+"
        elif escolha0 == 7:
            self.renda_per_capta_em_SM = "Sem_declaracao"
        #1 atributo (dificuldade_acesso)
        escolha1 = np.nonzero(np.random.multinomial(1, [np.random.uniform(0.11, 0.188), np.random.uniform(0.831, 0.871)]))
        if escolha1 == 0:
            self.dificuldade_acesso = "Havia"
        else:
            self.dificuldade_acesso = "Nao_havia"
        #2 atributo (regiao)
        escolha2 = np.nonzero(np.random.multinomial(1, [np.random.uniform(0.142, 0.180), np.random.uniform(0.122, 0.152),
                                               np.random.uniform(0.215, 0.243), np.random.uniform(0.216, 0.244),
                                               np.random.uniform(0.219, 0.265)]))
        if escolha2 == 0:
            self.regiao = 'Norte'
        elif escolha2 == 1:
            self.regiao = 'Nordeste'
        elif escolha2 == 2:
            self.regiao = 'Sudeste'
        elif escolha2 == 3:
            self.regiao = 'Sul'
        else:
            self.regiao = 'Centro-Oeste'
        #3 atributo (sexo)
        escolha3 = np.nonzero(np.random.multinomial(1, [np.random.uniform(0.43, 0.48), np.random.uniform(0.524, 0.566)]))
        if escolha3 == 0:
            self.sexo = 'Homem'
        else:
            self.sexo = 'Mulher'
        #4 atributo (cor)
        escolha4 = np.nonzero(np.random.multinomial(1, [np.random.uniform(0.42, 0.48), np.random.uniform(0.514, 0.558)]))
        if escolha4 == 0:
            self.cor = 'Branca'
        else:
            self.cor = 'Preta/parda'
        #5 atributo (instituicao_tipo)
        escolha5 = np.nonzero(np.random.multinomial(1, [np.random.uniform(0.154, 0.228), np.random.uniform(0.789, 0.829)]))
        if escolha5 == 0:
            self.instituicao_tipo = 'Publica'
        else:
            self.instituicao_tipo = 'Particular'
        #6 atributo (graduacao_tipo)
        escolha6 = np.nonzero(np.random.multinomial(1, [np.random.uniform(0.927, 0.963), np.random.uniform(0.023, 0.087)]))
        if escolha6 == 0:
            self.graduacao_tipo = "Presencial"
        else:
            self.graduacao_tipo = "A_distancia"
        #7 atributo (frequentou_curso_profissional)
        escolha7 = np.nonzero(np.random.multinomial(1, [np.random.uniform(0.199, 0.255), np.random.uniform(0.765, 0.781)]))
        if escolha7 == 0:
            self.frequentou_curso_profissional = "Frequentou"
        else:
            self.frequentou_curso_profissional = "Nao_frequentou"


class Populacao:
    def __init__(self, n):
        self.tamanho = int (n)
        self.individuo = []
        self.amostra(self.tamanho)

    def amostra(self, tamanho):
        for i in range(tamanho):
            self.individuo.append(Pessoas())
        return self.individuo
