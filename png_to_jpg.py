##
##import os
##from PIL import Image
##start_path = 'C://Users//kesav//Downloads//PQR//dataset//JPEGImages' # current directory
##for path,dirs,files in os.walk(start_path):
##    for filename in files:
##        
##        val=os.path.join(path,filename)
##        print(val[:-4])
##        im1 = Image.open(val)
##        im1.save(val[:-4]+'.jpg')
##        
##
import os
from PIL import Image
start_path = 'C://Users//kesav//Downloads//PQR//dataset//JPEGImages//' # current directory
for path,dirs,files in os.walk(start_path):
    for filename in files:
        val=os.path.join(path,filename)
        if val[:-4]=='.png':
            os.remove(val[:-4]+'.png')
        
