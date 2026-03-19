---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/eth__adin2111_8h_source.html
original_path: doxygen/html/eth__adin2111_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eth\_adin2111.h

[Go to the documentation of this file.](eth__adin2111_8h.md)

1/\*

2 \* Copyright (c) 2023 PHOENIX CONTACT Electronics GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_ETH\_ADIN2111\_H\_\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_ETH\_ADIN2111\_H\_\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <[zephyr/kernel.h](kernel_8h.md)>

12#include <[zephyr/device.h](device_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

[ 30](eth__adin2111_8h.md#a54e88cd118466a1a44ef02197fe2b59d)int [eth\_adin2111\_lock](eth__adin2111_8h.md#a54e88cd118466a1a44ef02197fe2b59d)(const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) timeout);

31

[ 41](eth__adin2111_8h.md#a72b5466138f087ac4e788bc878781c3e)int [eth\_adin2111\_unlock](eth__adin2111_8h.md#a72b5466138f087ac4e788bc878781c3e)(const struct [device](structdevice.md) \*dev);

42

[ 56](eth__adin2111_8h.md#ac768d3625f30e4a90903a3070347f38c)int [eth\_adin2111\_reg\_write](eth__adin2111_8h.md#ac768d3625f30e4a90903a3070347f38c)(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

57

[ 71](eth__adin2111_8h.md#a06e40561475a7f997e706da388717414)int [eth\_adin2111\_reg\_read](eth__adin2111_8h.md#a06e40561475a7f997e706da388717414)(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val);

72

[ 87](eth__adin2111_8h.md#ab2a247e4ee0c3ff778a972768ee5bc51)int [eth\_adin2111\_reg\_update](eth__adin2111_8h.md#ab2a247e4ee0c3ff778a972768ee5bc51)(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg,

88 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data);

89

[ 102](eth__adin2111_8h.md#a340b4d3786807c7feb423b36d6533a87)int [eth\_adin2111\_sw\_reset](eth__adin2111_8h.md#a340b4d3786807c7feb423b36d6533a87)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) delay);

103

[ 116](eth__adin2111_8h.md#ad737f44a16702f4c8ce3f8a8ae994364)int [eth\_adin2111\_mac\_reset](eth__adin2111_8h.md#ad737f44a16702f4c8ce3f8a8ae994364)(const struct [device](structdevice.md) \*dev);

117

[ 131](eth__adin2111_8h.md#a9752b1a6a75880af069af1b00ce43928)int [eth\_adin2111\_broadcast\_filter](eth__adin2111_8h.md#a9752b1a6a75880af069af1b00ce43928)(const struct [device](structdevice.md) \*dev, bool enable);

132

[ 141](eth__adin2111_8h.md#a86de61f524a1837ff8f701c5af969d1b)struct [net\_if](structnet__if.md) \*[eth\_adin2111\_get\_iface](eth__adin2111_8h.md#a86de61f524a1837ff8f701c5af969d1b)(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) port\_idx);

142

143#ifdef \_\_cplusplus

144}

145#endif

146

147#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_ETH\_ADIN2111\_H\_\_ \*/

[device.h](device_8h.md)

[eth\_adin2111\_reg\_read](eth__adin2111_8h.md#a06e40561475a7f997e706da388717414)

int eth\_adin2111\_reg\_read(const struct device \*dev, const uint16\_t reg, uint32\_t \*val)

Reads host MAC interface register over SPI.

[eth\_adin2111\_sw\_reset](eth__adin2111_8h.md#a340b4d3786807c7feb423b36d6533a87)

int eth\_adin2111\_sw\_reset(const struct device \*dev, uint16\_t delay)

Reset both the MAC and PHY.

[eth\_adin2111\_lock](eth__adin2111_8h.md#a54e88cd118466a1a44ef02197fe2b59d)

int eth\_adin2111\_lock(const struct device \*dev, k\_timeout\_t timeout)

Locks device access.

[eth\_adin2111\_unlock](eth__adin2111_8h.md#a72b5466138f087ac4e788bc878781c3e)

int eth\_adin2111\_unlock(const struct device \*dev)

Unlocks device access.

[eth\_adin2111\_get\_iface](eth__adin2111_8h.md#a86de61f524a1837ff8f701c5af969d1b)

struct net\_if \* eth\_adin2111\_get\_iface(const struct device \*dev, const uint16\_t port\_idx)

Get the port-related net\_if reference.

[eth\_adin2111\_broadcast\_filter](eth__adin2111_8h.md#a9752b1a6a75880af069af1b00ce43928)

int eth\_adin2111\_broadcast\_filter(const struct device \*dev, bool enable)

Enable/disable the forwarding (to host) of broadcast frames.

[eth\_adin2111\_reg\_update](eth__adin2111_8h.md#ab2a247e4ee0c3ff778a972768ee5bc51)

int eth\_adin2111\_reg\_update(const struct device \*dev, const uint16\_t reg, uint32\_t mask, uint32\_t data)

Update host MAC interface register over SPI.

[eth\_adin2111\_reg\_write](eth__adin2111_8h.md#ac768d3625f30e4a90903a3070347f38c)

int eth\_adin2111\_reg\_write(const struct device \*dev, const uint16\_t reg, uint32\_t val)

Writes host MAC interface register over SPI.

[eth\_adin2111\_mac\_reset](eth__adin2111_8h.md#ad737f44a16702f4c8ce3f8a8ae994364)

int eth\_adin2111\_mac\_reset(const struct device \*dev)

Reset the MAC device.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:680

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [ethernet](dir_e26e025f1b2d5c43527f6232564fe44e.md)
- [eth\_adin2111.h](eth__adin2111_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
