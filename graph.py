import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# autor: Cezary Panas

# Ziarno generatora liczb pseudo-losowych
np.random.seed(42)
# Powołuje stałe które wykorzystam w modelu są to punktowe predykcje ekspertów
p = 0.4
q = 0.7
r = 0.1

### Tworze strukture grafu :
graph = nx.DiGraph()
graph.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'ignore', 'check', 'fix', 'a', 'b', 'c', 'd', 'e'])
graph.add_edge(0, 'ignore', weight=1, cost=0)
graph.add_edge(0, 'check', weight=1, cost=1)
graph.add_edge(0, 'fix', weight=1, cost=3)
graph.add_edges_from([('ignore', 'a', {'weight': p, 'cost': 0}),
                      ('ignore', 'b', {'weight': 1 - p, 'cost': 0}),
                      ('a', 1, {'weight': q, 'cost': 30}),
                      ('a', 2, {'weight': 1 - q, 'cost': 0}),
                      ('b', 3, {'weight': r, 'cost': 20}),
                      ('b', 4, {'weight': 1 - r, 'cost': 0}),
                      ('check', 'c', {'weight': p, 'cost': 0}),
                      ('check', 'd', {'weight': 1 - p, 'cost': 0}),
                      ('c', 5, {'weight': 1, 'cost': 10}),
                      ('d', 'e', {'weight': 1, 'cost': 0}),
                      ('e', 6, {'weight': r, 'cost': 20}),
                      ('e', 7, {'weight': 1 - r, 'cost': 0}),
                      ('fix', 8, {'weight': p, 'cost': 7}),
                      ('fix', 9, {'weight': 1 - p, 'cost': 2})
                      ])


# 1 funkcja zlicza z grafu wartości prawdopodbieństw zajścia zdarzenia zgodnie z oceną ekspercką oraz podlicza koszty
# związane z decyzjami po krawedziach dążących do pewnego potencjalnego stanu świata
def calculate_accumulated_metrics(graph, leaf_node):
    paths = list(nx.all_simple_paths(graph, source=0, target=leaf_node))

    accumulated_cost = 0
    accumulated_prob = 1

    for path in paths:
        # koszt jest sumą kosztów na krawędziach
        cost = sum(graph[u][v]['cost'] for u, v in zip(path[:-1], path[1:]))
        accumulated_cost += cost

        # prawdopodbieństwo wystąpienia danego stanu świata (nalezy pamiętać że dla liści 1,2,3,4 suma = 1 , tak samo dla  5,6,7  i 8,9
        # są to prawdopodobieństwa zakładające, że obraliśmy daną strategię i należy rozważac je tyko w kontekście konkretnej strategii)
        prob = np.prod(list(graph[u][v]['weight'] for u, v in zip(path[:-1], path[1:])))
        accumulated_prob *= prob

    return accumulated_cost, accumulated_prob


#######################
####   SYMULACJA   ####
#######################

