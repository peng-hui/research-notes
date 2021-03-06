#### Paper summary
This SoK paper systematically summarizes previously proposed techniques in binary analysis, and tries to pave the road for future binary analysis especially building the base for comparison between different analysis methods. It attempts to mitigate the problem that research prototypes do not come into practical usage, and they are time-consuming to reproduce when new methods and papers come out. With such motivation, this paper implements angr, which supports and combines several analysis techniques, and evaluates them on current benchmarks and datasets.  Angr is open sourced at the same time.


#### Strengths
- provide an accessible, open, usable and effective binary analysis tool that can easily compare with others, and combine diverse binary analysis techniques and apply them on a large scale.
- open source and publicly available.
- evaluate on current datasets and benchmarks and it is effective to improve and rebuild above.


#### Weaknesses
- the VEX IR brings more instructions to the originals, which causes overheads and problem in real-world testing..
- only supports a few system calls, which means it can only support testing on several related applications, and more should be added in the future for further testing.
- built-in functions are conservative and not well modeled, or completely supported. It is always hard to re-implement built-in functions in one language to other languages, because of the native language-dependent characters and features.


#### Detailed comments, possible improvements, or related ideas
- it is good to see such an comprehensive tool being implemented to help future binary analysis and research, it eases the way to compare among different tools, especially the effectiveness and efficiency.
- more details should be added to the symbolic execution and backwards slicing parts, especially some commonly known problems like loops, and path explosion. 


#### Additional Questions
No questions, I like this paper. :)
