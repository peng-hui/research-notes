### Everything Old is New Again: Binary Security of WebAssembly Daniel (Security'20)

WebAssembly (WASM) is a portable and flexible binary code format that is
touted for its safety and security. In this paper, the authors first
introduce the unique features in WASM binaries compared with native
binaries, e.g., ELF. For example, WASM binaries are statically
type-checked before being executed. WASM has *managed data*, which
contains variables and values that are directly arranged by the
underlying VM, and *unmanaged data*, one linear memory\--a single,
global array of bytes. The unmanaged data contains the zero-initialized
data, read- and writable data, and read-only data. WASM supports
indirect calls by searching them in a table section with indices from
the stack. Some of the distinguishing characteristics make WASM
vulnerable to many standard native-binary issues and special WASM
problems. Because the stack and heap are managed in the unmanaged data
area, thus an attacker can manipulate the unmanaged data to write the
memory. The native binary protection mechanisms, e.g., canary, are not
applied to WASM yet. The authors thus generalize these problems and
present three attack primitives. 1) Attacks can write to the linear
memory through stack-based buffer overflow, stack overflow, and heap
metadata corruption. 2) The execution flow can be hijacked through the
heap, the stack, and even the constant data. 3) Unexpected behaviors can
happen by modifying the indirect call targets, host environment code
injection, etc. The authors further study the scenarios attacking WASM,
such as in-browser XSS and RCE in server-side applications. To
understand how realistic the attack primitives are in practice, the
authors implement a lightweight static analysis tool to extract code
information in the WASM code. The results show that, around one third of
functions use the unmanaged stack, which is susceptible to arbitrary
memory writes and inter-frame buffer overflow; 9.8% of all call
instructions are indirect; 49.2% of all functions are type-compatible
with at least one indirect call instruction, and 48.1% of all functions
can be reached by an indirect call instruction; and the static
prior-execution type checking is less effective than modern CFI
defenses. The authors create a publicly available benchmark for helping
evaluate future work on hardening WASM.
