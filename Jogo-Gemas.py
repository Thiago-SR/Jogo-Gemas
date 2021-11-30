import random
import copy
import os
import time

def criar_matriz(p1,p2):
    for l in range(parametro1):
        linha = []
        for c in range(parametro2):
            n = random.choice(letras)
            linha.append(n)
        jogo.append(linha)
    return jogo

def fim_dicas(jg,p1,p2):
    teste = copy.deepcopy(jg)
    dica = []
#================== PERMUTAÇÕES DE TESTE NAS LINHAS =======================
    for l in range(p1):
        for c in range(p2):
            if l != p1 -1:
                w = teste[l+1][c]
                teste[l+1][c] = teste[l][c]
                teste[l][c]= w
                for p in range(p1):
                    anterior = ''
                    pontuacao = 0
                    for q in range(p2):

                        if (teste[p][q] == anterior):
                            pontuacao += 1
                        else:
                            pontuacao = 0
                        if pontuacao >= 2:
                            dica.append((l, c))
                            dica.append((l + 1, c))
                            return 1, dica
                        anterior = teste[p][q]
                for q in range(p2):
                    pontuacao = 0
                    anterior = ''
                    for p in range(p1):
                        if (teste[p][q] == anterior):
                            pontuacao += 1

                        else:
                            pontuacao = 0
                        if pontuacao >= 2:
                            dica.append((l, c))
                            dica.append((l + 1, c))
                            return 1, dica
                        anterior = teste[p][q]
                teste[l][c] = teste[l + 1][c]
                teste[l + 1][c] = w
#================== PERMUTAÇÕES DE TESTE NAS COLUNAS  =======================
    for c in range(p2):
        for l in range(p1):
            if c != p2-1:
                w = teste[l][c+1]
                teste[l][c+1] = teste[l][c]
                teste[l][c]= w
                for p in range(p1):
                    anterior = ''
                    pontuacao = 0
                    for q in range(p2):

                        if (teste[p][q] == anterior):
                            pontuacao += 1
                        else:
                            pontuacao = 0
                        if pontuacao >= 2:
                            dica.append((l, c))
                            dica.append((l + 1, c))
                            return 1, dica
                        anterior = teste[p][q]
                for q in range(p2):
                    pontuacao = 0
                    anterior = ''
                    for p in range(p1):
                        if (teste[p][q] == anterior):
                            pontuacao += 1

                        else:
                            pontuacao = 0
                        if pontuacao >= 2:
                            dica.append((l, c))
                            dica.append((l + 1, c))
                            return 1, dica
                        anterior = teste[p][q]
                teste[l][c] = teste[l][c+1]
                teste[l][c+1] = w
    if len(dica)==0:
        return 0

def exibir(jg, p1, p2):
    for c in range(p2):
        print('   ', c, end='  ')
    print()
    for l in range(0, p1):
        print(f'{l} ', end='')
        for c in range(p2):
            print(jg[l][c], end='  ')
        print()
        print()

def pontos(jg, p1, p2,pt):
    for l in range(p1):
        for c in range(p2):
            if jg[l][c] == '     ':
                pt += 1
    return pt

def repor_itens(jg, p1, p2, lt):
    for i in range(p1 + p2):
        for l in range(p1):
            for c in range(p2):
                if jg[l][c] == '     ':
                    if l == 0:
                        jg[l][c] = random.choice(lt)
                    else:
                        jg[l][c] = jg[l - 1][c]
                        jg[l - 1][c] = '     '
    return jg

