#!/bin/bash

g++ -c ../common/cpp/prime.cpp -o ../common/cpp/prime.o && g++ problem10.cpp -o problem10.out -I../common/cpp ../common/cpp/prime.o && ./problem10.out
