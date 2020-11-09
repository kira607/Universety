//
// Created by kirill on 29.02.2020.
//

#include "writeFile.h"

void writeFile(std::string *words, unsigned int wordsSize, char opt)
{
    std::ofstream fout;
    std::string nameOfFile;

    switch(opt)
    {
        case '2':
        {
            nameOfFile = "count.txt";
        }
        break;
        case '3':
        {
            nameOfFile = "VtoC.txt";
        }
        break;
        case '4':
        {
            nameOfFile = "CtoV.txt";
        }
        break;
        case '5':
        {
            nameOfFile = "lex.txt";
        }
        break;
        case '6':
        {
            std::cout << "Input name of file: ";
            //input(nameOfFile, "Input name of file:");
            std::cin >> nameOfFile;
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(),'\n');
        }
        break;
        case '8':
        {
            nameOfFile = "NumOfRep.txt";
        }
        break;
        default:
        {
            std::cout << C_RED << "Error: Could not detect option number" << std::endl <<
                      "Terminating..." << C_NONE << std::endl;
        }
        return;
    }

    if(opt == '6')
    {
        std::fstream test(nameOfFile, std::ios::in);
        if (test.is_open()) {
            std::cout << C_RED << "File \"" << nameOfFile << "\" already exists!" << C_NONE << std::endl;
            std::cout << C_BLUE << "Are you sure want to rewrite \"" << nameOfFile << "\"? (y,n): " << C_NONE;
            char ch;
            std::cin >> ch;
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            if (ch != 'y') {
                std::cout << C_RED << "Terminating..." << C_NONE << std::endl;
                test.close();
                return;
            } else
                std::cout << C_BLUE << "Opening..." << C_NONE << std::endl;
        }

        test.close();
    }

    fout.open(nameOfFile);

    if (fout.is_open())
        std::cout << C_BLUE << "File \"" << nameOfFile << "\" opened successfully" << C_NONE << std::endl;
    else {
        std::cout << C_RED << "Error: could not open file \"" << nameOfFile << "\"" << C_NONE << std::endl;
        return;
    }

    for(int i = 0; i < wordsSize; ++i)
    {
        fout << words[i] << " ";
        if((i+1)%10 == 0)
        fout << std::endl;
    }

    std::cout << C_BLUE << "Changes has been written to " << nameOfFile << C_NONE << std::endl;

    fout.close();

}