### DeepBinDiff: Learning Program-Wide Code Representations for Binary Diffing
Analyzing binary diffing is useful for security analysis.
To match the functions and basic blocks in two binaries,
traditional approaches either statically leverage call graphs, control-flow graphs, and data-flow graphs or dynamically execute or slice the binaries.
Such techniques fall short on efficiency or scalability.
Learning-based methods have recently been proposed to achieve higher accuracy or/and better scalability.
However, existing learning-based methods have limitations of coarse-granularity, lack of program-wide dependency and basic block semantic information, and heavy dependence on training data in supervised learning.

Therefore, this paper proposes an unsupervised deep neural network based program-wide code representation learning for binary diffing.
The methodology is developed into DeepBinDiff.
In the pre-processing step, DeepBinDiff first extracts an inter-procedural CFG to obtain program-wide contextual information.
It then randomly selects at least 2 basic block level paths, i.e., random walks for distilling the semantics of tokens.
Above that, DeepBinDiff trains a token embedding from the Word2Vec Continuous Bag-of-Words model.
Each token in instructions is regarded as a word, and the two adjacent instructions are used as its context.
Feature vectors for basic blocks are generated based on the token embedding and the term frequency–inverse document frequency, which gives lower weight to those more frequent terms (tokens).
To locate similar basic blocks using the basic block embedding, DeepBinDiff first merges the two ICFGs of the two binaries into one graph and then introduces a k-hop greedy matching algorithm to find matching basic blocks.
In particular, DeepBinDiff extracts the string references, external library calls, and system calls in the terminal level of the ICFGs. It adds virtual nodes for them in the ICFGs and then links virtual notes to the two ICFGs.
The k-hop greedy matching algorithm finds matched pairs based on the similarity of neighbors starting from the virtual nodes until all k-hop neighbors of matched pairs are determined.

The evaluation compares DeepBinDiff with Asm2Vec and BinDiff. 
The authors equip Asm2Vec with the k-hop algorithm.
A variant of DeepBinDiff with contextual information excluded (DeepBinDiff-Ctx) is also included in the comparison.
The evaluation dataset includes Coreutils, Diffutils, and Findutils with a total of 113 binaries. 
The software is configured with multiple different versions and under different compiler optimization levels.
The ground truth of binary diffing is paved on the source code level analysis and manual verification.
To evaluate the effectiveness of the technique, the authors use precision and recall metrics to measure diffing results.
The results show that DeepBinDiff outperforms BinDiff and Asm2Vec for both cross-version and cross-optimization-level diffing.
The contextual information can help improve the effectiveness as well.
The case study on real-world vulnerabilities in OpenSSL demonstrates the piratical advantage for analyzing vulnerabilities.
