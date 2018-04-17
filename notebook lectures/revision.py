def hello(name):
    return ("hello "+name)

def count_items_in_list(given_list, item):
    """
    find the number of times 'item' is in the blacket
    """
    #for i in given list:
    #   print(i)

    for i in range(0, len(given_list)):
        print(given_list[i])

def order_matters():
    """return True if value is even and > 10"
       return "hello" if value is odd and greater
       return False otherwise"""
    if value % 2 == 0 and value > 10:
        return True
    elif value % 2 == 1 and value < 10:
        return "hello"
    else: False

if __name__ == "__main__":
    print(hello("code1161"))
    print(count_items_in_list([2,10,21], 1)