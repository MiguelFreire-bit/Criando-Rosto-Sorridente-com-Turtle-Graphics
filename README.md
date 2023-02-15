# Objetos Turtle Graphics
Repositório criado para armazenar projeto realizado em um livro técnico

# Objetivo

usar o turtle graphics para ilustrar visualmente conceitos como classe, objeto, método de classe, módulos e etc


## Passo a passo do programa
Primeiramente fiz o importe do módulo Turtle e depois instanciando um objeto Screen. 

Para iniciar a "caneta" instanciei um objeto Turtle chamado de "t". A classe Turtle, definida no módulo turtle, oferece os métodos para movimentar a caneta.

Para movimentar a caneta para uma coordenada específica usa-se o método goto(). o Rosto é feito com a função circle() e os olhos com dot(). A fim de fazer o sorriso usa-se uma variante do método circle() que utiliza um segundo argumento além do raio: um ângulo.



métodos de movimentação usados:

```
t.forward() #frente
t.left() #esquerda
t.right() #direita
```



métodos para levantar e descer a caneta

```
t.penup()
t.pendown()
```

