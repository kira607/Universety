//
// Created by kirill on 06.03.2020.
//

#include "calck.h"

double calck(const double &v, const double &c, const char &opt)
{
    double k1;

    if(c > 0 && v > 0)
    {
        if (opt == '3') k1 = v / c;
        else            k1 = c / v;
    }
    else if(c == 0 && v > 0)
    {
        if (opt == '3') k1 = v + 1000;
        else            k1 = 0;
    }
    else if(v == 0 && c > 0)
    {
        if (opt == '3') k1 = 0;
        else            k1 = c + 1000;
    }
    else k1 = -1;

    return k1;
}