import glob

txt_files = glob.glob("*.txt")

if txt_files:
    print(".txt files found:")
    for file in txt_files:
        print(f"- {file}")
else:
    print("No .txt files found.")
