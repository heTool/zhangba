def fib(max):
    n,a,b=0,0,1
    while n<max:
        
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'


    def count():
        fs=[]
        for i in range(1,4):
            def f():
                return i*i
            fs.append(f)
        return fs
    f1,f2,f3 = count()