file = "./data.txt"

defmodule Part1 do
    def read(file) do
        case File.read(file) do
            {:ok, body} -> parseData(body)
            {:error, reason} -> handleError(reason)
        end
    end

    def parseData(body) do
        strings = String.split(body, "\n")
        Enum.map(strings, fn x -> String.to_integer(x) end)
    end

    def handleError(reason) do
        IO.puts("Error" + reason)
    end

    def computeFuels(list) when is_list(list) do
        Enum.map(list, fn x -> computeFuel(x) end)
    end

    def computeFuel(x) when is_integer(x) do
        Integer.floor_div(x, 3) - 2
    end

    def sum(list) when is_list(list) do
        Enum.sum(list)
    end
end

defmodule Part2 do
    def read(file) do
        case File.read(file) do
            {:ok, body} -> parseData(body)
            {:error, reason} -> handleError(reason)
        end
    end

    def parseData(body) do
        strings = String.split(body, "\n")
        Enum.map(strings, fn x -> String.to_integer(x) end)
    end

    def handleError(reason) do
        IO.puts("Error" + reason)
    end

    def computeFuels(list) when is_list(list) do
        Enum.map(list, fn x -> computeFuel(x) end)
    end

    def computeFuel(x) when is_integer(x) do
        initial = fuelAlgorithm(x)
        compute(initial, initial)
    end

    def compute(a, b) do
        next = fuelAlgorithm(b)
        if next <= 0 do
            a
        else 
            compute(a + next, next);
        end 
    end

    def fuelAlgorithm(x) do
        Integer.floor_div(x, 3) - 2
    end

    def sum(list) when is_list(list) do
        Enum.sum(list)
    end
end

result = Part1.read(file)
fuelComputed = Part1.computeFuels(result)
result = Part1.sum(fuelComputed)
IO.puts(result)

result = Part2.read(file)
fuelComputed = Part2.computeFuels(result)
result = Part2.sum(fuelComputed)
IO.puts(result)