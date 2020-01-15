## Typy dynamiczne

.NET 4.5 wprowadził dynamiczny typ, który omija sprawdzanie w trakcie kompilacji. Dzięki temu w trakcie działania programu możemy zmieniać typ danych zapisany w zmiennych. Statyczne typy są kompilowane przez środowisko uruchomieniowe. Typy dynamiczne są omijane przez kompilator, przechwytywane przez środowisko uruchomieniowe i obsługiwane w czasie działania programu.

```c#
int i = 100;// typowanie bezpośrednie - typ ustalony przez nas
var j = 100; // typowanie pośrednie - kompilator sam ustala typ
dynamic k = 100; // typowanie dynamiczne - kompilator pomija - nie ma typu
```

W środowisku uruchomieniowym (ang. runtime) możemy sprawdzić jakiego typu jest typ dynamiczny.

```c#
static void Main(string[] args)
{
    dynamic dynamicVariable = 1;

    Console.WriteLine(dynamicVariable.GetType().ToString());
    // Output: System.Int32
}
```

Dynamiczny typ może zmieniać swój typ w środowisku uruchomieniowym (ang. runtime).

```c#
static void Main(string[] args)
{
    dynamic dynamicVariable = 100;
    Console.WriteLine("Dynamic variable value: {0}, Type: {1}",dynamicVariable, dynamicVariable.GetType().ToString());
    // Output: Dynamic variable value: 100, Type: System.Int32

    dynamicVariable = "Hello World!!";
    Console.WriteLine("Dynamic variable value: {0}, Type: {1}", dynamicVariable, dynamicVariable.GetType().ToString());
	// Output: Dynamic variable value: Hello World!!, Type: System.String
    
    dynamicVariable = true;
    Console.WriteLine("Dynamic variable value: {0}, Type: {1}", dynamicVariable, dynamicVariable.GetType().ToString());
	// Output: Dynamic variable value: True, Type: System.Boolean
    
    dynamicVariable = DateTime.Now;
    Console.WriteLine("Dynamic variable value: {0}, Type: {1}", dynamicVariable, dynamicVariable.GetType().ToString());
    // Output: Dynamic variable value: 01-01-2014, Type: System.DateTime
}
```

Nadużywanie typów dynamicznych jest często złą praktyką, lecz warto wiedzieć o tej funkcjonalności.

## ValueTuples

.NET 4.7 (C# 7.0) wprowadził ValueTuple. Jest to krotka wartości przydatna, gdy np chcemy napisać funkcję zwracającą 2 parametry.

Inicjalizacja

```c#
var person = (1, "Bill", "Gates");
```

lub explicite definiując typy

```c#
ValueTuple<int, string, string> person = (1, "Bill", "Gates");
```

albo krócej

```c#
(int, string, string) person = (1, "Bill", "Gates");
```

Powyższe trzy sposoby inicjalizacji są tożsame. Odwoływanie się do konkretnych wartości przebiega następująco:

```c#
person.Item1;  // returns 1
person.Item2;   // returns "Bill"
person.Item3;   // returns "Gates"
```

Można nadawać nazwy konkretnym polom:

```c#
(int Id, string FirstName, string LastName) person = (1, "Bill", "Gates");
person.Id;   // returns 1
person.FirstName;  // returns "Bill"
person.LastName; // returns "Gates"
```

ValueTuple może również służyć jako typ zwracany.

```c#
static void Main(string[] args)
{
    // change property names
    (int PersonId, string FName, string LName) = GetPerson();
}
static (int, string, string) GetPerson() 
{
    return (Id:1, FirstName: "Bill", LastName: "Gates");
}
```

## Programowanie równoległe

Lorem ipsum

## Zadania

### Zad1 (5pkt)

Sprawdź, że typowanie dynamiczne pozwala na uruchomienie kodu, w którym używamy metod nieistniejących (wywołaj runtime exception) 

### Zad2 (15pkt)

Napisz program z (TODO: ValueTuple + parallell)

Jeśli nie mają Państwo odpowiedniej wersji C# (przynajmniej 7.0), to proszę skorzystać z internetowego kompilatora https://ideone.com/.