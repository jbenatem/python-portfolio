from entidades.usuario import Usuario
from gestion.gestion_usuarios import GestionUsuarios

if __name__ == "__main__":
    # Insertar usuarios
    gestion = GestionUsuarios()
    usuario1 = Usuario('Jhon','Doe','DNI','12345678','987654321','prueba@gmail.com')
    gestion.addUsuario(usuario1)
    usuario2 = Usuario('Jack','Sparrow','DNI','87654321','999999999','prueba2@gmail.com')
    gestion.addUsuario(usuario2)
    usuario3 = Usuario('Tony','Stark','DNI','97654321','989999999','prueba3@gmail.com')
    gestion.addUsuario(usuario3)
    
    # Mostrar usuario al azar
    gestion.mostrarUsuarioRandom()
    
    # Eliminar usuarios
    gestion.eliminarUltimoUsuario()
    
    # Mostrar usuarios
    gestion.mostrarUsuarios()