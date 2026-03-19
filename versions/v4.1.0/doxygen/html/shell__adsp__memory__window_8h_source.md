---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/shell__adsp__memory__window_8h_source.html
original_path: doxygen/html/shell__adsp__memory__window_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_adsp\_memory\_window.h

[Go to the documentation of this file.](shell__adsp__memory__window_8h.md)

1/\*

2 \* Copyright (c) 2024 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef SHELL\_ADSP\_MEMORY\_WINDOW\_H\_\_

8#define SHELL\_ADSP\_MEMORY\_WINDOW\_H\_\_

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11#include <[zephyr/shell/shell.h](shell_2shell_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

17extern const struct [shell\_transport\_api](structshell__transport__api.md) [shell\_adsp\_memory\_window\_transport\_api](shell__adsp__memory__window_8h.md#a47c6df5cd7aaf460925783c10db2d5de);

18

19struct [sys\_winstream](structsys__winstream.md);

20

[ 22](structshell__adsp__memory__window.md)struct [shell\_adsp\_memory\_window](structshell__adsp__memory__window.md) {

[ 24](structshell__adsp__memory__window.md#a730dbada8e6804b6eeadfa278971ad4d) [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) [shell\_handler](structshell__adsp__memory__window.md#a730dbada8e6804b6eeadfa278971ad4d);

25

[ 26](structshell__adsp__memory__window.md#a398c24153b3263c74fe995a3c369a4cc) struct k\_timer [timer](structshell__adsp__memory__window.md#a398c24153b3263c74fe995a3c369a4cc);

27

[ 29](structshell__adsp__memory__window.md#a1baf124df654fc375612f6530652285d) void \*[shell\_context](structshell__adsp__memory__window.md#a1baf124df654fc375612f6530652285d);

30

[ 32](structshell__adsp__memory__window.md#a00650a08293ddbc232002d36a9d5dffb) struct [sys\_winstream](structsys__winstream.md) \*[ws\_rx](structshell__adsp__memory__window.md#a00650a08293ddbc232002d36a9d5dffb);

33

[ 35](structshell__adsp__memory__window.md#a89d8688c922ce5b7ccb93e04d4e6d68a) struct [sys\_winstream](structsys__winstream.md) \*[ws\_tx](structshell__adsp__memory__window.md#a89d8688c922ce5b7ccb93e04d4e6d68a);

36

[ 38](structshell__adsp__memory__window.md#aa9809847f068296c4f610d93b288ec54) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [read\_seqno](structshell__adsp__memory__window.md#aa9809847f068296c4f610d93b288ec54);

39};

40

[ 41](shell__adsp__memory__window_8h.md#a2d5483ee279894ca82bc14b41c3d3745)#define SHELL\_ADSP\_MEMORY\_WINDOW\_DEFINE(\_name) \

42 static struct shell\_adsp\_memory\_window \_name##\_shell\_adsp\_memory\_window;\

43 struct shell\_transport \_name = { \

44 .api = &shell\_adsp\_memory\_window\_transport\_api, \

45 .ctx = &\_name##\_shell\_adsp\_memory\_window, \

46 }

47

[ 56](shell__adsp__memory__window_8h.md#a03636e7b928b9c6a21d54270ba95480b)const struct [shell](structshell.md) \*[shell\_backend\_adsp\_memory\_window\_get\_ptr](shell__adsp__memory__window_8h.md#a03636e7b928b9c6a21d54270ba95480b)(void);

57

58#ifdef \_\_cplusplus

59}

60#endif

61

62#endif /\* SHELL\_ADSP\_MEMORY\_WINDOW\_H\_\_ \*/

[shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d)

void(\* shell\_transport\_handler\_t)(enum shell\_transport\_evt evt, void \*context)

**Definition** shell.h:646

[kernel.h](kernel_8h.md)

Public kernel APIs.

[shell.h](shell_2shell_8h.md)

[shell\_backend\_adsp\_memory\_window\_get\_ptr](shell__adsp__memory__window_8h.md#a03636e7b928b9c6a21d54270ba95480b)

const struct shell \* shell\_backend\_adsp\_memory\_window\_get\_ptr(void)

This function provides pointer to shell ADSP memory window backend instance.

[shell\_adsp\_memory\_window\_transport\_api](shell__adsp__memory__window_8h.md#a47c6df5cd7aaf460925783c10db2d5de)

const struct shell\_transport\_api shell\_adsp\_memory\_window\_transport\_api

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[shell\_adsp\_memory\_window](structshell__adsp__memory__window.md)

Memwindow based shell transport.

**Definition** shell\_adsp\_memory\_window.h:22

[shell\_adsp\_memory\_window::ws\_rx](structshell__adsp__memory__window.md#a00650a08293ddbc232002d36a9d5dffb)

struct sys\_winstream \* ws\_rx

Receive winstream object.

**Definition** shell\_adsp\_memory\_window.h:32

[shell\_adsp\_memory\_window::shell\_context](structshell__adsp__memory__window.md#a1baf124df654fc375612f6530652285d)

void \* shell\_context

Context registered by shell.

**Definition** shell\_adsp\_memory\_window.h:29

[shell\_adsp\_memory\_window::timer](structshell__adsp__memory__window.md#a398c24153b3263c74fe995a3c369a4cc)

struct k\_timer timer

**Definition** shell\_adsp\_memory\_window.h:26

[shell\_adsp\_memory\_window::shell\_handler](structshell__adsp__memory__window.md#a730dbada8e6804b6eeadfa278971ad4d)

shell\_transport\_handler\_t shell\_handler

Handler function registered by shell.

**Definition** shell\_adsp\_memory\_window.h:24

[shell\_adsp\_memory\_window::ws\_tx](structshell__adsp__memory__window.md#a89d8688c922ce5b7ccb93e04d4e6d68a)

struct sys\_winstream \* ws\_tx

Transmit winstream object.

**Definition** shell\_adsp\_memory\_window.h:35

[shell\_adsp\_memory\_window::read\_seqno](structshell__adsp__memory__window.md#aa9809847f068296c4f610d93b288ec54)

uint32\_t read\_seqno

Last read sequence number.

**Definition** shell\_adsp\_memory\_window.h:38

[shell\_transport\_api](structshell__transport__api.md)

Unified shell transport interface.

**Definition** shell.h:668

[shell](structshell.md)

Shell instance internals.

**Definition** shell.h:912

[sys\_winstream](structsys__winstream.md)

Lockless shared memory byte stream IPC.

**Definition** winstream.h:25

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_adsp\_memory\_window.h](shell__adsp__memory__window_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
