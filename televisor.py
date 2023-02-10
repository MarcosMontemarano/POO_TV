"""
Definir una clase TV que tenga los métodos power, está_encendido, canal_siguiente, canal_anterior y obtener_canal.
El método power conmuta entre el encendido y apagado del televisor, el resto de los métodos tiene nombres bastante descriptivos. Observar 
que los métodos power, canal_siguiente y canal_anterior no tienen por qué devolver nada, pero está_encendido devuelve un bool, y obtener_canal
devuelve un int con el número de canal en el que está el televisor, si es que está encendido (o sea, si está_encendido devuelve True).
"""

class televisor:
    # Atributos      
    def __init__(self): 
            self.canal = [1,2,3,4]
            self.power = False
    
    def obtener_canal(self,canal_actual):
           print("Se está viendo el canal N° {}".format(canal_actual))
    
    def canal_siguiente (self):
        for n in range(0,len(self.canal)):
            canal_actual = self.canal[n] + 1
        return canal_actual
    # Metodos
    def esta_encendido(self):
        if self.power :
            print("El televisor esta encendido")
        else:
            print("El televisor esta apagado")  
            
    # Setter Conmutador
    def set_power(self):
        if self.power :
            self.power = False
        else :
            self.power = True

una_tele = televisor() # A esta variable le otorgo los atributos de esta clase