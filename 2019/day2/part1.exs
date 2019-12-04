defmodule Challenge do
    def run(file) do
      read(file)
      |> swap
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

    defp swap(list) do
      List.replace_at(list, 1, 12)
      |> List.replace_at(2, 2)
    end

    defp process(list) when is_list(list) do
      compute(list)
    end

    defp compute(list, n \\ 0) when n < length(list) do
      case Enum.at(list, n) do
        1  -> compute(add(list, n), n + 4)
        2  -> compute(multiply(list, n), n + 4)
        99 -> print_output(list)
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

    def print_output(list) do
      res = Enum.at(list, 0)
      IO.puts("Result #{res}")
    end
end

file = "./data.txt"
Challenge.run(file)
