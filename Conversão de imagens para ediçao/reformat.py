
from PIL import Image
import sys,os
from path import Path

 # Criei esse script para salvar imagens em outros formatos, no caso jpg para png, em quantidades
 #diversas.

#print(Path("rename_save.py").abspath())

p = str(Path("rename_save.py").abspath())
print(p)
tam=len(p)
p=p[-tam:-14] 

#print('***',p)

listarq=os.listdir(p)
limagem=('.jpeg','.png')

for el in listarq:
    
    try:
        if el.lower().endswith(limagem)==True:
            print(el)
            #print(el.find('.'))
            pos=el.find('.')
            nnome='new_'+el[0:pos]+'.png'
            print(nnome)
     
            im=Image.open(el) 
            im.save(nnome,format='PNG',save_all=True)

    except OSError:   
            print("Nenhuma imagem encontrada no diretorio")

