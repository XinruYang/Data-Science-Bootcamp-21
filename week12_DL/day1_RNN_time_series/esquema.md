Red Neuronal Recursiva en series temporales

1. Analizamos los datos y vemos si se repiten comportamientos a lo largo del tiempo.

2. Definimos el tipo de entrenamiento que vamosa  utilizar:

    2.1. Si los datos no se repiten a lo largo del tiempo (estacionalidad) --> entrenamos el modelo dándole como dato de entrenamiento una parte representativa de todo el conjunto de datos. 
    2.2. Si los datos no se repiten a lo largo del tiempo --> tenemos que entrenar dándole poco a poco todo el conjunto de datos.

3. Repetimos los "step" últimos valores del conjunto de entrenamiento y de test. 

4. Redimensionamos los datos de entrenamiento y de test para que tengan la forma de (Nº Batches, 1, step)
    "step" == "embedding"

5. Entrenamos el modelo usando RNN, Simple RNN, LSTM, etc.

6. Dependiendo del resultado probamos diferentes arquitecturas, tamaño de ventana (step), batch-_size, épocas(...)

7. Nos quedamos con el mejor modelo. 