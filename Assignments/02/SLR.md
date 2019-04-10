# Universidade Federal de Maceió
## Instituto de Computação
## Aluno: Antonio Manoel

Gramática
----------
```
(0) S = Ea
(1) Ea = Ea 'opa' Ta
(2) Ea = Ta
(3) Ta = Ta 'opm' Pa
(4) Ta = Pa
(5) Pa = Fa '**' Pa
(6) Pa = Fa
(7) Fa = '(' Ea ')'
(8) Fa = 'id'
(9) Fa = 'ctn'
```
Cálculo dos conjuntos LR
-----------
```
0 = c({S = .Ea}) = {S = .Ea, Ea = .Ea 'opa' Ta, Ea =.Ta,
                     Ta = .Ta 'opm' Pa, Ta = .Pa, Pa = .Fa '**' Pa,
                     Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
1 = (0,  Ea) = {S = Ea., Ea = Ea. 'opa' Ta}
2 = (0,  Ta) = {Ea = Ta., Ta = Ta. 'opm' Pa}
3 = (0,  Pa) = {Ta = Pa.}
4 = (0,  Fa) = {Pa = Fa. '**' Pa, Pa = Fa.}
5 = (0, '(') = {Fa = '('. Ea ')', Ea = .Ea 'opa' Ta, Ea =.Ta,
                            Ta = .Ta 'opm' Pa, Ta = .Pa, Pa = .Fa '**' Pa,
                            Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
6 = (0, 'id') = {Fa = 'id'.}
7 = (0,'ctn') = {Fa = 'ctn'.}
8 = (1, 'opa') = {Ea = Ea 'opa'. Ta, Ta = .Ta 'opm' Pa,
                            Ta = .Pa, Pa = .Fa '**' Pa, Pa = .Fa,
                            Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
9 = (2, 'opm') = {Ta = Ta 'opm'. Pa, Pa = .Fa '**' Pa,
                            Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
10 = (4, '**') = {Pa = Fa '**'. Pa, Pa = .Fa, Fa = .'(' Ea ')',
                            Fa = .'id', Fa =.'ctn'}
11 = (5,  Ea) = {Ea = '(' Ea. ')', Ea = Ea. 'opa' Ta}
     (5,  Ta) = {Ea = Ta., Ta = Ta. 'opm' Pa}
     (5,  Pa) = {Ta = Pa.}
     (5,  Fa) = {Pa = Fa. '**' Pa, Pa = Fa.}
     (5,  '(') = {Fa = '('. Ea ')', Ea = .Ea 'opa' Ta, Ea =.Ta,
                            Ta = .Ta 'opm' Pa, Ta = .Pa, Pa = .Fa '**' Pa,
                            Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
     (5,  'id') = {Fa = 'id'.}
     (5,  'ctn') = {Fa = 'ctn'.}
12 = (8,  Ta) = {Ea = Ea 'opa' Ta.,  Ta = Ta. 'opm' Pa}
     (8,  Pa) = {Ta = Pa.}
     (8,  Fa) = {Pa = Fa. '**' Pa, Pa = Fa.}
     (8,  '(') = {Fa = '('. Ea ')', Ea = .Ea 'opa' Ta, Ea =.Ta,
                            Ta = .Ta 'opm' Pa, Ta = .Pa, Pa = .Fa '**' Pa,
                            Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
     (8,  'id') = {Fa = 'id'.}
     (8,  'ctn') = {Fa = 'ctn'.}
13 = (9,  Pa) = {Ta = Ta 'opm' Pa.}
     (9,  Fa) = {Pa = Fa. '**' Pa, Pa = Fa.}
     (9,  '(') = {Fa = '('. Ea ')', Ea = .Ea 'opa' Ta, Ea =.Ta,
                            Ta = .Ta 'opm' Pa, Ta = .Pa, Pa = .Fa '**' Pa,
                            Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
     (9,  'id') = {Fa = 'id'.}
     (9,  'ctn') = {Fa = 'ctn'.}
14 = (10, Pa) = {Pa = Fa '**' Pa.}
     (10, Fa) = {Pa = Fa. '**' Pa, Pa = Fa.}
     (10, '(') = {Fa = '('. Ea ')', Ea = .Ea 'opa' Ta, Ea =.Ta,
                            Ta = .Ta 'opm' Pa, Ta = .Pa, Pa = .Fa '**' Pa,
                            Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
     (10, 'id') = {Fa = 'id'.}
     (10, 'ctn') = {Fa = 'ctn'.}
15 = (11, ')') = {Ea = '(' Ea ')'.}
     (11, 'opa') = {Ea = Ea 'opa'. Ta,  Ta = .Ta 'opm' Pa,
                       Ta = .Pa, Pa = .Fa '**' Pa, Pa = .Fa, Fa = .'(' Ea ')',
                       Fa = .'id', Fa =.'ctn'}
     (12, 'opm') = {Ta = Ta 'opm'. Pa, Pa = .Fa '**' Pa,
                       Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
```
Conjuntos LR(0)
------------
```
0 = c({S = .Ea}) = {S = .Ea, Ea = .Ea 'opa' Ta, Ea =.Ta,
                     Ta = .Ta 'opm' Pa, Ta = .Pa, Pa = .Fa '**' Pa,
                     Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
T1 = (0,  Ea) = {S = Ea., Ea = Ea. 'opa' Ta}
T2 = (0,  Ta) = {Ea = Ta., Ta = Ta. 'opm' Pa}
T3 = (0,  Pa) = {Ta = Pa.}
T4 = (0,  Fa) = {Pa = Fa. '**' Pa, Pa = Fa.}
E5 = (0, '(') = {Fa = '('. Ea ')', Ea = .Ea 'opa' Ta, Ea =.Ta,
                            Ta = .Ta 'opm' Pa, Ta = .Pa, Pa = .Fa '**' Pa,
                            Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
E6 = (0, 'id') = {Fa = 'id'.}
E7 = (0,'ctn') = {Fa = 'ctn'.}
E8 = (1, 'opa') = {Ea = Ea 'opa'. Ta, Ta = .Ta 'opm' Pa,
                            Ta = .Pa, Pa = .Fa '**' Pa, Pa = .Fa,
                            Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
E9 = (2, 'opm') = {Ta = Ta 'opm'. Pa, Pa = .Fa '**' Pa,
                            Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
T10 = (4, '**') = {Pa = Fa '**'. Pa, Pa = .Fa, Fa = .'(' Ea ')',
                            Fa = .'id', Fa =.'ctn'}
T11 = (5,  Ea) = {Ea = '(' Ea. ')', Ea = Ea. 'opa' Ta}
T2 =  (5,  Ta) = {Ea = Ta., Ta = Ta. 'opm' Pa}
T3 =  (5,  Pa) = {Ta = Pa.}
T4 =  (5,  Fa) = {Pa = Fa. '**' Pa, Pa = Fa.}
E5 =  (5,  '(') = {Fa = '('. Ea ')', Ea = .Ea 'opa' Ta, Ea =.Ta,
                            Ta = .Ta 'opm' Pa, Ta = .Pa, Pa = .Fa '**' Pa,
                            Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
E6 =  (5,  'id') = {Fa = 'id'.}
E7 =  (5,  'ctn') = {Fa = 'ctn'.}
T12 = (8,  Ta) = {Ea = Ea 'opa' Ta.,  Ta = Ta. 'opm' Pa}
T3 =  (8,  Pa) = {Ta = Pa.}
T4 =  (8,  Fa) = {Pa = Fa. '**' Pa, Pa = Fa.}
E5 =  (8,  '(') = {Fa = '('. Ea ')', Ea = .Ea 'opa' Ta, Ea =.Ta,
                            Ta = .Ta 'opm' Pa, Ta = .Pa, Pa = .Fa '**' Pa,
                            Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
E6 =  (8,  'id') = {Fa = 'id'.}
E7 =  (8,  'ctn') = {Fa = 'ctn'.}
T13 = (9,  Pa) = {Ta = Ta 'opm' Pa.}
T4 =  (9,  Fa) = {Pa = Fa. '**' Pa, Pa = Fa.}
E5 =  (9,  '(') = {Fa = '('. Ea ')', Ea = .Ea 'opa' Ta, Ea =.Ta,
                            Ta = .Ta 'opm' Pa, Ta = .Pa, Pa = .Fa '**' Pa,
                            Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
E6 =  (9,  'id') = {Fa = 'id'.}
E7 =  (9,  'ctn') = {Fa = 'ctn'.}
T14 = (10, Pa) = {Pa = Fa '**' Pa.}
T4 =  (10, Fa) = {Pa = Fa. '**' Pa, Pa = Fa.}
E5 =  (10, '(') = {Fa = '('. Ea ')', Ea = .Ea 'opa' Ta, Ea =.Ta,
                            Ta = .Ta 'opm' Pa, Ta = .Pa, Pa = .Fa '**' Pa,
                            Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
E6 =  (10, 'id') = {Fa = 'id'.}
E7 =  (10, 'ctn') = {Fa = 'ctn'.}
E15 = (11, ')') = {Ea = '(' Ea ')'.}
E8 =  (11, 'opa') = {Ea = Ea 'opa'. Ta,  Ta = .Ta 'opm' Pa,
                       Ta = .Pa, Pa = .Fa '**' Pa, Pa = .Fa, Fa = .'(' Ea ')',
                       Fa = .'id', Fa =.'ctn'}
E9 =  (12, 'opm') = {Ta = Ta 'opm'. Pa, Pa = .Fa '**' Pa,
                       Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
```

