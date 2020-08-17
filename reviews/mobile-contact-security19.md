---
title: Review of Security'19 'Mobile Private Contact Discovery at Scale'
date: 2019-10-14 00:31:43
type: "post"
tags:
    - security
    - research
    - review
---

##### Application
Social applications like Whatsapp, Wechat generally ask for reading the contact information and try to find other users who are using the same applications. Some friend recommendations will be sent to certain users. However, the existing and previous protocols used in this filed are not able to guarantee the security or provide time efficient in real-world applications.

The host side holds the information about the local contact information, which are always in smaller number compared with the server side.(thousands v.s. millions).
<!--more-->
##### PSI (Private set intersection)
> "In general, secure two-party computation allows parties *P<sub>1</sub>* and *P<sub> 2 </sub>* to jointly compute a publicly known function *f* on their respective inputs *X<sub>1</sub>* and *X<sub>2 </sub>* s.t. the parties learn no information from thee protocol execution but the result"

##### OT (Oblivious Transfer (Extensions))
> OT is a cryptography protocol that in its most basic form allows a sender *P<sub>1</sub>* to obliviously transfer one out of two messages (*m<sub>0</sub>*, *m<sub>1</sub>*) to receive P<sub>2</sub>based on a selection bit b chosen by *P<sub>2 </sub>*s.t. *P<sub>1</sub>* learns nothing about *b* and *P<sub>2</sub>* learns only *m<sub>b</sub>* but nothing about *m<sub>1-b</sub>*

I haven't looked through this paper, as it is kind of improvement work above **PSI**, which is raised by other previously.  And this paper apply it two a new case -- mobile contact, which has an unbalanced dataset in the server side and the host side. 

Need to read the paper on **Security'15: Phasing: Private Set Intersection Using Permutation-based Hashing**



The conclusion part on this paper still shows that it is not capable to come into practice use because it does not meet the real-world low latency demand. 

Turing awardee Prof. Yao's paper Garbled circuits should take a look, **How to Generate and Exchange Secrets(Extended Abstract)**, I will definitely benefit from it.
