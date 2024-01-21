'''
#Method 1
import rich
d= {
    "cat" : "เเมว",
    "rat" : "03",
    "bat" : "เเมว",
}
print(d)
"""
output
{'cat': 'เเมว', 'rat': '03', 'bat': 'เเมว'}
"""
rich.print(d)
"""
output
{
    'cat': 'เเมว',
    'rat': '03',
    'bat': 'เเมว'
}
"""
'''

# Method 2
from rich import print
d= {
    "cat" : "เเมว",
    "rat" : "03",
    "bat" : "เเมว",
}
print(d)
"""
output
{
    'cat': 'เเมว',
    'rat': '03',
    'bat': 'เเมว'
}
"""