import os
# from pathlib import Path

path: str = r'C:\Users\Administrator\Desktop\imgs'
# osDir = Path(path)
# print(os.listdir(osDir))

lst1 = os.listdir(path)
print(type(lst1))

# for i in lst1:
#     print(i)

print(len(lst1))