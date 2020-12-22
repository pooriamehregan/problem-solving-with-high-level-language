#!/bin/bash

# check number of arguments
function move() {
  if [ $# -lt 2 ]; then
      echo "Not enough arguments to $0 command!"; exit
  else
      src=$1; dst=$2
  fi

  # check if directories exist
  if [ ! -d $src ] && [ ! -d $dst ]; then
      echo "Neither of given directories exist!"; exit
  elif [ ! -d $src ]; then
      echo "Directory doesn't exist: $src"; exit
  elif [ ! -d $dst ]; then
      echo "Directory doesn't exist: $dst";
      echo "Creating directory: $dst"
      mkdir $dst # directory gets created if not already exist
  fi

  # format YYYY-MM-DD-hh-mm
  dst=${2}/$(date +"%y-%m-%d-%H-%M")
  mkdir $dst

  cd $src

  # check if there is a forth argument like <*.txt>
  if [ $# -gt 2 ]; then
      files=$(ls $3)
  else
      files=$(ls)
  fi
  # move.sh each file/dir from src dir to dst dir
  for file in $files; do
      echo "Moving: ${file}"
      mv $file ${dst}
  done
}
