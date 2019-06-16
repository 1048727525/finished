#include<iostream>
#include<string>
#include<vector>
using namespace std;
struct Hoffman_Node
{
	int tag;
	char value;
	int weigh=0;
	int lson=-1;
	int rson=-1;
	int father = -1;
	string codec;
	bool sym=1;
};
bool finish = 0;
int b = 0;
void get_new_node(vector <Hoffman_Node>& nodes)
{
	for (; finish != 1;)
	{
		Hoffman_Node n;
		Hoffman_Node min1;
		Hoffman_Node min2;

		for (int i = 0; i < nodes.size(); i++)
		{
			if (nodes[i].sym)
			{
				if ((min1.weigh == 0) || (min1.weigh > nodes[i].weigh))
				{
					min1 = nodes[i];
				}
			}
		}
		nodes[min1.tag].sym = 0;

		for (int i = 0; i < nodes.size(); i++)
		{
			if (nodes[i].sym)
			{
				if ((min2.weigh == 0) || (min2.weigh > nodes[i].weigh))
				{
					min2 = nodes[i];
				}
			}
		}
		if (min2.weigh == 0)
		{
			finish = 1;
		}
		
		Hoffman_Node get_node;
		get_node.lson = min1.tag;
		get_node.rson = min2.tag;
		nodes[min1.tag].codec = "0";
		nodes[min2.tag].codec = "1";

		get_node.weigh = min1.weigh + min2.weigh;
		nodes[min2.tag].sym = 0;

		if (finish != 1)
		{
			get_node.tag = b;
			b++;
			nodes.push_back(get_node);
			nodes[min1.tag].father = get_node.tag;
			nodes[min2.tag].father = get_node.tag;
		}
	}
}

string decoder(string input, vector <Hoffman_Node>& nodes)
{
	string resualt;

	for (int i = 0;i<input.size();)
	{
		Hoffman_Node mem = nodes[nodes.size() - 1];
		while (1)
		{
			if ((input[i] == '0') && (mem.lson != -1))
			{
				mem = nodes[mem.lson];
				i++;
			}
			else if ((input[i] == '1') && (mem.rson != -1))
			{
				mem = nodes[mem.rson];
				i++;
			}
			else
			{
				resualt += mem.value;
				break;
			}
		}
	}
	return resualt;
}
void main()
{
	string a;
	cin >> a;
	char input_char[26] = { 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' };
	int input_rate[26] = { 0 };
	for each (char var in a)
	{
		input_rate[(int)var - 'a']++;
	}

	vector <Hoffman_Node> Nodes;

	for (int i = 0; i < 26; i++)
	{
		if (input_rate[i] != 0)
		{
			Hoffman_Node MyNode;
			MyNode.value = input_char[i];
			MyNode.weigh = input_rate[i];
			MyNode.tag = b;
			b++;
			Nodes.push_back(MyNode);
		}
	}

	int length = Nodes.size();
	get_new_node(Nodes);
	for (int i = 0; i < length; i++)
	{
		Hoffman_Node fa;
		fa= Nodes[i];
		for (; Nodes[fa.father].father != -1;)
		{
			Nodes[i].codec = Nodes[Nodes[i].father].codec +Nodes[i].codec ;
			fa = Nodes[fa.father];
		}
	}
	
	cout << "value" << "\t" << "weigh" << "\t" << "tag"<<"\t"<<"sym"<<"\t"<<"lson"<<"\t"<<"rson"<<"\t"<<"father"<<"\t"<<"codec"<<endl;
	for each (Hoffman_Node var in Nodes)
	{
		cout << var.value << "\t" << var.weigh << "\t" <<var.tag<<"\t"<< var.sym <<"\t"<<var.lson<<"\t"<<var.rson<<"\t"<<var.father<<"\t"<<var.codec<<endl;
	}

	string resualt;
	for each (char var in a)
	{
		for (int i = 0; i < length; i++)
		{
			if (var == Nodes[i].value)
				resualt += Nodes[i].codec;
		}
	}
	string g;
	g = decoder(resualt, Nodes);

	cout << endl;
	cout << "input: " << a << endl;
	cout << "coded: " << resualt << endl;
	cout << "decoder: " <<g<<endl;

	system("pause");
	
}