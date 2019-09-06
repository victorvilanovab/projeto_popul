# projeto_popul
Repositorio para correção do projeto
Alunos: Victor Vilanova e Alexandre Garriga
Foi desenvolvido com os dados da PNAD_2014
E foi feito com a sub amostra de pessoas com 15 anos ou mais de idade que freguentavam curso de qualificação profissional.

Expicação do código:

fizemos o uso da função [np.random.multinomial] que retorna uma espécie de histograma
(ela recebe 2 entradas: a quantidade de 'jogos' que queremos e uma lista de probabilidades).
Nesse sentido, a fim de tornar nosso trabalho mais realista, foi usada a função [np.random.uniform] para as probabilidades
(Que retorna um valor dentre dois intervalos), assim, usamos o coeficiente de variação, para obter os
intervalos gerando uma possível margem de erro.
Sendo assim, o resto foi gerar as pessoas de acordo com os 'histogramas' criados.

