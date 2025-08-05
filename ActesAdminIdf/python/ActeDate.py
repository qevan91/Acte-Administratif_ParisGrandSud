import os.path, time
pdFile = "C:/Users/e.quiatol/Downloads/del_2022_155.pdf"
print("Date de création: %s" % time.ctime(os.path.getctime(pdFile)))