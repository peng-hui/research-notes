### Web-Security [Personal summary]

I am currently working on web security (more on server-side). This is a collection of some related papers. I will simply add several sentences to summarize the paper content.

#### Server-side security
##### Attacks & Vulnerability detection
- Simulation of Built-in PHP Features for Precise Static Code Analysis (NDSS'2014) [[paper]](https://www.ndss-symposium.org/ndss2014/programme/simulation-built-php-features-precise-static-code-analysis/) [[code]](https://github.com/robocoder/rips-scanner)
    - Simulate sanitization and taint propagation of PHP built-in functions.
- Static Detection of Second-Order Vulnerabilities in Web Applications (Security'2014) :star2: **Facebook Internet Defense Prize** [[paper]](https://www.usenix.org/conference/usenixsecurity14/technical-sessions/presentation/dahse) [[code]](https://github.com/robocoder/rips-scanner)
    - New concept of second-order vulnerabilities: First store malicious data to database, and then launch attacks by database queries.
- Code Reuse Attacks in PHP: Automated POP Chain Generation (CCS'2014) [[paper]](https://dl.acm.org/doi/10.1145/2660267.2660363) [[code]](https://github.com/robocoder/rips-scanner)
    - Detect code reuse attacks in PHP (PHP Object Inject)
- FUSE: Finding File Upload Bugs via Penetration Testing (NDSS'2020) [[paper]](https://www.ndss-symposium.org/ndss-paper/fuse-finding-file-upload-bugs-via-penetration-testing/) [[code]](https://github.com/WSP-LAB/FUSE)
    - Some vulnerable web applications allow uploading files, which can be executable code files.
    - Detecting new types of bugs that haven't been studied before. 

##### Exploit generation
- Chainsaw: Chained Automated Workflow-based Exploit Generation (CCS'16) [[paper]](https://dl.acm.org/doi/10.1145/2976749.2978380)
    - Static exploit generation for PHP web applications, especially on SQLI and XSS. It is said without OOP support.
- NAVEX: Precise and Salable Exploit Generation for Dynamic Web Applications (Security'18) [[paper]](https://www.usenix.org/conference/usenixsecurity18/presentation/alhuzali) [[code]](https://github.com/aalhuz/navex)
    - Follow-up work of Chainsaw. Combine static and dynamic analysis, server-side and client-side code for exploit generation, including SQLI, XSS, EAR.
    - However, the code does not work :( in my testing.

##### Attack defense
- Rampart: Protecting Web Applications from CPU-Exhaustion Denial-of-Service Attacks (Security'18) [[paper]](https://www.usenix.org/conference/usenixsecurity18/presentation/meng)
  - Runtime defense against CPU-Exhaustion DoS attacks using a function level profiling in PHP Zend engine.


#### Client-side security

