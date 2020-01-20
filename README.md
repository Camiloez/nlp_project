# Estado de avance del proyecto





## 1. Dataset
El dataset utilizado es el WikiText-103, en el siguiente link se encuentra el dataset y un descripción de este:
https://blog.einstein.ai/the-wikitext-long-term-dependency-language-modeling-dataset/

Al tokenizar usanto str.split() se pierde alrededor de un 4% de los tokens en los tres datasets y un
0.04% del vocabulario, como la perdida de información es poco significativo se procedió a trabajar con el dataset en este estado.

## 2. Baseline

El baseline se encuentra en **baseline/baseline.ipynb**, en donde se implemento el modelo de trigramas con interpolación lineal, los hiparámetros del modelo se calibraron en el conjunto de validación y la configuración que minimiza el perplexity se evaluó en test obtuviendo un perplexity igual a **205.44**.

## 3. Codigo Proyecto

El codigo del proyecto se encuentra funcionando en **codigo_proyecto/train_GCNN.ipynb**, tras 50 epochs de entrenamiento el perplexity baja a 70-80. Se recomienda ejecutar con GPU.

- El código está casi todo sacado de https://towardsdatascience.com/how-to-build-a-gated-convolutional-neural-network-gcnn-for-natural-language-processing-nlp-5ba3ee730bfb
- Vale la pena revisar ese github
- En config.py están los parámetros, sino se pueden cambiar en el mismo jupyter al inicio, en params es el diccionario usado.
- Es necesario bajar embeddings de  https://nlp.stanford.edu/projects/glove/, el archivo es **glove.6B.300d.txt**
- Notar que se pueden usar otros embeddings, pero es importante que CALCE EL TAMAÑO, si por ejemplo usamos embeddings de tamaño 300 preentrenados (como glove), es importante que el mismo valor se asigne en los párametros a entrenar.

## 4. Requerimientos
```
torch 1.3.0
fastai 1.0.59
pandas 0.25.3
numpy 1.17.4
```
