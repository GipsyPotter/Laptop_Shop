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


class Shop:
    def __init__(self):
        self.laptops = []

    def add_product(self, laptop):
        self.laptops.append(laptop)

    def add_productlst(self, laptoplst):
        self.laptops.extend(laptoplst)

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


if __name__ == "__main__":
    shop = Shop()
    shop.read_file()
    shop.export_info()