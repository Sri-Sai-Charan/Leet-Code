#!/usr/bin/python3
import argparse

from numpy import array

def longestCommonPrefix(strs):
    prefix_common=strs[0]
    for current in strs:
        prefix_common = _common(prefix_common,current)

    return prefix_common
        
def _common(common,current):
    pass
    # length = min(common.length(),current.length())
    # temp = ""
    # for(char i=0; i<length; i++){
    #         if(s1[i] == s2[i])
    #             temp += s1[i];
    #         else
    #             break;
    #     }
    #     return temp;

def main():
    Parser = argparse.ArgumentParser()
    Parser.add_argument('--String_1', default='flower')
    Parser.add_argument('--String_2', default='flow')
    Parser.add_argument('--String_3', default='flight')



    Args = Parser.parse_args()
    str_array = [Args.String_1,Args.String_2,Args.String_3]
    # print(str_array)
    longestCommonPrefix(str_array)

if __name__ == '__main__':
    main()