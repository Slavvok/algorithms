def tree(n: int):
    if n < 1:
        return None

    width = 2 * n - 1

    for i in range(1, n + 1):
        curr_width = 2 * i - 1
        spaces = (width - curr_width) // 2
        print(spaces * " " + curr_width * "*")


import random


def gen(n):
    ids = [i for i in range(n)]
    random.shuffle(ids)

    for i in ids:
        d = {
            'id': ids[0],
            'data': 'adsfdfasdfasdf'
        }

        ids = ids[1:]
        yield d



if __name__ == '__main__':
    for ob in gen(100):
        print(ob)
