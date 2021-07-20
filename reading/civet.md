### Civet: An Efficient Java Partitioning Framework for Hardware Enclaves

#### Summary
Hardware enclaves can protect sensitive code and data.
Putting an entire Java program into an enclave brings high overhead and is prohibitively expensive.
Partitioning a program is a common practice to reduce resource overhead.
However, it is hard for Java programs because of the large code footprint and the requirement of a runtime.
This paper overcame the challenges and proposed the first partition tool, Civet, for Java programs.
Civet is able to identify trusted code in Java programs given developer specified entry classes.
Trusted code can be run within the enclaves using a lightweight JVM runtime environment, which contains a three-generation garbage collector optimized for enclaves.
To prevent type confusion attacks and information leakage in the boundary of trusted and untrusted code, Civet is equipped with a deep type check and dynamic type tracking.


Civet uses a static context-sensitive and flow-sensitive call graph analysis and point-to analysis to identify the trusted code given the entry classes. The call graph can also help shred unreachable code. The static analysis is conservative thus guarantees code integrity and remote attestation.

Civet uses another deep type check on the inputs entering enclaves. In particular, Civet defines the parts of the input that a type can be instantiated and assigned to, and lists all data elements that can be instantiated for each type. In this way, Civet validates the types and inputs and ensures the type integrity for enclave interfaces.

To avoid data leakage from enclaves to outsides, Civet uses dynamic taint-tracking to identify whether sensitive data is leaked. Civet supports both explicit and implicit taint-tracking.

Since enclaves have limited memory resources (without considering swap), the authors study existing garbage collection (GC) mechanisms and designed a three-generation GC, especially for enclaves.

As the tool is not fully automated, the evaluation mainly considers several case studies over several representative Java applications like Hadoop.
The results demonstrate Civet can help reduce the overhead compared with non-partitioned versions.
