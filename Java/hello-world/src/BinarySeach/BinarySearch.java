package BinarySeach;

interface BinarySearchProps {
  public static String find(int[] array, int esq, int dir, int elem, int meio) {
    return "";
  };
  
}

public class BinarySearch implements BinarySearchProps {
  public static String find(int[] array, int esq, int dir, int elem, int meio) {
    int current = (int) array[meio];

    if (esq > dir) {
      return "Elemento não encontrado";
    }
    
    if (current == elem) {
      StringBuffer sb = new StringBuffer();
      sb.append("O item buscado esta no índice: ");
      sb.append(meio);

      String result = sb.toString();

      return result;
    } else if (current < elem) {
      esq = meio + 1;
      meio = (esq + dir) / 2;
      
      return find(array, esq, dir, elem, meio);
    } else if (current > elem) {
      dir = meio - 1;
      meio = (esq + dir) / 2;
      
      return find(array, esq, dir, elem, meio);
    }
    
    return "";
  }
}
