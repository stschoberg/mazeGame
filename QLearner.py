from Board import Board
from Window import Window
from Player import Player
from Constants import ACTIONS, NUM_EPISODES, EPSILON
import random
import operator
import copy

class QLearner(object):
    qTable = {} # Maps cell to possible actions. Actions then map to reward
    discount = 0.9
    alpha = 0.9
    currState = (0,0)

    def __init__(self, b=Board()):
        self.board = b
        self.initQTable()

    def initQTable(self):
        for cell in self.board.getCells():
            self.qTable[cell] = {}
            for action in ACTIONS:
                if self.board.isValidCell(cell, action):
                    self.qTable[cell][action] = 0


    def learn(self):
        count = 0
        for episode in range(NUM_EPISODES):
            self.currState = (0, 0)
            count+=1
            # print(count)
            while not self.board.isTerminalCell(self.currState):
                action = self.epsilonGreedy(self.currState)
                self.evalQFunction(self.currState, action)
                self.currState = self.board.getCellAfterAction(self.currState, action)



        return self.qTable

    def epsilonGreedy(self, state):
        randInt = random.randint(1,11)
        if randInt <= EPSILON:

            validActions = list(filter(lambda action: self.board.isValidCell(state, action), ACTIONS))
            return random.choice(validActions)

        else:
            # Gets all qValues for specified state for all q values
            arr = {key: val for key, val in self.qTable.items() if key == state}
            # returns action that yields highest q value
            return max(arr[state], key=arr[state].get)


    def epsilon(self):
        return random.choice(ACTIONS)

    # Q(s,a)+=α⋅[r+γ⋅maxαQ(s′)−Q(s,a)]
    def evalQFunction(self,coord, action):
        nextCell = self.board.getCellAfterAction(coord, action)
        reward = self.board.getCellValue(nextCell)
        maxQSPrime = max([self.qTable[nextCell][action2] for action2 in ACTIONS if self.board.isValidCell(nextCell, action2)])

        self.qTable[coord][action] += (self.alpha * (reward + self.discount * maxQSPrime - self.qTable[coord][action]))
