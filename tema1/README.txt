Ciobanu Alin-Matei 335CB

- functia get_state(pattern, state, ch) returneaza starea urmatoare pentru
caracaterul ch curent.
- formez secventa de caractere citite pana in momentul curent, adaugand
caracterul curent : str = patt[0:state] + ch
- caut cel mai lung sufix in str care este prefix in pattern, folosind slice
- incep cu k = 1, astfel sar peste primul caracter din str si fac match
intre prefixul din pattern si sufixul din str


main:
- citesc din fisier pattern-ul si elimin newline-ul de la sfarsit
- citesc textul si elimin newline-ul de la sfarsit
- delta este un dictionar astfel: (stare_curenta, caracater) = urmatoarea stare
- for state in toate starile posibile (lungimea pattern-ului)
- for i in (65, 91) pentru a lua toate caracterele A-Z
- pentru  fiecare caracter din text, verific daca starea este finala si afisez
in fisire pozitia de la care incepe potrivirea pattern-ului