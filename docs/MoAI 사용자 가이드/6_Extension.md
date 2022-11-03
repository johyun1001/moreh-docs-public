# MoAI Pytorch extension

이 문서는 Moreh AI Framework에서 어떻게 NVIDIA APEX(A PyTorch EXtention)와 같은 기능을 사용하는지 대한 설명이 담겨있는 페이지입니다.

## NVIDIA APEX란?

NVIDIA APEX는 모델 학습 시 사용되는 Mixed Precision 기능 및 다양한 기능들을 Pytorch에서 간편하게 사용할 수 있도록 만들어진 확장 라이브러리입니다.

- https://github.com/NVIDIA/apex

## Moreh APEX 소개

Moreh 솔루션에서도 APEX 기능을 사용하실 수 있으며, 다음과 같이 NVIDIA APEX 코드를 대체할 수 있습니다. 더 좋은 점은 **Moreh 솔루션에서는 NVIDIA APEX 라이브러리를 설치하실 필요 없다는 것입니다**. 아래는 일반적인 NVIDIA APEX 코드 사용법과 이를 어떻게 Moreh APEX로 교체하는지 방법을 서술합니다.

## Distributed Data Parallel (DDP)

DDP는 NVIDIA APEX에서 제공하는 대표 기능 중 하나이며, 기존 Pytorch에서도 DDP기능을 제공하지만 사용방법이 다소 까다로워 NVIDIA에서 손쉽게 DDP기능을 Pytorch에서 사용할 수 있게끔 만든 기능입니다. 현재도 많은 딥러닝 연구자들이 사용하고 있습니다.

NIVIDA APEX에서 DDP를 적용하는 방법은 다음과 같습니다.

```bash
# FOR DISTRIBUTED: (can also use torch.nn.parallel.DistributedDataParallel instead)
from apex.parallel import DistributedDataParallel

parser = argparse.ArgumentParser()
# FOR DISTRIBUTED:  Parse for the local_rank argument, which will be supplied
# automatically by torch.distributed.launch.
parser.add_argument("--local_rank", default=0, type=int)
args = parser.parse_args()
```

하지만, Moreh 솔루션에서는 해당 기능을 사용하지않고 기본적으로 모든 데이터 처리를 DDP를 통합니다. 따라서, Moreh 솔루션에서는 DDP를 활용하는 코드를 없애도 무방합니다.

## Mixed Precision

NVIDIA APEX에서 일반적인 Mixed Precision 사용방법은 다음과 같습니다.

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