import pywhatkit 
   
try: 
  # search in google 
  pywhatkit.info("python", lines = 4) 
  print("\nBuscado exitosamente") 
   
except: 
  print("Ocurrio un Error")