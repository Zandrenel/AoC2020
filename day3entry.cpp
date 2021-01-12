#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int hits(int right,int down){
  int index = 0;
  string line;
  ifstream iFile;
  int len;
  int trees = 0;
  bool notFirstLine = false;
  int lnNum = 0;

  iFile.open("inputday3.txt");
  if (iFile.is_open()){
    while(getline(iFile, line)){
      lnNum += 1;
      if (lnNum % down == 1 || down == 1){
	//cout << lnNum % down << " " <<lnNum<<" "<<down<<" "<<right<< "\n";
	len = line.length();
	line = line;
	if (index >= len){
	    index = index-len;
	  }
	if (line[index] == '#'){
	  trees += 1;
	  line[index] = 'X';
	}
	else line[index] = 'O';
	//increment on slope
	
	index += right;

      }
      else line[index] = 'O';
      cout << line << '\n';

    }
    iFile.close();
  }
  
  else cout << "Unable to open input file";
  cout << "\n\n";
  return trees;
  
}



int main(){
  int x = hits(1,1);
  int y = hits(3,1);
  int z = hits(5,1);
  int a = hits(7,1);
  int b = hits(1,2);
  cout << "1,1: " << x << '\n';
  cout << "1,3: " << y << '\n';
  cout << "1,5: " << z << '\n';
  cout << "1,7: " << a << '\n';
  cout << "2,1: " << b << '\n';
  cout << (double)(x*y*z*a*b) << '\n';
  
  return 0;
}

