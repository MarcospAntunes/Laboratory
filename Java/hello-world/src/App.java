import BinarySeach.BinarySearch;
public class App {
    public static void main(String[] args) throws Exception {
      int[] array = {1,2,3,4,5,6,7};
        printValues(array);
        
        int dir = array.length - 1;
        int esq = 0;
        int meio = (esq + dir) / 2;
        
        System.err.println(BinarySearch.find(array,0, dir, 4, meio));
        System.err.println(BinarySearch.find(array,0, dir, 1, meio));
        System.err.println(BinarySearch.find(array,0, dir, 7, meio));
        System.err.println(BinarySearch.find(array,0, dir, 0, meio));
    }
    private static void printValues(int[] array) throws Exception {
      for(int i = 0; i < array.length; i = i + 1) {
        System.err.println(array[i]);
      }
    }
}
