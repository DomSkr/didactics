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

## Zadania (20 pkt)

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

### Zad2 (5pkt)

### Zad3 (10pkt - grafy)