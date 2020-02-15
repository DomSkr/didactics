# MPI - Message Passing Interface

### Standard komunikacji międzyprocesowej
Message Passing Interface (MPI, z ang., interfejs transmisji wiadomości) – protokół komunikacyjny będący standardem
przesyłania komunikatów pomiędzy procesami programów równoległych działających na jednym lub więcej komputerach.
Interfejs ten wraz z protokołem oraz semantyką specyfikuje, jak jego elementy winny się zachowywać w dowolnej implementacji.
Celami MPI są wysoka jakość, skalowalność oraz przenośność. MPI jest dominującym modelem wykorzystywanym obecnie w
klastrach komputerów oraz superkomputerach.

#### Zrozumieć różnicę
W pierwszym laboratorium pisaliśmy aplikację, która tworzyła nowe wątki i pilnowała by sekcje krytyczne były wykorzystywane przez jeden wątek.
Napisanie aplikacji z wykorzystaniem biblioteki implementującej standard MPI to działanie na poziomie procesu, wymienianie danych między nimi i odpowiednie zbieranie wyników.
Aplikacje napisane w oparciu o MPI mogą działać w obrębie jednego komputera lub też na wielu maszynach (klastrach) poprzez sieć komputerową.

#### Szczegóły implementacyjne
Aplikacje oparte o MPI muszą być odpowiednio napisane na poziomie kodu - to jest z wykorzystaniem odpowiednich funkcji i mechanizmów standardu.
Podstawowym podejściem jest tutaj rozbicie pracy na mastera i slave'ów. Master będzie procesem, który rozdziela pracę, wypisze wynik końcowy etc zaś
slave będą procesami, które faktycznie będą wykonywać zadanie obliczeniowe, a wynik zwracać masterowi.

Standard MPI jest zaimplementowany w wielu współczesnych językach programowania. Student otrzymuje pełną dowolność odnośnie języka i implementacji MPI, którą chce użyć w ramach laboratorium.
W ramach tej instrukcji pojawią się dwa przykłady - jeden w Pythonie, drugi w C++.

#### Literatura
- [Dokumentacja biblioteki mpi4py](https://mpi4py.readthedocs.io/en/stable/index.html)
- [Uruchamianie aplikacji napisanych w mpi4py](https://mpi4py.readthedocs.io/en/stable/tutorial.html#running-python-scripts-with-mpi)
- [Opis protokołu MPI](https://pl.wikipedia.org/wiki/Message_Passing_Interface)
- [Dokumentacja biblioteki OpenMP](https://pl.wikipedia.org/wiki/OpenMP) (użyta w przykładzie w języku C++)


### Przykłady i zadania wstępne
Przykłady mogą być budowane i uruchamiane na maszynie wirtualnej dostarczonej do przedmiotu (patrz moodle).
#### 1. Python - sortowanie

Kod przykładu znajduje się w pliku `sort.py` (katalog sort)
Uruchomienie przykładu (po wcześniejszej instalacji MPI, mpi4py, numpy) jest możliwe za pomocą:
```bash
mpiexec -n 2 python3 sort.py
```
Wartość n=2 ustawia w powyższej linijce ilość procesów na dwa.
Pierwszym z nich będzie master, który rozlosuje liczby do posortowania a następnie prześle do drugiego procesu zbiór do posortowania.
Drugi proces wykona sortowanie i odeśle wynik.

a) Uruchom powyższy przykład na dwóch procesach. Jaki jest wynik, co się stało i dlaczego?

b) Uruchom powyższy przykład na jednym procesie. Jaki jest wynik, co się stało i dlaczego?
 
c) Uruchom powyższy przykład na tylu procesach ile masz procesorów w systemie. Wykonaj zrzut ekranu z managera zadań (lub z programu `htop` jeśli pracujesz na linuxie) z listy procesów i z poziomu zużycia CPU.
Przynieś zrzut na zajęcia dbając jednocześnie by było widać, że jesteś jego autorem (na przykład w tle widać że jesteś zalogowany na swoje konto studenckie).

d) Uruchom powyższy przykład na tylu procesach ile masz procesorów * 4. Co można powiedzieć o czasie wykonania w stosunku do poprzednich uruchomień?
W systemie linux czas można zmierzyć za pomocą:
```bash
time YOUR COMMAND HERE (fox example mpiexec)
```

