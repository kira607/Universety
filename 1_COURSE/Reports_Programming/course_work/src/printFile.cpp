//
// Created by kirill on 06.03.2020.
//

#include "printFile.h"

void printFile(const std::string *words, const int &wordsSize)
{
    if (wordsSize != -1)
    {
        for (int i = 0; i < wordsSize; ++i)
        {
            std::cout << words[i] << " ";
            if ((i + 1) % 10 == 0)
                std::cout << std::endl;
        }
    }

    if(wordsSize == 0)
        std::cout << C_BLUE << "Looks like this file is empty" << C_NONE;
    if(wordsSize == -1)
        std::cout << C_RED << "No file has been opened" << C_NONE;

    std::cout << std::endl;
}