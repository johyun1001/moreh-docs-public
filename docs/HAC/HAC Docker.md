# Docker 사용하기

## Quick Start

Hyperscale AI Computing 서비스는 Docker 컨테이너 안에서 AI 가속기를 사용하는 PyTorch 프로그램을 실행할 수 있도록 전용 Docker 이미지를 제공하고 있습니다. VM에서 다음과 같이 실행하여 AI 가속기가 활성화된 컨테이너를 실행할 수 있습니다.

```
(pytorch) ubuntu@vm:~$ sudo moreh-docker-run
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
(moreh) root@vm:~# moreh-smi
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
(moreh) root@vm:~# python pytorch-sample.py
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
(moreh) root@vm:~# python pytorch-sample.py
...
[info] Requesting resources for KT AI Accelerator from the server...
[warning] KT AI Accelerator is already in use by another process:
[warning]   (pid: 10000) python train.py
[warning] Two or more processes cannot use KT AI Accelerator at the same time. The program will resume automatically after the process 10000 terminates...
```

이 문서의 나머지 부분에서는 Hyperscale AI Computing 서비스를 위한 Docker 컨테이너를 실행하는 과정을(즉, moreh-docker-run 명령이 내부적으로 하는 일을) 단계별로 자세히 설명합니다.

> 💡 Docker를 사용하지 않고도 VM 안에서 바로 AI 가속기를 사용해 PyTorch 프로그램 실행이 가능합니다. 이 문서는 특별히 Docker 기반으로 실행해야 하는 애플리케이션이 있는 분들을 대상으로 합니다.

## 이미지 내려받기

Hyperscale AI Computing 서비스는 전용 Docker 이미지를 위한 사설 registry를 제공하고 있습니다. 다음과 같이 실행하여 Docker Image를 내려받거나 바로 실행하실수가 있습니다.

```
(pytorch) ubuntu@moreh-server-new-9:~$ sudo moreh-docker-run
WARNING! Using --password via the CLI is insecure. Use --password-stdin.
WARNING! Your password will be stored unencrypted in /home/ubuntu/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
Unable to find image 'sys.deploy.kt-epc.moreh.io:5001/moreh:22.9.1' locally
22.9.1: Pulling from moreh
726b8a513d66: Pull complete
4f4fb700ef54: Pull complete
7da60f7be8c2: Pull complete
12ad2da3b577: Pull complete
98caf5a4948e: Pull complete
090d165a45e0: Pull complete
674df12613d3: Pull complete
Digest: sha256:c4d8dc1517296b0c18ae03b52e1e7ce20d09d40ebc0c423c92830fb73489621d
Status: Downloaded newer image for sys.deploy.kt-epc.moreh.io:5001/moreh:22.9.1
(moreh) root@moreh-server-new-9:~#
```

## 컨테이너 시작

다음과 같이 docker run 명령으로 컨테이너를 실행할 수 있습니다. 이 때 다음의 두 가지 옵션을 포함시켜야 합니다.

- **--net=host --privileged**
    - Hyperscale AI Computing 서비스는 GPU와의 빠른 통신을 위해 고속 InfiniBand 네트워크를 사용합니다. --net=host --privileged 옵션은 컨테이너 안에서도 InfiniBand 네트워크에 접속하여 GPU가 위치한 서버와 통신이 가능하도록 합니다. 컨테이너가 실행된 후 ifconfig 명령을 실행하여 ib0 인터페이스가 표시된다면 옵션이 정상적으로 적용된 것입니다.
- **-v /etc/moreh:/etc/moreh**
    - VM의 /etc/moreh 디렉터리에는 AI 가속기 사용 시 resource farm에 접속하기 위한 정보가 저장되어 있습니다. -v /etc/moreh:/etc/moreh 옵션은 컨테이너 안에서도 /etc/moreh 디렉터리에 resource farm 접속 정보가 저장되도록 합니다. 컨테이너가 실행된 후 moreh-smi 명령이 에러 없이 실행된다면 옵션이 정상적으로 적용된 것입니다.

```
(pytorch) ubuntu@vm:~$ sudo docker run --rm -it --net=host --privileged -v /etc/moreh:/etc/moreh sys.deploy.kt-epc.moreh.io:5001/moreh:latest /bin/bash
(moreh) root@vm:~#
```