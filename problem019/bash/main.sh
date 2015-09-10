#!/bin/bash
(
	for i in {1..12};
	do
		for j in {1901..2000};
		do
			ncal $i $j | grep '^Su  1 ';
		done;
	done;
) | wc -l
