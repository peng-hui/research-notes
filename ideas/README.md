- <s>Chrome bookmarks sync</s> **KILLED**
    - Bookmarks can sync from old version to new, some previously changed or deleted records are synced to new records/machines. XMPP protocol is open-source and widely used in lots of technical situations. Internet of things, push service. Need to confirm whether this thing is controllable.
    -  IT SEEMS TO BE AN ACCIDENT, I AM NOT ABLE TO REPLAY IN A NEW MACHINE. BUT I DID SEE THIS TWICE.
- <s>Heap exploit on PHP.</s> **KILLED**
    - The strings of php use a technology of **struct hack** to store multiple characters.But the memory is allocated on heap, and only the address returned to the pointer, so it does not have any violation. **The technique of structure hack might be safe.**
- Bug detection on LLVM/clang for C programs, like linux kernel.
    - Some papers:
    - [Pinpoint](https://www.cse.ust.hk/pg/research/projects/charlesz/pinpoint/)
    - Indirect Call from Prof. Kangjie, Best paper, CCS 2019.
    - Static analysis of Clang.
- <s>Not everything in code is shown to users on the web, like use some class to hide some information. We expect to see, these extra information is excessive, and should be removed or better hidden from  HTML. They can be inferred and reflect some sensitive info of the developer and the company/service provider. Second step is that, modify the engine to automatically identify these kinds of HMTL code and hide from users directly, which would be a defense mechanism.</s> <s>If currently the code in client side is generated locally, then it is reasonable to have these unrelated code/text inside.</s> **KILLED**
- <s>Difference between platforms. Malicious websites provide different information to different ip address/platforms. 
This kind of difference can reflect something? or they are doing so for what?? better make profit? why and how. except the layout difference.</s> **KILLED**
- <s>A fully concolic symbolic execution engine for PHP. I think our implementation on PHP-Parser should provide us more flexibility on how to evaluate some expressions.</s> Lack technical contribution.
- <s>Invisible information leakage on the browser, like some tags in css to hide.</s> **KILLED**
- Use NLP technology to analyze texts and for security research, especially for privacy related problems.
- <s>Instead of using symbolic execution, try NLP technologies to understand text descriptions and also from the source code to automatically generate code in destination language.</s> **KILLED**
    - Not sure whether it is capable for NLP.
    - Whether it can be analyzed accurately.
- It is quite interesting for PHP users to not correctly use some return values in the conditions of loop, which make it ends in advance. 
```
while ($entry = readdir($handler)) is wrong when read a file with name "0"
while(false != ($entry = readdir($handler))) # is right
```
- <s>Bug pattern in one program are more likely to appear in other apps of the same author.</s> **KILLED**
    - How to define a "same type" bug pattern? directly by vulnerability type?
- Robustness checking for code.
    - Formally describe the "correctness" behavior of an application.
    - Any case violates it can will be warned.
    - Run time defense for attacks
- Fuzzing can generate concrete inputs to trigger a bug, however, how to locate the source code of that bug might be difficult
    - Not sure.
    - Now that we have fuzzing, and we can collect a working path of a triggered bug, then the bug must because of something happened in the path.
    - However, for file system bugs, how to locate the reason is a problem.
    - I work on the direction.

- <s>Generate warning for PHP, a system research </s> **Killed. Already done**
    - Uninitialized variables in use.
    - Sometimes have bugs, e.g. uninitialized variables, but hard to find for developers.
    - Type conversion warning.

- Control a jrone
    - 5G.

- <s>Sensitive information leakage through warning and error messages.</s> **KILLED**
    - https://owasp.org/www-community/Improper_Error_Handling
    - How to measure the severity of sensitive information leakage? It is a problem.

- Concurrency bugs.
    - In web applications, there was a paper that statically studied concurrency bugs related to file/data operations. It has false positives.
    - In kernel, there are many using static analysis, symbolic execution and fuzzing to detect concurrency bugs. Some are about file systems.
    - Whether it is possible to extend the scope of web concurrency bugs to other operations, not just limited to file/data operations?
    - Whether it is possible to strengthen the fuzzing with some new technology, e.g., state-aware, etc.

- Fuzzing HTTP server
    - Concurrency fuzzing as a server handles multiple requests at the same time.
    - The input actually is limited. To traverse to other third-party Too many paths and states, how to filter out those of intersts in advance, it is possible to be fully automatic? Critical state-realted varaibles? Human efforts. Combine with static analysis to identify. Used in file system fuzzing, like generating more state-aware fuzzing.

- Data flow fuzzing. Tracking taint in the process in fuzzing.

- Maintain internal states for fuzzing?
    - Performance. It is a hard question. It is infeasible to monitor all internal states and thoroughly study and fuzz. How to do it selectively is a question.
    - Doing something like that is a hard question.
