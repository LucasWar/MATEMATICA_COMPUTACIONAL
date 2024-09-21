import random
from typing import List,Callable
class Mochila:
    def __init__(self,pesoMaximo = 500,numeroItens = 20,pesoMinimoItem = 1,pesoMaximoItem = 100 ,grauImpoItemMin = 1,grauImpoItemMax = 100) -> None:
        self.pesoMaximo = pesoMaximo
        self.numeroItens = numeroItens
        self.pesoMinimoItem = pesoMinimoItem
        self.pesoMaximoItem = pesoMaximoItem 
        self.grauImpoItemMin = grauImpoItemMin
        self.grauImpoItemMax = grauImpoItemMax
        self.itens = []
        self.instanciaItens()
        self.relacaoImportanciaPeso = list(map(self.calcImportanciaPeso,self.itens))
        self.listaFechada = []
        #ADD lista fechada para não reexplorar caminhos ja explorados

    def calcImportanciaPeso(self,item):
        return item['importancia']/item['peso']
    
    def instanciaItens(self):
        for _ in range(self.numeroItens):
            peso = random.randint(self.pesoMinimoItem,self.pesoMaximoItem)
            importancia = random.randint(self.grauImpoItemMin,self.grauImpoItemMax)
            self.itens.append({'peso':peso,'importancia':importancia})
        
        self.itens = sorted(self.itens,key = lambda x: x['importancia'] / x['peso'],reverse=True)

    def gerarSolucaoInicial(self):
        solucao = [0] * self.numeroItens
        pesoAtual = 0
        for i in range(self.numeroItens):
            pesoAtual += self.itens[i]['peso']
            if(pesoAtual <= self.pesoMaximo):
                solucao[i] = 1    
            else: 
                break
        return solucao
    
    def gerarNovaSolucao(self,solucao:list[int]):
        if(0 not in solucao or solucao in self.listaFechada):
            return solucao
        else:
            self.listaFechada.append(solucao)
            indicesZeros = [i for i, valor in enumerate(solucao) if valor == 0]
            indecesItensOn = [i for i, valor in enumerate(solucao) if valor == 1]

            novaSolucao = solucao[:]
            pesoAtual = self.funcaoFitPeso(novaSolucao)

            for i in indecesItensOn:
                for j in indicesZeros:
                    pesoNovo = pesoAtual - self.itens[i]['peso'] + self.itens[j]['peso']
                    if pesoNovo <= self.pesoMaximo:
                        importanciaAntiga = self.funcaoFitImportancia(novaSolucao)
                        novaSolucao[i] = 0
                        novaSolucao[j] = 1
                        importanciaNova = self.funcaoFitImportancia(novaSolucao)

                        if importanciaNova > importanciaAntiga:
                            return novaSolucao
                        else:
                            novaSolucao[i] = 1
                            novaSolucao[j] = 0

        return solucao
            
        # solucao = [0] * self.numeroItens
        # pesoTotal = 0
        # copiaItens = self.itens
        # while(True):
        #     index = random.randint(0,self.numeroItens-1)
        #     item = copiaItens[index]
        #     if((pesoTotal + item['peso']) <= self.pesoMaximo):
        #         solucao[index] = 1
        #         pesoTotal += item['peso']
        #     else:
        #         break
    
        # return solucao
    
    def funcaoFit(self,solucao:list[int]):
        peso = 0
        importancia = 0
        cont = 0
        for i in range(len(solucao)):
            naMochila = solucao[i]
            if(naMochila == 1):
                item = self.itens[i]
                peso += item['peso']
                importancia += item['importancia']
                cont += 1
        return importancia

    def funcaoFitPeso(self,solucao):
        peso = 0
        importancia = 0
        cont = 0
        for i in range(len(solucao)):
            naMochila = solucao[i]
            if(naMochila == 1):
                item = self.itens[i]
                peso += item['peso']
                importancia += item['importancia']
                cont += 1
        return peso  
    
    def funcaoFitImportancia(self,solucao):
        peso = 0
        importancia = 0
        cont = 0
        for i in range(len(solucao)):
            naMochila = solucao[i]
            if(naMochila == 1):
                item = self.itens[i]
                peso += item['peso']
                importancia += item['importancia']
                cont += 1
        return importancia
    
    def resultado(self,solucao):
        print(f"Solucao encontrada: {solucao}")
        print(f"Peso da solucão: {self.funcaoFitPeso(solucao)}    Peso Maximo da mochila: {self.pesoMaximo}")
        print(f"Importancia total da solucão: {self.funcaoFitImportancia(solucao)}")