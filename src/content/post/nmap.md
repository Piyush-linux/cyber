---
publishDate: "14 Aug 2023"
title: "Nmap"
description: "This post is to get you use to Nmap scanning as well as script which can be run on the services with open ports"
tags: ["hack"]
---

- Used as recon tool

- Host discovery
- Port discovery / enumeration
- Service discovery
- Operating system version detection
- Hardware (MAC) address detection
- Service version detection
- Vulnerability / exploit detection, using Nmap scripts (NSE)
- Nmap IDS / Portscan Detection & Scan Time Optimisation

```sh
nmap -sS 192.168.1.1 => SYN scan
nmap -sT 192.168.1.1 => TCP scan
nmap -sU 192.168.1.1 => UDP scan
nmap -sY 192.168.1.1 => SCTP scan
nmap -A 192.168.1.1 => Aggressive scan
```

---

- https://medium.com/@dandobusiness/a-guide-to-ethical-hacking-understanding-nmap-7aea71f65554
- https://highon.coffee/blog/