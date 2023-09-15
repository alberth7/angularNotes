# Fundamentos de Angular
by Nicolas Monila

## Qué es Angular: ventajas y cómo aprenderlo

Gran rendimiento de la aplicaciones
Multiplataforma
Across all Platforms
Incredible Tooling

## Qué es Angular: ventajas y cómo aprenderlo

NPM = Node Package Manager

 instalando clien general de angular
  
C:\Users\micha>npm install i -g @anglular/cli


- install client angualr

```
npm install -g @angular/cli
```


Verifica versión de Node: node -v

Verifica versión de npm: npm -v

Instala el CLI de Angular: npm -g @angular/cli

Verifica tu instalación: ng version

Crea tu primer proyecto: ng new my-project

Ejecuta el servidor de desarrollo: ng serve Dentro de la carpeta de tu 
proyecto.

iniciar server
```
ng serve
```

## Comandos de Angular para correr tu proyecto

Specific port
```
ng serve -o --port=3500
```

## Conceptos básicos de TypeScript para usar Angular
TypeScript es un superconjunto de JavaScript. Permite escribir código JS utilizando tipado de datos estáticos y clases. Convierte a JavaScript en un lenguaje más firme y seguro, reduciendo la tasa de errores gracias a la detección temprana de bugs.

## String interpolation

String interpolation es la manera de enviar datos desde nuestro componente hacia la vista. Utilizando el doble símbolo de llaves {{ }}, o también conocidos como brackets, puedes imprimir el valor de una variable, realizar operaciones matemáticas o hacer el llamado a una función dentro del código HTML.

```
<h1>{{ 'Hola Platzi' }}</h1>
<h2>1 + 1 = {{ 1 + 1 }}</h2>
<h3>{{ myFunction(); }}</h3>
```
componet.ts por defecto las variables son publicas

## Property Binding

Property Binding es la manera que dispone Angular para controlar y modificar las propiedades de los distintos elementos de HTML. Para esto, simplemente utiliza los corchetes [] para poder modificar dinámicamente ese atributo desde el controlador.
Utilidades

    El atributo src de la etiqueta <img> para modificar dinámicamente una imagen.
    El atributo href de un <a> para modificar un enlace.
    El atributo value de un <input> para autocompletar un valor de un formulario.
    El atributo disable de un <input> para habilitar/deshabilitar un campo de un formulario.

Si tienes en tu componente:
```
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  empresa = 'Platzi';
  habilitado = true;
}

<input [value]="empresa" [disabled]="habilitado"  />

```

Puedes modificar el value de un campo de un formulario de la siguiente manera:

## Introducción al Event Binding de Angular

A lo igual que el Property Binding nos permite modificar el valor de los atributos de los elementos HTML desde el controlador, el Event Binding permite controlar los eventos que suceden en estos elementos. El clic de un botón, detectar cambios en un campo, el envío de un formulario, entre otros eventos. Para esto utiliza los paréntesis () para el bindeo de la propiedad del elemento.

Si tienes en tu componente:
``````
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  enviarFormulario() {
    // ...
  }
}
``````

Puedes ejecutar el método enviarFormulario() cuando se realiza un clic en un botón de la siguiente manera:
```
<button (click)="enviarFormulario()" >
```

## Otros eventos que puedes escuchar

Además del evento clic, seguramente el más utilizado, hay otros eventos como el change para detectar cambios en un campo de formulario, el evento scroll para detectar el desplazamiento horizontal/vertical del usuario en el navegador, onKeyUp o onKeyDown para detectar cuando el usuario aprieta o deja de apretar un botón de su teclado.

La importancia del Event Binding en Angular está dada por la posibilidad de comunicar el componente y la vista, el código TS con el código HTML, intercambiando datos entre ellos.

Puedes enviarle al controlador el evento completo que se produce en la vista. Para esto, solo declara un parámetro $event en el método que se encuentra escuchando el evento.

Tienes en el controlador:
```
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  buttonClick($event: Event) {
    console.log($event);
  }
}
```
Y en el HTML:
```
<button (onKeyUp)="buttonClick($event)">
```
El método buttonClick() que recibe como parámetro $event del tipo Event, en el HTML bindea el evento onKeyUp y el método recibe argumento $event con el símbolo de pesos delante para que Angular entienda que se trata de un evento.

De esta manera, puedes registrar cada pulsación del teclado imprimiendo por consola el evento producido por el usuario.

Aporte creado por: Kevin Fiorentino.



