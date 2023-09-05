#include <iostream>
using namespace std;

int main()
{
	int E=1,S=1,M=1;
	int e,s,m;
	int count =0;
	cin >> e >> s >> m;

	for(E,S,M; ; E++,S++,M++)
	{	
		if(E%16==0)
			E=1;
		if(S%29==0)
			S=1;
		if(M%20==0)
			M=1;
		count++;

		if(E==e && S==s && M==m)
		{
			cout << count << endl;
			return 0;
		}
	}
}