def simulate(graph, n_simulations, p_expected, q_expected, r_expected, deviation_p, deviation_q, deviation_r,
             winning_strategies):
    # Initialize lists to store the results of each simulation
    global ignore_sum, fix_sum, check_sum, leaf_node_data
    accumulated_costs = []
    ignore_sums = []
    check_sums = []
    fix_sums = []
    winning_strategies = []
    for _ in range(n_simulations):
        # Truncated normal distributions :
        p = np.clip(np.random.normal(p_expected, deviation_p), 0, 1)
        q = np.clip(np.random.normal(q_expected, deviation_q), 0, 1)
        r = np.clip(np.random.normal(r_expected, deviation_r), 0, 1)

        # Update the graph with the varied probabilities
        edge_probabilities = {
            ('ignore', 'a'): p,
            ('ignore', 'b'): 1 - p,
            ('a', 1): q,
            ('a', 2): 1 - q,
            ('b', 3): r,
            ('b', 4): 1 - r,
            ('check', 'c'): p,
            ('check', 'd'): 1 - p,
            ('e', 6): r,
            ('e', 7): 1 - r,
            ('fix', 8): p,
            ('fix', 9): 1 - p
        }

        nx.set_edge_attributes(graph, edge_probabilities, 'weight')

        # Initialize strategy sums for the current simulation
        ignore_sum = 0
        check_sum = 0
        fix_sum = 0

        # Calculate and store accumulated metrics for each leaf node
        leaf_nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        strategy_assignment = {
            1: "ignore", 2: "ignore", 3: "ignore", 4: "ignore",
            5: "check", 6: "check", 7: "check",
            8: "fix", 9: "fix"
        }

        leaf_node_data = []
        for leaf_node in leaf_nodes:
            cost, prob = calculate_accumulated_metrics(graph, leaf_node)
            strategy = strategy_assignment[leaf_node]

            # Update strategy sum based on the strategy assignment
            if strategy == "ignore":
                ignore_sum += prob * cost
            elif strategy == "check":
                check_sum += prob * cost
            elif strategy == "fix":
                fix_sum += prob * cost

            leaf_node_info = {
                'Leaf Node': leaf_node,
                'Accumulated Cost': cost,
                'Accumulated Probability': prob,
                'Strat': strategy,
            }

            leaf_node_data.append(leaf_node_info)

        # Store results for the current simulation
        accumulated_costs.append(ignore_sum + check_sum + fix_sum)
        ignore_sums.append(ignore_sum)
        check_sums.append(check_sum)
        fix_sums.append(fix_sum)
    winning_strategy = min(zip(["ignore", "check", "fix"], [ignore_sum, check_sum, fix_sum]), key=lambda x: x[1])[0]
    winning_strategies.append(winning_strategy)

    return accumulated_costs, ignore_sums, check_sums, fix_sums, winning_strategies, leaf_node_data


###################################################################################################

def run_simulation_analysis(graph, n_simulations, p_expected, q_expected, r_expected, deviation_p, deviation_q,
                            deviation_r, show_plots=True):
    ignore_sums_all = []
    check_sums_all = []
    fix_sums_all = []
    winning_strategies_all = []
    leaf_node_data_all = []

    for simulation_num in range(1, n_simulations + 1):
        winning_strategies = []
        accumulated_costs, ignore_sums, check_sums, fix_sums, winning_strategies, leaf_node_data = simulate(
            graph.copy(), simulation_num, p_expected, q_expected, r_expected, deviation_p, deviation_q, deviation_r,
            winning_strategies)

        # Append results from each simulation

        ignore_sums_all.append(ignore_sums[-1])
        check_sums_all.append(check_sums[-1])
        fix_sums_all.append(fix_sums[-1])
        winning_strategies_all.extend(winning_strategies)
        leaf_node_data_all.extend(leaf_node_data)

    leaf_probabilities = {}

    for item in leaf_node_data_all:
        leaf_node = item['Leaf Node']
        probability = item['Accumulated Probability']
        cost = item['Accumulated Cost']
        strategy = item['Strat']

        if leaf_node not in leaf_probabilities:
            leaf_probabilities[leaf_node] = {'Probabilities': [], 'Costs': [], 'Strat': []}

        leaf_probabilities[leaf_node]['Probabilities'].append(probability)
        leaf_probabilities[leaf_node]['Costs'].append(cost)
        leaf_probabilities[leaf_node]['Strat'].append(strategy)
    leaf_statistics = {}

    for leaf_node, leaf_node_data_all in leaf_probabilities.items():
        probabilities = leaf_node_data_all['Probabilities']
        costs = leaf_node_data_all['Costs']
        strategy = leaf_node_data_all['Strat']

        mean_probability = np.mean(probabilities)
        std_dev_probability = np.std(probabilities)

        # No need to calculate mean cost as it remains constant
        accumulated_cost = costs[0]
        strategy = strategy[0]
        leaf_statistics[leaf_node] = {
            'Mean Probability': mean_probability,
            'Standard Deviation Probability': std_dev_probability,
            'Accumulated Cost': accumulated_cost,
            'Strat': strategy
        }

    print('\n')
    for leaf_node, stats in leaf_statistics.items():
        print(
            f'Leaf {leaf_node}: Cost = {stats["Accumulated Cost"]}, Probability = {stats["Mean Probability"]:.4f}, Std = {stats["Standard Deviation Probability"]:.4f}, Strategy {stats["Strat"]}')

    # Convert lists to NumPy arrays

    ignore_sums_all = np.array(ignore_sums_all)
    check_sums_all = np.array(check_sums_all)
    fix_sums_all = np.array(fix_sums_all)

    ignore_mean = np.mean(ignore_sums_all)
    ignore_std = np.std(ignore_sums_all)

    check_mean = np.mean(check_sums_all)
    check_std = np.std(check_sums_all)

    fix_mean = np.mean(fix_sums_all)
    fix_std = np.std(fix_sums_all)

    # Display statistics
    display_statistics(ignore_mean, ignore_std, check_mean, check_std, fix_mean, fix_std)

    # Count winning strategies
    count_winning_strategies(winning_strategies_all)

    if show_plots:
        # Plot histograms
        plot_histograms(ignore_sums_all, check_sums_all, fix_sums_all)

        # Plot cumulative distribution
        plot_cumulative_distribution(ignore_sums_all, check_sums_all, fix_sums_all)

        # Show plots
        plt.show()

    winning_counts = Counter(winning_strategies_all)
    return winning_counts['ignore'], winning_counts['check'], winning_counts['fix']


