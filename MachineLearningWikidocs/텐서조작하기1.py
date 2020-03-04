import numpy as np
import torch

t = np.array([0., 1., 2., 3., 4., 5., 6.])
print('-------------------------')
print('Rank of t: ',t.ndim)  # 몇차원인지 출력한다.
print('Shape of t: ',t.shape) # 크기를 출력한다.
print(t[4:-1]) # -1 은 끝번호

t2 = np.array([[1., 2., 3.], [2.,3.,4.],[5., 6., 7.], [8.,9.,10.]])
print('-------------------------')
print('Rank of t: ',t2.ndim)  # 몇차원인지 출력한다.
print('Shape of t: ',t2.shape) # 크기를 출력한다.

t3 = torch.FloatTensor([0., 1., 2., 3., 4., 5., 6.])
print('-------------------------')
print(t3.dim())
print(t3.shape)
print(t3.size())


t4 = torch.FloatTensor([[1., 2., 3.],
                       [4., 5., 6.],
                       [7., 8., 9.],
                       [10., 11., 12.]
                      ])
print('-------------------------')
print(t4[:, :-1])