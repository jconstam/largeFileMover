#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 [rootPath]"
    exit 1
fi

if [ ! -e "$1" ]; then
    echo "$1 is not a valid path"
    exit 1
fi

ROOT_DIR=$(realpath $1)/testing

echo "Creating Root Directory $ROOT_DIR"
mkdir -p $ROOT_DIR

echo "Creating Test File 1"
dd if=/dev/urandom of=$ROOT_DIR/test1.avi bs=1M count=1 &> /dev/null

echo "Creating Test File 2"
dd if=/dev/urandom of=$ROOT_DIR/test2.mkv bs=1M count=10 &> /dev/null

echo "Creating Test File 3"
dd if=/dev/urandom of=$ROOT_DIR/test3.jpg bs=1M count=100 &> /dev/null

echo "Done"