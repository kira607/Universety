#include <iostream>
#include <random>

std::mt19937 Rand(time(nullptr));

int main()
{
int size;
do{
std::cout << "Enter size of array(greater than 1): ";
std::cin >> size;
}while(size <= 1);

std::cout << "Ok, size is " << size << std::endl;

int arr[size][size];

char choice;
bool goOn = true;

while(goOn)
{
    std::cout << "How do I fill array?" << std::endl;
    std::cout << "1     Randomly      " << std::endl;
    std::cout << "2      With 1       " << std::endl;
    std::cout << "3   From 0 to max   " << std::endl;
    std::cout << "4     By myself     " << std::endl;
    std::cout << "Input: ";
    std::cin >> choice;

    switch(choice)
    {
    case '1':
        for(int i = 0; i < size; ++i)
        {
            for(int j = 0; j < size; ++j)
            {
                arr[i][j] = -100 + Rand()%201;
            }
        }
        goOn = false;
        break;
    case '2':
        for(int i = 0; i < size; ++i)
        {
            for(int j = 0; j < size; ++j)
            {
                arr[i][j] = 1;
            }
        } 
        goOn = false;
        break;
    case '3':
        for(int i = 0; i < size; ++i)
        {
            for(int j = 0; j < size; ++j)
            {
                arr[i][j] = i*size+j;
            }
        } 
        goOn = false;
        break;
    case '4':
        for(int i = 0; i < size; ++i)
        {
            for(int j = 0; j < size; ++j)
            {
                std::cout << '[' << i << "][" << j << "]: ";
                std::cin >> arr[i][j];
            }
        } 
        goOn = false;
        break;
    default:
    break;
    }
}

std::cout << "Original array:" << std::endl;
for(int i = 0; i < size; ++i)
{
    for(int j = 0; j < size; ++j)
    {
        std::cout << arr[i][j] << '\t';

    }
    std::cout << std::endl;
}

int num;
std::cout << "Enter number to multiply theese elements:" << std::endl <<
             "* * * -" << std::endl <<
             "* * - -" << std::endl <<
             "* - - -" << std::endl <<
             "- - - -" << std::endl <<
             "Input: ";
std::cin >> num;

for(int i = 0; i < size; ++i)
{
    for(int j = 0; j < size - 1 - i; ++j)
    {
        arr[i][j] *= num;
    }
}

std::cout << "New array:" << std::endl;
for(int i = 0; i < size; ++i)
{
    for(int j = 0; j < size; ++j)
    {
        std::cout << arr[i][j] << '\t';
    }
    std::cout << std::endl;
}

return 0;
}