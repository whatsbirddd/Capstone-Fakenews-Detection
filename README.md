# 📃capstone-fakenews-detection


## 🔍가짜 뉴스 탐지 프로젝트

- 가짜 뉴스의 다양한 정의 중 Incongruent News인 제목과 본문의 불일치 데이터를
추출하는 알고리즘을 개발

- 데이터셋 : Training Data (100,000개) / Validation Data (25,000개) / Test Data ( 25,000개)
  - Label : 1 (Fake), 0 (Real)

- Experiement
  - EDA
  - word embedding : word2vec, FastText, Glove
  - model : LSTM, CNN, bi-LSTM & attention, stacked RNN & attention, 3-CNN, BERT
  - hyper-parameter tuning
  - 샘플 데이터 제작 및 테스트
      - 목적 : 기존에 학교에서 받은 데이터셋은 굉장히 쉬운 문제들로 이루어져있다고 생각함. 어려운 문제에 대해 얼마나 해결할 수 있는지를 테스트하기 위해 샘플 데이터를 제작함.
      - 방법
          - 핵심 키워드는 동일하지만 뉘앙스가 다른 제목과 본문
          - 본문을 앞/중간/뒤 부분으로 나누어 다른 내용으로 섞어서 제작
          - 핵심 키워드는 동일하지만 긍/부정을 다르게 하여 제작
  - 합성 데이터셋 제작 및 모델 추가학습

      ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/acad9765-4190-4caa-8c7b-4d2fc22b947a/Untitled.png)

      - 참고 자료 : [https://jiho-ml.com/weekly-nlp-37/](https://jiho-ml.com/weekly-nlp-37/)
      - 25000개의 가짜뉴스 제작 : validation accuracy는 약간 떨어졌지만, 샘플 데이터에 대한 정답 비율은 높아짐. 기존 데이터셋으로 학습이 잘 된 모델에 효과적이었음.(lstm, bert)
  - 웹 서비스 개발
      - flask사용
