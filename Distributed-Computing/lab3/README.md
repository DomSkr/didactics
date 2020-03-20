# Docker & Kubernetes

## Docker
Uruchamianie kolejnych maszyn wirtualnych na tej samej maszynie hoście staje się mało wydajne. Im więcej zasobów mamy do
podziału i im więcej maszyn utworzymy tym więcej zasobów zmarnujemy. Każda maszyna wirtualna to nowy system operacyjny i
konieczność uruchomienia kolejnego jądra systemu.
Pojawia się pomysł, aby uruchomione było zawsze tylko jedno jądro systemu a kolejne maszyny wirtualne używały właśnie jego.
Tak rodzi się idea konteneryzacji a jedną z pierwszych jej implementacji jest Docker.

## Kubernetes
Sam Docker dotyczy pojedynczej maszyny (komputera/serwera). Gdy chcemy uruchamiać wiele kontenerów na wielu maszynach
potrzebujemy systemu do szeregowania zadań. Jednym z nich jest stworzony przez firmę Google, Kubernetes. Jest to ogromne narzędzie o dużych możliwościach.
Implementując kubernetesa postawiono sobie za cel rozwiązanie wielu problemów, które po drodze napotykają osoby wdrażające swoje aplikacje - 
sieć między kontenerami, wystawienie usługi na zewnątrz klastra, aktualizowanie bez przerw w działaniu usługi itp.

