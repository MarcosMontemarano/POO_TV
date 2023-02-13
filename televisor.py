"""
Definir una clase TV que tenga los métodos power, está_encendido, canal_siguiente, canal_anterior y obtener_canal.
El método power conmuta entre el encendido y apagado del televisor, el resto de los métodos tiene nombres bastante descriptivos. Observar 
que los métodos power, canal_siguiente y canal_anterior no tienen por qué devolver nada, pero está_encendido devuelve un bool, y obtener_canal
devuelve un int con el número de canal en el que está el televisor, si es que está encendido (o sea, si está_encendido devuelve True).
"""

class televisor:
    # Attributes      
    def __init__(self): # Constructor
            self.canal = [1,2,3,4]
            self.power = False
            self.canal_actual = self.canal[0]
    # Methods
    def obtener_canal(self):
        if self.power:
           print("Se está viendo el canal N° {}".format(self.canal_actual))
        else:
            print("El televisor se encuentra apagado")
    
    def canal_siguiente(self): # Sube los canales hasta el último y vuelve a comenzar
        if self.canal_actual != self.canal[len(self.canal)-1]:
            self.canal_actual += 1
        else:
            self.canal_actual = self.canal[0]
    
    def canal_anterior(self): # Baja los canales hasta el primero y vuelve a comenzar
        if self.canal_actual != self.canal[-len(self.canal)]:
            self.canal_actual -= 1
        else:
            self.canal_actual = self.canal[len(self.canal)-1]
    
    def esta_encendido(self):
        if self.power :
            print("El televisor esta encendido")
        else:
            print("El televisor esta apagado")  
            
    # Setter Conmutator
    def set_power(self):
        if self.power :
            self.power = False
            print("Apagado del televisor")
        else :
            self.power = True
            print("Encendido del televisor")

# class SmartTv(televisor):
#     def __init__(self):
#         super().__init__()
