# HAC 서비스 기본 개념

---
**이 문서는 HAC 서비스 기본 개념 및 작동 방법을 안내합니다.** 


**Q. Hyperscale AI Computing은 어떤 방식으로 GPU 자원을 사용하게 되나요?**

**A.** PyTorch와 함께 설치되는 Hyperscale AI Computing 지원 플러그인이 GPU 자원의 할당 및 사용을 위한 모든 작업을 자동으로 수행합니다.

먼저 PyTorch 프로그램이 실행되면 서버에 요청을 보내 resource farm에 위치하는 GPU 자원을 하나 이상 할당받습니다. 화면에 다음과 같은 메시지가 표시되면 GPU 자원에 연결이 완료된 것입니다.

```
[info] Requesting resources for KT AI Accelerator from the server...
[info] Initializing the worker daemon for KT AI Accelerator...
[info] [1/1] Connecting to resources on the server (192.168.00.00:00000)...
[info] Establishing links to the resources...
[info] KT AI Accelerator is ready to use.
```

이후 PyTorch 프로그램이 실행되면서 GPU 연산을 요청하면 이것을 원격에 위치한 GPU에 오프로딩(offloading)하게 됩니다. VM은 resource farm과 전용 네트워크로 연결되어 있으며 그 외의 물리적인 장치를 사용하지 않습니다.

AI 가속기의 사양이 높아지면 PyTorch 프로그램을 실행하기 위해 수~수십 개의 GPU를 동시에 사용할 수도 있습니다. 하지만 사용자는 이를 위해 PyTorch 프로그램을 DataParallel, DistributedDataParallel 등을 사용해 병렬화할 필요가 전혀 없습니다. AI 가속기에서는 단일 GPU를 위한 PyTorch 프로그램을 실행하면 됩니다. Hyperscale AI Computing 컴파일러가 자동으로 연산 작업을 병렬화하여 여러 GPU 자원에서 분산 처리합니다.

---

**Q. Hyperscale AI Computing 서비스는 일반 GPU 서버와 어떤 차이점이 있나요?**

**A.** Hyperscale AI Computing 서비스는 물리 GPU를 제공하는 대신 “KT AI Accelerator”라는 가상의 AI 가속기를 제공합니다. 기존 GPU 서버에서는 CUDA를 설치하고 CUDA 기반의 PyTorch를 설치하여 GPU를 사용하였습니다. 반면 Hyperscale AI Computing 서비스에서는 KT Cloud가 별도로 제공하는 PyTorch 버전을 사용해야 합니다. 여기에는 GPU 가상화 및 자동 병렬화를 위한 기능이 함께 포함되어 있습니다.

![GPUvsHAC](../image/GPUvsHAC.png)

기존 GPU 서버와 Hyperscale AI Computing 서비스 간의 차이점을 정리하자면 다음과 같습니다.
