
# Creational Patterns
Apuntes sobre el sitio [https://refactoring.guru/design-patterns/python] y el video asignado

## Builder

- Necesario un Director, se encarga de lo que necesita hacer con el producto.
- Guardar un objeto aplicando una función haciendo un resguardo
- Ver ejemplo en: builder.py

## Factory
-  Darle un nombre y da la clase especifica de lo que necesito.
-  En lugar de crear instancias de clases directamente en el código cliente, se utiliza una "fábrica" para manejar la creación de objetos.
- Ver ejemplo factory.py

## Prototype

- Permite copiar objetos existentes en lugar de crear nuevos objetos desde cero. Este patrón es útil cuando la creación de un objeto es costosa o compleja, y se prefiere hacer una copia de un objeto existente en lugar de construir uno nuevo.
- Copy vs DeepCopy: el copy, copia el primer nivel:
	- En el caso de tener una lista= [1,2,3,4 [88,99,100], 9]
		Al hacer el copy se obtiene los numeros y la referencia que esta dentro de la lista.
	- En el deepcopy si se obtiene toda la lista.


# Structural Patterns
## Decorators

- Añadir funcionalidades a un objeto de manera dinámica y flexible sin modificar su estructura.
- Una función que engloba o atrapa otra funcion hace codigo antes de llamar la función base y por ultimo llama a la función base

## Singleton
- Asegura que una clase tenga una única instancia y proporciona un punto de acceso global a esa instancia.

## Proxy
- Describen un objeto pero en tiempo de ejecución de ejecución aún no existe. 
- Sirva para ver cosas que van a existir en un momento

# Behavior Patterns

## Chain of Responsibility

- Permite pasar una solicitud a lo largo de una cadena de manejadores. Cada manejador en la cadena tiene la oportunidad de procesar la solicitud o de pasarla al siguiente manejador en la cadena.
-  Ver ejemplo chain_repon.py

## Command

- Se puede ver en django:  al usar migrate o makemigrations
## Iterador 

- Procesar datos muy pesados y se procesan por pedasos
- Permite recorrer una colección de elementos sin exponer su representación interna

## Observer

- Define una relación de dependencia uno a muchos entre objetos. Cuando un objeto cambia de estado, todos sus dependientes (observadores) son notificados y actualizados automáticamente.

### Otras notas
- Decoradores: implementar cosas sobre funciones