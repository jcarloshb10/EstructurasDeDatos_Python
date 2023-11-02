class Cancion():
    def __init__(self,artista,titulo,duracion):
        self.artista = artista
        self.titulo = titulo
        self.duracion = duracion

    def __eq__(self,cancion):
        if self.artista == cancion.artista and self.titulo == cancion.titulo and cancion is not None:
            return True
        else:
            return False
    def __str__(self):
        return "🎶"+ str(self.artista) + "" + str(self.titulo) + "" + str(self.duracion)
