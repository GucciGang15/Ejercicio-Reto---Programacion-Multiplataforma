import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
import style
import logic

class VistaPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.configurar_ventana()
        self.construir_interfaz()

    def configurar_ventana(self):
        self.ventana.title(style.TEXTO_TITULO)
        self.ventana.geometry(f"{style.VENTANA_ANCHO}x{style.VENTANA_ALTO}")
        self.ventana.resizable(False, False)
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.columnconfigure(1, weight=1)

    def construir_interfaz(self):
        self.lbl_titulo = ttk.Label(
            self.ventana,
            text=style.TEXTO_TITULO,
            font=style.FUENTE_TITULO,
            bootstyle=style.BOOTSTYLE_TITULO
        )
        self.lbl_titulo.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=style.PAD_TITULO_Y
        )

        self.lbl_fecha = ttk.Label(
            self.ventana,
            text=style.TEXTO_ETIQUETA_FECHA,
            font=style.FUENTE_ETIQUETA
        )
        self.lbl_fecha.grid(
            row=1,
            column=0,
            padx=style.PAD_X,
            pady=style.PAD_Y,
            sticky="e"
        )

        self.fecha_entry = ttk.DateEntry(
            self.ventana,
            dateformat="%d/%m/%Y",
            bootstyle=style.BOOTSTYLE_CALENDARIO
        )
        self.fecha_entry.grid(
            row=1,
            column=1,
            padx=style.PAD_X,
            pady=style.PAD_Y,
            sticky="w"
        )

        self.btn_calcular = ttk.Button(
            self.ventana,
            text=style.TEXTO_BOTON_CALCULAR,
            command=self.procesar_accion,
            bootstyle=style.BOOTSTYLE_BOTON
        )
        self.btn_calcular.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=style.PAD_Y
        )

        self.lbl_resultado = ttk.Label(
            self.ventana,
            text=style.TEXTO_INICIAL_RESULTADO,
            font=style.FUENTE_RESULTADO,
            bootstyle=style.BOOTSTYLE_ETIQUETA,
            wraplength=720,
            justify="center"
        )
        self.lbl_resultado.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=style.PAD_X,
            pady=style.PAD_Y
        )

    def procesar_accion(self):
        texto_fecha = self.fecha_entry.entry.get().strip()
        mensaje, es_error = logic.evaluar_estado_jubilacion(texto_fecha)

        if es_error:
            Messagebox.show_error(mensaje, title="Error de Registro")
            self.lbl_resultado.config(
                text=mensaje,
                bootstyle=style.BOOTSTYLE_ERROR
            )
        else:
            Messagebox.show_info(mensaje, title="Confirmación")
            if "debería pensar en jubilarse" in mensaje:
                estilo = style.BOOTSTYLE_ADVERTENCIA
            else:
                estilo = style.BOOTSTYLE_EXITO

            self.lbl_resultado.config(
                text=mensaje,
                bootstyle=estilo
            )