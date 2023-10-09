# Curso de TypeScript: Tipos avanzados y funciones

## Configuración del proyecto con ts-node

Acondicionemos nuestro entorno de trabajo con los archivos y configuraciones necesarias para trabajar con TypeScript. Además, haremos uso de la librería ts-node la cual nos va a permitir ejecutar directamente archivos TypeScript en NodeJS sin necesidad de hacer un proceso de transpilación.
Entorno para trabajar con TypeScript

Haciendo empleo de la terminal y un editor de código (utilizaremos Visual Studio Code) realizaremos las configuraciones básicas para poder ejecutar de manera sencilla nuestro código en TypeScript.
Carpeta para nuestro archivos

    Usando la terminal, creamos una carpeta ts-app e ingresamos a la misma

    mkdir ts-app

    cd ts-app

    Abrimos la carpeta en Visual Studio Code mediante la línea de comandos.

    code .

Archivos básicos

Dentro de Visual Studio Code, crearemos los archivos .editorconfig y .gitignore.
Archivo .gitignore

El código dentro de .gitignore lo generaremos usando el website gitignore.io.
Página Gitignoreio - Colocamos como parámetros macOS, Linux, Windows y Node, luego le damos a Crear o Create

Como parámetros colocamos macOS, Linux, Windows y Node. Luego le damos al botón Create. Esto nos generará un archivo como el siguiente:
Página Gitignoreio - Copiamos el código generado y los pegamos en nuestro archivo .gitgnore de nuestro proyecto

Copiamos todo el contenido y lo pegamos dentro del archivo .gitignore.
Archivo .editorconfig

Pegamos la siguiente configuración dentro de .editorconfig:

# Editor configuration, see <https://editorconfig.org>
root = true

[*]
charset = utf-8
indent_style = space
indent_size = 2
insert_final_newline = true
trim_trailing_whitespace = true

[*.ts]
quote_type = single

[*.md]
max_line_length = off
trim_trailing_whitespace = false>

Instalando TypeScript con Node

En la terminal, ejecutemos npm init -y dentro de la ruta de nuestro proyecto para inicializar Node con una configuración por defecto.
Instalación

Lo instalaremos de forma local, es decir, solo para nuestro proyecto:

npm i typescript --save-dev

Versión Descargada

Podemos verificar la versión instalada de TypeScript:

npx tsc --version

Configuración por defecto

Inicialicemos TypeScript con una configuración básica:

npx tsc --init

Ruta del Output

Configuremos la ruta en donde se guardarán nuestros archivos transpilados de TypeScript:

    Vamos al archivo tsconfig.json del proyecto.

    Busquemos el atributo "outDir" y descomentemos esa línea de código de ser necesario:
    Descomentando el atributo outDir del archivo tsconfig.json de nuestro proyecto

    Indicamos que todos los archivos transpilados sean almacenados en una carpeta llamada dist:
    Indicamos que el output sea guardado en una carpeta llamada dist

Para comprobar que esto funciona, vamos a crear una carpeta src y dentro generemos un archivo demo.ts con el siguiente código de ejemplo:

type UserId = string | number;
let userId: UserId;

userId = 'string';
userId = 1;

Transpilación

Ahora ejecutemos mediante la terminal el comando npx tsc para transpilar el código TypeScript. Automáticamente, se nos creará una carpeta dist:
Indicamos que el output sea guardado en una carpeta llamada dist

Es posible también transpilar de forma constante ante cualquier cambio que hagamos en nuestros archivos TypeScript:

npx tsc --watch

Librería ts-node

Esta librería nos permite ejecutar directamente TypeScript en NodeJS. Con esto nos ahorramos el tener que transpilar archivos TypeScript primero y luego ejecutar los archivos transpilados JavaScript con Node.
Instalación de ts-node

Ejecutamos el siguiente comando:

npm install -D ts-node

Antes de pasar a ejecutar nuestro código TypeScript con esta librería, agreguemos console.log('Hoola!' + userId); en nuestro archivo demo.ts:

type UserId = string | number;
let userId: UserId;

userId = 'string';
userId = 1;

console.log('Hoola!' + userId); // 👈

Ejecutando TypeScript con ts-node

