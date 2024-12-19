# Name: Ian Bubier
# Course: CS 325 - Analysis of Algorithms
# Assignment: Homework 8: Graph Algorithms - II
# Date: 11/26/2024

from collections import deque


def solve_puzzle(Board, Source, Destination):
    """
    Receives a 2-D puzzle of size MxN in which each cell is open "-" or blocked "#".
    Returns the shortest open path from a source cell to a destination cell.
    Employs a Breadth-First Search algorithm.
    :param Board: A 2D matrix.
    :param Source: A starting cell.
    :param Destination: An end cell.
    :return: The shortest path from Source to Destination.
    """
    node_queue = deque()
    visited = set()
    previous = {Source: None}
    length = {Source: 0}
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left
    node_queue.append(Source)

    while node_queue:
        node = node_queue.popleft()
        visited.add(node)
        neighbors = []

        # Constructs response if destination node is reached.
        if node == Destination:
            path_queue = deque()
            string_queue = deque()
            while node is not None:
                path_queue.append(node)
                if node in previous:
                    for move in moves:
                        if (node[0] + move[0], node[1] + move[1]) == previous[node]:
                            match move:
                                case (1, 0):
                                    string_queue.append('U')
                                case (-1, 0):
                                    string_queue.append('D')
                                case (0, 1):
                                    string_queue.append('L')
                                case (0, -1):
                                    string_queue.append('R')
                node = previous[node]
            output = []
            while path_queue:
                output.append(path_queue.pop())
            output_string = ''
            while string_queue:
                output_string = output_string + string_queue.pop()
            return tuple(output), output_string

        # Performs breadth-first search to build path.
        for move in moves:
            if (node[0] + move[0], node[1] + move[1]) not in visited \
                    and len(Board) > node[0] + move[0] >= 0 \
                    and len(Board[node[0]]) > node[1] + move[1] >= 0 \
                    and Board[node[0] + move[0]][node[1] + move[1]] == '-':
                neighbors.append((node[0] + move[0], node[1] + move[1]))
        for neighbor in neighbors:
            if neighbor not in length or length[node] + 1 < length[neighbor]:
                length[neighbor] = length[node] + 1
                previous[neighbor] = node
                node_queue.append(neighbor)

    # Returns None if destination node is unreachable.
    return None
