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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    stack = util.Stack()
    visited = set()

    start_state = problem.getStartState()
    stack.push((start_state, []))

    while not stack.isEmpty():
        curr_state, path = stack.pop()
        
        if curr_state not in visited:
            visited.add(curr_state)

            if problem.isGoalState(curr_state):
                return path
            
            for next_state, action, cost in problem.getSuccessors(curr_state):
                if next_state not in visited:
                    new_path = path + [action]
                    stack.push((next_state, new_path))
    return []

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    queue = util.Queue()
    visited = set()

    start_state = problem.getStartState()
    queue.push((start_state, []))
    visited.add(start_state)

    while not queue.isEmpty():
        curr_state, path = queue.pop()
        
        #if curr_state not in visited:
        #    visited.add(curr_state)

        if problem.isGoalState(curr_state):
            return path
            
        for next_state, action, cost in problem.getSuccessors(curr_state):
            if next_state not in visited:
                visited.add(next_state)
                new_path = path + [action]
                queue.push((next_state, new_path))
    return []

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    pri_q = util.PriorityQueue()
    visited = set()

    start_state = problem.getStartState()
    pri_q.push((start_state, [], 0), 0)  # (state, path, cost) priority 'shortest path'

    while not pri_q.isEmpty():
        curr_state, path, curr_state_cost = pri_q.pop()
        
        if curr_state not in visited:
            visited.add(curr_state)

            if problem.isGoalState(curr_state):
                return path
                
            for next_state, action, step_cost in problem.getSuccessors(curr_state):
                if next_state not in visited:
                    new_path = path + [action]
                    new_cost = curr_state_cost + step_cost
                    pri_q.push((next_state, new_path, new_cost), new_cost)
    return []

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    a_star = util.PriorityQueue()
    visited = set()

    start_state = problem.getStartState()
    a_star.push((start_state, [], 0), 0 + heuristic(start_state, problem))

    while not a_star.isEmpty():
        curr_state, path, curr_state_cost = a_star.pop()

        if curr_state not in visited:
            visited.add(curr_state)

            if problem.isGoalState(curr_state):
                return path
            
            for next_state, action, step_cost in problem.getSuccessors(curr_state):
                if next_state not in visited:
                    new_path = path + [action]
                    new_cost = curr_state_cost + step_cost
                    # Prioiry: cost_path + hueristic value
                    priority = new_cost + heuristic(next_state, problem)
                    a_star.push((next_state, new_path, new_cost), priority)
    return []        


    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
