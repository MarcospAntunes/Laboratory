import BinarySeach.BinarySearch;
import OOP.People;
import SortAlgorithms.SortAlgorithms;
public class App {
    public static void main(String[] args) throws Exception {
      int[] array = {1,2,3,4,5,6,7};
        printValues(array);
        
        int dir = array.length - 1;
        int esq = 0;
        int meio = (esq + dir) / 2;
        
        System.out.println(BinarySearch.find(array,0, dir, 4, meio));
        System.out.println(BinarySearch.find(array,0, dir, 1, meio));
        System.out.println(BinarySearch.find(array,0, dir, 7, meio));
        System.out.println(BinarySearch.find(array,0, dir, 0, meio));

        People newPeople = new People("Marcos", "Antunes", 21987741852L);
        newPeople.setNomeCompleto();
        printNewPeope(newPeople);

      sortArray();
    }
    private static void printValues(int[] array) throws Exception {
      for(int i = 0; i < array.length; i = i + 1) {
        System.out.println(array[i]);
      }
    }
    
    private static void printNewPeope(People newPeople) {
      String nomeCompleto = newPeople.getNomeCompleto();
      long telefone = newPeople.getTelefone();
      System.out.print(nomeCompleto);
      System.out.print(telefone);
    }
    
    private static void sortArray() {
      int[] newArray = {50,20,10,5,2,40,25,30,32,30};
      SortAlgorithms newInstance = new SortAlgorithms();
      int[] sortedArray = newInstance.mergeSort(newArray);
      
      System.out.println("\nArray ordenado: " + sortedArray);
    }
    
}
