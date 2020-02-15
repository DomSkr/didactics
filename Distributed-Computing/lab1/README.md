## 	Wybrane zagadnienia programowania równoległego/asynchronicznego w .NET

### Lock

Instrukcja ``lock`` uzyskuje blokadę wzajemnego wykluczania dla danego obiektu, wykonuje blok instrukcji, a następnie zwalnia blokadę. Gdy blokada jest utrzymywana, wątek, który przechowuje blokadę, może ponownie uzyskać i zwolnić blokadę. Każdy inny wątek jest blokowany przed uzyskaniem blokady i czeka na zwolnienie blokady.

Instrukcja ``lock`` ma postać

```c#
lock(x)
{
	//code...
}
```

gdzie ``x`` jest wyrażeniem typu referencyjnego.

W poniższym przykładzie zdefiniowano klasę `Account`, która synchronizuje dostęp do jego prywatnego `balance` pola przez zablokowanie na dedykowanym wystąpieniu `balanceLock`. Użycie tego samego wystąpienia do blokowania gwarantuje, że nie można jednocześnie aktualizować pola `balance` przez dwa wątki próbujące wywołać metody `Debit` lub `Credit` jednocześnie.

```c#
using System;
using System.Threading.Tasks;

public class Account
{
    private readonly object balanceLock = new object();
    private decimal balance;

    public Account(decimal initialBalance)
    {
        balance = initialBalance;
    }

    public decimal Debit(decimal amount)
    {
        lock (balanceLock)
        {
            if (balance >= amount)
            {
                Console.WriteLine($"Balance before debit :{balance, 5}");
                Console.WriteLine($"Amount to remove     :{amount, 5}");
                balance = balance - amount;
                Console.WriteLine($"Balance after debit  :{balance, 5}");
                return amount;
            }
            else
            {
                return 0;
            }
        }
    }

    public void Credit(decimal amount)
    {
        lock (balanceLock)
        {
            Console.WriteLine($"Balance before credit:{balance, 5}");
            Console.WriteLine($"Amount to add        :{amount, 5}");
            balance = balance + amount;
            Console.WriteLine($"Balance after credit :{balance, 5}");
        }
    }
}

class AccountTest
{
    static void Main()
    {
        var account = new Account(1000);
        var tasks = new Task[100];
        for (int i = 0; i < tasks.Length; i++)
        {
            tasks[i] = Task.Run(() => RandomlyUpdate(account));
        }
        Task.WaitAll(tasks);
    }

    static void RandomlyUpdate(Account account)
    {
        var rnd = new Random();
        for (int i = 0; i < 10; i++)
        {
            var amount = rnd.Next(1, 100);
            bool doCredit = rnd.NextDouble() < 0.5;
            if (doCredit)
            {
                account.Credit(amount);
            }
            else
            {
                account.Debit(amount);
            }
        }
    }
}
```



### Semafory

Semafor to chroniona zmienna lub abstrakcyjny typ danych, który stanowi klasyczną metodę kontroli dostępu przez wiele procesów do wspólnego zasobu w środowisku programowania równoległego. Pozawala na dowolne ograniczenie równoległej liczby dostępów do wspólnego zasobu.

.NET oferuje nam klasę ``Semaphore`` implementującą semafor. Za pomocą konstruktora ``Semaphore(Int32, Int32)`` możemy stworzyć semafor i zdefiniować inicjalną oraz maksymalną liczbę równoległych instrukcji.

```c#
using System;
using System.Threading;
namespace Program
{
    class Demo
    {
        static Thread[] t = new Thread[5];
        static Semaphore semaphore = new Semaphore(2, 2);
        static void DoSomething()
        {
            Console.WriteLine("{0} = waiting", Thread.CurrentThread.Name);
            semaphore.WaitOne();
            Console.WriteLine("{0} begins!", Thread.CurrentThread.Name);
            Thread.Sleep(1000);
            Console.WriteLine("{0} releasing...", Thread.CurrentThread.Name);
            semaphore.Release();
        }
        static void Main(string[] args)
        {
            for (int j = 0; j < 5; j++)
            {
                t[j] = new Thread(DoSomething);
                t[j].Name = "thread number " + j;
                t[j].Start();
            }
            Console.Read();
         }
    }
}
```

