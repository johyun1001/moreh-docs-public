### 남청주HAC 내의 conda 가상환경 초기화하기

남청주HAC VM에서 conda 환경에 문제가 생길경우, conda 가상환경을 다시 세팅하는 방법입니다. `pytorch` 라는 conda 가상환경 명으로 세팅한다고 가정하겠습니다.

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

```python
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
