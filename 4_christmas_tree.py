
def christmas_tree(n):
    if n == 1:
        return "#\n#"
    


def unit_test():
    assert christmas_tree(1) == "#\n#"
    assert christmas_tree(2) == " #\n" + \
                                "###\n" + \
                                " #"
    print("All unit tests passed")


unit_test()
