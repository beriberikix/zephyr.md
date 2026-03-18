---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/parser__url_8h_source.html
original_path: doxygen/html/parser__url_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

parser\_url.h

[Go to the documentation of this file.](parser__url_8h.md)

1/\* SPDX-License-Identifier: MIT \*/

2

3/\* Copyright Joyent, Inc. and other Node contributors. All rights reserved.

4 \*

5 \* Permission is hereby granted, free of charge, to any person obtaining a copy

6 \* of this software and associated documentation files (the "Software"), to

7 \* deal in the Software without restriction, including without limitation the

8 \* rights to use, copy, modify, merge, publish, distribute, sublicense, and/or

9 \* sell copies of the Software, and to permit persons to whom the Software is

10 \* furnished to do so, subject to the following conditions:

11 \*

12 \* The above copyright notice and this permission notice shall be included in

13 \* all copies or substantial portions of the Software.

14 \*

15 \* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

16 \* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

17 \* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

18 \* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

19 \* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING

20 \* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS

21 \* IN THE SOFTWARE.

22 \*/

23#ifndef ZEPHYR\_INCLUDE\_NET\_HTTP\_PARSER\_URL\_H\_

24#define ZEPHYR\_INCLUDE\_NET\_HTTP\_PARSER\_URL\_H\_

25

26#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

27#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

28#include <stddef.h>

29#include <[zephyr/net/http/parser\_state.h](parser__state_8h.md)>

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

[ 35](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4eb)enum [http\_parser\_url\_fields](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4eb) {

[ 36](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4ebab2b8b31b30d6bc897dde653f6cc9f06c) [UF\_SCHEMA](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4ebab2b8b31b30d6bc897dde653f6cc9f06c) = 0

[ 37](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4ebaf2aeb0b896645bd8100ca0f1e263a12f) , [UF\_HOST](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4ebaf2aeb0b896645bd8100ca0f1e263a12f) = 1

[ 38](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4eba357b6dc1326ed55be377b0d839e8ca0f) , [UF\_PORT](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4eba357b6dc1326ed55be377b0d839e8ca0f) = 2

[ 39](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4eba86b9abfa220db7b834490d8b36e915af) , [UF\_PATH](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4eba86b9abfa220db7b834490d8b36e915af) = 3

[ 40](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4ebabc8500a49ccad1cd91d66d1eefb503cc) , [UF\_QUERY](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4ebabc8500a49ccad1cd91d66d1eefb503cc) = 4

[ 41](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4eba32fb35461b96b6872f1427b2d51d1c30) , [UF\_FRAGMENT](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4eba32fb35461b96b6872f1427b2d51d1c30) = 5

[ 42](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4ebacb4a85c6a7d6cd0b64ec6e91e7ba8689) , [UF\_USERINFO](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4ebacb4a85c6a7d6cd0b64ec6e91e7ba8689) = 6

[ 43](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4eba4b40c88291e4fa018de04553e7e1adfd) , [UF\_MAX](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4eba4b40c88291e4fa018de04553e7e1adfd) = 7

44};

45

46/\* Result structure for http\_parser\_url\_fields().

47 \*

48 \* Callers should index into field\_data[] with UF\_\* values iff field\_set

49 \* has the relevant (1 << UF\_\*) bit set. As a courtesy to clients (and

50 \* because we probably have padding left over), we convert any port to

51 \* a uint16\_t.

52 \*/

