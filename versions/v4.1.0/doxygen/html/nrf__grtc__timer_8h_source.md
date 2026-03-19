---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nrf__grtc__timer_8h_source.html
original_path: doxygen/html/nrf__grtc__timer_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nrf\_grtc\_timer.h

[Go to the documentation of this file.](nrf__grtc__timer_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_TIMER\_NRF\_GRTC\_TIMER\_H

8#define ZEPHYR\_INCLUDE\_DRIVERS\_TIMER\_NRF\_GRTC\_TIMER\_H

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

14#include <[zephyr/sys\_clock.h](sys__clock_8h.md)>

15

29typedef void (\*z\_nrf\_grtc\_timer\_compare\_handler\_t)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) id, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) expire\_time,

30 void \*user\_data);

31

37[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) z\_nrf\_grtc\_timer\_chan\_alloc(void);

38

43void z\_nrf\_grtc\_timer\_chan\_free([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan);

44

49[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) z\_nrf\_grtc\_timer\_read(void);

50

58bool z\_nrf\_grtc\_timer\_compare\_evt\_check([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan);

59

68[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_nrf\_grtc\_timer\_compare\_evt\_address\_get([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan);

69

78[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_nrf\_grtc\_timer\_capture\_task\_address\_get([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan);

79

88bool z\_nrf\_grtc\_timer\_compare\_int\_lock([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan);

89

98void z\_nrf\_grtc\_timer\_compare\_int\_unlock([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan, bool key);

99

110int z\_nrf\_grtc\_timer\_compare\_read([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*val);

111

125int z\_nrf\_grtc\_timer\_set([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) target\_time,

126 z\_nrf\_grtc\_timer\_compare\_handler\_t handler, void \*user\_data);

127

138void z\_nrf\_grtc\_timer\_abort([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan);

139

147[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) z\_nrf\_grtc\_timer\_get\_ticks([k\_timeout\_t](structk__timeout__t.md) t);

148

162int z\_nrf\_grtc\_timer\_capture\_prepare([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan);

163

176int z\_nrf\_grtc\_timer\_capture\_read([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) chan, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*captured\_time);

177

190int z\_nrf\_grtc\_wakeup\_prepare([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) wake\_time\_us);

191

[ 199](nrf__grtc__timer_8h.md#a104efab2f0186b68694a14b118c6fd8e)int [nrf\_grtc\_timer\_clock\_driver\_init](nrf__grtc__timer_8h.md#a104efab2f0186b68694a14b118c6fd8e)(void);

200

201#ifdef \_\_cplusplus

202}

203#endif

204

205#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_TIMER\_NRF\_GRTC\_TIMER\_H \*/

[nrf\_grtc\_timer\_clock\_driver\_init](nrf__grtc__timer_8h.md#a104efab2f0186b68694a14b118c6fd8e)

int nrf\_grtc\_timer\_clock\_driver\_init(void)

Initialize the GRTC clock timer driver from an application- defined function.

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
- [nrf\_grtc\_timer.h](nrf__grtc__timer_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
