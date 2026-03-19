---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/console_2tty_8h_source.html
original_path: doxygen/html/console_2tty_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tty.h

[Go to the documentation of this file.](console_2tty_8h.md)

1/\*

2 \* Copyright (c) 2018 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_CONSOLE\_TTY\_H\_

8#define ZEPHYR\_INCLUDE\_CONSOLE\_TTY\_H\_

9

10#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

11#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

12#include <[zephyr/kernel.h](kernel_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

[ 18](structtty__serial.md)struct [tty\_serial](structtty__serial.md) {

[ 19](structtty__serial.md#a6264c52c87ee712552dc5278bfd2cade) const struct [device](structdevice.md) \*[uart\_dev](structtty__serial.md#a6264c52c87ee712552dc5278bfd2cade);

20

[ 21](structtty__serial.md#a7a3e934bc78b098cbe65789c58dd6076) struct k\_sem [rx\_sem](structtty__serial.md#a7a3e934bc78b098cbe65789c58dd6076);

[ 22](structtty__serial.md#a21484e1aa96bdf6281fdca4abbcc076e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[rx\_ringbuf](structtty__serial.md#a21484e1aa96bdf6281fdca4abbcc076e);

[ 23](structtty__serial.md#a6a05698de6e3a1e1e17b74e3f2c976ea) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rx\_ringbuf\_sz](structtty__serial.md#a6a05698de6e3a1e1e17b74e3f2c976ea);

[ 24](structtty__serial.md#a6fb2a066e70acd11257f525909463997) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rx\_get](structtty__serial.md#a6fb2a066e70acd11257f525909463997), [rx\_put](structtty__serial.md#a4c86a08aa09213f67b4695644d9379b6);

[ 25](structtty__serial.md#a78c894c6cf667bd81db68d4cfbac76fe) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [rx\_timeout](structtty__serial.md#a78c894c6cf667bd81db68d4cfbac76fe);

26

[ 27](structtty__serial.md#adf19fb8b5d7446037ae316ec1f72e759) struct k\_sem [tx\_sem](structtty__serial.md#adf19fb8b5d7446037ae316ec1f72e759);

[ 28](structtty__serial.md#ad06fda068fe0cc27be516e6533ecef83) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[tx\_ringbuf](structtty__serial.md#ad06fda068fe0cc27be516e6533ecef83);

[ 29](structtty__serial.md#a37e46e6176c0726465b558bedadfd890) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_ringbuf\_sz](structtty__serial.md#a37e46e6176c0726465b558bedadfd890);

[ 30](structtty__serial.md#a71d580fe2224a5c68ba02eb089df3bad) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tx\_get](structtty__serial.md#a71d580fe2224a5c68ba02eb089df3bad), [tx\_put](structtty__serial.md#a63f204b21deb4381157d7f6b46e0d922);

[ 31](structtty__serial.md#ac3c6954da53e2e89bc6fa56af80ef8b3) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [tx\_timeout](structtty__serial.md#ac3c6954da53e2e89bc6fa56af80ef8b3);

32};

33

[ 52](console_2tty_8h.md#a5a880bb61f0bdb0f37c501acc0408d32)int [tty\_init](console_2tty_8h.md#a5a880bb61f0bdb0f37c501acc0408d32)(struct [tty\_serial](structtty__serial.md) \*tty, const struct [device](structdevice.md) \*uart\_dev);

53

[ 63](console_2tty_8h.md#a109fd8ee6b581a796d67025a0e33abde)static inline void [tty\_set\_rx\_timeout](console_2tty_8h.md#a109fd8ee6b581a796d67025a0e33abde)(struct [tty\_serial](structtty__serial.md) \*tty, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

64{

65 tty->[rx\_timeout](structtty__serial.md#a78c894c6cf667bd81db68d4cfbac76fe) = timeout;

66}

67

[ 77](console_2tty_8h.md#a1c19c6ed8207ae711e047f9ae446e399)static inline void [tty\_set\_tx\_timeout](console_2tty_8h.md#a1c19c6ed8207ae711e047f9ae446e399)(struct [tty\_serial](structtty__serial.md) \*tty, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

78{

79 tty->[tx\_timeout](structtty__serial.md#ac3c6954da53e2e89bc6fa56af80ef8b3) = timeout;

80}

81

[ 93](console_2tty_8h.md#ad05b854f19b3bd97e2635bc8ebc07ce2)int [tty\_set\_rx\_buf](console_2tty_8h.md#ad05b854f19b3bd97e2635bc8ebc07ce2)(struct [tty\_serial](structtty__serial.md) \*tty, void \*buf, size\_t size);

94

[ 108](console_2tty_8h.md#af6383a47f82797af9a45bc81d84de1be)int [tty\_set\_tx\_buf](console_2tty_8h.md#af6383a47f82797af9a45bc81d84de1be)(struct [tty\_serial](structtty__serial.md) \*tty, void \*buf, size\_t size);

109

[ 121](console_2tty_8h.md#a90ec3fbbe5f0fad19361d23e821c960c)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [tty\_read](console_2tty_8h.md#a90ec3fbbe5f0fad19361d23e821c960c)(struct [tty\_serial](structtty__serial.md) \*tty, void \*buf, size\_t size);

122

[ 133](console_2tty_8h.md#af60d8a57ac3cb81a0a003a011a0f31e5)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [tty\_write](console_2tty_8h.md#af60d8a57ac3cb81a0a003a011a0f31e5)(struct [tty\_serial](structtty__serial.md) \*tty, const void \*buf, size\_t size);

134

135#ifdef \_\_cplusplus

136}

137#endif

138

139#endif /\* ZEPHYR\_INCLUDE\_CONSOLE\_TTY\_H\_ \*/

[tty\_set\_rx\_timeout](console_2tty_8h.md#a109fd8ee6b581a796d67025a0e33abde)

static void tty\_set\_rx\_timeout(struct tty\_serial \*tty, int32\_t timeout)

Set receive timeout for tty device.

**Definition** tty.h:63

[tty\_set\_tx\_timeout](console_2tty_8h.md#a1c19c6ed8207ae711e047f9ae446e399)

static void tty\_set\_tx\_timeout(struct tty\_serial \*tty, int32\_t timeout)

Set transmit timeout for tty device.

**Definition** tty.h:77

[tty\_init](console_2tty_8h.md#a5a880bb61f0bdb0f37c501acc0408d32)

int tty\_init(struct tty\_serial \*tty, const struct device \*uart\_dev)

Initialize serial port object (classically known as tty).

[tty\_read](console_2tty_8h.md#a90ec3fbbe5f0fad19361d23e821c960c)

ssize\_t tty\_read(struct tty\_serial \*tty, void \*buf, size\_t size)

Read data from a tty device.

[tty\_set\_rx\_buf](console_2tty_8h.md#ad05b854f19b3bd97e2635bc8ebc07ce2)

int tty\_set\_rx\_buf(struct tty\_serial \*tty, void \*buf, size\_t size)

Set receive buffer for tty device.

[tty\_write](console_2tty_8h.md#af60d8a57ac3cb81a0a003a011a0f31e5)

ssize\_t tty\_write(struct tty\_serial \*tty, const void \*buf, size\_t size)

Write data to tty device.

[tty\_set\_tx\_buf](console_2tty_8h.md#af6383a47f82797af9a45bc81d84de1be)

int tty\_set\_tx\_buf(struct tty\_serial \*tty, void \*buf, size\_t size)

Set transmit buffer for tty device.

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

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[tty\_serial](structtty__serial.md)

**Definition** tty.h:18

[tty\_serial::rx\_ringbuf](structtty__serial.md#a21484e1aa96bdf6281fdca4abbcc076e)

uint8\_t \* rx\_ringbuf

**Definition** tty.h:22

[tty\_serial::tx\_ringbuf\_sz](structtty__serial.md#a37e46e6176c0726465b558bedadfd890)

uint32\_t tx\_ringbuf\_sz

**Definition** tty.h:29

[tty\_serial::rx\_put](structtty__serial.md#a4c86a08aa09213f67b4695644d9379b6)

uint16\_t rx\_put

**Definition** tty.h:24

[tty\_serial::uart\_dev](structtty__serial.md#a6264c52c87ee712552dc5278bfd2cade)

const struct device \* uart\_dev

**Definition** tty.h:19

[tty\_serial::tx\_put](structtty__serial.md#a63f204b21deb4381157d7f6b46e0d922)

uint16\_t tx\_put

**Definition** tty.h:30

[tty\_serial::rx\_ringbuf\_sz](structtty__serial.md#a6a05698de6e3a1e1e17b74e3f2c976ea)

uint32\_t rx\_ringbuf\_sz

**Definition** tty.h:23

[tty\_serial::rx\_get](structtty__serial.md#a6fb2a066e70acd11257f525909463997)

uint16\_t rx\_get

**Definition** tty.h:24

[tty\_serial::tx\_get](structtty__serial.md#a71d580fe2224a5c68ba02eb089df3bad)

uint16\_t tx\_get

**Definition** tty.h:30

[tty\_serial::rx\_timeout](structtty__serial.md#a78c894c6cf667bd81db68d4cfbac76fe)

int32\_t rx\_timeout

**Definition** tty.h:25

[tty\_serial::rx\_sem](structtty__serial.md#a7a3e934bc78b098cbe65789c58dd6076)

struct k\_sem rx\_sem

**Definition** tty.h:21

[tty\_serial::tx\_timeout](structtty__serial.md#ac3c6954da53e2e89bc6fa56af80ef8b3)

int32\_t tx\_timeout

**Definition** tty.h:31

[tty\_serial::tx\_ringbuf](structtty__serial.md#ad06fda068fe0cc27be516e6533ecef83)

uint8\_t \* tx\_ringbuf

**Definition** tty.h:28

[tty\_serial::tx\_sem](structtty__serial.md#adf19fb8b5d7446037ae316ec1f72e759)

struct k\_sem tx\_sem

**Definition** tty.h:27

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [console](dir_2f086bf88c9e3ffd4c7c065f4bf7757c.md)
- [tty.h](console_2tty_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
