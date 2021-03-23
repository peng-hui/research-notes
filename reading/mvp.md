### MVP: Detecting Vulnerabilities using Patch-Enhanced Vulnerability Signatures

Recurring vulnerabilities widely exist in real-world software.
Detecting recurring vulnerabilities with a low false-positive rate is challenging.
Existing general bug detection tools might not able to capture the characteristics of recurring vulnerabilities; clone-based methods, on the other hand, cannot identify the patched software.
Since patched software shows little difference with the vulnerable version, distinguishing the patched and vulnerable versions is non-trivial.

In this work, the authors further consider both the vulnerable and the patched versions of the software.
In particular, they propose MVP, a patch-enhanced signature-based approach to detecting recurring vulnerabilities.
To generate the signatures, MVP first abstracts and normalizes the functions.
It then constructs tuples of control and data dependencies as the signatures.
They reduce the false positives by modeling the signatures of both vulnerable and patched software to filter out the patched targetting software.

The authors thoroughly evaluated MVP on ten open-sourced C/C++ programs with 25,377 patches.
MVP outperformed clone-based and matching-based approaches with higher precisions and recalls.
This demonstrated the patch enhanced signature is useful.
Besides, MVP discovered 97 new recurring vulnerabilities and was assigned 23 CVE IDs.
