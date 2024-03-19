# Projekt Analizy Decyzyjnej w Kontekście Zarządzania Ryzykiem Oprogramowania

## Wprowadzenie

Projekt ten stanowi kompleksową analizę decyzyjną dotyczącą zarządzania ryzykiem wadliwego oprogramowania dla firmy XYZ. W oparciu o raport opracowany przez ekspertów oraz symulacje numeryczne, przedstawia on strategie podejmowane przez firmę w zależności od potencjalnych konsekwencji.

## Opis Problemu

Firma XYZ stoi przed trudnym wyborem, mając do rozważenia trzy scenariusze związane z wadliwym oprogramowaniem. Obejmują one ignorowanie problemu, przeprowadzenie badania kodu lub zastosowanie hotfixu. Każda z tych opcji niesie za sobą różne koszty początkowe i ryzyko wystąpienia poważnych błędów.

## Implementacja Kodu

Kod został napisany w języku Python i wykorzystuje biblioteki takie jak NetworkX, NumPy i Matplotlib do symulacji i wizualizacji danych. Znajdziesz tu także zaawansowane funkcje analizy wrażliwości, które pozwalają na eksplorację różnych scenariuszy decyzyjnych.

## Analiza Wrażliwości

Projekt przeprowadza analizę wrażliwości na zmianę odchylenia standardowego prawdopodobieństwa wystąpienia poważnych błędów w kodzie oraz na wzrost kosztów decyzji "Check". Ponadto, analizuje on wpływ zmiany kary za błędy na opłacalność poszczególnych strategii.

## Wyniki Analizy

Po przeprowadzeniu symulacji stwierdzono, że strategia "Check" wygrywa najczęściej,następnie strategia "Fix" podczas gdy strategia "Ignore" jest silnie zdominowana przez pozostałe. Szczegółowe wyniki analizy oraz ich interpretację znajdziesz w raporcie `raport.pdf`.

## Uruchomienie Projektu

Aby uruchomić projekt lokalnie, wykonaj następujące kroki:

1. Upewnij się, że masz zainstalowane wymagane biblioteki

## Autor

Projekt został stworzony przez Cezarego Panasa.

---

### Dodatkowe Informacje

Pełny opis problemu oraz metodologia analizy znajdują się w raporcie `raport.pdf`.

Szczegółowe fragmenty analizy w kodzie można znaleźć w następujących miejscach:
- Funkcja obliczająca potencjalne stany świata (prawdopodobieństwo że skończymy w konkretnym węźle końcowym po wybraniu konkretnej strategii oraz koszty które poniesie firma) znajduje się w pliku `graph.py` w linijkach [60-83](https://github.com/username/repository/blob/branch/main.py#L60-L83).
- Funkcja symulująca analizę znajduje się w pliku `graph.py` w linijkach [86-144](https://github.com/username/repository/blob/branch/main.py#L86-L144).
- Analiza wrażliwości na zmianę odchylenia standardowego znajduje się w pliku `main.py` w linijkach [146-180](https://github.com/username/repository/blob/branch/main.py#L146-L180).
- Analiza kosztów przy wzroście kosztu decyzji "Check" znajduje się w pliku `main.py` w linijkach [182-222](https://github.com/username/repository/blob/branch/main.py#L182-L222).
- Analiza wpływu zmiany kary za błędy na opłacalność strategii znajduje się w pliku `main.py` w linijkach [224-269](https://github.com/username/repository/blob/branch/main.py#L224-L269).
- Analiza wszystkich prawdopodobieństw znajduje się w pliku `main.py` w linijkach [271-315](https://github.com/username/repository/blob/branch/main.py#L271-L315).

