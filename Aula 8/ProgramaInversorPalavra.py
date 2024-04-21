string = input("Digíte um texto: ")
inversa = ""
for x in string:
    print("x=",x)
    print("INV",inversa)
    inversa=x + inversa
print(inversa)