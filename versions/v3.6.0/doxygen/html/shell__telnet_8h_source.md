---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/shell__telnet_8h_source.html
original_path: doxygen/html/shell__telnet_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_telnet.h

[Go to the documentation of this file.](shell__telnet_8h.md)

1/\*

2 \* Copyright (c) 2019 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef SHELL\_TELNET\_H\_\_

8#define SHELL\_TELNET\_H\_\_

9

10#include <[zephyr/shell/shell.h](shell_2shell_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

16extern const struct [shell\_transport\_api](structshell__transport__api.md) [shell\_telnet\_transport\_api](shell__telnet_8h.md#a39f18c861db9a87f151285600d44014e);

17

[ 19](structshell__telnet__line__buf.md)struct [shell\_telnet\_line\_buf](structshell__telnet__line__buf.md) {

[ 21](structshell__telnet__line__buf.md#afdbfe1cad9640b8d9575303c77a8a97e) char [buf](structshell__telnet__line__buf.md#afdbfe1cad9640b8d9575303c77a8a97e)[CONFIG\_SHELL\_TELNET\_LINE\_BUF\_SIZE];

22

[ 24](structshell__telnet__line__buf.md#aaad811b725d1cb7a4601457c0a98b4aa) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structshell__telnet__line__buf.md#aaad811b725d1cb7a4601457c0a98b4aa);

25};

26

[ 28](structshell__telnet.md)struct [shell\_telnet](structshell__telnet.md) {

[ 30](structshell__telnet.md#a24d3153d685bb02815de5c3fc7384e3f) [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) [shell\_handler](structshell__telnet.md#a24d3153d685bb02815de5c3fc7384e3f);

31

[ 33](structshell__telnet.md#a4aca00a70a037d7d4564c9e8f6600225) void \*[shell\_context](structshell__telnet.md#a4aca00a70a037d7d4564c9e8f6600225);

34

[ 36](structshell__telnet.md#a753f176c0d29c02a97899c79d62d2f1e) struct [shell\_telnet\_line\_buf](structshell__telnet__line__buf.md) [line\_out](structshell__telnet.md#a753f176c0d29c02a97899c79d62d2f1e);

37

[ 39](structshell__telnet.md#a4181dc4c7835e0c4b5cf3e2f80b5b895) struct [net\_context](structnet__context.md) \*[client\_ctx](structshell__telnet.md#a4181dc4c7835e0c4b5cf3e2f80b5b895);

40

[ 42](structshell__telnet.md#af3d3839f8eccd43658e6b14c3fefe174) struct [k\_fifo](structk__fifo.md) [rx\_fifo](structshell__telnet.md#af3d3839f8eccd43658e6b14c3fefe174);

43

[ 48](structshell__telnet.md#a1b3150a2d968fb8bb9bfe46f1b940979) struct [k\_work\_delayable](structk__work__delayable.md) [send\_work](structshell__telnet.md#a1b3150a2d968fb8bb9bfe46f1b940979);

[ 49](structshell__telnet.md#adc057a32a6b48f27a39cdf2e428cd65a) struct [k\_work\_sync](structk__work__sync.md) [work\_sync](structshell__telnet.md#adc057a32a6b48f27a39cdf2e428cd65a);

50

[ 52](structshell__telnet.md#aaa088d04a181344111d2675f3e22a49b) bool [output\_lock](structshell__telnet.md#aaa088d04a181344111d2675f3e22a49b);

53};

54

[ 55](shell__telnet_8h.md#a82cf4289a4a5d724edd2d4d333eafe4e)#define SHELL\_TELNET\_DEFINE(\_name) \

56 static struct shell\_telnet \_name##\_shell\_telnet; \

57 struct shell\_transport \_name = { \

58 .api = &shell\_telnet\_transport\_api, \

59 .ctx = (struct shell\_telnet \*)&\_name##\_shell\_telnet \

60 }

61

[ 70](shell__telnet_8h.md#a628b99d20ef08a0b1165af07aee4888c)const struct [shell](structshell.md) \*[shell\_backend\_telnet\_get\_ptr](shell__telnet_8h.md#a628b99d20ef08a0b1165af07aee4888c)(void);

71

72#ifdef \_\_cplusplus

73}

74#endif

75

76#endif /\* SHELL\_TELNET\_H\_\_ \*/

[shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d)

void(\* shell\_transport\_handler\_t)(enum shell\_transport\_evt evt, void \*context)

**Definition** shell.h:590

[shell.h](shell_2shell_8h.md)

[shell\_telnet\_transport\_api](shell__telnet_8h.md#a39f18c861db9a87f151285600d44014e)

const struct shell\_transport\_api shell\_telnet\_transport\_api

[shell\_backend\_telnet\_get\_ptr](shell__telnet_8h.md#a628b99d20ef08a0b1165af07aee4888c)

const struct shell \* shell\_backend\_telnet\_get\_ptr(void)

This function provides pointer to shell telnet backend instance.

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2374

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:3889

[k\_work\_sync](structk__work__sync.md)

A structure holding internal state for a pending synchronous operation on a work item or queue.

**Definition** kernel.h:3972

[net\_context](structnet__context.md)

Note that we do not store the actual source IP address in the context because the address is already ...

**Definition** net\_context.h:201

[shell\_telnet\_line\_buf](structshell__telnet__line__buf.md)

Line buffer structure.

**Definition** shell\_telnet.h:19

[shell\_telnet\_line\_buf::len](structshell__telnet__line__buf.md#aaad811b725d1cb7a4601457c0a98b4aa)

uint16\_t len

Current line length.

**Definition** shell\_telnet.h:24

[shell\_telnet\_line\_buf::buf](structshell__telnet__line__buf.md#afdbfe1cad9640b8d9575303c77a8a97e)

char buf[CONFIG\_SHELL\_TELNET\_LINE\_BUF\_SIZE]

Line buffer.

**Definition** shell\_telnet.h:21

[shell\_telnet](structshell__telnet.md)

TELNET-based shell transport.

**Definition** shell\_telnet.h:28

[shell\_telnet::send\_work](structshell__telnet.md#a1b3150a2d968fb8bb9bfe46f1b940979)

struct k\_work\_delayable send\_work

The delayed work is used to send non-lf terminated output that has been around for "too long".

**Definition** shell\_telnet.h:48

[shell\_telnet::shell\_handler](structshell__telnet.md#a24d3153d685bb02815de5c3fc7384e3f)

shell\_transport\_handler\_t shell\_handler

Handler function registered by shell.

**Definition** shell\_telnet.h:30

[shell\_telnet::client\_ctx](structshell__telnet.md#a4181dc4c7835e0c4b5cf3e2f80b5b895)

struct net\_context \* client\_ctx

Network context of TELNET client.

**Definition** shell\_telnet.h:39

[shell\_telnet::shell\_context](structshell__telnet.md#a4aca00a70a037d7d4564c9e8f6600225)

void \* shell\_context

Context registered by shell.

**Definition** shell\_telnet.h:33

[shell\_telnet::line\_out](structshell__telnet.md#a753f176c0d29c02a97899c79d62d2f1e)

struct shell\_telnet\_line\_buf line\_out

Buffer for outgoing line.

**Definition** shell\_telnet.h:36

[shell\_telnet::output\_lock](structshell__telnet.md#aaa088d04a181344111d2675f3e22a49b)

bool output\_lock

If set, no output is sent to the TELNET client.

**Definition** shell\_telnet.h:52

[shell\_telnet::work\_sync](structshell__telnet.md#adc057a32a6b48f27a39cdf2e428cd65a)

struct k\_work\_sync work\_sync

**Definition** shell\_telnet.h:49

[shell\_telnet::rx\_fifo](structshell__telnet.md#af3d3839f8eccd43658e6b14c3fefe174)

struct k\_fifo rx\_fifo

RX packet FIFO.

**Definition** shell\_telnet.h:42

[shell\_transport\_api](structshell__transport__api.md)

Unified shell transport interface.

**Definition** shell.h:612

[shell](structshell.md)

Shell instance internals.

**Definition** shell.h:852

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_telnet.h](shell__telnet_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
