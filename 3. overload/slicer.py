class Slicer:

    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value


if __name__ == '__main__':

    X = Slicer()
    print(X[0])
    print(X[1])
    print(X[-1])

    print(X[2:4])
    print(X[::-1])

    X[1] = 100
    print(X[1])

    print(*X)
