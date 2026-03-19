---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hwinfo_8h_source.html
original_path: doxygen/html/hwinfo_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hwinfo.h

[Go to the documentation of this file.](hwinfo_8h.md)

1

6

7/\*

8 \* Copyright (c) 2018 Alexander Wachter

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_HWINFO\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_HWINFO\_H\_

15

24

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

27#include <stddef.h>

28#include <[errno.h](errno_8h.md)>

29#include <[zephyr/kernel.h](kernel_8h.md)>

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

[ 41](group__hwinfo__interface.md#ga08bca59db4b190eaaea4d47b7562869c)#define RESET\_PIN BIT(0)

[ 43](group__hwinfo__interface.md#ga737ea2c652086e38a9b895cc42593908)#define RESET\_SOFTWARE BIT(1)

[ 45](group__hwinfo__interface.md#gac9dc9b22ba1fc551a3d68810155a640e)#define RESET\_BROWNOUT BIT(2)

[ 47](group__hwinfo__interface.md#ga21fa7b8a5ec2e1c077dbc453ca3a4265)#define RESET\_POR BIT(3)

[ 49](group__hwinfo__interface.md#ga112ab452e5015120edcb88b9a6de3de0)#define RESET\_WATCHDOG BIT(4)

[ 51](group__hwinfo__interface.md#ga031454a8ff535f8cf66ddbdbc2acba5e)#define RESET\_DEBUG BIT(5)

[ 53](group__hwinfo__interface.md#ga846cce95f808d3c1a5b48376f8de3612)#define RESET\_SECURITY BIT(6)

[ 55](group__hwinfo__interface.md#ga3ce47e00b35b155416a3d48dd5c477ac)#define RESET\_LOW\_POWER\_WAKE BIT(7)

[ 57](group__hwinfo__interface.md#gad6721dc841941ccdca349999ce655e83)#define RESET\_CPU\_LOCKUP BIT(8)

[ 59](group__hwinfo__interface.md#gac32af4272b5356a498cb3d4ce6fb87e7)#define RESET\_PARITY BIT(9)

[ 61](group__hwinfo__interface.md#gaed16942e0487d525c79c539b385e6f31)#define RESET\_PLL BIT(10)

[ 63](group__hwinfo__interface.md#ga9bb4063cded0167c496b834d642fd73c)#define RESET\_CLOCK BIT(11)

[ 65](group__hwinfo__interface.md#gaf9659a85b05447ef9267606182bf568a)#define RESET\_HARDWARE BIT(12)

[ 67](group__hwinfo__interface.md#ga5aa032c5d8560a4bb351ca29d1464939)#define RESET\_USER BIT(13)

[ 69](group__hwinfo__interface.md#gade167088d6c99163f5af385bcac93f58)#define RESET\_TEMPERATURE BIT(14)

73

[ 94](group__hwinfo__interface.md#ga197b58d995c77aae423527d0f8d9ff31)\_\_syscall [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [hwinfo\_get\_device\_id](group__hwinfo__interface.md#ga197b58d995c77aae423527d0f8d9ff31)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, size\_t length);

95

96[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) z\_impl\_hwinfo\_get\_device\_id([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, size\_t length);

97

[ 110](group__hwinfo__interface.md#ga0f5ab222b4f7e75a3e9d3650e954a036)\_\_syscall int [hwinfo\_get\_device\_eui64](group__hwinfo__interface.md#ga0f5ab222b4f7e75a3e9d3650e954a036)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer);

111

112int z\_impl\_hwinfo\_get\_device\_eui64([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer);

113

[ 134](group__hwinfo__interface.md#ga390c1c29088813ace17856ffa97d97b5)\_\_syscall int [hwinfo\_get\_reset\_cause](group__hwinfo__interface.md#ga390c1c29088813ace17856ffa97d97b5)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*cause);

135

136int z\_impl\_hwinfo\_get\_reset\_cause([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*cause);

137

[ 147](group__hwinfo__interface.md#gaeaa23e68c53eb6a2b56f06c74b83e613)\_\_syscall int [hwinfo\_clear\_reset\_cause](group__hwinfo__interface.md#gaeaa23e68c53eb6a2b56f06c74b83e613)(void);

148

149int z\_impl\_hwinfo\_clear\_reset\_cause(void);

150

[ 162](group__hwinfo__interface.md#gaf0d345653c4fbb5f38a78aba766a6bb8)\_\_syscall int [hwinfo\_get\_supported\_reset\_cause](group__hwinfo__interface.md#gaf0d345653c4fbb5f38a78aba766a6bb8)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*supported);

163

164int z\_impl\_hwinfo\_get\_supported\_reset\_cause([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*supported);

165

169

170#ifdef \_\_cplusplus

171}

172#endif

173

174#include <zephyr/syscalls/hwinfo.h>

175

176#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_HWINFO\_H\_ \*/

[errno.h](errno_8h.md)

System error numbers.

[hwinfo\_get\_device\_eui64](group__hwinfo__interface.md#ga0f5ab222b4f7e75a3e9d3650e954a036)

int hwinfo\_get\_device\_eui64(uint8\_t \*buffer)

Copy the device EUI64 to a buffer.

[hwinfo\_get\_device\_id](group__hwinfo__interface.md#ga197b58d995c77aae423527d0f8d9ff31)

ssize\_t hwinfo\_get\_device\_id(uint8\_t \*buffer, size\_t length)

Copy the device id to a buffer.

[hwinfo\_get\_reset\_cause](group__hwinfo__interface.md#ga390c1c29088813ace17856ffa97d97b5)

int hwinfo\_get\_reset\_cause(uint32\_t \*cause)

Retrieve cause of device reset.

[hwinfo\_clear\_reset\_cause](group__hwinfo__interface.md#gaeaa23e68c53eb6a2b56f06c74b83e613)

int hwinfo\_clear\_reset\_cause(void)

Clear cause of device reset.

[hwinfo\_get\_supported\_reset\_cause](group__hwinfo__interface.md#gaf0d345653c4fbb5f38a78aba766a6bb8)

int hwinfo\_get\_supported\_reset\_cause(uint32\_t \*supported)

Get supported reset cause flags.

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [hwinfo.h](hwinfo_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
