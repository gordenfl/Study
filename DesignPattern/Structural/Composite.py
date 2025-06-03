# 这个模式就像一个  文件目录结构
# Fold -> Fold -> Files
# Fold 也是一种文件，可以包含文件，也可以包含Fold
class Employee(object):  # as basic file infomation
    def __init__(self):
        self.name = None
        self.id = None
        self.position = None

    def showEmployeeInfo(self):
        pass


class Developer(Employee):  # as text file
    def __init__(self, id, name, position):
        super().__init__()
        self.name = name
        self.id = id
        self.position = position

    def showEmployeeInfo(self):
        # super().showEmployeeInfo()
        return "Developer Info, Id:%d, Name:%s, Position:%s" % (self.id, self.name, self.position)


class Manager(Employee):  # as photo file
    def __init__(self, id, name, position):
        super().__init__()
        self.name = name
        self.id = id
        self.position = position

    def showEmployeeInfo(self):
        # super().showEmployeeInfo()
        return "Manager Info, id:%d, Name:%s, Position:%s" % (self.id, self.name, self.position)


class CompanyInfo(Employee):  # as a folder can include files and it is a file as well
    def __init__(self, name):
        super().__init__()
        self.employeeList = []
        self.name = name

    def showEmployeeInfo(self):
        ret = "Company name:"+self.name
        for emp in self.employeeList:
            ret += " "+emp.showEmployeeInfo()
        return ret

    def getEmployee(self, id):
        for emp in self.employeeList:
            if emp.id == id:
                return emp
        return None

    def addEmployee(self, emp):
        self.employeeList.append(emp)

    def removeEmployee(self, emp):
        self.employeeList.remove(emp)


def TestFiles():
    netease = CompanyInfo("Netease")
    netease.addEmployee(Developer(1, "Gordon", "C#/.NET Developer"))
    netease.addEmployee(
        Manager(2, "Oneqiong", "Software Developer - ITEKJP00020644", "CEO"))
    netease.addEmployee(
        Developer(3, "Bing", ".NET Developer (Device Integration)"))

    facebook = CompanyInfo("Facebook")
    facebook.addEmployee(Developer(4, "Ken", "Sr. .NET Developer"))
    facebook.addEmployee(Developer(5, "Dur", "Full Stack Software Developer"))

    employeeList = CompanyInfo("FullList")
    employeeList.addEmployee(netease)
    employeeList.addEmployee(facebook)

    employeeList.showEmployeeInfo()


if __name__ == "__main__":
    TestFiles()
