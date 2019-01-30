/* Universidade Federal de Alagoas - Campus A.C. Simões
*  Aluno: Antônio Manoel
*  Pseudo código das funções de um analisador descendente preditivo recursivo.
*/

void main(){
	//Abre o arquivo
	//Cria o analisador léxico
	//Cria o token
	//Acessa o primeiro token
    fpgm();
}

// pgm = ldecl '::' lsent'.'
void fpgm(){
	fldecl();
	if(tk.categ() == DPTDPT){
		tk.next();
		flsent(); //Implementar
		if(tk.categ() == PT){
			tk.next();
			if(tk.categ() == EOF){
				return;
			}else{
				erro(EOF, " esperado", tk)
			}
		}else{
			erro(PT, " esperado", tk);
		}
	}else{
		erro(DPTDPT, " esperado", tk);
	}
}

// ldecl = decl ldeclr
void fldecl(){
  fdecl();
  fldeclr();
}

//ldeclr = ';' declr ldeclr | e
void fldeclr(){
  if(tk.categ() == PTVG){
    fdeclr();
    fldeclr();
  }
}

//lid = 'id' lidr
void flid(){
  if(tk.categ() == 'id'){
    flidr();
  }else{
    erro(ID, " esperado", tk);
  }
}

//lid = ',' 'id' lidr | e
void flidr(){
  if(tk.categ() == VG){
    tk.next();
    if(tk.categ() == ID){
      tk.next();
      flidr();
    }
  }
}

//tipo = tbase tipof
void ftipo(){
  ftbase();
  ftipof();
}

//tipof = '[' 'cteI' ']' | e
void ftipof(){
  if(tk.categ() == LEFTBRA){
    tk.next();
    if(tk.categ() == CTEI){
      tk.next();
      if(tk.categ() == RIGHTBRA){
        tk.next();
      }else{
        erro(RIGHTBRA, " esperado", tk);
      }
    }else{
      erro(CTEI, " esperado", tk);
    }
  }
}

//tbase = 'int' | 'real'
void ftbase(){
  if(tk.categ() == INT){
    tk.next();
  }else if(tk.categ() == REAL){
    tk.next();
  }else{
    erro(INT, " ou ", REAL, "esperado");
  }
}

//lsent = sent lsentr
void flsent(){
  fsent();
  flsentr();
}

//lsentr = ';' sent lsentr | e
void flsentr(){
  if(tk.categ() ==  PTVG){
    tk.next();
    fsent();
    flsentr();
  }
}

//sent = atr | cond | iter
void fsent(){
  fatr();
  fcond();
  fiter();
}

//atr = 'id' '=' Ea
void fatr(){
  if(tk.categ() == ID){
    tk.next();
    if(tk.categ() == EQ){
      tk.next();
      fea();
    }else{
      erro(EQ, " esperado", tk);
    }
  }else{
    erro(ID, " esperado", tk);
  }
}

//cond = 'se' eb 'entao' lsent condf
void fcond(){
  if(tk.categ() == SE){
    tk.next();
    feb()
    if(tk.categ() == ENTAO){
      tk.next();
      flsent();
      fcondf();
    }else{
      erro(ENTAO, " esperado", tk);
    }
  }else{
    erro(SE, " esperado", tk);
  }
}

//condf = 'senao' lsent 'fim' | 'fim'
void fcondf(){
  if(tk.categ() == SENAO){
    tk.next();
    flsent();
    if(tk.categ() == FIM){
      tk.next();
    }else{
      erro(FIM, " esperado", tk);
    }
  }else if(tk.categ() == FIM){
    tk.next();
  }else{
    erro(SENAO, " ou ", FIM, " esperado", tk);
  }
}

//iter = 'para' atr 'ate' ea passo 'faça' lsent 'fim'
//    | 'enquanto' eb 'faça' lsent 'fim'
//    | 'repita' lsent 'enquanto' eb 'fim'
void fiter(){
  if(tk.categ() == PARA){
    tk.next();
    fatr();
    if(tk.categ() == ATE){
      tk.next();
      fea();
      fpasso();
      if(tk.categ() == FACA){
        tk.next();
        flsent();
        if(tk.categ() == FIM){
          tk.next();
        }else{
          erro(FIM, " esperado", tk);
        }
      }else{
        erro(FACA, " esperado", tk);
      }
    }else{
      erro(ATE, " esperado", tk);
    }
  }else if(tk.categ() == ENQUANTO){
    feb();
    if(tk.categ() == FACA){
      tk.next();
      flsent();
      if(tk.categ() == FIM){
        tk.next();
      }
    }else{
        erro(FACA, " esperado", tk);
    }
  }else if(tk.categ() == REPITA){
    tk.next();
    flsent();
    if(tk.categ() == ENQUANTO){
      tk.next();
      feb();
      if(tk.categ() == FIM){
        tk.next();
      }else{
        erro(FIM, " esperado", tk);
      }
    }else{
      erro(ENQUANTO, " esperado", tk);
    }
  }else{
    erro(PARA, " ou ", ENQUANTO, " ou ", REPITA, " esperado", tk);
  }
}

//passo = 'passo' ea | e
void fpasso(){
  if(tk.categ() == PASSO){
    fea();
  }
}
