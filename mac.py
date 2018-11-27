# -*- coding: utf-8 -*-

from sklearn import tree


lisal = 1

irregular = 0

maça = 1

laranja = 0

pomar = [ [150, lisal],[130, lisal] [180, irregular], [160, irregular] ]

resultado = [maça, maça, laranja, laranja]

clf =tree.DecisionTreeClassifier()
clf = clf.fit(pomar, resultado)

peso = input("Entre com o peso: ")

superficie = input("entre com a superficie: ")

resultadoUsuario = clf.predict([[peso, superficie]])

if resultadoUsuario == 1:
     print("é  uma maça")
else:
     print("é uma laranja")
