from Board import Board
from Window import Window
from Player import Player
from Constants import ACTIONS
import random
import operator


class QLearner(object):
    qTable = {} # Maps tuple of (Cell, action) to reward
    discount = 0.9
    alpha = 0.9
    currState = (0,0)

    def __init__(self, b=Board()):
        self.board = b
        self.initQTable()

    def initQTable(self):
        for cell in self.board.getCells():
            for action in ACTIONS:
                if self.board.isValidCell(cell, action):
                    self.qTable[(cell, action)] = 0



    def learn(self):
        for i in range(10000):
            print(i)
            self.currState = (0, 0)
            while not self.board.isTerminalCell(self.currState):
                action = self.epsilonGreedy(self.currState)
                self.evalQFunction(self.currState, action)
                self.currState = self.board.getCellAfterAction(self.currState, action)

        for ((cell, action), val) in self.qTable.items():
            print("Cell: {}, Action: {}, Value: {}".format(cell, action, val))

        return self.qTable

    def epsilonGreedy(self, state):
        randInt = random.randint(1,11)
        if randInt <= 3:
            validActions = list(filter(lambda action: self.board.isValidCell(state, action), ACTIONS))
            return random.choice(validActions)

        else:
            # Gets all qValues for specified state for all q values
            arr = {key: val for key, val in self.qTable.items() if key[0] == state}
            # returns action that yields highest q value
            return max(arr, key=arr.get)[1]


    def epsilon(self):
        return random.choice(ACTIONS)

    # Q(s,a)+=α⋅[r+γ⋅maxαQ(s′)−Q(s,a)]
    def evalQFunction(self,coord, action):
        nextCell = self.board.getCellAfterAction(coord, action)
        reward = self.board.getCellValue(nextCell)
        maxQSPrime = max([self.qTable[(nextCell, action2)] for action2 in ACTIONS if self.board.isValidCell(nextCell, action2)])

        self.qTable[(coord, action)] += (self.alpha * (reward + self.discount * maxQSPrime - self.qTable[(coord,action)]))
