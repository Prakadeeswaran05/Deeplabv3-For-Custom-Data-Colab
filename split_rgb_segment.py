import glob
import shutil
import os

src_dir = "C:\\Users\\kesav\\Downloads\\pics"
dst_dir = "C:\\Users\\kesav\\Downloads\\jpeg"
for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
    
    if 'L' in jpgfile:
        
        val=jpgfile.replace('_L','1')
        os.rename(jpgfile,val)
        shutil.copy(val, dst_dir)
        os.remove(val)
    
    else:
        
        
         
        val=jpgfile[:-4]+'1'+jpgfile[-4:]
        os.rename(jpgfile,val)
        shutil.copy(val,dst_dir)
            
     

        
        
for jpgfile in glob.iglob(os.path.join(src_dir, "*.png")):
    if 'L' in jpgfile:
        
        val=jpgfile.replace('_L','1')
        os.rename(jpgfile,val)
        shutil.copy(val, dst_dir)
        os.remove(val)
    
    else:
        
         
        val=jpgfile[:-4]+'1'+jpgfile[-4:]
        os.rename(jpgfile,val)
        shutil.copy(val,dst_dir)
    
    
        
    
            
    
