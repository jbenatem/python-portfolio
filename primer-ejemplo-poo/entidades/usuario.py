class Usuario():
    # Constructor
    def __init__(self, nombres, apellidos, tipoDoc, nroDoc, celular, email):
        self.nombres = nombres
        self.apellidos = apellidos
        self.tipoDoc = tipoDoc
        self.nroDoc = nroDoc
        self.celular = celular
        self.email = email
        
    # Getters y setters
    def getNombres(self):
        return self.nombres
    
    def setNombres(self, nombres):
        self.nombres = nombres
        
    def getApellidos(self):
        return self.apellidos
    
    def setApellidos(self, apellidos):
        self.apellidos = apellidos
        
    def getTipoDoc(self):
        return self.tipoDoc
    
    def setTipoDoc(self, tipoDoc):
        self.tipoDoc = tipoDoc
        
    def getNroDoc(self):
        return self.nroDoc
    
    def setNroDoc(self, nroDoc):
        self.nroDoc = nroDoc
        
    def getCelular(self):
        return self.celular
    
    def setCelular(self, celular):
        self.celular = celular
    
    def getEmail(self):
        return self.email
    
    def setEmail(self, email):
        self.email = email
        
    # Metodo para ver info
    def verInfo(self):
        info = 'Nombres: ' + self.nombres + '\nApellidos: ' + self.apellidos + '\nTipo documento: ' + self.tipoDoc + '\nNumero documento: ' + self.nroDoc + '\nCelular: ' + self.celular + "\nEmail: " + self.email
        return info