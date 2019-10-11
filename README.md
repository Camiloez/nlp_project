# Estado de avance del proyecto



## 1. Baseline

En el subdirectorio baseline/ en un archivo .ipynb se implemento el modelo de trigramas con interpolación lineal, los hiparámetros del modelo se calibraron en el conjunto de validación y la mejor configuración se probó en test obtuviendo un perplexity igual a **194.56**.

### 2. Dataset

Al tokenizar usanto str.split() se pierde alrededor de un 4% de los tokens en los tres datasets y un
0.04% del vocabulario, como la perdida de información es poco significativo se procedió a trabajar con el dataset en este estado.


https://blog.einstein.ai/the-wikitext-long-term-dependency-language-modeling-dataset/
