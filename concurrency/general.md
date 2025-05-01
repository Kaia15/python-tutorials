### Concurrency in Python

#### Core (Processor)
- Definition: The actual hardware unit inside a CPU that executes the instructions. There are multiple cores in modern CPUs(s).
Each core can run one thread at a time (however, with the hyper-threading technique, which makes a single core appear as two logical cores, there might be two threads running on the same core at a time).

#### Thread
- Definition: the smallest unit of execution within a process. 
- Property: 
    Multiple threads from one process share memory and resources, but they have their own instruction pointers, stacks, and registers.
    - One example of a multi-threading process: **Microsoft Word**
        - Thread 1: Format the text.
        - Thread 2: process the inputs.
        - Thread 3: control users' clicking, typing, and scrolling.
          
      ![image](https://github.com/user-attachments/assets/f49e769d-d8e6-4287-8fc1-17a44255d165)
        
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

