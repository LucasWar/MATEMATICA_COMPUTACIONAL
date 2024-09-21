import random
import os
class Tsp:
    def __init__(self,nome) -> None:
         self.matriz = self.lerArquivo(nome)

    def gerarSolucaoInicial(self):
        n = len(self.matriz)
        caminhoInicial = list(range(n))
        random.shuffle(caminhoInicial)
        return caminhoInicial

    def gerarNovaSolucao(self,caminho):
        nova_caminho = caminho[:]
        c1, c2 = sorted(random.sample(range(len(caminho)), 2))
        nova_caminho[c1:c2] = reversed(nova_caminho[c1:c2])
        return nova_caminho

    def lerArquivo(self,nome):
        arquivo = open(os.getcwd()+"\\TrabalhoMc\\entradas\\"+nome, "r")
        texto = arquivo.read()
        linhas = texto.strip().split('\n')
        matriz = []
        for linha in linhas:
            elementos = list(map(float, linha.split()))
            matriz.append(elementos)

        return matriz

    def funcaoFit(self,caminho: list[int]) -> int:
            matriz = self.matriz[:]
            distancaiTotal = 0
            for i in range(1, len(caminho)):
                distancaiTotal += matriz[caminho[i-1]][caminho[i]]
            distancaiTotal += matriz[caminho[-1]][caminho[0]]
            return distancaiTotal

    def resultado(self,solucao):
         print(f"Solucao: {solucao}")
         print(f"Valor menor caminho: {self.funcaoFit(solucao)}")