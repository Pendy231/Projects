
# Definim decoradorul pentru a adauga componente unei masini
def add_component(component_name):
    def decorador_add_component(func):
        def wrapper(car):
            #Apelam functia originala pentru a adauga componenta specificata
            func(car)
            #Afisam mesajul de confirmare la adaugare componentei
            print(f"Component{component_name} has been added to the car")
            #Adaugam componentele la lista de componente a masinii
            car.components.append(component_name)
        return wrapper
    return decorador_add_component
        
#Definim clasa car
class Car:
    def __init__(self):
        #Initializam o lista goala pentru componentele masini
        self.components = []
    @add_component("Engine")
    def add_engine(self):
        print("Installing the engine")
    @add_component("Wheels")
    def add_wheels(self):
        print("Attaching the Wheels")
    @add_component("Doors")
    def add_doors(self):
        print("Adding the doors")
        
#Cream un obiect Car
my_car = Car()
my_car.add_engine()
my_car.add_wheels()
my_car.add_doors()
    
print("Components in the car:", my_car.components)    

def add_component(component_name):
    def decorator(func):
        def wrapper(self):
            print(f"Adding {component_name}...")
            func(self)
            self.components.append(component_name)
            print(f"{component_name} added!")
        return wrapper
    return decorator

class Airplane:
    def __init__(self):
        self.components = []
    @add_component("Engine")
    def add_engine(self):
        print("Installing engine")
    @add_component("Wings")
    def add_wings(self):
        print("Put the wings")
    @add_component("Wheels")
    def add_wheels(self):
        print("Attaching the Wheels")
    @add_component("Doors")
    def add_doors(self):
        print("Adding the doors")
    
my_airplane = Airplane()

my_airplane.add_doors()
my_airplane.add_engine()
my_airplane.add_wheels()
my_airplane.add_wings()

print("Components in airplane:", my_airplane.components)



    
