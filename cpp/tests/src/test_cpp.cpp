#include <automobile>

#include <iostream>

int main() {

    vehicles::Motorcycle c("Yamaha");

    std::cout << "Made a motorcycle called: " << c.get_name() << std::endl;

    c.ride();

    return 0;
}

