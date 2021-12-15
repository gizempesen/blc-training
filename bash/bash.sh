#!/usr/bin/env bash

#EXAMPLE
NAME="Gizem"
echo "Hey $NAME!"

#VARIABLES
NAME="Gizem"
echo $NAME
echo "$NAME"
echo "${NAME}!"

#FUNCTIONS
get_name() {
  echo "Gizem"
}

echo $(get_name)

#LOOPS
for ((i = 0 ; i < 10 ; i++)); do
  echo $i
done

#CONDITIONS
if [[ -z "$string" ]]; then
  echo "String is empty"
elif [[ -n "$string" ]]; then
  echo "String is not empty"
fi
