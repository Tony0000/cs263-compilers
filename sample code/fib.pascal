program Fibonacci;
procedure fib(n: Integer);
var
  a, b, aux: Integer;

begin
  a := 0;
  b := 1;
  if n = 0 then
      writeln(a)
  else
      writeln(a);
      writeln(b);
      while a + b <= n do
      begin
        writeln(a + b);
        aux := a;
        a := b;
        b := b + aux;
      end;
end;

begin
  var n: Integer;
  read(n);
  fib(n);
end.
