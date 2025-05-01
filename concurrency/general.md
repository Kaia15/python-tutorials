### Concurrency in Python

#### Core (Processor)
- Definition: The actual hardware unit inside a CPU that executes the instructions. There are multiple cores in modern CPU(s).
- Each core can run one thread at a time (however, with hyper-threading technique, which makes a single core appear as 2 logical cores, there migth be 2 threads running on the same core at a time).

#### Thread
- Definition: the smallest unit of execution within a process. 
- Property: 
    - Multiple threads from one process share memory and resources but they have their own instruction pointers, stacks & registers.
    - One example of multi-threading process: **Microsoft Word**
        - Thread 1: format the text.
        - Thread 2: process the inputs.
        - Thread 3: control user's clicking, typing, scrolling.
        
##### Threading Library
##### AsyncIO

#### Process
##### Threads vs Processes


#### GIL (Global Interpreter Lock)
##### What is GIL
##### GIL's role in blocking threads


#### Multi-threading vs Multi-processing
##### Can a thread (from process A) and whole process B run on the same core (processor)?
##### Which threads often require GIL, and which ones do not?

#### C-extension or Native C (Numpy) and Multi-threading

