---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/serial_2uart__emul_8h_source.html
original_path: doxygen/html/serial_2uart__emul_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_emul.h

[Go to the documentation of this file.](serial_2uart__emul_8h.md)

1/\*

2 \* Copyright (c) 2023 Fabian Blatz

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SERIAL\_UART\_EMUL\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_SERIAL\_UART\_EMUL\_H\_

14

15#include <[zephyr/device.h](device_8h.md)>

16#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

[ 30](serial_2uart__emul_8h.md#ad31912ff18e7c7faf9849322d9c8a55b)typedef void (\*[uart\_emul\_callback\_tx\_data\_ready\_t](serial_2uart__emul_8h.md#ad31912ff18e7c7faf9849322d9c8a55b))(const struct [device](structdevice.md) \*dev, size\_t size,

31 void \*user\_data);

32

[ 43](serial_2uart__emul_8h.md#af3abd76a768e8031a1bba533f74044be)void [uart\_emul\_callback\_tx\_data\_ready\_set](serial_2uart__emul_8h.md#af3abd76a768e8031a1bba533f74044be)(const struct [device](structdevice.md) \*dev,

44 [uart\_emul\_callback\_tx\_data\_ready\_t](serial_2uart__emul_8h.md#ad31912ff18e7c7faf9849322d9c8a55b) cb, void \*user\_data);

45

[ 55](serial_2uart__emul_8h.md#ad0a91bf5b91639c912f41bd93aeacd69)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [uart\_emul\_put\_rx\_data](serial_2uart__emul_8h.md#ad0a91bf5b91639c912f41bd93aeacd69)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), size\_t size);

56

[ 66](serial_2uart__emul_8h.md#ae8aba3de78a625318524abfd46da1daa)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [uart\_emul\_get\_tx\_data](serial_2uart__emul_8h.md#ae8aba3de78a625318524abfd46da1daa)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), size\_t size);

67

[ 75](serial_2uart__emul_8h.md#a33278a5d083c2bb26cbd11088a1cba2e)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [uart\_emul\_flush\_rx\_data](serial_2uart__emul_8h.md#a33278a5d083c2bb26cbd11088a1cba2e)(const struct [device](structdevice.md) \*dev);

76

[ 84](serial_2uart__emul_8h.md#a1b7ee65706693f0489e6464bc04f689b)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [uart\_emul\_flush\_tx\_data](serial_2uart__emul_8h.md#a1b7ee65706693f0489e6464bc04f689b)(const struct [device](structdevice.md) \*dev);

85

[ 92](serial_2uart__emul_8h.md#a305c155ed8a824e7ddec0ad078669aa0)void [uart\_emul\_set\_errors](serial_2uart__emul_8h.md#a305c155ed8a824e7ddec0ad078669aa0)(const struct [device](structdevice.md) \*dev, int errors);

93

[ 100](serial_2uart__emul_8h.md#af15ff078214f0c7a96fc8c0091a8f922)void [uart\_emul\_set\_release\_buffer\_on\_timeout](serial_2uart__emul_8h.md#af15ff078214f0c7a96fc8c0091a8f922)(const struct [device](structdevice.md) \*dev, bool release\_on\_timeout);

101

102#ifdef \_\_cplusplus

103}

104#endif

105

106#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SERIAL\_UART\_EMUL\_H\_ \*/

[device.h](device_8h.md)

[types.h](include_2zephyr_2types_8h.md)

[uart\_emul\_flush\_tx\_data](serial_2uart__emul_8h.md#a1b7ee65706693f0489e6464bc04f689b)

uint32\_t uart\_emul\_flush\_tx\_data(const struct device \*dev)

Clear TX buffer content.

[uart\_emul\_set\_errors](serial_2uart__emul_8h.md#a305c155ed8a824e7ddec0ad078669aa0)

void uart\_emul\_set\_errors(const struct device \*dev, int errors)

Sets one or more driver errors.

[uart\_emul\_flush\_rx\_data](serial_2uart__emul_8h.md#a33278a5d083c2bb26cbd11088a1cba2e)

uint32\_t uart\_emul\_flush\_rx\_data(const struct device \*dev)

Clear RX buffer content.

[uart\_emul\_put\_rx\_data](serial_2uart__emul_8h.md#ad0a91bf5b91639c912f41bd93aeacd69)

uint32\_t uart\_emul\_put\_rx\_data(const struct device \*dev, const uint8\_t \*data, size\_t size)

Write (copy) data to RX buffer.

[uart\_emul\_callback\_tx\_data\_ready\_t](serial_2uart__emul_8h.md#ad31912ff18e7c7faf9849322d9c8a55b)

void(\* uart\_emul\_callback\_tx\_data\_ready\_t)(const struct device \*dev, size\_t size, void \*user\_data)

Define the application callback function signature for uart\_emul\_callback\_tx\_data\_ready\_set() functio...

**Definition** uart\_emul.h:30

[uart\_emul\_get\_tx\_data](serial_2uart__emul_8h.md#ae8aba3de78a625318524abfd46da1daa)

uint32\_t uart\_emul\_get\_tx\_data(const struct device \*dev, uint8\_t \*data, size\_t size)

Read data from TX buffer.

[uart\_emul\_set\_release\_buffer\_on\_timeout](serial_2uart__emul_8h.md#af15ff078214f0c7a96fc8c0091a8f922)

void uart\_emul\_set\_release\_buffer\_on\_timeout(const struct device \*dev, bool release\_on\_timeout)

Configures if rx buffer should be released on timeout, even when only partially filled.

[uart\_emul\_callback\_tx\_data\_ready\_set](serial_2uart__emul_8h.md#af3abd76a768e8031a1bba533f74044be)

void uart\_emul\_callback\_tx\_data\_ready\_set(const struct device \*dev, uart\_emul\_callback\_tx\_data\_ready\_t cb, void \*user\_data)

Set the TX data ready callback.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:422

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [serial](dir_19e6ea47bd3dc215ff4232c3392e0b57.md)
- [uart\_emul.h](serial_2uart__emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
