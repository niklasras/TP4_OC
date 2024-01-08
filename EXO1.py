numero = float(input("Vous cherchez la table de multiplication de quel nombre ?: "))
produit = 1
p = []
for i in range(0, 10):
    produit = numero*i
    p.append(round(produit, 2))

for i in range(len(p)):
    print(numero, "*", i, "=", p[i])