Cálculo das ações
---------
```
0 =  c({S = .Ea})
T1 = (0, Ea)     | [1, EOF] = AC
T2 = (0, Ta)     | [2, EOF, 'opa', ')'] = R2
T3 = (0, Pa)     | [3, EOF, 'opm', 'opa', ')'] = R4
T4 = (0, Fa)     | [4, EOF, 'opm', 'opa', ')'] = R6
E5 = (0, '(')    |
E6 = (0, 'id')   | [6, '**', EOF, 'opm', 'opa', ')'] = R8
E7 = (0, 'cten') | [7, '**', EOF, 'opm', 'opa', ')'] = R9
E8 = (1, 'opa')  |
E9 = (2, 'opm')  |
E10 = (4, '**')  |
T11 = (5, Ea)    |
T2 = (5, Ta)     |
T3 = (5, Pa)     |
T4 = (5, Fa)     |
E5 = (5, '(')    |
E6 = (5, 'id')   |
E7 = (5, 'cten') |
T12 = (8, Ta)    | [12, EOF, 'opa', ')'] = R1
T3 = (8, Pa)     |
T4 = (8, Fa)     |
E5 = (8, '(')    |
E6 = (8, 'id')   |
E7 = (8. 'cten') |
T13 = (9, Pa)    | [13, EOF, 'opm', 'opa', ')'] = R3
T4 = (9, Fa)     |
E5 = (9, '(')    |
E6 = (9, 'id')   |
E7 = (9, 'cten') |
T14 = (10, Pa)   | [14, EOF, 'opm', 'opa', ')'] = R5
T4 = (10, Fa)    |
E5 = (10, '(')   |
E6 = (10, 'id')  |
E7 = (10. 'cten')|
E15 = (11, ')')  | [15 '**', EOF, 'opm', 'opa', ')'] = R7
E8 = (11, 'opa') |
E9 = (12, 'opm') |
```

