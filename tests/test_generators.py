

def yield_list(lst: list[str]):
    for string in lst:
        number: str = yield
        yield string.upper() + number


def test_generators():
    lst = ['one', 'two', 'three']
    print(list(yield_list(lst)))
    generator = yield_list(lst)
    print(generator)

    for elem in yield_list(lst):
        print(elem)
    print('=============================')
    generator2 = yield_list(lst)

    generator2.send(' 1')
    print(next(generator2))
    generator2.send(' 2')
    print(next(generator2))
    generator2.send(' 3')
    print(next(generator2))

