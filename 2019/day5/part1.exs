defmodule Reader do
  def read(file) do
    case File.read(file) do
      {:ok, body}      -> parse(body)
      {:error, reason} -> handleError(reason)
    end
  end

  defp handleError(reason) do
      IO.puts("Error #{reason}")
  end

  defp parse(body) do
    String.split(body, ",")
    |> Enum.map(fn x -> String.to_integer(x) end)
  end
end

defmodule IntCodeComputer do
  def process(list, input) when is_list(list) do
    compute(list, input)
  end

  defp compute(list, input, n \\ 0) when n < length(list) do
    case parse_instruction(Enum.at(list, n)) do
      {1, a, b, c}     -> compute(add(list, n, {a, b, c}), input, n + 4)
      {2, a, b, c}     -> compute(multiply(list, n, {a, b, c}), input, n + 4)
      {3, _a, _b, c}   -> compute(store(list, input, n, {c}), input, n + 2)
      {4, _a, _b, c}   -> compute(output(list, n, {c}), input, n + 2) 
      {99, _a, _b, _c} -> IO.puts("\nDone")
    end
  end
  
  defp parse_instruction(instruction) do
    result = Integer.to_string(instruction)
    |> String.graphemes
    |> pad
    {
      String.to_integer(Enum.join(Enum.take(result, -2))),
      String.to_integer(Enum.at(result, 0)),
      String.to_integer(Enum.at(result, 1)),
      String.to_integer(Enum.at(result, 2))
    }
  end

  defp pad(list) do
    if length(list) <= 4 do
      pad(List.insert_at(list, 0, "0"))
    else
      list
    end
  end

  defp add(list, n, {a, b, c}) do
    i = if c == 0, do: Enum.at(list, Enum.at(list, n + 1)), else: Enum.at(list, n + 1)
    j = if b == 0, do: Enum.at(list, Enum.at(list, n + 2)), else: Enum.at(list, n + 2)
    pos = if a == 0, do: Enum.at(list, n + 3), else: Enum.at(list, n + 3)
    sum = i + j
    List.replace_at(list, pos, sum)
  end

  defp multiply(list, n, {a, b, c}) do
    i = if c == 0, do: Enum.at(list, Enum.at(list, n + 1)), else: Enum.at(list, n + 1)
    j = if b == 0, do: Enum.at(list, Enum.at(list, n + 2)), else: Enum.at(list, n + 2)
    pos = if a == 0, do: Enum.at(list, n + 3), else: Enum.at(list, n + 3)
    product = i * j
    List.replace_at(list, pos, product)
  end

  defp store(list, input, n, {c}) do
    pos = if c != 0, do: Enum.at(list, Enum.at(list, n + 1)), else: Enum.at(list, n + 1)
    List.replace_at(list, pos, input)
  end

  defp output(list, n, {c}) do
    test = if c != 0, do: Enum.at(list, Enum.at(list, n + 1)), else: Enum.at(list, n + 1)
    if Enum.at(list, test) == 0 do
      IO.puts("#{Enum.at(list,test)}")
    else
      IO.puts("#{Enum.at(list,test)}")
    end
    list 
  end
end


file = "./data.txt"
Reader.read(file)
|> IntCodeComputer.process(1)