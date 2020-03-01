## Funkcje anonimowe
[Funkcje anonimowe (Wyrażenia lambda)](https://pl.wikipedia.org/wiki/Funkcja_anonimowa) to definicje funkcji, które nie są powiązane z identyfikatorem.  
W C# możemy wyróżnić 2 rodzaje  
* Expression lambda
```c#
(input-parameters) => expression
```
Przykład:
```c#
Func<int, int> square = x => x * x;
Console.WriteLine(square(5));
// Output:
// 25
```
***
* Statement lambda
```c#
(input-parameters) => { <sequence-of-statements> }
```
Przykład:
```c#
Action<string> greet = name => 
{ 
    string greeting = $"Hello {name}!";
    Console.WriteLine(greeting);
};
greet("World");
// Output:
// Hello World!
```
Najczęstsze użycie funkcji anonimowych (wyrażeń lambda) to wykorzystywanie jako argumenty funkcji wyższego rzędu. Konkretnie w kontekście języka C# funkcjami wyższego rzędu są często zapytania LINQ.
## LINQ
[Language Integrated Query (LINQ)](https://pl.wikipedia.org/wiki/LINQ) to część technologii Microsoft .NET umożliwiająca tworzenie zapytań na obiektach. Składnia przypomina język SQL.  
[Oficjalna dokumentacja](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/)  
Przykład zastosowania LINQ wraz z wyrażeniem lambda (funkcją anonimową):
```c#
var Numbers = new int[] { 0, 5, 6, 7, 236, 2643743 };
var Results = Numbers.Where(x => x > 6);
```
Na kolekcji ``Numbers`` wykorzystujemy operator LINQ ``Where``, którzy zwraca nam kolekcję spełniającą warunek ``x => x > 6`` (będący wyrażeniem lambda). Warunek ten oznacza - "iksy, dla których x jest większe niż 6".
Zatem reasumując, połączenie powyższego zapytania LINQ oraz wyrażenia lambda pozwala nam zwrócić wszystkie elementy kolekcji będące większe niż 6.

## Zadania (20 pkt)
### Zad1 (4pkt)
Dla następującego zbioru liczb ``{ 1195, 843, 1950, 1044, 1374, 1218, 181, 1941, 669, 1770, 1515, 1393, 594, 93, 632, 1638, 1417, 1636, 973, 1821, 682, 696, 1076, 898, 453, 167, 562, 339, 568, 281, 1074, 1213, 847, 849, 1268, 1089, 833, 28, 1347, 1526, 1129, 461, 1629, 1426, 670, 689, 712, 783, 742, 499 }``
korzystając z LINQ znajdź
* Liczbę najmniejszą
* Liczbę największą
* Podzbiór liczb parzystych
* Największą liczbę podzelną przez 7
* Pierwszą liczbę parzystą w zbiorze
* Posortowany podzbiór liczb mniejszych niż 1500
### Zad2 (4pkt)
Stwórz klasę ``Student`` posiadającą pola, które widać w poniższym tworzeniu listy. Następnie stwórz taką listę i znajdź dla niej:
* Imię najstarszego studenta
* Posortowaną po imieniu listę studentów
* Listę studentów z nieparzystym ``StudentID``
* Stwórz w klasie student metodę ``void Greet()``, która wypisuję powitanie ``Hi I am {this.StudentName}``.
Następnie korzystając z [ForEach](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1.foreach?view=netframework-4.8) wykonaj tą metodę na każdym studencie niepochodzącym z Niemiec.
```c#
List<Student> studentList = new List<Student>() { 
    new Student() { StudentID = 1, StudentName = "John", Age = 18, Country = "Poland"  } ,
    new Student() { StudentID = 2, StudentName = "Steve",  Age = 22, Country = "Poland"  } ,
    new Student() { StudentID = 3, StudentName = "Bill",  Age = 18, Country = "USA"  } ,
    new Student() { StudentID = 4, StudentName = "Ram" , Age = 20, Country = "USA"  } ,
    new Student() { StudentID = 5, StudentName = "Ron" , Age = 21, Country = "Germany"  } 
};
```
### Zad3 (4pkt)
Wykorzystując LINQ wypisz wszystkie imiona i nazwiska wszystkich osób z poniższej listy, które spełniają przynajmniej 1 z poniższych warunków:
* Imię to Joe lub Bob
* Nazwisko to Smith
```c#
var fullNameList = new List<string>();
fullNameList.Add("Joe Thompson"):
fullNameList.Add("Bob Jones");
fullNameList.Add("Bob Smith");
fullNameList.Add("Billy Smith");
fullNameList.Add("Joe Williams");
fullNameList.Add("Joe Joejoe");
fullNameList.Add("Adam Malysz");
fullNameList.Add("Bob Bobovich");
```
### Zad4 (4pkt)
Wykorzystując LINQ wypisz z poniższej tablicy nazwiska osób posiadających przynajmniej 3 samogłoski w imieniu
```c#
string [] names = { "Adam Malysz",  
                    "Mariusz Pudzianowski",  
                    "Steven Seagal",  
                    "Chuck Norris",  
                    "Gianluigi Buffon",  
                    "Jan Kowalski",  
                    "Tadeusz Iksinski",  
                    "John Smith"  
                  };              
```
### Zad5 (4pkt)
Następujący string reprezentuje punkty zawodnika (oddzielone przecinkami) zdobyte w kolejnych zawodach w pewnym sporcie: ``"10,5,0,8,10,1,4,0,10,1"``.
W zasadach tego sportu 4 najgorsze rezultaty punktowe są odrzucane. Oblicz sumę punktów. Jedynie jednolinijkowe rozwiązania z wykorzystaniem LINQ będą akceptowane (w celu rozwiania wątpliwości - wyliczenie sumy jednolinijkowe. Prezentacja rezultatu może być w osobnej linii).
