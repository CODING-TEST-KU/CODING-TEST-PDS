package src.week1;

import java.util.*;

public class bj11652 {

    public static void main(String[] args){
        Scanner scan=new Scanner(System.in);
        int n=scan.nextInt();
        Map<Long, Integer> numbers=new HashMap<>();

        for (int i=0;i<n;i++){
            long num=scan.nextLong();
            numbers.put(num,numbers.getOrDefault(num,0)+1);
        }

        int max=0;
        long answer=Long.MAX_VALUE;

        for(Map.Entry<Long,Integer> num:numbers.entrySet()){
            long key=num.getKey();
            int count=num.getValue();
            if(max<count) {
                max=count;
                answer=key;
            }else if(max==count && answer>key){
                max=count;
                answer=key;
            }
        }

        System.out.println(answer);

    }
}
