# -*- coding: utf-8 -*-
import datasets
import pandas as pd
from fastai.text.all import *
from transformers import *
from blurr.data.all import *
from blurr.modeling.all import *
from web_scraping import crawling
from preprocess import Preprocess

class TextSummarize:
    def summarize_1(self, test_article):
        test_article = re.sub('\n', ' ', test_article)
        inf_learn = load_learner(fname='news_summary_100000.pkl')
        return inf_learn.blurr_generate(test_article)

    def summarize_2(self, test_article):
        test_article = re.sub('\n', ' ', test_article)
        inf_learn = load_learner(fname='news_summary_200000.pkl')
        return inf_learn.blurr_generate(test_article)


if __name__ == "__main__":
    text = """"""

    preprocessor = Preprocess()
    url_lst = ["https://klue.kr/lectures/107754",
               "https://klue.kr/lectures/107755",
               "https://klue.kr/lectures/107756"]
    text = crawling(url_lst)

    klue = preprocessor.list_to_df(text)
    print(preprocessor.klue_preprocess(klue))

    # a = TextSummarize()
    # print(a.summarize_1(text))
    # print(a.summarize_2(text))