Para ello, en la terminal digitamos npx ts-node seguido del nombre del archivo TypeScript a ejecutar o la ruta donde se encuentre dicho archivo dentro de un determinado proyecto:

npx ts-node src/demo.ts

En nuestro caso, nuestro archivo demo.ts se encuentra dentro de la carpeta src.

Coméntanos qué otras configuraciones realizas cuando trabajas con proyectos de TypeScript.

```
npm i nodemon -D
instalar globalmente.
npm i nodemon -g
ponerlo a funcionar y este recibiendo todos los cambios.
nodemon dist
```

## ENUMS

Un enum es un tipo de dato que nos permite crear un set de opciones. Estas opciones son almacenadas bajo una estructura llave-valor similar a un objeto.
Enums en TypeScript

Veamos algunos aspectos de los enums en TypeScript:

    Los declaramos usando la palabra reservada enum seguido del nombre que tendrá este.
    Entre llaves estarán los datos llave-valor.
    Se recomienda que el nombre del enum y de las llaves dentro del mismo estén en mayúscula:

// ENUM
enum ROLES {
	ADMIN = "admin",
	SELLER = "seller",
	CUSTOMER = "customer",
}

// TIPO DE DATO USER
type User = {
	username: string;
	role: ROLES;
}

// CONSTANTE
const nicoUser: User = { // `nicoUser` es del tipo de dato User
	username: 'nicobytes',
	role: ROLES.ADMIN // Le asignamos el rol ADMIN que es uno de los 3 roles disponibles
}

La ventaja que nos da esto es que disponemos de una lista de valores predeterminados que podemos asignar a una variable o a un atributo de la misma. Por tanto, no podemos asignar otro valor que no este dentro de las opciones que nos brinde el enum:
Los posibles valores que puede tomar el atributo role (ADMIN, SELLER o CUSTOMER) en la constante nicoUser
Analizando una librería con enums

Capacitor es una librería que nos ayuda a implementar aplicaciones multiplataformas. Realizaremos un pequeño análisis aparte de su código para observar cómo hacen empleo de los enums y cómo estos nos pueden ayudar en nuestros proyectos.

Podemos realizar la instalación con el siguiente comando:

npm install @capacitor/camera

Ahora veamos el siguiente código que podemos implementar con dicha librería:

import { Camera, CameraResultType } from '@capacitor/camera';

const takePicture = async () => {
  const image = await Camera.getPhoto({
    quality: 90,
    allowEditing: true,
    resultType: CameraResultType.Uri
  });
};

Observamos que CameraResultType es un enum que restringe al atributo resultType a tener un valor dentro de las opciones del enum. En este caso, dicho atributo recibe el valor de la llave Uri del enum.

En conclusión, un enum nos ayuda a no equivocarnos cuando asignemos valores a una variable reduciendo las posibilidades de asignación a una lista de opciones predefinidas.

Coméntanos: ¿Qué casos de uso encontrarías ideal utilizar los enums?

## TUPLES

Las tuplas o tuples nos permiten crear un array fuertemente tipado especificando el tipo de dato de cada elemento, así como una cantidad definida de elementos que podrá almacenar.

Las tuplas no vienen en el conjunto de tipos de datos por defecto de JavaScript.
Tuplas en TypeScript

Las definimos indicando entre [] el tipo de dato que cada elemento tendrá en la tupla.

const user: [string, number] = ['nicobytes', 15];

Al definir el tipado de cada uno también estamos definiendo la cantidad de valores que tendrá la tupla, por tanto, no podemos agregar más elementos.

let user: [string, number];

user = ['nico']; // Error: la tupla debe almacenar 2 valores (un `string` y un `number`)
user = ['nico', true]; // Error: el segundo elemento de la tupla debe ser del tipo `number`
user = ['nico', 20]; // Correcto: el primer elemento es del tipo `string` y el segundo de tipo `number`

Desestructuración

Podemos aplicar desestructuración para asignar a ciertas variables respectivamente los valores dentro de una tupla.

const user: [string, number] = ['nicobytes', 15];
const [username, age] = user;
console.log(username); // nicobytes

Nota

Este tipo de desestructuración también lo podemos ver en el hook useState de la librería React.

Cuéntanos: ¿En qué situaciones verías útil aplicar las tuplas en tus proyectos?

