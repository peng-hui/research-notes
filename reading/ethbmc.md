### ETHBMC: A Bounded Model Checker for Smart Contracts

Smart contracts are programs deployed on the block chains that allow users to encode rules for transactions.
Smart contracts also suffer from software failures as well as logic bugs, which could potentially lead to the loss of money.
Multiple systems proposed to detect such failures did not precisely consider the inter-contract communications, memory modeling, and cryptographic primitives.
Therefore, they overestimated the analysis and brought problems like false positives.

This paper introduces ETHBMC, a symbolic execution system that has overcome the limitations of existing works.
In particular, ETHBMC models the Keccaaak256 cryptographic hash functions with a special encoding scheme.
Since the same inputs for the hash functions produce the same results, the encoding scheme enforces a constraint that can directly operate on the relevant constant values and memory regions.
Besides, the whole execution environment is well modeled, which includes the graph-based memory models, and also the memory instructions.
Similar to other symbolic execution work, a SMT solver is leveraged to solve the constraints in a bounded model checker for Parity vulnerabilities.
There are a lot of detailed and formal descriptions about memory modeling and so on, which are not covered in the summary for short.

With ETHBMC, the authors automatically scanned all accounts on the Ethereum blockchain and successfully generated 5,905 exploits, where 1,989 were potential suicidal contracts and the remaining ones could be used to extract money.
Additionally, compared with two state-of-the-art works, teEther and MAIAN, ETHBMC could generate more exploits and identify more vulnerabilities.
