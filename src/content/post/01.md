---
title: "How to Search"
description: "One of the most important skill to master , is to know How To Research "
publishDate: "30 Sep 2023"
tags: ["research"]
---

### Lv1 : Just Google it
+ google (search) : "how to hide things inside image"
+ Content (links,pdf,blog) : you may found various information related to it
+ Keyword (Steagnography) : you find some unknow term , google those terms again 
	
### Lv2 : Vulnarability Searching
+ ExploitDB(searchsploit) , NVD , 
+ CVE : CVE-YEAR-ID_number

### Lv3 : Documentation / Man Pages
+ You may have to go through documentation to know the things , your gonna exploit
- linux : `man ssh` , `man ssh | grep "version"` , `tldr ssh`

---

## Google Dorks

To gather Information avaialbe in Public using Google Dork / Dorking / Opeartor


> intitle , intext , allintext , inurl , allinurl , site , filetype , before , after 

- The “site” operator allows you to search within a specific website
- The “intitle” operator searches for web pages with specific words or phrases in the title tag.
- The “inurl” operator searches for web pages that contain specific words or phrases in the URL. 
- The “filetype” operator allows you to search for specific file types, such as PDFs or Word documents
- The “intext” operator searches for pages that contain specific words or phrases within the body of the page
- The “related” operator is used to find web pages that are related to a specific URL
- movie: Search for information about a movie

```txt
# My Dorks
site:github.com google dorks
site:reddit.com learn chess 
intext:bash filetype:pdf

site:starbck.com inurl:admin
site:starbck.com intext:admin
bash Scripting filetype:pdf

site:www.att.com ext:php
"DB_PASSWORD" filetype:env
inurl:http site:.tv
allintext:password filetype:log after:2018 
```


__Resource__
- [Learn Basic Google Dork](https://www.freecodecamp.org/news/google-dorking-for-pentesters-a-practical-tutorial/)
- [Learn Advance Dorking](https://ahrefs.com/blog/google-advanced-search-operators/)
- [Search Dork](https://dorksearch.com/)
- [Search Code](https://grep.app/)













