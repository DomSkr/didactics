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

## Wybrane zagadnienia programowania równoległego/asynchronicznego

### Async/Await

[Task asynchronous programming model (TAP)](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/async/) dostarcza abstrakcję, która pozwala tworzyć asynchroniczny kod. Kod pisany w taki sposób jest standardową sekwencją poleceń. Można więc myśleć, iż wykonywane są one po kolei (kolejne wykonywane jest dopiero, gdy poprzednie się skończy). Jednakże kompilator dokonuje pewnych transformacji, za pomocą których  zamienia niektóre polecenia na zadania (ang. Task), które reprezentują wykonującą się pracę. W modelu tym używamy słów kluczowych ``async``, ``await`` oraz ``Task``. 

Definiując metodę, możemy użyć słowa kluczowego ``async``. Pozwala to nam na późniejsze użycie słowa kluczowego ``await``, które umożliwia nam na pewnego rodzaju czekanie na odpowiedź poszczególnych poleceń (asynchroniczne wykonanie kodu). Bez słowa kluczowego ``await`` metoda zdefiniowana ze słowem kluczowym ``async`` będzie normalną metodą synchroniczną.

W poniższym fragmencie kodu mamy metodę ``static async Task<float> CalculateTotalAfterTaxAsync(float value)``. ``Task<float>`` oznacza, iż metoda zawiera asynchroniczne (o ile wewnątrz metody używamy ``await``) zadanie zwracające typ ``float``. Jest ono zdefiniowany za pomocą ``var result = await Task.Run(() => value * 1.2f);``. Analizując tekst wypisywany na standardowe wyjście możemy zauważyć, iż rzeczywiście kod z metody asynchronicznej, na który czekamy wykonał się w tle. Główna metoda programu (``Main``) czeka na skończenie się asynchronicznej funkcji za pomocą ``totalAfterTax.Wait();``. 

```c#
using System;
using System.Threading.Tasks;

namespace AsyncApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("1.Doing some synchronous work");
            var totalAfterTax = CalculateTotalAfterTaxAsync(70);
            DoSomethingSynchronous();
            Console.WriteLine("5.Doing some synchronous work in Main again!");

            totalAfterTax.Wait();
            Console.ReadLine();
        }

        private static void DoSomethingSynchronous()
        {
            Console.WriteLine("4.Doing some synchronous work in method");
        }

        static async Task<float> CalculateTotalAfterTaxAsync(float value)
        {
            Console.WriteLine("2.Started CPU Bound asynchronous task on a background thread");
            var result = await Task.Run(() => value * 1.2f);
            Console.WriteLine($"3.Finished Task. Total of ${value} after tax of 20% is ${result} ");
            return result;
        }
    }
}
```

Output:

```
1.Doing some synchronous work
2.Started CPU Bound asynchronous task on a background thread
4.Doing some synchronous work in method
5.Doing some synchronous work in Main again!
3.Finished Task. Total of $70 after tax of 20% is $84 
```

### [Parallel Class](https://docs.microsoft.com/en-us/dotnet/api/system.threading.tasks.parallel?view=netframework-4.8)

Klasa Parallel wprowadzona w .NET frameworku 4.8 umożliwia wykonywanie iteracji pętli for oraz foreach równolegle. Przykładowe użycie:

```c#
void RotateMatrices(IEnumerable<Matrix> matrices, float degrees)
{
    Parallel.ForEach(matrices, matrix => matrix.Rotate(degrees));
}
```

## Zadania

### Zad1 (5pkt)

Sprawdź, że typowanie dynamiczne pozwala na uruchomienie kodu, w którym używamy metod nieistniejących (wywołaj runtime exception) 

### Zad2 (7pkt + dodatkowe 3pkt za interfejs graficzny)

Biblioteka ``System.Net.Http`` zawiera klasę ``HttpClient``. W niniejszym zadaniu wykorzystamy z tej klasy metodę ``GetStringAsync(string requestUri)``, która pozwala zczytać zawartość strony internetowej do zmiennej typu ``string``.

Proszę napisać aplikację konsolową z wykorzystaniem ``async`` i ``await``, która zapyta użytkownika o url strony  internetowej, a następnie asynchronicznie zczyta tą stronę do zmiennej i wyświetli użytkownikowi liczbę znaków znajdującą się na tej stronie. Podczas oczekiwania związanego z zczytywaniem strony proszę wyświetlić na standardowym wyjściu jakiś zapętlony komunikat związany z oczekiwaniem. W ogólności aplikacja ma symulować to, iż nie blokujemy interfejsu użytkownika podczas tego typu zapytań (dzieją się w tle). 

Dodatkowe 3 punkty można uzyskać jeśli zrobi się aplikację z interfejsem (a nie konsolową). Może być dowolna technologia (WPF/Windows Forms/inne). Wtedy nie trzeba wyświetlać komunikatu. Wystarczy to, iż interfejs będzie używalny w czasie wykonywania zapytania w tle.



### Zad3 (8pkt)

Napisz program zgodnie z zasadami programowania obiektowego zawierający klasy ``Figura`` (abstrakcyjna) oraz ``Kwadrat``, ``Prostokąt``, ``Koło`` dziedziczące po klasie ``Figura``. Każda z tych klas niech zawiera pola ``Pole``, ``Obwód``, ``Nazwa`` (zdefiniowany przez użytkownika string podawany w konstruktorze) oraz swoje specyficzne pola definiujące np. długość boku, czy promień. Ponadto, proszę zaimplementować metody liczące pola i obwody poszczególnych klas (przypisujące wartości polom ``Pole`` i ``Obwód``) oraz metodę typu getter zwracającą ``ValueTuple<double, double, string>`` z wartoścami pola, obwodui nazwy.

W funkcji ``Main`` proszę stworzyć po kilka obiektów z każdej klasy, dodać je do listy ``List<Figura>``. Następnie wykonać równolegle (za pomocą ``Parallel.ForEach`` lub ``Parallel.For``) dla każdego elementu z listy metody liczące pola i obwody. Na końcu proszę sekwencyjnie wypisać obwód, pole i nazwę każdej z figur (wartości pobierając z metody korzystającej z ValueTuple wspomnianej wcześniej).



Jeśli nie mają Państwo odpowiedniej wersji C# (przynajmniej 7.0), to proszę skorzystać z internetowego kompilatora https://ideone.com/.