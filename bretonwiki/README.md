# BretonWiki

A small Python package to fetch and format content from Breton Wikipedia.

```py
from bretonwiki import get_page

query = "Montroulez"  # Can be a word, sentence, or anything

print(get_page(query, is_only_summary=False))  # Get formatted str of the most relevant page
```

### Example output


[Title]
Montroulez

[Summary]
Montroulez zo ur gumun etre Leon ha Treger, e departamant Penn-ar-Bed, e Breizh.

[Section: Anv]
Ogée : Cette ville, qui se nommait Julia du temps de César, est une des plus anciennes et des plus célèbres de la province.
Cambry, Finistère, p. 5 : Ainsi Morlaix, si nous en croyons Conrad, archevêque de Salisbury, écrivain du douzième siècle, fut d'abord nommée Julia [...]. – Ainsi Drennalus, disciple de Joseph d'Arimathie, à son retour de l'île de Bretagne, passa par Morlaix, l'an 73 de J.C, en convertit les habitants ; ce lieu se nommait alors Saliocan ou Hanterallen.
Albert. Le Grand : Julia'.
Ch. Frochen, Finistère, Léon, p. 97 : Son nom vient probablement du celte Motreleg ("rue resserrée").
Bernard Tanguy, Communes du Finistère, p. 134 : Castrum Mons Relax, 1128 ; ecclesia S. Martini de Monte Relaxo, 1128 ; ecclesia Beati Melanii de Monte Relaxo, 1170 ; Mont Relays, XIIvet kantved ; (in) Montereleis, 1217 ; Montrelès, 1296 ; Montrelez, 1352 ; Morloys, 1371 ; Morlais, 1376 ; Morelaiz, 1385 ; Mourlaix, 1455 ; Montrelaes, Montrelaix, Mourlaix, 1464 ; Montrolaes, Morlaix, 1499 ; breton : Montroulez ; Ce mot ... (Relaix) ... n'est autre que le vieux-français "releis", "relais", « délaissé, abandonné ».
Éditions Flohic : noté Mons-Relaxus en 1128, du français "mont" et de l'ancien français "relais", « délaissé, abandonné ».
Daniel Delattre : Castrum Mons Relaxus au XIIè ; Montereleis au XIIè..
Gerdarzh
Relax = lec'h ehan war un hent roman (heñvelster insula = enez ; stabula = staol).

[Subsection: Dispac'h Gall]
Dre lezenn ar 26 a viz C'hwevrer 1790 e voe lakaet Montroulez da benn distrig Montroulez.
Dekred ar 26 a viz Du 1790 war al le ret : e penn-kentañ 1791 e voe nac'het al le ouzh ar Roue, ar vro hag al lezennoù gant Le Noannès, person parrez Sant-Melani, ha Pitot, person, ha Le Moine, kure, eus parrez Sant-Vazhev ; daou gure eus Sant-Melani, Le Ffevre ha Lucas, a reas al le.

[Subsection: XIXvet kantved]
Dezougen
1865: tizhet eo Montroulez gant an hent-houarn.
Brezel 1870-1871
Mervel a reas 144 gwaz ag ar gumun, eleze 1,02% ag he foblañs e 1866.

[Subsection: XXvet kantved]
Brezel-bed kentañ
Mervel a reas 604 gwaz ag ar gumun, da lavaret eo 3,96% ag he foblañs e 1911.
Eil brezel-bed
1943: d'an 29 a viz Genver e voe bombezet Montroulez gant ar Royal Air Force pa glaske distrujañ ar pont-meur hent-houarn ; lazhet e voe 39 bugel hag o skolaerez er skol Itron Varia Lourd, ha 27 den nann-soudard all. Kontet eo an darvoud e Gwerz Lazadeg Skolidigou Itron Varia Lourd.
Nijerezioù ar Gevridi aet d'ar strad e Montroulez : d'ar 4 a viz C'hwevrer 1941 e kouezhas ur Blenheim IV marilhet T2283 ha kodet PZ-F eus 55th Squadron ar Royal Air Force ; lazhet e voe he zri nijour, ne voe ket kavet o c'horfoù ; d'an 28 a viz Eost 1941 e kouezhas un Hurricane II marilhet BD857 eus 247th Squadron ar Royal Air Force nepell eus Montroulez ; tapet e voe he levier gant an Alamaned ; d'ar 25 a viz Ebrel 1942 e kouezhas pemp Spitfire Vb eus ar 501st Squadron eus ar Royal Air Force er mor e tu Montroulez ; pevar levier a varvas, met ne voe kavet korf ebet ; unan all a voe gloazet hepken ; d'ar 6 a viz Gwenholon 1944 e kouezhas un nijerez P-47 (486vet Bombing Group, 362vet FG, 378vet FS) eus aerlu SUA (United States Army Air Forces); he leviour a c'hellas adkavout e genvroidi.
Dieubet e voe Montroulez d'an 8 a viz Eost 1944 gant lu ar Stadoù-Unanet.
Brezel Indez-Sina
Lazhet e voe ul letanant-koronal eus an Aerlu gall d'an 21 a viz Here 1952 e Chua-Chan e Viêtnam.
Brezel Aljeria
Mervel a reas ur milour eus ar gumun d’an 2 a viz Meurzh 1957.
Stagidigezh
E 1959 e voe staget kumun Plouyann, en norzh da gêr, ouzh Montroulez.

[Subsection: Ar Brezoneg er Skol]
1934-1936 : ar c'huzul-kêr a savas a-du gant ar mennad skignet gant al luskad Ar Brezoneg er Skol (ABES) evit kelennadurezh ar brezhoneg er skolioù.

[Subsection: Ya d'ar brezhoneg]
D’ar 27 a viz Mezheven 2008 e voe votet ar garta Ya d'ar brezhoneg gant kuzul-kêr ar gumun.
Al label live 1 a oa bet roet da gumun Montroulez d'ar 6 a viz C'hwevrer 2009.

[Subsection: Deskadurezh]
Ur skol divyezhek zo eno abaoe 1988.
Ur skol Diwan zo e Montroulez ivez.
E distro-skol 2024 e oa enskrivet 57 bugel er skol Diwan, 77 er skol bublik ha 0 er skol gatolik, eleze 130 en holl.
