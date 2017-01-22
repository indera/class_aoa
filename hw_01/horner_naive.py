"""
Goal: implement and test the polynomial evaluation

@see CLRS v3 book page 41
@date: 2017-01-22
@author: Andrei Sura
"""

def horner(a, x):
    """
    T(n) = Theta(n^2) since we have to traverse a nested loop for each term

    :param a: list of "n" coefficients
    :x float: the value for which to compute the polynomial value
    """

    y = 0

    for i in range(len(a)):
        temp = 1

        print("temp= 1")

        for j in range(i):
            temp = temp * x
            print("temp= {}^{} = {}".format(x, i, temp))

        print("(i= {}, a[{}] = {}, y = y + a[i] * temp = {} + {}*{}" .format(i, i, a[i], y, a[i], temp))  # noqa
        y = y + a[i] * temp

    return y


data = [1, 2, 3]
x = 2

print("Evaluating P({}) for coefficients: {}".format(x, data))
print("y = 0")
print("Final: P({}) = {}".format(x, horner(data, x)))

"""
Evaluating P(2) for coefficients: [1, 2, 3]
y = 0
temp= 1
(i= 0, a[0] = 1, y = y + a[i] * temp = 0 + 1*1
temp= 1
temp= 2^1 = 2
(i= 1, a[1] = 2, y = y + a[i] * temp = 1 + 2*2
temp= 1
temp= 2^2 = 2
temp= 2^2 = 4
(i= 2, a[2] = 3, y = y + a[i] * temp = 5 + 3*4
Final: P(2) = 17

"""
