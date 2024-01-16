---
title: "Bash Scripting (Starter Pack)"
description: "Lets Automate our Daily Task by using Bash Scripting Scripting Scripting."
publishDate: "19 Sep 2023"
tags: ["bash","devops","script"]
---

- What is shell : hardware -> Kernel -( Shell )-> GUI
	- Check your shell : `echo $SHELL | echo $0`
	- Check available Shell : `cat /etc/shells`
- Shell Scripting : Collection of Commands & Statement (Instrution)
- abort running program : `Crtl+C`
- __SPACE__ is important part of its syntax


### Create your first bash program
1. Open terminal
  - `.sh` is extension of our program file
  - make a file called `hello.sh`
2. Input into your hello.sh file
  - The line “#!/bin/bash” is referred to as the shebang line , to tell the system to use bash as an interpreter for your script
 

### Hello World
- Create
```sh
# create 
touch sample.sh
# give permission to execute
chmod +x sample.sh
# edit 
vim sample.sh
```
- Code
```sh
#!/bin/bash
# Now print with `wcho`
echo "Hellow World !"
```
- Execute
```sh
bash sample.sh # 1. Direct : Hellow World !
./sample.sh # 2. Relative Path : Hellow World !
/home/piyush/sample.sh # 3. Absolute Path :  Hellow World !
```

### Shell
- The shell is the program we interact with when we type at a Unix command line prompt
- Unix shell programs : sh , dash , zsh , fish ; the most commonly used is bash. 
- Shell scripts can be used to automate tasks involving Unix, as well as command-line programs that run under Unix. 