Contribución creada por: Martín Álvarez (Platzi Contributor) con los 

## Unknown type

El unknown type nos indica que una variable es de un tipo de dato desconocido. Es similar a any, pero sin quitar el análisis de código estático que nos brinda TypeScript.

El tipo unknown nos fuerza a hacer una verificación de tipo. Esta es la forma que TypeScript sugiere trabajar con variables de las cuales no sabemos de qué tipo serán. Así evitamos utilizar constantemente any.
Unknown type en TypeScript

Usamos el keyword unknown para declarar una variable de este tipo.

let unknownVar: unknown;

Unknown vs. Any

Con any podemos hacer lo que queramos, no hay restricción alguna, pero con unknown vamos a tener advertencias al momento de utilizar alguna función o método con variables de este tipo.

let unknownVar: unknown;

unknownVar.toUpperCase(); // Nos marcará el editor una advertencia

Por ejemplo, no podemos directamente aplicar un método propio de un string a una variable unknown. Para ello debemos realizar una verificación de tipo para asegurarnos que se ejecutará dicho método siempre cuando unknownVar sea del tipo string en algún punto del programa:

let unknownVar: unknown;

if (unknownVar === 'string') {
	unknownVar.toUpperCase(); // Ahora ya no nos marcará como error.
}

Unknown en funciones

También podemos emplear unknown en funciones si no sabemos exactamente que nos va a devolver.

const parse = (str: string): unknown => {
	return JSON.parse(str)
}

Coméntanos: ¿Qué casos consideras conveniente utilizar el tipo de dato any por sobre unknown a pesar de sus beneficios? 🤔

##  Never type

El never type se usa para funciones que nunca van a terminar o que detienen el programa. Con esto TypeScript nos ayuda a detectarlos como por ejemplo un ciclo infinito cuando lanzamos un mensaje de error.
Never type en funciones infinitas

En el siguiente código, TypeScript infiere que el tipo es never, ya que su ejecución será infinita.

const withoutEnd = () => {
	while (true) {
		console.log('Nunca parar de aprender');
	}
}

Never vs. Void

Las funciones del tipo void son aquellas que no retornan ningún dato, simplemente ejecutan las instrucciones dentro del bloque de la función. Por tanto, no debemos confundirlas con las de tipo never:

const voidFunc = () => {
  for(let i = 1; i <= 5; i++){
    console.log(i)
  }
}

voidFunc()

/*
// Función infinita y de tipo Never 👇
const neverFunc = () => {
	while (true) {
		console.log('Nunca parar de aprender');
	}
}
*/

Never type en código con errores

Una función también puede ser del tipo never cuando tenemos un throw que lance un error y, como resultado, haga detener la ejecución.

const fail = (message: string) => { // TypeScript infiere que esta función se de tipo `never`
  throw new Error(message)
}

const example = (input:unknown) => {
  if(typeof input === 'string'){
    return 'Es un string';
  }
  else if (Array.isArray(input)){
    return 'Es un array';
  }
  return fail('Not Match'); // Lanzamos un error
}

console.log(example('Hola')) //'Es un string'
console.log(example([1,1,1,1])) // 'Es un array'
console.log(example(1212)) // error: Uncaught Error: Not Match
console.log(example('Hola después del fail')) // NUNCA SE EJECUTA, porque se lanzó un error previamente

## Parámetros opcionales y nullish-coalescing

Los parámetros opcionales son aquellos que podemos obviar su envío cuando mandamos datos en una función que requiere argumentos.

El nullish-coalescing nos permite evaluar si una variable está definida, pero si esta es null o undefined, retorna un segundo valor diferente.
Parámetros opcionales en TypeScript

Para denotar que un parámetro será opcional usamos el operador ? al lado. Siempre debemos colocar los parámetros opcionales al final.

const createProduct = (
	id: string | number, // Puede ser de tipo `string` o `number`.
	isNew: boolean,
	stock?: number, // PARÁMETRO OPCINAL.
) => {
	return { // Retornamos un objeto con los valores pasados como parámetros.
		id,
		stock,
		isNew
	}
}

console.log(
	createProduct(1, true)
) // { id: 1, stock: undefined, isNew: true }

Valores por defecto con el operador OR

