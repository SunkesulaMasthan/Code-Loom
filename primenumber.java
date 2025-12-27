import java.util.Scanner;
class primenumber{
public static void main(String args[]){
Scanner s=new Scanner(System.in);
int n=s.nextInt();
int c=0;
for(int i=1;i<=n;i++){
if(n%i==0)
c++;
}
if(c==2)
System.out.println("Prime");
else
System.out.println("Not Prime");
}
}
/*output:7
Prime
*/
