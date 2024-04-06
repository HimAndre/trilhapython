def times_a(*args):
    for args in args:
        print(args)

times_a("VASCO","FLU","FLA","BOT")

#*args
# *args é usado para passar um número variável de argumentos posicionais para uma função.
# O * antes de args indica que todos os argumentos posicionais extras (além dos argumentos já especificados) serão coletados em uma tupla.
# É útil quando você não sabe quantos argumentos serão passados para a função.

def concessionaria(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
concessionaria(marca="Fiat", modelo="Pulse", ano=2022)
  


# def exibir_poema(data_extenso, *args, **kwargs):
#     texto = "\n".join(args)
#     meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
#     mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
#     print(mensagem)


# exibir_poema(
#     "Zen of Python",
#     "Beautiful is better than ugly.",
#     "Explicit is bettedr than implicit.",
#     "Simple is better than complex.",
#     "Complex is better than complicated.",
#     "Flat is better than nested.",
#     "Sparse is better than dense.",
#     "Readability counts.",
#     "Special cases aren't special enough to break the rules.",
#     "Although practicality beats purity.",
#     "Errors should never pass silently.",
#     "Unless explicitly silenced.",
#     "In the face of ambiguity, refuse the temptation to guess.",
#     "There should be one-- and preferably only one --obvious way to do it.",
#     "Although that way may not be obvious at first unless you're Dutch.",
#     "Now is better than never.",
#     "Although never is often better than *right* now.",
#     "If the implementation is hard to explain, it's a bad idea.",
#     "If the implementation is easy to explain, it may be a good idea.",
#     "Namespaces are one honking great idea -- let's do more of those!",
#     autor="Tim Peters",
#     ano=1999,
# )
