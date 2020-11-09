//
// Created by kirill on 29.02.2020.
//

#include "input.h"

template <typename T, typename S>
void input(T &in, S &out)
{
    while(true)
    {
        std::cout << out << std::endl;
        std::cin >> in;
        if(std::cin.fail())
        {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(),'\n');
            std::cout << "Incorrect input" << std::endl;
        }
        else
        {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(),'\n');
            return;
        }
    }
}