## Data binding con ngModel
El atributo ngModel permite el intercambio de datos de forma bidireccional entre el componente y la vista. Lo que suceda en el componente, se verá reflejado en la vista. Lo que se suceda en la vista, inmediatamente impactará en el componente.

<input [(ngModel)]="name">

ngModel usar tanto los corchetes [] como los paréntesis (). De esta manera, se vuelve bidireccional el intercambio de datos. Si no quieres la bidirección, solo colocamos los corchetes [ngModel] para que la comunicación sea unidireccional.Para utilizar ngModel, es necesario hacer uso e importar Angular Forms. Para esto, dirígete al archivo app.module.ts que es el módulo principal de toda aplicación Angular y agrega lo siguiente:

```
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [ ... ],
  imports: [
    FormsModule
  ],
  providers: [],
  bootstrap: [ ... ]
})
export class AppModule { }
```
De esta manera puedes importar el módulo FormsModule desde @angular/forms y agregarlo a imports para emplear la propiedad [(ngModel)].

## Uso de *ngIf
Estructuras de control

El condicional “If” es un “If” en Javascript, en Java, en PHP, en Python o en cualquier lenguaje. Angular posibilita utilizar este condicionante embebido en el HTML para mostrar o no un elemento. Su sintaxis es algo particular, está compuesta por un asterisco seguido de las iniciales características de Angular “ng” y la palabra “If”.
``````
<div *ngIf="isPlatzi">Hola, soy Platzi</div>
``````
Si la condición dentro del “If” se cumple, se mostrará el <div> con el respectivo contenido dentro. De lo contrario, el usuario no verá dicho elemento en el navegador. En la condición del If puedes colocar cualquier operador lógico:

## Uso de *ngFor

Al igual que con un If, Angular permite iterar un array de números, de cadenas de caracteres o de objetos usando “*ngFor”.Si tienes en tu componente un array de datos:

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  myArray: string[] = [
    'Platzi',
    'es',
    'genial!'
  ];
}

Puedes mostrar cada elemento iterando el array en un elemento HTML:

<ul>
    <li *ngFor="let str of myArray">
        {{ str }}
    </li>
</ul>

El *ngFor crea una variable temporal llamada str (o el nombre que más te guste) que contiene cada valor de myArray. Finalmente, utilizando una interpolación, muestras el valor de str.Quedando tu HTML de la siguiente manera:

<ul><li>Platzi</li><li>es</li><li>genial!</li></ul>

Índice de iteración

    ngFor también cuenta con un índice con el número de iteraciones. Puedes acceder a este número agregando al ngFor index as i de la siguiente manera:

<ul>
    <li *ngFor="let str of myArray; index as i">
        {{ i }}. {{ str }}
    </li>
</ul>

Cada iteración contiene una variable i con el índice que le corresponde. Iniciando desde cero, da como resultado:

<ul>
    <li>0. Platzi</li>
    <li>1. es</li>
    <li>2. genial!</li>
</ul>

## Uso de *ngSwitch

Angular también ofrece la sentencia *ngSwitch y *ngSwitchCase para determinar el flujo de control de tu aplicación y qué elemento mostrar entre multiples elementos HTML. Además de utilizar un elemento default con *ngSwitchDefault en caso de que ninguna condición se cumpla.

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
    color: string = 'verde';
}

Ejemplo de *ngSwitchCase

<div [ngSwitch]="color">
    <p *ngSwitchCase="'azul'">
        El color el Azul
    </p>
    <p *ngSwitchCase="'verde'">
        El color el Verde
    </p>
    <p *ngSwitchCase="'rojo'">
        El color el Rojo
    </p>
    <p *ngSwitchDefault>
        No hay ningún color
    </p>
</div>



## Uso de *ngSwitch
 Angular también ofrece la sentencia *ngSwitch y *ngSwitchCase para determinar el flujo de control de tu aplicación y qué elemento mostrar entre multiples elementos HTML. Además de utilizar un elemento default con *ngSwitchDefault en caso de que ninguna condición se cumpla.

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
    color: string = 'verde';
}

Ejemplo de *ngSwitchCase

<div [ngSwitch]="color">
    <p *ngSwitchCase="'azul'">
        El color el Azul
    </p>
    <p *ngSwitchCase="'verde'">
        El color el Verde
    </p>
    <p *ngSwitchCase="'rojo'">
        El color el Rojo
    </p>
    <p *ngSwitchDefault>
        No hay ningún color
    </p>
</div>

## Estilos a la lista de productos

