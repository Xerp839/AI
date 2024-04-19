class Node:
    def __init__(self, name, states, parents=None, probabilities=None):
        self.name = name
        self.states = states
        self.parents = parents if parents else []
        self.probabilities = probabilities if probabilities else {}

    def add_probability(self, state, probability):
        self.probabilities[state] = probability

    def get_probability(self, state, parent_states):
        key = tuple(parent_states)
        return self.probabilities[key][self.states.index(state)] if key in self.probabilities else 0


class BayesianNetwork:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def get_node(self, name):
        return self.nodes.get(name)

    def get_parents_states(self, node):
        parent_states = []
        for parent in node.parents:
            parent_states.append(parent.state)
        return parent_states

    def get_probability(self, node_name, state, parent_states):
        node = self.get_node(node_name)
        return node.get_probability(state, parent_states)

    def predict_probability(self, node_name, state, evidence={}):
        node = self.get_node(node_name)
        parent_states = []
        for parent in node.parents:
            parent_states.append(evidence[parent.name])
        return self.get_probability(node_name, state, parent_states)


# Example usage
if __name__ == "__main__":
    # Create nodes
    weather = Node("Weather", ["Sunny", "Rainy"])
    umbrella = Node("Umbrella", ["Yes", "No"], parents=[weather])

    # Add probabilities
    weather.add_probability("Sunny", [0.7, 0.3])
    weather.add_probability("Rainy", [0.3, 0.7])
    umbrella.add_probability(("Sunny",), [0.9, 0.1])
    umbrella.add_probability(("Rainy",), [0.2, 0.8])

    # Create Bayesian Network
    bbn = BayesianNetwork()
    bbn.add_node(weather)
    bbn.add_node(umbrella)

    # Predict probability
    print("Probability of carrying an umbrella when it's Sunny:", bbn.predict_probability("Umbrella", "Yes", evidence={"Weather": "Sunny"}))
