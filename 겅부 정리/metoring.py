import tensorflow as tf
import pandas as pd

파일경로 = ''
레모네이드 = pd.read_csv(파일경로)

# 레모네이드.head()

독립 = 레몬네이드[['온도']]
종속 = 레몬네이드[['판매량']]
print(독립.shape, 종속.shape)

# 모델을 만듭니다.
X = tf.keras.layers.Input(shape=[1]) # 입력 변수 크기 설정
Y = tf.keras.layers.Dense(1)(X)  
# dense(출력변수크기, acvivation=)(입력되는 변수)

model = tf.keras.models.Model(x, y)
model.compile(loss='mse')
model.fit(독립, 종속, epochs=100, verbose=1)

model.predict(독립[0:10])

#X = tf.keras.layers.Input(shape=[13]) // (shape=(13,))
#H = tf.keras.layers.Dense(8, activation='swish')(X)
#H = tf.keras.layers.Dense(8, activation='swish')(H)
#H = tf.keras.layers.Dense(8, activation='swish')(H)
#Y = tf.keras.layers.Dense(1)(H)

# Deanse(unit 출력값 크기, activation 활성화 함수)


#model = tf.keras.modes.Squential()

#pandas에 대한 

#보스턴 집값구하기
#레모네이드
#아이리스품종분류

# https://github.com/eldertree777/tensorflow1/blob/master/%EB%B3%B4%EC%8A%A4%ED%84%B4.ipynb
# https://github.com/eldertree777/tensorflow1/blob/master/%EC%95%84%EC%9D%B4%EB%A6%AC%EC%8A%A4_%ED%92%88%EC%A2%85_%EB%B6%84%EB%A5%98.ipynb
# https://github.com/eldertree777/tensorflow1/blob/master/%ED%91%9C%EB%A5%BC_%EB%8B%A4%EB%A3%A8%EB%8A%94_%EB%8F%84%EA%B5%AC_pandas.ipynb

# tensorflow document layers.Dense
# https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense
# +
# https://han-py.tistory.com/207

# tensorflow document keras.Input
# https://www.tensorflow.org/api_docs/python/tf/keras/Input?version=nightly


# https://www.kaggle.com/

# NN(NEURAL NETWORKS)
# https://tutorials.pytorch.kr/beginner/blitz/neural_networks_tutorial.html


# Activation function  간단정리 사이트
# https://muzukphysics.tistory.com/193
