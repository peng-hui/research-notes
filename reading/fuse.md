### Title: FUSE: Finding File Upload Bugs via Penetration Testing
File upload bugs in web applications can bring severe security risks like remote code execution.
This paper proposes a penetration testing method, FUSE, to detect file upload bugs.
In particular, the authors focus on unrestricted file upload vulnerabilities and unrestricted executable file upload vulnerabilities.
FUSE contains 1) a Chain Coordinator,
2) an Upload Agent,
and 3) an Upload Validator.
In this work, the authors consider uploading PHP, JavaScript, (X)HTML, and .haccess.
The Chain Coordinator constructs a testing strategy, called a chain list that specifies how to generate mutated upload requests.
The chain list is a possible combination of all appliable mutation strategies.
The Upload Agent mutates seed files using 13 mutation strategies each tailored for different file types or request components.
The Upload Validator seeks the uploaded file URLs, and check whether the files are executable.
Not all applications expose the uploaded file URLs to end-users, therefore, a File Monitor is needed to be installed on the server-side to help validate bugs.

The authors evaluated FUSE on 33 web applications.
24 applications did not require the presence of the File Monitor.
FUSE discovered 30 previously unreported UEFU vulnerabilities and obtained 15 CVEs.
