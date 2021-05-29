from itertools import chain
from nltk.tokenize import word_tokenize, sent_tokenize
import numpy as np
import math

def lsa(sents):

    words = set(chain.from_iterable(sents))
    word_index = {word: k for k, word in enumerate(words)}
    
    num_words = len(word_index)
    num_sents = len(sents)

    # construindo a matriz termo-documento de frequências de palavras
    X = np.zeros((num_words, num_sents))

    for d, sent in enumerate(sents):
        for word in sent:
            w = word_index[word]
            X[w, d] += 1

    # matriz svg
    U, S, Vt = np.linalg.svd(X)

    return sents, U, S, Vt


def summarize_SJ(sents, V, S, k):

    shape_S = S.shape
    length_mat = np.zeros(shape=shape_S)

    for i in range(V.shape[0]):
        length = 0
        for j in range(k):
            length += math.pow(V[j][i], 2)

        length_mat[i] = math.sqrt(length * math.pow(S[i], 2))

    # lista com os índices das sentenças
    sentences_index = []
    length_max = sorted(length_mat, reverse=True)[:k]

    for i in range(k):
        for j in range(len(length_mat)):
            if length_mat[j] == length_max[i]:
                sentences_index.append(j)

    indexes = []

    for sent_index in sentences_index:
        if sent_index not in indexes:
            indexes.append(sent_index)
            print(' '.join(sents[sent_index]))


def main():
    f = open("nasa.txt", 'r', encoding="utf-8")

    # separando as sentenças do documento de texto
    sentences = [word_tokenize(i) for i in sent_tokenize(f.read())]

    # aplicando a técnica do lsa
    sents, U, S, Vt = lsa(sentences)

    print("Qual o tamanho do sumário?")
    k = int(input("Digite um número inteiro entre 1 e {0}: ".format(len(sents) - 1)))
    print()

    if k < 1 or k > 24:
        k = 5

    # aplicando técnica de seleção de sentenças
    summarize_SJ(sents, Vt.transpose(), S, k)


if __name__ == '__main__':
    main()