### Bash
- .sh , `bash file.sh`
- permission to execute 
- shebang (#)

1. Hellow World
```sh
echo "Hello World"
```
2. Command Program
```sh
# give current location
pwd
```

### Variable
- no space between var and assign value
```sh
#!/bin/bash 
#- variable ot print
username="denysdovhan"  # declare variable
echo $username          # display value
unset username          # delete variable

local local_var="I'm a local value" # declare a variable local to a single function
export GLOBAL_VAR="I'm a global variable" #  variables accessible to any program or script

# Right way
var="Hello"
# wrong way
var = "Hello"

# types
name="Piyush"
age=20
cmd=$(whoami)

# usage
echo "Name : $name , Age : $age yr , User : $cmd" # Name : Piyush , Age : 20 yr , User : piyu

# declare
readonly var="constant variable"

```

### Comment

- `# denotes a commen`
- The value of a variable is accessed with $
- Shell variables need not be “declared” or “defined

```sh
# Single Line
<<cmm
Multiline Comment
cmm
```

### Arrays

```sh
# define arrray , by space
arr=( 1 23 "ubuntu" linux )
# usage
echo "${arr[*]}" # Display all : 1 23 "ubuntu" linux
echo "${arr[2]}" # index of 2 : ubuntu
echo "${#arr[*]}" # get length : 4
echo "${arr[*]:1}" # specific value
echo "${arr[*]:2:2}" # specific range , start from index 1 with 2 value : ubuntu linux

# Modify array
arr+=( manjaro pop ) # update array
```

### Array : Key-value

```sh
declare -A arr
arr=( [name]="Piyush" [age]=20 )
echo "My name is ${arr[name]}" # My name is Piyush
```
## Arrays
### Declaration
```sh
# eg 1
fruits[0]=Apple
fruits[1]=Pear
fruits[2]=Plum
# eg 2
fruits=(Apple Pear Plum)
```
__Expansion__
```sh
echo ${fruits[1]} # Pear
echo ${fruits[*]} # Apple Pear Plum
echo ${fruits[@]} # Apple Pear Plum
```
```sh
printf "+ %s\n" "${fruits[@]}"
# + Apple
# + Desert fig
# + Plum
```

```sh
# eg : Slice
echo ${fruits[@]:0:2} # Apple Desert fig
# eg : Delete
unset fruits[0]
echo ${fruits[@]} # Apple Desert fig Plum Banana Cherry
```



### String Opearation

```sh
str="Hello World !" # Hello World !
length=${#str} # 13
uppr=${str^^} # HELLOW WORLD !
lwr=${str,,} # hello world !
replace=${str/Hello/Goodbye} # Goodbye World !
slice=${str:2:5} # llo W
```

### User Interaction

```sh
read -p "Your Name : " name
echo Hello $name
```

### Arthimatic Operation

- Direct opr
```sh
a=10
b=2
add=$(( a + b ))
sub=$(( a + b ))
mul=$(( a + b ))
div=$(( a + b ))

```

- using let
```sh
a=10
b=2

let mul=$a*$b # 20
let add=$a+$b # 12
let a++ # 11
```

## Brace expansion
```sh
echo beg{i,a,u}n # begin began begun
echo {0..5} # 0 1 2 3 4 5
echo {00..8..2} # 00 02 04 06 08 | {start..end..steps}
```

### Conditional Statement
```sh
marks=55
if [[ $marks -gt 35 ]]; then
	echo "passed"
fi
# passed

marks=55
if [[ $marks -gt 35 ]]; then
	echo "passed"
elif [[ $marks -lt 40 ]]; then
	echo "Failed"
else
	echo "Please provide a valid value !"
fi
# If marks are greater then 35 then pass
# If marks are less then 35 then fail
```
- __Opearators__ : -eq/== , gt,lt,ge,le,ne/!=
- `-eq` : for number
- `==` : for String


### Case

```sh
echo "a : to show current date"
echo "b : to show hostname"
read -p "Choice : " word 
case $word in
	a) 
		echo Date : $(date) 
		;;
	b) 
		echo User : $(hostname) 
		;;
	*) 
		echo "not a valid input"
esac
```

### Logial Operator

```sh
# Run Commands Concurrently
cmd_1 & cmd_2
# Run CMD 2 only after CMD 1 is completed
cmd_1 && cmd_2
# Run CMD_1 or CMD_2 ( CMD_1 doest not work then run CMD_2 )
cmd_1 || cmd_2 
# Ternary opr
COND && cmd_1 || cmd2
```

- example_1
```sh
#!/bim/bash
age=20
cou="indi"
if [[ $age -ge 18 ]] && [[ $cou == "india" ]] ; then
	echo "Working !"
fi
```

### Primary and combining expressions

**Working with the file system:**

| Primary       | Meaning                                                      |
| :-----------: | :----------------------------------------------------------- |
| `[ -e FILE ]` | True if `FILE` **e**xists.                                   |
| `[ -f FILE ]` | True if `FILE` exists and is a regular **f**ile.             |
| `[ -d FILE ]` | True if `FILE` exists and is a **d**irectory.                |
| `[ -s FILE ]` | True if `FILE` exists and not empty (**s**ize more than 0).  |
| `[ -r FILE ]` | True if `FILE` exists and is **r**eadable.                   |
| `[ -w FILE ]` | True if `FILE` exists and is **w**ritable.                   |
| `[ -x FILE ]` | True if `FILE` exists and is e**x**ecutable.                 |
| `[ -L FILE ]` | True if `FILE` exists and is symbolic **l**ink.              |
| `[ FILE1 -nt FILE2 ]` | FILE1 is **n**ewer **t**han FILE2.                   |
| `[ FILE1 -ot FILE2 ]` | FILE1 is **o**lder **t**han FILE2.                   |

**Working with strings:**

| Primary        | Meaning                                                     |
| :------------: | :---------------------------------------------------------- |
| `[ -z STR ]`   | `STR` is empty (the length is **z**ero).                    |
| `[ -n STR ]`   |`STR` is not empty (the length is **n**on-zero).             |
| `[ STR1 == STR2 ]` | `STR1` and `STR2` are equal.                            |
| `[ STR1 != STR2 ]` | `STR1` and `STR2` are not equal.                        |

**Arithmetic binary operators:**

| Primary             | Meaning                                                |
| :-----------------: | :----------------------------------------------------- |
| `[ ARG1 -eq ARG2 ]` | `ARG1` is **eq**ual to `ARG2`.                         |
| `[ ARG1 -ne ARG2 ]` | `ARG1` is **n**ot **e**qual to `ARG2`.                 |
| `[ ARG1 -lt ARG2 ]` | `ARG1` is **l**ess **t**han `ARG2`.                    |
| `[ ARG1 -le ARG2 ]` | `ARG1` is **l**ess than or **e**qual to `ARG2`.        |
| `[ ARG1 -gt ARG2 ]` | `ARG1` is **g**reater **t**han `ARG2`.                 |
| `[ ARG1 -ge ARG2 ]` | `ARG1` is **g**reater than or **e**qual to `ARG2`.     |

Conditions may be combined using these **combining expressions:**

| Operation      | Effect                                                      |
| :------------: | :---------------------------------------------------------- |
| `[ ! EXPR ]`   | True if `EXPR` is false.                                    |
| `[ (EXPR) ]`   | Returns the value of `EXPR`.                                |
| `[ EXPR1 -a EXPR2 ]` | Logical _AND_. True if `EXPR1` **a**nd `EXPR2` are true. |
| `[ EXPR1 -o EXPR2 ]` | Logical _OR_. True if `EXPR1` **o**r `EXPR2` are true.|




### Loop
- `break` : break out through loop
- `continue` : direct jump to next iteration of loop

- For Loop
```sh
# ex 1 : Array
for i in 1 2 3 4 ; do
	echo $i
done
# ex 2 : Range
for i in {1..4} ; do
	echo $i
done

#ex 3 : Array String
for i in Piyush Max Eren ; do
	echo $i
done

# ex 4 : Display each item from a File
FILE="/home/piyush/sample.txt"
for itm in $(cat $FILE) ; do
	echo $itm 
done



# ex 5 : Display all file in current dir 

files=($(find . -maxdepth 1 -type f))

for item in ${files[*]}
do
  echo "------------ File : $item"
  cat $item
done

# ex 6 : diaply each  array item 
arr=(1 5 2 5 2)
LEN=${#arr[*]}
for (( i = 0; i < LEN; i++ )); do
	echo ${arr[i]}
done
```

### While Loop

```sh
# ex 1 : counting
count=0
while [[ $count -le 10 ]]; do
	let count++
	echo "Number : $count"
	sleep 1s
done

# ex 2 : Monitoring
while [[ true ]]; do
	echo "Hello"
	sleep 2s
done

# ex 3 : read content
while read str
do
	echo "--- $str"
	sleep 2s
done < sam.sh

# ex 4 : read content from CSV file , IFS : Internal_Field_Separator
while IFS="," read col_1 col_2 col_3
do 
	echo ID : $col_1
	echo Name : $col_2
	echo Age : $col_3
	echo " --- "
done < file.csv
```

### Functions

```sh
# normal fn
fn_greet(){
	echo "Hello There !"
}

fn_greet

# param fn
fn_hello(){
	echo "Hello $1"
}

fn_hello "Piyush"

# Addition
fn_add(){
	ans=$(( $1 + $2 ))
	echo "$1 + $2 = $ans"
}

fn_add 2 6

```

### Argument Passing & Shifting
### ARGUMENT
1. Direct Input : > file.sh arg1

```sh
# bash file.sh arg1 ar2 
# argumnet acess with $1 , $2 , $3 ...
echo "What you passed : "$1 $2 
echo "How many you passed : "$#
```

2. Read Input : > file.sh
```sh
read -p "Enter your age : " var 
echo $var 
```

- no. of arg : $# 
- display all args : $@ 
- display Name of your script / shell : $0
- arg_1 & arg_2 : $1 , $2
```sh
#--< ./show.sh 23 45
#!/bin/bash
for arg in "$@"
do
	echo $arg 
done
# --> 23 45
echo $1
echo $2
echo $@
shift
echo $@
```

## Command substitution
```sh
now=`date +%T`
# or
now=$(date +%T)

echo $now # 19:08:26
```

```sh
text1=" world"
echo "Hello : "$username
echo "Hello : ${txt1}"
```

```sh
cat "$FILE" # prints 1 file: `Favorite Things.txt`
```


### Usefull command
```sh
# sleep 
sleep 3s
# exit
exit 1
echo $? # 0 : success , !0 : fail
exit status $? 

```

## Streams, pipes and lists

### Streams
```sh
# output of ls will be written to list.txt
ls -l > list.txt

# append output to list.txt
ls -a >> list.txt

# all errors will be written to errors.txt
grep da * 2> errors.txt

# read from errors.txt
less < errors.txt
```

### Pipes
```sh
ls -l | grep .md$ | less
```

## Utility
sleep n : n sec
basckground_cmd &
$(cmd output)

- ex 1 : 

```sh
read -p "website link to ping : " site
ping -c 1 $site
if [[ #? -eq 0 ]]; then
	echo "Successfully Ping !"
else
	echo "Fail Ping :("
fi
```


```sh
> basename ./dir/file.txt
txt
> dirname ./dir/file.txt
dir
> realpath ./dir/file.txt
/home/piyu/Documents/dir/file.txt
```

### Check if File / Dir exist

```sh
if [[ -d dir ]]; # check if dir exist
[[ ! -d dir ]]; # check if dir not exist
if [[ -f file.txt ]]; # check if file exist
[[ ! -f file.txt ]]; # check if file not exist
```


### Bash Variable

```sh
echo $HOME
echo $PWD
echo $USER
echo $SHELL
echo $RANDOM
# NO=$(( $RANDOM % 6 + 1 )) : no. between 1 to 6
echo $UID # show your user ID
```

### Redirects

```sh
# save name of files in one 
ls > files.txt
# write file
cat > sample.txt
# append into file
cat >> sample.txt
# create a log
echo "---------" >> pings.log
date >> pings.log
ping -c 1 www.google.com >> pings.log
# redirect error
cd /root &> error.log
# redirect error into void
cd /root &> /dev/null
```

### Log messages
Logger : /var/logs/message
ex : `logger "Hey buddy"`
```sh
pacman -S syslog-ng
systemctl enable syslog-ng
systemctl start syslog-ng
```

### Debug
```sh
# enable debug
set -x
# exit script if any command fails
set -e 

```
- ex : 1
```sh
#!/bin/bash 
set -x 

my_fun(){
	echo "$1"
}

my_fun "Piyush"

# + my_fun Piyush
# + echo 'Hello Piyush'
# Hello Piyush
```

### Running SCript in bg
- `nohup ./file.sh &`


### Automate Script
1. AT
- at 02:22 PM
- at 12:00 PM 31 July 2023
```sh
at 12:09 PM
> bash /home/user/logger.sh 
> Ctrl+D

> atq : check schedule job 
> atrm <id> : to remove schedule 
```
2. Cron TAB
- crontab.guru
> contab -l : check existing job
> contab -e : edit your cron job
	- `*(minute) *(hour) *(Day) *(month) *(week:sunday=0)`
	- 16 03 * * * cd /home/user/ && ./file.sh 


### Other Utils
> cut , sed , grep , find , awk , redircetion , regex ...

### Project
> Have Pseudo Code
- neofetch
- backup
- setup : app , WM 
- ram monitoring : free
- monitoring & alert email with scheduled jobs : postfix
- If you find 6 month old dir -gt 20MB then compress & archive them all .
- 

### Practice

```sh
#!/bin/bash
#--0.0.1 > revision
#--Monday 02 October 2023 08:59:26 AM IST > date created
# Debug : set -x
# fail exit : exit 1

```

---

## Resources
- [youtube](https://youtu.be/TtGM9GfBuok)
- shc Compiler
- [E-Book](https://github.com/bobbyiliev/introduction-to-bash-scripting)
__Main__
- https://github.com/denysdovhan/bash-handbook#introduction
- https://github.com/alebcay/awesome-shell
- https://github.com/Bash-it/bash-it
- http://tldp.org/LDP/Bash-Beginners-Guide/html/
- http://dotfiles.github.io/
- https://github.com/denysdovhan/learnyoubash
- https://github.com/koalaman/shellcheck
__CMD__
- https://www.commandlinefu.com/commands/browse
- https://www.bashoneliners.com/oneliners/popular/
__Advance__
- https://tldp.org/LDP/Bash-Beginners-Guide/html/
## Examples
- http://mywiki.wooledge.org/BashPitfalls