'''
Materia : raciocinio computacional
Aluno : Junior Scrobut ( Divansir de ramos Scrobut Junior)
Curso : Analise e desenvolvimento de sistemas
PUC-PR
Abril 2023
Conclusão projeto final 
'''

import json

lista = [] #Lista de estudantes
listas_disciplinas = [] #Lista das disciplinas
lista_turmas = [] #Lista das turmas 
lista_professores = [] #Lista dos professores
contador = 0

#Função para salvar dados em JSON
def salvar_dados():
    with open("dados.json", "w") as arquivo:
        json.dump({
            "lista": lista,
            "listas_disciplinas": listas_disciplinas,
            "lista_turmas": lista_turmas,
            "lista_professores": lista_professores
        }, arquivo)

#Menu principal
def menu():
  print("""
 =============================
 || [1]Gerenciar estudantes  ||
 || [2]Gerenciar professores ||
 || [3]Gerenciar diciplinas  || 
 || [4]Gerenciar turmas      ||
 || [5]Buscar dados          ||   
 || [6]Salvar dados          ||   
 || [7]Imprimir dados        ||      
 || [0] SAIR                 ||  
 ==============================""")

#Menu de operaçoes dos estudantes
def menu_operacoes():
        print("""
        ***MENU DE OPERAÇÕES ESTUDANTES***
    [1]Incluir estudante
    [2]Listar estudantes
    [3]Atualizar estudante
    [4]Excluir estudante
    [5]Voltar ao menu
    [6]Imprimir dados
    """)

#Função que inclue os estudantes
def incluir():
   global dicionario
   global codigo
   #Dicionario único dos estudantes
   dicionario = {}
   adicionar_nome = str(input("Digite seu nome:"))
   cpf = str(input("Digite seu CPF:"))
   codigo = int(input("Digite seu código:"))
   codigo_matricula = int(input("Digite o código da matrícula : "))
   dicionario['Nome:'] = adicionar_nome
   dicionario['Cpf:'] = cpf
   dicionario['Codigo:'] = codigo
   dicionario['Matricula:'] = codigo_matricula
   #Adicionando o dicionario com os valores dos estudantes na lista de estudantes
   lista.append(dicionario)

#Função que inclue professores
def incluir_professores():
#Dicionario unico dos professores
    dicionario_professores = {}
    codigo_professor = int(input("Digite o código do professor :"))
    cpf_professor = str(input("Digite o CPF do professor:"))
    nome_professor = str(input("Nome do professor : "))
    dicionario_professores['Codigo do professor:'] = codigo_professor
    dicionario_professores['CPF do professor:'] = cpf_professor
    dicionario_professores['Nome do professor:'] = nome_professor
   #Adicionando o dicionario com os valores dos professores na lista de professores
    lista_professores.append(dicionario_professores)


#Função que inclue as disciplinas
def disciplinas():
   dicionario_disciplinas = {}
   print("""
  =======================
  |MENU DE  DISCIPLINAS:|
  ========================""""")
   codigo_disciplina = int(input("Digite o código da  disciplina :"))
   nome_disciplina = str(input("Digite o nome da disciplina : "))
   dicionario_disciplinas['Código disciplina:'] = codigo_disciplina
   dicionario_disciplinas['Disciplina:'] = nome_disciplina
   listas_disciplinas.append(dicionario_disciplinas)

#Função de gerenciar turmas
def turma():
   while True:
    #Menu das turmas
    print(""" \n*** MENU DE OPERAÇÕES TURMAS ***\n
[1]Incluir turma
[2]Listar turma
[0]Voltar""")
    print('Escolha : ')
    #Analisa a escolha feita 
    escolha = int(input("  "))
    #Adiciona os dados a lista das turmas
    if escolha == 1 :
        dicionario_turmas = {}
        codigo_turma = int(input("Digite o código da turma"))
        codigo_prof = int(input("Digite o código do professor :"))
        codigo_materia = int(input("Digite o código da disciplina : "))
        dicionario_turmas['Código da turma:'] = codigo_turma
        dicionario_turmas['Código professor:'] = codigo_prof
        dicionario_turmas['Código da materia:'] = codigo_materia
        lista_turmas.append(dicionario_turmas)
    #Lista a lista  das turmas
    elif escolha == 2 :
    #Verifica se a lista das turmas está vazia
        if len(lista_turmas) == 0 :
          limpartela()
    #Se a lista estiver vazia a mensagem abaixo será exibida na tela
          print('Lista  das turmas vazia')
    #Exibe a lista das turmas
        else:
            print(lista_turmas)
    #Sai do menu das turmas
    elif escolha == 0 :
        break
    #Função erro em ação
    else:
     erro()

