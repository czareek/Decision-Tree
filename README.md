# Wspomaganie decyzji w warunkach niepewności przy wykorzystaniu drzewa decyzyjnego
## Wprowadzenie

Projekt stanowi kompleksową analizę dotyczącą wyboru optymalnego rozwiązania w  warunkach niepewności. Model w oparciu o ocenę ekspercką oraz symulacje numeryczne, pozwala zwizualizować potencjalne konsekwencje poszczególnych strategii.

## Opis Problemu

Firma XYZ stoi przed trudnym wyborem, mając do rozważenia trzy scenariusze w związku z wadliwym oprogramowaniem. Oto szczegółowy opis każdej opcji: **Zignorowanie problemu ("Ignore")**: Brak kosztów początkowych. Istnieje ryzyko, że błędy w oprogramowaniu okażą się poważne (40% szans), co skutkuje karą 30 milionów dolarów, lub niewielkie (60% szans) z karą 20 mln dolarów. Zaletą jest brak kosztów przy braku przypisania błędów do firmy. **Badanie kodu ("check")**: Koszty badania wynoszą 1 mln dolarów. Istnieje ryzyko, że błędy w oprogramowaniu okażą się poważne po badaniach (40% szans), co skutkuje koniecznością naprawy (ze względu na presję ze strony pracowników) za 10 mln dolarów plus koszty badań, lub niewielkie (60% szans). W takiej sytuacji zgodnie z polityką firmy jedyną dostępną opcją będzie zignorowanie problemu. **Hotfix ("Fix")**: Koszty początkowe wynoszą 3 mln dolarów. W trakcie przeprowadzania hotfixu może się okazac, że błędy będą poważne (dodatkowe 7 mln dolarów), lub niewielkie (dodatkowe 2 mln dolarów). 

## Implementacja Kodu

Kod został napisany w języku Python i wykorzystuje biblioteki takie jak NetworkX, NumPy i Matplotlib do symulacji i wizualizacji danych. Problem decyzyjny został sprowadzony do grafu skierowanego. Następnie wyniki symulacji poddano analizie wrażliwości, która pozwalaja na głębszą eksplorację scenariuszy decyzyjnych i zrozumienia problemu.

## Wyniki 


Rekomendacja: Strategia "Check" jest optymalna, uwzględniając koszty, ryzyko i stabilność wyników. Strategia "fix" ma niższe odchylenie standardowe kosztów, ale "Check" nadal przewyższa ją pod względem opłacalności. Strategia "ignore" jest silnie zdominowana przez dwie pozostałe strategie. Analiza wrażliwości, obejmująca zwiększenie odchylenia standardowego prawdopodobieństwa oraz wzrost kosztów decyzji "Check", dostarcza cennych informacji dla procesu decyzyjnego. Na podstawie uzyskanych wyników  rekomendowana  strategia to  "Check".

## Analiza Wrażliwości

Analiza wrażliwości, obejmująca zwiększenie odchylenia standardowego prawdopodobieństwa oraz wzrost kosztów decyzji "Check", dostarcza cennych informacji dla procesu decyzyjnego.
Projekt analizuje wpływ zmiany wysokości kary, kosztów przeprowadzenia badania na opłacalność poszczególnych strategii:

W wyniku zwiększenienia odchylenia standardowego prawdopodobieństwa "p" strategia "Check" nadal jest najbardziej opłacalna, chociaż jej przewaga zmniejszyła się. Strategia "Ignore" zyskała na konkurencyjności.

Analiza wzrostu kosztów decyzji "Check" pozwoliła określić maksymalne koszty, przy których strategia "Check" pozostaje optymalna. Maksymalny koszt to 1,70 - po przekroczeniu którego opłacalne staje się przyjęcie strategii "Fix".

Strategia "Ignore" stałaby się optymalna, gdyby kara za powiązanie dużych błędów w kodzie z firmą wynosiła mniej niż 17 (obecny koszt - 30).  

Redukcja kary za powiązanie niewielkich błędów w kodzie z firmą sprawiłaby, że strategia "Check" stałaby się jeszce bardziej atrakcyjna w porównaniu do innych strategii.





## Autor

Projekt został stworzony przez Cezarego Panasa.

---

### Dodatkowe Informacje

`graph.py` obejmuje: 
- utworzenie grafu, 
- funkcję kalkulującą prawodpodobienstwa wystąpienia konkretnych stanów świata po wybraniu odpowiedniej strategii oraz odpowiadające im skumulowane koszty,
- funkcję dokonującą symulacji w oparciu zakłócenia paremtrów (prawdopodobieństw zdarzeń p,q i r 0 w oparciu o cenzurowane rozkłady normalne,
- funkcję rysującą wykresy

`simulation.py`
- wykorzustuje funkcję "run_simulation_analisis" z pliku `graph.py` która przyjmuje jako argumenty opisane w treści zadania parametry oraz generuje histogramy wraz z oszacowaniami jądrowymi gęstości dla każdej strategii, a także dystrybuanty rozkładu prawdopodobieństwa każdej ze strategii na jednym wykresie.  

`sensitivity_analisis.py`
- Przeprowadza analizę wrażlwości kopiując orginalny graf i zmieniając wartośc konkretnego partametru w pętli 
  





