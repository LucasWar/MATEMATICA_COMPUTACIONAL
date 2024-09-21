import random,math
import operator

class temperaSimulada:

    def __init__(self,problema,obejetivo,tempFinal = 0.05,tempIncial = 4000,taxaResfri = 0.999,L = 5) -> None:
        self.objProblema = problema
        self.obejtivo = obejetivo
        self.T = tempIncial
        self.tempFinal = tempFinal
        self.taxaResfri = taxaResfri
        self.L = L

    def solver(self):
        if(self.obejtivo == 'MAX'):
            operador = operator.gt
            sinalVariacao = 1
        elif(self.obejtivo == 'MIN'):
            operador = operator.lt
            sinalVariacao = -1

        solucaoAtual = self.objProblema.gerarSolucaoInicial()
        melhorSolucao = solucaoAtual[:]


        while(self.T > self.tempFinal):
            for _ in range(self.L):
                try:
                    solucaoAleatoria = self.objProblema.gerarNovaSolucao(solucaoAtual[:])
                except:
                    solucaoAleatoria = self.objProblema.gerarNovaSolucao()

                valorFitSoluAtual = self.objProblema.funcaoFit(solucaoAtual)
                valorFitSoluAleatoria = self.objProblema.funcaoFit(solucaoAleatoria)

                if(operador(valorFitSoluAleatoria,valorFitSoluAtual)):
                    solucaoAtual = solucaoAleatoria[:]
                    
                    if(operador(valorFitSoluAleatoria,self.objProblema.funcaoFit(melhorSolucao))):
                        melhorSolucao = solucaoAtual[:]
                else:
                    variacao = valorFitSoluAleatoria - valorFitSoluAtual
                    if random.random() < math.exp((variacao * sinalVariacao) / self.T):
                        solucaoAtual = solucaoAleatoria[:]

            self.T = self.T * self.taxaResfri

        self.objProblema.resultado(melhorSolucao)
