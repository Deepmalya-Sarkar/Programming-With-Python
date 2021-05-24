#change the functionality of a function
# outer function(which needs to accept another function)

def functioning(funct1):
    def w():
        funct1()
    return w

@functioning
def iam():
    for i in range(5):
        print(i)


iam()