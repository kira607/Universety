//
// Created by kirill on 04.03.2020.
//

#include "countWords.h"

bool countWords(int wordsSize, std::string nameOfFile)
{
    if (wordsSize == -1)
    {
        std::cout << C_RED << "No file has been opened" << C_NONE;
        std::cout << std::endl;
        return false;
    }
    else if (wordsSize == 0)
    {
        std::cout << C_BLUE << "Looks like this file is empty" << C_NONE << std::endl;
        return false;
    }

    std::string *wordstmp = openFile(wordsSize, nameOfFile);
    std::sort(wordstmp, wordstmp + wordsSize);
    int uniqueWords = 1, counter = 1;
    std::string mostCommonWord{"NONE"};
    int max = 1;

    for (int i = 0; i < wordsSize;)
    {
        std::cout << '[' << uniqueWords << "] ";
        if (i == wordsSize - 1)
        {
            std::cout << '\t' << counter << '\t' << wordstmp[i] << std::endl;
            break;
        }
        for (int j = i + 1; j < wordsSize; ++j)
        {
            if (wordstmp[i] != wordstmp[j])
            {
                std::cout << '\t' << counter << '\t' << wordstmp[i] << std::endl;
                if (counter > max)
                {
                    max = counter;
                    mostCommonWord = wordstmp[i];
                }
                counter = 1;
                i = j;
                ++uniqueWords;
                break;
            }
            else
            {
                ++counter;
            }

            if (j == wordsSize - 1)
            {
                i = wordsSize;
                std::cout << '\t' << counter << '\t' << wordstmp[i] << std::endl;
            }
        }
    }

    std::cout << C_BLUE << "Unique words: " << uniqueWords << std::endl;
    if (max > 1)
        std::cout << "Most common word: \"" << mostCommonWord << "\" repeated " << max << " times" << std::endl;
    else
        std::cout << "All words are repeated only once" << std::endl << C_NONE;

    std::cout << "--\n";
}