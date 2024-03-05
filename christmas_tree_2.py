def christmas_tree(tree_height):

    if tree_height >= 5:
        trunk_size = 2
    else:
        trunk_size = 1

    for i in range(tree_height):
        for s in range(tree_height - i - 1):
            print(" ", end="")

        for a in range(2 * i + 1):
            print("*", end="")
        print()

    for i in range(trunk_size):
        print(" " * (tree_height - 1) + "*")


christmas_tree(3)
