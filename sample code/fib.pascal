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
      begin
          write(a);
          write(', ');
          write(b);
          while a + b <= n do
          begin
            write(', ');
            write(a + b);
            aux := a;
            a := b;
            b := b + aux;
          end;
      end;
end;

var n: Integer;
begin
  read(n);
  fib(n);
end.
