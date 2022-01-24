import os
missing_files = []
num_list = []
for num in range(len(os.listdir(r"C:\Users\PC\OneDrive\바탕 화면\PYTHON WORKSPACE\MY_PROJECT\Animal-face classification\Animal-Face-Classification\images\valid\rabbit"))):
    num_list.append(num)
files = os.listdir(r"C:\Users\PC\OneDrive\바탕 화면\PYTHON WORKSPACE\MY_PROJECT\Animal-face classification\Animal-Face-Classification\images\valid\rabbit")
for n in num_list:
    if "토끼상{}.jpg".format(n) in files:
        continue
    else:
        missing_files.append(n)

print("missing_files:",missing_files)