### 경량화 & 양자화 
양자화는 모델 경량화의 한 종류입니다. 모델 경량화에는 여러 가지 방법이 있으며, 양자화는 그 중 하나로, 모델의 크기와 메모리 사용량을 줄이고 추론 속도를 향상시키기 위한 기술입니다. 

### 모델 경량화 방법

#### 1. 양자화 (Quantization)
양자화는 모델의 가중치와 활성화를 32비트 부동 소수점에서 8비트 정수 또는 16비트 부동 소수점 등으로 줄이는 방법입니다. 이는 모델의 크기를 줄이고 추론 속도를 높이는 데 사용됩니다.

- **장점**:
  - 모델 크기 감소
  - 추론 속도 증가
  - 메모리 사용량 감소
- **단점**:
  - 정확도 손실 가능성

#### 2. 프루닝 (Pruning)
프루닝은 중요하지 않은 뉴런이나 연결을 제거하여 모델을 단순화하는 방법입니다. 모델의 특정 부분을 제거하여 계산 비용을 줄이고 모델을 더 작게 만듭니다.

- **장점**:
  - 모델 크기 감소
  - 계산 비용 감소
- **단점**:
  - 정확도 손실 가능성 (적절한 프루닝 기준이 필요)

#### 3. 지식 증류 (Knowledge Distillation)
지식 증류는 큰 모델(교사 모델)의 출력을 작은 모델(학생 모델)이 학습하도록 하여 작은 모델이 큰 모델의 성능을 학습하는 방법입니다. 이 방법을 통해 작은 모델이 큰 모델과 유사한 성능을 가질 수 있습니다.

- **장점**:
  - 작은 모델의 성능 향상
  - 경량화된 모델의 정확도 유지
- **단점**:
  - 추가적인 학습 단계 필요

#### 4. 모델 압축 (Model Compression)
모델 압축은 가중치 공유, 저비트 가중치 표현 등을 통해 모델을 압축하는 방법입니다. 다양한 기법을 사용하여 모델의 저장 공간을 줄입니다.

- **장점**:
  - 모델 크기 감소
- **단점**:
  - 구현의 복잡성

### 요약
양자화는 모델 경량화의 한 방법으로, 모델의 가중치와 활성화를 더 작은 비트 수로 표현하여 모델 크기를 줄이고 성능을 향상시키는 기술입니다. 다른 경량화 방법들과 함께 사용하면, 모델의 효율성을 극대화할 수 있습니다. 

#### 경량화의 전체적인 목표는 모델을 더 작게 만들고, 메모리 사용량을 줄이며, 추론 속도를 높이는 것입니다. 이를 통해 리소스가 제한된 환경에서도 고성능의 모델을 실행할 수 있습니다.
 
 
 모델의 매개변수를 32비트 부동 소수점에서 8비트 정수로 변환하는 것은 모델 경량화의 한 방법인 **양자화(Quantization)**입니다. 양자화는 주로 모델 크기를 줄이고, 추론 속도를 높이며, 메모리 사용량을 줄이기 위해 사용됩니다. 

### 비트 수 줄이기: 32비트 부동 소수점에서 8비트 정수로

#### 1. 32비트 부동 소수점 (Float32)
- **부동 소수점**: 소수점을 포함하는 숫자를 표현하는 방식입니다. 
- **32비트**: 총 32비트를 사용하여 하나의 숫자를 표현합니다.
  - **1비트**: 부호 비트 (양수/음수)
  - **8비트**: 지수 비트
  - **23비트**: 가수 비트 (실제 값)

예를 들어, `3.14159` 같은 숫자를 32비트 부동 소수점으로 표현할 수 있습니다.

#### 2. 8비트 정수 (Int8)
- **정수**: 소수점을 포함하지 않는 숫자를 표현하는 방식입니다.
- **8비트**: 총 8비트를 사용하여 하나의 숫자를 표현합니다.
  - **8비트**: 부호 있는 정수의 경우 -128부터 127까지의 값을 가질 수 있습니다.

예를 들어, `3` 같은 숫자를 8비트 정수로 표현할 수 있습니다.

### 양자화 과정

1. **32비트 부동 소수점 모델 준비**
   - 원본 모델은 대부분 32비트 부동 소수점 형식의 가중치를 가집니다.

2. **양자화 스케일 및 제로 포인트 계산**
   - 모델의 가중치를 8비트 정수로 변환하기 위해 스케일과 제로 포인트를 계산합니다.
   - **스케일**: 실수 범위를 8비트 정수 범위에 매핑하기 위한 비율.
   - **제로 포인트**: 실수 범위에서 0에 해당하는 정수 값.

3. **가중치 변환**
   - 각 가중치 값을 스케일과 제로 포인트를 사용하여 8비트 정수로 변환합니다.

### 예시

#### 원본 가중치 (32비트 부동 소수점)
```python
import numpy as np

float32_weights = np.array([0.1, 0.5, 0.9, -0.3, -0.7, 1.2], dtype=np.float32)
```

