#include <iostream>
#include <string>
#include <cstdio>
#include <map>

using namespace std;
map<string , int> mp;

int main()
{
	freopen("in.txt" , "r", stdin);
//	freopen("out.txt" , "w" , stdout);
	string str;
	while(cin >> str)
	{
		if(str == "*") break;
		int len = str.length() , flag = 1;
		for(int i = 0; i < len - 1; i++) {
		    mp.clear();
			for(int j = 0; j + i + 1 < len; j++) {
				string tmp = "";
				tmp += str[j];
				tmp += str[j+i+1];
				if(mp.count(tmp)) {flag = 0; break;}
				else mp[tmp] = 1;
			}
			if(!flag) break;
		}
		if(flag) cout << str << " is surprising." << endl;
		else cout << str << " is NOT surprising." << endl;
	}
}
