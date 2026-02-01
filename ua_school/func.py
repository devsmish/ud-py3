def otpusk():
    
    n = int(input("Дні відпустки: "))
    S = 0

    for i in range(n):
        S = S + i
        i = i + 1 
 
    print("За дні відпочинку ", n, "днів, зібрали", S, "камінців")

otpusk()