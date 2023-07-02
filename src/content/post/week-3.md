---
title: "Week 3 - Organize"
description: "This post is for testing and listing a number of different markdown elements"
publishDate: "2 Jul 2023"
tags: ["jrnl"]
---
# WEEKLY GOAL
- [ ] RHCSA
- [ ] CEH

# Weekly Learning


#  Day 1
## RHCSA ch1 : Setup
- Setup 
	+ Lab : Install [centos](https://app.vagrantup.com/centos/boxes/7) via [Vagrant](https://www.geeksforgeeks.org/what-is-vagrant/) in [Virtual Box]()
	+ Book : RHCSA_8 , vander San
	+ Readed : P1 > Ch1 & Ch2
	
# Day 2

## RHCSA ch2 : Exercise
__Execise : 2.1__

- Authenticate as the user who you created in Chapter 1, “Installing Red Hat Enterprise Linux” when installing your server.
- Type time ls. This executes the ls command where the Bash internal time shows information about the time it took to complete this command.
- Type which time. This shows the filename `/usr/bin/time` that was found in the $PATH variable.
- Type `echo $PATH` to show the contents of the $PATH variable. You can see that /usr/bin is included in the list, but because there also is an internal command time, the time command from the path will not be executed unless you tell the shell specifically to do so—the command in step 2 has executed the internal command for you because of command precedence.
- Type /usr/bin/time ls to run the /usr/bin/time command when executing ls. You’ll notice that the output differs completely. Ignore the meaning of the output; we’ll get back to that later. What matters for now is that you realize that these are really two different commands.

__Exercise 2-2 Using I/O Redirection and Pipes__

- Open a shell as user user and type cd without any arguments. This ensures that the home directory of this user is the current directory while working on this exercise. Type pwd to verify this.
+ Type ls. You’ll see the results onscreen.
+ Type ls > /dev/null. This redirects the STDOUT to the null device, with the result that you will not see it.
+ Type ls ilwehgi > /dev/null. This command shows a “no such file or directory” message onscreen. You see the message because it is not STDOUT, but rather an error message that is written to STDERR.
+ Type ls ilwehgi 2> /dev/null. Now you will no longer see the error message.
+ Type ls ilwehgi Documents 2> /dev/null. This shows the name of the Documents folder in your home directory while hiding the error message.
+ Type ls ilwehgi Documents 2> /dev/null > output. In this command, you still write the error message to /dev/null while sending STDOUT to a file with the name output that will be created in your home directory.
+ Type cat output to show the contents of this file.
+ Type echo hello > output. This overwrites the contents of the output file.
+ Type ls >> output. This appends the result of the ls command to the output file.
+ Type ls -R /. This shows a long list of files and folders scrolling over your computer monitor. (You might want to press Ctrl-C to stop [or wait some time]).
+ Type ls -R | less. This shows the same result, but in the pager less, where you can scroll up and down using the arrow keys on your keyboard.
+ Type q to close less. This will also end the ls program.
+ Type ls > /dev/tty1. This gives an error message because you are executing the command as an ordinary user and ordinary users cannot address device files directly (unless you were logged in to tty1). Only the user root has permission to write to device files directly.
__Exercise 2-3 Working with History__
+ Make sure that you have opened a shell as user student.
+ Type `history` to get an overview of commands that you have previously used.
+ Type some commands, such as the following: ls  pwd  cat /etc/hosts  ls -l, The goal is to fill the history a bit.
+ Open a second terminal on your server by right-clicking the graphical desktop and selecting the Open in Terminal menu option.
+ Type history from this second terminal window. Notice that you do not see the commands that you just typed in the other terminal. That is because the history file has not been updated yet.
+ From the first terminal session, press Ctrl-r. From the prompt that opens now, type ls. You’ll see the last ls command you used. Press `Ctrl-r` again. You’ll now see that you are looking backward and that the previous ls command is highlighted. Press Enter to execute it.
+ Type `history | grep cat`. The grep command searches the history output for any commands that contain the text cat. Note the command number of one of the cat commands you have previously used.
+ Type `!n`, where n is replaced by the number you noted in step 7. You’ll see that the last cat command is repeated.
+ Close this terminal by typing exit.
+ From the remaining terminal window, type history -c. This wipes all history that is currently in memory. Close this terminal session as well.
+ Open a new terminal session and type history. It may be a bit unexpected, but you’ll see a list of commands anyway. That is because history -c clears the in-memory history, but it does not remove the .bash_history file in your home directory.
__Exercise 2-4 Using Bash Completion__
+ Still from a user shell, type `gd` and press `Tab`. You’ll see that nothing happens.
+ Press Tab again. Bash now shows a short list of all commands that start with the letters gd.
+ To make it clear to Bash what you want, type i (so that your prompt at this point shows the command gdi). Press Tab again. Bash now knows what you want and opens gdisk for you. Press Enter to close the prompt that was just opened.
+ Use `cd /etc` to go to the /etc directory.
+ Type cat pas and press Tab. Because there is one file only that starts with pas, Bash knows what to do and automatically completes the filename. Press Enter to execute the command.
__Exercise 2-5 vim Practice__
- Type vim ~/testfile. This starts vim and opens a file with the name testfile in ~, which represents your current home directory.
+ Type i to enter input mode and then type the following text: cow  sheep  ox  chicken  snake  fish  oxygen
+ Press Esc to get back to command mode and type :w to write the file using the same filename.
+ Type :3 to go to line number 3.
+ Type dd to delete this line.
+ Type dd again to delete another line.
+ Type u to undo the last deletion.
+ Type o to open a new line.
+ Enter some more text at the current cursor position: tree  farm
+ Press Esc to get back into command mode.
+ Type :%s/ox/OX/g.
+ Type :wq to write the file and quit. If for some reason that does not work,use :wq!.
__Exercise 2-6 Managing the Shell Environment__
+ Open a shell in which you are user user.
+ Type `echo $LANG` to show the contents of the variable that sets your system keyboard and language settings.
+ Type `ls --help`. You’ll see that help about the ls command is displayed in the current language settings of your computer.
+ Type `LANG=es_ES.UTF-8`. This temporarily sets the language variable to Spanish.
+ Type `ls --help` again. You’ll see that now the ls help text is displayed in Spanish.
+ Type exit to close your terminal window. Because you have not changed the contents of any of the previously mentioned files, when you open a new shell, the original value of the LANG variable will be used. Open a shell as user again.
+ Verify the current value of the LANG variable by typing echo $LANG.
+ Type `vim .bashrc` to open the .bashrc configuration file.
+ In this file, add the line COLOR=red to set a variable with the name COLOR and assign it the value red. Notice that this variable doesn’t really change anything on your system; it just sets a variable.
+ Close the user shell and open a new user shell.
+ Verify that the variable COLOR has been set, by using echo $COLOR. Because the .bashrc file is included in the login procedure, the variable is set after logging in.
__Exercise 2-7 Using man -k__
+ Because `man -k 'find file'` does not give the expected result, it makes sense to look in the man page for the man command for additional information about man -k. Type `man man` to open the man page of man. Once in the man page, type /-k to look for a description of the -k option. Type n a few times until you get to the line that describes the option. You’ll see that man -k is equivalent to apropos and that you can read the man page of apropos for more details. So type q to exit this man page.
+ Type `man apropos` and read the first paragraphs of the description. You’ll see that the database searched by apropos is updated by the mandb program.
+ Type `man mandb`. This man page explains how to run mandb to update the mandb database. As you’ll read, all you need to do is type mandb, which does the work for you.
+ Type `mandb` to update the mandb database. Notice that you won’t see many man pages being added if the mandb database was already quite accurate.
__Exercise 2-8 Using info__
+  Type man ls. Type G to go to the end of the man page and look at the “See Also” section. It tells you that the full documentation for ls is maintained as a Texinfo manual. Quit the man page by pressing q.
+  Type pinfo coreutils 'ls invocation'. This shows the information about ls usage in the pinfo page. Read through it and press q when done.
__Explore Dir__
+  /usr/share/doc
+  /etcc/motd & /etc/issue




## CTF
+ netcat
### Web EXploitation
- html , css , js
- curl , wget , httpie
+ curl
```sh
curl url # fetch web
curl -o output.html url # Save Output
curl url -u "usr:psw" # Basic Auth
curl --request POST --data "mu data" url # Send Data
curl ur1 \ 
> url # curl 1 & 2
curl -O url.iso # Download File
```
- PORT
__Natas__
- curl : auth , referer 
- Browser , Inspect (Element,console,source,network) , UrlPath
0: natas0
	+ Inspect : Element , console  , Source
	+ 
1: g9D9cREhslqBKtcA2uocGHPfMZVzeFK6
	+ ShotCut Trick
2: h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7 
	+ url , path
3: G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q
	+ robots.txt
4: tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm
	- curl --referer http://natas5.natas.labs.overthewire.org/  http://natas4.natas.labs.overthewire.org/ -u "natas4:tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm"
5: Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD
	- Application > Cookie > LoggedIn : 1
6: fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR
	- Url , Path
7: jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr
	- PHP : FS , dir Struct , Mechanism
	