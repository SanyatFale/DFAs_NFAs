import networkx as nx
import matplotlib.pyplot as plt
from itertools import product

class NFA:
    def __init__(self):
        # Define the states
        self.states = {'q0', 'q1', 'q2'}

        # Define the alphabet
        self.alphabet = {'0', '1'}

        # Define the transition function
        self.transition = {
            'q0': {'0': {'q1'}, '1': {'q1', 'q2'}},
            'q1': {'0': {'q2'}},
            'q2': {'1': {'q0'}}
        }

        # Define the start state
        self.start_state = 'q0'

        # Define the set of accepting states
        self.accept_states = {'q2'}

    def process_input(self, input_str):
        current_states = {self.start_state}

        for symbol in input_str:
            if symbol not in self.alphabet:
                raise ValueError(f"Invalid symbol '{symbol}' in the input string.")

            next_states = set()
            for state in current_states:
                next_states.update(self.transition[state].get(symbol, set()))

            current_states = next_states

        return any(state in self.accept_states for state in current_states)

    def visualize(self):
        G = nx.DiGraph()

        for state in self.states:
            G.add_node(state, shape='circle', peripheries='2' if state in self.accept_states else '1')

        for start_state, transitions in self.transition.items():
            for symbol, end_states in transitions.items():
                for end_state in end_states:
                    G.add_edge(start_state, end_state, label=symbol)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, arrowsize=12, connectionstyle='arc3,rad=0.1')

        plt.show()

# Example usage:
nfa = NFA()

# Test strings
test_strings = ['10', '111', '001', '1101', '0', '1']

# Test the NFA with input strings
for test_str in test_strings:
    result = nfa.process_input(test_str)
    print(f'The NFA {"accepts" if result else "rejects"} the input "{test_str}"')

# Visualize the NFA
nfa.visualize()