#### 양자화 스케일 및 제로 포인트 계산
```python
min_value = np.min(float32_weights)
max_value = np.max(float32_weights)

# 8비트 정수 범위는 -128 ~ 127
qmin = -128
qmax = 127

# 스케일 계산
scale = (max_value - min_value) / (qmax - qmin)

# 제로 포인트 계산
zero_point = qmin - (min_value / scale)
zero_point = int(zero_point)
```

#### 8비트 정수로 가중치 변환
```python
int8_weights = ((float32_weights / scale) + zero_point).astype(np.int8)
```

이제 `int8_weights`는 원본 `float32_weights`의 8비트 정수 표현입니다.

### 전체 과정 요약
1. **원본 모델의 가중치**는 32비트 부동 소수점 값으로 되어 있습니다.
2. **양자화**를 통해 각 가중치 값을 8비트 정수 값으로 변환합니다. 이를 위해 **스케일**과 **제로 포인트**를 계산합니다.
3. **8비트 정수** 값으로 변환된 가중치로 모델을 저장하면, 모델 크기가 줄어들고 메모리 사용량이 감소하며 추론 속도가 빨라질 수 있습니다.

이 과정을 통해 모델의 크기를 줄이고, 특히 모바일 디바이스와 같이 자원이 제한된 환경에서 모델의 성능을 향상시킬 수 있습니다.


1. 모델 선택 및 경량화
1.1 LLM (Large Language Model)
모델 선택: LLaMA, DistilBERT, TinyBERT 등 경량화된 언어 모델 중 하나를 선택할 수 있습니다.

LLaMA: Meta AI에서 제공하는 대형 언어 모델로, 커스터마이징과 경량화가 가능.
DistilBERT: BERT의 경량화 버전으로, 더 작은 크기와 빠른 속도를 자랑.
TinyBERT: 또 다른 경량화된 BERT 모델.
경량화 방법:

양자화: 모델의 가중치를 32비트 부동 소수점에서 8비트 정수로 변환.
프루닝: 중요하지 않은 뉴런과 연결을 제거하여 모델 크기를 줄임.
지식 증류: 큰 모델의 지식을 작은 모델로 전이하여 학습.

### 양자화 후 튜닝 (Post-Training Quantization and Tuning)

양자화 후 튜닝은 모델을 양자화한 후 성능 저하를 최소화하기 위해 대표적인 데이터셋을 사용하여 모델을 재조정하는 과정입니다. 이는 양자화로 인한 정밀도 손실을 보완하기 위한 방법입니다.

#### TensorFlow Lite 양자화 후 튜닝

1. **양자화 후 튜닝**: 모델을 양자화한 후, 대표적인 데이터셋을 사용하여 모델을 다시 튜닝합니다. 이 과정은 양자화로 인해 손실된 모델 성능을 회복하는 데 도움을 줍니다.

```python
import tensorflow as tf

# 모델 로드
converter = tf.lite.TFLiteConverter.from_saved_model("path/to/saved_model")
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# 대표 데이터셋 설정
def representative_dataset():
    for _ in range(100):
        yield [np.random.rand(1, 224, 224, 3).astype(np.float32)]  # 입력 형태에 맞게 수정

converter.representative_dataset = representative_dataset

# 양자화 후 튜닝 수행
tflite_model = converter.convert()

# 양자화된 모델 저장
with open("model_quantized.tflite", "wb") as f:
    f.write(tflite_model)
```
### LoRa VS 양자화 후 튜닝 

### LoRa (Low-Rank Adaptation)

LoRa는 모델의 적응을 위한 기법으로, 특히 대형 언어 모델(LLM)을 효율적으로 미세 조정(Fine-Tuning)하기 위한 방법입니다. LoRa는 대형 모델의 특정 부분에 저차원 행렬을 추가하여 모델을 적응시키는 방법입니다. 이 방법은 모델의 전체 가중치를 업데이트하는 대신, 일부 중요한 부분만 업데이트하여 미세 조정의 효율성을 높입니다.

#### LoRa 개념

1. **저차원 행렬 추가**: 대형 모델의 일부 가중치 행렬에 저차원 행렬을 추가하여 모델을 적응시킵니다.
2. **효율적인 미세 조정**: 전체 모델을 다시 학습시키지 않고, 특정 부분만 업데이트하여 적응 속도와 효율성을 높입니다.

### 차이점 요약

1. **양자화 후 튜닝**:
   - **목적**: 양자화로 인한 성능 저하를 최소화.
   - **방법**: 대표 데이터셋을 사용하여 모델을 재조정.
   - **사용 사례**: 모델 경량화 후 성능 유지.

2. **LoRa (Low-Rank Adaptation)**:
   - **목적**: 대형 모델의 효율적인 미세 조정.
   - **방법**: 모델의 특정 가중치에 저차원 행렬 추가.
   - **사용 사례**: 대형 언어 모델의 빠른 적응 및 미세 조정.

따라서, 양자화 후 튜닝은 양자화된 모델의 성능을 유지하기 위한 방법이고, LoRa는 대형 모델을 효율적으로 미세 조정하기 위한 방법입니다. 두 방법은 서로 다른 목적과 상황에서 사용됩니다.
