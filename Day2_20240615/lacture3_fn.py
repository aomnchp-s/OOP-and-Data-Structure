#*arge, **kwarge parameter example
def fn(a, b, *arge, **kwarge):
    print(a)
    print(b)
    print(arge)
    print(kwarge)
#passing *arge, **kwarge argument 
fn(1,2,4,5,6,7,x=10,z=20)