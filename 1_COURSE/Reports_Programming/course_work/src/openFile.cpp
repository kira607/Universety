//
// Created by kirill on 29.02.2020.
//

#include "openFile.h"

std::string* openFile(int &wordsSize, std::string &name)
{
    std::string *words;
    std::string nameOfFile, tmpstr;

    if(name.empty())
    {
        std::cout << "Input name of file: ";
        std::cin >> nameOfFile;
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(),'\n');
    }
    else
    {
        nameOfFile = name;
    }

    std::ifstream fin;
    fin.open(nameOfFile);

    if (fin.is_open()) {
        if(nameOfFile.empty())std::cout << C_BLUE << "File \"" << C_RED << nameOfFile << C_BLUE << "\" opened successfully" << C_NONE << std::endl;
        name = nameOfFile;
    }
    else {
        std::cout << C_RED << "Error: could not open file \"" << nameOfFile << "\"" << C_NONE << std::endl;
        wordsSize = -1;
        return nullptr;
    }
    wordsSize = 0;


    for (fin >> tmpstr; !fin.eof(); fin >> tmpstr) {
        ++wordsSize;
    }
    if(!nameOfFile.empty())std::cout << wordsSize << " words found" << std::endl;

    fin.close();
    fin.open(nameOfFile);

    words = new std::string[wordsSize];

    for (int i = 0; i < wordsSize; ++i) {
        fin >> tmpstr;
        words[i] = tmpstr;
        //std::cout << words[i] << std::endl;
    }

    fin.close();

    return words;
}