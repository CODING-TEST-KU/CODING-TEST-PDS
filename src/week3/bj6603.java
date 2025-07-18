package src.week3;

import java.util.*;
import java.io.*;


public class bj6603 {
    public static void main(String[] args) throws IOException{

        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int n =Integer.parseInt(st.nextToken());

        Set<Integer> numSet;
        List<Integer> numList;

        while(n!=0){
            numSet=new HashSet<>();
            for(int i=0;i<n;i++){
                numSet.add(Integer.parseInt(st.nextToken()));
            }
            numList =numSet.stream().toList();

            Collections.sort(numList);

            st=new StringTokenizer(br.readLine());
            n=Integer.parseInt(st.nextToken());

        }
    }


}
