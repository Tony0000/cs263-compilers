program Fibonacci;
procedure fib(n: Integer);
var
  u, v, w: Integer;

begin
  if n <= 1 then
    write("0");
    exit(0);
  if n = 2 then
    write('0, 1, 1');
  u := 1;
  v := 1;
  write('0, 1, 1');
  while w+u < n do
  begin
    w := u + w;
    u := v;
    v := w;
    write(", ");
  end;
end;

begin
  var n: Integer;
  read(n);
  fib(n);
end.
