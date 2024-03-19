import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from graph import run_simulation_analysis, graph
np.random.seed(42)
def analyze_variance():
    p_expected = 0.4
    q_expected = 0.7
    r_expected = 0.1
    deviation_p = 0.20
    deviation_q = 0.05
    deviation_r = 0.05
    n_simulations = 100

    # print(
    #   "\nPrawodpodobieństwo p wystepowania wielu błedów w kodzie. Zdania ekspertów są mocno podzielone więc przyjeta wartosć 0,4")
    # print(
    # "może mieć większą wariancje niż pozostałe. Zwiększymy odch stand dla parametru dwukrotnie w symulacji i zobaczmy jaki wpływ ma to na wynik")

    graph_copy = deepcopy(graph)
    run_simulation_analysis(graph_copy, n_simulations, p_expected,
                                                                            q_expected, r_expected, deviation_p,
                                                                            deviation_q,
                                                                            deviation_r, show_plots=True)


def analyze_check_strategy():
    num_iterations = 25
    increment = 0.1
    ignore_all = []
    check_all = []
    fix_all = []
    cost_all = []
    graph_copy = deepcopy(graph)
    for _ in range(num_iterations):
        print(f"\nCheck cost = {graph_copy[0]['check']['cost']:.2f}\n")
        cost = graph_copy[0]['check']['cost']
        ignore, check, fix = run_simulation_analysis(graph_copy, n_simulations=100,
                                                                                p_expected=0.4, q_expected=0.7,
                                                                                r_expected=0.1,
                                                                                deviation_p=0.05, deviation_q=0.05,
                                                                                deviation_r=0.05, show_plots=False)
        graph_copy[0]['check']['cost'] += increment
        ignore_all.append(ignore)
        check_all.append(check)
        fix_all.append(fix)
        cost_all.append(cost)

    plt.plot(cost_all, ignore_all, label='Ignore', marker='o')
    plt.plot(cost_all, check_all, label='Check', marker='o')
    plt.plot(cost_all, fix_all, label='Fix', marker='o')
    plt.xlabel('Cost')
    plt.ylabel('Number of Wins')
    plt.title('Number of Wins at Different Costs')
    plt.legend()
    plt.grid(True)
    plt.show()

def analyze_penalty_1():
    number = 30
    i = -1
    ignore_all = []
    check_all = []
    fix_all = []
    penalty_all = []
    graph_copy = deepcopy(graph)
    for _ in range(number):
        print(f"\nPenalty  = {graph_copy['a'][1]['cost']:.2f}\n")
        penalty = graph_copy['a'][1]['cost']
        ignore, check, fix = run_simulation_analysis(graph_copy, n_simulations=100,
                                                                                p_expected=0.4, q_expected=0.7,
                                                                                r_expected=0.1,
                                                                                deviation_p=0.05, deviation_q=0.05,
                                                                                deviation_r=0.05, show_plots=False)
        graph_copy['a'][1]['cost'] += i
        ignore_all.append(ignore)
        check_all.append(check)
        fix_all.append(fix)
        penalty_all.append(penalty)
    plt.plot(penalty_all, ignore_all, label='Ignore', marker='o')
    plt.plot(penalty_all, check_all, label='Check', marker='o')
    plt.plot(penalty_all, fix_all, label='Fix', marker='o')
    plt.xlabel('Penalty')
    plt.ylabel('Number of Wins')
    plt.title('Number of Wins at Different Penalties')
    plt.legend()
    plt.grid(True)
    plt.show()

def analyze_penalty_2():
    num = 20
    i = -1
    ignore_all = []
    check_all = []
    fix_all = []
    penalty_all = []
    graph_copy = deepcopy(graph)
    for _ in range(num):
        print(f"\nPenalty = {graph_copy['b'][3]['cost']:.2f}\n")
        penalty = graph_copy['b'][3]['cost']
        ignore, check, fix = run_simulation_analysis(graph_copy, n_simulations=100,
                                                                                p_expected=0.4, q_expected=0.7,
                                                                                r_expected=0.1,
                                                                                deviation_p=0.05, deviation_q=0.05,
                                                                                deviation_r=0.05, show_plots=False)
        graph_copy['b'][3]['cost'] += i
        graph_copy['e'][6]['cost'] += i
        ignore_all.append(ignore)
        check_all.append(check)
        fix_all.append(fix)
        penalty_all.append(penalty)


    plt.plot(penalty_all, ignore_all, label='Ignore', marker='o')
    plt.plot(penalty_all, check_all, label='Check', marker='o')
    plt.plot(penalty_all, fix_all, label='Fix', marker='o')
    plt.xlabel('Penalty')
    plt.ylabel('Number of Wins')
    plt.title('Number of Wins at Different Penalties')
    plt.legend()
    plt.grid(True)
    plt.show()

def analyze_all_probabilities():
    p_expected = 0.5
    q_expected = 0.6
    r_expected = 0.2
    deviation_p = 0.05
    deviation_q = 0.05
    deviation_r = 0.05
    n_simulations = 500

    graph_copy = deepcopy(graph)
    run_simulation_analysis(graph_copy, n_simulations, p_expected, q_expected, r_expected, deviation_p, deviation_q,
                            deviation_r, show_plots=True)

    # Execute analyses


analyze_variance()
analyze_check_strategy()
analyze_penalty_1()
analyze_penalty_2()
analyze_all_probabilities()