Tabela de análise
-----------
```
+----+-----+------+------+-----+-----+------+--------+-----+----+----+----+----+
|    |'opa'| 'opm'| '**' | '(' | ')' | 'id' | 'cten' | EOF | Ea | Ta | Pa | Fa |
+----+-----+------+------+-----+-----+------+--------+-----+----+----+----+----+
| 0  |     |      |      | E5  |     | E6   |   E7   |     | 1  | 2  | 3  | 4  |
+----+-----+------+------+-----+-----+------+--------+-----+----+----+----+----+
| 1  | E8  |      |      |     |     |      |        | AC  |    |    |    |    |
+----+-----+------+------+-----+-----+------+--------+-----+----+----+----+----+
| 2  | R2  | E9   |      |     | R2  |      |        | R2  |    |    |    |    |
+----+-----+------+------+-----+-----+------+--------+-----+----+----+----+----+
| 3  | R4  | R4   |      |     | R4  |      |        | R4  |    |    |    |    |
+----+-----+------+------+-----+-----+------+--------+-----+----+----+----+----+
| 4  | R6  | R6   | E10  |     | R6  |      |        | R6  |    |    |    |    |
+----+-----+------+------+-----+-----+------+--------+-----+----+----+----+----+
| 5  |     |      |      | E5  |     | E6   |   E7   |     | 11 | 2  | 3  | 4  |
+----+-----+------+------+-----+-----+------+--------+-----+----+----+----+----+
| 6  | R8  | R8   | R8   |     | R8  |      |        | R8  |    |    |    |    |
+----+-----+------+------+-----+-----+------+--------+-----+----+----+----+----+
| 7  | R9  | R9   | R9   |     | R9  |      |        | R9  |    |    |    |    |
+----+-----+------+------+-----+-----+------+--------+-----+----+----+----+----+
| 8  |     |      |      | E5  |     | E6   |   E7   |     |    | 12 | 3  | 4  |
+----+-----+------+------+-----+-----+------+--------+-----+----+----+----+----+
| 9  |     |      |      | E5  |     | E6   |   E7   |     |    |    | 13 | 4  |
+----+-----+------+------+-----+-----+------+--------+-----+----+----+----+----+
| 10 |     |      |      | E5  |     | E6   |   E7   |     |    |    | 14 | 4  |
+----+-----+------+------+-----+-----+------+--------+-----+----+----+----+----+
| 11 | E8  |      |      |     |     |      |        |     |    |    |    |    |
+----+-----+------+------+-----+-----+------+--------+-----+----+----+----+----+
| 12 | R1  | E9   |      |     | R1  |      |        | R1  |    |    |    |    |
+----+-----+------+------+-----+-----+------+--------+-----+----+----+----+----+
| 13 | R3  | R3   |      |     | R3  |      |        | R3  |    |    |    |    |
+----+-----+------+------+-----+-----+------+--------+-----+----+----+----+----+
| 14 | R5  | R5   |      |     | R5  |      |        | R5  |    |    |    |    |
+----+-----+------+------+-----+-----+------+--------+-----+----+----+----+----+
| 15 | R7  | R7   | R7   |     | R7  |      |        | R7  |    |    |    |    |
+----+-----+------+------+-----+-----+------+--------+-----+----+----+----+----+
```
