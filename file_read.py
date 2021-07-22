import os

curr_working_dir = os.getcwd()

#creating a file
fp = open("temp_file.txt","w")
temp_list = ["abc","def","ghi"]
for each_elem in temp_list:
    fp.write(each_elem + "\n")
fp.close()

#count num of lines in a file
fp = open("temp_file.txt","r")

file_content = fp.read() #read entire file and store in the variable
file_content_list = file_content.split("\n")
#num_lines = len(file_content_list)
count =0
for each_elem in file_content_list:
    if each_elem:
        count+=1
num_lines = count
fp.close()
print(count)

#for deleting file
#os.remove("filename here")

#check if file exists:
#os.path.exists(pathtofile) - if exists, it will return True

#delete folder (directory)
#os.rmdir("folder name")

