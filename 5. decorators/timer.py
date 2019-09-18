import time

class timer:

    def __init__(self, func):
        self.func = func
        self.alltime = 0

    def __call__(self, *args, **kargs):
        start = time.perf_counter()
        result = self.func(*args, **kargs)
        elapsed = time.perf_counter() - start
        self.alltime += elapsed
        print(f'{self.func.__name__}: {elapsed:.6f}, {self.alltime:.6f}')
        return result

@timer
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer
def mapcall(N):
    return map((lambda x: x * 2), range(N))


result = listcomp(5)
listcomp(500000)
listcomp(5000000)
listcomp(10000000)
print(result)
print(f'allTime = {listcomp.alltime}')

print(' ')
result = mapcall(5)
mapcall(500000)
mapcall(5000000)
mapcall(10000000)
print(list(result))
print(f'allTime = {mapcall.alltime}')

print(f'map/comp = {round(mapcall.alltime / listcomp.alltime, 6)}')
