## Management Commands

Moreh AI Frameworks support multiple commands like below.

### moreh-smi

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