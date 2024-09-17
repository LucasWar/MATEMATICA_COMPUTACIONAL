import random
class Mochila:
    def __init__(self,pesoMaximo,numeroItens,pesoMinimoItem,pesoMaximoItem,grauImpoItemMin,grauImpoItemMax) -> None:
        self.pesoMaximo = pesoMaximo
        self.numeroItens = numeroItens
        self.pesoMinimoItem = pesoMinimoItem
        self.pesoMaximoItem = pesoMaximoItem 
        self.grauImpoItemMin = grauImpoItemMin
        self.grauImpoItemMax = grauImpoItemMax
        self.pesoAtual = 0
        self.itens = []

    def instanciaItens(self):
        for _ in range(self.numeroItens):
            peso = random.randint(self.pesoMinimoItem,self.pesoMaximoItem)
            importancia = random.randint(self.grauImpoItemMin,self.grauImpoItemMax)
            self.itens.append({'peso':peso,'importancia':importancia})

        # return self.itens

    def gerarSolucaoInicial(self):
        solucao = [0] * self.numeroItens
        pesoTotal = 0
        copiaItens = self.itens
        while(True):
            index = random.randint(0,self.numeroItens-1)
            item = copiaItens[index]
            if((pesoTotal + item['peso']) <= self.pesoMaximo):
                solucao[index] = 1
                pesoTotal += item['peso']
            else:
                break
    
        return solucao
    
    def gerarNovaSolucao(self):
        solucao = [0] * self.numeroItens
        pesoTotal = 0
        copiaItens = self.itens
        while(True):
            index = random.randint(0,self.numeroItens-1)
            item = copiaItens[index]
            if((pesoTotal + item['peso']) <= self.pesoMaximo):
                solucao[index] = 1
                pesoTotal += item['peso']
            else:
                break
    
        return solucao
    
    def funcaoFit(self,solucao):
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

    def addItem(self,pesoItem) -> None:
        self.pesoAtual += pesoItem
    
    def getPesoAtual(self) -> bool:
        return self.pesoAtual
    
    def getPesoMaximo(self) -> bool:
        return self.pesoMaximo
    
    def validarConjuntoItens(self) -> bool:
        if(self.pesoAtual <= self.pesoMaximo):
            return True
        else:
            return False
        
# mochila = Mochila(500,20,1,50,1,100)
# mochila.instanciaItens()
# teste = mochila.gerarSolução()
