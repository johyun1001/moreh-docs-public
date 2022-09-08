## Management Commands

Moreh AI Frameworks support multiple commands like below.

### moreh-smi
현재 선택된 Software-Defined Accelerator(SDA) Model, 실행중인 학습 프로세스 및 GPU Resource를 얼마나 할당받고있는지를 확인 할 수 있는 명령어입니다.
```
(pytorch) ubuntu@hac-worker01:~$ moreh-smi
+--------------------------------------------------------------------------------------------------------------+
|  Moreh-SMI 22.7.0                                            Client Version: 22.7.0  Server Version: 22.8.0  |
+--------------------------------------------------------------------------------------------------------------+
|  Device  |        Name         |            Token           |     Model    |  Memory Usage  |  Total Memory  |
+==============================================================================================================+
|      13  |  KT AI Accelerator  |  [TOKEN_VARIABLE]  |  Small.64GB  |  -             |  -             |
+--------------------------------------------------------------------------------------------------------------+

Processes:
+----------------------------------------------------------+
|  Device  |  Job ID  |  PID  |  Process  |  Memory Usage  |
+==========================================================+
+----------------------------------------------------------+
```

#### Supported Arguments
##### **--reset**
할당된 GPU 리소스를 리셋합니다

### moreh-docker-run
Moreh AI Framework(MAF)가 담긴 Docker Image를 실행합니다.

#### Supported Arguments
##### **--pullonly**, **-p**
해당 옵션값을 추가로 줄경우, MAF Container를 바로 실행하지않고 단순히 Image만 다운로드 받게 됩니다.
해당 옵션값을 사용할때는 `--target` 옵션값을 꼭 같이 사용해야하며, `--target`옵션 값 뒤에는 아래 예시와 같이 버전을 명시해줘야합니다.
```shell
moreh-docker-run --pullonly --target 22.8.0
```

##### **--version**, **-v**
MAF Docker Image 버전명을 보여줍니다.

### moreh-switch-model
Software-Defined Accelerator(SDA) Model을 변경하는 **대화형** 명령어입니다. 현재 지원하는 SDA Model은 다음과 같습니다. 번호로 SDA Model을 선택할수있고, q(또는 Q)로 대화를 종료 할 수 있습니다.

```shell
1. Small.64GB
2. Medium.128GB
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
13. 1.5xLarge.768GB
```

### update-moreh
Moreh AI Framework(MAF)를 업데이트하는 명령어입니다. 기본적으로 해당 명령어 실행시 현재까지 배포된 버전중 최신버전으로 업데이트를 진행합니다.

#### Supported Arguments
##### **--force --target**
MAF를 특정 버전으로 강제 다운(업)그레이드를 할수있는 옵션입니다. `--target` 옵션뒤에는 특정 버전을 아래와 같이 기입 해주시면 됩니다.
```shell
update-moreh --force --target 22.7.2
```