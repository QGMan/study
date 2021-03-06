# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 方法一：将[]改成()
# L= [x * x for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# g = (x * x for x in range(10))
# print(g)
# print(next(g))
# print(next(g))
# for x in g:
#     print (x)

# 方法二：定义generator的另一种方法。如果一个函数定义中包含yield关键字，
# 那么这个函数就不再是一个普通函数，而是一个generator。

# 练习
# 使用生成器书写斐波那契数列
def fib(max):
    n=0
    a=0
    b=1
    while n<max:
        # 循环输出b
        yield(b)
        a,b=b,a+b
        # 相当于，这里不是很懂
        # t = (b, a + b)  # t是一个tuple
        # a = t[0]
        # b = t[1]
        n=n+1
    return 'done'
fib(6)
