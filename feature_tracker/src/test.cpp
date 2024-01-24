#include<python3.6m/Python.h>
#include<iostream>

int main() {
    Py_Initialize();
    std::cout << "Hello, World!" << std::endl;
    return 0;
}