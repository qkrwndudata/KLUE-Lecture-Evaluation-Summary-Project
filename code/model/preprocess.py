from pykospacing import Spacing
import pandas as pd
import re
import urllib.request
import nltk
nltk.download('punkt')

class Preprocess:
    def list_to_df(self, klue_list):
        col_name = ['eval']
        klue = pd.DataFrame(klue_list, columns=col_name)
        return klue


    def klue_NULL_check(self, eval):
        eval.replace("", float("NaN"), inplace=True)
        return eval.isnull().values.any()


    def klue_drop_na(self, eval):
        eval.dropna(inplace=True)


    def lower(self, text):
        result = text.lower()
        return result


    def klue_lower(self, eval):
        lower_corpus = []
        for sent in eval:
            lower_corpus.append(self.lower(sent))

        klue['evaluation_low'] = lower_corpus

        return klue


    def klue_dict_sub(self, eval_low):
        grades = {"A": "에이", "A0": "에이", "A+": "에이플러스", "에이쁠": "에이플러스", "에이플": "에이플러스", "에이플러스": "에이플러스", "B": "비",
                  "B0": "비", "B+": "비플러스", "비쁠": "비플러스", "비플": "비플러스", "비 플러스": "비플러스", "C0": "씨",
                  "C": "씨", "C+": "씨플러스", "씨쁠": "씨플러스", "씨플": "씨플러스", "씨 플러스": "씨플러스", "에제": "에이", "에쁠": "에이플러스"
                  }

        replace_words = {
            "take home exam": "비대면 시험", "take-home exam": "비대면 시험", "ppt": "자료", "pdf": "자료", "ㅜㅜ": "", "ㅠㅠ": "", "ㅜ": "",
            "ㅠ": "", "5:5비율로": "반반으로",
            "t/f": "참 혹은 거짓", "캠": "카메라", "cpa, 씨파": "공인회계사시험", "o": "함", "x": "안함", "칼절평": "절대평가", "절평": "절대평가",
            "상평": "상대평가",
            "굿": "좋다", "잼관": "재무관리", "갓": "매우 좋으신", "줌, zoom, collaborate, 콜라보레이트, 칼투라, kaltura": "온라인 강의 플랫폼",
            "미디언": "중위수", "q1": "제1사분위수", "q3": "제3사분위수",
            "꿀강": "편한 강의", "띵강": "명강의", "헬강": "힘든 강의", "capm": "자본자산가격결정모형",
            "치팅시트": "참고 노트", "치팅페이퍼": "참고 노트", "오픈북": "참고 노트", "오픈 북": "참고 노트", "open book": "참고 노트",
            "flipped class": "쌍방향 소통 수업", "k-mooc": "온라인 수업", "mooc": "온라인 수업",
            "에이": "좋은 학점", "에이플러스": "좋은 학점", "비": "평범한 학점", "비플러스": "평범한 학점", "씨": "나쁜 학점", "씨플러스": "나쁜 학점",
            "peer review": "동료 평가", "case study": "사례 분석", "ipo": "기업평가",
            "r": "통계 프로그램", "spss": "통계 프로그램", "sas": "통계 프로그램", "sql": "통계 프로그램", "r studio": "통계 프로그램",
            "hbr": "경영학 잡지", "%": "퍼센트", "프로": "퍼센트", "퍼": "퍼센트",
            "ot, 오티": "오리엔테이션", "pg": "쪽", "page": "쪽", "essay": "에세이", "youtube": "유튜브", "q&a": "질의응답", "qna": "질의응답",
            "p/f": "합격 또는 불합격", "페논페": "합격 또는 불합격", "pass": "통과",
            "5:5": "반반", "1학년": "일학년", "2학년": "이학년", "3학년": "삼학년", "4학년": "사학년", "테뱅": "기출문제", "테스트뱅크": "기출문제",
            "비추": "추천 안함", "스윗": "친절한", "워크로드": "공부량", "work load": "공부량", 'b2b': '기업 대 기업'
        }

        grades_temp = {r'(\b){}(\b)'.format(k): r'\1{}\2'.format(v) for k, v in grades.items()}  # \b: 단어 경계와 일치
        replace_temp = {r'(\b){}(\b)'.format(k): r'\1{}\2'.format(v) for k, v in replace_words.items()}

        klue['evaluation_dict'] = eval_low.replace(grades_temp, regex=True)
        klue['evaluation_dict'] = klue['evaluation_dict'].replace(replace_temp, regex=True)

        return klue


    def text_cleaning(self, text):
        hangulenglish = re.compile('[^ \!0-9\u3131-\u3163\uac00-\ud7a3]+')  # 한글과 숫자 제외한 모든 글자
        result = hangulenglish.sub('', str(text))  # 해당 글자 공백으로 대체
        return result


    def klue_kor_only(self, eval_dict):
        cleaned_corpus = []
        for sent in eval_dict:
            cleaned_corpus.append(self.text_cleaning(sent))

        klue['evaluation_kor'] = cleaned_corpus
        return klue



    def klue_space(self, eval_kor):
        spacing = Spacing()

        spaced_corpus = []
        for sent in eval_kor:
            spaced_corpus.append(spacing(sent))

        klue['evaluation_spaced'] = spaced_corpus
        return klue

    def klue_preprocess(self, klue):
      klue = self.klue_lower(klue['eval'])

      eval_low = klue['evaluation_low']
      klue = self.klue_dict_sub(eval_low)

      eval_dict = klue['evaluation_dict']
      klue = self.klue_kor_only(eval_dict)

      eval_kor = klue['evaluation_kor']
      klue = self.klue_space(eval_kor)

      return klue['evaluation_spaced'].to_list()

if __name__ == "__main__":
    prepro = Preprocess()
    klue = prepro.list_to_df(klue_list)
    print(prepro.klue_preprocess(klue))