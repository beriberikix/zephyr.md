---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/pipe_8h_source.html
original_path: doxygen/html/pipe_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pipe.h

[Go to the documentation of this file.](pipe_8h.md)

1/\*

2 \* Copyright (c) 2022 Trackunit Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

8#include <[zephyr/kernel.h](kernel_8h.md)>

9

10#ifndef ZEPHYR\_MODEM\_PIPE\_

11#define ZEPHYR\_MODEM\_PIPE\_

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

23

[ 25](group__modem__pipe.md#gab9dd98d92d6446dd43852d280574f67a)enum [modem\_pipe\_event](group__modem__pipe.md#gab9dd98d92d6446dd43852d280574f67a) {

[ 26](group__modem__pipe.md#ggab9dd98d92d6446dd43852d280574f67aa68d9924c9fc58cf9ca8760573d32f891) [MODEM\_PIPE\_EVENT\_OPENED](group__modem__pipe.md#ggab9dd98d92d6446dd43852d280574f67aa68d9924c9fc58cf9ca8760573d32f891) = 0,

[ 27](group__modem__pipe.md#ggab9dd98d92d6446dd43852d280574f67aa6687ded90e569690afc72020e78624c4) [MODEM\_PIPE\_EVENT\_RECEIVE\_READY](group__modem__pipe.md#ggab9dd98d92d6446dd43852d280574f67aa6687ded90e569690afc72020e78624c4),

[ 28](group__modem__pipe.md#ggab9dd98d92d6446dd43852d280574f67aaa6e11b11afb91ec50c4d0dfb363e7ad4) [MODEM\_PIPE\_EVENT\_TRANSMIT\_IDLE](group__modem__pipe.md#ggab9dd98d92d6446dd43852d280574f67aaa6e11b11afb91ec50c4d0dfb363e7ad4),

[ 29](group__modem__pipe.md#ggab9dd98d92d6446dd43852d280574f67aae3ed9618f4986a7c3bef59e16a61316f) [MODEM\_PIPE\_EVENT\_CLOSED](group__modem__pipe.md#ggab9dd98d92d6446dd43852d280574f67aae3ed9618f4986a7c3bef59e16a61316f),

30};

31

35

36struct modem\_pipe;

37

41

[ 42](group__modem__pipe.md#gaf64941177c179cb9086a5736d1ea56f1)typedef void (\*[modem\_pipe\_api\_callback](group__modem__pipe.md#gaf64941177c179cb9086a5736d1ea56f1))(struct modem\_pipe \*pipe, enum [modem\_pipe\_event](group__modem__pipe.md#gab9dd98d92d6446dd43852d280574f67a) event,

43 void \*user\_data);

44

48

49typedef int (\*modem\_pipe\_api\_open)(void \*data);

50

51typedef int (\*modem\_pipe\_api\_transmit)(void \*data, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t size);

52

53typedef int (\*modem\_pipe\_api\_receive)(void \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t size);

54

55typedef int (\*modem\_pipe\_api\_close)(void \*data);

56

57struct modem\_pipe\_api {

58 modem\_pipe\_api\_open [open](fcntl_8h.md#ac843f2e35e60c3bbf1da47d84306f29b);

59 modem\_pipe\_api\_transmit transmit;

60 modem\_pipe\_api\_receive receive;

61 modem\_pipe\_api\_close [close](group__bsd__sockets.md#ga3c78073ab26ad78a7a1f715ba3580086);

62};

63

64struct modem\_pipe {

65 void \*data;

66 const struct modem\_pipe\_api \*api;

67 [modem\_pipe\_api\_callback](group__modem__pipe.md#gaf64941177c179cb9086a5736d1ea56f1) callback;

68 void \*user\_data;

69 struct k\_spinlock spinlock;

70 struct k\_event event;

71};

72

80void modem\_pipe\_init(struct modem\_pipe \*pipe, void \*data, const struct modem\_pipe\_api \*api);

81

85

[ 99](group__modem__pipe.md#ga7521ac0aeda8027c47741237e8312bf0)int [modem\_pipe\_open](group__modem__pipe.md#ga7521ac0aeda8027c47741237e8312bf0)(struct modem\_pipe \*pipe, [k\_timeout\_t](structk__timeout__t.md) timeout);

100

[ 112](group__modem__pipe.md#ga0a7312eadaa76b433fe8a319d8c9ec74)int [modem\_pipe\_open\_async](group__modem__pipe.md#ga0a7312eadaa76b433fe8a319d8c9ec74)(struct modem\_pipe \*pipe);

113

[ 124](group__modem__pipe.md#ga68674becf672b1009d629813c041b868)void [modem\_pipe\_attach](group__modem__pipe.md#ga68674becf672b1009d629813c041b868)(struct modem\_pipe \*pipe, [modem\_pipe\_api\_callback](group__modem__pipe.md#gaf64941177c179cb9086a5736d1ea56f1) callback, void \*user\_data);

125

[ 139](group__modem__pipe.md#ga72311fcb03f138d57e230af60340c9f6)int [modem\_pipe\_transmit](group__modem__pipe.md#ga72311fcb03f138d57e230af60340c9f6)(struct modem\_pipe \*pipe, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t size);

140

[ 154](group__modem__pipe.md#gab030b4040725ad4dab2399840ef73fde)int [modem\_pipe\_receive](group__modem__pipe.md#gab030b4040725ad4dab2399840ef73fde)(struct modem\_pipe \*pipe, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t size);

155

[ 161](group__modem__pipe.md#gad1a9fa3dba49a86c187328b7ee022293)void [modem\_pipe\_release](group__modem__pipe.md#gad1a9fa3dba49a86c187328b7ee022293)(struct modem\_pipe \*pipe);

162

[ 176](group__modem__pipe.md#ga4f5d30e87bb252c4e38ce2e3b10e78c5)int [modem\_pipe\_close](group__modem__pipe.md#ga4f5d30e87bb252c4e38ce2e3b10e78c5)(struct modem\_pipe \*pipe, [k\_timeout\_t](structk__timeout__t.md) timeout);

177

[ 189](group__modem__pipe.md#ga9814c9a1a5da33b2787ac058a6a037f5)int [modem\_pipe\_close\_async](group__modem__pipe.md#ga9814c9a1a5da33b2787ac058a6a037f5)(struct modem\_pipe \*pipe);

190

194

202void modem\_pipe\_notify\_opened(struct modem\_pipe \*pipe);

203

211void modem\_pipe\_notify\_closed(struct modem\_pipe \*pipe);

212

220void modem\_pipe\_notify\_receive\_ready(struct modem\_pipe \*pipe);

221

229void modem\_pipe\_notify\_transmit\_idle(struct modem\_pipe \*pipe);

230

234

238

239#ifdef \_\_cplusplus

240}

241#endif

242

243#endif /\* ZEPHYR\_MODEM\_PIPE\_ \*/

[open](fcntl_8h.md#ac843f2e35e60c3bbf1da47d84306f29b)

int open(const char \*name, int flags,...)

[close](group__bsd__sockets.md#ga3c78073ab26ad78a7a1f715ba3580086)

static int close(int sock)

POSIX wrapper for zsock\_close.

**Definition** socket.h:830

[modem\_pipe\_open\_async](group__modem__pipe.md#ga0a7312eadaa76b433fe8a319d8c9ec74)

int modem\_pipe\_open\_async(struct modem\_pipe \*pipe)

Open pipe asynchronously.

[modem\_pipe\_close](group__modem__pipe.md#ga4f5d30e87bb252c4e38ce2e3b10e78c5)

int modem\_pipe\_close(struct modem\_pipe \*pipe, k\_timeout\_t timeout)

Close pipe.

[modem\_pipe\_attach](group__modem__pipe.md#ga68674becf672b1009d629813c041b868)

void modem\_pipe\_attach(struct modem\_pipe \*pipe, modem\_pipe\_api\_callback callback, void \*user\_data)

Attach pipe to callback.

[modem\_pipe\_transmit](group__modem__pipe.md#ga72311fcb03f138d57e230af60340c9f6)

int modem\_pipe\_transmit(struct modem\_pipe \*pipe, const uint8\_t \*buf, size\_t size)

Transmit data through pipe.

[modem\_pipe\_open](group__modem__pipe.md#ga7521ac0aeda8027c47741237e8312bf0)

int modem\_pipe\_open(struct modem\_pipe \*pipe, k\_timeout\_t timeout)

Open pipe.

[modem\_pipe\_close\_async](group__modem__pipe.md#ga9814c9a1a5da33b2787ac058a6a037f5)

int modem\_pipe\_close\_async(struct modem\_pipe \*pipe)

Close pipe asynchronously.

[modem\_pipe\_receive](group__modem__pipe.md#gab030b4040725ad4dab2399840ef73fde)

int modem\_pipe\_receive(struct modem\_pipe \*pipe, uint8\_t \*buf, size\_t size)

Receive data through pipe.

[modem\_pipe\_event](group__modem__pipe.md#gab9dd98d92d6446dd43852d280574f67a)

modem\_pipe\_event

Modem pipe event.

**Definition** pipe.h:25

[modem\_pipe\_release](group__modem__pipe.md#gad1a9fa3dba49a86c187328b7ee022293)

void modem\_pipe\_release(struct modem\_pipe \*pipe)

Clear callback.

[modem\_pipe\_api\_callback](group__modem__pipe.md#gaf64941177c179cb9086a5736d1ea56f1)

void(\* modem\_pipe\_api\_callback)(struct modem\_pipe \*pipe, enum modem\_pipe\_event event, void \*user\_data)

**Definition** pipe.h:42

[MODEM\_PIPE\_EVENT\_RECEIVE\_READY](group__modem__pipe.md#ggab9dd98d92d6446dd43852d280574f67aa6687ded90e569690afc72020e78624c4)

@ MODEM\_PIPE\_EVENT\_RECEIVE\_READY

**Definition** pipe.h:27

[MODEM\_PIPE\_EVENT\_OPENED](group__modem__pipe.md#ggab9dd98d92d6446dd43852d280574f67aa68d9924c9fc58cf9ca8760573d32f891)

@ MODEM\_PIPE\_EVENT\_OPENED

**Definition** pipe.h:26

[MODEM\_PIPE\_EVENT\_TRANSMIT\_IDLE](group__modem__pipe.md#ggab9dd98d92d6446dd43852d280574f67aaa6e11b11afb91ec50c4d0dfb363e7ad4)

@ MODEM\_PIPE\_EVENT\_TRANSMIT\_IDLE

**Definition** pipe.h:28

[MODEM\_PIPE\_EVENT\_CLOSED](group__modem__pipe.md#ggab9dd98d92d6446dd43852d280574f67aae3ed9618f4986a7c3bef59e16a61316f)

@ MODEM\_PIPE\_EVENT\_CLOSED

**Definition** pipe.h:29

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [pipe.h](pipe_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
