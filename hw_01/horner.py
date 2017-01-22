"""
Goal: implement and test the polynomial evaluation

@see CLRS v3 book page 41
@date: 2017-01-22
@author: Andrei Sura
"""

def horner(a, x):
    """
    T(n) = Theta(n)

    :param a: list of "n" coefficients
    :x float: the value for which to compute the polynomial value
    """

    y = 0

    # for i in range(len(a)): (incorrect)
    for i in range(len(a)-1, -1, -1):
        print("(i= {}, a[{}] = {}, y = a[i] + x*y = {} + {}*{}"
              .format(i, i, a[i], a[i], x, y))  # noqa
        y = a[i] + x * y

    return y


data = [1, 2, 3]
x = 2

print("Evaluating P({}) for coefficients: {}".format(x, data))
print("y = 0")
print("Final: P({}) = {}".format(x, horner(data, x)))

"""
Evaluating P(2) for coefficients: [1, 2, 3]

y = 0
(i= 2, a[2] = 3, y = a[i] + x*y = 3 + 2*0
(i= 1, a[1] = 2, y = a[i] + x*y = 2 + 2*3
(i= 0, a[0] = 1, y = a[i] + x*y = 1 + 2*8
Final: P(2) = 17
"""
