import scipy
import scipy.spatial
import numpy as np
import matplotlib.pylab as plt
import re


def read_file(path_to_file):
    data = open(path_to_file).read().lower()
    sentences = [filter(lambda w: w != '', re.split('[^a-z]', s)) for s in data.split('\n')]
    # words = re.split('[^a-z]', data)
    # words = filter(lambda w: w != '', words)
    return sentences


def analyze_words(sentences):
    stat = {}
    num = {}
    for s in sentences:
        for w in s:
            if stat.get(w, None) is None:
                stat[w] = 0
            stat[w] += 1
    for i, w in enumerate(stat.keys()):
        num[w] = i
    # print stat
    # print num
    return num


def create_matrix(num, sentences):
    def count(s, w):
        c = 0
        for i in s:
            if i == w:
                c += 1
        return c
    pred_mat = [[count(s, w) for w in num.keys()] for s in sentences]
    # return np.array(pred_mat, dtype=float)
    return pred_mat


def find_cosine(matrix):
    stat = {}
    min1 = 1.0
    ind1 = 1
    min2, ind2 = 1.0, 0
    for i, s in enumerate(matrix):
        if i != 0:
            r = scipy.spatial.distance.cosine(np.array(matrix[0]), np.array(s))
            stat[i] = r
            if r < min1:
                min1 = r
                ind1 = i
    stat[ind1] = 1.0
    for k, v in stat.items():
        if v < min2:
            min2 = v
            ind2 = k
    print min1, ind1, min2, ind2


if __name__ == "__main__":
    sentences = read_file('sentences.txt')
    num = analyze_words(sentences)
    word_matrix = create_matrix(num, sentences)
    find_cosine(word_matrix)

