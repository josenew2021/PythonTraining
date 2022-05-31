def solucion(b,n):

    n = 15
    b = 25   
    tries = 1

    while True:
        input_number = int(input("Ingrese un número: "))
        
        if input_number<0 or input_number>b:
             print("¡Te saliste del intervalo!")
             
        elif input_number > n:
            print("¡Ups! Te pasaste")
            tries+=1
            
        elif input_number < n:
            print("¡Ups! Estás por debajo")
            tries+=1
         
        
        elif input_number == n:
            print(f"¡LO LOGRASTE! Usaste {tries} intentos")
            break
           