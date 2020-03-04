import torch
import torch.nn.functional as F

torch.manual_seed(1)

z = torch.FloatTensor([1,2,3])
# 가설
hypothesis = F.softmax(z, dim=0)
print(hypothesis)
print(hypothesis.sum())



x = torch.rand(3,5, requires_grad=True)
# dim = 0 행끼리 계산 dim = 1 열끼리 계산
hypothesis = F.softmax(x, dim=1)
print(hypothesis)

y = torch.randint(5,(3,)).long()
print(y)

y_one_hot = torch.zeros_like(hypothesis)
y_one_hot.scatter_(1, y.unsqueeze(1),1)

print(y_one_hot)

cost = (y_one_hot * -torch.log(hypothesis)).sum(dim=1).mean()
print(cost)


# 첫번째
(y_one_hot * -torch.log(hypothesis)).sum(dim=1).mean()
# 두번째 torch.log + F.softmax 를 합침
(y_one_hot * - F.log_softmax(x, dim=1)).sum(dim=1).mean()
# 세번째  F.nll_loss() 를 넣을때는 one_hot 벡터를 넣을 필요없이 실제값을 바로 인자로 사용
F.nll_loss(F.log_softmax(x, dim=1), y)
# 네번째 cross_entropy 함수는 비용함수 + 소프트맥스 함수까지 포함하고있다.
F.cross_entropy(x,y)