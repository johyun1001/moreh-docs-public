# Get Started with Moreh

## 1. Conda 환경 세팅 및 Moreh 설치

VM에서 conda 환경에 문제가 생길경우, conda 가상환경을 다시 세팅하는 방법입니다. `pytorch` 라는 conda 가상환경 명으로 세팅한다고 가정하겠습니다.

1. 가상환경 삭제 (이미 삭제했다면 Skip 하셔도 됩니다)

```bash
# 현재 pytorch 가상환경 내에서

conda deactivate
conda env remove -n pytorch
```

2. 가상환경 재생성

```bash
conda create -y -n pytorch python=3.8
conda activate pytorch
```

3. pytorch 패키지 설치

```bash
conda install -y torchvision torchaudio numpy protobuf==3.13.0 pytorch==1.7.1 cpuonly -c pytorch
```

4. moreh 솔루션 업데이트

```bash
update-moreh --force --target 22.8.0
```

5. 정상 설치 확인

```jsx
(pytorch) ubuntu@ktlab2:~$ python
Python 3.8.13 (default, Mar 28 2022, 11:38:47)
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.__version__
'1.7.1'
>>> torch.version.moreh
'22.8.0'
```



## 2. Docker 이미지로 Moreh 실행

Hyperscale AI Computing 서비스는 Docker 컨테이너 안에서 AI 가속기를 사용하는 PyTorch 프로그램을 실행할 수 있도록 전용 Docker 이미지를 제공하고 있습니다. VM에서 다음과 같이 실행하여 AI 가속기가 활성화된 컨테이너를 실행할 수 있습니다.

```
(pytorch) ubuntu@vm:~$ **sudo moreh-docker-run**
...
Login Succeeded
Unable to find image 'sys.deploy.kt-epc.moreh.io:5001/moreh:0.8.0' locally
0.8.0: Pulling from moreh
...
Digest: sha256:003b54de6395f468799db818e1c884a3dfd92f7ec296a40c082b123cc9298ac2
Status: Downloaded newer image for sys.deploy.kt-epc.moreh.io:5001/moreh:0.8.0
(moreh) root@vm:~#
```

컨테이너 안에서 AI 가속기 정보를 조회하고 PyTorch 프로그램을 실행시킬 수 있습니다.

```
(moreh) root@vm:~# **moreh-smi**
+--------------------------------------------------------------------------------------------------------------+
|  Moreh-SMI 0.8.0                                               Client Version: 0.8.0  Server Version: 0.8.0  |
+--------------------------------------------------------------------------------------------------------------+
|  Device  |        Name         |            Token           |     Model    |  Memory Usage  |  Total Memory  |
+==============================================================================================================+
|       1  |  KT AI Accelerator  |  ZXhhbXBsZSB0b2tlbiBzdHI=  |  small.16gb  |  -             |  -             |
+--------------------------------------------------------------------------------------------------------------+

Processes:
+----------------------------------------------------------+
|  Device  |  Job ID  |  PID  |  Process  |  Memory Usage  |
+==========================================================+
+----------------------------------------------------------+
(moreh) root@vm:~# **python pytorch-sample.py**
Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-images-idx3-ubyte.gz to data/FashionMNIST/raw/train-images-idx3-ubyte.gz
26427392it [00:04, 5389702.34it/s]
Extracting data/FashionMNIST/raw/train-images-idx3-ubyte.gz to data/FashionMNIST/raw
Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-labels-idx1-ubyte.gz to data/FashionMNIST/raw/train-labels-idx1-ubyte.gz
32768it [00:00, 36542.51it/s]
Extracting data/FashionMNIST/raw/train-labels-idx1-ubyte.gz to data/FashionMNIST/raw
Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-images-idx3-ubyte.gz to data/FashionMNIST/raw/t10k-images-idx3-ubyte.gz
4423680it [00:08, 505491.87it/s]
Extracting data/FashionMNIST/raw/t10k-images-idx3-ubyte.gz to data/FashionMNIST/raw
Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-labels-idx1-ubyte.gz to data/FashionMNIST/raw/t10k-labels-idx1-ubyte.gz
8192it [00:00, 13945.86it/s]
Extracting data/FashionMNIST/raw/t10k-labels-idx1-ubyte.gz to data/FashionMNIST/raw
Processing...
Done!
[info] Requesting resources for KT AI Accelerator from the server...
[info] Initializing the worker daemon for KT AI Accelerator...
[info] [1/1] Connecting to resources on the server (192.168.00.00:00000)...
[info] Establishing links to the resources...
[info] KT AI Accelerator is ready to use.
Epoch 1
loss: 2.298501  [    0/60000]
loss: 2.287861  [ 6400/60000]
loss: 2.270298  [12800/60000]
^C
```

컨테이너 안에서 인식되는 AI 가속기는 VM에 할당된 AI 가속기와 동일한 것입니다. VM에서 가속기 모델을 변경하면 컨테이너 안에서도 적용되며 그 반대도 마찬가지입니다. 또한 VM에서 AI 가속기를 사용하는 동안은 컨테이너 안에서는 AI 가속기를 사용할 수 없으며 이것 역시 반대도 마찬가지입니다. 예를 들어 VM에서 AI 가속기를 사용하는 train.py 프로그램이 실행 중인 동안 컨테이너에서 AI 가속기를 사용하는 다른 프로그램을 실행할 경우, 아래와 같은 메시지를 출력하고 VM에서 train.py 프로그램이 끝날 때까지 대기하게 됩니다.

