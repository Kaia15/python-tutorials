1. What is an interpreter?

  A skilled artisan must understand the tools with which they work. A carpenter needs to understand saws and planes. A chef needs to understand knives and pots. A programmer, among other tools, needs to understand the compilers that implement the programming languages they use.
  
  A full understanding of compilation requires a full course or two. So here, we will take a necessarily brief look at how to implement programming languages. The goal is to understand some of the basic implementation techniques, to demystify the tools you’re using. Although you might never need to implement a full general-purpose programming language, it’s highly likely that at some point in your career you will want to design and implement some small, special-purpose language. Sometimes those are called domain-specific languages (DSLs). What we cover here should help you with that task.
  
  A compiler and an interpreter are programs that implement a programming language. However, they differ in their implementation strategy.
  
  A compiler’s primary task is translation. It takes as input a source program and produces as output a target program. The source program is typically expressed in a high-level language, such as Java or OCaml. The target program is typically expressed in a low-level language, such as MIPS or x86 assembly. Then the compiler’s job is done, and it is no longer needed. Later, the OS helps to load and execute the target program. Typically, a compiler results in higher-performance implementations.
  
  An interpreter’s primary task is execution. It takes as input a source program and directly executes that program without producing any target program. The OS loads and executes the interpreter, and the interpreter is then responsible for executing the program. Typically, an interpreter is easier to implement than a compiler.
  
  It’s also possible to implement a language using a mixture of compilation and interpretation. The most common example of that involves virtual machines that execute bytecode, such as the Java Virtual Machine (JVM) or the OCaml virtual machine (which used to be called the Zinc Machine). With this strategy, a compiler translates the source language into bytecode, and the virtual machine interprets the bytecode.
