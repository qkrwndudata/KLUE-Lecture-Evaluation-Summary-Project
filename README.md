# KLUE 강의 평가 요약 프로젝트

#### 주제: 자연어 처리 기법을 이용해 고려대학교 강의 평가 사이트인 KLUE의 강의별 텍스트 요약을 진행
---

#### 프로젝트 진행 과정
- 전처리:

  1. 크롤링을 통한 데이터 수집 (저작권 문제로 인한 데이터 수집 한계로 최종적으로는 10개 리뷰만을 사용해 성능 확인)
  2. dictionary를 사용해 빈도수 높은 키워드 및 비속어 대체
  3. group by를 사용해 multi document를 long document로 변환
  
- Fine Tuning: 리뷰 텍스트와 가장 비슷하면서 평서문 기반의 abstractive summarization label을 제공하는 데이터 선택

- 모델링: 최종적으로 KoBART를 선정

  1. KoBART
  2. KoT5
  3. BertShared
  
- API 개발:

  1. REST API 구현: Fine tuning 모델 적용
  2. 모델 배포: 포드포워딩을 통해 개인 PC 기반의 모델 배포
  
#### 프로젝트 결과

![image](https://user-images.githubusercontent.com/79184083/224680213-792e085a-4640-4dca-8fcf-c9da70a07743.png)


