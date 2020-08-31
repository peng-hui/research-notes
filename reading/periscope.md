---
title: Review of PeriScope-An Effective Probing and Fuzzing Framework for Hardware-OS boundary
date: 2020-03-09 16:38:13
tags:
    - research
    - security
    - review
---

很长一段时间看paper都是大概扫过problem + methodology，对于文章具体的，具体细节没有很关注。常常老板问我一些细节的时候我总不能回答。这次看了NDSS'19的PeriScope，觉得还是蛮有意思的。

这是一篇非常系统安全的文章，没有炫酷的ML算法和巧妙设计(可能没有什么实际影响力的)problem statement。但不得不说，作为一篇系统安全文章，我非常喜欢。
<!--more-->

###### Background

外围设备和OS之间的交互的常见方式

- 中断
- Memory-Mapped I/O
- Direct Memory Access (DMA)

已有的研究一般需要1）相应的硬件设备 2）虚拟机来模拟。

###### Threat model

Compromised peripheral devices can sent arbitrary data to drivers.  

###### Methods

- 检测驱动初始化时创建页的API，并标注所创建的页
- 将这些页设置成 un-present in page table，触发page fault.
- 在page-fault的handler里面进行fuzzing
- Complete dynamic testing.

我非常喜欢这篇paper，是因为里面提到的基本上所有的背景内容我都了解，但是我并没有能够发现这个问题并发top。其次，这个designer是非常聪明的，他的implementation虽然可能有些tricky，但是却能够带来好处，比如device-agnostic. 而且非常直接而且有效。

我比较好奇的是，paper中提到检测漏洞的标志是crash the kernel. 这个标准是不是有些局限呢？是否可以扩大这个范围，利用一些其他的指标来判断？常见的fuzzing OS kernel的工具一般都是这样设计的吗？

Fuzzing OS 触发漏洞之后重启OS，一些shallow的漏洞会组织Fuzzing到更深的地方。如何防止已知的漏洞。

Fuzzing states. Fuzz a program and try multiple inputs. One invalid input might not trigger a bug because states set by previous inputs.

An invalid input triggers a bug, but it is hard to understand the bug if without other global state information about the system.