def cadeias(jg, p1, p2, pt, lt):
    pt = 0
    for g in range(p1):
        for i in range(p1*p2):
            pt_temporario = 0
            for l in range(p1):
                posicoes = []
                pontuacao = 0
                anterior = ''
                for c in range(p2):

                    if (jg[l][c] == anterior):
                        posicoes.append(c)
                        posicoes.append(c - 1)
                        pontuacao += 1

                    else:
                        pontuacao = 0
                        posicoes = []
                    anterior = jg[l][c]

                    if pontuacao >= 2:
                        exibir(jg,p1,p2)
                        time.sleep(2)
                        os.system('cls')
                        for i in posicoes:
                            jg[l][i] = '     '
                        exibir(jg, p1, p2)
                        time.sleep(1)
                        os.system('cls')
            pt_temporario = pontos(jg, p1, p2, pt_temporario)
            pt += pt_temporario
            pt_temporario = 0
            jg = repor_itens(jg, p1, p2, lt)

        for i in range(p1*p2):
            pt_temporario = 0
            for c in range(p2):
                posicoes = []
                pontuacao = 0
                anterior = ''
                for l in range(p1):
                    if (jg[l][c] == anterior):
                        posicoes.append(l)
                        posicoes.append(l - 1)
                        pontuacao += 1

                    else:
                        pontuacao = 0
                        posicoes = []

                    anterior = jg[l][c]
                    if pontuacao >= 2:
                        exibir(jg, p1, p2)
                        time.sleep(2)
                        os.system('cls')
                        for i in posicoes:
                            jg[i][c] = '     '
                        exibir(jg, p1, p2)
                        time.sleep(1)
                        os.system('cls')


            pt_temporario = pontos(jg, p1, p2, pt_temporario)
            pt += pt_temporario
            pt_temporario = 0
            jg = repor_itens(jg, p1, p2, lt)

    return jg, pt

def verificar_cadeia(jg,p1,p2,n1,n2,n3,n4):
    if n1 == n3:
        anterior = ''
        pontuacao = 0
        for c in range(p2):#VERIFICAR SE APERMUTAÇÃO FORMOU CADEIA NA LINHA
            if jg[n1][c] == anterior:
                pontuacao+= 1
            else:
                pontuacao = 0
            if pontuacao >=2:
                return True
            anterior = jg[n1][c]
        anterior = ''
        pontuacao = 0
        for l in range(p1):# VERIFICAR SE A PERMUTAÇÃO FORMOU CADEIA NA COLUNA N2
            if jg[l][n2]== anterior:
                pontuacao +=1
            else:
                pontuacao = 0
            if pontuacao>=2:
                return True
            anterior = jg[l][n2]

        for l in range(p1):# VERIFICAR SE A PERMUTAÇÃO FORMOU CADEIA NA COLUNA N4
            if jg[l][n4]== anterior:
                pontuacao +=1
            else:
                pontuacao = 0
            if pontuacao>=2:
                return True
            anterior = jg[l][n4]
    elif n2 ==n4:
        anterior = ''
        pontuacao = 0
        for l in range(p1):  # VERIFICAR SE A PERMUTAÇÃO FORMOU CADEIA NA COLUNA N2
            if jg[l][n2] == anterior:
                pontuacao += 1
            else:
                pontuacao = 0
            if pontuacao >= 2:
                return True
            anterior = jg[l][n2]

        anterior = ''
        pontuacao = 0
        for c in range(p2):  # VERIFICAR SE APERMUTAÇÃO FORMOU CADEIA NA LINHA N1
            if jg[n1][c] == anterior:
                pontuacao += 1
            else:
                pontuacao = 0
            if pontuacao >= 2:
                return True
            anterior = jg[n1][c]

        anterior = ''
        pontuacao = 0
        for c in range(p2):  # VERIFICAR SE APERMUTAÇÃO FORMOU CADEIA NA LINHA N3
            if jg[n3][c] == anterior:
                pontuacao += 1
            else:
                pontuacao = 0
            if pontuacao >= 2:
                return True
            anterior = jg[n3][c]
    return False

a = '\033[0;31;41m  a  \033[m'# VERMELHO
b = '\033[0;32;42m  b  \033[m'#VERDE
c = '\033[0;33;43m  c  \033[m'#AMARELO
d = '\033[0;34;44m  d  \033[m'#AZUL
e = '\033[0;35;45m  e  \033[m'#ROSA
letras = [a, b, c, d, e]# CORES DAS GEMAS
dicas = []# VARIAVEL PARA ARMAZENAR AS POSIÇÕES DAS DICAS
pontuacao = 0 # VARIÁVEL PARA ARMAZENAR A PONTUAÇÃO DO JOGADOR