Wątek teoretyczny odnośnie Dockera i Kubernetesa opisano szerzej [tutaj](https://magnifier.pl/konteneryzacja-docker-kubernetes/).

Wszystkie zadania (zarówno przygotowanie jak i właściwą laborkę) należy wykonywać na maszynie wirtualnej do przedmiotu (osobna instrukcja dostępna w materiałach).

## Zadania wstępne do wykonania

### Uruchomienie kontenera w oparciu obraz dostępny w internecie

Analogicznie do serwisu github.com powstał serwis dockerhub.com. Jest to oficjalny 'rejestr' obrazów utrzymywany przez firmę Docker.
Próba pobrania bądź uruchomienia obrazu, który nie znajduje się na dysku spowoduje pobranie obrazu właśnie z tego oficjalnego serwisu.
W ramach tego przykładu użyty będzie obraz [busybox](https://hub.docker.com/_/busybox).

#### Uruchomienie interaktywne
Wykonanie polecenia ```docker run -it busybox``` sprawi, że zostanie uruchomiony kontener `busybox` a my od razu przejmiemy sesję jego terminala.
Możemy wykonywać dowolne polecenia wewnątrz kontenera, np. `ip a`. Zauważysz wtedy, że każdy kontener otrzymuje swój własny adres IP.
Warto również zwrócić uwagę, że wewnątrz kontenera brakuje całkiem sporo popularnych programów, jak np `curl`. Jest to zgodne z jednym z podstawowych założeń
tworzenia obrazów - trzymamy je możliwie najlżejsze a potrzebne aplikacje instalujemy na etapie budowania.

Wykonajmy polecenie `ps aux`. W jego wyniku zauważymy, że wewnątrz kontenera działa tylko jeden proces - `sh`. Jest to nasza sesja terminala, zaś sam proces ma identyfikator 1.
Gdy proces o tym identyfikatorze zostanie wyłączony (przestanie działać), to cały kontener kończy pracę.

Jako że kontener uruchomiony jest interaktywnie to zamknięcie sesji poleceniem `exit` spowoduje zatrzymanie kontenera.

Po zatrzymaniu kontenera, dalej jest on dostępny do ponownego uruchomienia.
Aktualnie uruchomione kontenery można wylistować komendą `docker ps`.
Nasz kontener nie jest już uruchomiony, więc nie pojawił się na tej liście. Aby go zobaczyć, należy wykonać polecenie `docker ps -a`.

Na liście znajdzie się nasz kontener ze statusem `Exited`. O ile nie nadamy nazwy kontenerowi to zostanie ona przydzielona losowo.
Do poleceń wymagających nazw kontenerów można używać wartości z kolumny `CONTAINER ID` lub wylosowanej nazwy. 

Aby ostatecznie wyrzucić kontener z systemu, dla kontenerów już zatrzymanych można wykonać polecenie:
```docker rm [CONTAINER ID]```.

#### Uruchomienie innego procesu przy starcie kontenera
```docker run -it busybox [CMD]```

Naszym poleceniem będzie `sleep` na `10` sekund.

```docker run -it busybox sleep 10```

Po uruchomieniu kontenera na 10 sekund tracimy dostęp do wiersza poleceń (sleep nie jest interaktywny).
Gdy po 10 sekundach proces się kończy to kontener znowu jest w stanie `EXITED`. Proszę to zweryfikować i usunąć kontener (jak w poprzednim punkcie).

#### Uruchomienie kontenera w tle i wykonywanie na nim innych poleceń
Zamiast uruchamiania interaktywnego (przejmującego terminal), można uruchomić kontener w tle (jako daemon).

```docker run -d busybox sleep inf```
Powoduje to uruchomienie kontenera, w którym procesem `1` będzie sleep inf. Kontener zostanie uruchomiony w tle.
Tak uruchomiony kontener pojawi się na liście `docker ps`.
Na takim kontenerze, można wykonywać inne polecenia za pomocą komendy `docker exec`. Przykładowo:
```docker exec [CONTAINER ID] ls /``` wylistuje zawartość z głównego katalogu:
```
bin
dev
etc
home
proc
root
sys
tmp
usr
var
```
Możemy również wylistować w ten sposób procesy:
```docker exec [CONTAINER ID] ps aux```
```
PID   USER     TIME  COMMAND
    1 root      0:00 sleep inf
   36 root      0:00 ps aux
```
W szczególności możemy też wykonywać polecenia interaktywne:
```
docker exec -it [CONTAINER ID] sh 
```
Spowoduje to 'wejście' do wnętrza kontenera, a co za tym idzie, możliwość wykonywania w nim poleceń. Tym razem po wykonaniu `exit`, kontener nie zostanie zatrzymany. Ponieważ proces `sh` nie ma ID `1`.

Aby zatrzymać taki kontener należy wpisać polecenie `docker stop [CONTAINER ID]`.
Następnie można go usunąć `docker rm [CONTAINER ID]`.

Jest też możliwe usunięcie działającego kontenera poleceniem: `docker rm -f [CONTAINER ID]`

### Praca z obrazami
Po wpisaniu polecenia `docker images` zobaczymy listę obrazów dostęnych na naszej maszynie.
Proces pobierania obrazów z internetu nazywamy `pullowaniem` - `docker pull [IMAGE]`, a wysyłaniem do zewnętrznych rejestrów `pushowaniem` - `docker push [IMAGE]`.
Dodatkowo `docker run` również pobiera obrazy, jeśli nie są dostępne na maszynie. Stąd obecność obrazu `busybox` na liście.
Obrazy można usuwać z dysku za pomocą polecenia `docker rmi [image]`

Obrazy mogą mieć swoje wersje - `tag`. Brak tagu oznacza używanie tagu domyślnego - `latest`.

#### Pobranie i uruchomienie obrazu httpd
Będziemy chcieli pobrać i uruchomić obraz [httpd](https://hub.docker.com/_/httpd?tab=tags) z nieco starszym tagiem niż aktualny.
```docker pull httpd:2.4```

Zweryfikuj obecność obrazu na liście obrazów.

Httpd to serwer HTTP(S) stron internetowych. Uruchomimy teraz pobrany obraz i zobaczymy jaką stronę hostuje. 
```docker run -p 80:80 --name www -d httpd:2.4```
Uruchomiony tak kontener wystawi port 80 (domyślny port protokołu HTTP) na zewnątrz. Dodatkowo kontener otrzyma nazwę `www`.

Za pomocą aplikacji `curl` odpytujemy o stronę internetową:
```curl localhosl```

Powinien pojawić się kod HTML `<html><body><h1>It works!</h1></body></html>`. Jest to domyślna 'strona', którą hostuje httpd.

Strona otworzy się również w przeglądarce internetowej z naszego komputera (poprzez adresację 'Host Only VirtualBoxa). Należy otworzyć przeglądarkę i wejść pod adres maszyny wirtualnej np. `192.168.56.X`.

#### Budowanie własnych obrazów
Budowanie własnych obrazów opiera się na plikach `Dockerfile` i zbiorze kilku słów kluczowych, które mogą być w nich użyte.
Najważniejszym jest `RUN`, który pozwala wykonywać polecenia podobnie jak dla wiersza poleceń.
Każdy obraz musi mieć jakąś podstawę - albo inny już istniejący obraz, albo tak zwany `scratch` (budowa obrazu od zera). Do zdefiniowania punktu początkowego używamy słowa kluczowego `FROM`.
Często chcemy ustawić komendę (lub punkt wejścia), którą uruchamiany kontener ma wykonywać. Można do tego użyć słowa kluczowego `ENTRYPOINT` lub `CMD`.

Przykładowy dockerfile:
```
FROM ubuntu:18.04
RUN apt update
RUN apt -y install nginx
CMD ["echo", "Image created"]
````

Należy skopiować ten plik do dowolnej lokalizacji (najlepiej nowy pusty katalog) a plik nazwać `Dockerfile`. Następnie należy wejść do utworzonego katalogu i wykonać polecenie `docker build`.
Chcemy zbudować obraz z bieżącej lokalizacji i jednocześnie nadać mu nazwę oraz tag 1.0. Dokonujmy tego za pomocą polecenia:
```docker build . -t my-nginx:1.0```

Dla treningu uruchom zbudowany obraz na różne sposoby.

Literatura do przeczytania związana z budowaniem:
- [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#dockerfile-reference)
- [Dobre praktyki przy budowaniu obrazów](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

Pytanie kontrolne: Jaką dobrą praktykę łamie powyższy przykład?
- [Lista słów kluczowych w dockerfile](https://kapeli.com/cheat_sheets/Dockerfile.docset/Contents/Resources/Documents/index)

#### Publikowanie obrazów w rejestrze docker hub
W tym podrozdziale opublikujemy obraz zbudowany przed chwilą w serwisie dockerhub.
Na początek należy założyć sobie konto: https://hub.docker.com/signup
Następnie, po zalogowaniu tworzymy sobie nowe repozytorium: https://hub.docker.com/repository/create
Tak jak nazwane zostanie repozytorium, tak samo powinien nazywać się obraz do opublikowania. W naszym przypadku podamy nazwę `my-nginx`.

Gdy repozytorium jest już utworzone, możemy przejść ponownie do naszej konsoli.
Na początek z poziomu dockera musimy się zalogować do rejestru dockerhub. Wykonajmy polecenie
```docker login``` 
Po podaniu swoich poprawnych danych nastąpi zalogowanie.

Docker wymaga odpowiedniego nazewnictwa obrazów, aby można było je poprawnie opublikować.
W przypadku dockerhuba obraz musi mieć postać `DOCKERHUB_USER/NAZWA_OBRAZU:TAG`.

Nadajmy teraz naszemu obrazowi odpowiednią nazwę. Użyjemy do tego, polecenia `docker tag`.
```docker tag my-nginx:1.0 mzylowski/my-nginx:1.0```

Następnie wykonajmy polecenie, które opublikuje nasz obraz w serwisie:
```docker push mzylowski/my-nginx:1.0```

Efektem wykonania polecenia będzie podobny output:
```
The push refers to repository [docker.io/mzylowski/my-nginx]
8cd3b2bd8324: Pushed
74652bd59c5a: Pushed
f55aa0bd26b8: Mounted from library/ubuntu
1d0dfb259f6a: Mounted from library/ubuntu
21ec61b65b20: Mounted from library/ubuntu
43c67172d1d1: Mounted from library/ubuntu
1.0: digest: sha256:0b7f62334e07ad92017266a88015fbe65a1096f531fe77e8fb670dab8f321a16 size: 1576
```

Na stronie dockerhub w repozytorium pojawi się wrzucony właśnie tag.

Teraz na dowolnym komputerze (o ile repozytorium) jest publiczne, można wykonać polecenie:
docker pull mzylowski/my-nginx:1.0

### Kubernetes
Na przygotowanej maszynie wirtualnej należy uruchomić polecenie ```CHANGE_MINIKUBE_NONE_USER=true minikube start --vm-driver=none```.
Spowoduje to uruchomienie małego jednowęzłowego klastra (UWAGA: minikuba nie powinno się używać produkcyjnie).

Po wykonaniu tego polecenia program kubectl będzie skonfigurowany do używania klastra minikube. Można wykonać np polecenie:
```kubectl get nodes```
W odpowiedzi zobaczymy jeden `node` - uruchomionego minikube'a. Węzeł powinien być w stanie `Running`.

Dodatkowo możemy wykonać np polecenie ```kubectl cluster-info```, zwróci nam ono kilka informacji. Jeśli polecenia skończą się
jakimiś błędami to pojawił się jakiś problem z uruchomieniem klastra i wykonywanie dalszych poleceń nie ma sensu, aż do uporania się z nimi.

W dalszej części instrukcji zajmiemy się dwoma tematami z Kubernetesa - POD'ami oraz Job'ami. Jest to tylko mały wycinek możliwości, które oferuje ta platforma.

#### POD
POD w kubernetesie jest podstawowym bytem, PODy mogą być uruchamiane samodzielnie, lub kontrolowane przez inne byty kubernetesa, takie jak `deamonset`, `deployment`, `job`, `replica set` i inne.
POD należy rozumieć jako 'pojemnik na kontenery'. W każdym PODzie może być uruchomione wiele kontenerów. POD otrzymuje jeden adres IP i jest on współdzielony przez wszystkie kontenery. Konsekwencją tego podejścia jest to, że dwa kontenery w tym samym podzie nie mogą wystawić takiego samego portu.

Obiektami w Kubernetesie zarządzamy za pomocą plików yaml.
Skopiuj poniższy kod i zapisz go do pliku nginx.yaml:
```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
    ports:
    - containerPort: 80
```

Następnie wykonaj polecenie:
```kubectl apply -f nginx.yaml```

Poleceniem:
```kubectl get pod```
Można pobierać listę PODów.
Zaraz po wykonaniu polecenia appply, uruchom kilkukrotnie to polecenie. Być może zauważysz zmianę stanu POD'a.

Dokładnie informacje na temat POD'a można uzyskać poleceniem:
```kubectl describe pod nginx```

Wykonując polecenie `docker ps` zauważysz, że uruchomienie tego POD'a przez kubernetesa to de facto uruchomienie kontenera.
Na liście działających kontenerów zauważysz pozycję w stylu:
```k8s_nginx_nginx_default_JAKIS_ID```
Usuń ten kontener, a następnie sprawdź listę PODów za pomocą `kubectl get po`.
Wystarczająco szybkie sprawdzenie listy podów, ponownie pozwoli zauważyć stan `ContainerCreating` a następnie `Running`.
Wniosek jest z tego taki, że POD będzie bronił swoje kontenery przed zatrzymaniem w ten sposób.
Przy uzyskaniu stanu `Running` na liście `docker ps` ponownie pojawi się kontener.

Prawidłowym sposobem na usunięcie POD'a jest ```kubectl delete po nginx```

#### Uruchomienie JOB'a
Obiekt `JOB` reprezentuje jednorazową pracę do wykonania. Praca raz wykonana z sukcesem spowoduje zakończenie pracy PODów.

Tym razem dla polecenia `kubectl apply` podaj taki plik yaml:
```
apiVersion: batch/v1
kind: Job
metadata:
  name: pi
spec:
  template:
    spec:
      containers:
      - name: pi
        image: perl
        command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: Never
  backoffLimit: 4
```

Analizując ten plik kubernetes najpierw powoła do życia obiekt `job`.
Można to zauważyć wykonując polecenie ```kubectl get jobs```.
Obiekt `Job` powoła do życia odpowiednie PODy wypisane w definicji. W naszym przypadku będzie to POD z jednym kontenerem opartym na obrazie `perl`.
Listując pody tak jak w poprzednim zadaniu zobaczymy ten powołany do życia przez JOB'a.
Jego nazwa to będzie nazwa job'a (pi) oraz identyfikator nadany przez kubernetesa.

Obserwuj status Joba i Poda do czasu, gdy Pod osiągnie stan `Completed`. Gdy to nastąpi możesz wyciągnąć wynik zadania obliczeniowego wykonanego w perlu:
```kubectl logs pi-r7hcg```
Oczywiście `r7hcg` należy zastąpić swoim ID.

W odpowiedzi otrzymamy liczbę PI z dokładnością do 2000 miejsc po przecinku.

Aby usunąć JOB'a należy wykonać polecenie:
```kubectl delete job pi```
Oczywiście razem z Jobem zostanie usunięty Pod związany z zadaniem.

#### Zadania domowe do samodzielnego wykonania
1. Bazując na obrazie nginx należy utworzyć nowy obraz, w którym tekst `It works`. Zostanie zastąpiony naszym numerem indeksu.
Najlepiej utworzyć odpowiedni plik index.html w tej samej lokalizacji co plik Dockerfile i w procesie budowania skopiować go do lokalizacji `/usr/share/nginx/html`. Słowo kluczowe `COPY` w pliku Dockerfile, będzie tutaj przydatne.
2. Uruchomić kontener i w przeglądarce internetowej zobaczyć zmodyfikowaną stronę. Przynieś zrzut na zajęcia dbając jednocześnie by było widać, że jesteś jego autorem (na przykład w tle widać, że jesteś zalogowany na swoje konto studenckie).
3. Odpowiednio otagować obraz, stworzyć dla niego repozytorium i opublikować go z tagiem 1.0 na dockerhubie.


## Zadania laboratoryjne (10pkt)

### Zad1 (1pkt) - Screen
Zaprezentuj prowadzącemu screen z uruchomienia zadania wstępnego do laboratorium (numer indeksu) (Zadanie domowe numer 2).

### Zad2 (4 pkt)
Bazując na pliku Dockerfile z zadania domowego, przygotuj jego kolejną wersję:
- Usuń całkiem plik index.html z lokalizacji `/usr/share/nginx/html`
- Do lokalizacji `/usr/share/nginx/html` wrzucić 3 dowolnie wybrane memy z internetu. Mogą być one skopiowane w procesie budowania lub pobrane np aplikacją wget.
- Otagować obraz wersją 2.0 i opublikować na dockerhubie w stworzonym w ramach 3 zadania domowego repozytorium.

### Zad3 (5 pkt) - Uruchomienie Joba na Kubernetesie 
Na potrzeby przedmiot został przygotowany obraz `mzylowski/life-calculator:0.1` - https://hub.docker.com/r/mzylowski/life-calculator
Wewnątrz znajduje się prosta aplikacja napisana w go-langu licząca sens życia i wszechświata. Aplikacja nazywa się `universer`.
Należy na kubernetesie uruchomić joba, który wyliczy sens dla naszego numeru indexu. Numer indexu należy przekazać jako parametr do polecenie `universer`.

Aby oddać zadanie należy pokazać POD w stanie 'Completed' oraz log z tego POD'a. Musi się tam znajdować poprawna odpowiedź wyliczona w oparciu o Twój numer indeksu.
