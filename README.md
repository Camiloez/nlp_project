# Estado de avance del proyecto



## 1. Baseline

En el subdirectorio baseline/ en un archivo .ipynb se implemento el modelo de trigramas con interpolación lineal, los hiparámetros del modelo se calibraron en el conjunto de validación y la mejor configuración se probó en test obtuviendo un perplexity igual a **194.56**.

### 2. Dataset

Al tokenizar usanto str.split() se pierde alrededor de un 4% de los tokens en los tres datasets y un
0.04% del vocabulario, como la perdida de información es poco significativo se procedió a trabajar con el dataset en este estado.


https://blog.einstein.ai/the-wikitext-long-term-dependency-language-modeling-dataset/


### 3. Codigo Proyecto

El codigo del proyecto se encuentra funcionando en codigo_proyecto/train_GCNN.ipynb,
ejecutar las celdas en orden y ver al final al entrenar que a los 50 epochs aprox el perplexity baja cercano a 70-80.
Se recomienda mucho usar GPU ya que demora mucho.

- El código está casi todo sacado de https://towardsdatascience.com/how-to-build-a-gated-convolutional-neural-network-gcnn-for-natural-language-processing-nlp-5ba3ee730bfb
- Vale la pena revisar ese github
- En config.py están los parámetros, sino se pueden cambiar en el mismo jupyter al inicio, en
params es el diccionario usado.
- Es necesario bajar embeddings de glove https://www.kaggle.com/thanakomsn/glove6b300dtxt
- Notar que se pueden usar otros embeddings, pero es importante que CALCE EL TAMAÑO, si por ejemplo usamos embeddings de tamaño 300 preentrenados (como glove), es importante que el mismo valor se asigne en los párametros a entrenar.

