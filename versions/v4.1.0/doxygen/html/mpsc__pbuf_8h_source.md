---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mpsc__pbuf_8h_source.html
original_path: doxygen/html/mpsc__pbuf_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mpsc\_pbuf.h

[Go to the documentation of this file.](mpsc__pbuf_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_SYS\_MPSC\_PBUF\_H\_

7#define ZEPHYR\_INCLUDE\_SYS\_MPSC\_PBUF\_H\_

8

9#include <[zephyr/kernel.h](kernel_8h.md)>

10#include <[zephyr/sys/mpsc\_packet.h](mpsc__packet_8h.md)>

11#include <[string.h](string_8h.md)>

12#include <[stdint.h](stdint_8h.md)>

13#include <[stdbool.h](stdbool_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

25

26/\*

27 \* Multi producer, single consumer packet buffer allows to allocate variable

28 \* length consecutive space for storing a packet. When space is allocated

29 \* it can be filled by the user (except for the first 2 bits) and when packet

30 \* is ready it is committed. It is allowed to allocate another packet before

31 \* committing the previous one.

32 \*

33 \* If buffer is full and packet cannot be allocated then null is returned unless

34 \* overwrite mode is selected. In that mode, oldest entry are dropped (user is

35 \* notified) until allocation succeeds. It can happen that candidate for

36 \* dropping is currently being claimed. In that case, it is omitted and next

37 \* packet is dropped and claimed packet is marked as invalid when freeing.

38 \*

39 \* Reading packets is performed in two steps. First packet is claimed. Claiming

40 \* returns pointer to the packet within the buffer. Packet is freed when no

41 \* longer in use.

42 \*/

43

47

[ 52](group__MPSC__PBUF__FLAGS.md#ga6bed4eecb4eca06fb86a70c09505ccb8)#define MPSC\_PBUF\_SIZE\_POW2 BIT(0)

53

[ 59](group__MPSC__PBUF__FLAGS.md#ga983332f7aff31ed7b7e62cacf7960497)#define MPSC\_PBUF\_MODE\_OVERWRITE BIT(1)

60

[ 62](group__MPSC__PBUF__FLAGS.md#gad0f57dbcecbb51a6b5b916c31a8eaab2)#define MPSC\_PBUF\_MAX\_UTILIZATION BIT(2)

63

[ 65](group__MPSC__PBUF__FLAGS.md#ga71a287b22771128b80c23d9263677498)#define MPSC\_PBUF\_FULL BIT(3)

66

68

69/\* Forward declaration \*/

70struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md);

71

[ 78](group__mpsc__buf.md#ga00b0a1839bc466c623928a29921d76b8)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[mpsc\_pbuf\_get\_wlen](group__mpsc__buf.md#ga00b0a1839bc466c623928a29921d76b8))(const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*packet);

79

[ 86](group__mpsc__buf.md#ga87f3795770880fb552316a8cac7b85ae)typedef void (\*[mpsc\_pbuf\_notify\_drop](group__mpsc__buf.md#ga87f3795770880fb552316a8cac7b85ae))(const struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer,

87 const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*packet);

88

[ 90](structmpsc__pbuf__buffer.md)struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) {

[ 92](structmpsc__pbuf__buffer.md#a55df06357be70a3b633213199d987e71) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tmp\_wr\_idx](structmpsc__pbuf__buffer.md#a55df06357be70a3b633213199d987e71);

93

[ 95](structmpsc__pbuf__buffer.md#a3f292f281f08b97d10183f9248ee7c4d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [wr\_idx](structmpsc__pbuf__buffer.md#a3f292f281f08b97d10183f9248ee7c4d);

96

[ 98](structmpsc__pbuf__buffer.md#aeea63b40d7b24e4396fa228bcf2a171f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tmp\_rd\_idx](structmpsc__pbuf__buffer.md#aeea63b40d7b24e4396fa228bcf2a171f);

99

[ 101](structmpsc__pbuf__buffer.md#af9340dd31ea8e37b4d609898b126497a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rd\_idx](structmpsc__pbuf__buffer.md#af9340dd31ea8e37b4d609898b126497a);

102

[ 104](structmpsc__pbuf__buffer.md#a10e9152b8c85be62eac0a3828e3b1e2a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structmpsc__pbuf__buffer.md#a10e9152b8c85be62eac0a3828e3b1e2a);

105

[ 107](structmpsc__pbuf__buffer.md#a1a986b86547aa644747b9a79a982b780) struct [k\_spinlock](structk__spinlock.md) [lock](structmpsc__pbuf__buffer.md#a1a986b86547aa644747b9a79a982b780);

108

[ 113](structmpsc__pbuf__buffer.md#acdebdb6e7175ea3f39f484885ff6bec2) [mpsc\_pbuf\_notify\_drop](group__mpsc__buf.md#ga87f3795770880fb552316a8cac7b85ae) [notify\_drop](structmpsc__pbuf__buffer.md#acdebdb6e7175ea3f39f484885ff6bec2);

114

[ 116](structmpsc__pbuf__buffer.md#ad87f240d978605258cb03d7d1e5e006f) [mpsc\_pbuf\_get\_wlen](group__mpsc__buf.md#ga00b0a1839bc466c623928a29921d76b8) [get\_wlen](structmpsc__pbuf__buffer.md#ad87f240d978605258cb03d7d1e5e006f);

117

118 /\* Buffer. \*/

[ 119](structmpsc__pbuf__buffer.md#a2b5cb8a3c7f4d41cf587318ccf6b0a76) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[buf](structmpsc__pbuf__buffer.md#a2b5cb8a3c7f4d41cf587318ccf6b0a76);

120

121 /\* Buffer size in 32 bit words. \*/

[ 122](structmpsc__pbuf__buffer.md#a917ecd5a37f6c1560091a7a63c50fd2c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [size](structmpsc__pbuf__buffer.md#a917ecd5a37f6c1560091a7a63c50fd2c);

123

124 /\* Store max buffer usage. \*/

[ 125](structmpsc__pbuf__buffer.md#adad43580b7a632877cf7b577585a495a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_usage](structmpsc__pbuf__buffer.md#adad43580b7a632877cf7b577585a495a);

126

[ 127](structmpsc__pbuf__buffer.md#ae860724c0784ae560e7d03b1b6389fa0) struct k\_sem [sem](structmpsc__pbuf__buffer.md#ae860724c0784ae560e7d03b1b6389fa0);

128};

129

[ 131](structmpsc__pbuf__buffer__config.md)struct [mpsc\_pbuf\_buffer\_config](structmpsc__pbuf__buffer__config.md) {

132 /\* Pointer to a memory used for storing packets. \*/

[ 133](structmpsc__pbuf__buffer__config.md#a2090b3da5dc85c68601fd7bdb54f6174) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[buf](structmpsc__pbuf__buffer__config.md#a2090b3da5dc85c68601fd7bdb54f6174);

134

135 /\* Buffer size in 32 bit words. \*/

[ 136](structmpsc__pbuf__buffer__config.md#aa321ccd5bcec6359ed329418c24e5260) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [size](structmpsc__pbuf__buffer__config.md#aa321ccd5bcec6359ed329418c24e5260);

137

138 /\* Callbacks. \*/

[ 139](structmpsc__pbuf__buffer__config.md#a2c0ed75bc95a03bb3a9ebfa55ca54227) [mpsc\_pbuf\_notify\_drop](group__mpsc__buf.md#ga87f3795770880fb552316a8cac7b85ae) [notify\_drop](structmpsc__pbuf__buffer__config.md#a2c0ed75bc95a03bb3a9ebfa55ca54227);

[ 140](structmpsc__pbuf__buffer__config.md#a43ea61f310a062f4460ab1b085276265) [mpsc\_pbuf\_get\_wlen](group__mpsc__buf.md#ga00b0a1839bc466c623928a29921d76b8) [get\_wlen](structmpsc__pbuf__buffer__config.md#a43ea61f310a062f4460ab1b085276265);

141

142 /\* Configuration flags. \*/

[ 143](structmpsc__pbuf__buffer__config.md#a88c3049ff8d7942e834fed28ede234b1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structmpsc__pbuf__buffer__config.md#a88c3049ff8d7942e834fed28ede234b1);

144};

145

[ 152](group__mpsc__buf.md#ga5152b9ae9c0da98fde3f8b73afac52b8)void [mpsc\_pbuf\_init](group__mpsc__buf.md#ga5152b9ae9c0da98fde3f8b73afac52b8)(struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer,

153 const struct [mpsc\_pbuf\_buffer\_config](structmpsc__pbuf__buffer__config.md) \*config);

154

[ 171](group__mpsc__buf.md#ga398dd24464a5da03e80a3fc7d728dddd)union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*[mpsc\_pbuf\_alloc](group__mpsc__buf.md#ga398dd24464a5da03e80a3fc7d728dddd)(struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer,

172 size\_t wlen, [k\_timeout\_t](structk__timeout__t.md) timeout);

173

[ 180](group__mpsc__buf.md#gaa537b9e73ca4fda26a92dc56b960270e)void [mpsc\_pbuf\_commit](group__mpsc__buf.md#gaa537b9e73ca4fda26a92dc56b960270e)(struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer,

181 union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*packet);

182

[ 193](group__mpsc__buf.md#gabc366638ec262c7ec41b320f0dcc6a87)void [mpsc\_pbuf\_put\_word](group__mpsc__buf.md#gabc366638ec262c7ec41b320f0dcc6a87)(struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer,

194 const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) word);

195

[ 208](group__mpsc__buf.md#ga7f4df1864fad89ec9557b6f0e18c9589)void [mpsc\_pbuf\_put\_word\_ext](group__mpsc__buf.md#ga7f4df1864fad89ec9557b6f0e18c9589)(struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer,

209 const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) word,

210 const void \*data);

211

[ 223](group__mpsc__buf.md#ga7b52261bac98a7a0c6bae2a838f23316)void [mpsc\_pbuf\_put\_data](group__mpsc__buf.md#ga7b52261bac98a7a0c6bae2a838f23316)(struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer,

224 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data, size\_t wlen);

225

[ 232](group__mpsc__buf.md#ga9642d07deca00bc25cea2ae253ec7d76)const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*[mpsc\_pbuf\_claim](group__mpsc__buf.md#ga9642d07deca00bc25cea2ae253ec7d76)(struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer);

233

[ 240](group__mpsc__buf.md#ga54f8705fa262a6cda75f1feecde5e57e)void [mpsc\_pbuf\_free](group__mpsc__buf.md#ga54f8705fa262a6cda75f1feecde5e57e)(struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer,

241 const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*packet);

242

[ 250](group__mpsc__buf.md#ga2c8ac7f489fba611a2bca25bb2bbb5fb)bool [mpsc\_pbuf\_is\_pending](group__mpsc__buf.md#ga2c8ac7f489fba611a2bca25bb2bbb5fb)(struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer);

251

[ 258](group__mpsc__buf.md#ga73be0efc020500865cfa07c45494f4a5)void [mpsc\_pbuf\_get\_utilization](group__mpsc__buf.md#ga73be0efc020500865cfa07c45494f4a5)(struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer,

259 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*now);

260

[ 269](group__mpsc__buf.md#ga8ee7fd071effaca18797862d423279d7)int [mpsc\_pbuf\_get\_max\_utilization](group__mpsc__buf.md#ga8ee7fd071effaca18797862d423279d7)(struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*max);

273

274#ifdef \_\_cplusplus

275}

276#endif

277

278#endif /\* ZEPHYR\_INCLUDE\_SYS\_MPSC\_PBUF\_H\_ \*/

[mpsc\_pbuf\_get\_wlen](group__mpsc__buf.md#ga00b0a1839bc466c623928a29921d76b8)

uint32\_t(\* mpsc\_pbuf\_get\_wlen)(const union mpsc\_pbuf\_generic \*packet)

Callback prototype for getting length of a packet.

**Definition** mpsc\_pbuf.h:78

[mpsc\_pbuf\_is\_pending](group__mpsc__buf.md#ga2c8ac7f489fba611a2bca25bb2bbb5fb)

bool mpsc\_pbuf\_is\_pending(struct mpsc\_pbuf\_buffer \*buffer)

Check if there are any message pending.

[mpsc\_pbuf\_alloc](group__mpsc__buf.md#ga398dd24464a5da03e80a3fc7d728dddd)

union mpsc\_pbuf\_generic \* mpsc\_pbuf\_alloc(struct mpsc\_pbuf\_buffer \*buffer, size\_t wlen, k\_timeout\_t timeout)

Allocate a packet.

[mpsc\_pbuf\_init](group__mpsc__buf.md#ga5152b9ae9c0da98fde3f8b73afac52b8)

void mpsc\_pbuf\_init(struct mpsc\_pbuf\_buffer \*buffer, const struct mpsc\_pbuf\_buffer\_config \*config)

Initialize a packet buffer.

[mpsc\_pbuf\_free](group__mpsc__buf.md#ga54f8705fa262a6cda75f1feecde5e57e)

void mpsc\_pbuf\_free(struct mpsc\_pbuf\_buffer \*buffer, const union mpsc\_pbuf\_generic \*packet)

Free a packet.

[mpsc\_pbuf\_get\_utilization](group__mpsc__buf.md#ga73be0efc020500865cfa07c45494f4a5)

void mpsc\_pbuf\_get\_utilization(struct mpsc\_pbuf\_buffer \*buffer, uint32\_t \*size, uint32\_t \*now)

Get current memory utilization.

[mpsc\_pbuf\_put\_data](group__mpsc__buf.md#ga7b52261bac98a7a0c6bae2a838f23316)

void mpsc\_pbuf\_put\_data(struct mpsc\_pbuf\_buffer \*buffer, const uint32\_t \*data, size\_t wlen)

Put a packet into a buffer.

[mpsc\_pbuf\_put\_word\_ext](group__mpsc__buf.md#ga7f4df1864fad89ec9557b6f0e18c9589)

void mpsc\_pbuf\_put\_word\_ext(struct mpsc\_pbuf\_buffer \*buffer, const union mpsc\_pbuf\_generic word, const void \*data)

Put a packet consisting of a word and a pointer.

[mpsc\_pbuf\_notify\_drop](group__mpsc__buf.md#ga87f3795770880fb552316a8cac7b85ae)

void(\* mpsc\_pbuf\_notify\_drop)(const struct mpsc\_pbuf\_buffer \*buffer, const union mpsc\_pbuf\_generic \*packet)

Callback called when packet is dropped.

**Definition** mpsc\_pbuf.h:86

[mpsc\_pbuf\_get\_max\_utilization](group__mpsc__buf.md#ga8ee7fd071effaca18797862d423279d7)

int mpsc\_pbuf\_get\_max\_utilization(struct mpsc\_pbuf\_buffer \*buffer, uint32\_t \*max)

Get maximum memory utilization.

[mpsc\_pbuf\_claim](group__mpsc__buf.md#ga9642d07deca00bc25cea2ae253ec7d76)

const union mpsc\_pbuf\_generic \* mpsc\_pbuf\_claim(struct mpsc\_pbuf\_buffer \*buffer)

Claim the first pending packet.

[mpsc\_pbuf\_commit](group__mpsc__buf.md#gaa537b9e73ca4fda26a92dc56b960270e)

void mpsc\_pbuf\_commit(struct mpsc\_pbuf\_buffer \*buffer, union mpsc\_pbuf\_generic \*packet)

Commit a packet.

[mpsc\_pbuf\_put\_word](group__mpsc__buf.md#gabc366638ec262c7ec41b320f0dcc6a87)

void mpsc\_pbuf\_put\_word(struct mpsc\_pbuf\_buffer \*buffer, const union mpsc\_pbuf\_generic word)

Put single word packet into a buffer.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[mpsc\_packet.h](mpsc__packet_8h.md)

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[string.h](string_8h.md)

[k\_spinlock](structk__spinlock.md)

Kernel Spin Lock.

**Definition** spinlock.h:45

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[mpsc\_pbuf\_buffer\_config](structmpsc__pbuf__buffer__config.md)

MPSC packet buffer configuration.

**Definition** mpsc\_pbuf.h:131

[mpsc\_pbuf\_buffer\_config::buf](structmpsc__pbuf__buffer__config.md#a2090b3da5dc85c68601fd7bdb54f6174)

uint32\_t \* buf

**Definition** mpsc\_pbuf.h:133

[mpsc\_pbuf\_buffer\_config::notify\_drop](structmpsc__pbuf__buffer__config.md#a2c0ed75bc95a03bb3a9ebfa55ca54227)

mpsc\_pbuf\_notify\_drop notify\_drop

**Definition** mpsc\_pbuf.h:139

[mpsc\_pbuf\_buffer\_config::get\_wlen](structmpsc__pbuf__buffer__config.md#a43ea61f310a062f4460ab1b085276265)

mpsc\_pbuf\_get\_wlen get\_wlen

**Definition** mpsc\_pbuf.h:140

[mpsc\_pbuf\_buffer\_config::flags](structmpsc__pbuf__buffer__config.md#a88c3049ff8d7942e834fed28ede234b1)

uint32\_t flags

**Definition** mpsc\_pbuf.h:143

[mpsc\_pbuf\_buffer\_config::size](structmpsc__pbuf__buffer__config.md#aa321ccd5bcec6359ed329418c24e5260)

uint32\_t size

**Definition** mpsc\_pbuf.h:136

[mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md)

MPSC packet buffer structure.

**Definition** mpsc\_pbuf.h:90

[mpsc\_pbuf\_buffer::flags](structmpsc__pbuf__buffer.md#a10e9152b8c85be62eac0a3828e3b1e2a)

uint32\_t flags

Flags.

**Definition** mpsc\_pbuf.h:104

[mpsc\_pbuf\_buffer::lock](structmpsc__pbuf__buffer.md#a1a986b86547aa644747b9a79a982b780)

struct k\_spinlock lock

Lock.

**Definition** mpsc\_pbuf.h:107

[mpsc\_pbuf\_buffer::buf](structmpsc__pbuf__buffer.md#a2b5cb8a3c7f4d41cf587318ccf6b0a76)

uint32\_t \* buf

**Definition** mpsc\_pbuf.h:119

[mpsc\_pbuf\_buffer::wr\_idx](structmpsc__pbuf__buffer.md#a3f292f281f08b97d10183f9248ee7c4d)

uint32\_t wr\_idx

Write index.

**Definition** mpsc\_pbuf.h:95

[mpsc\_pbuf\_buffer::tmp\_wr\_idx](structmpsc__pbuf__buffer.md#a55df06357be70a3b633213199d987e71)

uint32\_t tmp\_wr\_idx

Temporary write index.

**Definition** mpsc\_pbuf.h:92

[mpsc\_pbuf\_buffer::size](structmpsc__pbuf__buffer.md#a917ecd5a37f6c1560091a7a63c50fd2c)

uint32\_t size

**Definition** mpsc\_pbuf.h:122

[mpsc\_pbuf\_buffer::notify\_drop](structmpsc__pbuf__buffer.md#acdebdb6e7175ea3f39f484885ff6bec2)

mpsc\_pbuf\_notify\_drop notify\_drop

User callback called whenever packet is dropped.

**Definition** mpsc\_pbuf.h:113

[mpsc\_pbuf\_buffer::get\_wlen](structmpsc__pbuf__buffer.md#ad87f240d978605258cb03d7d1e5e006f)

mpsc\_pbuf\_get\_wlen get\_wlen

Callback for getting packet length.

**Definition** mpsc\_pbuf.h:116

[mpsc\_pbuf\_buffer::max\_usage](structmpsc__pbuf__buffer.md#adad43580b7a632877cf7b577585a495a)

uint32\_t max\_usage

**Definition** mpsc\_pbuf.h:125

[mpsc\_pbuf\_buffer::sem](structmpsc__pbuf__buffer.md#ae860724c0784ae560e7d03b1b6389fa0)

struct k\_sem sem

**Definition** mpsc\_pbuf.h:127

[mpsc\_pbuf\_buffer::tmp\_rd\_idx](structmpsc__pbuf__buffer.md#aeea63b40d7b24e4396fa228bcf2a171f)

uint32\_t tmp\_rd\_idx

Temporary read index.

**Definition** mpsc\_pbuf.h:98

[mpsc\_pbuf\_buffer::rd\_idx](structmpsc__pbuf__buffer.md#af9340dd31ea8e37b4d609898b126497a)

uint32\_t rd\_idx

Read index.

**Definition** mpsc\_pbuf.h:101

[mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md)

Generic packet header.

**Definition** mpsc\_packet.h:49

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [mpsc\_pbuf.h](mpsc__pbuf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