Para evitar tener como retorno valores undefined podríamos emplear el operador lógico || (OR) para asignar un valor por defecto.

const createProduct = (
	id: string | number, // Puede ser de tipo `string` o `number`.
	isNew?: boolean,	// PARÁMETRO OPCINAL.
	stock?: number, // PARÁMETRO OPCINAL.
) => {
	return { // Retornamos un objeto con los valores pasados como parámetros.
		id,
		stock: stock || 10,
		isNew
	}
}

console.log(
	createProduct(1, true)
) // { id: 1, stock: undefined, isNew: true }

El problema de usar valores falsy en JavaScript

El operador || evalúa si el primer valor es falsy, de serlo retorna un segundo valor, si no es falsy retorna el primero. Los valores que son considerados falsy en JavaScript son:

    String vacío “”
    Número 0
    El valor booleano false

Aquí surge un problema: si nosotros deseáramos mandar como argumento un valor que JavaScript considera falsy, entonces el operador || no tomará en cuenta nuestros valores y los cambiará por los de defecto:

const createProduct = (
	id: string | number, // Puede ser de tipo `string` o `number`.
	isNew?: boolean,	// PARÁMETRO OPCINAL.
	stock?: number, // PARÁMETRO OPCINAL.
) => {
	return { // Retornamos un objeto con los valores pasados como parámetros.
		id,
		stock: stock || 10,
		isNew: isNew || true
	}
}

console.log(
	createProduct(1, false, 0)
) // { id: 1, stock: 10, isNew: true }
// 👆 JavaScript retorna los valores por defecto de `isNew` y `stock`
//		y no los que mandamos en los argumentos.

Este problema podemos solucionarlo con el nullish-coalescing.
Nullish-coalescing para asignar valores por defecto

El nullish-coalescing se representa con el operador ??. Esto evalúa si el primer valor está definido, si no lo está, retorna el segundo:

const createProduct = (
	id: string | number, // Puede ser de tipo `string` o `number`.
	isNew?: boolean,	// PARÁMETRO OPCINAL.
	stock?: number, // PARÁMETRO OPCINAL.
) => {
	return { // Retornamos un objeto con los valores pasados como parámetros.
		id,
		stock: stock ?? 10,
		isNew: isNew ?? true
	}
}

console.log(
	createProduct(1, false, 0)
) // { id: 1, stock: 0, isNew: false }

## Parámetros por defecto
Los parámetros por defecto se usan para predefinir valores a los parámetros de una función en caso de no especificar un valor al invocarla.
Parámetros por defecto en TypeScript

En TypeScript, usamos el signo = para definir el valor por defecto que cierto parámetro tendrá. Veamos un ejemplo:

// Definición de función
const createProduct = (
	id: string | number,
	isNew: boolean = true, // 👀
	stock: number = 10, // 👀
) => {
	return { // Retornamos un objeto con los valores pasados como parámetros.
		id,
		stock,
		isNew
	}
}

// Impresión en consola
console.log(
	createProduct(1)
) // { id: 1, stock: 10, isNew: true } `stock` y `isNew` por defecto

console.log(
	createProduct(2, false)
) // { id: 1, stock: 10, isNew: false } `stock` por defecto

console.log(
	createProduct(3, false, 50)
) // { id: 1, stock: 50, isNew: false }

Podemos usar esto como alternativa al nullish-coalescing.

## p Parametros Rest

En JavaScript, los parámetros rest nos permiten enviar la cantidad de parámetros que queramos a una función. Se denotan con ... seguido del nombre con el cual identificaremos a estos parámetros:

`` // JavaScript function sum(...args){ //...args` -> Parámetros rest const suma = args.reduce((acumulador, num) => acumulador + num, 0) return suma }

console.log(sum(1,2)) // 5 console.log(sum(1,2,3,4,5)) // 15 console.log(sum(1,2,3,4,5,6,7,8,9,10)) // 55 ```
Parámetros rest en TypeScript

En TypeScript, lo único que cambia es el tipado de los parámetros.

`` // TypeScript function sum(...args: number[]){ //...args` -> Parámetros rest const suma = args.reduce((acumulador, num) => acumulador + num, 0) return suma }

