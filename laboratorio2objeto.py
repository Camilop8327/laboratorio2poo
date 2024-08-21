class Papeleria:
    def __init__(self,color,genero):

        self.color=color
        self.genero=genero

librohist=Papeleria("Amarillo", "Historia")
libroRoman=Papeleria("Rojo", "Romance")

print(type(librohist))
print(type(libroRoman))

print(librohist.color, librohist.genero)
print(libroRoman.color, libroRoman.genero)