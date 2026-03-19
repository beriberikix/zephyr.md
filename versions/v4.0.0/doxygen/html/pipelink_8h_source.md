---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/pipelink_8h_source.html
original_path: doxygen/html/pipelink_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pipelink.h

[Go to the documentation of this file.](pipelink_8h.md)

1/\*

2 \* Copyright (c) 2024 Trackunit Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#include <[zephyr/modem/pipe.h](pipe_8h.md)>

8#include <[zephyr/devicetree.h](devicetree_8h.md)>

9#include <[zephyr/sys/util.h](sys_2util_8h.md)>

10

11#ifndef ZEPHYR\_MODEM\_PIPELINK\_

12#define ZEPHYR\_MODEM\_PIPELINK\_

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

24

[ 26](group__modem__pipelink.md#ga399168cacd287e376df68c4cf221ba00)enum [modem\_pipelink\_event](group__modem__pipelink.md#ga399168cacd287e376df68c4cf221ba00) {

[ 28](group__modem__pipelink.md#gga399168cacd287e376df68c4cf221ba00ab1a51a16b5dbe02ebca8fb0efe4be81f) [MODEM\_PIPELINK\_EVENT\_CONNECTED](group__modem__pipelink.md#gga399168cacd287e376df68c4cf221ba00ab1a51a16b5dbe02ebca8fb0efe4be81f) = 0,

[ 30](group__modem__pipelink.md#gga399168cacd287e376df68c4cf221ba00ae118b022efcba2033701dfb8f2e7d38d) [MODEM\_PIPELINK\_EVENT\_DISCONNECTED](group__modem__pipelink.md#gga399168cacd287e376df68c4cf221ba00ae118b022efcba2033701dfb8f2e7d38d),

31};

32

34

36struct modem\_pipelink;

37

39

[ 46](group__modem__pipelink.md#ga4f93732f1df6cab41cc352526d6a849e)typedef void (\*[modem\_pipelink\_callback](group__modem__pipelink.md#ga4f93732f1df6cab41cc352526d6a849e))(struct modem\_pipelink \*link,

47 enum [modem\_pipelink\_event](group__modem__pipelink.md#ga399168cacd287e376df68c4cf221ba00) event,

48 void \*user\_data);

49

51

53struct modem\_pipelink {

54 struct modem\_pipe \*pipe;

55 [modem\_pipelink\_callback](group__modem__pipelink.md#ga4f93732f1df6cab41cc352526d6a849e) callback;

56 void \*user\_data;

57 bool connected;

58 struct [k\_spinlock](structk__spinlock.md) spinlock;

59};

60

62

[ 69](group__modem__pipelink.md#ga7ee7b3454a9fe94c20855a893dd2b2a1)void [modem\_pipelink\_attach](group__modem__pipelink.md#ga7ee7b3454a9fe94c20855a893dd2b2a1)(struct modem\_pipelink \*link,

70 [modem\_pipelink\_callback](group__modem__pipelink.md#ga4f93732f1df6cab41cc352526d6a849e) callback,

71 void \*user\_data);

72

[ 79](group__modem__pipelink.md#ga7c7638ad3f22533f374e002b787b11ce)bool [modem\_pipelink\_is\_connected](group__modem__pipelink.md#ga7c7638ad3f22533f374e002b787b11ce)(struct modem\_pipelink \*link);

80

[ 87](group__modem__pipelink.md#gab09d76f7bd93a19b82a7d5e818b80d80)struct modem\_pipe \*[modem\_pipelink\_get\_pipe](group__modem__pipelink.md#gab09d76f7bd93a19b82a7d5e818b80d80)(struct modem\_pipelink \*link);

88

[ 93](group__modem__pipelink.md#ga684ff47ddb0e0487022cea62052b32e2)void [modem\_pipelink\_release](group__modem__pipelink.md#ga684ff47ddb0e0487022cea62052b32e2)(struct modem\_pipelink \*link);

94

96

98void modem\_pipelink\_init(struct modem\_pipelink \*link, struct modem\_pipe \*pipe);

99

101void modem\_pipelink\_notify\_connected(struct modem\_pipelink \*link);

102

104void modem\_pipelink\_notify\_disconnected(struct modem\_pipelink \*link);

105

107

109

115#define MODEM\_PIPELINK\_DT\_SYM(node\_id, name) \

116 \_CONCAT\_4(\_\_modem\_pipelink\_, DT\_DEP\_ORD(node\_id), \_, name)

117

119

[ 125](group__modem__pipelink.md#ga46d06461a5a465f4a73c135f721e3aa5)#define MODEM\_PIPELINK\_DT\_DECLARE(node\_id, name) \

126 extern struct modem\_pipelink MODEM\_PIPELINK\_DT\_SYM(node\_id, name)

127

[ 133](group__modem__pipelink.md#gac1010375931a7a5076d066e2c5ed9a14)#define MODEM\_PIPELINK\_DT\_DEFINE(node\_id, name) \

134 struct modem\_pipelink MODEM\_PIPELINK\_DT\_SYM(node\_id, name)

135

[ 141](group__modem__pipelink.md#gada75e5995e78c8c8daa5a16f5e5abb4a)#define MODEM\_PIPELINK\_DT\_GET(node\_id, name) \

142 (&MODEM\_PIPELINK\_DT\_SYM(node\_id, name))

143

150

[ 151](group__modem__pipelink.md#gaedc5b4665d541fe4d471a287177e6674)#define MODEM\_PIPELINK\_DT\_INST\_DECLARE(inst, name) \

152 MODEM\_PIPELINK\_DT\_DECLARE(DT\_DRV\_INST(inst), name)

153

[ 154](group__modem__pipelink.md#ga1ca071affbb19bfac4c2ef7f25bf9c65)#define MODEM\_PIPELINK\_DT\_INST\_DEFINE(inst, name) \

155 MODEM\_PIPELINK\_DT\_DEFINE(DT\_DRV\_INST(inst), name)

156

[ 157](group__modem__pipelink.md#ga1c3a0ff1f1939e12fdefee85a7f5eeed)#define MODEM\_PIPELINK\_DT\_INST\_GET(inst, name) \

158 MODEM\_PIPELINK\_DT\_GET(DT\_DRV\_INST(inst), name)

159

161

163

164#ifdef \_\_cplusplus

165}

166#endif

167

168#endif /\* ZEPHYR\_MODEM\_PIPELINK\_ \*/

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[modem\_pipelink\_event](group__modem__pipelink.md#ga399168cacd287e376df68c4cf221ba00)

modem\_pipelink\_event

Pipelink event.

**Definition** pipelink.h:26

[modem\_pipelink\_callback](group__modem__pipelink.md#ga4f93732f1df6cab41cc352526d6a849e)

void(\* modem\_pipelink\_callback)(struct modem\_pipelink \*link, enum modem\_pipelink\_event event, void \*user\_data)

Pipelink callback definition.

**Definition** pipelink.h:46

[modem\_pipelink\_release](group__modem__pipelink.md#ga684ff47ddb0e0487022cea62052b32e2)

void modem\_pipelink\_release(struct modem\_pipelink \*link)

Clear callback.

[modem\_pipelink\_is\_connected](group__modem__pipelink.md#ga7c7638ad3f22533f374e002b787b11ce)

bool modem\_pipelink\_is\_connected(struct modem\_pipelink \*link)

Check whether pipelink pipe is connected.

[modem\_pipelink\_attach](group__modem__pipelink.md#ga7ee7b3454a9fe94c20855a893dd2b2a1)

void modem\_pipelink\_attach(struct modem\_pipelink \*link, modem\_pipelink\_callback callback, void \*user\_data)

Attach callback to pipelink.

[modem\_pipelink\_get\_pipe](group__modem__pipelink.md#gab09d76f7bd93a19b82a7d5e818b80d80)

struct modem\_pipe \* modem\_pipelink\_get\_pipe(struct modem\_pipelink \*link)

Get pipe from pipelink.

[MODEM\_PIPELINK\_EVENT\_CONNECTED](group__modem__pipelink.md#gga399168cacd287e376df68c4cf221ba00ab1a51a16b5dbe02ebca8fb0efe4be81f)

@ MODEM\_PIPELINK\_EVENT\_CONNECTED

Modem pipe has been connected and can be opened.

**Definition** pipelink.h:28

[MODEM\_PIPELINK\_EVENT\_DISCONNECTED](group__modem__pipelink.md#gga399168cacd287e376df68c4cf221ba00ae118b022efcba2033701dfb8f2e7d38d)

@ MODEM\_PIPELINK\_EVENT\_DISCONNECTED

Modem pipe has been disconnected and can't be opened.

**Definition** pipelink.h:30

[pipe.h](pipe_8h.md)

[k\_spinlock](structk__spinlock.md)

Kernel Spin Lock.

**Definition** spinlock.h:45

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [pipelink.h](pipelink_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
