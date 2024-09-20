#crear tipos de datos para generar comparacion 
num1 = 2
num2 = 5
#OP
#AND
print(num1 == num2 and num1 >= num2)#V
print(num1 == num2 and num1 > num2)#F
print(num1 < num2 and num1 > num2)#F
print(num1 < num2 and num1 == num2)#F
######################
#nombre = input("Digite el usuario: ")
#contra = input ("Digite la contaseña: ")
#print(nombre == "jose" and contra >= "jose1!")#V
#OR
print(num1 == num2 or num1 <= num2)#V
print(num1 <= num2 or num1 > num2)#F
print(num1 > num2 or num1 > num2)#F
print(num1 < num2 or num1 == num2)#F

#NOT
print(not True)#F
print(not False)#V