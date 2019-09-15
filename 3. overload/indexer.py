class Indexer:

    def __getitem__(self, index):
        return index ** 2

if __name__ == '__main__':

    X = Indexer()
    print(X[5])

    for k in range(5):
        print(f'{X[k]}', end=' ')

    print(f'\n{Indexer()[11]}')
