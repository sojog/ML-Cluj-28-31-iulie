
class Model:
    def __init__(self, name, version):
        self.name = name
        self.version = version
    
    def __str__(self):
        return f"Modelul cu numele {self.name} are versiunea {self.version}"
    


if __name__ == "__main__":
    obiect = Model("DTC", "0.9")
    print(obiect)