#Menu dos professores    
def professores(lista_professores):
   while True:
      print(""" \nMENU PROFESSORES\n
[1] Adicionar professor
[2] Listar professores 
[3] Excluir professores
[4] Buscar professor
[5] Voltar ao menu  
      """)
      escolha = int(input())
      if escolha == 1 :    
         incluir_professores()
      elif escolha == 2 :
         print( lista_professores)
      elif escolha == 3 :
         if len(lista_professores) == 0 :
            print("Não há professores para excluir")
         else:
            print(lista_professores)
            excluir()
      elif escolha == 4 :
         buscar_dados()
      elif escolha == 5 :
         limpartela()
         break
#Listagem dos estudantes
def listar():
#Vê se a lista está vazia
   if len(lista)== 0:
      print("LISTA VAZIA")
#Imprime a listagem com os dados dos estudantes e o número de cadastros  de estudantes feitos
   else:
    listagem = 'LISTAGEM'
    print(f"{listagem:=^20}")
    print('Total de cadastros:',contador)
    print(lista)

#Função para imprimir os dados em TXT
def imprimir():
#Verifica ambas a lista e se estiverem vazias não imprime nada
   if len(lista) == 0 and len(listas_disciplinas) == 0:
      print('Não há itens para serem impressos')
#Imprime todos os dados
   else:
      #Imprime informações gerais sobre o aluno
      with open("cadastro.txt","w") as arquivo_saida:
       for alunos in lista:
         arquivo_saida.write("NOME :" + alunos['Nome:'] + "\n")
         arquivo_saida.write("CPF :" + alunos['Cpf:'] + "\n")
         arquivo_saida.write("CODIGO :" + str(alunos['Codigo:']) + "\n")
         arquivo_saida.write("NUMERO DA MATRICULA :" + str(alunos['Matricula:']) + "\n")
         arquivo_saida.write("="*30 + "\n\n")
         
         #Imprime informações sobre disciplinas
         for disciplinas in listas_disciplinas:
          arquivo_saida.write("Nome da materia:" + disciplinas['Disciplina:'] + "\n")
          arquivo_saida.write("Codigo da disciplina:" +  str(disciplinas['Código disciplina:']) + "\n" )
          arquivo_saida.write("="* 30  + "\n\n")

        #Imprime informações sobre as turmas
         for turmas in lista_turmas:
            arquivo_saida.write("Codigo da turma :" + str(turmas['Código da turma:']) + "\n") 
            arquivo_saida.write("Codigo do professor :" + str(turmas['Código professor:']) + "\n")
            arquivo_saida.write("Codigo da materia :" + str(turmas['Código da materia:']) + "\n")
            arquivo_saida.write("="* 30  + "\n\n")
        #Imprime as informações sobre os professores(a)
         for professores in lista_professores:
            arquivo_saida.write("Codigo do professor :" + str(professores['Codigo do professor:']) + "\n" )
            arquivo_saida.write("Nome do professor :" + str(professores['Nome do professor:'])+ "\n")
            arquivo_saida.write("CPF do professor :" + str(professores['CPF do professor:'] + "\n"))

#Permite editar um registro dos alunos 
def editar():
   #Se a lista estiver vazia não fara a mudança
   if len (lista)== 0 :
      print("Não há informações para atualizar")
   else:
#Faz a mudança com base no codigo digitado
      cod = int(input("Digite o código para efetuar a atualização:"))
   for alunos in lista :
      if alunos['Codigo:'] == cod:
         adicionar_nome = str(input("Digite seu nome:"))
         cpf = str(input("Digite seu CPF:"))
         codigo = input("Digite seu código:")
         print("Lista atualizada")
         print(lista)
         break
      else:
         print("Nenhuma mudança feita")

#Função para excluir um aluno 
def excluir():
#Lê se a lista de estudante esta vazia,caso estiver vazia não ira excluir nada
   if len(lista) == 0   :
      print("Não há registros para excluir")
   else:
#Exclui a lista
      print(lista)
      remov = int(input("Digite o código que deseja excluir:"))
#Iteração sobre cada item no código
   for item in lista:
      if item['Codigo:'] == remov:
        item.pop('Nome:',None) #Remove o nome
        item.pop('Cpf:',None) #Remove o cpf
        item.pop('Codigo:',None) #Remove o codigo
        item.pop('Matricula:',None) #Remove o número da matrícula
        print("Item removido.")
        break    
      print(lista)

#Função para buscar dados
def buscar_dados():
#Menu inicial da busca de dados
    print("""
    *** MENU DE BUSCA ***
    [1] Buscar aluno por código  
    [2] Buscar aluno por nome    
    [3] Buscar aluno por CPF
    [4] Buscar disciplina por código
    [5] Buscar disciplina por nome
    [6] Buscar turma por código
    [7] Buscar turma por professor
    [8] Buscar turma por disciplina
    [9] Buscar professor por nome
    [0] Voltar
    """)
#Pergunta a opção escolhida
    opcao = int(input("Escolha uma opção: "))
#Entra para verificar o valor escolhido na opçao (vale para todos os números do menu)
    if opcao == 1:
        codigo = int(input("Digite o código do aluno: "))
