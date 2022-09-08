import random

class GestionUsuarios():
    def __init__(self):
        self.usuarios = []
        self.puntero = 0
        
    def getPuntero(self):
        return self.puntero
        
    def addUsuario(self, usuario):
        self.usuarios.append(usuario)
        self.puntero+=1
        
    def eliminarUltimoUsuario(self):
        self.usuarios.pop(self.puntero-1)
        self.puntero-=1
        
    def mostrarUsuarioRandom(self):
        i = random.randint(0, self.puntero-1)
        print("--------------------------usuario ganador--------------------------")
        print(self.usuarios[i].verInfo())
        
    def mostrarUsuarios(self):
        i = 1
        for usuario in self.usuarios:
            print("--------------------------usuario % s--------------------------" % (i))
            print(usuario.verInfo())
            i+=1