#!/bin/bash


g++ -c ../common/cpp/prime.cpp -o ../common/cpp/prime.o && g++ problem7.cpp -o problem7.out -I../common/cpp ../common/cpp/prime.o && ./problem7.out
