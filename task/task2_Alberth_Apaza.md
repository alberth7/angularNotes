ngOnInit(): Se llama después de que Angular ha inicializado las propiedades del componente. Es donde se debe realizar tareas de inicialización, como configurar valores iniciales, realizar llamadas a servicios, etc.

ngAfterViewInit(): Este método se llama después de que Angular ha inicializado la vista del componente y se ha establecido la relación entre la vista y el componente. Es un buen lugar para realizar tareas que requieren acceso a los elementos del DOM, como manipulaciones del DOM o configuraciones de bibliotecas externas.

En el ejemplo, se trata de acceder a ViewChild en ngOnInit() del componente padre, ViewChild se inicializa en ngAfterViewInit() del componente hijo. Esto significa que cuando se llama ngOnInit() del componente padre, ViewChild aún no está disponible porque ngAfterViewInit() del componente hijo aún no se ha ejecutado.

Por eso, en ngOnInit() del componente padre, childElement es la propiedad que contiene el elemento del DOM obtenido a través de ViewChild en el componente hijo, es undefined o nulo, lo que provoca un error si intentas acceder a él.

Para poder utilizar el valor obtenido por ViewChild en el ciclo de vida ngOnInit() del componente padre:

Una de las soluciones es retrasar a ngOnInit() del padre pero esto puede retrasar la ejecución de la lógica hasta después de que se haya completado la inicialización del componente padre.

Es importante asegurarse de que ViewChild esté disponible antes de intentar acceder a él en ngOnInit() del componente padre.

El static: true se utiliza para aceder al elemto desde un inicio, static: true puede ser útil en situaciones en las que necesitas acceder al elemento antes de que Angular haya completado la renderización de la vista, como en el constructor del componente. Sin embargo, en la mayoría de los casos, es preferible no usar static: true y permitir que Angular realice la búsqueda dinámicamente para asegurarse de que el elemento esté disponible después de la renderización completa de la vista.