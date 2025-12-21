#plagiarism Detection using the difflib library where you could see the amount of Words matching one another in the read 
#demo1 contents are as follows : 
          #Hey this is my First ever Python Proejct and i am quite a lot happy 
          #Thank you 2025 ..
#demo2 contents are as follows:
         #Hey i am using Python and it's kinda really crazy experience 
         #What do u think ...
from difflib import SequenceMatcher
with open("demo1.txt") as one_file, open("demo2.txt") as two_file:
    data_file1=one_file.read()
    data_file2=two_file.read()
    mactches=SequenceMatcher(None,data_file1,data_file2).ratio()
    print(f"The plagiarized content is {mactches*100}% ")