#For que vai percorrer a lista em busca do código (A metadologia é usada para todos )
        for aluno in lista:
            if aluno['Codigo:'] == codigo:
                print(aluno)
                break
        else:
            print("Aluno não encontrado.")
    elif opcao == 2:
        nome = str(input("Digite o nome do aluno: "))
        for aluno in lista:
            if aluno['Nome:'] == nome:
                print(aluno)
        else:
            print("Aluno não encontrado.")
    elif opcao == 3 :
        cpf = str(input("Digite o CPF do aluno: "))
        for aluno in lista:
            if aluno['Cpf:'] == cpf:
                print(aluno)
        else:
            print("Aluno não encontrado.")
    elif opcao == 4 :
        codigo = int(input("Digite o código da disciplina: "))
        for disciplina in listas_disciplinas:
            if disciplina['Código disciplina:'] == codigo:
                print(disciplina)
        else:
            print("Disciplina não encontrada.")
    elif opcao == 5 :
        nome = str(input("Digite o nome da disciplina: "))
        for disciplina in listas_disciplinas:
            if disciplina['Disciplina:'] == nome:
                print(disciplina)
        else:
            print("Disciplina não encontrada.")
    elif opcao == 6 :
        codigo = int(input("Digite o código da turma: "))
        for turma in lista_turmas:
            if turma['Código da turma:'] == codigo:
                print(turma)
        else:
            print("Turma não encontrada.")
    elif opcao ==  7 :
        codigo = int(input("Digite o código do professor: "))
        for turma in lista_turmas:
            if turma['Código professor:'] == codigo:
                print(turma)
        else:
            print("Turma não encontrada.")
    elif opcao ==  8 :
        codigo = int(input("Digite o código da disciplina: "))
        for turma in lista_turmas:
            if turma['Código da materia:'] == codigo:
                print(turma)
        else:
            print("Turma não encontrada.")
    elif opcao ==  9 :
        codigo = int(input("Digite o nome do professor:"))
        for professor in lista_professores:
          if professor['Nome do professor:'] == codigo :
             print("Professor encontrado :\n",professor)
        else:
             print("Professor não encontrado")
    elif opcao == 10 :
       print('a')
    elif opcao == 0 :
       menu()
#Função para sair do programa 
def sair():
   print("Saindo ...")
   exit()     

#Função que exibe erro não escolher uma opção válida  dentro das opçoes do menu
def erro():
   limpartela()
   erro = "ERRO DIGITE UM VALOR VÁLIDO !!"
   print(f'\n\n{erro:^60}')

#Função para limpar a tela,a fim de deixar o programa mais organizado
def limpartela():
   print("\n"*100)

#Laço de repetição do menu principal
while True:
   menu()
#Escolha para determinar oque o usuário deseja fazer
   escolha_menus = int(input("Digite sua escolha:"))
   if escolha_menus == 1 :
#Entra no menu de operações de estudantes 
      while True :
         menu_operacoes()
         escolha = int(input("Digite a escolha :"))
#Se a escolha for 1 ,a função incluir (estudantes) será executada,incrementando um número de cadastros
         if escolha == 1 :
            incluir()
            contador +=1
#Se a escolha for 2, a função listar(listar os estudantes) sera executada
         elif escolha == 2 :
            listar()
#Se a escolha for 3, a função editar(estudantes) sera executada
         elif escolha == 3 :
            editar()
#Se a escolha for 4, a função excluir(estudantes) sera executada
         elif escolha == 4 :
            excluir()
#Aqui se a escolha for 5 o loop do menu de operaçoes dos estudantes sera encerrado,voltando para o menu principal
         elif escolha == 5 :
            break
#Função para imprimir os dados(em txt) dos estudantes
         elif escolha == 6 :
            imprimir()
#Se não entrar em nenhuma das condições de escolha,será mostrado a "mensagem valor invalido"
         else:
            print("Valor inválido")
#Aqui caso a escolha do menu principal seja 2 irá entrar na função do menu professores
   elif escolha_menus == 2 :
      professores(lista_professores=lista_professores)
#Aqui caso a escolha do menu principal seja  3 irá entrar na função do menu de disciplinas
   elif escolha_menus == 3:
    disciplinas()
#Aqui caso a escolha do menu principal seja 4 irá entrar na função do menu de turmas
   elif escolha_menus == 4 : 
      turma()
#Aqui caso a escolha do menu principal seja 5 irá entrar na função de buscar dados
   elif escolha_menus == 5 :
        buscar_dados()
#Aqui caso a escolha do menu principal seja 6 irá entrar na função de salvar dados em JSON
   elif escolha_menus == 6 :
      salvar_dados()
#Aqui caso seja escolhida a opção 0 ,será o fim do programa
   elif escolha_menus == 0 :
      sair()
#Aqui caso seja escolhido irá imprimir os dados em TXT
   elif escolha_menus == 7 :
      imprimir()
#Caso não entre em nenhuma condição a função erro será executada
   else:
      erro()

