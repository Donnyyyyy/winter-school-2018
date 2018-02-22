class F:
    def __init__(self, func):
        self.__func = func
        self.__computed = {}

    def __call__(self, x):
        if x in self.__computed:
            return self.__computed[x]
        else:
            try:
                val = self.__func(x)
            except ZeroDivisionError:
                return None
            self.__computed[x] = val
            return val

def read_f():
    str_f = 'lambda x: ' + input()
    func = eval(str_f)
    return F(func)