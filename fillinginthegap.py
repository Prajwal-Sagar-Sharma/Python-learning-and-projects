# Write a program that finds all files with a given prefix, such as spam001.txt, 
# spam002.txt, and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt). 
# Have the program rename all the later files to close this gap.
# As an added challenge, write another program that can insert gaps 
# into numbered files so that a new file can be added
import os,re
class Cheker:
    def __init__(self,path):
        self.path=path
    def file_checking(self,file_name):
        file_checking_pattern=r'\w+\d+\.txt'
        value=re.search(file_checking_pattern,file_name)
        if value:
            return True
        return False
    def number_finder(self,file_name):
        pattern=r'\d+'
        value=re.findall(pattern,file_name)
        return int("".join(value))
    
    def file_initial_word(self,file_name):
        pattern=r'[^0-9]+'
        value=re.search(pattern,file_name)
        return value.group()
    def file_with_patterns(self):
        os.chdir(self.path)
        files=[i for i in os.listdir()  if os.path.isfile(i) ]
        return ([i for i in os.listdir() if self.file_checking(i) ])

    def gap_remover(self):
        files_with_pattern=self.file_with_patterns()
        initial_number=self.number_finder(files_with_pattern[0])
        print(initial_number)
        for i in range(1,len(files_with_pattern)):
            current_file_number=self.number_finder(files_with_pattern[i])
            if current_file_number-1!=initial_number:
                file_word=self.file_initial_word(files_with_pattern[i])
                print(file_word)
                os.rename(files_with_pattern[i],f"{file_word}{initial_number+1}.txt")
            initial_number+=1


    def gap_filler(self):
        files_with_pattern=self.file_with_patterns()
        gaps=[]
        initial_number=self.number_finder(files_with_pattern[0])
        for i in range(1,len(files_with_pattern)):
            current_file_number=self.number_finder(files_with_pattern[i])
            if current_file_number-1!=initial_number:
                gaps.extend(range(initial_number+1,current_file_number))
            initial_number+=1
        initial_word=self.file_initial_word(files_with_pattern[0])
        for i in set(gaps):
            open(f'{initial_word}{i}.txt','w').close()
        


path='E:\My Python Journey\Project'  


checker=Cheker(path)
checker.gap_filler()


