## Entity Framework

[Entity Framework](https://docs.microsoft.com/en-us/ef/) to framework mapowania obiektowo-relacyjnego (ang. Object-Relational Mapping) dla platformy .NET. Pozwala tworzyć strukturę bazy danych za pomocą kodu (i nie tylko).

## CRUD

CRUD (ang. create, read, update, delete) - cztery podstawowe funkcje w aplikacjach korzystających z pamięci trwałej. Zarówno ASP.NET Framework jak i ASP.NET Core umożliwiają skorzystanie z szablonu do implementacji CRUD.

## Zadanie (20pkt +5 dodatkowych)

Stwórz prostą aplikację z funkcjonalnością CRUD, wykorzystującą Entity Framework w jednej z dwóch technologii (podlinkowane tutoriale zawierają wszystkie potrzebne informacje do wykonania zadania, a nawet wiele nadmiarowych):

* ASP.NET Framework MVC 5 - [tutorial](https://docs.microsoft.com/en-us/aspnet/mvc/overview/getting-started/introduction/getting-started)
* ASP.NET Core MVC - [tutorial](https://docs.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-3.1&tabs=visual-studio)

Punktacja:

* Stworzenie szablonu - **2 pkt**
* Modyfikacja istniejącego widoku - stopki, treści - **2 pkt**
* Stworzenie nowego widoku z dowolną treścią tekstową, przekierowania z głównej strony na nową stronę - **2 pkt**
* Stworzenie modelu danych - dowolna sensowna klasa z przynajmniej pięcioma polami typu ``int``,  ``string``  - **2 pkt**
* Stworzenie lokalnej bazy danych za pomocą entity framework - połączenie jej ze stworzonym modelem (Connection String). - **7pkt**
* Stworzenie szablonu CRUD dla istniejącego modelu (Najłatwiej za pomocą mechanizmu Add Scaffold) - **5pkt**
* [**Dodatkowe**] Stworzenie drugiego modelu, szablonu CRUD dla nowego modelu oraz modyfikacja pierwszego modelu tak, aby zawierał referencję do obiektu z drugiego modelu (relacja - klucz obcy). Następnie w widoku tworzenia obiektu z pierwszego modelu należy doimplementować wybór drugiego modelu (do którego chcemy przechowywać referencję) za pomocą dropdown listy. - **5pkt**