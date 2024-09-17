from classMochila import Mochila
from tsp import Tsp
import random,math
import operator


class temperaSimulada:

    def __init__(self,problema,obejetivo) -> None:
        self.objProblema = problema
        self.obejtivo = obejetivo
    
    def resolver(self):
        
        if(self.obejtivo == 'MAX'):
            operador = operator.gt
        elif(self.obejtivo == 'MIN'):
            operador = operator.lt

        mochila = Tsp('FIVE.txt')

        T = 4000
        solucaoAtual = mochila.gerarSolucaoInicial()
        melhorSolucao = solucaoAtual[:]

        L = 5
        taxaResfri = 0.999

        while(T > 0.05):
            for _ in range(L):
                solucaoAleatoria = mochila.gerarNovaSolucao(solucaoAtual[:])

                valorFitSoluAtual = mochila.funcaoFit(solucaoAtual)
                valorFitSoluAleatoria = mochila.funcaoFit(solucaoAleatoria)

                if(operador(valorFitSoluAleatoria,valorFitSoluAtual)):
                    solucaoAtual = solucaoAleatoria[:]
                    if(operador(valorFitSoluAtual,mochila.funcaoFit(melhorSolucao))):
                        melhorSolucao = solucaoAtual[:]
                else:
                    variacao = valorFitSoluAleatoria - valorFitSoluAtual
                    if random.random() < math.exp(-variacao / T):
                        solucaoAtual = solucaoAleatoria[:]
                
            T = T * taxaResfri


        print(mochila.funcaoFit(melhorSolucao))

        print(melhorSolucao)
