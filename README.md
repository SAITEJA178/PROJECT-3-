# PROJECT-3-
TO CHECK THE HEAD - COWS 
legs = 16
heads = 6

for cows  in range(heads +1):
   hens = heads - cows
   
   if cows*4 + hens*2 == legs:
       print("cows =", cows)
       print("Hens =", hens)
       flag = True
       break
  
