# 生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？

# 方法一：循环
# L=[]
# for x in range(1,11):
#     L.append(x*x)
# print(L)
# 不推荐，太繁琐

# 方法二：列表生成式
L=[x*x for x in range(1,11) if x%2==0] 
print(L)
