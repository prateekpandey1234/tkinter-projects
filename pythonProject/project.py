class member:
    def __init__(self,*args):
        self.age=""
        self.salary=10000
        self.name=""
        self.gender=""
        self.room=""
        self.phone=""
        self.entry=""
        self.hospital={}
    def add(self):
        print("Please enter every details in given format\n:-->")
        for i in range(6):
            if i==0:
                self.name=input("Enter name:-->")
            if i==1:
                self.entry=input("Enter entry time:-->")
            if i ==2 :
                self.phone = input("Enter phone number:-->")
            if i ==3 :
                self.gender = input("Enter gender of person:-->")
            if i ==4 :
                self.age = input("Enter age :-->")
        self.hospital.update({str(self.name):(self.entry,self.age,self.phone,self.gender,self.room,self.salary)})

    def remove(self):
        name = input("Please enter the name of patient to be removed:-->")
        if name in self.hospital.keys():
            self.hospital.pop(name)
            print("SUCCESS!")
        else:
            print("\033[91mError not found!\nTry again !")
class patient(member):
    def __init__(self,*args):
        super().__init__(*args)
    def read(self):
        name=input("Enter the name of patient:-->")
        if name in self.hospital.keys():
            print("NAME:->{},\nAGE:->{},\nGENDER:->{},\nNUMBER:->{},\nENTRY:->{},\nSALARY:->{}".format(self.name,self.age,self.gender,
                                                                                                       self.phone,self.entry, self.salary))
        else:
            raise Exception
class staff(member):
    def __init__(self,*args):
        super().__init__(*args)
        self.salary=""
    def read(self):
        name=input("Enter the name of staff:-->")
        print(name)
        if name in self.hospital.keys():
            print("NAME:->{},\nAGE:->{},\nGENDER:->{},\nNUMBER:->{},\nENTRY:->{},\nSALARY:->{}".format(self.name,self.age,self.gender,self.phone,self.entry
                                                                                                   ,self.salary))
        else:
            print(self.hospital)
global pat
global stf
pat = patient()
stf = staff()
def hosp():
    task="patient"
    print("HELLO! \nPlease select either staff or patient to see their details \n:--->")
    type=str(input()).lower()
    try:
        if type=="patient" or type=="staff":

            for i in range(3):
                task1 = str(input("\033[94mEnter the task you wan to do!:-->")).lower()

                if task1=="add" or task1=="remove" or task1=="read":
                    task=task1
                    raise NameError
                else:
                    print("\033[93mPlease enter what you want to do!")
                    if i==2:
                        raise ArithmeticError

        else:
            raise ArithmeticError
    except NameError as e:
        if task == "add":
            if type == "patient":
                pat.add()
            elif type == "staff":
                stf.add()
        elif task == "read":
            if type == "patient":
                pat.read()
            elif type == "staff":
                stf.read()
        elif task=="remove":
            if type=="patient":
                pat.remove()
            elif type=="staff":
                stf.remove()
        hosp()
    except ArithmeticError as e:
        print("\033[91mError not found!\nTry again !")
        hosp()

if __name__=="__main__":
    hosp()
