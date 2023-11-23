import os
circuloPath = os.path.dirname(os.path.abspath(__file__))
print(circuloPath)
circuloPath = circuloPath + '\\persons_data'
print(circuloPath)
circuloPath = circuloPath.replace("\\","/")
print(circuloPath)