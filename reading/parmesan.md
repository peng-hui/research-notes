#### Title: ParmeSan: Sanitizer-guided Greybox Fuzzing

Code coverage guided fuzzers usually attempt to investigate and cover new code blocks, while they actually overestimate the target of bug coverage, i.e., not all code are relevant to bugs.
Previously, compiler sanitizers are integrated into fuzzers to detect and confirm bugs, while the instrumentations they made can be used as a better matrix to guide the fuzzing process. 
In this work, the authors propose ParmeSan, a fuzzing pipeline that utilizes the compiler sanitizers to speed up fuzzing.
ParmeSan consists of three components: 1) target acquisition, 2) dynamic CFG and 3) the fuzzer on the top.
First, the target acquisition collects interesting targets by comparing the code difference when equipped with and without sanitizer.
A preliminary study demonstrates the strong inconsistency between the bugs and sanitizer checks.
Because some sanitizers might instrument too many basic blocks, the authors propose to use profile-guide pruning, and complexity-based pruning to remove less interesting targets.
Second, to steer the execution, the dynamic CFG is incrementally constructed at run time through data flow analysis (DFA) to measure the distance for prioritizing the seeds in the input queue.
Besides, ParmeSan binds the input bytes and the reachability of the target to prioritize certain bytes for mutation.
Third, ParmeSan employs a DFA-enhanced input mutation. ParmeSan also enables efficient bug detection by a *lazysan* technique, where the bloated instrumented code is only executed when the desired target check is reached.

The evaluation compared ParmeSan with directed fuzzers on a benchmark of known CVEs, and demonstrated that ParmeSan could find bugs much faster.
Besides, in the context of coverage-guided fuzzers, ParmeSan outperformed both AFLGo and Angora.
The statistics of branch coverage showed that,
in all cases except one, ParmeSan could find bugs with much less code coverage.
The choices of sanitizers allow ParmeSan to especially detect certain types of bugs, while sanitizers can have a diverse impact on performance improvement.
Last, ParmeSan also detected new bugs that the state-of-the-art fuzzers failed to find.