#### 2. Przykład drugi - atak słownikowy
Na początek poczytaj czym jest [etyczny hacking](http://panmore.com/ethical-hacking-code-of-ethics-security-risk-issues) i nie używaj zdobytej tu wiedzy do robienia złych rzeczy.

Rozważmy następującą sytuację i ustalmy następujące założenia:
- Następuje wyciek bazy danych z serwisu X. Jako haker zdobywasz zrzut tej bazy danych.
- W zrzucie znajdujesz zaszyfrowane hasło pewnego użytkownika. 
`HASH` tego hasła to
```eceae5d000a33657f4fa2c474328ae07558748bbdb2fd02015d356c22caf0dd5f79a156e2b2900f6feb4a9cacef8ab3218749c45358eaaea9734a8f13f72d34b``` 
Zaś jego `salt` to ```bG4kBv```.
Jeśli nie rozumiesz powyższych pojęć, bądź chcesz się doszkolić z tematu bezpieczeństwa haseł to przeczytaj ten [artykuł](https://crackstation.net/hashing-security.htm).
- Przy tworzeniu nowego konta na stronie X zauważasz, że wymaganiem co do trudności hasła jest: *Dokładnie 3 małe litery (bez cyfr i znaków specjalnych)*.
Oczywiście jest to szalenie niebezpieczne założenie, ustalamy je tylko dla uproszczenia.
W oparciu o to założenie przygotowujemy słownik wszystkich możliwych haseł. Znajduje się on w pliku `dictionary.txt`.
- Piszemy aplikację, która pozwoli nam przeprowadzić atak słownikowy na podane wyżej `HASH` i `salt`. Aplikacja ma działać na wielu procesach (MPI).
Kod programu dostarczony jest w pliku `cracker.cpp`. Detale implementacyjne:
    - Serwis X jest opublikowany w internecie w oparciu o opensource'owy system blogowy. Oznacza to, że udało się przejrzeć algorytm szyfrujący hasła w kodzie systemu blogowego na githubie.
    - Przy rejestracji hasło jest najpierw szyfrowane algorytmem MD5 a hash wynikowy używane jest jako wejście do algorytmu SHA512. Wynik SHA jest zapisywany do bazy danych. Salt nie jest używany. (linia 109 w cracker.cpp)
    - Przy pierwszym logowaniu nadawany jest `salt` a następnie wykonanych zostaje `100000` rund hashowania z użyciem nadanego `salt`. Jest to ostateczny hash. (linie 96 i 112 w cracker.cpp)
    - Zauważmy, że część kodu, którą chcemy zrównoleglić to hashowanie poszczególnych słów ze słownika i ich porównywanie z zadanym hashem. Zaczyna się to dziać w lini 70 w cracker.cpp.
    - Oczywiście można napisać program używając mastera i slave'ów (podobnie jak w pierwszym przykładzie), ale ten przykład ma zademonstrować zrównoleglanie pętli. Kluczową linią, która zapewni nam równoległość jest tutaj linia 69:
    ```cpp
      # pragma omp parallel for private(word) shared(found) schedule(dynamic)
    ```
    Wskazuje ona, że `word` jest zmienną prywatną w obrębie procesu, zaś zmienna found jest dzielona między procesy - ustawienie jej na 1 oznacza, że któryś z wątków znalazł hash i program się zakończy (linia 73). To biblioteka `omp` zadba o po prawną pracę sekcji krytycznej.
    Pętla rozpoczęta od tej linijki będzie uruchamiała się równolegle na tylu procesach, ile wskażemy przy uruchamianiu programu.

##### Zadania do wykonania
a) Zbudować załączony program. Na linuxie można osiągnąć to za pomocą:
```
g++ cracker.cpp -fopenmp -lcrypto -std=c++11 -o pwcracker
```
b) Uruchomić zbudowany program używając dostarczonego słownika i podanego wyżej `hasha` oraz `salta`.
Efektem uruchomienia będzie "złamanie" hasła. Na czterech rdzeniach program powinien wyrobić się w 2 godziny. Jeśli masz wyjątkowo wolny komputer to możesz wyrzucić pierwszą połowę słownika (poprawne hasło jest w jego drugiej połowie :)).

c) Wykonaj zrzut ekranu na którym widać końcówkę outputu z programu i rozszyfrowane hasło. Zrzut ekranu ma jednoznacznie identyfikować studenta - niech w tle będzie widać np zalogowanie na profil studenta na stronie WSB. Przynieś zrzut na zajęcia.

Uwaga: liczbę procesów ustawiamy za pomocą zmiennej środowiskowej `OMP_NUM_THREADS`:
```bash
export OMP_NUM_THREADS=4
```
Dobrym ustawieniem wydaje się ustawienie `OMP_NUM_THREADS` na ilość taką samą jak liczba dostępnych rdzeni procesora.


---


## Zadania laboratoryjne (10pkt)

### Zad1 (2pkt) - Screeny
#### a) (1pkt)
Zaprezentuj prowadzącemu screen z uruchomienia w domu pierwszego przykładu. Dodatkowe pytanie może zostać zadane.
#### b) (1pkt) 
Zaprezentuj prowadzącemu screen z uruchomienia w domu drugiego przykładu. Jakie było hasło? Dodatkowe pytanie może zostać zadane.

### Zad2 (2 pkt) - Modyfikacja sortowania
Niech slave oblicza sumę posortowanej tablicy. Jeśli jest parzysta niech posortuje ją odwrotnie i dopiero wtedy odeśle wynik. 


### Zad3 (6 pkt) - Kradzież nagłówków
W dowolnym języku programowania, używając dowolnej implementacji MPI napisz program realizujący poniższą funkcjonalność:
Należy utworzyć plik domains.txt, umieścić w pliku kilka adresów do stron internetowych, np:
```
https://wsb.zylowski.net/
https://wsb.zylowski.net/faq/
https://www.telegraph.co.uk/technology/6125914/How-20-popular-websites-looked-when-they-launched.html
```
Należy napisać program, który otworzy ten plik i dla każdej domeny:
- Odwiedzi stronę internetową i pobierze do pamięci jej zawartość
- Przeanalizuje treść strony i wypisze na ekran wszystkie nagłówki pierwszego i drugiego poziomu. (Zwartość tagów HTML ```<h1>, <h2>```)
Np dla strony:
```
https://www.telegraph.co.uk/technology/6125914/How-20-popular-websites-looked-when-they-launched.html
```
Są to:
```
How 20 popular websites looked when they launched
From Google to youtube, from craigslist to flickr - how some of today's biggest sites looked back in the early days of their existence.
Related Articles
Technology
```
Odwiedzanie i analiza strona ma zostać zrównoleglona. Np to master może odczytywać plik i delegować strony do otwarcia poszczególnym procesom.
Można też wykorzystać zrównolegloną pętlę.
