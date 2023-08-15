# utilizamos o extend para passar uma nova lista. Ao invés de passar objeto por objeto como acontece no append, passamos a lista de objetos completa

linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]
