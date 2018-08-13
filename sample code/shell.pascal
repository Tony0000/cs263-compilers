program shellsort
function shellsort (vector: array of Integer, size: Integer) : Integer
	begin
	  var
	  j, value : Integer;
	  var gap := 1;

  while gap < size do
  begin
      gap = 3 * gap + 1;
  end;

  while gap > 1 do
    	begin
	    gap = gap / 3;
	    for i := gap to size do
        begin
	      value = vector[i];
	      j = i - gap;
	      while j >= 0 and value < vector[j] do
        	begin
	        vector[j / gap] = vector[j];
	        j = j - gap;
	      end;
	      vector[j - gap] = value;
	    end;
	  end;
	  shellsort := vector;
	end;

	procedure echoArray (vector : array of Integer, size: Integer)
	begin
	  var i : Integer;
	  for i := 0 to size do
  begin
	    write(vector[i])
	  end;
	end;

	begin
	var i, n : Integer;
  read(n);
  type int_vector = array[0..n] of Integer;
  var vector: int_vector;
  for i := 0 to 10 do
  begin
	    read(vector[i]);
	end;
	  echoArray(vector, n);
	  array = shellsort(vector, n);
	  echoArray(vector, n);
end.
