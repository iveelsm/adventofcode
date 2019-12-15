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
    String.split(body, "\n")
    |> Enum.map(fn x ->
      String.split(x, ")")
    end)
  end
end


defmodule Tree do
  defstruct [:nodes]

  defmodule Node do
    defstruct [:distance, :name]

    def new(distance, name) do
      %__MODULE__{
        distance: distance,
        name: name
      }
    end
  end

  def new(root) do
    %{root => Tree.Node.new(0, root)}
  end

  def add(tree, parent, child) do
    existing = find(tree, parent)
    Map.put(tree, child, Tree.Node.new(existing.distance + 1, child))
  end

  def find(tree, name) do
    Map.fetch!(tree, name)
  end

  def sum(tree) do
    Map.values(tree)
    |> Enum.reduce(0, fn (x, acc) -> x.distance + acc end)
  end
end

defmodule TreeBuilder do
  def build(data) do
    case find_start(data) do
      nil -> IO.puts("Error finding start")
      [root, _y]   ->
        Tree.new(root)
        |> build_tree(root, data)
    end
  end

  defp build_tree(tree, parent, data) do
    case find_nodes(parent, data) do
      nil    -> tree
      nodes  -> add_nodes(tree, parent, data, nodes)
    end
  end

  defp add_nodes(tree, parent, data, [head | tail]) do
    [_x, y] = head
    add_node(tree, parent, y)
    |> build_tree(y, data)
    |> add_nodes(parent, data, tail)
  end

  defp add_nodes(tree, _parent, _data, []) do
    tree
  end

  defp add_node(tree, parent, node), do: Tree.add(tree, parent, node)
  defp find_nodes(name, data), do: Enum.filter(data, fn [x, _y] -> x == name end)
  defp find_start(data), do: Enum.find(data, fn [x, _y] -> x == "COM" end)
end

file = "./data.txt"
Reader.read(file)
|> TreeBuilder.build
|> Tree.sum
|> IO.puts
