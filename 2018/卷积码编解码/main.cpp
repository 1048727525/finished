#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<math.h>
#include<cstdlib>
#include<ctime>
using namespace std;
const int inf = 100;

//string转化成int数组
vector <int> str_to_ints(string str)
{
	vector <int> a;
	for each (char var in str)
	{
		int b = var - '0';
		a.push_back(b);
	}
	return a;
}
string code(string inputcode, int o1, int k1, string* strs, int strs_length)
{
	//输入参数
	int k=k1;
	int o=o1;
	vector <string> ks;
	for (int i = 0; i < strs_length; i++)
	{
		string a;
		a = strs[i];
		ks.push_back(a);
	}

	string k_str;
	for (int i = 0; i < k; i++)
	{
		for (int n = 0; n < o; n++)
		{
			k_str += ks[n][i];
		}
	}
	
	string input_str;
	string output_str;
	vector <string> creat;
	input_str= inputcode;

	//产生生成矩阵
	int creat_r_num = (input_str.size() - 1)*o;
	int creat_l_num = 0;
	int creat_length = creat_r_num + k_str.size();
	for (int i = 0; i <input_str.size(); i++)
	{
		string le(creat_l_num,'0');
		string ri(creat_r_num, '0');
		string m = le + k_str + ri;
		creat.push_back(m);
		creat_r_num = creat_r_num - o;
		creat_l_num = creat_l_num + o;
	}
	/*
	cout << endl<<"生成矩阵如下：" << endl;
	for each (string var in creat)
	{
		cout << var << endl;
	}
	*/

	//卷积运算
	vector <int> input = str_to_ints(input_str);
	for (int i = 0; i < creat_length; i++)
	{
		string a;
		int out=0;
		for (int n = 0; n < input_str.size(); n++)
		{
			a = a + creat[n][i];
		}
		vector <int> b = str_to_ints(a);
		for (int m = 0; m < b.size(); m++)
		{
			out = out + b[m] * input[m];
		}
		if (out % 2 == 0)
			output_str = output_str + '0';
		else
			output_str = output_str + '1';
	}

	return output_str;
}

int get_hm(string a, string b)
{
	if (a.size() == b.size())
	{
		int hm = 0;
		for (int i = 0; i < a.size(); i++)
		{
			if (a[i] != b[i])
				hm++;
		}
		return hm;
	}
	else
		return -1;
	
}

int str_to_int(string input)
{
	int output=0;
	for (int i = 0; i < input.size(); i++)
	{
		if (input[i] == '1')
			output = output + pow(2, (input.size() -i- 1));
	}
	return output;
}


string get_bi_string(int a)
{
	string b;
	if (a == 0)
		return "0";
	else
	{
		while (a / 2 != 0)
		{
			if (a % 2 == 1)
			{
				b = '1' + b;
			}
			else
				b = '0' + b;
			a = a / 2;
		}
		b = '1' + b;
		return b;
	}
}


string get_out(string input,string control)
{
	for (int i = 0; i < input.size(); i++)
	{
		if (control[i] == '0')
		{
			input[i] = '0';
		}
	}
	int a = 0;
	for each (char var in input)
	{
		if (var == '1')
			a++;
	}
	if (a % 2 == 0)
		return "0";
	else
		return "1";
}

struct ver_node
{
	int inner;
	string out;
	int pace;
	int hm=inf;
	string code;
};

string get_uni(int a, string input)
{
	if (input.size() != a)
	{
		string b(a - input.size(), '0');
		return b + input;
	}
	return input;
}

