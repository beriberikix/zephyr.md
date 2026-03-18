---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/retention_8h_source.html
original_path: doxygen/html/retention_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

retention.h

[Go to the documentation of this file.](retention_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_RETENTION\_

13#define ZEPHYR\_INCLUDE\_RETENTION\_

14

15#include <[stdint.h](stdint_8h.md)>

16#include <stddef.h>

17#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

18#include <[zephyr/kernel.h](kernel_8h.md)>

19#include <[zephyr/device.h](device_8h.md)>

20#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

34

[ 35](group__retention__api.md#ga769bf90c91fd3722878869fac90f9b49)typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[retention\_size\_api](group__retention__api.md#ga769bf90c91fd3722878869fac90f9b49))(const struct [device](structdevice.md) \*dev);

[ 36](group__retention__api.md#gaefaa65af1dc36193ddd4e75c9bc5d7ca)typedef int (\*[retention\_is\_valid\_api](group__retention__api.md#gaefaa65af1dc36193ddd4e75c9bc5d7ca))(const struct [device](structdevice.md) \*dev);

[ 37](group__retention__api.md#ga6f9ae5917a8fbe4353da2f5a643c56b9)typedef int (\*[retention\_read\_api](group__retention__api.md#ga6f9ae5917a8fbe4353da2f5a643c56b9))(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer,

38 size\_t size);

[ 39](group__retention__api.md#ga45734d6dbf7438229a2d51de58f304b5)typedef int (\*[retention\_write\_api](group__retention__api.md#ga45734d6dbf7438229a2d51de58f304b5))(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

40 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, size\_t size);

[ 41](group__retention__api.md#ga87c06c45b70c4bf2e3a2c7f36b26ab89)typedef int (\*[retention\_clear\_api](group__retention__api.md#ga87c06c45b70c4bf2e3a2c7f36b26ab89))(const struct [device](structdevice.md) \*dev);

42

[ 43](structretention__api.md)struct [retention\_api](structretention__api.md) {

[ 44](structretention__api.md#ac92d0f6bd43fa0cbe2695deab72d98fa) [retention\_size\_api](group__retention__api.md#ga769bf90c91fd3722878869fac90f9b49) [size](structretention__api.md#ac92d0f6bd43fa0cbe2695deab72d98fa);

[ 45](structretention__api.md#a6a6f7f01474b924bb8b042125c2b3b3a) [retention\_is\_valid\_api](group__retention__api.md#gaefaa65af1dc36193ddd4e75c9bc5d7ca) [is\_valid](structretention__api.md#a6a6f7f01474b924bb8b042125c2b3b3a);

[ 46](structretention__api.md#af067a77869e1e528ebc9f6d3230f7dc0) [retention\_read\_api](group__retention__api.md#ga6f9ae5917a8fbe4353da2f5a643c56b9) [read](structretention__api.md#af067a77869e1e528ebc9f6d3230f7dc0);

[ 47](structretention__api.md#a11e7d9bb0238fd5e5b0ef25c1b254420) [retention\_write\_api](group__retention__api.md#ga45734d6dbf7438229a2d51de58f304b5) [write](structretention__api.md#a11e7d9bb0238fd5e5b0ef25c1b254420);

[ 48](structretention__api.md#a9800e85498958dfd499706a21207ca63) [retention\_clear\_api](group__retention__api.md#ga87c06c45b70c4bf2e3a2c7f36b26ab89) [clear](structretention__api.md#a9800e85498958dfd499706a21207ca63);

49};

50

[ 59](group__retention__api.md#gaf20780720d64144b50e03f9e04d3f39b)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [retention\_size](group__retention__api.md#gaf20780720d64144b50e03f9e04d3f39b)(const struct [device](structdevice.md) \*dev);

60

[ 71](group__retention__api.md#gaa3f12ad0b1929a828e8d42c7c073a16d)int [retention\_is\_valid](group__retention__api.md#gaa3f12ad0b1929a828e8d42c7c073a16d)(const struct [device](structdevice.md) \*dev);

72

[ 84](group__retention__api.md#ga7b4c04850ec0b57d120a0f1425d8b583)int [retention\_read](group__retention__api.md#ga7b4c04850ec0b57d120a0f1425d8b583)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, size\_t size);

85

[ 98](group__retention__api.md#ga6131168ffc3f6d0e4329cf56f32071cc)int [retention\_write](group__retention__api.md#ga6131168ffc3f6d0e4329cf56f32071cc)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, size\_t size);

99

[ 107](group__retention__api.md#gaab8a56b5879faabd10982bc110577a1d)int [retention\_clear](group__retention__api.md#gaab8a56b5879faabd10982bc110577a1d)(const struct [device](structdevice.md) \*dev);

108

112

113#ifdef \_\_cplusplus

114}

115#endif

116

117#endif /\* ZEPHYR\_INCLUDE\_RETENTION\_ \*/

[device.h](device_8h.md)

[retention\_write\_api](group__retention__api.md#ga45734d6dbf7438229a2d51de58f304b5)

int(\* retention\_write\_api)(const struct device \*dev, off\_t offset, const uint8\_t \*buffer, size\_t size)

**Definition** retention.h:39

[retention\_write](group__retention__api.md#ga6131168ffc3f6d0e4329cf56f32071cc)

int retention\_write(const struct device \*dev, off\_t offset, const uint8\_t \*buffer, size\_t size)

Writes data to the retention area (underlying data does not need to be cleared prior to writing),...

[retention\_read\_api](group__retention__api.md#ga6f9ae5917a8fbe4353da2f5a643c56b9)

int(\* retention\_read\_api)(const struct device \*dev, off\_t offset, uint8\_t \*buffer, size\_t size)

**Definition** retention.h:37

[retention\_size\_api](group__retention__api.md#ga769bf90c91fd3722878869fac90f9b49)

ssize\_t(\* retention\_size\_api)(const struct device \*dev)

**Definition** retention.h:35

[retention\_read](group__retention__api.md#ga7b4c04850ec0b57d120a0f1425d8b583)

int retention\_read(const struct device \*dev, off\_t offset, uint8\_t \*buffer, size\_t size)

Reads data from the retention area.

[retention\_clear\_api](group__retention__api.md#ga87c06c45b70c4bf2e3a2c7f36b26ab89)

int(\* retention\_clear\_api)(const struct device \*dev)

**Definition** retention.h:41

[retention\_is\_valid](group__retention__api.md#gaa3f12ad0b1929a828e8d42c7c073a16d)

int retention\_is\_valid(const struct device \*dev)

Checks if the underlying data in the retention area is valid or not.

[retention\_clear](group__retention__api.md#gaab8a56b5879faabd10982bc110577a1d)

int retention\_clear(const struct device \*dev)

Clears all data in the retention area (sets it to 0).

[retention\_is\_valid\_api](group__retention__api.md#gaefaa65af1dc36193ddd4e75c9bc5d7ca)

int(\* retention\_is\_valid\_api)(const struct device \*dev)

**Definition** retention.h:36

[retention\_size](group__retention__api.md#gaf20780720d64144b50e03f9e04d3f39b)

ssize\_t retention\_size(const struct device \*dev)

Returns the size of the retention area.

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[retention\_api](structretention__api.md)

**Definition** retention.h:43

[retention\_api::write](structretention__api.md#a11e7d9bb0238fd5e5b0ef25c1b254420)

retention\_write\_api write

**Definition** retention.h:47

[retention\_api::is\_valid](structretention__api.md#a6a6f7f01474b924bb8b042125c2b3b3a)

retention\_is\_valid\_api is\_valid

**Definition** retention.h:45

[retention\_api::clear](structretention__api.md#a9800e85498958dfd499706a21207ca63)

retention\_clear\_api clear

**Definition** retention.h:48

[retention\_api::size](structretention__api.md#ac92d0f6bd43fa0cbe2695deab72d98fa)

retention\_size\_api size

**Definition** retention.h:44

[retention\_api::read](structretention__api.md#af067a77869e1e528ebc9f6d3230f7dc0)

retention\_read\_api read

**Definition** retention.h:46

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [retention](dir_acb4c99582103da541bc87f13e94ee5a.md)
- [retention.h](retention_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
