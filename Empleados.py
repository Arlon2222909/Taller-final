class Empleado:
    
    def __init__(self,nombre,id,salario):
        self.nombre = nombre
        self.id = id
        self.tareas = []
        self.salario = salario 
    
    def asignar_tarea(self,tarea):
        self.tareas.append(tarea)
        
    def Calcularsalario(self):
        return self.salario
    
    
class Tarea:
    
    def __init__(self,problema):
        self.problema = problema
        
class Departamento:
    
    def __init__(self,nombre):
        self.nombre = nombre
        self.empleado = []
        
    def agregar(self,empleado):
        self.empleado.append(empleado)
        
    def informe(self):
        for empleado in self.empleado:
            print(f'Empleado: {empleado.nombre}, Salario: {empleado.Calcularsalario()}, Tareas: {[tarea.problema for tarea in empleado.tareas]}')
            
departamento = Departamento("Compras")
empleado1 = Empleado("Juan Alberto Lisboa",222,2000000)
empleado2 = Empleado("Sebastian Contreras Rojas",333,1500000)

tarea1 = Tarea('Comprar productos')
tarea2 = Tarea('Atender al cliente')

empleado1.asignar_tarea(tarea1)
empleado2.asignar_tarea(tarea2)

departamento.agregar(empleado1)
departamento.agregar(empleado2)

departamento.informe()