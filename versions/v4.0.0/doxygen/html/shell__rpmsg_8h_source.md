---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/shell__rpmsg_8h_source.html
original_path: doxygen/html/shell__rpmsg_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_rpmsg.h

[Go to the documentation of this file.](shell__rpmsg_8h.md)

1/\*

2 \* Copyright (c) 2024 Basalte bv

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SHELL\_RPMSG\_H\_

8#define ZEPHYR\_INCLUDE\_SHELL\_RPMSG\_H\_

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11#include <[zephyr/shell/shell.h](shell_2shell_8h.md)>

12#include <openamp/rpmsg.h>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

18extern const struct [shell\_transport\_api](structshell__transport__api.md) [shell\_rpmsg\_transport\_api](shell__rpmsg_8h.md#a9189ca38b2b0d084a9169828abcf91d7);

19

[ 21](structshell__rpmsg__rx.md)struct [shell\_rpmsg\_rx](structshell__rpmsg__rx.md) {

[ 23](structshell__rpmsg__rx.md#ae8a514d32794e9b52fa7d3d4cdcd181c) void \*[data](structshell__rpmsg__rx.md#ae8a514d32794e9b52fa7d3d4cdcd181c);

[ 25](structshell__rpmsg__rx.md#a77a9481931a3b2ab7d8f033644b1b813) size\_t [len](structshell__rpmsg__rx.md#a77a9481931a3b2ab7d8f033644b1b813);

26};

27

[ 29](structshell__rpmsg.md)struct [shell\_rpmsg](structshell__rpmsg.md) {

[ 31](structshell__rpmsg.md#a72307140d40e6dd9cb735e3141d66f69) [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) [shell\_handler](structshell__rpmsg.md#a72307140d40e6dd9cb735e3141d66f69);

32

[ 34](structshell__rpmsg.md#ae2d42a908ddd784e8a792ecd47700d18) void \*[shell\_context](structshell__rpmsg.md#ae2d42a908ddd784e8a792ecd47700d18);

35

[ 37](structshell__rpmsg.md#ace1a7aefb13b92f5167dd4d3af3c39e9) bool [ready](structshell__rpmsg.md#ace1a7aefb13b92f5167dd4d3af3c39e9);

38

[ 40](structshell__rpmsg.md#aca5ea2487d3712f9fdeb6f90043cbf53) bool [blocking](structshell__rpmsg.md#aca5ea2487d3712f9fdeb6f90043cbf53);

41

[ 43](structshell__rpmsg.md#ae2f9b114e042df5fd83fcec9c2784df3) struct rpmsg\_endpoint [ept](structshell__rpmsg.md#ae2f9b114e042df5fd83fcec9c2784df3);

44

[ 46](structshell__rpmsg.md#ac8e38cdb8c3ffe1f630126e085238cc9) struct [k\_msgq](structk__msgq.md) [rx\_q](structshell__rpmsg.md#ac8e38cdb8c3ffe1f630126e085238cc9);

47

[ 49](structshell__rpmsg.md#a9bd628e39d3f7fb766d0c33b378e3cdb) struct [shell\_rpmsg\_rx](structshell__rpmsg__rx.md) [rx\_buf](structshell__rpmsg.md#a9bd628e39d3f7fb766d0c33b378e3cdb)[CONFIG\_SHELL\_RPMSG\_MAX\_RX];

50

[ 52](structshell__rpmsg.md#a03fad4774300bfd923aafdd660b258df) struct [shell\_rpmsg\_rx](structshell__rpmsg__rx.md) [rx\_cur](structshell__rpmsg.md#a03fad4774300bfd923aafdd660b258df);

53

[ 55](structshell__rpmsg.md#a358e50712674ada1d01a22394e79f964) size\_t [rx\_consumed](structshell__rpmsg.md#a358e50712674ada1d01a22394e79f964);

56};

57

[ 58](shell__rpmsg_8h.md#a95bbdb52f1dab7231087cc94fba5a62c)#define SHELL\_RPMSG\_DEFINE(\_name) \

59 static struct shell\_rpmsg \_name##\_shell\_rpmsg; \

60 struct shell\_transport \_name = { \

61 .api = &shell\_rpmsg\_transport\_api, \

62 .ctx = (struct shell\_rpmsg \*)&\_name##\_shell\_rpmsg, \

63 }

64

[ 71](shell__rpmsg_8h.md#adf66e74fc7cf312979d8b79d4dffbbf5)int [shell\_backend\_rpmsg\_init\_transport](shell__rpmsg_8h.md#adf66e74fc7cf312979d8b79d4dffbbf5)(struct rpmsg\_device \*rpmsg\_dev);

72

[ 81](shell__rpmsg_8h.md#a486b7ee360b0cb75ab6df977464c4878)const struct [shell](structshell.md) \*[shell\_backend\_rpmsg\_get\_ptr](shell__rpmsg_8h.md#a486b7ee360b0cb75ab6df977464c4878)(void);

82

83#ifdef \_\_cplusplus

84}

85#endif

86

87#endif /\* ZEPHYR\_INCLUDE\_SHELL\_RPMSG\_H\_ \*/

[shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d)

void(\* shell\_transport\_handler\_t)(enum shell\_transport\_evt evt, void \*context)

**Definition** shell.h:624

[kernel.h](kernel_8h.md)

Public kernel APIs.

[shell.h](shell_2shell_8h.md)

[shell\_backend\_rpmsg\_get\_ptr](shell__rpmsg_8h.md#a486b7ee360b0cb75ab6df977464c4878)

const struct shell \* shell\_backend\_rpmsg\_get\_ptr(void)

This function provides pointer to shell RPMsg backend instance.

[shell\_rpmsg\_transport\_api](shell__rpmsg_8h.md#a9189ca38b2b0d084a9169828abcf91d7)

const struct shell\_transport\_api shell\_rpmsg\_transport\_api

[shell\_backend\_rpmsg\_init\_transport](shell__rpmsg_8h.md#adf66e74fc7cf312979d8b79d4dffbbf5)

int shell\_backend\_rpmsg\_init\_transport(struct rpmsg\_device \*rpmsg\_dev)

Initialize the Shell backend using the provided rpmsg\_dev device.

[k\_msgq](structk__msgq.md)

Message Queue Structure.

**Definition** kernel.h:4503

[shell\_rpmsg\_rx](structshell__rpmsg__rx.md)

RPMsg received message placeholder.

**Definition** shell\_rpmsg.h:21

[shell\_rpmsg\_rx::len](structshell__rpmsg__rx.md#a77a9481931a3b2ab7d8f033644b1b813)

size\_t len

The length of the data.

**Definition** shell\_rpmsg.h:25

[shell\_rpmsg\_rx::data](structshell__rpmsg__rx.md#ae8a514d32794e9b52fa7d3d4cdcd181c)

void \* data

Pointer to the data held by RPMsg endpoint.

**Definition** shell\_rpmsg.h:23

[shell\_rpmsg](structshell__rpmsg.md)

RPMsg-based shell transport.

**Definition** shell\_rpmsg.h:29

[shell\_rpmsg::rx\_cur](structshell__rpmsg.md#a03fad4774300bfd923aafdd660b258df)

struct shell\_rpmsg\_rx rx\_cur

The current rx message.

**Definition** shell\_rpmsg.h:52

[shell\_rpmsg::rx\_consumed](structshell__rpmsg.md#a358e50712674ada1d01a22394e79f964)

size\_t rx\_consumed

The number of bytes consumed from rx\_cur.

**Definition** shell\_rpmsg.h:55

[shell\_rpmsg::shell\_handler](structshell__rpmsg.md#a72307140d40e6dd9cb735e3141d66f69)

shell\_transport\_handler\_t shell\_handler

Handler function registered by shell.

**Definition** shell\_rpmsg.h:31

[shell\_rpmsg::rx\_buf](structshell__rpmsg.md#a9bd628e39d3f7fb766d0c33b378e3cdb)

struct shell\_rpmsg\_rx rx\_buf[CONFIG\_SHELL\_RPMSG\_MAX\_RX]

Buffer for received messages.

**Definition** shell\_rpmsg.h:49

[shell\_rpmsg::rx\_q](structshell__rpmsg.md#ac8e38cdb8c3ffe1f630126e085238cc9)

struct k\_msgq rx\_q

Queue for received data.

**Definition** shell\_rpmsg.h:46

[shell\_rpmsg::blocking](structshell__rpmsg.md#aca5ea2487d3712f9fdeb6f90043cbf53)

bool blocking

Setting for blocking mode.

**Definition** shell\_rpmsg.h:40

[shell\_rpmsg::ready](structshell__rpmsg.md#ace1a7aefb13b92f5167dd4d3af3c39e9)

bool ready

Indicator if we are ready to read/write.

**Definition** shell\_rpmsg.h:37

[shell\_rpmsg::shell\_context](structshell__rpmsg.md#ae2d42a908ddd784e8a792ecd47700d18)

void \* shell\_context

Context registered by shell.

**Definition** shell\_rpmsg.h:34

[shell\_rpmsg::ept](structshell__rpmsg.md#ae2f9b114e042df5fd83fcec9c2784df3)

struct rpmsg\_endpoint ept

RPMsg endpoint.

**Definition** shell\_rpmsg.h:43

[shell\_transport\_api](structshell__transport__api.md)

Unified shell transport interface.

**Definition** shell.h:646

[shell](structshell.md)

Shell instance internals.

**Definition** shell.h:890

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_rpmsg.h](shell__rpmsg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
