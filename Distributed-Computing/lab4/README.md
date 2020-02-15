## Message Broker
Message broker to wzorzec architektoniczny odpowiadaj¹cy za przekazywanie wiadomoœci miêdzy klientami. Najpopularniejsze typy message broker'ów to
* Kolejka komunikatów (ang. message queue)
* Publikuj¹cy-subskrybuj¹cy (ang. publish-subscribe)

**Kolejka komunikatów**, zgodnie z nazw¹, to kolejka (FIFO) sk³adaj¹ca siê z komunikatów. Przychodz¹ce wiadomoœci dodawane s¹ na koniec kolejki. Odbiorcy pobieraj¹ wiadomoœci z kolejki. Jako przyk³ad mo¿na podaæ sytuacjê, w której mamy do wykonania listê zadañ w pewnej kolejnoœci przez grupê osób. Osoba, która aktualnie nie wykonuje zadania, pobiera pierwsze z listy i zaczyna je wykonywaæ. 
**Publikuj¹cy-subskrybuj¹cy** to wzorzec, w którym mamy do czynienia z producentami oraz konsumentami wiadomoœci. Producenci dodaj¹ wiadomoœci do list (np. ró¿ne kategorie wiadomoœci), a konsumenci subskrybuj¹ odpowiednie listy (wyra¿aj¹ chêæ otrzymywania wiadomoœci z danej listy). Jeœli mamy wielu subskrybentów tej samej listy, to wszyscy z nich otrzymuj¹ t¹ wiadomoœæ. Przyk³ad - mechanizm subskrypcji w serwisie youtube. 
## Apache Kafka
Apache Kafka to otwarte oprogramowanie bêd¹ce skalowalnym, rozproszonym, message brokerem o wysokiej wydajnoœci. Najczêœciej u¿ywane jest w formie publikuj¹cy-subskrybuj¹cy (ang. publish-subscribe).
#### Architektura Apache Kafka
Najczêœciej architektura zwi¹zana z Apache Kafk¹ posiada nastêpuj¹ce elementy:
 * Kafka Cluster - Kolekcja jednego lub wiêcej serwerów s³u¿¹cych jako message broker
 * ZooKeeper - Serwis odpowiadaj¹cy za konfiguracjê klastra w rozproszonym œrodowisku
 * Producent - Komponent odpowiadaj¹cy za produkowanie wiadomoœci i przesy³anie ich do Kafki. Mo¿e byæ ich wielu.
 * Konsument - Komponent odpowiadaj¹cy za konsumowanie/pobieranie wiadomoœci. Mo¿e byæ ich wielu.

Podstawow¹ jednostk¹ danych w Kafce jest wiadomoœæ (ang. message). Reprezentowana jest ona jako para klucz-wartoœæ. Komunikacja miêdzy producentami, konsumentami oraz kafk¹ odbywa siê za pomoc¹ protoko³u TCP. Klaster kafki mo¿na skalowaæ dodaj¹c kolejne serwery. Wiadomoœci s¹ replikowane zgodnie z konfiguracj¹ pomiêdzy poszczególne serwery (wêz³y), co przyspiesza pracê z wieloma konsumentami. Wiadomoœci grupowane s¹ w tematy (ang. topic). Ka¿dy temat zwi¹zany jest pewnego rodzaju kategori¹ wiadomoœci.  
Wiêcej szczegó³ów na temat Apache Kafka mo¿na znaleŸæ [tutaj](https://kafka.apache.org/documentation/).
Instalacja opcjonalnie mo¿e byæ przeprowadzona na maszynie wirtualnej dostarczonej do przedmiotu (patrz moodle).

#### Kafka client
Kafka posiada API, za pomoc¹ którego konsumenci i producenci mog¹ siê komunikowaæ z brokerem. W sporej czêœci jêzyków napisane zosta³y biblioteki umo¿liwiaj¹ce konfiguracjê i zarz¹dzanie producentami/konsumentami. Przyk³ad takiej implementacji na platformê .NET, to Kafka .NET Client.  Proszê zapoznaæ siê z [procesem instalacji](https://github.com/confluentinc/confluent-kafka-dotnet#referencing) tej biblioteki oraz przyk³adowym kodem reprezentuj¹cym dzia³anie [producenta](https://github.com/confluentinc/confluent-kafka-dotnet#basic-producer-examples) oraz [konsumenta](https://github.com/confluentinc/confluent-kafka-dotnet#basic-consumer-example).

## Zadanie (10pkt)
W grupach 2-3 osobowych proszê wykonaæ nastêpuj¹ce zadania:
1. (2pkt) Instalacja oraz uruchomienie Kafka + Zookeeper - [Quickstart wg dokumentacji](https://kafka.apache.org/quickstart)/[Skonteneryzowane rozwi¹zanie](https://github.com/simplesteph/kafka-stack-docker-compose/blob/master/zk-single-kafka-single.yml)
2. (3pkt) Napisanie aplikacji bêd¹cej producentem wiadomoœci. Wys³anie wiadomoœci na server Kafka skonfigurowany w punkcie pierwszym.
3. (3pkt) Napisanie aplikacji bêd¹cej konsumentem wiadomoœci. Pobranie wiadomoœci z servera Kafki z punktu pierwszego i wyœwietlenie go w konsoli.
4. (2pkt) Wykorzystuj¹c serwer Kafki oraz aplikacje z punktów 2 i 3 proszê uruchomiæ 3 producentów jednoczeœnie (ka¿dy pisz¹cy wiadomoœci na osobny temat (topic)). Proszê uruchomiæ 5 aplikacji konsumentów. Niech ka¿dy z nich zczytuje wiadomoœci z dwóch tematów oraz je wyœwietla w konsoli.
