#include <iostream>
#include <vector>

std::vector<int> twoSum(std::vector<int>& nums, int target) {
        int i = 0;
        int j = nums.size()-1;
        int sum = 0;
        
        while(true){
            sum = nums.at(i)+nums.at(j);
            if(sum==target){
                break;
            }
            if(sum<target){
                i++;
            }else{
                j--;
            }            
        }
        std::vector<int> output={i,j};
        return output;
    }

int main(){
    std::vector<int> nums = {2,7,11,15};
    std::vector<int> output;
    output = twoSum(nums,9);
    std::cout<<'\n'<<"Output : ";
    for (int i = 0; i < output.size(); i++)
    {
        std::cout<<output.at(i)<<'\t';
    }
    std::cout<<'\n';
    return 0;
}