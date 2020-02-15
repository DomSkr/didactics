## Message Broker
Message broker to wzorzec architektoniczny odpowiadaj�cy za przekazywanie wiadomo�ci mi�dzy klientami. Najpopularniejsze typy message broker'�w to
* Kolejka komunikat�w (ang. message queue)
* Publikuj�cy-subskrybuj�cy (ang. publish-subscribe)

**Kolejka komunikat�w**, zgodnie z nazw�, to kolejka (FIFO) sk�adaj�ca si� z komunikat�w. Przychodz�ce wiadomo�ci dodawane s� na koniec kolejki. Odbiorcy pobieraj� wiadomo�ci z kolejki. Jako przyk�ad mo�na poda� sytuacj�, w kt�rej mamy do wykonania list� zada� w pewnej kolejno�ci przez grup� os�b. Osoba, kt�ra aktualnie nie wykonuje zadania, pobiera pierwsze z listy i zaczyna je wykonywa�. 
**Publikuj�cy-subskrybuj�cy** to wzorzec, w kt�rym mamy do czynienia z producentami oraz konsumentami wiadomo�ci. Producenci dodaj� wiadomo�ci do list (np. r�ne kategorie wiadomo�ci), a konsumenci subskrybuj� odpowiednie listy (wyra�aj� ch�� otrzymywania wiadomo�ci z danej listy). Je�li mamy wielu subskrybent�w tej samej listy, to wszyscy z nich otrzymuj� t� wiadomo��. Przyk�ad - mechanizm subskrypcji w serwisie youtube. 
## Apache Kafka
Apache Kafka to otwarte oprogramowanie b�d�ce skalowalnym, rozproszonym, message brokerem o wysokiej wydajno�ci. Najcz�ciej u�ywane jest w formie publikuj�cy-subskrybuj�cy (ang. publish-subscribe).
#### Architektura Apache Kafka
Najcz�ciej architektura zwi�zana z Apache Kafk� posiada nast�puj�ce elementy:
 * Kafka Cluster - Kolekcja jednego lub wi�cej serwer�w s�u��cych jako message broker
 * ZooKeeper - Serwis odpowiadaj�cy za konfiguracj� klastra w rozproszonym �rodowisku
 * Producent - Komponent odpowiadaj�cy za produkowanie wiadomo�ci i przesy�anie ich do Kafki. Mo�e by� ich wielu.
 * Konsument - Komponent odpowiadaj�cy za konsumowanie/pobieranie wiadomo�ci. Mo�e by� ich wielu.

Podstawow� jednostk� danych w Kafce jest wiadomo�� (ang. message). Reprezentowana jest ona jako para klucz-warto��. Komunikacja mi�dzy producentami, konsumentami oraz kafk� odbywa si� za pomoc� protoko�u TCP. Klaster kafki mo�na skalowa� dodaj�c kolejne serwery. Wiadomo�ci s� replikowane zgodnie z konfiguracj� pomi�dzy poszczeg�lne serwery (w�z�y), co przyspiesza prac� z wieloma konsumentami. Wiadomo�ci grupowane s� w tematy (ang. topic). Ka�dy temat zwi�zany jest pewnego rodzaju kategori� wiadomo�ci.  
Wi�cej szczeg��w na temat Apache Kafka mo�na znale�� [tutaj](https://kafka.apache.org/documentation/).
Instalacja opcjonalnie mo�e by� przeprowadzona na maszynie wirtualnej dostarczonej do przedmiotu (patrz moodle).

#### Kafka client
Kafka posiada API, za pomoc� kt�rego konsumenci i producenci mog� si� komunikowa� z brokerem. W sporej cz�ci j�zyk�w napisane zosta�y biblioteki umo�liwiaj�ce konfiguracj� i zarz�dzanie producentami/konsumentami. Przyk�ad takiej implementacji na platform� .NET, to Kafka .NET Client.  Prosz� zapozna� si� z [procesem instalacji](https://github.com/confluentinc/confluent-kafka-dotnet#referencing) tej biblioteki oraz przyk�adowym kodem reprezentuj�cym dzia�anie [producenta](https://github.com/confluentinc/confluent-kafka-dotnet#basic-producer-examples) oraz [konsumenta](https://github.com/confluentinc/confluent-kafka-dotnet#basic-consumer-example).

## Zadanie (10pkt)
W grupach 2-3 osobowych prosz� wykona� nast�puj�ce zadania:
1. (2pkt) Instalacja oraz uruchomienie Kafka + Zookeeper - [Quickstart wg dokumentacji](https://kafka.apache.org/quickstart)/[Skonteneryzowane rozwi�zanie](https://github.com/simplesteph/kafka-stack-docker-compose/blob/master/zk-single-kafka-single.yml)
2. (3pkt) Napisanie aplikacji b�d�cej producentem wiadomo�ci. Wys�anie wiadomo�ci na server Kafka skonfigurowany w punkcie pierwszym.
3. (3pkt) Napisanie aplikacji b�d�cej konsumentem wiadomo�ci. Pobranie wiadomo�ci z servera Kafki z punktu pierwszego i wy�wietlenie go w konsoli.
4. (2pkt) Wykorzystuj�c serwer Kafki oraz aplikacje z punkt�w 2 i 3 prosz� uruchomi� 3 producent�w jednocze�nie (ka�dy pisz�cy wiadomo�ci na osobny temat (topic)). Prosz� uruchomi� 5 aplikacji konsument�w. Niech ka�dy z nich zczytuje wiadomo�ci z dw�ch temat�w oraz je wy�wietla w konsoli.
