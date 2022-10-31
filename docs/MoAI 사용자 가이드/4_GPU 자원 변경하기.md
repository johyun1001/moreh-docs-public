# GPU 자원 변경하기

SDA를 변경하여 VM에서 사용할 GPU 자원의 양을 조정할 수 있습니다. 다음 명령어(moreh-switch-model)를 통해 VM에서 작업하는 사용자에게 제공하는 GPU의 크기를 확인 후 변경할 수 있습니다.

<aside>
💡 GPU 자원 변경 기술은 1개 혹은 복수의 물리 GPU(s)들을 하나의 논리 GPU로 만들어주는 하드웨어 가상화 기술입니다. 즉, pytorch/tensorflow 코드 상에서 cuda 혹은 cuda:0 보여지며 실제 계산은 물리 GPU들에 병렬적으로 처리됩니다.

</aside>
