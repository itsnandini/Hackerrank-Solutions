import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class Solution {
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        int count = sc.nextInt();
        int[] input = new int[count];
        for(int i = 0; i < count; i++)
        {
            input[i] = sc.nextInt();
        }
        for(int i = count-1; i >= 0; i--)
        {
            System.out.print(input[i] + " "); 
        }  
    }
}
