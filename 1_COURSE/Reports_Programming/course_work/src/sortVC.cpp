//
// Created by kirill on 06.03.2020.
//

#include "sortVC.h"

void sortVC(std::string *words, const int &wordsSize, char &opt)
{
    if(opt != '3' && opt != '4')
    {
        std::cout << C_RED << "Error: could not detect sort option" << C_NONE << std::endl;
        return;
    }

    int Vowels[wordsSize];
    int Consonants[wordsSize];
    //int Non_letters[wordsSize];

    for (int i = 0; i < wordsSize; ++i)
    {
        Vowels[i] = 0;
        Consonants[i] = 0;
        //Non_letters[i] = 0;

        for(auto c : words[i])
        {
            if(c == 'a' || c == 'e' || c == 'i' || c == 'y' ||
               c == 'o' || c == 'u' || c == 'A' || c == 'Y' ||
               c == 'E' || c == 'I' || c == 'O' || c == 'U')
                Vowels[i] += 1;
            else if(isalpha(c))
                Consonants[i] += 1;
            //else
                //Non_letters[i] += 1;
        }
        /*
        if(Vowels[i] == 0) std::cout << "\e[31m";
        std::cout << "{tmp}" << words[i] << " \t\tVowels:" << Vowels[i] << std::endl;
        std::cout << "\e[0m";
         */

        double k1, k2;

        k1 = calck(Vowels[i],Consonants[i],opt);

        if(i>0)
        {
            for(int j = 0; j < i; ++j)
            {
                k2 = calck(Vowels[j],Consonants[j],opt);

                if(k2 < k1)
                {
                    int vtmp = Vowels[i];
                    Vowels[i] = Vowels[j];
                    Vowels[j] = vtmp;

                    int ctmp = Consonants[i];
                    Consonants[i] = Consonants[j];
                    Consonants[j] = ctmp;

                    std::string stmp = words[i];
                    words[i] = words[j];
                    words[j] = stmp;
                }
            }
        }
    }
    /*
    for(int i = 0; i < wordsSize; ++i)
    {
        double k3 = calck(Vowels[i],Consonants[i],opt);
        std::cout << k3 << " ";
        if((i+1)%15==0) std::cout << std::endl;
    }
    std::cout << std::endl;
    */

    writeFile(words,wordsSize,opt);
}