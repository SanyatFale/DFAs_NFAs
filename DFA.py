import networkx as nx
import matplotlib.pyplot as plt

class DFA:
    def __init__(self):
        # Define the states
        self.states = {'q0', 'q1', 'q2'}

        # Define the alphabet
        self.alphabet = {'0', '1'}

        # Define the transition function
        self.transition = {
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q2', '1': 'q1'},
            'q2': {'0': 'q2', '1': 'q2'},
        }

        # Define the start state
        self.start_state = 'q0'

        # Define the set of accepting states
        self.accept_states = {'q2'}

    def process_input(self, input_str):
        current_state = self.start_state

        for symbol in input_str:
            if symbol not in self.alphabet:
                raise ValueError(f"Invalid symbol '{symbol}' in the input string.")

            current_state = self.transition[current_state][symbol]

        return current_state in self.accept_states

    def visualize(self):
        G = nx.DiGraph()

        for state in self.states:
            is_accepting = state in self.accept_states
            node_attrs = {'color': 'red' if is_accepting else 'skyblue', 'peripheries': '2' if is_accepting else '1'}
            G.add_node(state, **node_attrs)

        for start_state, transitions in self.transition.items():
            for symbol, end_state in transitions.items():
                G.add_edge(start_state, end_state, label=symbol)

        pos = nx.spring_layout(G)
        edge_labels = {(start, end): label for start, end, label in G.edges(data='label')}

        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color=[node_attrs['color'] for node_attrs in G.nodes.values()])
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

        plt.show()

# Example usage:
dfa = DFA()

# Test strings
test_strings = ['1101', '1010', '000', '111', '1001']

for test_str in test_strings:
    result = dfa.process_input(test_str)
    print(f'The DFA {"accepts" if result else "rejects"} the input "{test_str}"')

    

# Example usage:
dfa = DFA()

# Visualize the DFA
dfa.visualize()
