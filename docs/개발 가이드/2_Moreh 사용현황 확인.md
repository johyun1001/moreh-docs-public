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

