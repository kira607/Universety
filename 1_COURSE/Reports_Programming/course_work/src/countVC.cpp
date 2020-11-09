//
// Created by kirill on 29.02.2020.
//

#include <iostream>
#include "countVC.h"

void countVC(const std::string *words, const int wordsSize, int &V, int &C, int &N)
{
    V = 0; C = 0; N = 0;
    for(int i = 0; i < wordsSize; ++i)
    {
        for(auto c : words[i])
        {
            if(c == 'a' || c == 'e' || c == 'i' || c == 'y' ||
               c == 'o' || c == 'u' || c == 'A' || c == 'Y' ||
               c == 'E' || c == 'I' || c == 'O' || c == 'U')
                ++V;
            else if(isalpha(c))
                ++C;
            else
                ++N;
        }
    }
}