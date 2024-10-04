import flet as ft
import random



        

#funcion principal 
def main(page: ft.Page):
    #variables globales
    global numero_secreto,entrada_numero,texto_resultado,boton_adivinar

    page.title="Adivina el numero"
    
    #generar numero aleatoreo
    numero_secreto= random.randint(1,100)
    
    #crear los elementos de la interfaz
    titulo=ft.Text("Adivina el numero secreto entre 1y 100",size=20,color="white")
    entrada_numero=ft.TextField(label="tu Adivinansa",width=150)
    boton_adivinar=ft.ElevatedButton("Adivinar")
    texto_resultado=ft.Text("",color="white")
    
    contenedor_principal=ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                entrada_numero,
                boton_adivinar,
                texto_resultado,
                ft.Image(
                    src="https://i.ibb.co/Gxgryg9/laser.gif",
                    fit=ft.ImageFit.COVER,
                    width=150,
                    height=200
                )
            ],alignment="CENTER",
            horizontal_alignment="CENTER",
            spacing=20
        ),
        bgcolor="black",
        width=page.window.width,
        height=page.window.height,
        padding=20
    )
    page.add(contenedor_principal)
ft.app(main)