En el decorador de tu componente, verás la propiedad styleUrls donde se hace referencia a la hoja de estilos que el componente utiliza.

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
    ...
}

En este archivo puedes escribir todo el código CSS que tu componente necesita. Por ejemplo, si escogiste SCSS:

div {
    margin: 15px;
    h1 {
        font-family: Arial;
        font-size: 22px;
        font-weight: bold;
    }
    p {
        font-family: Arial;
        font-size: 18px;
        padding-bottom: 10px;
    }
}

Preprocesadores de CSS

Dependiendo el preprocesador que hayas elegido, tus hojas de estilos tendrán una extensión u otra. A excepción de .css si no escogiste utilizar un preprocesador.
scss .scss
sass .sass
les .less

    TIP: Para escojer otro preprocesador, puedes realizar este cambio manualmente en el archivo ‘angular.json’ en la raíz de tu proyecto

## Dynamic class & style
Class binding

La versatilidad de Angular te permite agregar o quitar clases y estilos a tus elementos HTML a partir de condicionantes. Así como anteriormente utilizaste los corchetes [] para bindear atributos como el [src] de una imagen o el [href] de un enlace, puedes bindear clases para que Angular las agregue o quite dinámicamente si se cumple una condición de la siguiente manera:

<div [class.active-color]="isActive">
</div>

Imagina que tienes en tu componente una propiedad llamada isActive que agregará la clase active-color si esta es verdadera o quitará la clase si es falsa. Luego ya puedes darle los estilos que más te gusten al elemento HTML en tu hoja de estilos utilizando la clase active-color.
Style binding

También puedes añadir estilos inline a los elementos HTML bindeando la propiedad [style] seguido de la propiedad CSS que quieres modificar dinámicamente:

<p [style.color]="isActive ? 'blue' : 'red'"></p>

A partir del valor de isActive, dependiendo si este es verdadero o falso, puedes emplear un operador ternario para cambiar el color del párrafo.

Aporte creado por: Kevin Fiorentino.

la Socion del hoisting es formularios reactivos

## NgClass y NgStyle

Con el binding de [class] y [style] puedes agregar clases y estilos fácilmente. Pero se vuelve algo complicado en el caso de que necesites agregar varias clases o modificar muchos estilos. Es por esto que Angular ofrece las directivas ngClass y ngStyle para este propósito.

Puedes bindear la directiva [ngStyle] o [ngClass] y pasarle un objeto con cada propiedad o clase que deseas agregar:

<p
    [ngStyle]="{
        'color': textColor,
        'background': textBackground
    }"
></p>

El operador ternario será tu mejor aliado para agregar o quitar clases y estilos:

<div
    [ngClass]="isAvailable ? 'active-class' : 'deactivate-class'"
></div>

O puedes usar las Interpolaciones en lugar del binding:

<p
    ngClass="{{ isAvailable ? 'active-class' : 'deactivate-class' }}"
></p>



## Crear un formulario

Conociendo la directiva [(ngModel)] que nos facilita el intercambio de datos de forma bidireccional entre la vista y el componente, puedes crear tu primer formulario apoyándote de esta directiva y de otras características propias de Angular para el manejo y validación de formularios.
Paso 1

Crea un simple formulario de Login en el HTML y las variables en el componente para capturar los valores de los campos con ngModel:

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  form = {
    email: '',
    password = ''
  };
}

<form>
    <div>
        <label></label>
        <input name="email" type="email" [(ngModel)]="form.email" required />
    </div>
    <div>
        <label></label>
        <input name="password" type="password" [(ngModel)]="form.password" required />
    </div>
    <div>
        <button type="submit">Iniciar sesión</button>
    </div>
</form>

Paso 2

Agregale al componente un método que responda al evento del envío del formulario llamado submitLogin(). Puedes enlazar este método al formulario con la directiva (ngSubmit) que va colocada en la etiqueta <form> junto con una variable de template para ponerle un nombre al formulario como por ejemplo #formLogin="ngForm". Tienes que igualar el nombre de tu variable a ngForm para que Angular reconozca que se trata de un formulario.

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  form = {
    email: '',
    password = ''
  };
  submitLogin() {
    // Login del usuario
  }
}

<form (ngSubmit)="submitLogin()" #formLogin="ngForm">
    <div>
        <label></label>
        <input name="email" type="email" [(ngModel)]="form.email" required />
    </div>
    <div>
        <label></label>
        <input name="password" type="password" [(ngModel)]="form.password" required />
    </div>
    <div>
        <button type="submit">Iniciar sesión</button>
    </div>
