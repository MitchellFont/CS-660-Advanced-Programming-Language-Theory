# CS-660: Advanced Programming Language Theory

Welcome to the repository for my coursework in **CS-660: Advanced Programming Language Theory** at Southern New Hampshire University. 

## Course Overview
This course explores the essential and universal concepts and implementation options of modern programming languages. The primary focus is on analyzing alternative programming paradigms for efficient and concise problem-solving. Through theoretical analysis and practical applications, this coursework builds the capacity to recommend, implement, and defend the most appropriate programming language and paradigm for a given architectural challenge.

### Core Competencies
* **CS-63970**: Analyze various aspects of programming languages using fundamental and universal concepts.
* **CS-63971**: Use programming paradigms for problem-solving.
* **CS-63972**: Recommend appropriate programming languages as a solution for given problems.

---

## Key Projects & Deliverables

### 1. Domain-Specific Language (DSL) Design: HCQL
**Focus:** Language Architecture, Parsers, and Execution Models
* Designed the **Health Check Query Language (HCQL)**, a custom DSL built to automate daily server health validations.
* Prioritized strict security governance and operational safety by limiting the language to idempotent, sequential execution without complex control structures like loops.
* Architected the execution pipeline, including lexing, parsing against a formal grammar, generating an Abstract Syntax Tree (AST), and interpreting commands via a Python engine.

### 2. Modernizing Legacy Systems
**Focus:** Paradigm Shifts and Technical Debt Reduction
* Analyzed a legacy inventory management service written in ANSI C 99, identifying severe limitations related to global locks, ad hoc error handling, and manual memory management.
* Proposed and documented a complete architectural migration to **Java** using an **Object-Oriented Programming (OOP)** paradigm.
* Demonstrated how OOP encapsulation and Java's concurrent collections seamlessly resolve global lock bottlenecks while eliminating segmentation faults through automated garbage collection.

### 3. Memory Management: Go vs. Rust
**Focus:** Runtime Behavior and Concurrency Safety
* Conducted a deep-dive comparative analysis of **Go** and **Rust** for high-performance concurrent applications.
* Evaluated Go's automated runtime garbage collector and escape analysis against Rust's strict compiler-verified ownership model and zero-cost abstractions.
* Analyzed their contrasting concurrency models: Go's Goroutines and channel communication versus Rust's "fearless concurrency" and borrow checker.

### 4. Comparative Language Analysis: Microservices
**Focus:** Distributed Systems and Scalability
* Compared **Node.js** and **Go** for cloud-native backend microservices.
* Assessed Node.js's asynchronous, single-threaded event loop for I/O-bound tasks against Go's Ahead-of-Time (AOT) compilation and native Goroutine multithreading.
* Concluded with architectural recommendations based on container size, deployment maintainability, and horizontal scaling costs on commodity cloud instances.

---

* ## Technologies & Concepts Explored
* **Languages Analyzed:** Java, Python, Go, Rust, Node.js, ANSI C 99
* **Programming Paradigms:** Object-Oriented (OOP), Procedural/Imperative, Functional, Concurrent
* **Language Theory:** Lexical analysis, parsing (ANTLR/Lark), Abstract Syntax Trees (AST), interpreters vs. compilers, static vs. dynamic typing, memory models (Garbage Collection vs. Ownership), escape analysis.
