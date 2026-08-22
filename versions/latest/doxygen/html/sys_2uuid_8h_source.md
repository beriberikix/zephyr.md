---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/sys_2uuid_8h_source.html
original_path: doxygen/html/sys_2uuid_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uuid.h

[Go to the documentation of this file.](sys_2uuid_8h.md)

1/\*

2 \* Copyright (c) 2025, SECO Mind Srl

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_UUID\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_UUID\_H\_

9

16

17#include <[zephyr/kernel.h](kernel_8h.md)>

18#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

31

[ 33](group__uuid.md#ga5db91c4b658dc322b42959cb5c851020)#define UUID\_SIZE 16U

34

[ 36](group__uuid.md#ga6d37dd9ad8391595db1b71ca2103a228)#define UUID\_STR\_LEN 37U

37

[ 39](group__uuid.md#ga1d71eb34412c3e04f9f85bb8320548d6)#define UUID\_BASE64\_LEN 25U

40

[ 45](group__uuid.md#gae28fa917e2f1ad587da4cf901f0de94a)#define UUID\_BASE64URL\_LEN 23U

46

[ 48](structuuid.md)struct [uuid](structuuid.md) {

50 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val[[UUID\_SIZE](group__uuid.md#ga5db91c4b658dc322b42959cb5c851020)];

52};

53

[ 62](group__uuid.md#ga1e1e2f008f5ac3366bf474de27d42b66)int [uuid\_generate\_v4](group__uuid.md#ga1e1e2f008f5ac3366bf474de27d42b66)(struct [uuid](structuuid.md) \*out);

63

[ 80](group__uuid.md#ga6f692b733f600e0346317f3d25d84409)int [uuid\_generate\_v5](group__uuid.md#ga6f692b733f600e0346317f3d25d84409)(const struct [uuid](structuuid.md) \*ns, const void \*data, size\_t data\_size,

81 struct [uuid](structuuid.md) \*out);

82

[ 92](group__uuid.md#ga1fd6f837800e0bd9bd0e4c4e5891568e)int [uuid\_copy](group__uuid.md#ga1fd6f837800e0bd9bd0e4c4e5891568e)(const struct [uuid](structuuid.md) \*data, struct [uuid](structuuid.md) \*out);

93

[ 103](group__uuid.md#gacf4a46349ed1a7a6a44b3cc84c687bc1)int [uuid\_from\_buffer](group__uuid.md#gacf4a46349ed1a7a6a44b3cc84c687bc1)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data[[UUID\_SIZE](group__uuid.md#ga5db91c4b658dc322b42959cb5c851020)], struct [uuid](structuuid.md) \*out);

104

[ 114](group__uuid.md#gadf6084420d0ee8cc41a522ebb2c71e7d)int [uuid\_from\_string](group__uuid.md#gadf6084420d0ee8cc41a522ebb2c71e7d)(const char data[[UUID\_STR\_LEN](group__uuid.md#ga6d37dd9ad8391595db1b71ca2103a228)], struct [uuid](structuuid.md) \*out);

115

[ 125](group__uuid.md#ga2562309a55cbd49b70e1c60a761fb08f)int [uuid\_to\_buffer](group__uuid.md#ga2562309a55cbd49b70e1c60a761fb08f)(const struct [uuid](structuuid.md) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) out[[UUID\_SIZE](group__uuid.md#ga5db91c4b658dc322b42959cb5c851020)]);

126

[ 136](group__uuid.md#gaac4b9f9b243c9ecbeac94f0b4947ede1)int [uuid\_to\_string](group__uuid.md#gaac4b9f9b243c9ecbeac94f0b4947ede1)(const struct [uuid](structuuid.md) \*data, char out[[UUID\_STR\_LEN](group__uuid.md#ga6d37dd9ad8391595db1b71ca2103a228)]);

137

[ 147](group__uuid.md#ga2c73bd8b52693f1c28dbbc10e145e098)int [uuid\_to\_base64](group__uuid.md#ga2c73bd8b52693f1c28dbbc10e145e098)(const struct [uuid](structuuid.md) \*data, char out[[UUID\_BASE64\_LEN](group__uuid.md#ga1d71eb34412c3e04f9f85bb8320548d6)]);

148

[ 159](group__uuid.md#ga68dcce718b9e98d4873fe7c40d99ad4c)int [uuid\_to\_base64url](group__uuid.md#ga68dcce718b9e98d4873fe7c40d99ad4c)(const struct [uuid](structuuid.md) \*data, char out[[UUID\_BASE64URL\_LEN](group__uuid.md#gae28fa917e2f1ad587da4cf901f0de94a)]);

160

164

165#ifdef \_\_cplusplus

166}

167#endif

168

169#endif /\* ZEPHYR\_INCLUDE\_SYS\_UUID\_H\_ \*/

[UUID\_BASE64\_LEN](group__uuid.md#ga1d71eb34412c3e04f9f85bb8320548d6)

#define UUID\_BASE64\_LEN

Length of the UUID base64 string representation, including the NULL terminator.

**Definition** uuid.h:39

[uuid\_generate\_v4](group__uuid.md#ga1e1e2f008f5ac3366bf474de27d42b66)

int uuid\_generate\_v4(struct uuid \*out)

Generate a UUIDv4.

[uuid\_copy](group__uuid.md#ga1fd6f837800e0bd9bd0e4c4e5891568e)

int uuid\_copy(const struct uuid \*data, struct uuid \*out)

Copy an UUID into another UUID.

[uuid\_to\_buffer](group__uuid.md#ga2562309a55cbd49b70e1c60a761fb08f)

int uuid\_to\_buffer(const struct uuid \*data, uint8\_t out[16U])

Create a uuid\_t from a binary (big-endian) formatted UUID.

[uuid\_to\_base64](group__uuid.md#ga2c73bd8b52693f1c28dbbc10e145e098)

int uuid\_to\_base64(const struct uuid \*data, char out[25U])

Convert a UUID to its base 64 (RFC 3548, RFC 4648) string representation.

[UUID\_SIZE](group__uuid.md#ga5db91c4b658dc322b42959cb5c851020)

#define UUID\_SIZE

Number of bytes in the binary representation of a UUID.

**Definition** uuid.h:33

[uuid\_to\_base64url](group__uuid.md#ga68dcce718b9e98d4873fe7c40d99ad4c)

int uuid\_to\_base64url(const struct uuid \*data, char out[23U])

Convert a UUID to its base 64 (RFC 4648 sec.

[UUID\_STR\_LEN](group__uuid.md#ga6d37dd9ad8391595db1b71ca2103a228)

#define UUID\_STR\_LEN

Length of the UUID canonical string representation, including the NULL terminator.

**Definition** uuid.h:36

[uuid\_generate\_v5](group__uuid.md#ga6f692b733f600e0346317f3d25d84409)

int uuid\_generate\_v5(const struct uuid \*ns, const void \*data, size\_t data\_size, struct uuid \*out)

Generate a UUIDv5.

[uuid\_to\_string](group__uuid.md#gaac4b9f9b243c9ecbeac94f0b4947ede1)

int uuid\_to\_string(const struct uuid \*data, char out[37U])

Convert a UUID to its canonical (RFC9562) string representation.

[uuid\_from\_buffer](group__uuid.md#gacf4a46349ed1a7a6a44b3cc84c687bc1)

int uuid\_from\_buffer(const uint8\_t data[16U], struct uuid \*out)

Create a uuid\_t from a binary (big-endian) formatted UUID.

[uuid\_from\_string](group__uuid.md#gadf6084420d0ee8cc41a522ebb2c71e7d)

int uuid\_from\_string(const char data[37U], struct uuid \*out)

Parse a UUID from its canonical (RFC9562) string representation.

[UUID\_BASE64URL\_LEN](group__uuid.md#gae28fa917e2f1ad587da4cf901f0de94a)

#define UUID\_BASE64URL\_LEN

Length of the UUID base64 URL and filename safe string representation, including the NULL terminator.

**Definition** uuid.h:45

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uuid](structuuid.md)

Binary representation of a UUID.

**Definition** uuid.h:48

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [uuid.h](sys_2uuid_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
