#include <algorithm>
#include "openFile.h"
#include "countVC.h"
#include "writeFile.h"
#include "countWords.h"
#include "Colors.h"
#include "sortVC.h"
#include "printFile.h"

int main()
{   
    char choice = '1';
    std::string *words{nullptr}, nameOfFile = "";
    int wordsSize = -1;
    int V{-1}, C{-1}, N{-1};

    while(choice != '0')
    {
        std::cout << C_BLUE << "File opened: ";
        if(nameOfFile.empty()) std::cout << "NONE";
        else                   std::cout << nameOfFile;
        std::cout << C_NONE << std::endl;

        std::cout << "+=========== M E N U =============+" << std::endl;
        std::cout << "| 1         Open file           1 |" << std::endl;
        std::cout << "| 2 Count vowels and consonants 2 |" << std::endl;
        std::cout << "| 3  Sort vowels -> consonants  3 |" << std::endl;
        std::cout << "| 4  Sort consonants -> vowels  4 |" << std::endl;
        std::cout << "| 5   Sort lexicographically    5 |" << std::endl;
        std::cout << "| 6       Write in file         6 |" << std::endl;
        std::cout << "| 7       Print    file         7 |" << std::endl;
        std::cout << "| 8 Count number of repetitions 8 |" << std::endl;
        std::cout << "| 0           Exit              0 |" << std::endl;
        std::cout << "+=================================+" << std::endl;
        std::cout << "| Input: "; std::cin >> choice;
        std::cin.clear(); std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

        switch(choice)
        {
            case '1': //open file
                delete [] words;
                V = -1; C = -1; N = -1; nameOfFile = "";
                std::cout << "Found possible files:" << std::endl << system("ls") << '\r' << std::endl;
                words = openFile(wordsSize,nameOfFile);
                std::cout << std::endl;
                break;
            case '2': //count vowels & consonants
            {
                if(wordsSize == -1)
                {
                    std::cout << C_RED << "No file has been opened" << C_NONE << std::endl;
                    break;
                }
                if(V==-1)
                {
                    countVC(words, wordsSize, V, C, N);
                }

                std::cout << C_BLUE << std::endl;
                std::cout << "Vowels: " << V << std::endl;
                std::cout << "Consonants: " << C << std::endl;
                std::cout << "Non-letters: " << N << std::endl;
                std::cout << C_NONE;
                //writeFile(words,wordsSize,choice);
                std::cout << "--" << std::endl;
            }
                break;
            case '3': //sort V->C
            {
                if(wordsSize == -1)
                {
                    std::cout << C_RED << "No file has been opened" << C_NONE << std::endl;
                    break;
                }
                else if(wordsSize == 0)
                {
                    std::cout << C_BLUE << "Looks like this file is empty" << C_NONE << std::endl;
                    break;
                }
                sortVC(words,wordsSize,choice);
                std::cout << "--" << std::endl;
            }
            break;
            case '4': //sort C->V
            {
                if(wordsSize == -1)
                {
                    std::cout << C_RED << "No file has been opened" << C_NONE << std::endl;
                    break;
                }
                else if(wordsSize == 0)
                {
                    std::cout << C_BLUE << "Looks like this file is empty" << C_NONE << std::endl;
                    break;
                }
                sortVC(words,wordsSize,choice);
                std::cout << "--" << std::endl;
            }
            break;
            case '5': //sort lexicographically
            {
                if(words)
                {
                std::sort(words,words+wordsSize);
                writeFile(words,wordsSize,choice);
                std::cout << "--" << std::endl;
                }
                else
                std::cout << C_RED << "No data to sort" << C_NONE << std::endl << C_BLUE
                << "Use \"Open file\" to use this option" << C_NONE << std::endl;
            }
                break;
            case '6': //write in file
            {
                if(words)
                writeFile(words,wordsSize);
                else
                std::cout << C_RED << "No data to write" << C_NONE << std::endl;
            }
                break;
            case '7': // print file
            {
                printFile(words,wordsSize);
            }
            break;
            case '8': //count words
            {
                if(!countWords(wordsSize,nameOfFile)) break;
                //else writeFile(words,wordsSize,choice);
            }
            break;
            case '0':
                std::cout << C_BLUE << "Finishing..." << C_NONE << std::endl;
                delete [] words;
                break;
            default:
                std::cout << C_RED << "Wrong input" << C_NONE << std::endl;
                break;
        }
    }
    return 0;
}