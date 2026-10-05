import ttkbootstrap as ttk
import style
from view import VistaPrincipal

if __name__ == "__main__":
    ventana = ttk.Window(
        title=style.TEXTO_TITULO,
        themename=style.TEMA_VENTANA
    )
    app = VistaPrincipal(ventana)
    ventana.mainloop()