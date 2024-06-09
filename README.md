Fotografska zajednica je web servis koja vam omogućuje da istražite raznoliki svijet fotografije i pronađete savršenog fotografa koji odgovara vašim zahtjevima. 
Bez obzira trebate li fotografiranje za posebni događaj, portrete, modne snimke, vjenčanja. Jedinstvena značajka je mogućnost ocjenjivanja fotografa od strane korisnika.


Osnobne funkcije su: 
-Dodavanje fotografa 
-čitanje(pregled) fotografa
-Uređivanje fotografa
-Brisanje fotografa 

Dodatne funkcionalnosi su: 
-Pretraživanje fotografa po imenu ili prezimenu
-Sortiranje po ocjeni(silazno i uzlazno)
-Sortiranje po cijeni(silazno i uzlazno)
-Graf ocjena svakog fotografa(stupčasti graf)
-Graf cijena svakog fotografa(stupčasti graf)
-Graf prema vrsti fotografije(kružni graf)




Za pokretanje aplikacije, potrebno je slijediti ove korake: Prvo, instalirali Docker na svom računalu, te preuzeti sve datoteke koje su dostupne na GitHub repozitoriju i sačuvati 
ih u odabranu mapu na svom računalu. Nakon toga otvoriti CMD na svom računalu. Navigirati do mape sa spremljenim datotekama uz naredbu cd kako bismo je premjestili u direktorij gdje 
smo sačuvali preuzete datoteke. Upotrijebiti sljedeću naredbu kako bismo stvorili Docker image:docker build --tag fotografi . Ova naredba stvara Docker image imenovanu 
fotografi iz trenutnog direktorija (.). Nakon što smo izgradili Docker image, treba pokrenuti kontejner koristeći sljedeću naredbu: 
docker container: docker run -p 5000:5000 fotografi Ova naredba pokreće Docker kontejner na portu 5000 i usmjerava ga na port 5000 unutar kontejnera. 
Kontejner je izgrađen na temelju image koju smo prethodno stvorili. Nakon što je kontejner pokrenut, pristupamo aplikaciji putem web preglednika. 
Otvorite preglednik i unijeti sljedeću adresu: http://localhost:5000 Sada možemo koristiti aplikaciju i pristupiti njezinim funkcionalnostima putem web preglednika.
