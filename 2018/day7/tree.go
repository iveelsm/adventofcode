package main

type TreeNode struct {
	node    string
	enables []*TreeNode
	prereqs []*TreeNode
}

type Tree struct {
	heads []*TreeNode
	nodes map[string]*TreeNode
}

func BuildTree(data []Instruction) Tree {
	tree := Tree{
		heads: make([]*TreeNode, 0, 0),
		nodes: make(map[string]*TreeNode),
	}
	for _, instruction := range data {
		tree = Append(tree, instruction.node, instruction.nextNode)
	}
	return tree
}

func Append(t Tree, node string, nextNode string) Tree {
	current, currentOk := t.nodes[node]
	next, nextOk := t.nodes[nextNode]
	if currentOk {
		if !nextOk {
			next = &TreeNode{
				node: nextNode,
			}
		}
	} else {
		current = &TreeNode{
			node: node,
		}

		if !nextOk {
			next = &TreeNode{
				node: nextNode,
			}
		}

	}
	return addNewNodes(t, current, next)
}

func addNewNodes(t Tree, current *TreeNode, next *TreeNode) Tree {
	current.enables = addNode(current.enables, next)
	next.prereqs = addNode(next.prereqs, current)
	if len(current.prereqs) == 0 {
		t.heads = addNode(t.heads, current)
	}
	t.nodes[current.node] = current
	t.nodes[next.node] = next
	return t
}

func addNode(current []*TreeNode, addition *TreeNode) []*TreeNode {
	for _, n := range current {
		if addition.node == n.node {
			return current
		}
	}
	return append(current, addition)
}

func (t *TreeNode) InArray(a []*TreeNode) bool {
	for _, i := range a {
		if i.node == t.node {
			return true
		}
	}
	return false
}

func (t *TreeNode) IsAvailable(result string) bool {
	available := true
	for _, el := range t.prereqs {
		inCompleted := InString(result, el.node)
		if !inCompleted {
			return false
		}
	}
	return available
}
