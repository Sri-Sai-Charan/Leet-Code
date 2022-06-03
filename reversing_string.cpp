#include <iostream>
#include <vector>

void reverseString(std::vector<char>& s);

void reverseString(std::vector<char>& s) {
    int i = 0;
    int j = s.size()-1;
    while(i<j){
        std::swap(s.at(i),s.at(j));
        i++;
        j--;
    }

}

int main(){
    // const char* s[] ;
    std::vector<char> s ={'h','e','l','l','o'};
    std::cout<<"Input : ";
    for (int i = 0; i < 5; i++)
    {
        std::cout<<s.at(i);
    }
    std::cout<<'\n';
    reverseString(s);
    std::cout<<"Output : ";
    for (int i = 0; i < 5; i++)
    {
        std::cout<<s.at(i);
    }
    std::cout<<'\n';

    return 0;
}