</form>

Paso 3

Finalmente, gracias a esta conexión de tu formulario con el componente, se activará el método submitLogin() al hacer clic en el botón. Para validar tu formulario, utiliza la variable de template para imprimir un mensaje de error en pantalla o deshabilitar el botón de envío de la siguiente manera:

...
<div>
    <button [disabled]="formLogin.invalid" type="submit">Iniciar sesión</button>
</div>
...

## Objetos en funciones

Nuestras funciones pueden recibir objetos como argumentos. En TypeScript también podemos declarar el tipado de estos. Veamos un ejemplo:

//TypeScript
function imprimirDatos( data: { username: string, email: string } ): void {

    console.log(`Tu nombre de usuario es ${data.username} y tu email es ${data.email}`)
    
}

imprimirDatos({
      username: 'freddier',
      email: 'freddy@email.com'
})

En el ejemplo, el nombre data hace referencia al objeto que recibirá la función imprimirDatos. Por ello, para acceder al valor de username lo definimos en el console.log como data.username y para el email como data.email, pues así es como se accede a las propiedades de un objeto.

Finalmente, cuando invocamos imprimirDatos y queremos enviar el objeto que nos pide como parámetro, simplemente se colocará entre llaves los atributos del mismo sin colocar un nombre de referencia como data tal como lo hicimos en la definición de la función.

## Objetos como tipos
En TypeScript también podemos usar los Alias para definir la estructura de tipado que debería tener un objeto:

//TypeScript
type userData = {
    username: string,
    email: string
}

Y luego este “nuevo tipo” puede ser usado en un array, por ejemplo, para definir el tipado de los objetos que queramos añadir:

//TypeScript
type userData = {
    username: string,
    email: string
}

let usersList: userData[] = [];

usersList.push({
    username: "freddier", //CORRECTO
    email: "freddy@email.com", //CORRECTO
});
usersList.push({
    username: "cvander", //CORRECTO
    email: true, // ERROR. Debe ser de tipo string y NO de tipo boolean
});

## Módulos: import y export

Nuestro código puede ser dividido en varios módulos (archivos), por lo que para poder usar las funciones o variables que existen en uno y queramos acceder desde otro, utilizamos import y export.
Export

/*---->  Archivo: funciones.ts  <----*/
export function suma(a: number, b: number): number {
    return a + b;
}

export function resta(a: number, b: number): number {
    return a - b;
}

export let numerosRandom = [1, 30, 40, 50];
export type Sizes = "S" | "M" | "L" | "XL";

Como observamos, tenemos un archivo llamado funciones.ts la cual contiene dos funciones: suma y resta. Si estas queremos usarlas desde otro archivo, necesitamos usar la palabra reservada export justo antes de definir nuestra función (lo mismo aplica para las variables). De esta forma indicamos que serán exportados para ser utilizados desde otro archivo JavaScript/TypeScript.
Import

/*---> Archivo: programa.ts  <---*/

import {suma, resta, Sizes} from "./funciones.ts";

Finalmente, las funciones o variables que queramos utilizar desde otro archivo son importadas de la siguiente manera:

    Usamos la palabra reservada import
    Entre llaves indicamos las funciones y/o variables que queremos acceder. Hacemos una separación con comas
    Usamos la palabra reservada from, seguido de, entre comillas dobles o simples, la ruta de la ubicación en la que se encuentra el archivo del cual estamos importando su código.

Nota

Si es un módulo TypeScript lo que estamos importando, es importante que en la ruta de los import figure la extensión .ts de dicho archivo. Si es un archivo JavaScript, colocar la extensión .js es opcional.

## Usando librerías que soportan TypeScript

Las librerías que tienen soporte para TypeScript nos facilitan su uso, y más aún si usas editores de código que se integran bien con este “lenguaje”, pues brindan información muy útil como indicar:

    La cantidad de parámetros esperados por una función
    El tipo de datos de los parámetros y variables
    El tipo de dato que retornará la función
    Autocompletado al usar métodos de un módulo
    Mejores prácticas

https://date-fns.org/docs/Getting-Started#installation

## Usando librerías que NO soportan TypeScript

El ecosistema de TypeScript ha creado unos módulos para agregar manualmente el tipado a las librerías que no tienen soporte de tipos.

Por ejemplo, si quieres trabajar con la librería lodash, en Visual Studio Code se te indicará que instales un sistema de tipos para que puedas desarrollar sin problemas desde TypeScript:
Error al queres utilizar lodash en TypeScript

https://lodash.com/

## 



