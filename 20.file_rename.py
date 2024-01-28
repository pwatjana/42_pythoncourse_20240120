import os
from datetime import datetime

files = os.listdir("text")

for file in files:
    name = file.split(".")[0]
    extension = file.split(".")[-1]
    now = datetime.now()
    name = str(now) + "_" +name+ extension
    os.rename("folder/"+ file,"folder/"+ name)