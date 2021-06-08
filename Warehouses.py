# Set variables

Access_Code = False
Warehouse_1 = "250 Sedans"
Warehouse_2 = "184 Trucks"
Warehouse_3 = "1239 Vehicles,Quad Bikes, Bakkies"
Warehouse_4 = "3127 Sedans, Vehicles, Quad_Bikes, Bakkies, Trucks "
Warehouse_5 = "10423 Sedans, Vehicles, Quad_Bikes, Bakkies, Trucks"

# Create Main Warehouse Class
class Plant:
    def __init__(self, Warehouse_1, Warehouse_2, Warehouse_3, Warehouse_4, Warehouse_5):
        self.Warehouse_1 = Warehouse_1
        self.Warehouse_2 = Warehouse_2
        self.Warehouse_3 = Warehouse_3
        self.Warehouse_4 = Warehouse_4
        self.Warehouse_5 = Warehouse_5

# Create Function for each senior manager in each wherehouse
    def Senior_Manager(Warehouse_1):
        guest = int(input("Please Enter The Access Code: "))
        if Access_Code == True:
            print("Acess Granted")
        else:
            print("Access Denied, check front desk for direction")

    def Senior_Manager(Warehouse_2):
        guest = int(input("Please Enter The Access Code: "))
        if Access_Code == True:
            print("Acess Granted")
        else:
            print("Access Denied, check front desk for direction")


    def Senior_Manager(Warehouse_3):
        guest = int(input("Please Enter The Access Code: "))
        if Access_Code == True:
            print("Acess Granted")
        else:
            print("Access Denied, check front desk for direction")

    def Senior_Manager(Warehouse_4):
        guest = int(input("Please Enter The Access Code: "))
        if Access_Code == True:
            print("Acess Granted")
        else:
            print("Access Denied, check front desk for direction")

    def Senior_Manager(Warehouse_5):
        guest = int(input("Please Enter The Access Code: "))
        if Access_Code == True:
            print("Acess Granted")
        else:
            print("Access Denied, check front desk for direction")


# Create Warehouse functions
    def Warehouse_1(self):
        if "Sedans" == 250:
            return True
        else:
            return False

    def Warehouse_2(self):
        if "Trucks" == 184:
            return True
        else:
            return False

    def Warehouse_3(self):
        if "Vehicles,Quad Bikes, Bakkies" == 1239:
            return True
        else:
            return False


    def Warehouse_4(self):
        if "Sedans, Vehicles, Quad_Bikes, Bakkies, Trucks" == 3127:
            return True
        else:
            return False


    def Warehouse_5(self):
        if "Sedans, Vehicles, Quad_Bikes, Bakkies, Trucks" == 10423:
            return True
        else:
            return False

# Warehouse Repairs

faults = int(input("Enter the number of faults: "))

    def Repairs(Warehouse_1):
        if faults == 0:
            return "Everything is fully operational"
        else:
            return "Make repairs to warehouse_1"


    def Repairs(Warehouse_2):
        if faults == 0:
            return "Everything is fully operational"
        else:
            return "Make repairs to warehouse_2"


    def Repairs(Warehouse_3):
        if faults == 0:
            return "Everything is fully operational"
        else:
            return "Make repairs to warehouse_3"


    def Repairs(Warehouse_4):
        if faults == 0:
            return "Everything is fully operational"
        else:
            return "Make repairs to warehouse_4"


    def Repairs(Warehouse_5):
        if faults == 0:
            return "Everything is fully operational"
        else:
            return "Make repairs to warehouse_5"











