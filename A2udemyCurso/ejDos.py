#CREAMOS UNA VARIABLE "NOTA" QUE TENGA EL VALOR DE 4.5
#CREAMOS UNA VARIABLE "TRABAJO_REALIZADO" QUE TENGA EL VALOR "SI"
#CALCULAR EL VALOR DE LA VARIABLE "NOTA_FINAL", TENIENDO EN CUENTA QUE, SI LA NOTA FINAL ES MAYOR A 4
#Y EL VALOR DE LA VARIABLE "TRABAJO RELIZADO ES IGUAL A "SI", ENTONCES "NOTA_FINAL" SERA IGUAL A
#"APROBADO", EN CASO CONTRARIO SERA IGUAL A "SUSPENSO"

nota = 4.5
trabajo_realizado = "si"

nota_final=float(input("Nota final = "))

if nota_final >= 4.0 and trabajo_realizado == "si":
    nota_final = "Aprobado"
    print(nota_final)
else:
    nota_final = "Suspenso"
    print(nota_final)