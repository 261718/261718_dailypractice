def outer():
    x = "local"
    
    def inner():
       
        nonlocal x
        x=7
        print("inner:", x)
    
    inner()
    print("outer:", x)

outer()


def fun():
    ss = 10
    return ss
fun()