string vertibi(string input,int o,int k,string* strs,int strs_length)
{
	const int N=100;
	ver_node nodes[N][N];
	string output;
	int lines[N] = { 0 };
	int line = input.size()/o;
	ver_node node;
	node.inner = 0;
	node.out = -1;
	node.hm = 0;
	nodes[0][0] = node;
	lines[0] = 1;
	line++;
	int state_num = pow(2, k);;
	vector <string> input_spilt;
	for (int i = 0; i < input.size(); i = i + o)
	{
		string a = input.substr(i, o);
		input_spilt.push_back(a);
	}

	for (int i = 0;i<line-1;i++)
	{
		for (int n = 0; n < state_num; n++)
		{
			if ((nodes[i][n].inner) > 0 || (nodes[i][n].inner == 0))
			{
				int inner0 = nodes[i][n].inner >> 1;
				int inner1 = nodes[i][n].inner >> 1;
				inner1 = inner1 + pow(2, k - 1);
				ver_node node0;
				ver_node node1;
				node0.inner = inner0;
				node0.pace = 0;
				node1.inner = inner1;
				node1.pace = 1;

				string maker0 = "0" + get_uni(k, get_bi_string(nodes[i][n].inner));
				string maker1 = "1" + get_uni(k, get_bi_string(nodes[i][n].inner));

				string out0;
				string out1;
				for (int i = 0; i < strs_length; i++)
				{
					out0 = out0 + get_out(maker0, strs[i]);
				}
				for (int i = 0; i < strs_length; i++)
				{
					out1 = out1 + get_out(maker1, strs[i]);
				}
				node0.out = out0;
				node1.out = out1;
				node0.hm = nodes[i][n].hm+get_hm(node0.out, input_spilt[i]);
				node1.hm = nodes[i][n].hm+get_hm(node1.out, input_spilt[i]);
				node0.code = nodes[i][n].code + '0';
				node1.code = nodes[i][n].code + '1';
				if(node0.hm<nodes[i + 1][node0.inner].hm)
					nodes[i + 1][node0.inner] = node0;
				if (node1.hm<nodes[i + 1][node1.inner].hm)
					nodes[i + 1][node1.inner] = node1;
				lines[i + 1] = lines[i + 1] + 2;
			}
		}
	}
	int min = nodes[line - 1][0].hm;
	ver_node min_node = nodes[line - 1][0];
	
	for (int i = 0; i < state_num; i++)
	{
		if (nodes[line - 1][i].hm < min)
			min_node = nodes[line - 1][i];
	}
	output = min_node.code;
	return output;
}

string creat_mis(int num, string input)
{
	srand((unsigned)time(0));
	int a=rand() % input.size();
	
	for (int i = 0; i < num; i++)
	{
		if (input[a] == '0')
			input[a] = '1';
		else
			input[a] = '0';
		int b = a;
		while (a==b)
		{
			b = rand() % input.size();
		}
		a = b;
	}
	return input;
}

void main()
{
	const int num=2;
	string input = "10111";
	//string b[num] = {"00","10","11"};
	string b[num] = {"111","101"};
	int o = 2;
	int k = 3;
	string coded_res = code(input, o, k, b, num);
	cout << "("<<o<<","<<"1,"<<k<<")" << "   " << "input: " << input<<"   "<<"registers: ";
	for each (string var in b)
	{
		cout << var << " ";
	}
	cout << endl;
	cout<<"coded: "<< coded_res<<endl<<endl;
	string right_ans = vertibi(coded_res, o, k - 1, b, num);
	cout<<"lossless:"<<endl<<"decoded: "<< right_ans<<endl<<endl;

	int num1 = 0.1*coded_res.size();
	cout << "error rate=0.1" << "   "<<"mistakes number="<<num1<<endl;
	cout << "right: "<<coded_res << endl;
	string mis1 = creat_mis(num1, coded_res);
	cout << "errro: "<< mis1 <<endl;
	cout << "decoded: " << vertibi(mis1, o, k - 1, b, num)<<endl<<endl;

	int num2 = 0.15*coded_res.size();
	cout << "error rate=0.15" << "   " << "mistakes number=" << num2 << endl;
	cout << "right: " << coded_res << endl;
	string mis2= creat_mis(num2, coded_res);
	cout << "errro: " << mis2 << endl;
	cout << "decoded: " << vertibi(mis2, o, k - 1, b, num) << endl<<endl;

	int num3 = 0.2*coded_res.size();
	cout << "error rate=0.2" << "   " << "mistakes number=" << num3 << endl;
	cout << "right: " << coded_res << endl;
	string mis3 = creat_mis(num3, coded_res);
	cout << "errro: " << mis3 << endl;
	cout << "decoded: " << vertibi(mis3, o, k - 1, b, num) << endl<<endl ;
	
	system("pause");
}