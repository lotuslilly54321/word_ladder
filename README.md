# Word Ladder
## About
Word Ladder is a python program that solves 4-letter word ladders in a given number of moves(if possible).
## Pre Setup
1. Verify that python is set up locally by opening your Terminal and typing python and checking if an interactive shell shows up.
You should get something like this:
```
Python 2.7.12 |Anaconda 4.1.1 (x86_64)| (default, Jul  2 2016, 17:43:17) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2336.11.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
```

## Setup
1. download the .zip of this project.
2. unzip the file into a directory
3. open Terminal and ```cd``` to the directory.

## Using the Program
There are two ways to run the program

Method one:
1. type ```python word_ladder.py``` into your terminal
2. press enter
3. The program will default to using 'cool' as the start word and 'warm' as the end word. It will find answers of length 6 or less.

Method two:
1. type ```python word_ladder.py``` and then your desired start word, end word, and maximum length of the answer.
Example: ```python word_ladder.py hate love 5```
In the example above, the start word is 'hate', the end word is 'love', and the maximum length is 5.
2. press enter

## Example Output:
```
Answer:
hate
bate
late
lave
love
Answer:
hate
date
dote
dove
love
Answer:
hate
date
late
lave
love
Answer:
hate
fate
late
lave
love
Answer:
hate
gate
late
lave
love
Answer:
hate
habe
have
lave
love
Answer:
hate
hake
have
lave
love
Answer:
hate
hake
lake
lave
love
Answer:
hate
hale
have
lave
love
Answer:
hate
hame
have
lave
love
Answer:
hate
hame
home
lome
love
Answer:
hate
hame
lame
lave
love
Answer:
hate
hame
lame
lome
love
Answer:
hate
hare
have
lave
love
Answer:
hate
have
cave
cove
love
Answer:
hate
have
cave
lave
love
Answer:
hate
have
hive
live
love
Answer:
hate
have
lave
leve
love
Answer:
hate
have
lave
live
love
Answer:
hate
have
lave
love
Answer:
hate
have
nave
lave
love
Answer:
hate
have
pave
lave
love
Answer:
hate
have
rave
lave
love
Answer:
hate
have
rave
rove
love
Answer:
hate
have
save
lave
love
Answer:
hate
have
wave
lave
love
Answer:
hate
haze
have
lave
love
Answer:
hate
late
lace
lave
love
Answer:
hate
late
lade
lave
love
Answer:
hate
late
lade
lode
love
Answer:
hate
late
lake
lave
love
Answer:
hate
late
lame
lave
love
Answer:
hate
late
lame
lome
love
Answer:
hate
late
lane
lave
love
Answer:
hate
late
lane
lone
love
Answer:
hate
late
lase
lave
love
Answer:
hate
late
lase
lose
love
Answer:
hate
late
lave
leve
love
Answer:
hate
late
lave
live
love
Answer:
hate
late
lave
love
Answer:
hate
late
lite
live
love
Answer:
hate
mate
late
lave
love
Answer:
hate
mate
mote
move
love
Answer:
hate
pate
late
lave
love
Answer:
hate
pate
pave
lave
love
Answer:
hate
rate
late
lave
love
Answer:
hate
rate
rave
lave
love
Answer:
hate
rate
rave
rove
love
Answer:
hate
rate
rote
rove
love
Answer:
hate
sate
late
lave
love
Answer:
hate
sate
save
lave
love
```


