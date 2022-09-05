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

#### Arguments
##### --reset
reset gpu resource

### moreh-docker-run
Moreh AI Framework(MAF)가 담긴 Docker Image를 실행합니다.

### moreh-switch-model
Software-Defined Accelerator(SDA) Model을 변경하는 명령어입니다. 현재 지원하는 SDA Model은 다음과 같습니다.

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