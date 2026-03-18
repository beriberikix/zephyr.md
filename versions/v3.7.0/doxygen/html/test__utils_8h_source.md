---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/test__utils_8h_source.html
original_path: doxygen/html/test__utils_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

test\_utils.h

[Go to the documentation of this file.](test__utils_8h.md)

1/\* test\_utils.h - TinyCrypt interface to common functions for tests \*/

2

3/\*

4 \* Copyright (C) 2015 by Intel Corporation, All Rights Reserved.

5 \*

6 \* Redistribution and use in source and binary forms, with or without

7 \* modification, are permitted provided that the following conditions are met:

8 \*

9 \* - Redistributions of source code must retain the above copyright notice,

10 \* this list of conditions and the following disclaimer.

11 \*

12 \* - Redistributions in binary form must reproduce the above copyright

13 \* notice, this list of conditions and the following disclaimer in the

14 \* documentation and/or other materials provided with the distribution.

15 \*

16 \* - Neither the name of Intel Corporation nor the names of its contributors

17 \* may be used to endorse or promote products derived from this software

18 \* without specific prior written permission.

19 \*

20 \* THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"

21 \* AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE

22 \* IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE

23 \* DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE

24 \* FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL

25 \* DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR

26 \* SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER

27 \* CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,

28 \* OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE

29 \* OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

30 \*/

31

32#ifndef \_\_TEST\_UTILS\_H\_\_

33#define \_\_TEST\_UTILS\_H\_\_

34

35#include <[zephyr/tc\_util.h](tc__util_8h.md)>

36#include <tinycrypt/constants.h>

37

[ 38](test__utils_8h.md#ac6d829df5f0e4fd29a01d2302366bd6a)static inline void [show\_str](test__utils_8h.md#ac6d829df5f0e4fd29a01d2302366bd6a)(const char \*label, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), size\_t len)

39{

40 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) i;

41

42 [TC\_PRINT](tc__util_8h.md#a31562104efbbaec65655dc0b661c0164)("%s = ", label);

43 for (i = 0U; i < ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))len; ++i) {

44 [TC\_PRINT](tc__util_8h.md#a31562104efbbaec65655dc0b661c0164)("%02x", [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)[i]);

45 }

46 [TC\_PRINT](tc__util_8h.md#a31562104efbbaec65655dc0b661c0164)("\n");

47}

48

49static inline

[ 50](test__utils_8h.md#a0c05eeb12526a2c168109f7e5a40d833)void [fatal](test__utils_8h.md#a0c05eeb12526a2c168109f7e5a40d833)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) testnum, const void \*expected, size\_t expectedlen,

51 const void \*computed, size\_t computedlen)

52{

53 [TC\_ERROR](tc__util_8h.md#a6fcd0e6c5448a9198cdaed1e88e86e1b)("\tTest #%d Failed!\n", testnum);

54 [show\_str](test__utils_8h.md#ac6d829df5f0e4fd29a01d2302366bd6a)("\t\tExpected", expected, expectedlen);

55 [show\_str](test__utils_8h.md#ac6d829df5f0e4fd29a01d2302366bd6a)("\t\tComputed ", computed, computedlen);

56 [TC\_PRINT](tc__util_8h.md#a31562104efbbaec65655dc0b661c0164)("\n");

57}

58

59static inline

[ 60](test__utils_8h.md#ade1c76cc0df2be800876862b3a5941ab)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [check\_result](test__utils_8h.md#ade1c76cc0df2be800876862b3a5941ab)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) testnum, const void \*expected,

61 size\_t expectedlen, const void \*computed,

62 size\_t computedlen, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) verbose)

63{

64 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) result = [TC\_PASS](tc__util_8h.md#afb66a88e5d1e781aeb5aa9739a8fe868);

65

66 ARG\_UNUSED(verbose);

67

68 if (expectedlen != computedlen) {

69 [TC\_ERROR](tc__util_8h.md#a6fcd0e6c5448a9198cdaed1e88e86e1b)("The length of the computed buffer (%zu)",

70 computedlen);

71 [TC\_ERROR](tc__util_8h.md#a6fcd0e6c5448a9198cdaed1e88e86e1b)("does not match the expected length (%zu).",

72 expectedlen);

73 result = [TC\_FAIL](tc__util_8h.md#a196c300c18de32c79d757131b579a3a5);

74 } else {

75 if ([memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(computed, expected, computedlen) != 0) {

76 [fatal](test__utils_8h.md#a0c05eeb12526a2c168109f7e5a40d833)(testnum, expected, expectedlen,

77 computed, computedlen);

78 result = [TC\_FAIL](tc__util_8h.md#a196c300c18de32c79d757131b579a3a5);

79 }

80 }

81

82 return result;

83}

84

85#endif

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)

int memcmp(const void \*m1, const void \*m2, size\_t n)

[tc\_util.h](tc__util_8h.md)

[TC\_FAIL](tc__util_8h.md#a196c300c18de32c79d757131b579a3a5)

#define TC\_FAIL

**Definition** tc\_util.h:68

[TC\_PRINT](tc__util_8h.md#a31562104efbbaec65655dc0b661c0164)

#define TC\_PRINT(fmt,...)

**Definition** tc\_util.h:133

[TC\_ERROR](tc__util_8h.md#a6fcd0e6c5448a9198cdaed1e88e86e1b)

#define TC\_ERROR(fmt,...)

**Definition** tc\_util.h:117

[TC\_PASS](tc__util_8h.md#afb66a88e5d1e781aeb5aa9739a8fe868)

#define TC\_PASS

**Definition** tc\_util.h:67

[fatal](test__utils_8h.md#a0c05eeb12526a2c168109f7e5a40d833)

static void fatal(uint32\_t testnum, const void \*expected, size\_t expectedlen, const void \*computed, size\_t computedlen)

**Definition** test\_utils.h:50

[show\_str](test__utils_8h.md#ac6d829df5f0e4fd29a01d2302366bd6a)

static void show\_str(const char \*label, const uint8\_t \*s, size\_t len)

**Definition** test\_utils.h:38

[check\_result](test__utils_8h.md#ade1c76cc0df2be800876862b3a5941ab)

static uint32\_t check\_result(uint32\_t testnum, const void \*expected, size\_t expectedlen, const void \*computed, size\_t computedlen, uint32\_t verbose)

**Definition** test\_utils.h:60

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [include](dir_d5cd24c9babba9527629083c466f69cc.md)
- [zephyr](dir_91e5ce9bd56815b1bd388aa667b3762f.md)
- [test\_utils.h](test__utils_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
