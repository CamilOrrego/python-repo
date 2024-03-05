def create_christmas_tree(tree_height):
    # Define the trunk size based on the tree height.
    if tree_height >= 5:
        trunk_size = 2
    else:
        trunk_size = 1
    # Define the amount of spaces and asterisks.
    for i in range(tree_height):
        # Define the amount of sapaces that is going to have the tree in each line
        for s in range(tree_height - i - 1):
            print(" ", end="")
        # Define the amount of asterisks that is going to have the tree in each line
        for a in range(2 * i + 1):
            print("*", end="")
        # print to continue in another line
        print()
    # Print tree trunk
    for i in range(trunk_size):
        print(" " * (tree_height - 1) + "*")


create_christmas_tree(6)