def plot_histograms(ignore_sums, check_sums, fix_sums):
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    sns.histplot(ignore_sums, kde=True, bins=30, color='blue', label='Ignore Strategy')
    plt.title('Density Plot - Ignore Strategy')
    plt.xlabel('Accumulated Cost')
    plt.legend()

    plt.subplot(1, 3, 2)
    sns.histplot(check_sums, kde=True, bins=30, color='orange', label='Check Strategy')
    plt.title('Density Plot - Check Strategy')
    plt.xlabel('Accumulated Cost')
    plt.legend()

    plt.subplot(1, 3, 3)
    sns.histplot(fix_sums, kde=True, bins=30, color='green', label='Fix Strategy')
    plt.title('Density Plot - Fix Strategy')
    plt.xlabel('Accumulated Cost')
    plt.legend()

    plt.tight_layout()


def plot_cumulative_distribution(ignore_sums, check_sums, fix_sums):
    plt.figure(figsize=(8, 6))

    sns.kdeplot(ignore_sums, cumulative=True, color='blue', label='Ignore Strategy')
    sns.kdeplot(check_sums, cumulative=True, color='orange', label='Check Strategy')
    sns.kdeplot(fix_sums, cumulative=True, color='green', label='Fix Strategy')

    plt.title('Cumulative Distribution of Accumulated Costs')
    plt.xlabel('Accumulated Cost')
    plt.ylabel('Cumulative Probability')
    plt.legend()


def display_statistics(ignore_mean, ignore_std, check_mean, check_std, fix_mean, fix_std):
    print(f"\nIgnore Strategy: Mean = {ignore_mean:.2f}, Standard Deviation = {ignore_std:.2f}")
    print(f"Check Strategy:  Mean = {check_mean:.2f}, Standard Deviation = {check_std:.2f}")
    print(f"Fix Strategy:    Mean = {fix_mean:.2f},  Standard Deviation = {fix_std:.2f}")


def count_winning_strategies(winning_strategies_all):
    winning_counts = Counter(winning_strategies_all)
    print(f"Number of wins for 'ignore' strategy: {winning_counts['ignore']}")
    print(f"Number of wins for 'check' strategy: {winning_counts['check']}")
    print(f"Number of wins for 'fix' strategy: {winning_counts['fix']}")
