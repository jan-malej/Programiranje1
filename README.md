# Izdelki v LEGO spletni trgovini
Iz LEGO spletne trgovine (https://www.lego.com/en-gb/categories/all-sets) bom pobral in analiziral okoli 1200 izdelkov, ki so tam navedeni. Pri vsakem izdelku bom zajel:
- številko izdelka (ID),
- ime,
- oceno (od 1 - 5),
- podatek, če je izdelek sploh na zalogi,
- ceno.

Moje hipoteze so:
- večina izdelkov je na zalogi,
- povprečna cena izdelka je 150€,
- povprečna ocena izdelkov je višja od 4,
- izdelki, ki jih ni na zalogi so povprečno dražji in bolje ocenjeni od ostalih.

V datoteki `lego_zajem.py` je program, s katerim sem zajel podatke. Uporabil sem tudi nekaj funkcij iz `orodja.py`.
V mapi Datoteke se nahajajo 3 datoteke:
- dve .txt, v katerih je vzorec "neparsane" kode iz spletnega naslova, ni pa to celotna koda, saj bi bilo le-te preveč,
- `podatki.csv`, kjer sem prej opisane zajete podatke zbral. V stolpcu 'zaloga' so logične vrednosti true/false, ki povejo ali je izdelek na zalogi. Cene izdelkov so navedene v centih.

V datoteki `analiza.ipynb` so pridobljeni podatki analizirani, zraven pa so podani tudi kratki opisi dobljenih rezultatov.
