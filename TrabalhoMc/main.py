from classMochila import Mochila
from tsp import Tsp
from solver import temperaSimulada


tsp = Tsp("FIVE.txt")

mochila = Mochila()
solver = temperaSimulada(mochila,'MAX')
solver.solver()

