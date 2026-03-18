---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/shell__log__backend_8h_source.html
original_path: doxygen/html/shell__log__backend_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_log\_backend.h

[Go to the documentation of this file.](shell__log__backend_8h.md)

1/\*

2 \* Copyright (c) 2018 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef SHELL\_LOG\_BACKEND\_H\_\_

8#define SHELL\_LOG\_BACKEND\_H\_\_

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11#include <[zephyr/logging/log\_backend.h](log__backend_8h.md)>

12#include <[zephyr/logging/log\_output.h](log__output_8h.md)>

13#include <[zephyr/sys/mpsc\_pbuf.h](mpsc__pbuf_8h.md)>

14#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

19extern const struct [log\_backend\_api](structlog__backend__api.md) [log\_backend\_shell\_api](group__shell__api.md#gaddf27615ed72440ecb63aa1d84962c82);

20

[ 22](shell__log__backend_8h.md#a4d98f9c89ac476fe4ef2299921dd0c7d)enum [shell\_log\_backend\_state](shell__log__backend_8h.md#a4d98f9c89ac476fe4ef2299921dd0c7d) {

[ 23](shell__log__backend_8h.md#a4d98f9c89ac476fe4ef2299921dd0c7da1dd95c355c7e47f53dee0804e8209b1d) [SHELL\_LOG\_BACKEND\_UNINIT](shell__log__backend_8h.md#a4d98f9c89ac476fe4ef2299921dd0c7da1dd95c355c7e47f53dee0804e8209b1d),

[ 24](shell__log__backend_8h.md#a4d98f9c89ac476fe4ef2299921dd0c7daf49ef7ffee9d397007533897ba0cf935) [SHELL\_LOG\_BACKEND\_ENABLED](shell__log__backend_8h.md#a4d98f9c89ac476fe4ef2299921dd0c7daf49ef7ffee9d397007533897ba0cf935),

[ 25](shell__log__backend_8h.md#a4d98f9c89ac476fe4ef2299921dd0c7dae0888042a003fdb68effd8a63358cc57) [SHELL\_LOG\_BACKEND\_DISABLED](shell__log__backend_8h.md#a4d98f9c89ac476fe4ef2299921dd0c7dae0888042a003fdb68effd8a63358cc57),

[ 26](shell__log__backend_8h.md#a4d98f9c89ac476fe4ef2299921dd0c7da82ae0d6b6bd04ff39b2485b2a078362f) [SHELL\_LOG\_BACKEND\_PANIC](shell__log__backend_8h.md#a4d98f9c89ac476fe4ef2299921dd0c7da82ae0d6b6bd04ff39b2485b2a078362f),

27};

28

[ 30](structshell__log__backend__control__block.md)struct [shell\_log\_backend\_control\_block](structshell__log__backend__control__block.md) {

[ 31](structshell__log__backend__control__block.md#abade26ad804e1f890f33e26290e10ea2) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [dropped\_cnt](structshell__log__backend__control__block.md#abade26ad804e1f890f33e26290e10ea2);

[ 32](structshell__log__backend__control__block.md#a244df3aac60b84d1e5ef7bbdc360c807) enum [shell\_log\_backend\_state](shell__log__backend_8h.md#a4d98f9c89ac476fe4ef2299921dd0c7d) [state](structshell__log__backend__control__block.md#a244df3aac60b84d1e5ef7bbdc360c807);

33};

34

[ 36](structshell__log__backend.md)struct [shell\_log\_backend](structshell__log__backend.md) {

[ 37](structshell__log__backend.md#a653ca6a48ab4d6166ad9e2e25afbbca9) const struct [log\_backend](structlog__backend.md) \*[backend](structshell__log__backend.md#a653ca6a48ab4d6166ad9e2e25afbbca9);

[ 38](structshell__log__backend.md#ad535b0244a1936cce72c10e14c3ca605) const struct [log\_output](structshell__log__backend.md#ad535b0244a1936cce72c10e14c3ca605) \*[log\_output](structshell__log__backend.md#ad535b0244a1936cce72c10e14c3ca605);

[ 39](structshell__log__backend.md#af6439c070382d4376d347328ed942695) struct [shell\_log\_backend\_control\_block](structshell__log__backend__control__block.md) \*[control\_block](structshell__log__backend.md#af6439c070382d4376d347328ed942695);

[ 40](structshell__log__backend.md#a24632f6459b4587de33646d809088b53) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timeout](structshell__log__backend.md#a24632f6459b4587de33646d809088b53);

[ 41](structshell__log__backend.md#aa04574a9aa9a1268850555f8c9756402) const struct [mpsc\_pbuf\_buffer\_config](structmpsc__pbuf__buffer__config.md) \*[mpsc\_buffer\_config](structshell__log__backend.md#aa04574a9aa9a1268850555f8c9756402);

[ 42](structshell__log__backend.md#a4382a87da96780513c1717fa760630b0) struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*[mpsc\_buffer](structshell__log__backend.md#a4382a87da96780513c1717fa760630b0);

43};

44

[ 46](structshell__log__backend__msg.md)struct [shell\_log\_backend\_msg](structshell__log__backend__msg.md) {

[ 47](structshell__log__backend__msg.md#a5384e4abed0cc4f7799eb957da4d47c5) struct [log\_msg](structlog__msg.md) \*[msg](structshell__log__backend__msg.md#a5384e4abed0cc4f7799eb957da4d47c5);

[ 48](structshell__log__backend__msg.md#a87af115f2c8c9222f3b4926866b957ba) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp](structshell__log__backend__msg.md#a87af115f2c8c9222f3b4926866b957ba);

49};

50

52int z\_shell\_log\_backend\_output\_func([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structlog__msg.md#a2336290d5ac4b87cbd998d81cc49ab7e), size\_t length, void \*ctx);

53

69#ifdef CONFIG\_SHELL\_LOG\_BACKEND

70#define Z\_SHELL\_LOG\_BACKEND\_DEFINE(\_name, \_buf, \_size, \_queue\_size, \_timeout) \

71 LOG\_BACKEND\_DEFINE(\_name##\_backend, log\_backend\_shell\_api, false); \

72 LOG\_OUTPUT\_DEFINE(\_name##\_log\_output, z\_shell\_log\_backend\_output\_func,\

73 \_buf, \_size); \

74 static struct shell\_log\_backend\_control\_block \_name##\_control\_block; \

75 static uint32\_t \_\_aligned(Z\_LOG\_MSG\_ALIGNMENT) \

76 \_name##\_buf[\_queue\_size / sizeof(uint32\_t)]; \

77 const struct mpsc\_pbuf\_buffer\_config \_name##\_mpsc\_buffer\_config = { \

78 .buf = \_name##\_buf, \

79 .size = ARRAY\_SIZE(\_name##\_buf), \

80 .notify\_drop = NULL, \

81 .get\_wlen = log\_msg\_generic\_get\_wlen, \

82 .flags = MPSC\_PBUF\_MODE\_OVERWRITE, \

83 }; \

84 struct mpsc\_pbuf\_buffer \_name##\_mpsc\_buffer; \

85 static const struct shell\_log\_backend \_name##\_log\_backend = { \

86 .backend = &\_name##\_backend, \

87 .log\_output = &\_name##\_log\_output, \

88 .control\_block = &\_name##\_control\_block, \

89 .timeout = \_timeout, \

90 .mpsc\_buffer\_config = &\_name##\_mpsc\_buffer\_config, \

91 .mpsc\_buffer = &\_name##\_mpsc\_buffer, \

92 }

93

94#define Z\_SHELL\_LOG\_BACKEND\_PTR(\_name) (&\_name##\_log\_backend)

95#else /\* CONFIG\_LOG \*/

96#define Z\_SHELL\_LOG\_BACKEND\_DEFINE(\_name, \_buf, \_size, \_queue\_size, \_timeout)

97#define Z\_SHELL\_LOG\_BACKEND\_PTR(\_name) NULL

98#endif /\* CONFIG\_LOG \*/

99

106void z\_shell\_log\_backend\_enable(const struct [shell\_log\_backend](structshell__log__backend.md) \*backend,

107 void \*ctx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) init\_log\_level);

108

113void z\_shell\_log\_backend\_disable(const struct [shell\_log\_backend](structshell__log__backend.md) \*backend);

114

121bool z\_shell\_log\_backend\_process(const struct [shell\_log\_backend](structshell__log__backend.md) \*backend);

122

123#ifdef \_\_cplusplus

124}

125#endif

126

127#endif /\* SHELL\_LOG\_BACKEND\_H\_\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[log\_backend\_shell\_api](group__shell__api.md#gaddf27615ed72440ecb63aa1d84962c82)

const struct log\_backend\_api log\_backend\_shell\_api

[kernel.h](kernel_8h.md)

Public kernel APIs.

[log\_backend.h](log__backend_8h.md)

[log\_output.h](log__output_8h.md)

[mpsc\_pbuf.h](mpsc__pbuf_8h.md)

[shell\_log\_backend\_state](shell__log__backend_8h.md#a4d98f9c89ac476fe4ef2299921dd0c7d)

shell\_log\_backend\_state

Shell log backend states.

**Definition** shell\_log\_backend.h:22

[SHELL\_LOG\_BACKEND\_UNINIT](shell__log__backend_8h.md#a4d98f9c89ac476fe4ef2299921dd0c7da1dd95c355c7e47f53dee0804e8209b1d)

@ SHELL\_LOG\_BACKEND\_UNINIT

**Definition** shell\_log\_backend.h:23

[SHELL\_LOG\_BACKEND\_PANIC](shell__log__backend_8h.md#a4d98f9c89ac476fe4ef2299921dd0c7da82ae0d6b6bd04ff39b2485b2a078362f)

@ SHELL\_LOG\_BACKEND\_PANIC

**Definition** shell\_log\_backend.h:26

[SHELL\_LOG\_BACKEND\_DISABLED](shell__log__backend_8h.md#a4d98f9c89ac476fe4ef2299921dd0c7dae0888042a003fdb68effd8a63358cc57)

@ SHELL\_LOG\_BACKEND\_DISABLED

**Definition** shell\_log\_backend.h:25

[SHELL\_LOG\_BACKEND\_ENABLED](shell__log__backend_8h.md#a4d98f9c89ac476fe4ef2299921dd0c7daf49ef7ffee9d397007533897ba0cf935)

@ SHELL\_LOG\_BACKEND\_ENABLED

**Definition** shell\_log\_backend.h:24

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[log\_backend\_api](structlog__backend__api.md)

Logger backend API.

**Definition** log\_backend.h:63

[log\_backend](structlog__backend.md)

Logger backend structure.

**Definition** log\_backend.h:94

[log\_msg](structlog__msg.md)

**Definition** log\_msg.h:94

[log\_msg::data](structlog__msg.md#a2336290d5ac4b87cbd998d81cc49ab7e)

uint8\_t data[]

**Definition** log\_msg.h:100

[mpsc\_pbuf\_buffer\_config](structmpsc__pbuf__buffer__config.md)

MPSC packet buffer configuration.

**Definition** mpsc\_pbuf.h:131

[mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md)

MPSC packet buffer structure.

**Definition** mpsc\_pbuf.h:90

[shell\_log\_backend\_control\_block](structshell__log__backend__control__block.md)

Shell log backend control block (RW data).

**Definition** shell\_log\_backend.h:30

[shell\_log\_backend\_control\_block::state](structshell__log__backend__control__block.md#a244df3aac60b84d1e5ef7bbdc360c807)

enum shell\_log\_backend\_state state

**Definition** shell\_log\_backend.h:32

[shell\_log\_backend\_control\_block::dropped\_cnt](structshell__log__backend__control__block.md#abade26ad804e1f890f33e26290e10ea2)

atomic\_t dropped\_cnt

**Definition** shell\_log\_backend.h:31

[shell\_log\_backend\_msg](structshell__log__backend__msg.md)

Shell log backend message structure.

**Definition** shell\_log\_backend.h:46

[shell\_log\_backend\_msg::msg](structshell__log__backend__msg.md#a5384e4abed0cc4f7799eb957da4d47c5)

struct log\_msg \* msg

**Definition** shell\_log\_backend.h:47

[shell\_log\_backend\_msg::timestamp](structshell__log__backend__msg.md#a87af115f2c8c9222f3b4926866b957ba)

uint32\_t timestamp

**Definition** shell\_log\_backend.h:48

[shell\_log\_backend](structshell__log__backend.md)

Shell log backend instance structure (RO data).

**Definition** shell\_log\_backend.h:36

[shell\_log\_backend::timeout](structshell__log__backend.md#a24632f6459b4587de33646d809088b53)

uint32\_t timeout

**Definition** shell\_log\_backend.h:40

[shell\_log\_backend::mpsc\_buffer](structshell__log__backend.md#a4382a87da96780513c1717fa760630b0)

struct mpsc\_pbuf\_buffer \* mpsc\_buffer

**Definition** shell\_log\_backend.h:42

[shell\_log\_backend::backend](structshell__log__backend.md#a653ca6a48ab4d6166ad9e2e25afbbca9)

const struct log\_backend \* backend

**Definition** shell\_log\_backend.h:37

[shell\_log\_backend::mpsc\_buffer\_config](structshell__log__backend.md#aa04574a9aa9a1268850555f8c9756402)

const struct mpsc\_pbuf\_buffer\_config \* mpsc\_buffer\_config

**Definition** shell\_log\_backend.h:41

[shell\_log\_backend::log\_output](structshell__log__backend.md#ad535b0244a1936cce72c10e14c3ca605)

const struct log\_output \* log\_output

**Definition** shell\_log\_backend.h:38

[shell\_log\_backend::control\_block](structshell__log__backend.md#af6439c070382d4376d347328ed942695)

struct shell\_log\_backend\_control\_block \* control\_block

**Definition** shell\_log\_backend.h:39

[atomic.h](sys_2atomic_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_log\_backend.h](shell__log__backend_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
