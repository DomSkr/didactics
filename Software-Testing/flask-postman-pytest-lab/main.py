import os
from flask import Flask, Response, request
import random
import string
import db as db
app = Flask(__name__)
db.init_app(app)


cant_hack_me = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))


@app.route("/")
def main():
    return "Witam w aplikacji będącej sprawdzianem umiejętności zdobytych na laboratoriach<br>" \
           "Do zdobycia jest 12 punktów. <br>" \
           "Lista zadan znajduje się pod adresem /zadania"

@app.route('/zadania')
def zadania():
    return Response("Proszę zapisać sobie zapytania, ponieważ trzeba będzie odtworzyć je przy prowadzącym.<br><br>"
                    "1 (2 punkty). Wykonaj zapytanie typu POST z parametrem body {'punkty' : 2} na endpoint /panda. <br><br>"
                    "2 (2 punkty). Wykonaj zapytanie GET do endpointu /websites tak, "
                    "aby wyświetlić jego zawartość (json z stronami internetowymi). Wymagany będzie token autoryzacyjny 'token':'nr_ind' reprezentujący państwa numer indeksu (*niekoniecznie prawdziwy - więcej informacji niżej).<br><br>"
                    "3 (3 punkty). Jak widać - w zadaniu pierwszym wymagana jest autoryzacja numerem indeksu. "
                    "Dla uproszczenia (i zgodności z RODO) nie są wymagane prawdziwe dane, lecz dowolny int 3 do 5 cyfrowy.<br>"
                    "Okazuje się jednak, iż w tym zakresie istnieją szczególne wartości, dla których jest inna (błędna) odpowiedź!   "
                    "Napisz test automatyczny, który przeiteruje po poprawnym zakresie i sprawdzi, czy odpowiedź jest taka, jak oczekiwana. Test powinien"
                    " zwrócić status fail dla tych szczególnych wartości.<br><br>"
                    "4 (2 punkty). Napisz test automatyczny sprawdzający poprawność odpowiedzi endpointu /random_pokemon.<br>"
                    "Endpoint ten powinien zwracać odpowiedź jako json z trzema polami<br>"
                    " * 'name' będący stringiem od 3 do 8 znaków<br>"
                    " * 'height' będący intem z zakresu 50-250<br>"
                    " * 'weight' będący liczbą zmiennoprzecinkową z zakresu 10.00 - 2500.00<br><br>"
                    "5 (1 punkt). Znajdź ukryty endpoint. Jest dość długi, ale może autor zadania omyłkowo trzyma kod źródłowy gdzieś w znanym studentom miejscu?<br><br>"
                    "6 (2 punkty). Znajdź ukryty endpoint. Jest dość krótki :). Ponadto po powyższym zadaniu mają pewnie państwo kod źródłowy - więc pewnie to łatwe do zrobienia.", 200)


@app.route('/websites')
def websites():
    # TODO: dać token akceptowalny dowolny int między 3, a 5 cyfr
    # TODO: zrobic kinda CRUDa?
    return Response("Access denied! Authorize with your numer indeksu as 'token':'nr_indeksu' header", 403)


@app.route('/random_pokemon')
def pokemons():
    # Niech zwraca json {'name': string od 3-8 znakow,
    return Response(500)


@app.route('/panda')
def panda():
    # TODO: obsługa jak w zad1
    return Response(500)


@app.route('/dodatkowy_punkt_zostanie_przyznany_jak_ktos_tu_wejdzie')
def add_point1():
    return Response("Gratuluję! Przyznano dodatkowy punkt", 200)


@app.route(f'/{cant_hack_me}')
def add_point2():
    return Response("Tutaj to dam i ze 2 punkty", 200)


if __name__ == "__main__":
    print(cant_hack_me)
    app.run(host="0.0.0.0", port=8080)
