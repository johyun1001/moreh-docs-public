## 자주 묻는 질문

### CUDA 설정관련
HAC 의 VM 상에서는 CUDA 설치되어 있지 않기 때문에 따로 경로가 존재하지 않습니다. HAC은 CUDA Driver 가 아닌 AI Accelerator 가 자동으로 할당되어 학습이 진행되는 방식입니다. 따라서 CUDA 개발도구를 직접 설치하지 않고 Pytorch 코드를 수행시키셔도 자동으로 GPU가 할당되어 진행되게 됩니다. 

### Docker를 활용한 MAF GPU 연산
Docker환경안에서도 MAF GPU연산을 사용하실수 있습니다. Docker용 MAF Image는 다음과 같은 명령어로 실행하실수 있습니다.

```shell
sudo moreh-docker-run --target 22.8.0
```

만일, Docker Container 실행을 시키지않고 단순히 Docker용 MAF Image만 다운받길 원하시다면 아래 명령어를 이용하여 이미지를 다운받으실수있습니다.

```
sudo moreh-docker-run --pullonly --target 22.8.0
```

### 모델 학습 종료 이후에도 여전히 리소스를 할당받고 있을때
때때로 모델 학습 종류 이후에도 해당 프로세스가 GPU 리소스를 계속해서 할당받고 있을수가 있습니다. 해당 현상이 발생했을경우에는 아래 명령어를 사용하시는걸 제안드립니다.

```shell
moreh-smi --reset
```

> 위의 명령어로도 여전히 프로세스가 실행중인걸로 보인다면 `moreh-smi` 명령어에서 나오는 PID를 이용하여 강제로 종료시킬 수 있습니다.