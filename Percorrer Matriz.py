# Percorrer matrizes de forma simples e operando seus elementos


# Nome do projeto: Operando Matrizes 
# Linguagem: Python
# Utilizações: Variáveis, Repetições e Listas
# Autor: Rafael Lua - rafaellua13




# Matriz
vetor = [
         [1,2,3],
         [4,5,6],
         [7,8,9]
         ] 



# Soma das Colunas
print('Colunas: ')
soma = 0
for x in range(len(vetor)):
  for y in range(len(vetor[0])):
    print('->',vetor[y][x])
    soma += vetor[y][x]
  print(soma)
  soma = 0



# Soma Linhas
print()
print('Linhas: ')

soma = 0
for x in range(len(vetor)):
  for y in range(len(vetor[0])):
    print('->',vetor[x][y])
    soma += vetor[x][y]
  print(soma)
  soma = 0



# Soma Diagonal
print()
print('Diagonal: ')

soma = 0
for x in range(len(vetor)):
    print('->',vetor[x][x])
    soma += vetor[x][x]
    
print(soma)



# Soma Diagonal Inversa
print()
print('Diagonal Inversa:')

var = 0
soma = 0
for x in range(len(vetor)):   
    
    for y in range(len(vetor)-1,var-1,-1):
      
      print('->',vetor[x + var][y])  
      soma += vetor[x + var][y]

      var += 1
      
print(soma)

