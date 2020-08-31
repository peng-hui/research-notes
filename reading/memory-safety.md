==+== ENGG 5105/CSCI 5470 Paper Review Form
==-== DO NOT CHANGE LINES THAT START WITH "==" UNLESS DIRECTED!
==-== For further guidance, go to:
==-== http://course.cse.cuhk.edu.hk/~csci5470/

==+== =====================================================================
==+== Begin Review
==+== Paper #1
==-== Title: SoK: Eternal War in Memory

==+== Reviewer: LI, Penghui, 1155137827

==+== A. Overall merit
==-== Choices:
==-==    1. Reject
==-==    2. Weak reject
==-==    3. Weak accept
==-==    4. Accept
==-==    5. Strong accept
==-== Enter the number of your choice:  3


==+== B. Reviewer expertise
==-== Choices:
==-==    1. No familiarity
==-==    2. Some familiarity
==-==    3. Knowledgeable
==-==    4. Expert
==-== Enter the number of your choice: 1


==+== C. Paper summary 
This paper summarizes the problems existed in memory corruption, and previous/current protection techniques. It does an investigation in a wide range of security problems/attacks in memory safety, especially memory corruption. Then it evaluates the corresponding protection mechanisms for different attacks and the limitations, focusing on CPU performance, memory performance, different layers of compatibility and robustness. At last, it gives some suggestions for better adoption and future research directions above current state.

==+== D. Strengths 
1. This paper precisely explains the attack v.s. protection models in memory corruptions and how attackers generate exploits, which they claim to be a new general model. The general attack models and potential threats to programs raise attention from researcher to better understand the attacks themselves and the defenses.
2. It evaluates and compares proposed mechanisms to defend against memory corruptions in performance, compatibility, and robustness. It might be the first systematical comparison work between these defense mechanisms, and it shows the problems with current policies for memory security and why sometimes stricter policies are not possible and not applied in real world.
3. It then gives some suggestions to further improve based on the found in this paper.


==+== E. Weaknesses 
1. It does not provide something totally new about how to attack or how to protect above what they observe in their evaluations of different defense mechanisms, but just gives some suggestions.
2. Typically, I doubt about the contributions of this paper, as this paper is more about summarizing existing works in last several decades, and it is organized more like a survey paper, it does not propose something practical and how it can help for a better memory safety, with lower performance overhead, better robustness.  

==+== F. Detailed comments, possible improvements, or related ideas
1. False positives are generally not allowed in modern operating systems so do all the methods mentioned guarantee that?  
2. Method like pointer based bounds checking is able to escape from FPs and FNs, but causing unavoidable overheads, e.g. 67% with all models protected. So, it is possible to reach a acceptable balance of FPs or FNs and overheads?  
3. In table II, what do the blanks and space lines mean, especially the column of compatibility.

==+== G. Additional Questions
1. How about the difficulty of deploying such approaches in different systems even if they have FNs, would it be a problem in the way of practice?

==+== End Review

