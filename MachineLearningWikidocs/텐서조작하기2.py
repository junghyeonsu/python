import numpy as np
import torch

t = np.array([
    [[0,1,2],[3,4,5]],
    [[6,7,8],[7,8,9]]
    ])

ft = torch.FloatTensor(t)

print(ft.shape)
print(ft.dim())

# 전체 원소의 수는 유지한다!
print(ft.view([-1,3]).shape)
print(ft.view([-1,1,3]).shape)

print('-------------------------------')

ft2 = torch.FloatTensor([[0],[1],[2]])
print(ft2)
print(ft2.shape , ft2.dim())

# 크기가 1인 차원을 없앤다. 지금 [3,1]이니까 열을 없앤다. => (3) 으로 바뀜
print(ft2.squeeze())

print('--------------------------------')

ft3 = torch.FloatTensor([0,1,2])
print(ft3)
print(ft3.unsqueeze(1))
print(ft3.unsqueeze(-1))

print(ft3.view(1,-1))

print('----------------------------------')

x = torch.FloatTensor([[1,2],[2,3]])
y = torch.FloatTensor([[2,1],[3,2]])

# dim=0 행을 늘려라 , dim=1 열을 늘려라
print(torch.cat([x,y], dim=0))

print('----------------------------------')
x = torch.FloatTensor([1, 4])
y = torch.FloatTensor([2, 5])
z = torch.FloatTensor([3, 6])

print(torch.stack([x,y,z]))

print('----------------------------------')
x = torch.FloatTensor([[1],[2],[3]])
y = torch.FloatTensor([[2],[4],[6]])
print(x.mul(2))
print(x)
# _ 를 붙이면 덮어쓰기를 한다!
print(x.mul_(2))
print(x)