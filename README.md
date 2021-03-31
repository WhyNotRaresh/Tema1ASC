Nume:   Badita Rares Octavian
Grupă:  333CB

# Tema 1 ASC

Organizare
-
Tema a fost realizată prin gestionare unor cozi de catre clasa marketplace.
Nu există interacțiune directă între producători și consumatori.

Fiecărui producător îi este asociată o coadă în care poate adauga poduse doar dacă aceasta nu este plină,
prin accesul funcției:
```python
def publish(self, producer_id: int, product: Product) -> bool
```

Fiecare consumator își crează un nou coș de cumpărături atunci când are de procesat o comandă nouă.
Asupra coșului său, un consumator poate executa 2 comenzi:
1. pentu a adăuga un produs nou in coș, funcția ciclează prin toate cozile și verifică capul cu produsul
   pe care el îl caută. Funcția intoarce ```True``` dacă produsul a fost adăugat in coș:
   ```python
   def add_to_cart(self, cart_id: int, product: Product) -> bool
   ```
1. pentru a șterge un produs din coș, funcția încearcă să șteargă produsul din coș, iar dacă reușește produsul este
   introdus într-o coada separată de produse care nu sunt nici ale unui producător, dar nici într-un coș:
   ```python
   def remove_from_cart(self, cart_id: int, product: Product) -> None
   ```

Implementare
-

* Tema este realizată integral (toate cele 10 teste publice îmi trec pe mașina locală).
* Pentru că tema am facut-o pe Windows, in [run_tests.sh](https://github.com/WhyNotRaresh/Tema1ASC/blob/master/assignments/1-marketplace/skel/run_tests.sh)
  am schimbat executabilul din ```PYTHON_CMD=python3``` în ```PYTHON_CMD=py```.

Resurse utilizate
-

* Pentru lucrul cu cozi am utilizat pagina de manual: https://docs.python.org/3/library/queue.html
* Pentru a face acest README și pentru a învăța despre markdown: https://guides.github.com/features/mastering-markdown/

[Github](https://github.com/WhyNotRaresh/Tema1ASC)
-