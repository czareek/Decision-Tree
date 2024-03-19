import numpy as np

from graph import run_simulation_analysis, graph

np.random.seed(42)

# Show the plot
plt.title("Graph Visualization")
plt.show()
p_expected = 0.4  # Prawdopodbieństwo że oprogramowanie jest bardzo wadliwe
q_expected = 0.7  # Błędy zostaną powiązane z firma jeżeli kod jest bardzo wadliwy
r_expected = 0.1  # Błędy zostaną powiązane z firma jeżeli kod ma niewiele błędów
deviation_p = 0.05
deviation_q = 0.05
deviation_r = 0.05
n_simulations = 500  # liczba symulacji

run_simulation_analysis(graph, n_simulations, p_expected, q_expected, r_expected, deviation_p, deviation_q, deviation_r,
                        show_plots=True)
