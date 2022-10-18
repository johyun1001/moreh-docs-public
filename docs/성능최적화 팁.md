# Hyperscale AI Computing 이용 방법

# 상품 신청

Hyperscale AI Computing 서버는 D1 플랫폼의 DX-M1 존에서 제공되는 서비스입니다. SSH key pair 기반의 접속 인증 방식을 사용하므로 서버를 생성하기 전에 우선 'Server > SSH Key Pair' 메뉴에서 key pair를 생성해야 합니다.

(KT에서 스크린샷 추가 필요)

D1 플랫폼의 'Server > Server' 메뉴로 이동하여 [서버 생성] 버튼을 클릭합니다.

(KT에서 스크린샷 추가 필요)

서버 생성 위치, tier, 서버 이름, 서버 타입, key pair를 선택하고 좌측에서 Hyperscale AI Computing 서버 상품을 선택합니다. 원하는 OS 타입과 사양을 선택 후, 하단에서 GPU 사양과 reference model을 선택하고 `[생성하기]` 버튼을 클릭합니다. Hyperscale AI Computing 서버의 root 디스크는 기본 100 GB로 제공되며, 시간 요금제로만 제공됩니다.

(KT에서 스크린샷 추가 필요)

서버 생성 요청 후, 서버 리스트에서 신청한 서버가 '사용' 상태이면 생성이 완료된 것입니다.

(KT에서 스크린샷 추가 필요)

서버 목록에서 Hyperscale AI Computing 서버를 선택한 후 `[...]` 버튼을 클릭하고 '상세 정보' 메뉴로 이동하여 생성한 서버의 상태를 조회할 수 있습니다. Hyperscale AI Computing 서버의 경우 GPU 사양, GPU 프로그램 실행 상태 및 reference model 정보를 추가 확인할 수 있습니다.

(KT에서 스크린샷 추가 필요)

마찬가지로 Hyperscale AI Computing 서버를 선택한 후 `[...]` 버튼을 클릭하고 'GPU 사양변경' 메뉴로 이동하여 GPU 사양을 변경할 수 있습니다. 단, VM 내부에서 GPU를 사용하는 프로그램이 실행 중인 동안에는 사양을 변경할 수 없습니다. GPU 사양은 터미널에서도 변경이 가능합니다. (하단의 'AI 가속기 모델 변경' 장을 참고하십시오.) GPU에서 실제 프로그램을 실행하지 않는 한, 사양을 선택하는 것만으로는 별도의 요금이 부과되지 않습니다.

# VM 접속하기

(KT에서 스크린샷 추가 필요)

생성한 Hyperscale AI Computing 서버에 접속하기 위해서는 '접속설정' 메뉴를 통해 포트포워딩 설정이 필요합니다. 접속 설정은 'Server > Server' 메뉴에서도 가능하고, 'Server >Networking' 메뉴에서도 가능합니다. 접근을 원하는 사설 포트(SSH 접속의 경우 22번)와 공인 IP에서 사용할 공인 포트 설정을 합니다.

(KT에서 스크린샷 추가 필요)

포트포워딩 규칙 추가/삭제 시, 방화벽 설정도 함께 적용해 주어야 VM 접속이 가능합니다. 접속 설정 후 'Server > Networking' 메뉴에서 방화벽 설정을 통해 방화벽 룰을 추가한 후 사용할 수 있습니다.

## macOS 혹은 Linux 환경에서 접속하기

macOS의 경우 Cmd + Space를 누른 뒤 '터미널'을 입력하여 터미널을 실행합니다. Linux의 경우 시작 버튼을 눌러 Terminal을 실행합니다. 이후 VM 생성 시 사용한 key pair 파일이 있는 디렉터리로 이동합니다.

우선 해당 key pair 파일(예: keypair1.pem)의 권한을 변경해야 SSH 접속이 가능합니다. 터미널에서 다음과 같이 실행하여 권한을 변경할 수 있습니다.

```
user@machine:~$ chmod 0600 keypair1.pem
```

