from operator import concat

def buscaBinaria(lista: list, esq, dir, elem, meio = None):
  if meio == None:
    meio = (esq + dir) / 2;
  
  current = lista[int(meio)];

  if esq > dir:
    return "Elemento não encontrado";

  if current == elem:
    return concat("O item buscado esta no índice: ", str(int(meio)));
  elif current < elem:
    esq = meio + 1;
    return buscaBinaria(lista, esq, dir, elem, meio=(esq + dir) / 2);
  elif current > elem:
    dir = meio - 1;
    return buscaBinaria(lista, esq, dir, elem, meio=(esq  +dir) / 2);
    
  return;


array1 = [1,2,3,4,5,6,7,8,10]
array2 = ["a","b","c","d","e","f","g","h","i"]

print(buscaBinaria(array1, 0, len(array1) - 1, 5));
print(buscaBinaria(array2, 0, len(array1) - 1, "a"));
print(buscaBinaria(array2, 0, len(array1) - 1, "f"));