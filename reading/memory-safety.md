#### Paper summary 
This paper summarizes the problems existed in memory corruption, and previous/current protection techniques. It does an investigation in a wide range of security problems/attacks in memory safety, especially memory corruption. Then it evaluates the corresponding protection mechanisms for different attacks and the limitations, focusing on CPU performance, memory performance, different layers of compatibility and robustness. At last, it gives some suggestions for better adoption and future research directions above current state.

#### Strengths 
- This paper precisely explains the attack v.s. protection models in memory corruptions and how attackers generate exploits, which they claim to be a new general model. The general attack models and potential threats to programs raise attention from researcher to better understand the attacks themselves and the defenses.
- It evaluates and compares proposed mechanisms to defend against memory corruptions in performance, compatibility, and robustness. It might be the first systematical comparison work between these defense mechanisms, and it shows the problems with current policies for memory security and why sometimes stricter policies are not possible and not applied in real world.
- It then gives some suggestions to further improve based on the found in this paper.


#### Weaknesses 
- It does not provide something totally new about how to attack or how to protect above what they observe in their evaluations of different defense mechanisms, but just gives some suggestions.
- Typically, I doubt about the contributions of this paper, as this paper is more about summarizing existing works in last several decades, and it is organized more like a survey paper, it does not propose something practical and how it can help for a better memory safety, with lower performance overhead, better robustness.  

#### Detailed comments, possible improvements, or related ideas
- False positives are generally not allowed in modern operating systems so do all the methods mentioned guarantee that?  
- Method like pointer based bounds checking is able to escape from FPs and FNs, but causing unavoidable overheads, e.g. 67% with all models protected. So, it is possible to reach a acceptable balance of FPs or FNs and overheads?  
- In table II, what do the blanks and space lines mean, especially the column of compatibility.

#### Additional Questions
- How about the difficulty of deploying such approaches in different systems even if they have FNs, would it be a problem in the way of practice?