[ 53](structhttp__parser__url.md)struct [http\_parser\_url](structhttp__parser__url.md) {

[ 54](structhttp__parser__url.md#a77af61a480f11c41938810dd76ca49eb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [field\_set](structhttp__parser__url.md#a77af61a480f11c41938810dd76ca49eb); /\* Bitmask of (1 << UF\_\*) values \*/

[ 55](structhttp__parser__url.md#a875fb8faf3ee45707078eda5435fa563) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [port](structhttp__parser__url.md#a875fb8faf3ee45707078eda5435fa563); /\* Converted UF\_PORT string \*/

56

57 struct {

[ 58](structhttp__parser__url.md#a6510826f3aa9a1100ac5f714323edeb1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [off](structhttp__parser__url.md#a6510826f3aa9a1100ac5f714323edeb1); /\* Offset into buffer in which field

59 \* starts

60 \*/

[ 61](structhttp__parser__url.md#a60fb784a989dd5a95e5bd19d468d22c7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structhttp__parser__url.md#a60fb784a989dd5a95e5bd19d468d22c7); /\* Length of run in buffer \*/

[ 62](structhttp__parser__url.md#a911c18d1fc54309a7665d942c55cfae9) } [field\_data](structhttp__parser__url.md#a911c18d1fc54309a7665d942c55cfae9)[[UF\_MAX](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4eba4b40c88291e4fa018de04553e7e1adfd)];

63};

64

[ 65](parser__url_8h.md#a9f477f452dcabd0d22f4a96ce0bfda57)enum [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) [parse\_url\_char](parser__url_8h.md#a9f477f452dcabd0d22f4a96ce0bfda57)(enum [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), const char ch);

66

67/\* Initialize all http\_parser\_url members to 0 \*/

[ 68](parser__url_8h.md#a64e907d36fbcc883033c6bbe5a78b1b3)void [http\_parser\_url\_init](parser__url_8h.md#a64e907d36fbcc883033c6bbe5a78b1b3)(struct [http\_parser\_url](structhttp__parser__url.md) \*u);

69

70/\* Parse a URL; return nonzero on failure \*/

[ 71](parser__url_8h.md#aeb269310a348fd68fd001b30b690fc83)int [http\_parser\_parse\_url](parser__url_8h.md#aeb269310a348fd68fd001b30b690fc83)(const char \*buf, size\_t buflen,

72 int is\_connect, struct [http\_parser\_url](structhttp__parser__url.md) \*u);

73

74#ifdef \_\_cplusplus

75}

76#endif

77#endif

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

[types.h](include_2zephyr_2types_8h.md)

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[parser\_state.h](parser__state_8h.md)

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[http\_parser\_url\_init](parser__url_8h.md#a64e907d36fbcc883033c6bbe5a78b1b3)

void http\_parser\_url\_init(struct http\_parser\_url \*u)

[http\_parser\_url\_fields](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4eb)

http\_parser\_url\_fields

**Definition** parser\_url.h:35

[UF\_FRAGMENT](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4eba32fb35461b96b6872f1427b2d51d1c30)

@ UF\_FRAGMENT

**Definition** parser\_url.h:41

[UF\_PORT](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4eba357b6dc1326ed55be377b0d839e8ca0f)

@ UF\_PORT

**Definition** parser\_url.h:38

[UF\_MAX](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4eba4b40c88291e4fa018de04553e7e1adfd)

@ UF\_MAX

**Definition** parser\_url.h:43

[UF\_PATH](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4eba86b9abfa220db7b834490d8b36e915af)

@ UF\_PATH

**Definition** parser\_url.h:39

[UF\_SCHEMA](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4ebab2b8b31b30d6bc897dde653f6cc9f06c)

@ UF\_SCHEMA

**Definition** parser\_url.h:36

[UF\_QUERY](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4ebabc8500a49ccad1cd91d66d1eefb503cc)

@ UF\_QUERY

**Definition** parser\_url.h:40

[UF\_USERINFO](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4ebacb4a85c6a7d6cd0b64ec6e91e7ba8689)

@ UF\_USERINFO

**Definition** parser\_url.h:42

[UF\_HOST](parser__url_8h.md#a9ca1f91c2958091e2ac9e9b2f903d4ebaf2aeb0b896645bd8100ca0f1e263a12f)

@ UF\_HOST

**Definition** parser\_url.h:37

[parse\_url\_char](parser__url_8h.md#a9f477f452dcabd0d22f4a96ce0bfda57)

enum state parse\_url\_char(enum state s, const char ch)

[http\_parser\_parse\_url](parser__url_8h.md#aeb269310a348fd68fd001b30b690fc83)

int http\_parser\_parse\_url(const char \*buf, size\_t buflen, int is\_connect, struct http\_parser\_url \*u)

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[http\_parser\_url](structhttp__parser__url.md)

**Definition** parser\_url.h:53

[http\_parser\_url::len](structhttp__parser__url.md#a60fb784a989dd5a95e5bd19d468d22c7)

uint16\_t len

**Definition** parser\_url.h:61

[http\_parser\_url::off](structhttp__parser__url.md#a6510826f3aa9a1100ac5f714323edeb1)

uint16\_t off

**Definition** parser\_url.h:58

[http\_parser\_url::field\_set](structhttp__parser__url.md#a77af61a480f11c41938810dd76ca49eb)

uint16\_t field\_set

**Definition** parser\_url.h:54

[http\_parser\_url::port](structhttp__parser__url.md#a875fb8faf3ee45707078eda5435fa563)

uint16\_t port

**Definition** parser\_url.h:55

[http\_parser\_url::field\_data](structhttp__parser__url.md#a911c18d1fc54309a7665d942c55cfae9)

struct http\_parser\_url::@255021360070075037010254254033340210153147024225 field\_data[UF\_MAX]

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [parser\_url.h](parser__url_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
