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
    strings = String.split(body, "\n")
    Enum.map(strings, fn x -> parse_line(x) end)
  end

  defp parse_line(line) do
    String.split(line, ",")
  end 
end

defmodule Segment do
  defstruct [:start, :end]

  def intersection(seg1, seg2) do
    a = { seg1.start.x, seg1.start.y }
    b = { seg1.end.x, seg1.end.y }
    c = { seg2.start.x, seg2.start.y }
    d = { seg2.end.x, seg2.end.y }
    cond do
      !envelope_check(a, b, c, d) -> {false, :disjoint, nil}
      true -> do_intersection(a, b, c, d, calc_denom(a, b, c, d))
    end
  end

  defp do_intersection(a, b, c, d, denom) when denom == 0, do: parallel_int(a, b, c, d)
  defp do_intersection(a, _, c, d, _) when a == c or a == d, do: {true, :vertex, a}
  defp do_intersection(_, b, c, d, _) when b == c or b == d, do: {true, :vertex, b}
  defp do_intersection({ax, ay}, {bx, by}, {cx, cy}, {dx, dy}, denom) do
    s = (ax * (dy - cy) + cx * (ay - dy) + dx * (cy - ay)) / denom
    t = -(ax * (cy - by) + bx * (ay - cy) + cx * (by - ay)) / denom

    cond do
      (t == 0 || t == 1) && collinear_not_between({ax, ay}, {bx, by}, {cx, cy}) -> {false, :disjoint, nil}
      (t == 0 || t == 1) && collinear_not_between({ax, ay}, {bx, by}, {dx, dy}) -> {false, :disjoint, nil}
      (s == 0 || s == 1) && collinear_not_between({cx, cy}, {dx, dy}, {ax, ay}) -> {false, :disjoint, nil}
      (s == 0 || s == 1) && collinear_not_between({cx, cy}, {dx, dy}, {bx, by}) -> {false, :disjoint, nil}
      s == 0 -> {true, :vertex, {ax, ay}}
      s == 1 -> {true, :vertex, {bx, by}}
      t == 0 -> {true, :vertex, {cx, cy}}
      t == 1 -> {true, :vertex, {dx, dy}}

      s > 0.0 && s < 1.0 && t > 0.0 && t < 1.0 -> {true, :interior, {ax + s * (bx - ax), ay + s * (by - ay)}}

      true -> {false, :disjoint, nil}
    end
  end

  defp calc_denom({ax, ay}, {bx, by}, {cx, cy}, {dx, dy}) do
    ax * (dy - cy) + bx * (cy - dy) + dx * (by - ay) + cx * (ay - by)
  end

  defp envelope_check({ax, ay}, {bx, by}, {cx, cy}, {dx, dy}) do
    cond do
      (ax < cx && ax < dx && bx < cx && bx < dx) -> false
      (ax > cx && ax > dx && bx > cx && bx > dx) -> false
      (ay < cy && ay < dy && by < cy && by < dy) -> false
      (ay > cy && ay > dy && by > cy && by > dy) -> false

      true -> true
    end
  end

  defp parallel_int(a, b, c, d) do
    cond do
      !collinear(a, b, c) -> {false, :disjoint, nil}

      a == c && (between(a, b, d) || between(a, d, b)) -> {true, :edge, nil}
      a == d && (between(a, b, c) || between(a, c, b)) -> {true, :edge, nil}
      b == c && (between(a, b, d) || between(b, d, a)) -> {true, :edge, nil}
      b == d && (between(a, b, c) || between(b, c, a)) -> {true, :edge, nil}

      a == c || a == d -> {true, :vertex, a}
      b == c || b == d -> {true, :vertex, b}

      true -> {true, :edge, nil}
    end
  end

  defp collinear_not_between(a, b, c) do
     collinear(a, b, c) && !between(a, b, c)
  end

  defp collinear({ax, ay}, {bx, by}, {cx, cy}) do
    cross({ax - cx, ay - cy}, {bx - cx, by - cy}) == {0, 0, 0}
  end

  defp cross({x1, y1}, {x2, y2}), do: {0, 0, x1 * y2 - y1 * x2}

  defp between({ax, ay}, {bx, by}, {_, py}) when ax == bx, do: ((ay <= py) && (py <= by)) || ((ay >= py) && (py >= by))
  defp between({ax, _}, {bx, _}, {px, _}), do: ((ax <= px) && (px <= bx)) || ((ax >= px) && (px >= bx))
end

defmodule Point do
  defstruct [:x, :y]
end

defmodule SegmentMapper do
  def map(directions) do
    current = %Point{x: 0, y: 0}
    list = []
    add_segment(directions, current, list)
  end

  defp add_segment([head | tail], current, list) do
    end_point = next_point(head, current)
    segment = %Segment{start: current, end: end_point}
    list = List.insert_at(list, length(list) - 1, segment)
    add_segment(tail, end_point, list)
  end

  defp add_segment([], _current, list) do
    list
  end

  defp next_point(movement, current) do
    [direction | amount] = String.graphemes(movement)
    amount = String.to_integer(Enum.join(amount))
    case direction do
      "R" -> %Point{x: current.x + amount, y: current.y}
      "L" -> %Point{x: current.x - amount, y: current.y}
      "D" -> %Point{x: current.x, y: current.y - amount}
      "U" -> %Point{x: current.x, y: current.y + amount}
    end
  end
end


defmodule IntersectionCalculator do
  def find(first, second) do
    set = []
    iterate_n(set, first, second)
  end

  defp iterate_n(set, [head | tail], second) do
    set = iterate_v(set, head, second)
    iterate_n(set, tail, second)
  end

  defp iterate_n(set, [], _second) do
    set
  end

  defp iterate_v(set, i, [head | tail]) do
    { intersects, _type, point } = Segment.intersection(i, head)
    if(intersects == true) do
      {x, y} = point
      IO.puts("Point: #{x}, #{y}")
      iterate_v(List.insert_at(set, length(set) - 1, %Point{x: x, y: y}), i, tail)
    else
      iterate_v(set, i, tail)
    end
  end

  defp iterate_v(set, _first, []) do
    set
  end
end

defmodule MinimumManhattan do
  def minimum(intersections) do
    Enum.map(intersections, fn p -> abs(p.x) + abs(p.y) end)
  end
end

file = "./data.txt"
data = Reader.read(file)
segments = Enum.map(data, fn x -> SegmentMapper.map(x) end)
IntersectionCalculator.find(Enum.at(segments, 0), Enum.at(segments, 1))
|> MinimumManhattan.minimum
|> Enum.each(fn x -> IO.puts(x) end)