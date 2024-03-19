linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()
print(linguagens)
#ordenar de forma alfabética
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)
print(linguagens)
#indicamos ao interpretador q queremos inverter a ordem
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))
#indicar ordenação por tamanho
#de forma que o len é o tamanho dos objs, x são os objtos
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)




