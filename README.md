### Web-Security [Personal summary]

I am currently working on web security (more on server-side). This is a collection of some related papers. I will simply add several sentences to summarize the paper content.

#### Server-side security
* Chainsaw: Chained Automated Workflow-based Exploit Generation (CCS'16) [[paper]](https://dl.acm.org/doi/10.1145/2976749.2978380)
  * Static exploit generation for PHP web applications, especially on SQLI and XSS. It is said without OOP support.

- NAVEX: Precise and Scalable Exploit Generation for Dynamic Web Applications (Security'18) [[paper]](https://www.usenix.org/conference/usenixsecurity18/presentation/alhuzali) [[code]](https://github.com/aalhuz/navex)
  - Follow-up work of Chainsaw. Combine static and dynamic analysis, server-side and client-side code for exploit generation, including SQLI, XSS, EAR.
  - However, the code does not work :( in my testing.
- Rampart: Protecting Web Applications from CPU-Exhaustion Denial-of-Service Attacks (Security'18) [[paper]](https://www.usenix.org/conference/usenixsecurity18/presentation/meng)
  - Runtime defence against CPU-Exhaustion DoS attacks using a function level profiling in PHP Zend engine.
- FUSE: Finding File Upload Bugs via Penetration Testing (NDSS'2020) [[paper]](https://www.ndss-symposium.org/ndss-paper/fuse-finding-file-upload-bugs-via-penetration-testing/)
  - Some vulnerable web applications allow uploading files, which can be executable code files.
  - Detecting new types of bugs that haven't been studied before. 

#### Client-side security