console.log(sum(1,2)) // 5 console.log(sum(1,2,3,4,5)) // 15 console.log(sum(1,2,3,4,5,6,7,8,9,10)) // 55 ```

El nombre de los parámetros rest pueden ser el que queramos: ...args, ...params, ...props, etc.

## Parámetros rest

En JavaScript, los parámetros rest nos permiten enviar la cantidad de parámetros que queramos a una función. Se denotan con ... seguido del nombre con el cual identificaremos a estos parámetros:

`` // JavaScript function sum(...args){ //...args` -> Parámetros rest const suma = args.reduce((acumulador, num) => acumulador + num, 0) return suma }

console.log(sum(1,2)) // 5 console.log(sum(1,2,3,4,5)) // 15 console.log(sum(1,2,3,4,5,6,7,8,9,10)) // 55 ```
Parámetros rest en TypeScript

En TypeScript, lo único que cambia es el tipado de los parámetros.

`` // TypeScript function sum(...args: number[]){ //...args` -> Parámetros rest const suma = args.reduce((acumulador, num) => acumulador + num, 0) return suma }

console.log(sum(1,2)) // 5 console.log(sum(1,2,3,4,5)) // 15 console.log(sum(1,2,3,4,5,6,7,8,9,10)) // 55 ```

El nombre de los parámetros rest pueden ser el que queramos: ...args, ...params, ...props, etc.

## Sobrecarga de funciones: la solución
Cuando el tipado del retorno de una función puede ser más de un tipo de dato (por ejemplo, que el retorno pueda ser string, number o boolean), TypeScript en primera instancia no permite utilizar los métodos propios de un tipo de dato específico a menos que se realice una validación de tipos previamente.
Retorno de funciones con más de un tipo de dato

Supongamos que tenemos una función que puede recibir como parámetro un valor de tipo string o string[] (un array con elementos de tipo string) y retorne lo inverso, osea un string[] si se envía un string o un string si manda un string[]:

// Nico => [N,i,c,o] || Entrada: string => Salida: string[]
// [N,i,c,o] => Nico || Entrada: string[] => Salida: string

function parseStr(input: string | string[]): string | string[] {
  if (Array.isArray(input)) {
    return input.join(''); // string
  } else {
    return input.split(''); // string[]
  }
}

Invoquemos a la función y guardemos su retorno en una variable:

// Nico => [N,i,c,o] || Entrada: string => Salida: string[]
// [N,i,c,o] => Nico || Entrada: string[] => Salida: string

function parseStr(input: string | string[]): string | string[] {
  if (Array.isArray(input)) {
    return input.join(''); // string
  } else {
    return input.split(''); // string[]
  }
}

// 👇
const rptaStr = parseStr(['N','I','C','O']); // Retorna un string
console.log('rptaStr', "['N','i','c','o'] =>", rptaStr);

Como podemos notar a rptaStr se le es asignado un valor de tipo string el cual es el tipado del retorno de la función en este caso. Sin embargo, si intentamos aplicar un método propio de los string como por ejemplo toLowerCase (convierte a minúscula los caracteres), TypeScript nos marcará error:

// Nico => [N,i,c,o] || Entrada: string => Salida: string[]
// [N,i,c,o] => Nico || Entrada: string[] => Salida: string

function parseStr(input: string | string[]): string | string[] {
  if (Array.isArray(input)) {
    return input.join(''); // string
  } else {
    return input.split(''); // string[]
  }
}

const rptaStr = parseStr(['N','I','C','O']); // Retorna un string
rptaStr.toLowerCase(); // ⛔ Error
console.log('rptaStr', "['N','i','c','o'] =>", rptaStr);

Validación de tipos

Ante el problema mostrado anteriormente, podríamos validar el tipo de dato del retorno de la función antes de utilizar el método correspondiente a dicho tipo:

// Nico => [N,i,c,o] || Entrada: string => Salida: string[]
// [N,i,c,o] => Nico || Entrada: string[] => Salida: string

function parseStr(input: string | string[]): string | string[] {
  if (Array.isArray(input)) {
    return input.join(''); // string
  } else {
    return input.split(''); // string[]
  }
}

const rptaStr = parseStr(['N','I','C','O']); // Retorna un string

