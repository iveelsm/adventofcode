defmodule Challenge do
    def run(file) do
      read(file)
      |> process
    end

    defp read(file) do
        case File.read(file) do
            {:ok, body} -> parseData(body)
            {:error, reason} -> handleError(reason)
        end
    end

    defp parseData(body) do
        strings = String.split(body, ",")
        Enum.map(strings, fn x -> String.to_integer(x) end)
    end

    defp handleError(reason) do
        IO.puts("Error " + reason)
    end

    defp swap(list, n, v) do
      List.replace_at(list, 1, n)
      |> List.replace_at(2, v)
    end

    defp process(list) when is_list(list) do
      {n, v} = iterate_n(list)
      IO.puts("N: #{n}, V: #{v}, Result: #{100 * n + v}")
    end

    defp iterate_n(list, n \\ 0) when n < 100 do
      result = iterate_v(list, n)
      case result do
        nil -> iterate_n(list, n + 1)
        _ -> result
      end
    end

    defp iterate_v(list, n, v \\ 0)

    defp iterate_v(list, n, v) when v < 100 do
      s = swap(list, n, v)
      result = compute(s)
      case result do
        19690720 -> {n, v}
        _ -> iterate_v(list, n, v + 1)
      end
    end

    defp iterate_v(_list, _n, v) when v >= 100 do
      nil
    end

    defp compute(list, n \\ 0) when n < length(list) do
      case Enum.at(list, n) do
        1  -> compute(add(list, n), n + 4)
        2  -> compute(multiply(list, n), n + 4)
        99 -> Enum.at(list, 0)
      end
    end

    defp add(list, n) do
      a = Enum.at(list, Enum.at(list, n + 1))
      b = Enum.at(list, Enum.at(list, n + 2))
      c = Enum.at(list, n + 3)
      sum = a + b
      List.replace_at(list, c, sum)
    end

    defp multiply(list, n) do
      a = Enum.at(list, Enum.at(list, n + 1))
      b = Enum.at(list, Enum.at(list, n + 2))
      c = Enum.at(list, n + 3)
      product = a * b
      List.replace_at(list, c, product)
    end
end

file = "./data.txt"
Challenge.run(file)
