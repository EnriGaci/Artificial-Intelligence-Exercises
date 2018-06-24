# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

# @param parent Dict of child:parent values
# @param moves Dict of (child,parent):move from child to parent
# @returns result List with moves to perform to reach solution
def solution(parent,child,moves):
    """
    Returns the list of moves to solution\n
    parent Dict of child:parent values\n
    child Dict element to start iteration\n
    moves Dict of (child,parent):move from child to parent\n
    returns result List with moves to perform to reach solution
    """
    # List of directions our agent will follow
    # i.e ['South','West']
    result = []
    current_parent = parent[child]
    while current_parent != '-1':
        result.append(moves[child,current_parent])
        child = current_parent
        current_parent = parent[child]
    return list(reversed(result))

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    s = util.Stack()
    v = problem.getStartState()
    moves = {}

    s.push(v)
    discovered = {v:"False"}
    parent = {v:"-1"}

    while s.isEmpty() == False:
        v = s.pop()
        if discovered[v] == "False":
            discovered[v] = "True"
            for action in problem.getSuccessors(v):
                child = action[0]
                if problem.isGoalState(child):
                    parent[child] = v
                    moves[child,v] = action[1]
                    return solution(parent,child,moves)
                try:
                    if discovered[child]:
                        discovered[child] = "True"
                except:
                    parent[child] = v
                    moves[child,v] = action[1]
                    discovered[child] = "False"
                    s.push(child)



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    node = problem.getStartState()

    if problem.isGoalState(node):
        return True

    frontier = util.Queue()
    frontier.push(node)
    moves = {}
    explored = set()
    parent = []
    # node:parent dict. Keeps track of the parent
    # for each node
    parent = {node:"-1"}

    while frontier.isEmpty() == False:
        node = frontier.pop()
        explored.add(node)

        for action in problem.getSuccessors(node):
            # action[0] has the position tsolutionupple i.e (5,4)
            child = action[0]
            # store the move from parent to child. Move is
            # one of 'South','West','East',North'
            moves[child,node] = action[1]

            if (child not in explored) and (child not in frontier.list):
                parent[child] = node
                if problem.isGoalState(child):
                    return solution(parent,child,moves)
                frontier.push(child)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    moves = {}
    explored_set = set()
    parent = []
    frontier = util.PriorityQueue()
    node = problem.getStartState()

    frontier.push(node,0)
    # node:parent dict. Keeps track of the parent
    # for each node
    parent = {node:"-1"}

    while frontier.isEmpty() == False:
        node = frontier.pop()

        if problem.isGoalState(node):
            return solution(parent,node,moves)

        explored_set.add(node)

        for action in problem.getSuccessors(node):
            # action[0] has the position tsolutionupple i.e (5,4)
            child = action[0]

            if (child not in explored_set) and (child not in frontier.heap):
                parent[child] = node
                # store the move from parent to child. Move is
                # one of 'South','West','East',North'
                moves[child,node] = action[1]
                frontier.push(child,action[2])
            elif (child in frontier.heap):
                # this function checks if the new priority
                # is greater than the current of the child.
                # If so, it updates it
                frontier.update(child,action[2])



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