// Validación de tipos
if (typeof rtaStr === 'string') { // 👈
  rtaStr.toLowerCase(); // ✅ Ya podemos utilizar los métodos sin problemas
}

console.log('rptaStr', "['N','i','c','o'] =>", rptaStr);

Sobrecarga de funciones en TypeScript

La sobrecarga de funciones nos permite definir varias declaraciones de una función con el mismo nombre que puedan recibir diferentes parámetros y/o con diferente tipado. A estas declaraciones se les suelen llamar firmas y la última firma en declarar es la que tendrá la implementación de la función, mientras las otras se quedarán solo declaradas sin código dentro.
Sobrecarga de funciones en vez de la validación de tipos

Podemos usar esta característica presente en TypeScript para ahorrarnos la validación de tipos, como por ejemplo en el problema que hemos visto más arriba con la función parseStr:

// Nico => [N,i,c,o] || Entrada: string => Salida: string[]
// [N,i,c,o] => Nico || Entrada: string[] => Salida: string

// Sobrecarga de funciones 👇
function parseStr(input: string): string[]; // 👀
function parseStr(input: string[]): string; // 👀

function parseStr(input: unknown): unknown { // Función principal
  if (Array.isArray(input)) {
    return input.join(''); // string
  } else {
    return input.split(''); // string[]
  }
}

const rptaStr = parseStr(['N','I','C','O']); // Retorna un string
// Usaremos un método propio del tipo de dato "string"
rtaStr.toLowerCase(); // ✅ No necesitamos de la validación de datos para usar los métodos de este tipo de dato
console.log('rptaStr', "['N','i','c','o'] =>",rptaStr);

const rptaArray = parseStr('Nico'); // Retorna un string[] (un array de elementos de tipo string)
// Usaremos un método propio del tipo de dato "string[]"
rtaArray.reverse(); // ✅ No necesitamos de la validación de datos para usar los métodos de este tipo de dato
console.log('rptaArray', 'Nico =>', rptaArray);

Puesto que en las firmas adicionales (sobrecargas) de la función parseStr ya manejamos los tipos de datos string y string[], el tipado tanto de los parámetros y como del retorno de la firma que contiene la lógica de la función puede ser del tipo unknown o any.

## Interfaces

Las interfaces nos permiten crear moldes de objetos con sus respectivas propiedades y tipado. Para generar interfaces usamos la palabra reservada interface.

interface Product {
	id: number | string;
	title: string;
	price: number;
	stock: number;
}

Si bien podemos hacerlo mismo con type:

type Product = {
  id: number | string;
  title: string;
  price: number;
  stock: number;
}

Existen algunas diferencias que hacen a interface una mejor opción para definir objetos.
Interfaces vs. Type

Veamos la diferencia entre usar interface y type:

    Utilizamos type para definir principalmente tipos primitivos o directos (declaraciones cortas y puntuales), mientras que con una interface definimos una estructura llave-valor de propiedades que describan lo que debe tener un objeto.

type Sizes = 'S' | 'M' | 'L' | 'XL';

interface Product {
	id: number | string;
	title: string;
	price: number;
	stock: number;
	size?: Sizes;
}

    Los interface se pueden fácilmente extender (realizar herencia), mientras que con los type no. Esto los hace más escalables.

## Estructuras complejas

En TypeScript, puedes combinar los enums, types e interfaces de varias formas para crear estructuras de datos complejas y precisas.
Enums en interfaces

Podríamos asociar el tipado de una de las propiedades de un interface con un enum:

enum Color {
  Negro,
  Blanco,
  Morado
}

interface FiguraGeometrica {
  nombre: string;
  color: Color;
}

const rectangulo: FiguraGeometrica = {
  nombre: "rectángulo",
  color: Color.Morado
};

Types en Interfaces

En los atributos de un interface podríamos usar un type para dar un tipado customizable:

type Coordenadas = [number, number];

interface Punto {
  ubicacion: Coordenadas;
  etiqueta: string;
}

const punto: Punto = {
  ubicacion: [10, 5],
  etiqueta: "Punto A"
};

Combinación de Enums y Types

En TypeScript, también es posible juntar los enums y types. Por ejemplo, podemos declarar un type que tenga la estructura de objeto en el que una de sus propiedades es un valor del set de opciones perteneciente a un enum:

