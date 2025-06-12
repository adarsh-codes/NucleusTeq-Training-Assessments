def merge_files(files,merge_file):
    with open(merge_file,'a+') as m_file:
        for file in files:
            with open(file,'r+') as i_file:
                m_file.write(i_file.read())

files = ['file.txt','file2.txt']
merge_files(files,'merged.txt')

