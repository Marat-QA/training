
def percents(x, y):
    """Comment"""
    one_percent = x / 100
    result = y / one_percent
    return result

def print_percents(x,y):
    """Coment"""
    print(str(y) + " is " + str(percents(x, y)) + " % of " + str(x))


percents(200,50)