이후 SSH 명령을 실행하여 서버에 접속할 수 있습니다. Hyperscale AI Computing 서버는 현재 Ubuntu 18.04를 지원하기 때문에 계정명 ubuntu로 접속해야 합니다. 포트의 경우 접속 설정 시 지정한 공인 포트를 입력해 주면 됩니다. (예를 들어 서버의 사설 포트 22번을 공인 포트 10022번으로 연결하였을 경우 -p 10022로 입력)

```
user@machine:~$ ssh -i keypair1.pem ubuntu@[공인 IP] -p [포트]
```

## Windows 환경에서 접속하기

PuTTY 프로그램을 사용하여 VM 접속이 가능합니다. PuTTY가 없을 경우 아래 URL을 통해 설치 가능합니다.

- PuTTY 설치: [https://www.putty.org/](https://www.putty.org/)

PuTTY를 통해 서버에 접속하려면 우선 포털에서 다운로드한 .pem 파일을 .ppk 파일로 변환해야 합니다. 우선 시작 메뉴에서 'PuTTYgen'을 입력하여 실행합니다. (PuTTY를 package 버전으로 설치하면 PuTTYgen이 자동으로 같이 설치됩니다.)

(KT에서 스크린샷 추가 필요)

[Load] 버튼을 클릭하여 .pem 파일을 불러 옵니다.

(KT에서 스크린샷 추가 필요)

.pem 파일이 보이지 않을 경우, 아래 그림과 같이 확장자를 'All Files (*.*)'로 바꿔 줍니다.

(KT에서 스크린샷 추가 필요)

.pem 파일을 성공적으로 불러 오면 아래와 같은 화면이 나타납니다. 여기서 `[확인]` 버튼을 클릭합니다.

(KT에서 스크린샷 추가 필요)

[Save private key] 버튼을 클릭한 다음 '예'를 선택하여 변환된 .ppk 파일을 저장합니다.

(KT에서 스크린샷 추가 필요)

이제 시작 메뉴에서 'PuTTY'를 입력하여 PuTTY 프로그램을 실행합니다.

(KT에서 스크린샷 추가 필요)

좌측의 'Connection > SSH > Auth' 메뉴를 선택한 다음 `[Browse]` 버튼을 클릭하여 아까 전에 생성한 .ppk 파일을 선택합니다.

(KT에서 스크린샷 추가 필요)

이제 다시 좌측의 'Session' 메뉴로 이동하여 'Host Name' 란에 ubuntu@[공인 IP]를 입력합니다. Hyperscale AI Computing 서버는 현재 Ubuntu 18.04를 지원하기 때문에 계정명 ubuntu로 접속해야 합니다. 'Port' 란에는 접속 설정 시 지정한 공인 포트를 입력해 주면 됩니다. (예를 들어 서버의 사설 포트 22번을 공인 포트 10022번으로 연결하였을 경우 10022를 입력) 마지막으로 하단의 `[Open]` 버튼을 클릭하여 서버에 접속합니다.

(KT에서 스크린샷 추가 필요)

# 소프트웨어 환경

Hyperscale AI Computing 서비스 VM에는 Anaconda 환경 위에 Python 3.8, PyTorch 1.7.1 및 Hyperscale AI Computing 지원을 위한 플러그인이 설치되어 있습니다. 다음과 같이 실행하여 PyTorch 버전 및 Hyperscale AI Computing 플러그인 버전 정보를 확인할 수 있습니다.

```
(pytorch) ubuntu@vm:~$ python
Python 3.8.12 (default, Oct 12 2021, 13:49:34)
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.__version__
'1.7.1'
>>> torch.version.moreh
'0.8.0'
>>> quit()
(pytorch) ubuntu@vm:~$
```


>⚠️ 기본 Anaconda 환경에 설치되어 있는 PyTorch를 삭제하거나 다른 버전으로 덮어쓸 경우 Hyperscale AI Computing 지원 프러그인이 지워질 수도 있으니 유의하십시오. Hyperscale AI Computing 서비스는 conda 혹은 pip 명령이 기존 PyTorch를 삭제하거나 덮어 쓰려고 하면 원래 상태로 자동 복구를 시도할 것입니다. 만약 자동 복구가 정상 동작하지 않아 PyTorch 패키지 혹은 Hyperscale AI Computing 플러그인에 문제가 생겼을 경우 복구하는 방법은 '자주 묻는 질문' 문서를 참고하십시오.


# AI 가속기 정보 확인

터미널에서 moreh-smi 명령을 실행하여 현재 Hyperscale AI Computing 서비스로 사용 중인 AI 가속기 정보를 확인할 수 있습니다.

```
(pytorch) ubuntu@vm:~$ moreh-smi
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
```

PyTorch 프로그램이 AI 가속기를 사용 중인 동안에는 다음과 같이 실행 중인 프로세스 정보, 전체 메모리 용량과 현재 메모리 사용량이 함께 표시됩니다.

```
(pytorch) ubuntu@vm:~$ moreh-smi
+--------------------------------------------------------------------------------------------------------------+
|  Moreh-SMI 0.8.0                                               Client Version: 0.8.0  Server Version: 0.8.0  |
+--------------------------------------------------------------------------------------------------------------+
|  Device  |        Name         |            Token           |     Model    |  Memory Usage  |  Total Memory  |
+==============================================================================================================+
|       1  |  KT AI Accelerator  |  ZXhhbXBsZSB0b2tlbiBzdHI=  |  small.16gb  |  320 MiB       |  16368 MiB     |
+--------------------------------------------------------------------------------------------------------------+

Processes:
+-------------------------------------------------------------------+
|  Device  |  Job ID  |   PID   |      Process     |  Memory Usage  |
+===================================================================+
|       1  |    5000  |  10000  |  python test.py  |  320 MiB       |
+-------------------------------------------------------------------+
```

# AI 가속기 모델 변경

터미널에서 moreh-switch-model 명령을 실행하여 AI 가속기 모델을 다른 것으로 변경할 수 있습니다. 변경할 모델 순번(1~8)을 입력하고, q를 입력하여 프로그램을 종료합니다.

```
(pytorch) ubuntu@vm:~$ moreh-switch-model
Current KT AI Accelerator: small.16gb

1. small.16gb*
2. medium.32gb
3. large.48gb
4. large.64gb
5. xlarge.96gb
6. 2xlarge.192gb
7. 3xlarge.288gb
8. 4xlarge.384gb

Selection (1-8, q, Q): 5
The KT AI Accelerator model is successfully switched to  "xlarge.96gb".

1. small.16gb
2. medium.32gb
3. large.48gb
4. large.64gb
5. xlarge.96gb*
6. 2xlarge.192gb
7. 3xlarge.288gb
8. 4xlarge.384gb

Selection (1-8, q, Q): q
(pytorch) ubuntu@vm:~$
```


>⚠️ AI 가속기에서 프로그램이 실행 중인 동안에는 가속기 모델을 변경할 수 없습니다.

# PyTorch 프로그램 실행

Hyperscale AI Computing 서비스의 공식 지원 모델에 대한 실행 방법은 별도의 모델별 매뉴얼을 참고하십시오.

VM의 sample 디렉터리에 MNIST 데이터베이스를 학습시키는 간단한 PyTorch 샘플 프로그램이 설치되어 있습니다. ([https://pytorch.org/tutorials/beginner/basics/optimization_tutorial.html](https://pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)) 다음과 같이 실행하여 AI 가속기가 잘 동작하는지를 확인할 수 있습니다. 초반의 몇 iteration을 확인한 다음에는 프로그램을 종료해도 됩니다.

```
(pytorch) ubuntu@vm:~$ cd sample
(pytorch) ubuntu@vm:~/sample$ ls
pytorch-sample.py
(pytorch) ubuntu@vm:~/sample$ python pytorch-sample.py
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

만약 "KT AI Accelerator is ready to use." 메시지와 함께 학습이 정상 시작되지 않고 다른 에러 메시지와 함께 프로그램이 종료된다면 '자주 묻는 질문' 문서를 참고하여 조치하거나 기술 지원을 받으시기 바랍니다.

# 소프트웨어 업데이트

Hyperscale AI Computing 서비스는 지속적으로 소프트웨어 업데이트가 이루어지고 있습니다. 터미널에서 update-moreh 명령을 실행하여 소프트웨어가 최신 버전이 아닌 경우 자동으로 업데이트할 수 있습니다.

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

구 버전의 소프트웨어를 사용할 경우 PyTorch 프로그램 실행 시에 경고 메시지가 표시되거나("A newer version of Moreh AI Framework is available.") 아예 AI 가속기 할당이 불가능할 수 있습니다("The current version of Moreh AI Framework is outdated and no longer supported in the system.").

# GPU 자원 할당

Hyperscale AI Computing 서비스는 실제 PyTorch 프로그램을 실행하면 GPU 자원을 할당받고 프로그램이 종료되면 GPU 자원을 할당 해제합니다. 이 과정은 자동으로 이루어지며 사용자가 특별히 개입할 필요가 없습니다.

하나의 VM에서 AI 가속기를 사용하는 프로그램을 동시에 두 개 이상 실행할 수는 없습니다. 예를 들어 AI 가속기를 사용하는 train.py 프로그램이 실행 중인 동안 마찬가지로 AI 가속기를 사용하는 inference.py 프로그램을 실행할 경우, 나중에 실행한 프로그램은 아래와 같은 메시지를 출력하고 앞에 실행한 프로그램이 끝날 때까지 대기하게 됩니다.

```
(pytorch) ubuntu@vm:~$ python inference.py
...
[info] Requesting resources for KT AI Accelerator from the server...
[warning] KT AI Accelerator is already in use by another process:
[warning]   (pid: 10000) python train.py
[warning] Two or more processes cannot use KT AI Accelerator at the same time. The program will resume automatically after the process 10000 terminates...
```

많은 수의 PyTorch 프로그램들이 모델 학습 시 학습 데이터를 빠르게 불러 오기 위해 별도의 DataLoader 프로세스를 띄우는 방식으로 동작합니다. 이 경우 PyTorch 프로그램이 비정상 종료했을 때(예를 들어 Ctrl+C로 강제 종료했을 때) 주 프로세스는 없어지더라도 DataLoader 프로세스들은 없어지지 않고 남아 있는 경우가 있습니다. DataLoader 프로세스가 실행 중이면 AI 가속기에서 새로운 프로그램을 실행할 수 없을 뿐더러 VM의 CPU 코어와 메인 메모리를 지속적으로 점유하기 때문에 다른 프로그램 실행 시 문제가 될 수 있습니다. 현재 VM에 실행 중인 Python 프로세스가 존재하는지 ps aux | grep python 명령으로 확인할 수 있습니다. 또한 실행 중인 모든 Python 프로세스를 pkill python 명령으로 제거할 수 있습니다.

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

한편 Hyperscale AI Computing 시스템에 동시에 너무 많은 자원 할당 요청이 들어 올 경우 일시적으로 GPU 자원의 할당이 불가능할 수 있습니다. 이 경우 프로그램이 아래와 같은 메시지를 출력하고 GPU 자원이 할당될 때까지 대기할 수 있습니다. 이 경우 가만히 있으면 GPU 자원을 할당 받은 이후 자동으로 실행이 재개됩니다.

```
(pytorch) ubuntu@vm:~$ python train.py
...
[info] Requesting resources for KT AI Accelerator from the server...
[warning] Not enough resources are currently available for KT AI Accelerator. All resources in the system are being used by other users. The program will resume automatically when resources become available...
```

이외에 GPU 자원 할당에 실패하는 경우가 있다면 '자주 묻는 질문' 문서를 참고하여 조치하거나 기술 지원을 받으시기 바랍니다.