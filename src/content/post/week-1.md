---
title: "Week 1 : Explore"
description: "This post is for testing and listing a number of different markdown elements"
publishDate: "24 Jun 2023"
tags: ["jrnl"]
---

> “It’s just pathetic to give up on something before you even give it a shot.” – Reiko Mikami


## Weekly Accomplishment
- [x] Blog Creation : [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/)
- [x] TMH : [Intro](https://sm4rty.medium.com/free-350-tryhackme-rooms-f3b7b2954b8d)
- [x] what is : [CTF](https://www.youtube.com/watch?v=UL5wWt0Pwp4&pp=ygULd2hhdCBpcyBjdGY%3D)
- [x] Linux Tool : [Tmux](https://youtu.be/DzNmUNvnB04)
- [x] Linux Util : [FTP](https://www.youtube.com/watch?v=q37lf7lTVA4&pp=ygUJbGludXggZnRw)
- [x] Linux Pratice Bandit CTF (Lv 1 - 12): [OTW](https://overthewire.org/wargames/)
- [x] [IP Adress](https://www.youtube.com/watch?v=5WfiTHiU4x8&list=PLIhvC56v63IKrRHh3gvZZBAGvsvOhwrRF)

## Vunarability
- How should i write my blog ?
	+ write-up : Documenting steps used to hack an target
	+ In Form of __Writeups__ which will get me more familar with how should a make an report
	+ I know it would be complete different think to create a write up
- Setup My Personal Portfolio
	+ setup social media
	+ setup projects (Websites)
- This week learning Path 
	+ To Explore
	+ Know what can be learend in Cyber Security
	+ What Certification ca be achived

## Steps
1. Explore the content
2. Take note of each topic
3. Arrange the note in related content 
4. Priortise according to your preference
5. Breake into blocks
6. Go indetail stufy of each block
7. Have master DB of each and every topic taken down



## Reflection
- Focus on __Health__ : exercise , food , driks
- Explore from every medium possible : discover , instagram , twitter , blogs , github etc ...
- It was a great strat for me 

## Resoucres
### Begginer CTF
+ [PICO](https://play.picoctf.org)
+ [OTW](https://overthewire.org/)
+ [VH](https://www.vulnhub.com/)
+ [H101](https://ctf.hacker101.com/ctf/)
+ [SN](https://github.com/Srinivas11789/SecurityNuggets)


---
---

## FTP
> ftp , sftp , ftps , vsftpd

[FTP (File Transfer Protocol)](https://linuxize.com/post/how-to-use-linux-ftp-command-to-transfer-files/) is a network protocol used for transferring files from one computer system to another.

```sh
ftp piyush@192.168.0.101 -p 2121 # Establish an FTP Connection 
? # cmd used under ftp
# ftp -v domain.com
get remote_file ~/own/path # download
put own_file # upload
delete file # delete
! # access local PC
exit
ls ,get,mget,put,mput,mkdir,rmdir,delete,mdelete,
bye
```

## Over The Wire
- CTF
	+ what is CTF
	+ what is OTW
- pre
	+ basic linux understanding
	+ cmd : file , find , grep
	+ SSH
	
```
Lv0 : bandit0
	- cat readme
Lv1 : NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL
	- cat ./-
Lv2 : rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
	- cat spaces\ in\ this\ filename
Lv3 : aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
	- ls -a
	- cat .hidden
Lv4 : 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe
	- cd inhere/
	- file ./*
Lv5 : lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
	- find . -size 1033c
Lv6 : P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU
	- find / -size 33c -user bandit7 -group bandit6 | grep "pas"
Lv7 : z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S
	- cat data.txt | grep -i "millionth"
Lv8 : TESKZC0XvTetK0S9xNwm25STk5iWrBvP
	- cat data.txt | sort | uniq -u
Lv9 : EN632PlfYiZbn3PhVK3XOGSlNInNE00t
	- strings data.txt | grep "="
Lv10 : G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
	- cat data.txt | base64 -d
Lv11 : 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
	- R&D : ROT13
Lv12 : JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
	- xxd -r data.txt # convert hex to binary
	- file sample # if file type is Gzip / bzip2 / tar
		+ mv sample sample.gz
		+ gunzip sample.gz
Lv13 : wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
	- ssh ,  ssh private key
Lv14 : fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
	- nc
	- https://www.youtube.com/watch?v=7_LPdttKXPc
	- http://computer.howstuffworks.com/web-server5.htm
15 : jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
```

## Next Week
+ [ ] Linux Tool : VIM
+ [ ] Networking : OSI , TCP/IP , IP , subnet , openSSl , SSH , Packet etc
+ [ ] command : netstat,netcat,nslookup,nmap,netdiscover,dig,ip,host,ping,mtr,curl,wget,http,ftp
- [ ] Web Project : 

Thank You 💚