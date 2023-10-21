#include <iostream>
using namespace std;
int func(int x)
{
    int rem,cnt=0;
    while(x>0)
    {
        rem=x%10;
        if(rem==0)
        {cnt+=1;}
        else
        { break;}
        x=x/10;
    }
    return(cnt);
}
int main()
{
    int num;
    cout<<"Enter a number : ";
    cin>>num;
    cout<<"number of trailing zeroes : "<<func(num)<<endl;
    return 0;
}
