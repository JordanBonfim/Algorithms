
n = int(input("Digite o número: "))
div=[]
for i in range(1,int(n/2)+1):
    if(n%i==0):
        div.append(i)
soma=0
for j in div:
    soma+=j
if(soma==n):
    print("Número perfeito")
else:
    print("Não é um número perfeito")
