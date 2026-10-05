# Ejercicio-Reto---Programacion-Multiplataforma

Migrar la aplicación de jubilación vista en clase a ttkbootstrap, usando una fecha de nacimiento en lugar de la edad, y generar el ejecutable para Ubuntu.

Instrucciones

Parte del archivo jubilacionGUI.py realizado en clases, se debe modificar para que cumpla con lo siguiente:

1. Migración a ttkbootstrap: 

Reemplaza tk.Tk() por ttk.Window y aplicar un tema (themename).
Usa los widgets de ttkbootstrap: ttk.Label y ttk.Button.

2. Diseño de la ventana:

Organizar los widgets con grid(). No uses place().
Usar bootstyle para darle color a los widgets.

3. Fecha de nacimiento:

Cambiar el Entry por un DateEntry para pedir la fecha de nacimiento, con formato dd/mm/aaaa (dia/mes/año).

4. Cálculo de la edad exacta:

Calcula la edad a partir de la fecha de nacimiento.
Debe ser exacta: tomar en cuenta si la persona ya cumplió años este año o todavía no.

5. Validaciones:

Si la fecha escrita no es válida, muestra un mensaje de error.
Si la fecha es futura, muestra un mensaje de error.

6. Resultado:

Mostrar la edad de la persona y los años que faltan para jubilarse (o, si ya tiene 60 o más, que debería pensar en jubilarse).
El resultado debe aparecer tambien en un Messagebox de ttkbootstrap y en una etiqueta(Label de ttkboostrap) de la ventana.