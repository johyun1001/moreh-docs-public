# Moreh Apex

해당 페이지는 NVIDIA APEX(A PyTorch EXtention)을 사용할경우 어떻게 Moreh AI Framework에서 돌리는지에 대한 설명이 담겨져있는 페이지입니다.

# NVIDIA APEX란?

NVIDIA APEX는 모델 학습시 사용되는 Mixed Precision 기능과 Distributed Data Parallel(이하 DDP) 기능을 Pytorch에서 간편하게 사용할수있도록 만들어진 확장 라이브러리입니다.

- https://github.com/NVIDIA/apex

# Moreh APEX

Moreh 솔루션에서도 APEX기능을 사용하실수 있으며, 다음과 같이 NVIDIA APEX 코드를 대체하실수있습니다. 더 좋은점은 **Moreh 솔루션에서는 NVIDIA APEX 라이브러리를 설치하실 필요가 없습니다**. 아래는 일반적인 NVIDIA APEX 코드 사용법과 이를 어떻게 Moreh APEX로 교체하는지 방법을 서술합니다.

## Distributed Data  Parallel (DDP)

DDP는 NVIDIA APEX에서 제공하는 대표 기능중 하나이며, 기존 Pytorch에서도 DDP기능을 제공하지만 사용방법이 다소 까다로워 NVIDIA에서 손쉽게 DDP기능을 Pytorch에서 사용 할 수 있게끔 만든 기능입니다. 현재도 많은 딥러닝 연구자들이 사용하고 있습니다.

하지만, Moreh 솔루션에서는 해당 기능을 사용하지않고 기본적으로 모든 데이터 처리를 DDP를 통합니다. 따라서, Moreh 솔루션에서는 DDP를 활용하는 코드를 없애도 무방합니다.

## Mixed Precision

NVIDIA APEX에서 일반적인 Mixed Precision사용방법은 다음과 같습니다.

```bash
from apex import amp

# Declare model and optimizer as usual, with default (FP32) precision
model = torch.nn.Linear(D_in, D_out).cuda()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

# Allow Amp to perform casts as required by the opt_level
model, optimizer = amp.initialize(model, optimizer, opt_level="O1")
...
# loss.backward() becomes:
with amp.scale_loss(loss, optimizer) as scaled_loss:
    scaled_loss.backward()
...
```

Moreh 솔루션에서의 Mixed Precision 사용방법은 다음과 같습니다. 위에서 설명드린것처럼, Moreh 솔루션은 별도의 NVIDIA APEX 라이브러리 설치가 필요없습니다. 따라서, Pytorch 라이브러리를 바로 사용합니다.

```bash
import torch

# Declare model and optimizer as usual, with default (FP32) precision
model = torch.nn.Linear(D_in, D_out).cuda()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)
# 
amp = torch.moreh.apex.amp

# Allow Amp to perform casts as required by the opt_level
model, optimizer = amp.initialize(model, optimizer, opt_level="O1")
...
# loss.backward() becomes:
with amp.scale_loss(loss, optimizer) as scaled_loss:
    scaled_loss.backward()
...
```