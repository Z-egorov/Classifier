import pandas as pd
import sys

file_path = "/home/zhenia/Muzhichki/engine/data.txt"

df = pd.read_csv(file_path, header = None)
df.columns = ["site", "theme"]
df.to_csv('data.csv', index = None)

print("Exported")
sys.stdout.flush()
