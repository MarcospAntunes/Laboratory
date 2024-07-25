package SortAlgorithms;
import java.util.ArrayList;
import java.util.Arrays;

interface SortAlgorithmsProps { 
  public int[] mergeSort(int[] arr); 
}

public class SortAlgorithms implements SortAlgorithmsProps {
  private int[] arr;
  private int left;
  private int right;
  
  public void SortAlgorithms(int[] arr) {
    this.arr = arr;
  }
  
  private static int[] slice(int[] arr, int start, int end) {
    int[] slice = new int[end - start];
    
    for(int i = 0; i < slice.length; i++) {
      slice[i] = arr[start + i];
    }
    
    return  slice;
  }
  
  private int[] merge(int[] left, int[] right) {
    ArrayList<Integer> resultArray = new ArrayList<Integer>();
    int leftIndex = 0;
    int rightIndex = 0;
    
    while(leftIndex < left.length & rightIndex < right.length) {
      if(left[leftIndex] < right[rightIndex]) {
        resultArray.add(left[leftIndex]);
        leftIndex++;
      } else {
        resultArray.add(right[rightIndex]);
        rightIndex++;
      }
    }
    
    int[] arrayListToArray = new int[resultArray.size()];
    for(int i = 0; i < resultArray.size(); i++) {
      arrayListToArray[i] = (int) resultArray.get(0);
    }
    
   return arrayListToArray;
  }
  
  public int[] mergeSort(int[] arr) {
    
    if(arr.length == 1) {
      return  arr;
    }
    
    int middle = (int) Math.floor((arr.length / 2));
    int[] left = slice(arr, 0, middle);
    int[] right = slice(arr, middle, arr.length);
    
    int[] array1 = mergeSort(left);
    int[] array2 = mergeSort(right);
    
    int[] array = merge(array1, array2);
    
    return array;
  }
}
