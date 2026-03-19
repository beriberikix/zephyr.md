---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/lorawan_2emul_8h_source.html
original_path: doxygen/html/lorawan_2emul_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

emul.h

[Go to the documentation of this file.](lorawan_2emul_8h.md)

1/\*

2 \* Copyright (c) 2024 A Labs GmbH

3 \* Copyright (c) 2024 tado GmbH

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_LORAWAN\_EMUL\_H\_

9#define ZEPHYR\_INCLUDE\_LORAWAN\_EMUL\_H\_

10

11#include <[stdbool.h](stdbool_8h.md)>

12#include <[stdint.h](stdint_8h.md)>

13

14#include <[zephyr/lorawan/lorawan.h](lorawan_8h.md)>

15

[ 23](lorawan_2emul_8h.md#ad3b92479562707f0819696a5de0baa41)typedef void (\*[lorawan\_uplink\_cb\_t](lorawan_2emul_8h.md#ad3b92479562707f0819696a5de0baa41))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) port, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data);

24

[ 35](lorawan_2emul_8h.md#abedb7884445ac1bb0eb0351a6c413761)void [lorawan\_emul\_send\_downlink](lorawan_2emul_8h.md#abedb7884445ac1bb0eb0351a6c413761)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) port, bool data\_pending, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) rssi, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) snr,

36 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data);

37

[ 43](lorawan_2emul_8h.md#a665c46cfe16f6c894e44a3bfbbf235b7)void [lorawan\_emul\_register\_uplink\_callback](lorawan_2emul_8h.md#a665c46cfe16f6c894e44a3bfbbf235b7)([lorawan\_uplink\_cb\_t](lorawan_2emul_8h.md#ad3b92479562707f0819696a5de0baa41) cb);

44

45#endif /\* ZEPHYR\_INCLUDE\_LORAWAN\_EMUL\_H\_ \*/

[lorawan\_emul\_register\_uplink\_callback](lorawan_2emul_8h.md#a665c46cfe16f6c894e44a3bfbbf235b7)

void lorawan\_emul\_register\_uplink\_callback(lorawan\_uplink\_cb\_t cb)

Register callback for emulated uplink messages.

[lorawan\_emul\_send\_downlink](lorawan_2emul_8h.md#abedb7884445ac1bb0eb0351a6c413761)

void lorawan\_emul\_send\_downlink(uint8\_t port, bool data\_pending, int16\_t rssi, int8\_t snr, uint8\_t len, const uint8\_t \*data)

Emulate LoRaWAN downlink message.

[lorawan\_uplink\_cb\_t](lorawan_2emul_8h.md#ad3b92479562707f0819696a5de0baa41)

void(\* lorawan\_uplink\_cb\_t)(uint8\_t port, uint8\_t len, const uint8\_t \*data)

Defines the emulator uplink callback handler function signature.

**Definition** emul.h:23

[lorawan.h](lorawan_8h.md)

Public LoRaWAN APIs.

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [lorawan](dir_025fd8c7c9e823719407606758d0c447.md)
- [emul.h](lorawan_2emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
