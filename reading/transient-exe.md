
#### Paper summary
Transient execution has been proposed several years before, and brings serious threat to modern CPUs/Computer Architectures, including Intel, AMD and ARM. 
However, for the defense, in both software and hardware layers, there is still a lot of work. 
Systematic overview and summary are necessary to the right direction for future research.
In this paper, the authors present a systematization of transient execution attacks, and the possible defense mechanisms.
They classify current transient attacks and uncover some un-investigated exploitable attacks.
After that, an evaluation is done about the defense.

#### Strengths
This paper precisely introduce different types of transient attacks, especially Spectre and Meltdown, and the main cause of them, 
they are categorized in the way how attacker bypass the security protection methods, and this paper introduces a new classification to uncover those serious transient attacks.
There are over 10 types of Spectre and Meltdown transient attacks mentioned and attached with specific details about the reasons and real-word impact on each on them. 
Gadget analysis in real world softwares are used as comparisons with this paper, the decision tree shows the gadget analysis and classification fit more in this work.
Further evaluation presents the drawbacks of currently proposed defenses for Spectre and Meltdown.

#### Weaknesses
It seems that it is not able to enumerate all types of transient attacks at the time like today as transient attacks are just raised several years ago, there is still such potential to further exploit.
No new defense technology is raised in this work.

#### Detailed comments, possible improvements, or related ideas
I would prefer to see more demonstrations about the pipelines/re-order execution of multi-processors CPUs, including graphs and texts. 
Currently
Future work part in the paper currently only focuses on Meltdown-type attacks without Spectre, and others.
Possible to add more potential and vulnerable techniques that are because of the design/optimization of CPU.
