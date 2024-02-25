class TV:
    numTV=0
    def __init__ (self, marca, estado):
        self._marca=marca
        self._estado=estado
        self._canal=1
        self._precio=500
        self._volumen=1
        self._control=None
        TV._numTV=+1
    
    def setMarca (self,marca):

        self._marca=marca
    
    def getMarca (self):

        return self._marca
    
    def setCanal (self,canal):

        if canal >= 0 and canal <= 7:

            self._canal = canal
                   
    def getCanal (self):

        return self._canal
    
    def setPrecio (self,precio):

        self._precio = precio
    
    def getPrecio (self):

        return self._precio
    
    def setVolumen (self,volumen):

        if volumen >= 0 and volumen <= 120:

            self._volumen = volumen
                   
    def getVolumen (self):

        return self._volumen
    
    def setControl (self, control):

        self._control=control

    def getControl (self):
        
        return self._control
    
    @classmethod
    def setNumTV(cls, numTV):
        cls._numTV = numTV
    
    @classmethod
    def getNumTV(cls):
        return cls._numTV 
    
    def turnOn(self):

        self._estado = True

    def turnOff(self, estado):

        self._estado = False
    
    def getEstado(self):

        return self._estado
    
    def canalUp(self):

        if self._estado and self._canal <=119:

            self._canal += 1 
        
    def canalDown(self):

        if self._estado and self._canal >= 2:

            self._canal -= 1
