## Funkcje anonimowe
[Funkcje anonimowe (Wyrażenia lambda)](https://pl.wikipedia.org/wiki/Funkcja_anonimowa) to definicje funkcji, które nie są powiązane z identyfikatorem.  
W C# możemy wyróżnić 2 rodzaje  
* Expression lambda
```
(input-parameters) => expression
```
Przykład:
```
Func<int, int> square = x => x * x;
Console.WriteLine(square(5));
// Output:
// 25
```
***
* Statement lambda
```
(input-parameters) => { <sequence-of-statements> }
```
Przykład:
```
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
```
var Numbers = new int[] { 0, 5, 6, 7, 236, 2643743 };
var Results = Numbers.Where(x => x > 6);
```
Na kolekcji ``Numbers`` wykorzystujemy operator LINQ ``Where``, którzy zwraca nam kolekcję spełniającą warunek ``x => x > 6`` (będący wyrażeniem lambda). Warunek ten oznacza - "iksy, dla których x jest większe niż 6".
Zatem reasumując, połączenie powyższego zapytania LINQ oraz wyrażenia lambda pozwala nam zwrócić wszystkie elementy kolekcji będące większe niż 6.

## Zadania
### Zad1