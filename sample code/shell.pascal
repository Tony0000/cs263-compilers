program shellsort;
const
  MaxN = 100;
type
  TArray = array [0..MaxN] of Integer;
var
    k, n : Integer;
    v, inv_v: TArray;

procedure echoArray (var vector: TArray; var size: Integer);
var i : Integer;
begin
  for i := 0 to size do
   begin
    write(vector[i]);
    write(' ');
   end;
end;

procedure ShellSort ( var A : TArray; N : Integer );
var
  i, j, step, tmp : Integer;
begin
  step:=N div 2;
  while step>0 do
	begin
    for i:=step to N do
		begin
      tmp:=A[i];
      j:=i;
      while (j >= step) and (A[j-step] > tmp) do
      begin
        A[j]:=A[j-step];
        j := j - step;
      end;
      A[j]:=tmp;
    end;
    step:=step div 2;
  end;
  echoArray(A, n);
end;

begin
  read(n);
  n := n-1;
  for k := 0 to n do
  begin
	    read(v[k]);
  end;
  write('desordenados: ');
  echoArray(v, n);
  writeln('');
  write('ordenados: ');
  shellsort(v, n);
end.
