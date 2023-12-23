import winsound
import time

while True:
    cas = (input("Napiš čas, který potřebuješ nastavit, vše udávej v sekundách: "))
    try:
        
        for i in range(int(cas),-1,-1):
            if i < int(cas):
                time.sleep(1.00)
                print(float(i), end= '\r')
            else:
                print(float(i), end= '\r')                            
        
        winsound.Beep(200, 3000)
        
            
    except ValueError:
        time.sleep(1)
        print("Zadal jste neplatný formát")
        time.sleep(1)



            
        
    

    
    


        

    
   



        
