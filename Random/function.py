random = [4, 5, 8, 3, 9]
checker = [3]
def value_checker(value, find):
    for find in value:
        if find >= value:
            print("nice") 
        else:
            print("dam dats tuff")

value_checker(random, checker)