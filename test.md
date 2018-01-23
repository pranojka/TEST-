Teorijski deo
---

Dati sto konciznije odgvore u formi prosto prosirenih recenica na svako od sledecih pitanja.

01. Sta je to JSON? -java script object notation
02. Sta je to XML?-hiper text marcup langugae 
03. Sta je to URL?-uniform resource location
04. Sta je to HTTP?-hipper text markap protokor 
05. Sta je to RESTful API? Representational state transfer web servis koji pruza interoperability izmedju komjuterskog sistema i interneta
06. Koje HTTP metode imamo?-get, head, post,put,delete,connect , options,trace,patch
07. Sta je to DNS? domain name system
08. Sta je to private IP? privatna IP addresa je adresa koje koja se koristi za internu upotrebu 
09. Sta je to AJAX? Asynchronous JavaScript And XML i sluzi za kreiranje ascihronus web aplikaciju
10. Sta je to TCP/IP? transmition control protokol/internet protokol skup komunikacijskih protokola
11. Sta je to kes memorija? mala memorija koja sluzi sa zapis podataka koji se cesto koriste , u nju se za razliku od bafer memorije moze pitati na koje mesto se zeli upisati i sa kojeg mesta se zeli citati
12. Koja je razlika izmedju klase i objekta?Klasa definiše objekte, tj. njene atribute i metode koji se primenjuju na objektima (objektni metodi) ili samo na nivou klase (statički metodi).

Backend
---

1. U `models.py` fajlu implementirati `Comment` model (klasu) u Python-u koja sadrzi atribute:
- `text`: sam komentar, i
- `date`: datum komentara u formatu `YYYY-MM-DD`
"Override"-ovati `__repr__` metod.

2. U `models.py` fajlu definisati `COMMENTS` varijablu koja sadrzi niz od 3 elementa koji su tipa `Comment`. 

3. U `app.py` fajlu napraviti Flask applikaciju koja ima `index` "view" funkciju koja handle-uje `/` route. Funkcija bi trebalo da vraca HTML string koji u `body`-ju sadrzi heading "Welcome!".

4. U `app.py` dodati `comments` "view" funkciju koja handle-uje `/comments` route. Funkcija bi trebalo da vraca HTML koji u `body`-ju sadrzi tabelu komentara. Koristiti Flask template.

5.  U `app.py` dodati `api_comments` "view" funkciju koja handle-uje `/api/v1.0/comments` route. Funkcija bi trebalo da vraca JSON reprezentaciju `COMMENTS` niza.

Frontend
---

U `home.html` fajlu imlementirati jednostavnu klijent aplikaciju kojom moze da testira prethodno implementirani API end point. Koristiti `form` i `iframe`.

Algoritmi
---

Napisati i JavaScript i Python funkciju koja predstavlja resenje sledeceg zadataka:

Write a program that prints the numbers from 1 to 100. But for multiples of three print `Fizz` instead of the number and for the multiples of five print `Buzz`. For numbers which are multiples of both three and five print `FizzBuzz`.

Uputstvo
---

Resenja i odgovore predati u okviru GitHub repozitorijuma.
