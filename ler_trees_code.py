nodes_number = 0
colors = []
node_list = []

count_l = 0
count_e = 0
count_r = 0

class Node:
    def __init__(self, key, colour):
        self.key = key
        self.colour = colour
        self.parent = None
        self.left = None
        self.right = None
        self.left_key = None
        self.right_key = None
        self.is_principal = False
        self.w = 0   #number of whites in left subtree
        self.ww = 0  #number of whites in right subtree
        self.b = 0   #number of blacks in left subtree
        self.bb = 0  #number of blacks in right subtree
        self.whites = 0
        self.blacks = 0
        self.visited = False


def get_inputs_from_file(dir):
    global nodes_number
    global colors

    line_num = 0
    file = open(dir)

    for line in file:
        if line_num == 0:
            nodes_number = line.strip("\n")
            nodes_number = int(nodes_number)

        elif line_num == 1:
            temp_line = line.strip("\n")
            colors = temp_line.split()
            for i in range(nodes_number):
                node = Node(i, int(colors[i]))
                node_list.append(node)

        else:
            temp_line = line.strip("\n")
            temp_line = temp_line.split()
            a = int(temp_line[0])
            b = int(temp_line[1])
            c = int(temp_line[2])

            if c == 0:
                node_list[a].left = node_list[b]
                node_list[b].parent = node_list[a]

            elif c == 1:
                node_list[a].right = node_list[b]
                node_list[b].parent = node_list[a]

        line_num += 1

    file.close()

def postorder(node):
    global count_l
    global count_e
    global count_r

    if node:

        postorder(node.left)        # First recur on left child
        postorder(node.right)        # the recur on right child

        # now print the data of node
        # print("----------------------")
        # print("Processing the node --->", node.key, node.colour)

        if not node.right and not node.left: # NODE IS A LEAF
            if node.colour == 0:
                node.whites += 1
            elif node.colour == 1:
                node.blacks += 1
            # print("Whites", node.whites, "blacks", node.blacks)

        elif node.left and not node.right:  # ONLY LEFT CHILD

            if node.colour == 0: #white
                node.whites += node.left.whites + 1
                node.blacks += node.left.blacks
            elif node.colour == 1: #black
                node.blacks += node.left.blacks + 1
                node.whites += node.left.whites
            # print("Whites", node.whites, "blacks", node.blacks)

            if node.left.colour == 0:
                node.w = node.left.whites
                node.b = node.left.blacks
            elif node.left.colour == 1:
                node.b = node.left.blacks
                node.w = node.left.whites

            # print("w", node.w)
            # print("b", node.b)
            # print("ww", node.ww)
            # print("bb", node.bb)

        elif node.right and not node.left:  # ONLY RIGHT CHILD

            if node.colour == 0: #white
                node.whites += node.right.whites + 1
                node.blacks += node.right.blacks
            elif node.colour == 1: #black
                node.blacks += node.right.blacks + 1
                node.whites += node.right.whites
            # print("Whites", node.whites, "blacks", node.blacks)

            if node.right.colour == 0:
                node.bb = node.right.blacks
                node.ww = node.right.whites
            elif node.right.colour == 1:
                node.bb = node.right.blacks
                node.ww = node.right.whites

            # print("w", node.w)
            # print("b", node.b)
            # print("ww", node.ww)
            # print("bb", node.bb)

        elif node.right and node.left: # BOTH CHILDREN

            if node.colour == 0:
                node.whites += node.right.whites + node.left.whites + 1
                node.blacks += node.right.blacks + node.left.blacks
            elif node.colour == 1:
                node.blacks += node.left.blacks + node.right.blacks + 1
                node.whites += node.right.whites + node.left.whites
            # print("Whites", node.whites, "blacks", node.blacks)

            if node.left.colour == 0:
                node.w = node.left.whites
                node.b = node.left.blacks
            elif node.left.colour == 1:
                node.b = node.left.blacks
                node.w = node.left.whites

            if node.right.colour == 0:
                node.bb = node.right.blacks
                node.ww = node.right.whites
            elif node.right.colour == 1:
                node.bb = node.right.blacks
                node.ww = node.right.whites

            # print("w", node.w)
            # print("ww", node.ww)
            # print("b", node.b)
            # print("bb", node.bb)

        if node.b > 0 and node.bb > 0 and node.w > 0 and node.ww > 0:
            if node.w/node.b > node.ww/node.bb:
                # print("L-node----------->", node.key)
                count_l += 1
            elif node.w/node.b == node.ww/node.bb:
                # print("E-node----------->", node.key)
                count_e += 1
            elif node.w/node.b < node.ww/node.bb:
                # print("R-node----------->", node.key)
                count_r += 1


get_inputs_from_file("pubdata_ler/pub09.in")
postorder(node_list[0])
print(count_l, count_e, count_r)