print('=' * 35)
print('- Defina os tamanho da área do jogo. ')
print('- O jogo deve ser no mínimo 3 x 3, e no máximo 10 x 10.')
print('=' * 35)
parametro1 = 0
parametro2 = 0
jogo = []
while (3 > parametro1 or parametro1 > 10) or (3 > parametro2 or parametro2 > 10):
    parametro1 = int(input('Quantas linhas você deseja que o jogo tenha? '))
    parametro2 = int(input('Quantas colunas você deseja que o jogo tenha? '))
    if (3 > parametro1 or parametro1 > 10) or (3 > parametro2 or parametro2 > 10):
        print('=' * 35)
        print('\033[0;30;41mTamanho do jogo inválido!\033[m')
        print('=' * 35)

os.system('cls')

jogo = criar_matriz(parametro1,parametro2)# CRIAR A MATRIZ DO JOGO
comecar = fim_dicas(jogo,parametro1,parametro2)

while len(comecar)==1:# GARANTIR QUE O JOGO NÃO VAI DAR GAME OVER SEM O JOGADOR TER JOGADO
    jogo = criar_matriz(parametro1,parametro2)
jogo = cadeias(jogo, parametro1, parametro2, pontuacao, letras)[0]# VERIFICAR SE A MATRIZ JÁ FOI CRIADA COM CADEIAS FORMADAS

