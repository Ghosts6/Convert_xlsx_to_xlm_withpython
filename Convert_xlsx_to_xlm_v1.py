import  jpype     

import  asposecells     

jpype.startJVM() 

from asposecells.api import Workbook

workbook = Workbook("phonebook01.xlsx")

workbook.save("phonebook01.xml")

jpype.shutdownJVM()
