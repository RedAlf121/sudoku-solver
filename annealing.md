# 🔥 Simulated Annealing

El recocido o temple simulado es un algoritmo de optimización ⚙️. Es una forma de buscar la mejor solución cuando no se tiene una forma de calcular de forma lineal 📉.

Este algoritmo está inspirado en un proceso para trabajar metales llamado Annealing 🧊🔩.

## 🧪 Contexto desde la física

Cuando se quiere eliminar tensiones de un metal, se hace lo siguiente:  
Se calienta el metal a una alta temperatura 🌡️ (sin caer en la temperatura de fusión que lo derrite)  
Y luego se va dejando enfriar poco a poco ❄️ hasta que llega a temperatura ambiente 🌬️.  
Eso hace que el metal sea maleable y se faciliten procesos en frío como cortar ✂️, doblar 🔧, etc.  
En teoría, el metal estaría en su estado óptimo ✅.

### ❓ ¿Y por qué ocurre eso?

Sucede que el metal, al estar a altas temperaturas, los átomos del metal se empiezan a mover de forma arbitraria 🔀.  
Al irse enfriando comienzan a agruparse 🧲 ya que el aumento de la temperatura no es 100% parejo.  
Por la propia forma del metal, no son exactamente iguales las temperaturas.  
Como no son iguales, hay átomos que se van a enfriar más rápido y se van a agrupar con otros, lo que crea una estructura que le dicen granos cristalinos 🧊✨.

### 💻 ¿Y ahora qué tiene que ver todo eso con programación?

¡Bastante! La idea es tomar ese proceso y hacer algunas analogías 🔄:  

 El metal sería el problema 🧩. Queremos buscar el estado óptimo 🥇.  
 Los átomos serían cada uno de los estados 🔢.


Entonces, teniendo eso:  

 Al subir la temperatura 🔥 vamos a aceptar cualquier tipo de estado prácticamente.  
 Porque en este contexto, la temperatura define el grado de libertad con el que vas a probar estados 🎲.  
 A medida que baje la temperatura, vas a ser más conservador 🧊.


Vas comparando con una función que es la que vas a optimizar 📈.  
Para tomar un estado, compruebas si es mejor que el que ya tenías ✅.  
En caso de que no, vas a darle un chance según una tolerancia 🎯.  
En este caso usan una distribución llamada distribución de Boltzmann 📊,  
donde evalúan esa tolerancia según esta expresión:
e^(-delta/T)


 delta es la diferencia entre lo que da la función en el nuevo estado y en el actual 🔁.


Perfectamente puede ser otra función, pero esta es la que más se relaciona al fenómeno físico 🧠.  
Lo importante es que sea una función que crezca al inicio y vaya decreciendo lentamente hasta hacer una asíntota 📉.  
También importante que la función esté entre 0 y 1 🔢.  
Según esa tolerancia, vas a probar quedarte con ese valor 🧪.

🧩 Vale, muchas vueltas y ¿dónde está el sudoku?

Para aterrizar con un ejemplo real vamos a usar el sudoku 🧠.  
Primeramente, resolver un sudoku no es una función que se pueda optimizar directamente. Hay que ponerse creativos 🎨.

Lo que se puede hacer es contar la cantidad de errores ❌.  
Si yo pongo un número, no puede ser cualquier número.  
Tiene que evitar repetirse en la misma columna 📊, fila 📈 y en el cuadrante 📦 donde pusiste ese número.  
Entonces, si el número que colocas en una casilla no es el que va... ¡pues tienes un error! 🚫

Entonces conseguido ✅: ya convertimos el problema de resolver el sudoku en un problema de optimización.  
¿Cómo minimizar la cantidad de errores? 🎯

Ahora, teniendo la función a optimizar, queda crear los estados o vecinos (también se les dice así) 🤝.

En este caso hay que usar la aleatoriedad 🎲:  

 Primero se rellena el tablero con números arbitrarios 🔢, no importa que uno se equivoque.  
 Ya ese es un estado y un punto de partida 🛫.  
 Ahora, para generar un vecino, se buscan todas las casillas que se pueden modificar 🧮, en las que no vino un número por defecto  
 se toma una posición cualquiera y se le pone un número 🔄.
Ya con eso se tiene todo listo ✅ solo queda subirle la temperatura 🔥 y a que se cocine la solución 🍳.
```python
def solveSudoku(mat, time_step=0):
    temperature = 100
    initial = init(mat)
    score = cost_function(initial)
    i = 1
    voids = modified(mat)
    print_sudoku(initial)
    print('\n')
    if time_step != 0:
        time.sleep(time_step)
    while score != 0 and temperature > 0.1:
        neighbor = generate_neighbor(initial, voids)
        print_sudoku(neighbor)
        print('\n')
        if time_step != 0:
            time.sleep(time_step)
        neighbor_score = cost_function(neighbor)

        delta = score - neighbor_score
        print(f"delta: {delta} temperature: {temperature}")
        if delta > 0 or random.random() < exp(delta / temperature):
            initial = neighbor
            score = neighbor_score

        temperature *= 0.999
        i += 1
        if i == 1000:
            initial = init(mat)
    return initial
```

Acá por ejemplo se prueba con 100, puede ser con cualquier otro número.  
Entonces normalmente en estos algoritmos se prueban varias iteraciones 🔁 porque no se sabe a veces cuándo es que se debe parar. ¡No es el caso! 😎 porque aquí estamos seguros que el estado final es cuando lleguemos a 0 🎯.


Ahora la idea es que cuando se resten las funciones se mira si es mayor, como ya restamos podemos comparar si delta dio mayor que 0 o no.  
Y si no, pues todavía está la opción de darle un chance 🎲.

El valor de 0.999 con el que se baja la temperatura es ajustable 🔧. Puedes probar con cualquier otro número para ver cómo afecta el rendimiento.


Y eso sería todo de cómo funciona el algoritmo de recocido simulado 🧊🔥.  
Es un algoritmo que depende mucho de si se tiene mucha información 📚 porque es bastante lento en cuanto a iteraciones 🐢.  
Si lo comprueban, es más lento que el mismo de backtracking 🧠.  
Es más útil cuando se tiene una función muy complicada de llegar a un punto, o si te interesa llegar a un punto óptimo pero tampoco tanto, ya que usa mucha aleatoriedad 🎰.

También es importante cómo ajustas la temperatura 🌡️, cada cuánto baja ⏳, cómo buscas los diferentes estados 🧭 — todo eso influye en la cantidad de iteraciones que termina haciendo tu algoritmo de recocido ♻️.
