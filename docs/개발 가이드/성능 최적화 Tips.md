# 성능 최적화 Tips


### 1. 자동 병렬화가 효율적으로 되지 않을 경우

Moreh의 딥러닝 컴파일러는 Multi GPU 환경에서 자동으로 연산을 병렬화하여 실행합니다. 기본적으로 어떤 종류의 연산이 들어와도 최대한의 parallelism을 찾아내도록 구현되어 있으나, 연산 패턴이 다소 복잡할 경우 불필요한 통신이 추가되어 성능이 저하될 수 있습니다.

이와 같은 문제를 피하기 위해서는 컴파일러가 이해하기 쉬운 형태로 모델을 구성해야 합니다. 보통의 경우 가장 쉬운 방법은

**모든 텐서의 outermost dimension(stride가 가장 큰 dimension)이 항상 batch dimension이 되도록**

연산들을 구성하는 것입니다. 예를 들어 전달해주신 test.py의 연산의 경우, 아래 연산부가 문제가 되었습니다.

qkv = qkv.permute((4,0,2,1,3)) # b n h d qkv -> qkv b h n d

queries, keys, values = qkv[0], qkv[1], qkv[2]

여기서 qkv를 permute 할 때, outermost dimension이 batch dimension이 아니게 되어 불필요한 통신이 발생한 것을 파악했습니다. 이를 회피하기 위해서는 다음과 같이 코드를 수정해주면 됩니다.

qkv = qkv.permute((0,4,2,1,3)) # b n h d qkv -> b qkv h n d

queries, keys, values = qkv[:,0,:], qkv[:,1,:], qkv[:,2,:]

### 2. 연산이 충분히 크지 않을 경우

3xLarge 모델의 경우 device 24개를 사용하는 모델입니다. 때문에 batch size가 충분히 크지 않은 경우 GPU Underutilization 문제가 발생할 수 있습니다.

예시로 드신 모델규모/batch size들은 3xLarge model에서 실행하기에는 다소 작은 것으로 보입니다(이 부분은 교수님께서도 이미 의심(?)하셔서 batch size를 직접 키워보신 것 같은데, 이때는 1번 문제때문에 scalable한 성능이 나오지 않았을 것 같습니다).

모델의 다른 파라미터(emb_size 등)를 수정하지 않고 3xLarge 모델을 돌릴 경우, batch size를 24576까지 키울 수 있는 것으로 보입니다. 혹시 batch size를 많이 키울수 없을 경우는 다른 모델 파라미터를 키워보시기 바랍니다.

### 3. relaxed-fp32 옵션 사용

현재 Nvidia GPU 기반 PyTorch의 경우, fp32로 모델을 구성하여 실행하더라도 내부적으로 TF32 연산을 섞어서 사용하도록 구현되어 있습니다.

이와 유사하게, Moreh framework도 throughput 향상을 위해 자동으로 bf16 연산을 섞어서 사용하도록 하는 옵션을 제공하고 있습니다. 이 옵션은 기본적으로 disable 되어있으며, enable하기 위해서는 스크립트 시작 부분에 아래와 같이 적어주시면 됩니다.

torch.moreh.options.allow_

relaxed_fp32 = True

저희의 지금까지의 경험 상, language model에 대해서는 이 옵션을 사용해도 수렴에 문제가 발생하지 않는 것을 확인했습니다 (타 모델들도 검토중입니다).

### 4. loss를 찍는 문제

Moreh AI Framework는 기본적으로 Frontend(사용자 python process)의 동작과 Backend(GPU cluster)의 동작이 asynchronous하게 돌아갑니다. 때문에  loss를 찍기 전 까지의 process를 파악하는 것은 (예: 예제코드의 tqdm이 화면에 찍어주는 process) 실제 모델 실행 시간을 파악하는 데에 큰 도움이 되지 않습니다. loss가 화면에 찍히는 시점에서의 시간이 실제 유의미한 모델 실행 시간이라고 이해해주시면 될 것 같습니다.

그리고 말씀하신대로 loss를 너무 빈번하게 찍어보면, Frontend와 Backend의 동작 사이에 불필요한 synchronization point들이 생겨서 모델의 전체적인 Throughput을 떨어뜨리게 됩니다.

저희의 경험 상 통상적으로 10~100 iteration마다 loss를 한번 씩 logging하는 식으로

스크립트를 작성하시면, Throughput을 크게 해치지 않고 training 추이를 파악할 수 있습니다.

### 5. 기타

현재 예시로 보여주신 스크립트의 경우, 제가 이해하기로는 일반적인 transformer의 encoder 구조와 크게 다르지 않은 것으로 보입니다. 저희가 현재 huggingface의 LM script에 대해서 성능 검증을 어느 정도 진행하였고, 이를 reference script를 제공하고 있는데요. 혹시 성능을 더 높이셔야 한다면 huggingface model script를 사용하시는 것도 가능한 옵션이 될 것 같습니다.

상기 설명한 내용 중 1~3까지를 반영한 스크립트를 첨부합니다. 제 실험 기준으로, 3xLarge model에 대해 100 iteration, batch size 24576으로 257초 정도의 시간이 걸립니다. 실제 사용하시는 모델은 예제 코드보다 embed_dim등이 더 큰 것으로 보이는데, 이 경우 batch size를 더 작게 주셔도 될 것 같습니다.

추가적인 성능 향상이 필요하시거나, 다른 질문 사항이 있으시면 언제든지 메일 주세요.

## Batch size 조절관련

- "user가 HAC system의 특성을 이해하고 (or manual을 잘 보고) batch size를 잘 늘려서 테스트한 경우"에 발생한 버그
- 최우선순위로 고쳐야 함
- "user가 moreh-switch-model만 하고 batch size를 제대로 늘리지 않은 경우"에 발생한 버그
- 특히 batch size < device count 인 경우
- 해결은 해야 하나 우선순위는 낮음
- user가 이렇게 쓰고 있다고 하면, 정합성 문제와 별도로 이렇게 쓰지 말라고 안내를 하는게 throughput 측면에서도 맞음
- RM-130이나 RM-137등, 외부에 throughput showcase할 용도라면, 이렇게 실험을 하고 있으면 안 됨