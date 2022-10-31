# Reference Model 

**Reference Model (이하 RM) 이란?**

Moreh framework 에서 학습, 추론이 가능한 딥러닝 모델을 의미합니다. 정기적으로 프레임워크와 함께 배포되며 Moreh 솔루션에서 딥러닝 학습에 필수적인 단계들을 수행할 수 있는 모델을 다운로드 할 수 있습니다.
따라서 사용자는 RM을 활용하여 직접 코딩하지 않아도 바로 학습, 추론을 수행할 수 있습니다. 

아래 간단한 명령어 한 줄로 다양한 Reference Model(이하 RM) Code를 얻을 수 있습니다. 

```bash
get-reference-model resnet
```

위와 같은 명령어 실행 시 ResNet에 대한 RM Code 설치 파일을 다운로드 받게 되며, 동시에 해당 설치 파일을 실행시켜 실행환경을 세팅해줍니다. 명령어 실행 완료 시 모델명에 따른 폴더가 생성이 되며 해당 폴더로 들어가 아래 명령어로 바로 모델을 실행(학습) 시킬 수가 있습니다.

```bash
# 학습 모델 폴더로 이동
cd resnet

# 학습 모델 실행
python train.py
```

어떤 모델 코드들이 제공하는지 궁금하시다면 아래와 같은 명령어로 제공가능한 모델 목록을 보실수가 있습니다.

가장 범용적으로 쓰이는 딥러닝 모델과 Moreh 솔루션을 이용한 딥러닝 학습 모범 사례로 쓰일만한 안전한 모델들이 목록에 나타납니다.

```bash
get-reference-model -h

# [INFO] Availabel Model List => 3dunet alexnet arcface bart bert dcgan deeplabv3m deeplabv3r densenet dlrm fasterrcnn fcn_resnet gnmt googlenet gpt gpt2 inceptionv3 lraspp maskrcnn mnasnet mobilenetv2 mobilenetv3 ncf resnet resnet2p1d resnet3d resnetMC resnext retinanet rnnt roberta shufflenetv2 speech2text squeezenet ssd ssdlite stdc t5 tacotron2 transformer transformerXL unet vgg wideresnet yolor yolov5 (2022-10-20 기준)
```

만일, 모델 설치 파일(.sh)에 대해서 수정 사항이 필요할 경우엔 아래와 같이 `--download-only` 옵션을 추가하여 모델 설치 파일만 다운로드 받으실수도 있습니다. 해당 옵션을 추가하고 실행하면 실행경로에 `install_MODEL_NAME.sh` 파일이 생성됩니다.

```bash
get-reference-model --download-only resnet
```