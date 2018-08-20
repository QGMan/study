# 要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，
# 并在适当的条件结束for循环。对于函数改成的generator来说，
# 遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束

# 练习
# 杨辉三角定义如下：
# 写一个generator，不断输出下一行的list
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1


def triangles():
    L = [1]
    yield L
    while True:
        L = [1]+[L[x]+L[x+1] for x in range(len(L)-1)]+[1]
        yield L

def yhui():
    n = 0
    for L in triangles():
        print(L)
        n = n+1
        if n == 10:
            break
yhui()