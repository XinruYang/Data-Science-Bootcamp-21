NO SUPERVISADO:

    1. Algoritmos de clusterización:
        
        - Kmeans: recibe un "k" y busca "k" clusters en los datos.

            - Desventajas: La aleatoriedad a la hora de encontrar esos clusters. 
                Solución: Tenemos que comprobar la inercia y el coeficiente de siluette para encontrar el mejor "k". 

            - Ventajas: Busca los "k" clusters que especifiques.

        - DBSCAN: algoritmo que busca clusters a partir de la densidad de las instancias teniendo en cuenta un épsilon y un "min samples".

            - Desventajas: Problemas si las variables tienen diferentes magnitudes. 
                Solución: Estandarizar/Normalizar.

            - Ventajas: No tiene tan en cuenta la aleatoriedad porque se basa en dos parámetros. 



    2. Algoritmos para reducir la dimensionalidad: 

        - PCA (Principal Component Analysis): Necesita el número de dimensiones al que quiers que disminuya el conjunto de datos original. 

            - Ventajas: permite la entrada de un valor relativo [0, 1] que representa el mínimo porcentaje de información que va a mantener antes de bajar una dimensión. 

        - TSNE:  Necesita el número de dimensiones al que quiers que disminuya el conjunto de datos original. 

            - Desventajas de los dos: Cada vez que bajes una dimensión, pierdes información con respecto a la dimensión superior. 

            - Ventajas de los dos: 
                1. Disminuye la complejidad de computación de los datos.
                2. Si bajas a la dimensión 2 o 3 permite visualizaci´n y podrás encontrar visualmente grupos.
                3. Puedes marcar cuanta información qiueres perder como máximo -> o bien esto o bien a qué dimensión quieres bajar. 
