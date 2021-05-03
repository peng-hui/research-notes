### SmartVerif: Push the Limit of Automation Capability of Verifying Security Protocols by Dynamic Strategies

Security protocols provide secure communications on insecure networks by applying cryptographic primitives.
Verifying security protocols and preventing design flaws are important.
However, existing verification solutions suffer from non-termination or false attacks due to the global states, unbounded sessions, abstraction, etc.
In this work, the authors design SmartVerif that uses dynamic strategy instead of static one during the verification.
In particular, SmartVerif tries to find a path with complete and correct proof.
Each node in the path (proof) represents a supporting lemma that is necessary for proving its parent node and finally a security property.
To find the lemmata automatically and smartly, SmartVerif introduces Deep Q Network (DQN) to select support lemma according to the historical incorrect paths 
Since a loop in a path can result in non-termination in path searching, SmartVerif detects loops to estimate the correctness of a proof path and label incorrect paths.

The evaluation aims to demonstrate the effectiveness of SmartVerif compared with existing tools.
In particular, SmartVerif outperforms other verification tools and achieves 100% success rate in verifying all testing security protocols.
Besides, SmartVerif is fully automated.
It is highly efficient, finishing most protocols with around 25 epochs and well solves the path/time explosion problem.
To understand the efficacy of the dynamic strategy, SmartVerif is compared with two naive searching algorithms--DFS and BFS.
It shows much better performance with less time used and higher quality nodes generated. 
