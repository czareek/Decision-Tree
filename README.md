# Projekt Analizy Decyzyjnej w Kontekście Zarządzania Ryzykiem Oprogramowania

## Wprowadzenie

Projekt stanowi kompleksową analizę dotyczącą wyboru optymalnego rozwiązania w  warunkach niepewności. Model w oparciu o ocenę ekspercką oraz symulacje numeryczne, pozwala zwizualizować potencjalne konsekwencje poszczególnych strategii.

## Opis Problemu

Firma XYZ stoi przed trudnym wyborem, mając do rozważenia trzy scenariusze w związku z wadliwym oprogramowaniem. Oto szczegółowy opis każdej opcji: **Zignorowanie problemu ("Ignore")**: Brak kosztów początkowych. Istnieje ryzyko, że błędy w oprogramowaniu okażą się poważne (40% szans), co skutkuje karą 30 milionów dolarów, lub niewielkie (60% szans) z karą 20 mln dolarów. Zaletą jest brak kosztów przy braku przypisania błędów do firmy. **Badanie kodu ("check")**: Koszty badania wynoszą 1 mln dolarów. Istnieje ryzyko, że błędy w oprogramowaniu okażą się poważne po badaniach (40% szans), co skutkuje koniecznością naprawy (ze względu na presję ze strony pracowników) za 10 mln dolarów plus koszty badań, lub niewielkie (60% szans). W takiej sytuacji zgodnie z polityką firmy jedyną dostępną opcją będzie zignorowanie problemu. **Hotfix ("Fix")**: Koszty początkowe wynoszą 3 mln dolarów. W trakcie przeprowadzania hotfixu może się okazac, że błędy będą poważne (dodatkowe 7 mln dolarów), lub niewielkie (dodatkowe 2 mln dolarów). 

## Implementacja Kodu

Kod został napisany w języku Python i wykorzystuje biblioteki takie jak NetworkX, NumPy i Matplotlib do symulacji i wizualizacji danych. Problem decyzyjny został sprowadzony do grafu skierowanego. Następnie wyniki symulacji poddano analizie wrażliwości, która pozwalaja na głębszą eksplorację scenariuszy decyzyjnych i zrozumienia problemu.

## Analiza Wrażliwości

Projekt przeprowadza analizę wrażliwości na zmianę odchylenia standardowego prawdopodobieństwa wystąpienia poważnych błędów w kodzie oraz na wzrost kosztów przeprowadzenia badania kodu "Check". Ponadto, analizuje on wpływ zmiany kary za błędy na opłacalność poszczególnych strategii.

## Wyniki Analizy

Po przeprowadzeniu symulacji stwierdzono, że strategia "Check" wygrywa najczęściej,następnie strategia "Fix" podczas gdy strategia "Ignore" jest silnie zdominowana przez pozostałe. Szczegółowe wyniki analizy oraz ich interpretację znajdziesz w raporcie `raport.pdf`.


## Autor

Projekt został stworzony przez Cezarego Panasa.

---

### Dodatkowe Informacje

Pełny opis problemu oraz metodologia analizy znajdują się w raporcie `raport.pdf`.

Szczegółowe fragmenty analizy w kodzie można znaleźć w następujących miejscach:
- Funkcja obliczająca potencjalne stany świata (prawdopodobieństwo że skończymy w konkretnym węźle końcowym po wybraniu konkretnej strategii oraz koszty które poniesie firma) znajduje się w pliku `graph.py` w linijkach [60-83]([https://github.com/czareek/Decision-Tree/edit/main/README.md](https://github.com/czareek/Decision-Tree/blob/main/graph.py)).
- Funkcja symulująca analizę znajduje się w pliku `graph.py` w linijkach [86-144](https://github.com/czareek/Decision-Tree/blob/main/graph.py).
- Analiza wrażliwości na zmianę odchylenia standardowego znajduje się w pliku `sensitivity_analisis.py` w linijkach [146-180](https://github.com/czareek/Decision-Tree/blob/main/sensitivity_analisis.py).
- Analiza kosztów przy wzroście kosztu decyzji "Check" znajduje się w pliku `sensitivity_analisis.py` w linijkach [182-222](https://github.com/czareek/Decision-Tree/blob/main/sensitivity_analisis.py).
- Analiza wpływu zmiany kary za błędy na opłacalność strategii znajduje się w pliku `sensitivity_analisis.py` w linijkach [224-269](https://github.com/czareek/Decision-Tree/blob/main/sensitivity_analisis.py).
- Analiza wszystkich prawdopodobieństw znajduje się w pliku `main.py` w linijkach [271-315](https://github.com/czareek/Decision-Tree/blob/main/sensitivity_analisis.py).

