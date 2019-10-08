import numpy as np
from nltk import bigrams, trigrams
from collections import defaultdict

class Trigrams():
    def fit(self, corpus):
        """
        Ajusta el modelo en el corpus de entrenamiento, guarda los parámetros en atributos.

        Parameters:
            corpus: {list of str}, shape (corpus_size)
            corpus de entrenamiento tokenizado.
        Returns:
            self: object
        """
        ## Crear diccionarios que guardaran la probabilidad de cada n-gram
        model1 = defaultdict(lambda: 0)
        model2 = defaultdict(lambda: defaultdict(lambda: 0))
        model3 = defaultdict(lambda: defaultdict(lambda: 0))

        ## Contar frecuencia de co-ocurrencia
        N = len(corpus)
        for sentence in corpus:
            # Unigrams
            model1[None]=N
            for w1 in sentence:
                model1[w1]+=1
            # Bigrams
            model2[None][None]=N
            for w1, w2 in bigrams(sentence, pad_right=True, pad_left=True):
                model2[w1][w2] += 1
            # Trigrams
            for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
                model3[(w1, w2)][w3] += 1

        ## Transformar conteo a probabilidades
        # Trigrams
        for w1_w2 in model3:
            w1, w2 = w1_w2[0], w1_w2[1]
            total_count = model2[w1][w2]
            for w3 in model3[w1_w2]:
                model3[w1_w2][w3] /= total_count
        # Bigrams
        for w1 in model2:
            total_count = model1[w1]
            for w2 in model2[w1]:
                model2[w1][w2] /= total_count
        # Unigrams
        total_count = sum(model1.values())
        for w1 in model1:
            model1[w1] /= total_count

        self.model1 = model1
        self.model2 = model2
        self.model3 = model3

    def predict_proba_trigam(self, lamb, trigram):
        """
        Calcula la probabilidad de un trigrama usando interpolación lineal.
            - p(w3|w1,w2) = lamb_1*q(w3|w1,w2)+lamb_2*q(w3|w2)+lamb_3*q(w3)
            - lamb>=0, lamb_1+lamb_2+lamb_3=1
        Parameters:
            lamb: {array}, shape =3
            hiperparámetros del modelo, cada componente debe ser positivo y deben sumar 1.

        Returns:
            score: float
            probabilidad del trigrama
        """
        w1, w2, w3 = trigram
        proba = lamb[0]*self.model3[(w1,w2)][w3]+lamb[1]*self.model2[w2][w3]+lamb[2]*self.model1[w3]
        return proba

    def get_perplexity(self, lamb, corpus):

        """
        Obtiene la perplexity del modelo en un conjunto de validación
            -perplexity = exp(NLL/N), donde NLL es la negative-log-likelihood del modelo y
             N el número de trigramas en el corpus.

        Parameters:
            - corpus: {list of str}, shape (corpus_size)
              corpus de validación tokenizado.
            - lamb: {array}, shape =3
              hiperparámetros del modelo, cada componente debe ser positivo y deben sumar 1.
        Returns:
            score: float
            perplexity
        """

        N = 0 #contador de trigramas del conjunto de validación
        NLL = 0 #negative-log-likelihood
        for sentence in corpus:
            for trigram in trigrams(sentence, pad_right=True, pad_left=True):
                trigram_proba = self.predict_proba_trigam(lamb, trigram)
                NLL = NLL - np.log(trigram_proba)
                N = N+1
        perplexity = np.exp(NLL/N)

        return perplexity
