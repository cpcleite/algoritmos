from random import randrange, seed


def merge(a, b):
    # Merge
    pt_a = 0
    pt_b = 0
    len_a = len(a)
    len_b = len(b)
    ordem = []

    while (pt_a < len_a) or (pt_b < len_b):
        if (pt_a >= len_a) and (pt_b < len_b):
            ordem.extend(b[pt_b:])
            pt_b = len_b

        elif (pt_b >= len_b) and (pt_a < len_a):
            ordem.extend(a[pt_a:])
            pt_a = len_a

        else:
            if a[pt_a] <= b[pt_b]:
                ordem.append(a[pt_a])
                pt_a += 1

            else:
                ordem.append(b[pt_b])
                pt_b += 1

    return ordem


def merge_sort(dados):
    if (dados is None) or len(dados) <= 1:
        return dados
    else:
        metade = int(len(dados) / 2)
        a = merge_sort(dados[:metade])
        b = merge_sort(dados[metade:])
        return merge(a, b)


def merge_and_count(b, c, len_b, len_c):
    pt_b = 0
    pt_c = 0
    trocas = 0
    ordem = []

    while (pt_b < len_b) or (pt_c < len_c):
        if (pt_b >= len_b) and (pt_c < len_c):
            ordem.extend(c[pt_c:])
            pt_c = len_c

        elif (pt_c >= len_c) and (pt_b < len_b):
            ordem.extend(b[pt_b:])
            pt_b = len_b

        else:
            if b[pt_b] <= c[pt_c]:
                ordem.append(b[pt_b])
                pt_b += 1

            else:
                ordem.append(c[pt_c])
                pt_c += 1
                trocas += (len_b - pt_b)

    return ordem, trocas


def sort_and_count(dados, len):
    if (len <= 1):
        return dados, 0
    else:
        metade = int(len / 2)
        b, x = sort_and_count(dados[:metade], metade)
        c, y = sort_and_count(dados[metade:], len - metade)
        d, z = merge_and_count(b, c, metade, len - metade)
        return d, x + y + z


def mat_sub(a, b):
    l_a = len(a)
    c = []
    for i in range(l_a):
        aux = []
        for j in range(l_a):
            aux.append(a[i][j] - b[i][j])
        c.append(aux)
    return c


def mat_add(a, b):
    l_a = len(a)
    c = []
    for i in range(l_a):
        aux = []
        for j in range(l_a):
            aux.append(a[i][j] + b[i][j])
        c.append(aux)
    return c


def append_cols(a, b):
    c = []
    for i in range(len(a)):
        aux = []
        aux.extend(a[i])
        for j in range(len(b)):
            aux.append(b[i][j])
        c.append(aux)
    return c


def append_lines(a, b):
    c = a.copy()
    for i in range(len(b)):
        c.append(b[i])
    return c


def mat_mul(x, y):
    length = len(x)
    new_len = int(length / 2)
    if length == 1:
        return [[x[0][0] * y[0][0]]]
    else:
        a = [i[: new_len] for i in x[: new_len]]
        b = [i[new_len:] for i in x[: new_len]]
        c = [i[: new_len] for i in x[new_len:]]
        d = [i[new_len:] for i in x[new_len:]]
        e = [i[: new_len] for i in y[: new_len]]
        f = [i[new_len:] for i in y[: new_len]]
        g = [i[: new_len] for i in y[new_len:]]
        h = [i[new_len:] for i in y[new_len:]]

        p1 = mat_mul(a, mat_sub(f, h))
        p2 = mat_mul(mat_add(a, b), h)
        p3 = mat_mul(mat_add(c, d), e)
        p4 = mat_mul(d, mat_sub(g, e))
        p5 = mat_mul(mat_add(a, d), mat_add(e, h))
        p6 = mat_mul(mat_sub(b, d), mat_add(g, h))
        p7 = mat_mul(mat_sub(a, c), mat_add(e, f))

        rs11 = mat_add(mat_sub(mat_add(p5, p4), p2), p6)
        rs12 = mat_add(p1, p2)
        rs21 = mat_add(p3, p4)
        rs22 = mat_sub(mat_sub(mat_add(p1, p5), p3), p7)

        return append_lines(append_cols(rs11, rs12), append_cols(rs21, rs22))


def partition(a, pivot, start, end):
    if pivot > start:
        a[start], a[pivot] = a[pivot], a[start]

    pivot_value = a[start]
    leftmost_greater = start + 1

    for index in range(start + 1, end):
        if (a[index] < pivot_value):
            if index != leftmost_greater:
                a[index], a[leftmost_greater] = a[leftmost_greater], a[index]
            leftmost_greater += 1

    pivot = leftmost_greater - 1
    a[start], a[pivot] = a[pivot], a[start]

    return pivot


def quicksort(a, start=0, stop=None):

    if stop is None:
        length = len(a) - start
    else:
        length = stop

    if (length - start) <= 1:
        return a

    rnd = randrange(start, length)

    pivot = partition(a, rnd, start, length)

    quicksort(a, start, pivot)
    quicksort(a, pivot + 1, length)

    return a


def rselect(a, order, start=0, end=None):
    """Randomized Selection Algorithm

    Parameters
    ----------
    a : list
        List to be sorted
    length : int
        Length of a list
    order : int
        i th statistic wanted

    Returns
    -------
    a element
        a's element
    """
    if end is None:
        end = len(a)

    if (end - start) == 1:
        return a[start]

    rnd = randrange(start, end)

    pivot = partition(a, rnd, start, end)

    if (order-1) == pivot:
        return a[pivot]
    elif pivot >= order:
        return rselect(a, order,  start, pivot)
    else:
        return rselect(a, order, pivot+1, end)


if __name__ == '__main__':
    a = [3, 8, 2, 5, 1, 4, 7, 6]
    seed(123)
    print(rselect(a, 3))
    print(quicksort(a))
