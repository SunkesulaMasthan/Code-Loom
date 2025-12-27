import java.util.Scanner;
class bubblesort{
public static void main(String args[]){
Scanner s=new Scanner(System.in);
int n=s.nextInt();
int a[]=new int[n];
for(int i=0;i<n;i++)
a[i]=s.nextInt();
for(int i=0;i<n-1;i++){
for(int j=0;j<n-1-i;j++){
if(a[j]>a[j+1]){
int t=a[j];
a[j]=a[j+1];
a[j+1]=t;
}
}
}
for(int i=0;i<n;i++)
System.out.print(a[i]+" ");
}
}
/*output:5
3 4 2 1 5
1 2 3 4 5 */
