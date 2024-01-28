

import httpx
from rich import print

def get_cat_ids(n: int) -> dict:
    """Get lists of cat ids from the cataas API"""
    ret[]
    for _ in range (n):
        with httpx.Client() as client:
        r = client.get("url")
        r.raise_for_status()
        ret.append({
            'id':r.json{}.get('id'),
            'ext': r.json {} ["mimetype"].split{"/"}[-1]
        })
    return ret

# pull list of obj ids
# r = httpx.get("url")
# r.json()
# output {'Tag' : ['cute'], 'mimetype' : 'image/jpeg', Size : 54254 , 'id' : 'ojfhikdmk265'}

# run debugger can check line by line
# debug consle can see result

#build module
# 1. build folder
# 2. create File
# 3. move code to new file.
# vs code will auto create from name import name
# if have output file , should create folder for output file separately
# from file name.py import function name inside name.py

#python scheduler package
#schedule.every(int).seconds.do(function name)
#schedule.every(int).day.do(function name)

#console
#update log of data output

#config.py 
#.env >> user , key api , passsword
# https://resend.com/ > generate API

# curl -sSL https://install.python-poetry.org | python3 - --uninstall
# curl -sSL https://install.python-poetry.org | python3 -
# code ~/.zshrc
# code ~/.bashrc
# poetry config virtualenvs.in-project true
# poetry add selenium chromedriver-autoinstaller
