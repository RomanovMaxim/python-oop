class Stepper:

    def __getitem__(self, i):
        return self.data[i]

if __name__ == '__main__':

    X = Stepper()
    X.data = "Python"

    print(X[1])

    for item in X:
        print(item, end=' ')
    print()

    print('t' in X)