enum Size {
  Chico = "S",
  Mediano = "M",
  Grande = "L"
}

type Producto = {
  name: string;
  size: Size; // 👈 Enum
};

const camiseta: Producto = {
  name: "Camiseta",
  size: Size.Mediano
};

Interfaces, enums y types juntos

Es posible usar enums y types dentro de un interface para crear una sola estructura compleja para poder generar objetos con información más detallada y precisa:

enum TipoVehiculo {
  Automóvil,
  Motocicleta
}

type Especificaciones = {
  marca: string;
  modelo: string;
  año: number;
};

interface Vehiculo {
  tipo: TipoVehiculo; // 👈 Enum
  especificaciones: Especificaciones; // 👈 Type
}

// Objeto
const vehiculo: Vehiculo = {
  tipo: TipoVehiculo.Automóvil,
  especificaciones: {
    marca: "Toyota",
    modelo: "Corolla",
    año: 2020
  }
};

Al combinar estas estructuras, tienes la capacidad de producir estructuras de datos más complejas y establecer tipos más detallados para tus objetos y variables. Esto da como resultado un código más claro, seguro y fácil de mantener.

## Extender interfaces
En TypeScript, la herencia en interfaces permite crear una interfaz nueva basada en otra interfaz existente, heredando sus propiedades y métodos.
Herencia de interfaces en TypeScript

Utilizamos la palabra clave extends para aplicar la herencia en interfaces. Veamos un ejemplo:

interface Animal {
  nombre: string;
  comer(): void;
}

interface Mascota extends Animal { // 👈 Herencia de interfaces
// Hereda la propiedad `nombre` y el método `comer()` de la interfaz `Animal`
  jugar(): void;
}

class Perro implements Mascota {
  nombre: string;

  constructor(nombre: string) {
    this.nombre = nombre;
  }

  comer() {
    console.log(this.nombre + " está comiendo.");
  }

  jugar() {
    console.log(this.nombre + " está jugando.");
  }
}

const miPerro = new Perro("Firulais");
miPerro.comer(); // "Firulais está comiendo."
miPerro.jugar(); // "Firulais está jugando."

En el ejemplo, declaramos una interface llamada Animal con un atributo nombre y un método comer(). Después, implementamos otra llamada Mascota que extiende la interfaz Animal y agrega un nuevo método con el nombre jugar(). La clase Perro implementa la interfaz Mascota, por lo que no solo debe implementar el método jugar(), sino también el atributo nombre y el método comer() que fueron heredados de la interfaz Animal en la interfaz Mascota.


## Facer para hacer crud

## Omit y Pick Type

DTOs

Es una abreviatura para referirnos a Data Transfer Objects u Objeto de Transferencias de datos.

Hay momentos particulares en los que nosotros no necesitamos del todo los tipos, es decir, hay parámetros que no hacen falta, por ejemplo, mandarlos al momento de la creación de un objeto, ya que estos son automáticos como el ID o la fecha de creación.

Así que podemos omitir algunos parámetros o campos que en ese particular momento no hacen falta, esto no significa que no están el objeto, sino que al momento de la creación solo necesitamos ciertos parámetros y la API, la base de datos se encargará de insertar lo demás.

Omit

Con omit podemos omitir las propiedades, campos o llaves que quieramos.
Sintaxis

interface InterfaceName extends Omit<TypeOrInterface, keyToOmit1 | ... | keyToOmitN> {
	statements
}

type typeNameDto = Omit<TypeOrInterface, keyToOmit1 | ... | keyToOmitN>

Pick

Es lo contrario de Omit, aquí yo elijo los campos que quiero que estén en mi type o interface.
Sintaxis

interface InterfaceName extends Pick<TypeOrInterface, keyToPick1 | ... | keyToPickN> {
	statements
}

type typeNameDto = Pick<TypeOrInterface, keyToPick1 | ... | keyToPickN>

Buenas prácticas

Una buena práctica es que los DTOs tengan su propio archivo.
Pequeña aclaración sobre nuestro código en esta clase

En el caso de las categorías en los productos, cuando creamos un producto no es que creamos una categoría a la vez, esta ya viene creada y solo la relacionamos, tenemos que mandar solamente el ID de la categoría a la que está relacionado el producto.







