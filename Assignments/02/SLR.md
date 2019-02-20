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
    |   I0 = c({S = .Ea}) = {S = .Ea, Ea = .Ea 'opa' Ta, Ea =.Ta,
                             Ta = .Ta 'opm' Pa, Ta = .Pa, Pa = .Fa '**' Pa,
                             Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
T1  |  I1 = goto(I0,  Ea) = {S = Ea., Ea = Ea. 'opa' Ta}
T2  |  I2 = goto(I0,  Ta) = {Ea = Ta., Ta = Ta. 'opm' Pa}
T3  |  I3 = goto(I0,  Pa) = {Ta = Pa.}
T4  |  I4 = goto(I0,  Fa) = {Pa = Fa. '**' Pa, Pa = Fa.}
E5  |  I5 = goto(I0, '(') = {Fa = '('. Ea ')', Ea = .Ea 'opa' Ta, Ea =.Ta,
                            Ta = .Ta 'opm' Pa, Ta = .Pa, Pa = .Fa '**' Pa,
                            Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
E6  |  I6 = goto(I0, 'id') = {Fa = 'id'.}
E7  |  I7 = goto(I0,'ctn') = {Fa = 'ctn'.}
E8  |  I8 = goto(I1, 'opa') = {Ea = Ea 'opa'. Ta, Ta = .Ta 'opm' Pa,
                            Ta = .Pa, Pa = .Fa '**' Pa, Pa = .Fa,
                            Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
E9  |  I9 = goto(I2, 'opm') = {Ta = Ta 'opm'. Pa, Pa = .Fa '**' Pa,
                            Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
E10 | I10 = goto(I4, '**') = {Pa = Fa '**'. Pa, Pa = .Fa, Fa = .'(' Ea ')',
                            Fa = .'id', Fa =.'ctn'}
T11 | I11 = goto(I5,  Ea) = {Ea = '(' Ea. ')', Ea = Ea. 'opa' Ta}
T2  |  I2 = goto(I5,  Ta) = {Ea = Ta., Ta = Ta. 'opm' Pa}
T3  |  I3 = goto(I5,  Pa) = {Ta = Pa.}
T4  |  I4 = goto(I5,  Fa) = {Pa = Fa. '**' Pa, Pa = Fa.}
E5  |  I5 = goto(I5,  '(') = {Fa = '('. Ea ')', Ea = .Ea 'opa' Ta, Ea =.Ta,
                            Ta = .Ta 'opm' Pa, Ta = .Pa, Pa = .Fa '**' Pa,
                            Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
E6  |  I6 = goto(I5,  'id') = {Fa = 'id'.}
E7  |  I7 = goto(I5,  'ctn') = {Fa = 'ctn'.}
T12 | I12 = goto(I8,  Ta) = {Ea = Ea 'opa' Ta.,  Ta = Ta. 'opm' Pa}
T3  |  I3 = goto(I8,  Pa) = {Ta = Pa.}
T4  |  I4 = goto(I8,  Fa) = {Pa = Fa. '**' Pa, Pa = Fa.}
E5  |  I5 = goto(I8,  '(') = {Fa = '('. Ea ')', Ea = .Ea 'opa' Ta, Ea =.Ta,
                            Ta = .Ta 'opm' Pa, Ta = .Pa, Pa = .Fa '**' Pa,
                            Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
E6  |  I6 = goto(I8,  'id') = {Fa = 'id'.}
E7  |  I7 = goto(I8,  'ctn') = {Fa = 'ctn'.}
T13 | I13 = goto(I9,  Pa) = {Ta = Ta 'opm' Pa.}
T4  |  I4 = goto(I9,  Fa) = {Pa = Fa. '**' Pa, Pa = Fa.}
E5  |  I5 = goto(I9,  '(') = {Fa = '('. Ea ')', Ea = .Ea 'opa' Ta, Ea =.Ta,
                            Ta = .Ta 'opm' Pa, Ta = .Pa, Pa = .Fa '**' Pa,
                            Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
E6  |  I6 = goto(I9,  'id') = {Fa = 'id'.}
E7  |  I7 = goto(I9,  'ctn') = {Fa = 'ctn'.}
T14 | I14 = goto(I10, Pa) = {Pa = Fa '**' Pa.}
T4  |  I4 = goto(I10, Fa) = {Pa = Fa. '**' Pa, Pa = Fa.}
E5  |  I5 = goto(I10, '(') = {Fa = '('. Ea ')', Ea = .Ea 'opa' Ta, Ea =.Ta,
                            Ta = .Ta 'opm' Pa, Ta = .Pa, Pa = .Fa '**' Pa,
                            Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
E6  |  I6 = goto(I10, 'id') = {Fa = 'id'.}
E7  |  I7 = goto(I10, 'ctn') = {Fa = 'ctn'.}
T15 | I15 = goto(I11, ')') = {Ea = '(' Ea ')'.}
E8  |  I8 = goto(I11, 'opa') = {Ea = Ea 'opa'. Ta,  Ta = .Ta 'opm' Pa,
                       Ta = .Pa, Pa = .Fa '**' Pa, Pa = .Fa, Fa = .'(' Ea ')',
                       Fa = .'id', Fa =.'ctn'}
E9  |  I9 = goto(I12, 'opm') = {Ta = Ta 'opm'. Pa, Pa = .Fa '**' Pa,
                       Pa = .Fa, Fa = .'(' Ea ')', Fa = .'id', Fa =.'ctn'}
```
