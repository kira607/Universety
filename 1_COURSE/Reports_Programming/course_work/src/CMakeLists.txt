cmake_minimum_required(VERSION 3.15)
project(kr)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17 -Wall")

set(SOURCE_FILES
        main.cpp
        input.cpp
        input.h
        openFile.cpp
        openFile.h
        countVC.cpp
        countVC.h
        writeFile.cpp
        writeFile.h
        countWords.cpp
        countWords.h
        Colors.h
        sortVC.cpp
        sortVC.h calck.cpp calck.h printFile.cpp printFile.h)

add_executable(kr ${SOURCE_FILES})

