import pickle
import re

import joblib
from konlpy.tag import Mecab
from tensorflow.keras.preprocessing.sequence import pad_sequences
import collections


def preprocessing(text):
    m = Mecab()

    cleaned_text = re.sub('[^가-힣]', ' ', text)  # 한글과 영어 소문자만 남기고 다른 글자 모두 제거
    tokenized_text = m.morphs(cleaned_text)
    removed_by_len_text = [token for token in tokenized_text if len(token) > 1]
    return removed_by_len_text


# loading
with open('model_data/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

loaded_model = joblib.load('model_data/model_final.pkl')


def process(title, body):
    sample_title = '- 트위터, 코로나에 2분기 이용자 늘고 매출은 줄어'
    sample_body = '트위터가 신종 코로나바이러스 감염증 사태가 끝난 뒤에도 직원들이 근무 시간의 절반 정도는 재택근무를 하도록 허용하기로 했다고 경제매체 CNBC가 9일 보도했다. 보도에 따르면 트위터는 최근 직원들에게 사무실로 복귀해도 안전한 때가 된 뒤에도 재택근무를 할 수 있도록 더 많은 융통성을 주겠다고 통지했다. 새 지침에 따르면 모든 트위터 직원은 근무 시간의 절반 미만 범위에서 재택근무를 할 수 있다. 또 직원들은 부서장에게 풀타임으로 재택근무를 하도록 승인해달라고 요청할 수 있고, 급여를 조정하는 조건으로 다른 지역으로 이사할 수도 있다. 다만 데이터센터 관리직 같은 일부 직무는 계속해서 일터로 출근해야 한다. 트위터는 앞서 미국 직원들에게 최소한 내년 1월까지 재택근무를 하게 될 것으로 예상하라고 밝힌 바 있다. 트위터 대변인은 "우리가 언제 안전하게 일터로 돌아갈 수 있을지에 대해 미리 준비할 수 있도록 직원들에게 옵션을 제공하기 위해 내부적으로 지침을 공유했다"고 말했다. 트위터는 이런 근무 형태를 하이브리드 모델이라고 지칭했다. 소셜미디어 트위터처럼 영구적으로 계속 집에서 일하는 형태보다는 페이스북처럼 부서장 승인 아래 재택근무를 허용하는 형태에 가깝다고 CNBC는 지적했다. 트위터의 직원은 16만6천여명에 달한다.'

    # preprocessing
    preprocessed_title = preprocessing(title)
    preprocessed_body = preprocessing(body)

    # counter
    preprocessed_body_20 = [i[0] for i in collections.Counter(preprocessed_body).most_common(20)]

    # tokenization
    tokenized_title = tokenizer.texts_to_sequences([preprocessed_title])
    tokenized_body = tokenizer.texts_to_sequences([preprocessed_body])

    # padding
    padded_title = pad_sequences(tokenized_title, 10)
    padded_body = pad_sequences(tokenized_body, 415)

    probability = loaded_model.predict([padded_title, padded_body])
    print("score:", probability)

    if probability >= 0.5:
        result = 1
        probability = int(probability*100)
    else:
        result = 0
        probability = 100 - int(probability*100)
    return probability, result, preprocessed_title, preprocessed_body_20
