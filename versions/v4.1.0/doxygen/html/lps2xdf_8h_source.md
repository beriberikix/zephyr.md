---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/lps2xdf_8h_source.html
original_path: doxygen/html/lps2xdf_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lps2xdf.h

[Go to the documentation of this file.](lps2xdf_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicroelectronics

3 \* Copyright (c) 2023 PHYTEC Messtechnik GmbH

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LPS2xDF\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LPS2xDF\_H\_

9

10/\* Data rate \*/

[ 11](lps2xdf_8h.md#aba5086849d797518ce64484c3f7c40c2)#define LPS2xDF\_DT\_ODR\_POWER\_DOWN 0

[ 12](lps2xdf_8h.md#a4ace0b4fcaa9251e69c934564c116634)#define LPS2xDF\_DT\_ODR\_1HZ 1

[ 13](lps2xdf_8h.md#a30282e0a4f090bb3106ccb21f577de64)#define LPS2xDF\_DT\_ODR\_4HZ 2

[ 14](lps2xdf_8h.md#a9bfb85c1e7e6a5f176e6e52447112ba1)#define LPS2xDF\_DT\_ODR\_10HZ 3

[ 15](lps2xdf_8h.md#a7ff9cde8d5f782008fd302962e61f62e)#define LPS2xDF\_DT\_ODR\_25HZ 4

[ 16](lps2xdf_8h.md#a5f767d66c25ee9d30b292f451fe898e9)#define LPS2xDF\_DT\_ODR\_50HZ 5

[ 17](lps2xdf_8h.md#aead62a263aae03b5a4b0d4aa4832c921)#define LPS2xDF\_DT\_ODR\_75HZ 6

[ 18](lps2xdf_8h.md#a014ee98e7252de3f16d5cc95d602a575)#define LPS2xDF\_DT\_ODR\_100HZ 7

[ 19](lps2xdf_8h.md#a75287fb5fe773719de936e3c35b38935)#define LPS2xDF\_DT\_ODR\_200HZ 8

20

21/\* Low Pass filter \*/

[ 22](lps2xdf_8h.md#ae76b2b2a597dfc2f15dbf310a49846dd)#define LPS2xDF\_DT\_LP\_FILTER\_OFF 0

[ 23](lps2xdf_8h.md#a73930a4a4a834b102cacfcc262b47b05)#define LPS2xDF\_DT\_LP\_FILTER\_ODR\_4 1

[ 24](lps2xdf_8h.md#a3dbce218e79cfb34de7cacb216cf9e12)#define LPS2xDF\_DT\_LP\_FILTER\_ODR\_9 3

25

26/\* Average (number of samples) filter \*/

[ 27](lps2xdf_8h.md#aa2a9f4859187ec438fbf0caf8e97d2d1)#define LPS2xDF\_DT\_AVG\_4\_SAMPLES 0

[ 28](lps2xdf_8h.md#ab8401d04498cbc2db82f653fe43bd9c6)#define LPS2xDF\_DT\_AVG\_8\_SAMPLES 1

[ 29](lps2xdf_8h.md#aa78c0c206a4313eeb53607d2f1541a8d)#define LPS2xDF\_DT\_AVG\_16\_SAMPLES 2

[ 30](lps2xdf_8h.md#a0aa8b28e50ad119bec6082bd152fa6cc)#define LPS2xDF\_DT\_AVG\_32\_SAMPLES 3

[ 31](lps2xdf_8h.md#a5859a72559cf5121f284eaf3c2acf50f)#define LPS2xDF\_DT\_AVG\_64\_SAMPLES 4

[ 32](lps2xdf_8h.md#a17b064199992bae3a44fbe34f068f042)#define LPS2xDF\_DT\_AVG\_128\_SAMPLES 5

[ 33](lps2xdf_8h.md#a5695d812598ee97cf07a0f13a229c08c)#define LPS2xDF\_DT\_AVG\_256\_SAMPLES 6

[ 34](lps2xdf_8h.md#ac656a90e3be782d9df47c4bb893843c1)#define LPS2xDF\_DT\_AVG\_512\_SAMPLES 7

35

36/\* Full Scale Pressure Mode \*/

[ 37](lps2xdf_8h.md#a77848469494ffd8912bdc79f65e6fe86)#define LPS28DFW\_DT\_FS\_MODE\_1\_1260 0

[ 38](lps2xdf_8h.md#a924ab5b02a02c3b28626a87f860c0055)#define LPS28DFW\_DT\_FS\_MODE\_2\_4060 1

39

40/\* Full Scale Pressure Mode \*/

[ 41](lps2xdf_8h.md#abcff3a9fb4a7b883b75bc59c5bd547f3)#define ILPS22QS\_DT\_FS\_MODE\_1\_1260 0

[ 42](lps2xdf_8h.md#a896769c2a9611c670d3e04e554c35ea0)#define ILPS22QS\_DT\_FS\_MODE\_2\_4060 1

43

44#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LPS22DF\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lps2xdf.h](lps2xdf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
