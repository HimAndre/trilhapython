mensagem = "Olá, mundo!"  # Esta variável está no escopo global

def saudacao():
    print(mensagem)  # Podemos acessar a variável global dentro da função

saudacao()  # Saída: Olá, mundo!
#Imagine que o escopo global é como uma sala de aula onde todos os alunos podem ver e usar as mesmas coisas. Tudo o que é definido fora de qualquer função pode ser acessado de qualquer lugar no código.

def saudacao():
    mensagem_local = "Olá, mundo!"  # Esta variável está no escopo local da função
    print(mensagem_local)

saudacao()  # Saída: Olá, mundo!

# Se tentarmos acessar a variável local fora da função, obteremos um erro
print(mensagem_local)  # Isso irá resultar em um NameError
#Agora, pense em um escopo local como uma mesa individual de um aluno. O aluno pode ter suas próprias coisas na mesa que não podem ser vistas ou usadas pelos outros alunos na sala de aula (ou seja, outras funções não podem acessar essas variáveis).