Output:

```
thread number 2 = waiting
thread number 0 = waiting
thread number 3 = waiting
thread number 1 = waiting
thread number 4 = waiting
thread number 2 begins!
thread number 1 begins!
thread number 2 releasing...
thread number 1 releasing...
thread number 4 begins!
thread number 3 begins!
thread number 4 releasing...
thread number 0 begins!
thread number 3 releasing...
thread number 0 releasing...
```

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

Klasa Parallel umożliwia wykonywanie iteracji pętli for oraz foreach równolegle. Przykładowe użycie:

```c#
void SquareMatrices(IEnumerable<Matrix> matrices)
{
	Parallel.ForEach(matrices, matrix => matrix.Square());
}
```

## Zadania (10pkt)

### Zad1 (7pkt)
#### a) (5pkt)
Stwórz klasy ``Ksiazka``, ``Uzytkownik`` oraz odpowiednie metody i pola. Każda książka powinna mieć zdefiniowaną liczbę stron - ``int`` (może być losowo generowany z zakresu), identyfikator - ``int`` (uznajmy, iż 2 książki o tym samym identyfikatorze to ten sam tytuł, lecz inne instancje) . Użytkownicy mają listę książek, które chcieliby przeczytać (lista identyfikatorów). Użytkownicy odpytują (każdy w osobnym wątku) o książki  (aż przeczytają wszystko co chcą) z odpowiednim identyfikatorem (po kolei), a następnie wykonują na nich metodę ``PrzeczytajKsiazke(Ksiazka ksiazka)``, która wykorzystuje mechanizm ``lock`` (tylko 1 użytkownik naraz może czytać książkę). Przykładowa implementacja metody ``PrzeczytajKsiazke(Ksiazka ksiazka)``:

```c#
Console.WriteLine($"Uzytkownik {this.ID} chce przeczytac ksiazke {ksiazka.ID}");
lock (ksiazka)
{
	Console.WriteLine($"Uzytkownik {this.ID} rozpoczal czytanie ksiazki {ksiazka.ID}");
	Thread.Sleep(ksiazka.strony);
	Console.WriteLine($"Uzytkownik {this.ID} przeczytal ksiazke {ksiazka.ID}");
}
```

Niech w programie będzie przynajmniej 20 użytkowników, przynajmniej 200 książek i każdy z użytkowników niech ma na liście do przeczytania przynajmniej 40 książek.
#### b) (2pkt)
Zmodyfikuj program z podpunktu a) tak, aby zamiast mechanizmu ``lock`` wykorzystać mechanizm ``Semaphore`` i umożliwiać przeczytanie książki czterem użytkownikom naraz.

### Zad2 (3pkt)

Biblioteka ``System.Net.Http`` zawiera klasę ``HttpClient``. W niniejszym zadaniu wykorzystamy z tej klasy metodę ``GetStringAsync(string requestUri)``, która pozwala zczytać zawartość strony internetowej do zmiennej typu ``string``.

Proszę napisać aplikację konsolową z wykorzystaniem ``async`` i ``await``, która zapyta użytkownika o url strony  internetowej, a następnie asynchronicznie zczyta tą stronę do zmiennej i wyświetli użytkownikowi liczbę znaków znajdującą się na tej stronie. Podczas oczekiwania związanego z zczytywaniem strony proszę wyświetlić na standardowym wyjściu jakiś zapętlony komunikat związany z oczekiwaniem. W ogólności aplikacja ma symulować to, iż nie blokujemy interfejsu użytkownika podczas tego typu zapytań (dzieją się w tle). 
