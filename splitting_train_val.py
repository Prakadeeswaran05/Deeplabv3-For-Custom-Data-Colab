


import os



full_path_to_images ='C:\\Users\\kesav\\Downloads\\jpeg'


print(os.getcwd())


os.chdir(full_path_to_images)


print(os.getcwd())

# Defining list to write paths in
p = []


for current_dir, dirs, files in os.walk('.'):
    # Going through all files
    for f in files:
        # Checking if filename ends with '.jpeg'
        if f.endswith('.png') or f.endswith('.jpg'):
       
            
            path_to_save_into_txt_files = f[:-4]
            print(f[0:10])                                   
            p.append(path_to_save_into_txt_files + '\n')



p_test = p[:int(len(p) * 0.25)]
p_train = p[int(len(p) * 0.25):]

with open('train.txt', 'w') as train_txt:
    # Going through all elements of the list
    for e in p_train:
        # Writing current path at the end of the file
        train_txt.write(e)


with open('test.txt', 'w') as test_txt:
    # Going through all elements of the list
    for e in p_test:
        # Writing current path at the end of the file
        test_txt.write(e)
with open('trainval.txt', 'w') as trainval_txt:
    # Going through all elements of the list
    for e in p:
        # Writing current path at the end of the file
        trainval_txt.write(e)        
        

