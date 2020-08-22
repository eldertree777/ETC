[수업자료](https://opentutorials.org/module/4966/28965)

- 회귀와 분류를 구현하는 방법 -> 알고리즘
- 뉴럴 네트워크 알고리즘

- 뉴럴네트워크 = 인공신경망 = 딥러닝
- AI > machine leaning > deep learning


# 머신러닝 프로세스

```python
    # 1. 과거의 데이터를 준비합니다.
        레모네이드 = pd.read_csv(파일경로)
        독립 = 레모네이드[['온도']]
        종속 = 레모네이드[['판매량']]
        print(독립변수.shape, 종속변수.shape) 


    # 2. 모델의 구조를 만듭니다.
        X = tf.keras.layers.Input(shape=[1])
        Y = tf.keras.layers.Dense(1)(X)
        model = tf.keras.models.Model(X, Y)
        model.compile(loss='mse')

    # 3. 데이터로 모델을 학습합니다.
        model.fit(독립, 종속, epochs=1000) 
        
        #epochs 몇회반복?
        # model.fit(독립, 종속, epochs=1000, verbose=0
        #verbose=0 : 실행결과를 표시 하지 않는다

    # 4. 모델을 이용합니다.
        model.predict(독립)
        model.predict([[15]])
        # model.predict(독립[0:10])
```

# 실습환경  Google Colaboratory
    - jupyter notebook
    - colab notebook

# 표를 다루는 도구 판다스

```python
    import pandas as pd

     #파일들로 부터 데이터 읽어오기
    파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
    레모네이드 = pd.read_csv(파일경로)

    파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
    보스톤 = pd.read_csv(파일경로)

    파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
    아이리스 = pd.read_csv(파일경로)

    #데이터 모양확인
    print(독립변수.shape, 종속변수.shape) 

    # 데이터 모양으로 확인  (행 , 열)
    print(레모네이드.shape)
    print(보스톤.shape)
    print(아이리스.shape)

    print(레모네이드.columns)
    print(보스톤.columns)
    print(아이리스.columns)

    #데이터 분리
    독립 = 레모네이드[['온도']]
    종속 = 레모네이드[['판매량']]
    print(독립.shape, 종속.shape)

    독립 = 보스톤[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax',
        'ptratio', 'b', 'lstat']]
    종속 = 보스톤[['medv']]
    print(독립.shape, 종속.shape)

    독립 = 아이리스[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
    종속 = 아이리스[['품종']]
    print(독립.shape, 종속.shape)

    레모네이드.head()
    보스톤.head()
    아이리스.head()
```

[실습소스코드](https://colab.research.google.com/github/blackdew/tensorflow1/blob/master/practice1-pandas.ipynb)

실습을 통해 배울 도구들

- 파일 읽어오기: read_csv('/경로/파일명.csv')
- 모양 확인하기: 데이터.shape
- 칼럼 선택하기: 데이터[['칼럼명1', '칼럼명2', '칼럼명3']]
- 칼럼 이름 출력하기: 데이터.columns
- 맨 위 5개 관측치 출력하기: 데이터.head()
- 샘플 데이터

- GitHub github link: https://github.com/blackdew/tensorflow1/tree/master/csv
- 레모네이드: https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv
- 보스톤: https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv
- 아이리스: https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv


- model.fit(독립, 종속, epochs=10)
- loss = (예측 - 결과)^2
- import 라이브러리 as 불러올변수
- x = tf.keras.layers.Input(shape=[독립변수 칼럼수])
- y = tf.keras.layers.Dense(종속변수 칼럼수)(x)

- weight , bias

## 모델의 수식 확인
- model.get_weights()

- [deeplearning workbook](https://docs.google.com/spreadsheets/d/11DAONRZ92ob0T0YRIT5KgU9vNeO28bYNvteu_-fbRV0/edit#gid=0)


# 분류형 (분류 예측)

- 원핫잇코딩(수치화)
- 인코딩 = pd.get_dummies(아이리스)

```py
# 모델의 구조를 만듭니다.
x = tf.keras.layers.Input(shape = [4])
y = tf.keras.layers.Dense(3, activation='softmax')(x)
model = tf.keras.models.Model(x,y)
model.compile(loss = 'categorical_crossentropy' , metrics = 'accuracy')
```
- softmax : 0,1으로 값을 만듬


# 히든레이어

```py
X = tf.keras.layers.Input(shape=[13])
H = tf.keras.layers.Dense(10,activation = 'swish')(X)
Y = tf.keras.layers.Dense(1)(H)
model = tf.keras.models.Model(X,Y)
model.compile(loss='mse', metrics = 'accuracy')
```
