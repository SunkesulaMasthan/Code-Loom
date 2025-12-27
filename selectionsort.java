import java.util.Scanner;
class selectionsort{
public static void main(String args[]){
Scanner s=new Scanner(System.in);
int n=s.nextInt();
int a[]=new int[n];
for(int i=0;i<n;i++)
a[i]=s.nextInt();
for(int i=0;i<n-1;i++){
int min=i;
for(int j=i+1;j<n;j++){
if(a[j]<a[min])
min=j;
}
int t=a[i];
a[i]=a[min];
a[min]=t;
}
for(int i=0;i<n;i++)
System.out.print(a[i]+" ");
}
}
/*output:5
10 29 7 88 99
7 10 29 88 99 */
