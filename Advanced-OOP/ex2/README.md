## Typy generyczne

[Typy generyczne](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/generics/) pozwalają na opóźnienie w dostarczeniu specyfikacji typu danych w elementach takich jak klasy czy metody do momentu użycia ich w trakcie wykonywania programu. Innymi słowy, typy generyczne pozwalają na napisanie klasy lub metody, która może działać z każdym typem danych.

Informacje potrzebne na dzisiejszym laboratorium:

- [Typy generyczne w C#](https://www.tutorialsteacher.com/csharp/csharp-generics)
- [Ograniczenia typów generycznych w C#](https://www.tutorialsteacher.com/csharp/constraints-in-generic-csharp)
- [Kolekcje generyczne](https://www.tutorialsteacher.com/csharp/csharp-generic-collections)



Przykład metody generycznej zamieniającej 2 elementy.

```c#
static void Swap<T>(ref T input1, ref T input2)
{
    T temp = default(T);
 
    temp = input2;
    input2 = input1;
    input1 = temp;
}
 
static void Main(string[] args)
{
    int first = 4;
    int second = 5;
 
    Swap<int>(ref first, ref second);
}
```

## Zadania (20 pkt + 5 dodatkowych)

### Zad1 (5pkt)

Napisz metodę generyczną, która łączy (concatenate) elementy kolekcji w jednego stringa i go zwraca. Poniżej zachowanie dla przykładowego inputu

```c#
int[] integers = { 1, 2, 3, 4, 5 };
char[] characters = { 'a', 'b', 'c', 'd', 'e', 'f' };
List<string> strings = new List<string>{"This", " class", " is", " awesome"};
Console.WriteLine(ConcatenateCollection(strings));
Console.WriteLine(ConcatenateCollection(characters));
Console.WriteLine(ConcatenateCollection(integers));
// Output:
// 12345
// abcdef
// This class is awesome
```

### Zad2 (15pkt + możliwość zdobycia 5 pkt dodatkowych)

Zaimplementuj rozwiązanie wykorzystujące algorytm Dijkstry dla poniższego problemu. Przykład pseudokodu reprezentującego algorytm Dijkstry znajduje się [tutaj](https://pl.wikipedia.org/wiki/Algorytm_Dijkstry). 

W zadaniu poza poprawnością punktowana będzie architektura aplikacji. Proszę stworzyć aplikację zgodnie z paradygmatami programowania obiektowego i wykorzystać poznane na zajęciach mechanizmy (LINQ/typy anonimowe/typy generyczne) - w ramach rozsądku - nic na siłę. Przykładowe użycie tych mechanizmów/zgodność z paradygmatami:

- Reprezentacja miasta (wierzchołka) poprzez klasę z odpowiednimi polami.
- Wykorzystywanie mechanizmów kolekcji generycznych do konkretnych typów obiektów - np. stworzenie listy miast/wierzchołków.
- Przeszukiwanie listy miast z wykorzystaniem LINQ i typów anonimowych.
- Reprezentacja grafu/sieci miast za pomocą klasy z odpowiednimi polami (np. lista wierzchołków, lista krawędzi)

#### Dodatkowe punkty

Za zaimplementowanie grafu dla algorytmu Dijkstry za pomocą kopca można uzyskać dodatkowe 5 punktów. Okazuje się to być bardzo efektywne. Uzyskujemy wtedy dużo mniejszą złożoność obliczeniową. 

---

### Treść zadania

Dana jest lista miast. Każde bezpośrednie połączenie pomiędzy dwoma miastami ma stowarzyszony z nim koszt (liczba całkowita większa niż 0). Celem jest znalezienie ścieżek o minimalnym koszcie pomiędzy parami miast. Zakładamy, że koszt każdej ścieżki (liczony jako suma kosztów wszystkich bezpośrednich połączeń należących do ścieżki) wynosi co najwyżej 200000. Nazwa każdego miasta to napis złożony ze znaków a,...,z o długości co najwyżej 10.

#### Wejście

```pseudocode
s [liczba przypadków testowych <= 10]
n [liczba miast <= 10000]
NAME [nazwa miasta]
p [liczba miast sąsiednich do miasta NAME]
nr cost [nr - numer miasta połączonego z miastem NAME (indeks pierwszego miasta to 1)]
           [cost - koszt połączenia]
r [liczba ścieżek do znalezienia <= 100]
NAME1 NAME2 [NAME1 - nazwa miasta startowego, NAME2 - nazwa miasta docelowego]
[pusta linia odziela przypadki testowe]
```

#### Wyjście

```
cost [koszt optymalnego połączenia pomiędzy miastami NAME1 i NAME2 (w osobnych liniach)]
```

### Przykład

```
Wejście:
1
4
gdansk
2
2 1
3 3
bydgoszcz
3
1 1
3 1
4 4
torun
3
1 3
2 1
4 1
warszawa
2
2 4
3 1
2
gdansk warszawa
bydgoszcz warszawa

Wyjście:
3
2
```

### Testy

W katalogu z zadaniem znajduje się skompresowany plik [testy.zip](testy.zip) z testami sprawdzającymi poprawność algorytmu. Zawiera on pliki input oraz output. Input to plik z danymi wejściowymi, a output z wyjściem odpowiadającym temu wejściu.

Sprawdzenie swojego kodu:

``program.exe < input > moj_output``

Następnie za pomocą dowolnego narzędzia (np Notepad++ ma do tego funkcję) możemy sprawdzić czy pliki ``moj_output`` oraz ``output`` mają dokładnie taką samą zawartość.

