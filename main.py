import winsound
import time

cas = (input("Napiš čas, který potřebuješ nastavit, vše udávej v sekundách: "))
konecCas = int(cas) + 1
        
for i in range(1,konecCas):
    time.sleep(1)
    print(float(i))
                            
if konecCas:
    winsound.Beep(200, 5000)
            
        
        

    
    


        

    
   



        
