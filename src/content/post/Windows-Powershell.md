---
title: "Windows : Powershell"
description: "Collection of blogs  , writeUps and articles which can be really usefull"
publishDate: "29 Sep 2023"
tags: ["windows"]
---

Powershell 

## Basic
- It haa `\` slash unlike linux with `/` slash


```
pwd
cd .\Desktop\
cd ..
cd C:\Users
ls

```
### Linux vs Windows
```
Linux command	PowerShell cmdlet	Description
cat	Get-Content	Show the contents of a file
cd	Set-Location	Change directory
clear	Clear-Host	Clear contents of the terminal screen
cp	Copy-Item	Copy a file to another file
dir	Get-ChildItem	Show the files and folders in current folder
echo	Write-Output	Output text to screen
history	Get-History	Retrieve the list of previously uses commands
kill	Stop-Process	Terminate a process
ls	Get-ChildItem	Show the files and folders in the current folder
man	help	Get help for a specific command
md	mkdir / New-Item	Create a folder, mkdir
mount	New-PSDrive	Mount a temporary or persistent drive or folder
mv	Move-Item	Move a file or folder to another location or rename it
popd	Pop-Location	Change current working directory
ps	Get-Process	Retrieve running processes
pushd	Push-Location	Save the current directory and move to another
pwd	Get-Location	Show current location
rm	Remove-Item	Remove file
rmdir	Remove-Item	Remove directory
sleep	Start-Sleep	Sleep for x seconds
sort	Sort-Object	Sort output
tee	Tee-Object	Write output to file from pipe
```

## Help
```pwsh
< C + [space] > // completion
echo "Hello World !" // Print Hello World !
gal echo 
Get-Help Get-ChildItem

// cmdlets
Get-Alias
Get-ChildItem // ls ; dir 
Get-Content .\file.txt

// Pipes
Get-ChildItem | Parent
Get-ChildItem | Select-Object -Index 0 | Select-Object Name
(Get-ChildItem).Name
(Get-ChildItem).ToString()

```