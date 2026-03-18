---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/exc__handle_8h_source.html
original_path: doxygen/html/exc__handle_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exc\_handle.h

[Go to the documentation of this file.](exc__handle_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_EXC\_HANDLE\_H\_

8#define ZEPHYR\_INCLUDE\_EXC\_HANDLE\_H\_

9

10/\*

11 \* This is used by some architectures to define code ranges which may

12 \* perform operations that could generate a CPU exception that should not

13 \* be fatal. Instead, the exception should return but set the program

14 \* counter to a 'fixup' memory address which will gracefully error out.

15 \*

16 \* For example, in the case where user mode passes in a C string via

17 \* system call, the length of that string needs to be measured. A specially

18 \* written assembly language version of strlen (arch\_user\_string\_len)

19 \* defines start and end symbols where the memory in the string is examined;

20 \* if this generates a fault, jumping to the fixup symbol within the same

21 \* function will return an error result to the caller.

22 \*

23 \* To ensure precise control of the state of registers and the stack pointer,

24 \* these functions need to be written in assembly.

25 \*

26 \* The arch-specific fault handling code will define an array of these

27 \* z\_exc\_handle structures and return from the exception with the PC updated

28 \* to the fixup address if a match is found.

29 \*/

30

31struct z\_exc\_handle {

32 void \*start;

33 void \*end;

34 void \*fixup;

35};

36

37#define Z\_EXC\_HANDLE(name) \

38 { name ## \_fault\_start, name ## \_fault\_end, name ## \_fixup }

39

40#define Z\_EXC\_DECLARE(name) \

41 void name ## \_fault\_start(void); \

42 void name ## \_fault\_end(void); \

43 void name ## \_fixup(void)

44

45#endif /\* ZEPHYR\_INCLUDE\_EXC\_HANDLE\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [common](dir_7cbd25c8850fe30be392200e83a608be.md)
- [exc\_handle.h](exc__handle_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
