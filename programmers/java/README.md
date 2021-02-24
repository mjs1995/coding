# import java.util.Arrays;
- Array.sort(변수) -정렬

- if(!변수명[].equlas(변수명[])) {
  }

- ArrayList<Integer> a1 = new ArrayList<Integer>(); list
- System.out.println("Hello Java"); 결과값 확인 
- length vs size()
```java
    public static void main(String[] args) {
    String[] arr = new String[3];
    arr[0] = "GwangJik";
    arr[1] = "KeonHo";
    arr[2] = "TaeRim";    
    for(int i = 0 ; i < arr.length ; i++){
        System.out.println("arr[" + i + "] = " + arr[i]);
    }
}
----------------------------------------
result
 
arr[0] = GwangJik
arr[1] = KeonHo
arr[2] = TaeRim

public static void main(String[] args) {
            
    ArrayList<String> list = new ArrayList<String>();
            
    list.add("GwangJik");
    list.add("KeonHo");
    list.add("TaeRim");
            
    for(int i = 0 ; i < list.size() ; i++){
        System.out.println("list[" + i + "] = " + list.get(i));
    }
            
}--------------------------------------------------
result
 
list[0] = GwangJik
list[1] = KeonHo
list[2] = TaeRim
```

- 인덱싱 리스트
```java
int min = Collections.min(arr2);       
int index_of_min = arr2.indexOf(min);
arr2.remove(index_of_min);
answer = new int[arr2.size()];
        for(int i=0; i<arr2.size(); i++ ){
            answer[i] = arr2.get(i);
        }
```
