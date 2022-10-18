# Quick Start: ResNet

ResNet은 대표적인 image classification용 CNN 모델 중 하나입니다. 224×224 크기의 이미지를 입력 받아 풍선, 딸기, 고양이 등 사전에 정의된 여러 가지 사물 유형 중 하나로 분류합니다.

- [K. He et al., Deep Residual Learning for Image Recognition, arXiv:1512.03385](https://arxiv.org/abs/1512.03385)

Hyperscale AI Computing 서비스를 사용해 ResNet-50 모델을 학습시키고, 또 학습된 모델을 사용해 실제 이미지를 분류할 수 있습니다. 학습/추론을 위한 PyTorch 스크립트와, 실제 모델 학습을 시켜 보기 위한 샘플 데이터(ImageNet 데이터베이스의 일부)를 제공합니다. ImageNet 데이터베이스와 호환되는 포맷의 데이터가 있다면 이를 사용해 ResNet-50 모델을 학습시킬 수 있습니다.

## VM 생성

아래 버튼을 클릭하여 Hyperscale AI Computing VM을 생성하십시오.

("VM 생성하기" 버튼)

ResNet 학습을 위해서는 최소 다음 사양으로 VM을 생성하기를 권장합니다.

- OS: Ubuntu 18.04
- CPU: 8 vCore, 단 medium.128gb 이상의 AI 가속기를 사용할 경우 16 vCore
- 메인 메모리: 32 GB

VM 생성 시 Hyperscale AI Computing 서비스가 제공하는 여러 가지 AI 가속기 모델 중 한 가지를 선택해야 합니다. AI 가속기 모델에 따라 ResNet-50 모델의 학습 시간이 달라집니다. 다음 계산 성능 측정치를 참고하여 AI 가속기 모델을 선택하십시오. 특히 ResNet-50 학습 용도로는 large.256gb 이하의 모델을 선택하시기를 권장합니다. 모델 구조 상 크기가 큰 AI 가속기에서 추가적인 성능 향상을 얻지 못할 수 있습니다. 너무 부담 가지실 필요는 없습니다 — VM을 생성한 후에도 언제든지 필요하다면 AI 가속기 모델을 다른 것으로 변경할 수 있습니다.

|AI 가속기 모델|학습 처리 속도(초당 이미지 학습량)|샘플 데이터 1회 학습(1 epoch)시 소요 시간|
|------|---|---|
|Small.64GB|326장|6분 37초|
|Medium.128GB|646장|3분 24초|
|Large.256GB|1210장|1분 55초|

>위 성능은 테스트 환경에서 측정된 것으로 실 사용 환경에서는 차이가 생길 수 있습니다.

또한 VM의 reference model로는 Vision 카테고리의 ResNet 모델을 선택하십시오. 마지막으로 "생성하기" 버튼을 클릭하면 VM 생성이 완료됩니다.

## VM 접속하기

아래 버튼을 클릭하여 클라우드 콘솔에서 Hyperscale AI Computing 서버 정보를 확인할 수 있습니다.

("클라우드 콘솔 열기" 버튼)

서버 접속을 위해 우선 클라우드 콘솔에서 포트포워딩 설정 및 방화벽 설정을 진행합니다. 그 다음 macOS나 Linux의 경우 ssh 명령을 사용해서, Windows의 경우 PuTTY와 같은 SSH 클라이언트 프로그램을 사용해서 서버에 접속할 수 있습니다. VM 접속 방법은 Hyperscale AI Computing 사용자 매뉴얼을 참고하십시오.

("사용자 매뉴얼 열기" 버튼 — 클릭 시 "이용 방법" 페이지의 "VM 접속하기" 장으로 이동하면 됩니다.)

## 모델 코드 및 샘플 데이터 설치

VM에 접속하면 홈 디렉터리 밑에 install.sh 스크립트가 위치하고 있습니다. 이를 실행하여 ResNet-50 모델 코드 및 샘플 데이터를 설치하십시오. 설치에는 수 분 정도가 걸릴 수 있습니다. 설치 중에 VM 접속이 끊어지지 않도록 유의하십시오.

설치가 완료되면 홈 디렉터리 밑에 resnet, dataset/imagenet_100cls 디렉터리가 생성됩니다. resnet 디렉터리에는 ResNet-50 모델 학습/추론을 위한 PyTorch 스크립트가 들어 있습니다. dataset/imagenet_100cls 디렉터리에는 샘플 데이터로 사용 가능한 ImageNet 데이터베이스의 일부가 저장되어 있습니다.

설치가 정상적으로 이루어졌다면 홈 디렉터리 밑의 downloads 디렉터리는 지워도 무방합니다.

```
(pytorch) ubuntu@vm:~$ ls
install.sh  sample
(pytorch) ubuntu@vm:~$ ./install.sh

- Installing resnet reference code...
(중략)
Install complete!

- Reference code of resnet   : [ OK    ] (Saved at /home/ubuntu/resnet)
- Dataset imagenet_100cls    : [ OK    ] (Saved at /home/ubuntu/dataset/imagenet_100cls)
- Link dataset               : [ OK    ] (Linked dataset at /home/ubuntu/resnet/data)

(pytorch) ubuntu@vm:~$ ls
dataset  downloads  install.sh  sample  resnet
(pytorch) ubuntu@vm:~$ ls dataset
imagenet_100cls
(pytorch) ubuntu@vm:~$ ls resnet
data  dataset  inference.py  LICENSE.md  model  requirements.txt  train.py  utils.py
```

## Hyperscale AI Computing 시스템 환경 확인

VM에는 기본적으로 Python 3.8, PyTorch 1.7.1 및 Hyperscale AI Computing 지원을 위한 플러그인이 설치되어 있습니다. 다음과 같이 실행하여 PyTorch 버전 및 Hyperscale AI Computing 플러그인 버전 정보를 확인할 수 있습니다.

```
(pytorch) ubuntu@vm:~$ python
Python 3.8.12 (default, Oct 12 2021, 13:49:34)
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.__version__
'1.7.1'
>>> torch.version.moreh
'22.7.0'
>>> quit()
(pytorch) ubuntu@vm:~$
```

또한 터미널에서 moreh-smi 명령을 실행하여 VM에 연결된 AI 가속기 정보를 확인할 수 있습니다.

```
(pytorch) ubuntu@vm:~$ moreh-smi
+--------------------------------------------------------------------------------------------------------------+
|  Moreh-SMI 22.7.0                                              Client Version: 22.7.0 Server Version: 22.7.0 |
+--------------------------------------------------------------------------------------------------------------+
|  Device  |        Name         |            Token           |     Model    |  Memory Usage  |  Total Memory  |
+==============================================================================================================+
|       1  |  KT AI Accelerator  |  ZXhhbXBsZSB0b2tlbiBzdHI=  |  small.64gb  |  -             |  -             |
+--------------------------------------------------------------------------------------------------------------+

Processes:
+----------------------------------------------------------+
|  Device  |  Job ID  |  PID  |  Process  |  Memory Usage  |
+==========================================================+
+----------------------------------------------------------+
```

## ResNet 학습 시작하기

홈 디렉터리 아래의 resnet 디렉터리로 이동한 다음 train.py 스크립트를 실행하여 ResNet-50 모델 학습을 시작할 수 있습니다.

```
(pytorch) ubuntu@vm:~$ cd ~/resnet
(pytorch) ubuntu@vm:~/resnet$ python train.py --save-model model.pt -b 256
| INFO     | __main__:parse_args:140 - PARAMETER | mode : train
| INFO     | __main__:parse_args:140 - PARAMETER | load_checkpoint :
| INFO     | __main__:parse_args:140 - PARAMETER | checkpoint_path : ./checkpoint
| INFO     | __main__:parse_args:140 - PARAMETER | checkpoint_epoch_interval : 0
| INFO     | __main__:parse_args:140 - PARAMETER | init_model :
...
[info] Requesting resources for KT AI Accelerator from the server...
[info] Initializing the worker daemon for KT AI Accelerator...
[info] [1/1] Connecting to resources on the server (192.168.00.00:00000)...
[info] Establishing links to the resources...
[info] KT AI Accelerator is ready to use.
| INFO     | __main__:train:305 - Epoch 1/42 start
..
```

--save-model 옵션은 학습이 완료된 모델을 어느 파일에 저장할지를 지정합니다. 위 예시의 경우 학습이 완료된 모델을 model.pt 파일에 저장합니다.

b 옵션은 mini-batch size, 즉 학습 이미지 몇 장을 한 번에 AI 가속기에서 학습시킬 것인지를 지정합니다. AI 가속기 사양이 높아질수록 거기에 맞춰 mini-batch size를 키워 주어야 최적의 성능을 얻을 수 있습니다. 또한 medium.128gb 이상의 모델을 사용할 경우 --num-workers 8 옵션을 추가하여 학습 데이터를 더 많은 CPU 코어에서 불러오도록 해야 충분한 성능을 얻을 수 있습니다. Hyperscale AI Computing의 AI 가속기 모델별로 권장하는 실행 옵션은 다음과 같습니다.

- small.64gb: -b 256
- medium.128gb: -b 512 --num-workers 8
- large.256gb: -b 1024 --num-workers 8

현재 사용 중인 AI 가속기 모델이 무엇인지는 moreh-smi 명령으로 확인할 수 있습니다.

train.py 스크립트는 기본적으로 샘플 데이터를 42회 반복 학습(42 epoch)시킵니다. 데이터 학습 횟수를 수정하기 위해서는 스크립트 실행 시 -e 옵션을 주면 됩니다.

```
(pytorch) ubuntu@vm:~/resnet$ python train.py --save-model model.pt -b 256 -e 100
...
[info] Requesting resources for KT AI Accelerator from the server...
[info] Initializing the worker daemon for KT AI Accelerator...
[info] [1/1] Connecting to resources on the server (192.168.00.00:00000)...
[info] Establishing links to the resources...
[info] KT AI Accelerator is ready to use.
| INFO     | __main__:train:305 - Epoch 1/100 start
...
```

## 학습 중간에 체크포인트 저장하기

장시간 모델을 학습할 경우 주기적으로 현재까지의 학습 상태를 체크포인트로 저장해 두는 것이 안전합니다. 체크포인트를 저장하면 나중에 특정 시점에서부터 다시 학습을 이어서 시작할 수 있습니다.

우선 train.py 스크립트를 실행할 때 `--checkpoint-epoch-interval` 옵션을 사용하여 몇 epoch마다 체크포인트를 저장할지 지정할 수 있습니다. 아래는 2 epoch마다 체크포인트를 저장하는 예시입니다. 모델을 학습하는 동안 checkpoint 디렉터리 안에 epoch별 체크포인트 저장됩니다.

```
(pytorch) ubuntu@vm:~/resnet$ python train.py --save-model model.pt -b 256 --checkpoint-epoch-interval 2
...
(pytorch) ubuntu@vm:~/resnet$ ls checkpoint
10  12  14  16  18  2  20  22  24  26  28  30  32  34  36  38  4  40  42  6  8
```

>⚠️ 주의: 체크포인트를 주기적으로 저장함에 따라 checkpoint 디렉터리에 저장되는 데이터 용량이 매우 커질 수 있습니다. VM에 충분한 저장 용량이 확보되어 있는지 미리 확인하십시오. 터미널에서 df -h 명령을 실행하면 저장 용량이 몇 %나 남았는지 확인할 수 있습니다.

그리고 `--load-checkpoint` 옵션을 사용하여 어느 체크포인트에서 학습을 재개할지 지정할 수 있습니다. 아래는 24번째 epoch 완료 후에 기록된 체크포인트부터 학습을 재개하는 예시입니다.

```
(pytorch) ubuntu@vm:~/resnet$ python train.py --save-model model.pt -b 256 --load-checkpoint ./checkpoint/24
```

## 학습 옵션

모델 학습 결과에 하이퍼파라미터 값이 큰 영향을 미친다는 것은 익히 알려진 사실입니다. train.py 스크립트는 learning rate, momentum 등 여러 가지 하이퍼파라미터 값을 옵션으로 수정할 수 있는 기능을 제공합니다. 구체적으로 어떤 옵션을 제공하는지는 터미널에서 python train.py --help를 실행하여 확인할 수 있습니다.

## 학습된 모델로 추론하기

홈 디렉터리 아래의 resnet 디렉터리로 이동한 다음 inference.py 스크립트를 실행하여, 기존에 학습시킨 ResNet-50 모델로 입력 데이터에 대한 추론을 할 수 있습니다. 즉, 각각의 입력 이미지가 사전에 정의된 사물 유형 중 어디에 속하는지를 판단할 수 있습니다.

--model 옵션에는 train.py 스크립트로 학습하여 저장한 모델 파일을, --dataset 옵션에는 추론할 이미지들이 저장된 디렉터리를 지정합니다. --output 옵션에는 추론 결과를 어느 파일에 저장할지를 지정합니다. 추론 결과는 CSV 파일로 저장되며 텍스트 편집기나 Excel 등을 사용해 열어 볼 수 있습니다.

```
(pytorch) ubuntu@vm:~$ cd ~/resnet
(pytorch) ubuntu@vm:~/resnet$ python inference.py --model model.pt --dataset ./data/val/n01518878 --output output.csv -b 256
| INFO     | __main__:parse_args:48 - PARAMETER | model : model.pt
| INFO     | __main__:parse_args:48 - PARAMETER | dataset : ./data/val/n01518878
| INFO     | __main__:parse_args:48 - PARAMETER | output : output.csv
| INFO     | __main__:parse_args:48 - PARAMETER | batch_size : 256
| INFO     | __main__:parse_args:48 - PARAMETER | log_interval : 1
| INFO     | __main__:parse_args:48 - PARAMETER | num_classes : 100
| INFO     | __main__:parse_args:49 -
| INFO     | __main__:parse_args:50 -
[info] Requesting resources for KT AI Accelerator from the server...
[info] Initializing the worker daemon for KT AI Accelerator...
[info] [1/1] Connecting to resources on the server (192.168.00.00:00000)...
[info] Establishing links to the resources...
[info] KT AI Accelerator is ready to use.
| INFO     | utils:load_model:120 - Load model's params from model.pt
| INFO     | utils:load_model:122 - Load complete!
| INFO     | __main__:inference:77 - Inference start
...
```

추론 시에도 마찬가지로 -b 옵션으로 이미지 몇 장을 한 번에 추론할 것인지를 결정합니다. AI 가속기 사양이 높아질수록 거기에 맞춰 mini-batch size를 키워 주어야 최적의 성능을 얻을 수 있습니다. Hyperscale AI Computing의 AI 가속기 모델별로 권장하는 mini-batch size는 다음과 같습니다.

- small.64gb: -b 256
- medium.128gb: -b 512 --num-workers 8
- medium.256gb: -b 1024 --num-workers 8

## AI 가속기 모델 변경하기

Hyperscale AI Computing 사용 중에 필요하다면 언제든지 AI 가속기의 모델을 변경할 수 있습니다. 예를 들어 모델 학습이 예상보다 오래 걸릴 경우, 프로그램을 중단한 후 AI 가속기를 더 큰 것으로 교체하고 마지막 체크포인트부터 다시 실행을 재개할 수 있습니다. 혹은 추론할 이미지의 개수가 많지 않을 경우 AI 가속기를 작은 모델로 교체하여 자원을 효율적으로 사용할 수 있습니다.

AI 가속기 모델 변경을 위해서는 터미널에서 moreh-switch-model 명령을 실행한 다음 변경할 모델 순번(1~8)을 입력하고, q를 입력하여 프로그램을 종료합니다.

```
(pytorch) ubuntu@vm:~$ moreh-switch-model
Current KT AI Accelerator: Medium.128GB

1. Small.64GB
2. Medium.128GB*
3. Large.256GB
4. xLarge.512GB
5. 2xLarge.1024GB
6. 3xLarge.1536GB
7. 4xLarge.2048GB
8. 6xLarge.3072GB
9. 8xLarge.4096GB
10. 12xLarge.6144GB
11. 24xLarge.12288GB
12. 48xLarge.24576GB

Selection (1-12, q, Q): 5
The KT AI Accelerator model is successfully switched to  "2xLarge.1024GB".

1. Small.64GB
2. Medium.128GB
3. Large.256GB
4. xLarge.512GB
5. 2xLarge.1024GB*
6. 3xLarge.1536GB
7. 4xLarge.2048GB
8. 6xLarge.3072GB
9. 8xLarge.4096GB
10. 12xLarge.6144GB
11. 24xLarge.12288GB
12. 48xLarge.24576GB

Selection (1-12, q, Q): q
(pytorch) ubuntu@vm:~$
```

> ⚠️ AI 가속기에서 프로그램이 실행 중인 동안에는 가속기 모델을 변경할 수 없습니다.


## 샘플 데이터가 아닌 다른 데이터로 학습하기

ImageNet 데이터베이스와 호환되는 포맷의 데이터가 있다면 이를 사용해 ResNet-50 모델을 학습시킬 수 있습니다. 우선 your_training_data 디렉터리에 다음과 같이 이미지를 저장하십시오.

- your_training_data/train/(사물 유형 이름) 디렉터리 안에 해당 사물 유형에 대한 training set 이미지를 모두 저장합니다.
- your_training_data/val/(사물 유형 이름) 디렉터리 안에 해당 사물 유형에 대한 validation set 이미지를 모두 저장합니다.

사물 유형 이름은 임의로 설정할 수 있습니다. 모델 학습 시에는 알파벳 순서로 0번부터 유형 번호가 부여됩니다. ResNet-50 모델은 입력 이미지의 유형 번호를 알아내도록 학습이 됩니다. 또한 사물 유형의 가짓수도 꼭 샘플 데이터처럼 100가지일 필요가 없습니다.

그 다음 ResNet-50 모델 학습을 위해 train.py 스크립트를 실행할 때 --dataset 옵션으로 your_training_data 디렉터리의 위치를 지정하십시오.

```
(pytorch) ubuntu@vm:~/resnet$ python train.py --save-model model.pt -b 256 --dataset ~/your_training_data
...
| INFO     | __main__:parse_args:140 - PARAMETER | dataset : ~/your_training_data
...
[info] Requesting resources for KT AI Accelerator from the server...
[info] Initializing the worker daemon for KT AI Accelerator...
[info] [1/1] Connecting to resources on the server (192.168.00.00:00000)...
[info] Establishing links to the resources...
[info] KT AI Accelerator is ready to use.
| INFO     | __main__:train:305 - Epoch 1/42 start
...
```

또한 학습된 ResNet-50 모델로 입력 데이터에 대한 추론을 할 때, 해당 모델이 몇 가지 사물 유형을 분류하도록 학습되었는지를 --num-classes 옵션으로 지정해야 합니다.

```
(pytorch) ubuntu@vm:~/resnet$ python inference.py --model model.pt --dataset ~/your_inference_data --output output.csv -b 256 --num-classes 300
...
| INFO     | __main__:parse_args:48 - PARAMETER | num_classes : 300
| INFO     | __main__:parse_args:49 -
| INFO     | __main__:parse_args:50 -
[info] Requesting resources for KT AI Accelerator from the server...
[info] Initializing the worker daemon for KT AI Accelerator...
[info] [1/1] Connecting to resources on the server (192.168.00.00:00000)...
[info] Establishing links to the resources...
[info] KT AI Accelerator is ready to use.
| INFO     | utils:load_model:120 - Load model's params from model.pt
| INFO     | utils:load_model:122 - Load complete!
| INFO     | __main__:inference:77 - Inference start
...
```

## 사용 시 주의사항

- AI 가속기에서는 동시에 두 개 이상의 프로그램을 실행할 수 없습니다. 예를 들어 학습 작업이 실행 중인 동안 다른 학습/추론 작업을 실행할 수 없습니다. 이 경우 나중에 실행한 프로그램은 아래와 같은 메시지를 출력하고 앞에 실행한 프로그램이 끝날 때까지 대기하게 됩니다. 만약 AI 가속기를 사용하는 다른 프로그램이 없는데도 아래와 같은 메시지가 출력될 경우, 사용자 매뉴얼의 '자주 묻는 질문'을 참고하십시오.

```
(pytorch) ubuntu@vm:~/resnet$ python train.py
...
[info] Requesting resources for KT AI Accelerator from the server...
[warning] KT AI Accelerator is already in use by another process:
[warning]   (pid: 10000) python train.py
[warning] Two or more processes cannot use KT AI Accelerator at the same time. The program will resume automatically after the process 10000 terminates...
```

- 모델 학습/추론 과정에서 데이터를 빠르게 불러 오기 위해 별도의 DataLoader 프로세스가 실행됩니다. train.py 혹은 inference.py 스크립트가 비정상 종료했을 때(예를 들어 Ctrl+C로 강제 종료했을 때) 주 프로세스는 없어지더라도 DataLoader 프로세스는 없어지지 않고 남아 있는 경우가 있습니다. 이 경우 AI 가속기에서 새로운 프로그램을 실행할 수 없을 뿐더러 VM의 CPU 코어와 메인 메모리를 지속적으로 점유하기 때문에 다른 프로그램 실행 시 문제가 될 수 있습니다. 현재 VM에 실행 중인 Python 프로세스가 존재하는지 ps aux | grep python 명령으로 확인할 수 있습니다. 또한 실행 중인 모든 Python 프로세스를 pkill python 명령으로 제거할 수 있습니다.

```
(pytorch) ubuntu@vm:~$ ps aux | grep python
root      1700  0.0  0.0 169104 17136 ?        Ssl  Dec03   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root      1900  0.0  0.0 185956 20112 ?        Ssl  Dec03   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
ubuntu    9900 84.1  0.1 3688828 508348 pts/1  Sl   08:50   0:18 python train.py
ubuntu    9901 79.5  0.1 3671492 491104 pts/1  Sl   08:50   0:17 python train.py
ubuntu    9902 65.4  0.1 3670744 490580 pts/1  Sl   08:50   0:14 python train.py
ubuntu    9903 67.5  0.1 3671280 490440 pts/1  Sl   08:50   0:14 python train.py
ubuntu   10000  0.0  0.0  14864  1116 pts/2    S+   08:51   0:00 grep --color=auto python
(pytorch) ubuntu@vm:~$ pkill python
(pytorch) ubuntu@vm:~$ ps aux | grep python
root      1700  0.0  0.0 169104 17136 ?        Ssl  Dec03   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root      1900  0.0  0.0 185956 20112 ?        Ssl  Dec03   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
ubuntu   10001  0.0  0.0  14864  1116 pts/2    S+   08:51   0:00 grep --color=auto python
```

- Hyperscale AI Computing 서비스는 지속적으로 소프트웨어 업데이트가 이루어지고 있습니다. 터미널에서 update-moreh 명령을 실행하여 소프트웨어가 최신 버전이 아닌 경우 자동으로 업데이트할 수 있습니다. 구 버전의 소프트웨어를 사용할 경우 train.py 혹은 inference.py 프로그램 실행 시에 경고 메시지가 출력되거나 아예 AI 가속기 할당이 불가능할 수 있습니다.

```
(pytorch) ubuntu@vm:~$ update-moreh
Currently installed: 0.8.0
Possible upgrading version: 0.8.1

Do you want to upgrade? (y/n, default:n)
y
...
Finished processing dependencies for moreh-driver==0.8.1

installed : /usr/bin/moreh-smi
installed : /usr/bin/moreh-switch-model
installed : /usr/bin/update-moreh
installed : /usr/lib/libcommunication.so
installed : /usr/lib/libmodnnruntime.so
```

- 기타 사용 시 유의사항은 Hyperscale AI Computing 사용자 매뉴얼을 참고하십시오.