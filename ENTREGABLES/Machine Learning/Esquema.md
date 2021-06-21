Machine Learning 

1. Datos. Detectar el tipo de problema:
    - Clasificación (LogisticRegression, SVC, Knn, Decission Tree Clasificator, Random Forest Classificator,...)
    - Regresión ( Regresion Lineal, non-linear Polinómica, SVR, Decission Tree Regressor, Random Forest Regressor,...)

2. EDA: Data Wrangling:
    - WebScraping, API, Json, CSV, BBDD (SQL/NoSQL), WEB
    - Correlaciones
    - Feature Engineering (Extracción de características): outliers, regex, NaNs, distribuciones, estandarizar(acercar la media a cero y la desviación típica a 1), normalizar, encoding (dummies)
    - Visualizar los datos para entender
    - Columnas agregadas: media de otras columnas numércas
    - Ponderaciones de columnas (dar más peso al valor de una columna)
    - Eliminar columnas colineales

3. Maquetar los datos para poder hacer el train y el test (X, y) --> Partir los datos en un conjunto de entrenamiento y de test. Elegimos un % de train y test y semilla. 

4. Cross validation --> con el objetivo de saber cómo es el comportamiento de mi modelo para mis datos. (Nos da una primera aproximación para ver si mi modelo funciona, nos da una primera visión de los datos)

5. GridSearch & Pipeline (RECOMENDACIÓN!!: NO PROBAR MÁS DE UN ALGORITMO A LA VEZ. UNA VARIABLE CON EL GRIDSEARCH POR CADA ALGORITMO)

6. Nos quedamos con el mejor modelo y probamos el score con el conjunto de TEST. Nos quedamos con el qe mejor generalice.
    - GridSearch nos da el score solo con el conjunto de entrenamiento, hay que probarlo también con el de test. 

7. Guardamos para futuras pruebas y estar relajados. 

# if i % 1000 == 0:
#    pickle.dump(model, open(path + "model"))
# para guardar cada 1000 iteracciones

8. Entrenamos con todos los datos .fit(X,y)
Es decir, una vez probado todo lo que tenemos que probar, lo que tenemos que hacer es un --> model.fit(X, y) --> Si  nos sale un peor score, volver a empezar y cambiar los detalles e intentar encajar con el conjunto de test que tienen ellos. 



