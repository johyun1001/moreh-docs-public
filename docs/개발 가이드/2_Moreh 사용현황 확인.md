# Moreh 솔루션 사용현황 확인하기

Moreh 솔루션은 꾸준히 업데이트되고 있습니다. 본 문서에서는 Moreh 솔루션을 업데이트하는 방법에 대해서 설명합니다.

기본적으로 Moreh 솔루션은 `update-moreh` 라는 명령어 만으로 업데이트 할 수 있습니다. 기본적으로 해당 명령어 실행시 현재까지 배포된 버전 중 가장 최신버전으로 업데이트 합니다.

```jsx
update-moreh
```

특정 버전으로 업(다운)그레이드 할 수도 있습니다. `--target` 이라는 옵션을 이용하면 됩니다.

```jsx
update-moreh --target 22.10.2 # upgrade
update-moreh --target 22.8.0 # downgrade
```

현재 Moreh 솔루션이 정상적으로 동작하지 않아 동일한 버전으로 다시 Moreh 솔루션을 설치하고 싶은 경우나, 원하는 타켓 버전으로 업(다운)그레이드가 정상적으로 되지 않을 경우 `--force` 옵션을 통해 강제로 Moreh 솔루션의 업데이트를 진행할 수 있습니다.

```jsx
# 22.10.2 버전을 강제 설치
update-moreh --target 22.10.2 --force

# 최신버전으로 재설치
update-moreh --force
```

Client Version과 Server Version이 달라도 update-moreh를 진행해도 Moreh 솔루션은 무리없이 변경된 버전들에서 RM 및 Pytorch 가 무리 없이 정상적으로 동작합니다. 

- (다운)그레이드 해도 server 버전에는 영향을 미치지 않으니 그대로 진행하시면 됩니다.
    
    ![HAC](./image/updatemoreh.png)
    