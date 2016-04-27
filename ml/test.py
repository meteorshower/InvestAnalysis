#coding=utf8

import sys, re, os, xlrd, nltk, random
import jieba as jb
import jieba.posseg as ps
import jieba.analyse as aly
#from nltk.book import *
from nltk.corpus import names
from nltk.classify import apply_features
from nltk.parse import stanford
from nltk.tokenize.stanford_segmenter import StanfordSegmenter
#from nltk.corpus import sinica_treebank
#from snownlp import SnowNLP
# from textblob import TextBlob

reload(sys)
sys.setdefaultencoding('utf8')
#jb.load_userdict('userdict.txt')
#jb.add_word('test', '99999')

def testcase():
    pattern = {}
    sh = xlrd.open_workbook(u'坚守模式.xls').sheet_by_index(0)
    for r in range(sh.nrows):
        for c in range(2,5):
            value = sh.cell_value(r, c)
            words = '\t'.join([word for word, tag in ps.cut(value, HMM=True)])
            tags = '\t'.join([tag for word, tag in ps.cut(value, HMM=True)])
            pattern[tags] = pattern.get(tags, []) + [words]
        #print ' '.join(['%s/%s' % (word, tag) for word, tag in ps.cut(' '.join(sh.row_values(r)[2:]))])
    for p, info in pattern.iteritems():
        print p
        print  '\n'.join(list(set(info)))

#TODO 中文

if __name__ == "__main__":
    testcase()
