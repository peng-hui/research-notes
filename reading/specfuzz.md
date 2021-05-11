### Title: SpecFuzz Bringing Spectre-type vulnerabilities to the surface
Speculative execution vulnerabilities (e.g., Spectre) are a microarchitectural attack exploiting the branch speculations in the CPU architectures.
In the high-performance pipeline design,
modern CPUs speculatively execute certain following instructions when encountering data or control hazards.
The prediction made for the program control flow might not necessarily be correct; 
the execution then roll back to recover the program states.
However, the results in the mispredicted paths are kept in hardware buffers, e.g., Reorder Buffer (ROB) and can be revealed through additional side-channel attacks.

Since the mispredicted paths are corrected at the CPU architecture level, they are not visible at the program level.
Therefore, program-level detection methods cannot identify such vulnerabilities.
In this work, the authors propose a simulator that brings spectre-type bound-check-bypass vulnerabilities to the surface thus existing detection tools can recognize them.
In particular, they simulate the program behaviors in CPU at the program level by inserting inverted terminators to the basic blocks following conditional statements.
The inverted terminators first try to execute the mispredicted paths (just as CPUs do) and then roll back to the normal execution.
The rollback is done by a process level state saving and restoring, i.e., all registers and memory are saved before going through the mispredicted paths and restored.
The authors also handle the nested simulations.
The misprediction simulator is integrated into a fuzzing framework, namely SpecFuzz.
SpecFuzz is assisted with enhanced program level checkers to detect vulnerabilities.

SpecFuzz was evaluated on bound-check-bypass vulnerabilities and it was able to identify all of them.
It outperformed the state-of-the-art works (e.g., Spectector) and achieved a conservative instrumentation overhead.