while True:
    entrada_certa = 'n'# VARIAVEL DE CONTROLE DE ENTRADA DAS GEMAS QUE SERÃO PERMUTADAS
    fim_jogo = fim_dicas(jogo, parametro1, parametro2)#FUNÇÃO PARA BUSCAR A DICA E IDENTIFICAR O FIM DO JOGO
    fim_jogo = list(fim_jogo)
    if len(fim_jogo) == 1 :# IDENTIFICAR O FIM DO JOGO
        print('\033[0;30;41mGAME OVER\033[m')
        print('\033[0;30;41mPONTUAÇÃO FINAL: {}\033[m'.format(pontuacao))
        break
    else:
        dicas = fim_jogo[1]

    while entrada_certa == 'n':
        exibir(jogo,parametro1,parametro2)#EXIBIR A MATRIZ DO JOGO
        print('''        \033[0;34;40m-- DICA : PRESS (D) -----------\033[m
        \033[0;34;40m-- SAIR : PRESS (S) -----------\033[m
        \033[0;34;40m-- CONTINUAR : PRESS (ENTER) --\033[m''')
        menu = input().upper()
        if menu == 'D':
            os.system('cls')
            pontuacao-=1
            print('POSIÇÕES: {} / {}'.format(dicas[0], dicas[1]))# EXIBIR A DICA
        elif menu == 'S':# ENCERRAR O JOGO
            break
        elif menu == '':
            try:
                print('=' * 30)
                print('PONTOS:', pontuacao)
                print('=' * 30)
                print('Qual a primeira posição? ')
                print('=' * 30)
                n1 = int(input('linha: '))
                print('=' * 30)
                n2 = int(input('coluna: '))
                print('=' * 30)
                print('Para qual posição? ')
                print('=' * 30)
                n3 = int(input('linha: '))
                print('=' * 30)
                n4 = int(input('coluna: '))
                print('=' * 30)
        #============ VERIFICAR SE A PERMUTAÇÃO É VALIDA E SE A POSIÇÃO DIGITADA EXISTE =====================
                if (n1 == len(jogo)-1) and (n2 == 0) :# se for o canto inferior esquerdo
                    if (n3 == n1-1 and n4 == n2) or (n4 == n2+1 and n3 == n1):
                        entrada_certa = 's'
                        t = jogo[n1][n2]
                        jogo[n1][n2] = jogo[n3][n4]
                        jogo[n3][n4] = t
                        verificador = verificar_cadeia(jogo,parametro1,parametro2,n1,n2,n3,n4)
                        if verificador == False:
                            print('\033[0;30;41mMOVIMENTO INVÁLIDO!!!\033[m')
                            t = jogo[n1][n2]
                            jogo[n1][n2] = jogo[n3][n4]
                            jogo[n3][n4] = t
                            time.sleep(5)
                    else:
                        print('\033[0;30;41m As gemas que serão permutadas devem ser adjacentes!\033[m')
                        time.sleep(5)
                elif (n1 == len(jogo)-1) and (n2 == len(jogo[0])-1) : # se for o canto infeior direito
                    if  (n3 == n1-1 and n4 == n2) or (n4 == n2-1 and n3 == n1):
                        entrada_certa = 's'
                        t = jogo[n1][n2]
                        jogo[n1][n2] = jogo[n3][n4]
                        jogo[n3][n4] = t
                        verificador = verificar_cadeia(jogo, parametro1, parametro2, n1, n2, n3, n4)
                        if verificador == False:
                            print('\033[0;30;41mMOVIMENTO INVÁLIDO!!!\033[m')
                            t = jogo[n1][n2]
                            jogo[n1][n2] = jogo[n3][n4]
                            jogo[n3][n4] = t
                            time.sleep(5)
                    else:
                        print('\033[0;30;41m As gemas que serão permutadas devem ser adjacentes!\033[m')
                        time.sleep(5)
                elif (n1 == 0) and (n2 == 0): #canto superior esquerdo
                    if (n3 == n1+1 and n4 == n2) or (n4 == n2+1 and n3 == n1):
                        entrada_certa = 's'
                        t = jogo[n1][n2]
                        jogo[n1][n2] = jogo[n3][n4]
                        jogo[n3][n4] = t
                        verificador = verificar_cadeia(jogo, parametro1, parametro2, n1, n2, n3, n4)
                        if verificador == False:
                            print('\033[0;30;41mMOVIMENTO INVÁLIDO!!!\033[m')
                            t = jogo[n1][n2]
                            jogo[n1][n2] = jogo[n3][n4]
                            jogo[n3][n4] = t
                            time.sleep(5)
                    else:
                        print('\033[0;30;41m As gemas que serão permutadas devem ser adjacentes!\033[m')
                        time.sleep(5)
                elif (n1 == 0) and (n2 == len(jogo[0])-1):#canto superior direito
                    if (n3 == n1+1 and n4 == n2) or (n4 == n2-1 and n3 == n1):
                        entrada_certa = 's'
                        t = jogo[n1][n2]
                        jogo[n1][n2] = jogo[n3][n4]
                        jogo[n3][n4] = t
                        verificador = verificar_cadeia(jogo, parametro1, parametro2, n1, n2, n3, n4)
                        if verificador == False:
                            print('\033[0;30;41mMOVIMENTO INVÁLIDO!!!\033[m')
                            t = jogo[n1][n2]
                            jogo[n1][n2] = jogo[n3][n4]
                            jogo[n3][n4] = t
                            time.sleep(5)
                    else:
                        print('\033[0;30;41m As gemas que serão permutadas devem ser adjacentes!\033[m')
                        time.sleep(5)
                elif (n1 == 0): # se for da primeira linha
                    if (n3 == n1+1 and n4 == n2) or (n4 == n2+1 and n3 == n1) or (n4 == n2-1 and n3 == n1):
                        entrada_certa = 's'
                        t = jogo[n1][n2]
                        jogo[n1][n2] = jogo[n3][n4]
                        jogo[n3][n4] = t
                        verificador = verificar_cadeia(jogo, parametro1, parametro2, n1, n2, n3, n4)
                        if verificador == False:
                            print('\033[0;30;41mMOVIMENTO INVÁLIDO!!!\033[m')
                            t = jogo[n1][n2]
                            jogo[n1][n2] = jogo[n3][n4]
                            jogo[n3][n4] = t
                            time.sleep(5)
                    else:
                        print('\033[0;30;41m As gemas que serão permutadas devem ser adjacentes!\033[m')
                        time.sleep(5)
                elif (n1 == len(jogo)-1):# se for da ultima linha
                    if(n3 == n1-1 and n4 == n2) or (n4 == n2+1 and n3 == n1) or (n4 == n2-1 and n3 == n1):
                        entrada_certa = 's'
                        t = jogo[n1][n2]
                        jogo[n1][n2] = jogo[n3][n4]
                        jogo[n3][n4] = t
                        verificador = verificar_cadeia(jogo, parametro1, parametro2, n1, n2, n3, n4)
                        if verificador == False:
                            print('\033[0;30;41mMOVIMENTO INVÁLIDO!!!\033[m')
                            t = jogo[n1][n2]
                            jogo[n1][n2] = jogo[n3][n4]
                            jogo[n3][n4] = t
                            time.sleep(5)
                    else:
                        print('\033[0;30;41m As gemas que serão permutadas devem ser adjacentes!\033[m')
                        time.sleep(5)
                elif (n2 == 0): # se for da primeira coluna
                    if (n3 == n1+1 and n4 == n2) or (n3 == n1-1 and n4 == n2) or (n4 == n2+1 and n3 == n1):
                        entrada_certa = 's'
                        t = jogo[n1][n2]
                        jogo[n1][n2] = jogo[n3][n4]
                        jogo[n3][n4] = t
                        verificador = verificar_cadeia(jogo, parametro1, parametro2, n1, n2, n3, n4)
                        if verificador == False:
                            print('\033[0;30;41mMOVIMENTO INVÁLIDO!!!\033[m')
                            t = jogo[n1][n2]
                            jogo[n1][n2] = jogo[n3][n4]
                            jogo[n3][n4] = t
                            time.sleep(5)
                    else:
                        print('\033[0;30;41m As gemas que serão permutadas devem ser adjacentes!\033[m')
                        time.sleep(5)
                elif (n2 == len(jogo[0])-1):# se for da ultima coluna
                    if (n3 == n1+1 and n4 == n2) or (n3 == n1-1 and n4 == n2) or (n4 == n2+1 and n3 == n1):
                        entrada_certa = 's'
                        t = jogo[n1][n2]
                        jogo[n1][n2] = jogo[n3][n4]
                        jogo[n3][n4] = t
                        verificador = verificar_cadeia(jogo, parametro1, parametro2, n1, n2, n3, n4)
                        if verificador == False:
                            print('\033[0;30;41mMOVIMENTO INVÁLIDO!!!\033[m')
                            t = jogo[n1][n2]
                            jogo[n1][n2] = jogo[n3][n4]
                            jogo[n3][n4] = t
                            time.sleep(5)
                    else:
                        print('\033[0;30;41m As gemas que serão permutadas devem ser adjacentes!\033[m')
                        time.sleep(5)
                else:
                    if (n3 == n1+1 and n4 == n2) or (n3 == n1-1 and n4 == n2) or (n4 == n2+1 and n3 == n1) or (n4 == n2-1 and n3 == n1):
                        entrada_certa ='s'
                        t = jogo[n1][n2]
                        jogo[n1][n2] = jogo[n3][n4]
                        jogo[n3][n4] = t
                        verificador = verificar_cadeia(jogo, parametro1, parametro2, n1, n2, n3, n4)
                        if verificador == False:
                            print('\033[0;30;41mMOVIMENTO INVÁLIDO!!!\033[m')
                            t = jogo[n1][n2]
                            jogo[n1][n2] = jogo[n3][n4]
                            jogo[n3][n4] = t
                            time.sleep(5)
                    else:
                        print('\033[0;30;41m As gemas que serão permutadas devem ser adjacentes!\033[m')
                        time.sleep(5)
            except ValueError:
                print('\033[0;30;41mENTRADA INVÁLIDA!!!\033[m')
                time.sleep(5)
            os.system('cls')
        elif menu == 'S':# ENCERRAR O JOGO
            print('\033[0;30;41mPONTUAÇÃO FINAL: {}\033[m'.format(pontuacao))
            print('\033[0;30;41mFIM DE JOGO\033[m')
            time.sleep(5)
            break
        else:
            print('\033[0;30;41mALTERNATIVA INEXISTENTE!!!\033[m')
            time.sleep(5)
            os.system('cls')
    if menu== 'S':
        break
    auxiliar = cadeias(jogo, parametro1, parametro2, pontuacao, letras)# A variavel auxiliar armazena a pontuação do jogo e a nova matriz gerada pela função cadeias
    pontuacao += auxiliar[1]
    jogo = auxiliar[0]