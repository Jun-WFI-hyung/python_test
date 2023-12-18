import torch
import torch.nn as nn

# 입력 특성의 개수
input_features = 5

# 출력 특성의 개수
output_features = 10


# Linear 모듈 정의
linear_layer = nn.Linear(input_features, output_features)

# 가중치 행렬
weights = linear_layer.weight

# 편향 벡터
bias = linear_layer.bias

print("가중치 행렬의 크기:", weights.size())  # (output_features, input_features)
print("편향 벡터의 크기:", bias.size())       # (output_features,)


x = torch.Tensor([[1,2,3,4,5]])
w = torch.randn((5,10))
print(w.size())
y1 = linear_layer(x)
y2 = torch.matmul(x, w)
print(y1.size())
print(y2.size())