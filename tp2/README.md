# TP2

Para imprimir una matriz en el tp, incluimos el modulo `pandas` que se puede instalar utilizando el script `dependencies.sh`:

``` sh dependencies.sh ```

### Formato de los archivos:

El programa debe recibir por parámetro el path del archivo donde se encuentran los costos entre cada depósito. El archivo debe ser de tipo texto y presentar por renglón, separados por coma un par de depósitos con su distancia.

Ejemplo: "depositos.txt"

```
A,B,54
A,D,-3
B,C,8
...
```

### Ejemplo de invocación:

python3 minimizando_costos.py -f *Path al archivo de ciudades* --file *nombre_del_archivo.txt* 