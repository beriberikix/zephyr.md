---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/nrf__rtc__timer_8h_source.html
original_path: doxygen/html/nrf__rtc__timer_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nrf\_rtc\_timer.h

[Go to the documentation of this file.](nrf__rtc__timer_8h.md)

1/\*

2 \* Copyright (c) 2016-2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_TIMER\_NRF\_RTC\_TIMER\_H

8#define ZEPHYR\_INCLUDE\_DRIVERS\_TIMER\_NRF\_RTC\_TIMER\_H

9

10#include <[zephyr/sys\_clock.h](sys__clock_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 18](nrf__rtc__timer_8h.md#adf3ef3038c82f7970bb1898186df58a7)#define NRF\_RTC\_TIMER\_MAX\_SCHEDULE\_SPAN BIT(23)

19

33typedef void (\*z\_nrf\_rtc\_timer\_compare\_handler\_t)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) id,

34 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) expire\_time,

35 void \*user\_data);

36

44[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) z\_nrf\_rtc\_timer\_chan\_alloc(void);

45

50void z\_nrf\_rtc\_timer\_chan\_free([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan);

51

56[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) z\_nrf\_rtc\_timer\_read(void);

57

66[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_nrf\_rtc\_timer\_compare\_evt\_address\_get([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan);

67

78[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_nrf\_rtc\_timer\_capture\_task\_address\_get([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan);

79

88bool z\_nrf\_rtc\_timer\_compare\_int\_lock([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan);

89

98void z\_nrf\_rtc\_timer\_compare\_int\_unlock([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan, bool key);

99

106[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_nrf\_rtc\_timer\_compare\_read([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan);

107

133int z\_nrf\_rtc\_timer\_set([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) target\_time,

134 z\_nrf\_rtc\_timer\_compare\_handler\_t handler,

135 void \*user\_data);

136

162int z\_nrf\_rtc\_timer\_exact\_set([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) target\_time,

163 z\_nrf\_rtc\_timer\_compare\_handler\_t handler,

164 void \*user\_data);

165

176void z\_nrf\_rtc\_timer\_abort([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan);

177

186[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) z\_nrf\_rtc\_timer\_get\_ticks([k\_timeout\_t](structk__timeout__t.md) t);

187

199int z\_nrf\_rtc\_timer\_nrf53net\_offset\_get(void);

200

214int z\_nrf\_rtc\_timer\_trigger\_overflow(void);

215

216#ifdef \_\_cplusplus

217}

218#endif

219

220#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_TIMER\_NRF\_RTC\_TIMER\_H \*/

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[sys\_clock.h](sys__clock_8h.md)

Variables needed for system clock.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [timer](dir_21cf19e3c466cbc66f61aa827c3fd772.md)
- [nrf\_rtc\_timer.h](nrf__rtc__timer_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