```
(moreh) root@vm:~# **python pytorch-sample.py**
...
[info] Requesting resources for KT AI Accelerator from the server...
[warning] KT AI Accelerator is already in use by another process:
[warning]   (pid: 10000) python train.py
[warning] Two or more processes cannot use KT AI Accelerator at the same time. The program will resume automatically after the process 10000 terminates...
```

이 문서의 나머지 부분에서는 Hyperscale AI Computing 서비스를 위한 Docker 컨테이너를 실행하는 과정을(즉, moreh-docker-run 명령이 내부적으로 하는 일을) 단계별로 자세히 설명합니다.

<aside>
💡 Docker를 사용하지 않고도 VM 안에서 바로 AI 가속기를 사용해 PyTorch 프로그램 실행이 가능합니다. 이 문서는 특별히 Docker 기반으로 실행해야 하는 애플리케이션이 있는 분들을 대상으로 합니다.

</aside>

### 2-1. 이미지 내려받기

Hyperscale AI Computing 서비스는 전용 Docker 이미지를 위한 사설 registry를 제공하고 있습니다. 다음과 같이 실행하여 사설 registry에 로그인하고 Docker 이미지 최신 버전을 다운로드할 수 있습니다.

```
(pytorch) ubuntu@vm:~$ **sudo docker login -uguest -pguest sys.deploy.kt-epc.moreh.io:5001**
WARNING! Using --password via the CLI is insecure. Use --password-stdin.
WARNING! Your password will be stored unencrypted in /home/ubuntu/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
(pytorch) ubuntu@vm:~$ **sudo docker image pull sys.deploy.kt-epc.moreh.io:5001/moreh:latest**
latest: Pulling from moreh
284055322776: Pull complete
3cc7ef3422d9: Pull complete
c8ec61cd0a03: Pull complete
17ab1f47ffda: Pull complete
720062349d38: Pull complete
Digest: sha256:003b54de6395f468799db818e1c884a3dfd92f7ec296a40c082b123cc9298ac2
Status: Downloaded newer image for sys.deploy.kt-epc.moreh.io:5001/moreh:latest
sys.deploy.kt-epc.moreh.io:5001/moreh:latest
(pytorch) ubuntu@vm:~$ **sudo docker images**
REPOSITORY                              TAG       IMAGE ID       CREATED        SIZE
sys.deploy.kt-epc.moreh.io:5001/moreh   latest    8fed6aa6b12c   30 hours ago   3.42GB
(pytorch) ubuntu@vm:~$ **sudo docker logout sys.deploy.kt-epc.moreh.io:5001**
Removing login credentials for sys.deploy.kt-epc.moreh.io:5001
```

### 2-2. 컨테이너 시작

다음과 같이 docker run 명령으로 컨테이너를 실행할 수 있습니다. 이 때 다음의 두 가지 옵션을 포함시켜야 합니다.

- **--net=host --privileged**
    - Hyperscale AI Computing 서비스는 GPU와의 빠른 통신을 위해 고속 InfiniBand 네트워크를 사용합니다. --net=host --privileged 옵션은 컨테이너 안에서도 InfiniBand 네트워크에 접속하여 GPU가 위치한 서버와 통신이 가능하도록 합니다. 컨테이너가 실행된 후 ifconfig 명령을 실행하여 ib0 인터페이스가 표시된다면 옵션이 정상적으로 적용된 것입니다.
- **-v /etc/moreh:/etc/moreh**
    - VM의 /etc/moreh 디렉터리에는 AI 가속기 사용 시 resource farm에 접속하기 위한 정보가 저장되어 있습니다. -v /etc/moreh:/etc/moreh 옵션은 컨테이너 안에서도 /etc/moreh 디렉터리에 resource farm 접속 정보가 저장되도록 합니다. 컨테이너가 실행된 후 moreh-smi 명령이 에러 없이 실행된다면 옵션이 정상적으로 적용된 것입니다.

```jsx
(pytorch) ubuntu@vm:~$ **sudo docker run --rm -it --net=host --privileged -v /etc/moreh:/etc/moreh sys.deploy.kt-epc.moreh.io:5001/moreh:latest /bin/bash**
(moreh) root@vm:~#
```
### 2-3. Docker Image 실행

```
### **moreh-docker-run**
```
Moreh AI Framework(MAF)가 담긴 Docker Image를 실행합니다.

**Supported Arguments**

**--pullonly, -p**

해당 옵션값을 추가로 줄경우, MAF Container를 바로 실행하지않고 단순히 Image만 다운로드 받게 됩니다.

해당 옵션값을 사용할때는 `--target` 옵션값을 꼭 같이 사용해야하며, `--target`옵션 값 뒤에는 아래 예시와 같이 버전을 명시해줘야합니다.

```bash
**moreh-docker-run --pullonly --target** 22.8.0
```

**--version, -v**

MAF Docker Image 버전명을 보여줍니다.