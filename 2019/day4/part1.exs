defmodule Reader do
  def read(file) do
    case File.read(file) do
      {:ok, body}      -> parse(body)
      {:error, reason} -> handleError(reason)
    end
  end

  defp handleError(reason) do
      IO.puts("Error " + reason)
  end

  defp parse(body) do
    String.split(body, "-")
    |> Enum.map(fn x -> String.to_integer(x) end)
  end
end

defmodule PasswordFinder do
  def find(values) do
    find(Enum.at(values, 0), Enum.at(values, 1))
  end

  defp find(current, maximum, set \\ [])

  defp find(current, maximum, set) when current <= maximum do
    case is_valid(current) do
      true -> 
        IO.puts("Number #{current} is valid")
        new_set = List.insert_at(set, length(set), current)
        find(current + 1, maximum, new_set)
      false -> find(current + 1, maximum, set)
    end
  end

  defp find(current, maximum, set) when current > maximum do
    set
  end

  defp is_valid(digit) do
    test = String.graphemes(Integer.to_string(digit))
    true && length(test) == 6 && two_adjacent(test) && always_increasing(test)
  end

  defp two_adjacent([head | tail]) do
    case head == Enum.at(tail, 0) do
      true -> true
      false -> two_adjacent(tail)
    end
  end

  defp two_adjacent([]) do
    false
  end

  defp always_increasing([head | tail]) do
    if length(tail) > 0 do
      case head <= Enum.at(tail, 0) do
        false -> false
        true -> always_increasing(tail)
      end
    else
      true
    end
  end

  defp always_increasing([]) do
    true
  end
end


file="./data.txt"
Reader.read(file)
|> PasswordFinder.find
|> length
|> IO.puts