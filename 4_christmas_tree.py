
def christmas_tree(n):
    tree = ""
    for i in range(n):
        tree = tree + " "*(n-i-1) + "#"*(2*i+1) + "\n" 
    tree = tree + " "*(n-1) + "#" 
    return tree
    


def unit_test():
    assert christmas_tree(1) == "#\n#"
    assert christmas_tree(2) == " #\n" + \
                                "###\n" + \
                                " #"
    assert christmas_tree(3) == "  #\n" + \
                                " ###\n" + \
                                "#####\n" + \
                                "  #"
    assert christmas_tree(4) == "   #\n" + \
                                "  ###\n" + \
                                " #####\n" + \
                                "#######\n" + \
                                "   #"
    print("All unit tests passed")


unit_test()
