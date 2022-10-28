# GPU 자원 변경하기

SDA를 변경하여 VM에서 사용할 GPU 자원의 양을 조정할 수 있습니다. 다음 명령어(moreh-switch-model)를 통해 VM에서 작업하는 사용자에게 제공하는 GPU의 크기를 확인 후 변경할 수 있습니다.

<aside>
💡 SDA(이하 Software-Defined Accelerator) 기술은 1개 혹은 복수의 물리 GPU(s)들을 하나의 논리 GPU로 만들어주는 하드웨어 가상화 기술입니다. 즉, SDA는 pytorch/tensorflow 코드 상에서 cuda 혹은 cuda:0 보여지며 실제 계산은 물리 GPU들에 병렬적으로 처리됩니다.

</aside>

```
moreh-switch-model
```

moreh-switch-model 툴은 SDA를 변경하는 ****대화형**** 명령어입니다. 현재 지원하는 SDA는 다음(Figure 1)과 같습니다. 번호로 SDA을 선택할수있고, q(또는 Q)로 대화를 종료 할 수 있습니다. 

제일 작은 단위의 SDA는 Small.64GB이며 총 64GB 메모리를 가지고 있습니다. 그 이상 SDA는 Small.64GB의 배수만큼의 계산능력과 메모리를 가집니다. 예를 들어 Large.256GB는 Small.64GB에 비해 4배의 계산능력과 메모리를 가집니다. 

<aside>
ℹ️ 지원하는 SDA에서 Small.64GB가 최소의 단위이지만 1 GPU를 의미하지는 않습니다.

</aside>

```bash
(pytorch) ubuntu@moreh-server:~$ moreh-switch-model

Current KT AI Accelerator: 3xLarge.1536GB
1. Small.64GB
2. Medium.128GB
3. Large.256GB
4. xLarge.512GB
5. 2xLarge.1024GB
6. 3xLarge.1536GB*
7. 4xLarge.2048GB
8. 6xLarge.3072GB
9. 8xLarge.4096GB
10. 12xLarge.6144GB
11. 24xLarge.12288GB
12. 48xLarge.24576GB
13. 1.5xLarge.768GB
```
Figure 1. moreh-switch-model 출력 화면