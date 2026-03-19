---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/shell__telnet_8h_source.html
original_path: doxygen/html/shell__telnet_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

7#ifndef ZEPHYR\_INCLUDE\_SHELL\_TELNET\_H\_

8#define ZEPHYR\_INCLUDE\_SHELL\_TELNET\_H\_

9

10#include <[zephyr/net/socket.h](net_2socket_8h.md)>

11#include <[zephyr/shell/shell.h](shell_2shell_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

17extern const struct [shell\_transport\_api](structshell__transport__api.md) [shell\_telnet\_transport\_api](shell__telnet_8h.md#a39f18c861db9a87f151285600d44014e);

18

[ 19](shell__telnet_8h.md#a6307a5cc6b33233351090fa871695609)#define SHELL\_TELNET\_POLLFD\_COUNT 3

[ 20](shell__telnet_8h.md#ab3b85da7a39a8270dfa23bc099113528)#define SHELL\_TELNET\_MAX\_CMD\_SIZE 3

21

[ 23](structshell__telnet__line__buf.md)struct [shell\_telnet\_line\_buf](structshell__telnet__line__buf.md) {

[ 25](structshell__telnet__line__buf.md#afdbfe1cad9640b8d9575303c77a8a97e) char [buf](structshell__telnet__line__buf.md#afdbfe1cad9640b8d9575303c77a8a97e)[CONFIG\_SHELL\_TELNET\_LINE\_BUF\_SIZE];

26

[ 28](structshell__telnet__line__buf.md#aaad811b725d1cb7a4601457c0a98b4aa) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structshell__telnet__line__buf.md#aaad811b725d1cb7a4601457c0a98b4aa);

29};

30

[ 32](structshell__telnet.md)struct [shell\_telnet](structshell__telnet.md) {

[ 34](structshell__telnet.md#a24d3153d685bb02815de5c3fc7384e3f) [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) [shell\_handler](structshell__telnet.md#a24d3153d685bb02815de5c3fc7384e3f);

35

[ 37](structshell__telnet.md#a4aca00a70a037d7d4564c9e8f6600225) void \*[shell\_context](structshell__telnet.md#a4aca00a70a037d7d4564c9e8f6600225);

38

[ 40](structshell__telnet.md#a753f176c0d29c02a97899c79d62d2f1e) struct [shell\_telnet\_line\_buf](structshell__telnet__line__buf.md) [line\_out](structshell__telnet.md#a753f176c0d29c02a97899c79d62d2f1e);

41

[ 43](structshell__telnet.md#aaecfc5551f4a586ca0ef268b64ff6911) struct [zsock\_pollfd](structzsock__pollfd.md) [fds](structshell__telnet.md#aaecfc5551f4a586ca0ef268b64ff6911)[[SHELL\_TELNET\_POLLFD\_COUNT](shell__telnet_8h.md#a6307a5cc6b33233351090fa871695609)];

44

[ 46](structshell__telnet.md#add80ca8c2ab03e3f3214c4783c5e5a3a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_buf](structshell__telnet.md#add80ca8c2ab03e3f3214c4783c5e5a3a)[[CONFIG\_SHELL\_CMD\_BUFF\_SIZE](shell_2shell_8h.md#abb162a9a784f605dea4b02a0a6cc0c16)];

47

[ 49](structshell__telnet.md#aeaf80d8b274937c2f517fef7ad67cc0c) size\_t [rx\_len](structshell__telnet.md#aeaf80d8b274937c2f517fef7ad67cc0c);

50

[ 52](structshell__telnet.md#a671009aae6ebcac90fea2b5648e9f0ce) struct [k\_mutex](structk__mutex.md) [rx\_lock](structshell__telnet.md#a671009aae6ebcac90fea2b5648e9f0ce);

[ 53](structshell__telnet.md#a471d042c6921cf9b71eb8fa58bfd63ac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd\_buf](structshell__telnet.md#a471d042c6921cf9b71eb8fa58bfd63ac)[[SHELL\_TELNET\_MAX\_CMD\_SIZE](shell__telnet_8h.md#ab3b85da7a39a8270dfa23bc099113528)];

[ 54](structshell__telnet.md#a2939e9ae41aea8ff20d7d40aa7479669) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd\_len](structshell__telnet.md#a2939e9ae41aea8ff20d7d40aa7479669);

55

[ 60](structshell__telnet.md#a1b3150a2d968fb8bb9bfe46f1b940979) struct [k\_work\_delayable](structk__work__delayable.md) [send\_work](structshell__telnet.md#a1b3150a2d968fb8bb9bfe46f1b940979);

[ 61](structshell__telnet.md#adc057a32a6b48f27a39cdf2e428cd65a) struct [k\_work\_sync](structk__work__sync.md) [work\_sync](structshell__telnet.md#adc057a32a6b48f27a39cdf2e428cd65a);

62

[ 64](structshell__telnet.md#aaa088d04a181344111d2675f3e22a49b) bool [output\_lock](structshell__telnet.md#aaa088d04a181344111d2675f3e22a49b);

65};

66

[ 67](shell__telnet_8h.md#a82cf4289a4a5d724edd2d4d333eafe4e)#define SHELL\_TELNET\_DEFINE(\_name) \

68 static struct shell\_telnet \_name##\_shell\_telnet; \

69 struct shell\_transport \_name = { \

70 .api = &shell\_telnet\_transport\_api, \

71 .ctx = (struct shell\_telnet \*)&\_name##\_shell\_telnet \

72 }

73

[ 82](shell__telnet_8h.md#a628b99d20ef08a0b1165af07aee4888c)const struct [shell](structshell.md) \*[shell\_backend\_telnet\_get\_ptr](shell__telnet_8h.md#a628b99d20ef08a0b1165af07aee4888c)(void);

83

84#ifdef \_\_cplusplus

85}

86#endif

87

88#endif /\* ZEPHYR\_INCLUDE\_SHELL\_TELNET\_H\_ \*/

[shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d)

void(\* shell\_transport\_handler\_t)(enum shell\_transport\_evt evt, void \*context)

**Definition** shell.h:624

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[shell.h](shell_2shell_8h.md)

[CONFIG\_SHELL\_CMD\_BUFF\_SIZE](shell_2shell_8h.md#abb162a9a784f605dea4b02a0a6cc0c16)

#define CONFIG\_SHELL\_CMD\_BUFF\_SIZE

**Definition** shell.h:34

[shell\_telnet\_transport\_api](shell__telnet_8h.md#a39f18c861db9a87f151285600d44014e)

const struct shell\_transport\_api shell\_telnet\_transport\_api

[shell\_backend\_telnet\_get\_ptr](shell__telnet_8h.md#a628b99d20ef08a0b1165af07aee4888c)

const struct shell \* shell\_backend\_telnet\_get\_ptr(void)

This function provides pointer to shell telnet backend instance.

[SHELL\_TELNET\_POLLFD\_COUNT](shell__telnet_8h.md#a6307a5cc6b33233351090fa871695609)

#define SHELL\_TELNET\_POLLFD\_COUNT

**Definition** shell\_telnet.h:19

[SHELL\_TELNET\_MAX\_CMD\_SIZE](shell__telnet_8h.md#ab3b85da7a39a8270dfa23bc099113528)

#define SHELL\_TELNET\_MAX\_CMD\_SIZE

**Definition** shell\_telnet.h:20

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2994

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:3985

[k\_work\_sync](structk__work__sync.md)

A structure holding internal state for a pending synchronous operation on a work item or queue.

**Definition** kernel.h:4068

[shell\_telnet\_line\_buf](structshell__telnet__line__buf.md)

Line buffer structure.

**Definition** shell\_telnet.h:23

[shell\_telnet\_line\_buf::len](structshell__telnet__line__buf.md#aaad811b725d1cb7a4601457c0a98b4aa)

uint16\_t len

Current line length.

**Definition** shell\_telnet.h:28

[shell\_telnet\_line\_buf::buf](structshell__telnet__line__buf.md#afdbfe1cad9640b8d9575303c77a8a97e)

char buf[CONFIG\_SHELL\_TELNET\_LINE\_BUF\_SIZE]

Line buffer.

**Definition** shell\_telnet.h:25

[shell\_telnet](structshell__telnet.md)

TELNET-based shell transport.

**Definition** shell\_telnet.h:32

[shell\_telnet::send\_work](structshell__telnet.md#a1b3150a2d968fb8bb9bfe46f1b940979)

struct k\_work\_delayable send\_work

The delayed work is used to send non-lf terminated output that has been around for "too long".

**Definition** shell\_telnet.h:60

[shell\_telnet::shell\_handler](structshell__telnet.md#a24d3153d685bb02815de5c3fc7384e3f)

shell\_transport\_handler\_t shell\_handler

Handler function registered by shell.

**Definition** shell\_telnet.h:34

[shell\_telnet::cmd\_len](structshell__telnet.md#a2939e9ae41aea8ff20d7d40aa7479669)

uint8\_t cmd\_len

**Definition** shell\_telnet.h:54

[shell\_telnet::cmd\_buf](structshell__telnet.md#a471d042c6921cf9b71eb8fa58bfd63ac)

uint8\_t cmd\_buf[3]

**Definition** shell\_telnet.h:53

[shell\_telnet::shell\_context](structshell__telnet.md#a4aca00a70a037d7d4564c9e8f6600225)

void \* shell\_context

Context registered by shell.

**Definition** shell\_telnet.h:37

[shell\_telnet::rx\_lock](structshell__telnet.md#a671009aae6ebcac90fea2b5648e9f0ce)

struct k\_mutex rx\_lock

Mutex protecting the input buffer access.

**Definition** shell\_telnet.h:52

[shell\_telnet::line\_out](structshell__telnet.md#a753f176c0d29c02a97899c79d62d2f1e)

struct shell\_telnet\_line\_buf line\_out

Buffer for outgoing line.

**Definition** shell\_telnet.h:40

[shell\_telnet::output\_lock](structshell__telnet.md#aaa088d04a181344111d2675f3e22a49b)

bool output\_lock

If set, no output is sent to the TELNET client.

**Definition** shell\_telnet.h:64

[shell\_telnet::fds](structshell__telnet.md#aaecfc5551f4a586ca0ef268b64ff6911)

struct zsock\_pollfd fds[3]

Array for sockets used by the telnet service.

**Definition** shell\_telnet.h:43

[shell\_telnet::work\_sync](structshell__telnet.md#adc057a32a6b48f27a39cdf2e428cd65a)

struct k\_work\_sync work\_sync

**Definition** shell\_telnet.h:61

[shell\_telnet::rx\_buf](structshell__telnet.md#add80ca8c2ab03e3f3214c4783c5e5a3a)

uint8\_t rx\_buf[CONFIG\_SHELL\_CMD\_BUFF\_SIZE]

Input buffer.

**Definition** shell\_telnet.h:46

[shell\_telnet::rx\_len](structshell__telnet.md#aeaf80d8b274937c2f517fef7ad67cc0c)

size\_t rx\_len

Number of data bytes within the input buffer.

**Definition** shell\_telnet.h:49

[shell\_transport\_api](structshell__transport__api.md)

Unified shell transport interface.

**Definition** shell.h:646

[shell](structshell.md)

Shell instance internals.

**Definition** shell.h:890

[zsock\_pollfd](structzsock__pollfd.md)

Definition of the monitored socket/file descriptor.

**Definition** socket\_poll.h:31

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_telnet.h](shell__telnet_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
