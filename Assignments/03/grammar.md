# Universidade Federal de Alagoas
Instituto de Computação

Aluno: Antonio Manoel



### Adaptar a gramática para análise descendente

Gramática
-----------
```
(1) Res = Ea '='       {printf("%f", Ea.val);}
(2) Ea = Ea1 '+' Ta    {Ea.val = Ea1.val + Ta.val;}
(3)    | Ea1 '-' Ta    {Ea.val = Ea1.val - Ta.val;}
(4)    | Ta            {Ea.val = Ta.val;}
(5) Ta = Ta '*' Fa     {Ta.val = Ta1.val * Fa.val;}
(6)    | Ta '/' Fa     {Ta.val = Ta1.val / Fa.val;}
(7)    | Fa            {Ta.val = Fa.val;}
(8) Fa = '(' Ea ')'    {Fa.val = Ea.val;}
(9)    |'cteN'         {Fa.val = atof(cteN.lex);}
```
Adaptada
--------
```
(1) Res = Ea '='
(2) Ea = Ta Ear
(3) Ear = '+' Ta Ear
(4) Ear = '-' Ta Ear
(5) Ear = $
(6) Ta = Fa Tar
(7) Tar = '*' Fa Tar
(8) Tar = '/' Fa Tar
(9) Tar = $
(10) Fa = '(' Ea ')'
(11) Fa = 'cteN'
```

### Adicionar ações semânticas
-------------
```
(1) Res = Ea '=' {printf("%f", Ea.val);}
(2) Ea = Ta {Ear.h = Ta.val} Ear {Ea.val = Ear.s}
(3) Ear = '+' Ta {Ear1.h = Ea1.val + Ta.val} Ear1 {Ea.val = Ea1.val + Ta.val}
(4) Ear = '-' Ta {Ear1.h = Ea1.val + Ta.val;} Ear1 {Ea.val = Ea1.val + Ta.val;}
(5) Ear = $ {Ear.s = Ear.h}
(6) Ta = Fa {Tar.h = Fa.val} Tar {Ta.val = Tar.s}
(7) Tar = '*' Fa {Tar1.h = Tar.h * Fa.val} Tar1 {Tar.s=Tar1.s}
(8) Tar = '/' Fa {Tar1.h = Tar.h / Fa.val} Tar1 {Tar.s=Tar1.s}
(9) Tar = $ {Tar.s = Tar.h}
(10) Fa = '(' Ea ')' {Fa.val = Ea.val}
(11) Fa = 'cteN' {Fa.val = atof(cten.lex)}
```
