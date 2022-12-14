class Human:
    def __int__(self, name, age, gender, birth_date, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_date = birth_date
        self.email = email

    def export_info(self):
        print(f"-- HUMAN --")
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"gender: {self.gender}")
        print(f"birth_date: {self.birth_date}")
        print(f"email: {self.email}")


class Time:
    def __int__(self, day, month, year, hour, minute, second):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minute = minute
        self.second = second

    def export_info(self):
        print(f"-- TIME --")
        print(f"{self.day} - {self.month} - {self.year}")
        print(f"{self.hour} : {self.minute} : {self.second}")


class Info:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def export_info(self):
        print(f"{self.name}: {self.value}")


class Laptop:
    def __init__(self, brand, name, cpu, gpu, ram, storage, price, id):
        self.brand = Info("brand", brand)
        self.name = Info("name", name)
        self.cpu = Info("cpu", cpu)
        self.gpu = Info("gpu", gpu)
        self.ram = Info("ram", ram)
        self.storage = Info("storage", storage)
        self.price = Info("price", price)
        self.id = Info("id", id)

    def export_info(self):
        print(f"-- LAPTOP -- ")
        self.brand.export_info()
        self.name.export_info()
        self.cpu.export_info()
        self.gpu.export_info()
        self.ram.export_info()
        self.storage.export_info()
        self.price.export_info()
        self.id.export_info()

    def change_value(self, name, value):
        if name == "brand":
            self.brand.value = value
        elif name == "name":
            self.name.value = value
        elif name == "cpu":
            self.cpu.value = value
        elif name == "gpu":
            self.gpu.value = value
        elif name == "ram":
            self.ram.value = value
        elif name == "storage":
            self.storage.value = value
        elif name == "price":
            self.price.value = value
        elif name == "id":
            self.id.value = value
        else:
            print("Invalid name")


class Shop:
    def __init__(self):
        self.laptops = []

    def add_product(self, laptop):
        self.laptops.append(laptop)

    def add_productlst(self, laptoplst):
        self.laptops.extend(laptoplst)

    def replace(self, id, laptop):
        for i in range(len(self.laptops)):
            if self.laptops[i].id.value == id:
                self.laptops[i] = laptop
                break

    def read_file(self):
        f = open("laptop.txt", "r")
        for line in f:
            line = line.strip()
            line = line.split(",")
            self.add_product(Laptop(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7]))

    def export_info(self):
        print(f"-- SHOP --")
        for laptop in self.laptops:
            laptop.export_info()

    def change_value(self, id, name, value):
        for laptop in self.laptops:
            if laptop.id.value == id:
                laptop.change_value(name, value)
                self.replace(id, laptop)
                break


    def write_file(self):
        f = open("laptop.txt", "w")
        for laptop in self.laptops:
            f.write(
                f"{laptop.brand.value},{laptop.name.value},{laptop.cpu.value},{laptop.gpu.value},{laptop.ram.value},{laptop.storage.value},{laptop.price.value},{laptop.id.value}\n")
        f.close()


if __name__ == "__main__":
    shop = Shop()
    shop.read_file()
    shop.export_info()
    shop.change_value("1", "brand", "Dell")
    shop.export_info()
