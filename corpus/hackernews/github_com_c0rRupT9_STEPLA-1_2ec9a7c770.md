---
title: "Show HN: We built an 8-bit CPU as 2nd year EE students"
url: "https://github.com/c0rRupT9/STEPLA-1"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-18T11:40:19Z"
metadata:
  score: "82"
---

# Show HN: We built an 8-bit CPU as 2nd year EE students

> Source: hackernews | Category: news | 2026-06-18T11:40:19Z

Score: 82 | Comments: 20

Hi! me and my friends together built an 8 bit CPU implemented in Logisim purely from scratch. The control unit of this system does not implement the generic microcode ROM or any kind of RAM. This was made purely from discrete logic gates and coded the system to run different programs.<p>key features:
Custom 16-instruction Harvard ISA, 8-bit fixed 
format, 4 general purpose registers<p>Hardwired control unit built entirely from AND&#x2F;OR gate logic matrix<p>Dual-phase clocking to eliminate race conditions<p>Bootstrap Control Unit that cold-boots via ROM-to-RAM transfer
Early-exit conditional branching that saves upto 25% cycles when conditions aren&#x27;t met<p>Full design specification document with version control<p>Since this was our first time doing such teamwork and a new thing we used RISC based system that fetches an 8-bit instruction from Instruction memory 4 bits of which translate to an instruction the last two bits are for source and destination registers. 
There are a total of 4 registers in the system with two memory units namely Data SRAM and I SRAM, the system follows a Harvard architecture.<p>There are design discrepancies too since it was our first time designing such a system and on top of that completely hardwired too.<p>To solve the problem of cold booting a bootloader is present too that copies the contents of a temporary ROM into instruction RAM and then hands over the reins to the CPU.<p>We also implemented conditional branching as well as early exit branching too that only checks for zero or carry flag and branches without wasting cycles, if the conditions are not met the Program counter increments.<p>Moreover we also created a complete documentation with version control describing each necessary part assuming prior knowledge.<p>Please take a look at it at <a href="https:&#x2F;&#x2F;github.com&#x2F;c0rRupT9&#x2F;STEPLA-1" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;c0rRupT9&#x2F;STEPLA-1</a><p>For future development I want to implement a RISC CPU using FPGA&#x27;s and connect it to an actual DRAM. We are also selling the full spec document and Logisim files for $5 to fund our passion
<a href="https:&#x2F;&#x2F;tcfdiq.gumroad.com&#x2F;l&#x2F;zyyux" rel="nofollow">https:&#x2F;&#x2F;tcfdiq.gumroad.com&#x2F;l&#x2F;zyyux</a>
Thankyou!
