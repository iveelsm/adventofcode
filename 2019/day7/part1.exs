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
    { new_list, next } = case parse_instruction(Enum.at(list, n)) do
      {1, a, b, c}      -> add(list, n, {a, b, c})
      {2, a, b, c}      -> multiply(list, n, {a, b, c})
      {3, _a, _b, _c}   -> store(list, input, n)
      {4, _a, _b, _c}   -> output(list, n)
      {5, _a, b, c}     -> jump_if_true(list, n, {b, c})
      {6, _a, b, c}     -> jump_if_false(list, n, {b, c})
      {7, a, b, c}      -> less_than(list, n, {a, b, c})
      {8, a, b, c}      -> equals(list, n, {a, b, c})
      {99, _a, _b, _c}  -> {nil, nil}
    end
    case {new_list, next} do
        {nil, nil} -> IO.puts("Done")
        {_, _}     -> compute(new_list, input, next)
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
    { List.replace_at(list, pos, sum), n + 4 }
  end

  defp multiply(list, n, {a, b, c}) do
    i = if c == 0, do: Enum.at(list, Enum.at(list, n + 1)), else: Enum.at(list, n + 1)
    j = if b == 0, do: Enum.at(list, Enum.at(list, n + 2)), else: Enum.at(list, n + 2)
    pos = if a == 0, do: Enum.at(list, n + 3), else: Enum.at(list, n + 3)
    product = i * j
    { List.replace_at(list, pos, product), n + 4 }
  end

  defp store(list, input, n) do
    pos = Enum.at(list, n + 1)
    { List.replace_at(list, pos, input), n + 2 }
  end

  defp output(list, n) do
    test = Enum.at(list, n + 1)
    if Enum.at(list, test) == 0 do
      IO.puts("#{Enum.at(list,test)}")
    else
      IO.puts("#{Enum.at(list,test)}")
    end
    { list, n + 2}
  end

  defp jump_if_true(list, n, {b, c}) do
    i = if c == 0, do: Enum.at(list, Enum.at(list, n + 1)), else: Enum.at(list, n + 1)
    j = if b == 0, do: Enum.at(list, Enum.at(list, n + 2)), else: Enum.at(list, n + 2)
    next = if i != 0, do: j, else: n + 3
    {list, next}
  end

  defp jump_if_false(list, n, {b, c}) do
    i = if c == 0, do: Enum.at(list, Enum.at(list, n + 1)), else: Enum.at(list, n + 1)
    j = if b == 0, do: Enum.at(list, Enum.at(list, n + 2)), else: Enum.at(list, n + 2)
    next = if i == 0, do: j, else: n + 3
    { list, next }
  end

  defp less_than(list, n, {a, b, c}) do
    i = if c == 0, do: Enum.at(list, Enum.at(list, n + 1)), else: Enum.at(list, n + 1)
    j = if b == 0, do: Enum.at(list, Enum.at(list, n + 2)), else: Enum.at(list, n + 2)
    pos = if a == 0, do: Enum.at(list, n + 3), else: Enum.at(list, n + 3)
    lt = if i < j, do: 1, else: 0
    { List.replace_at(list, pos, lt), n + 4 }
  end

  defp equals(list, n, {a, b, c}) do
    i = if c == 0, do: Enum.at(list, Enum.at(list, n + 1)), else: Enum.at(list, n + 1)
    j = if b == 0, do: Enum.at(list, Enum.at(list, n + 2)), else: Enum.at(list, n + 2)
    pos = if a == 0, do: Enum.at(list, n + 3), else: Enum.at(list, n + 3)
    equals = if i == j, do: 1, else: 0
    { List.replace_at(list, pos, equals), n + 4}
  end
end

defmodule AmplifierProcess do
  def compute_max(data) do

  end

  def process(data, [head | tail], start \\ 0) do
    Int
  end

  def process(_data, [], output) do
    output
  end
end

file = "./data.txt"
Reader.read(file)
|> IntCodeComputer.process(5)
