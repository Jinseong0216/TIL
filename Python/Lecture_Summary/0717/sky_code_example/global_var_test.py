a = 100

def test_func(p1):
    global a
    print(a)
    #b = a + p1
    #print(b)
    
    a = a + p1
    #print(a)
    
test_func(200)