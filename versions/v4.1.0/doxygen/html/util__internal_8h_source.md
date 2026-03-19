---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/util__internal_8h_source.html
original_path: doxygen/html/util__internal_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

util\_internal.h

[Go to the documentation of this file.](util__internal_8h.md)

1/\*

2 \* Copyright (c) 2011-2014, Wind River Systems, Inc.

3 \* Copyright (c) 2020, Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

14

15#ifndef ZEPHYR\_INCLUDE\_SYS\_UTIL\_INTERNAL\_H\_

16#define ZEPHYR\_INCLUDE\_SYS\_UTIL\_INTERNAL\_H\_

17

18#include "[util\_loops.h](util__loops_8h.md)"

19

20/\* IS\_ENABLED() helpers \*/

21

22/\* This is called from IS\_ENABLED(), and sticks on a "\_XXXX" prefix,

23 \* it will now be "\_XXXX1" if config\_macro is "1", or just "\_XXXX" if it's

24 \* undefined.

25 \* ENABLED: Z\_IS\_ENABLED2(\_XXXX1)

26 \* DISABLED Z\_IS\_ENABLED2(\_XXXX)

27 \*/

28#define Z\_IS\_ENABLED1(config\_macro) Z\_IS\_ENABLED2(\_XXXX##config\_macro)

29

30/\* Here's the core trick, we map "\_XXXX1" to "\_YYYY," (i.e. a string

31 \* with a trailing comma), so it has the effect of making this a

32 \* two-argument tuple to the preprocessor only in the case where the

33 \* value is defined to "1"

34 \* ENABLED: \_YYYY, <--- note comma!

35 \* DISABLED: \_XXXX

36 \*/

37#define \_XXXX1 \_YYYY,

38

39/\* Then we append an extra argument to fool the gcc preprocessor into

40 \* accepting it as a varargs macro.

41 \* arg1 arg2 arg3

42 \* ENABLED: Z\_IS\_ENABLED3(\_YYYY, 1, 0)

43 \* DISABLED Z\_IS\_ENABLED3(\_XXXX 1, 0)

44 \*/

45#define Z\_IS\_ENABLED2(one\_or\_two\_args) Z\_IS\_ENABLED3(one\_or\_two\_args 1, 0)

46

47/\* And our second argument is thus now cooked to be 1 in the case

48 \* where the value is defined to 1, and 0 if not:

49 \*/

50#define Z\_IS\_ENABLED3(ignore\_this, val, ...) val

51

52/\* Implementation of IS\_EQ(). Returns 1 if \_0 and \_1 are the same integer from

53 \* 0 to 4096, 0 otherwise.

54 \*/

55#define Z\_IS\_EQ(\_0, \_1) Z\_HAS\_COMMA(Z\_CAT4(Z\_IS\_, \_0, \_EQ\_, \_1)())

56

57/\* Used internally by COND\_CODE\_1 and COND\_CODE\_0. \*/

58#define Z\_COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code) \

59 \_\_COND\_CODE(\_XXXX##\_flag, \_if\_1\_code, \_else\_code)

60#define Z\_COND\_CODE\_0(\_flag, \_if\_0\_code, \_else\_code) \

61 \_\_COND\_CODE(\_ZZZZ##\_flag, \_if\_0\_code, \_else\_code)

62#define \_ZZZZ0 \_YYYY,

63#define \_\_COND\_CODE(one\_or\_two\_args, \_if\_code, \_else\_code) \

64 \_\_GET\_ARG2\_DEBRACKET(one\_or\_two\_args \_if\_code, \_else\_code)

65

66/\* Gets second argument and removes brackets around that argument. It

67 \* is expected that the parameter is provided in brackets/parentheses.

68 \*/

69#define \_\_GET\_ARG2\_DEBRACKET(ignore\_this, val, ...) \_\_DEBRACKET val

70

71/\* Used to remove brackets from around a single argument. \*/

72#define \_\_DEBRACKET(...) \_\_VA\_ARGS\_\_

73

74/\* Used by IS\_EMPTY() \*/

75/\* reference: https://gustedt.wordpress.com/2010/06/08/detect-empty-macro-arguments/ \*/

76#define Z\_HAS\_COMMA(...) \

77 NUM\_VA\_ARGS\_LESS\_1\_IMPL(\_\_VA\_ARGS\_\_, 1, 1, 1, 1, 1, 1, 1, 1, \

78 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \

79 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \

80 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0)

81#define Z\_TRIGGER\_PARENTHESIS\_(...) ,

82#define Z\_IS\_EMPTY\_(...) \

83 Z\_IS\_EMPTY\_\_( \

84 Z\_HAS\_COMMA(\_\_VA\_ARGS\_\_), \

85 Z\_HAS\_COMMA(Z\_TRIGGER\_PARENTHESIS\_ \_\_VA\_ARGS\_\_), \

86 Z\_HAS\_COMMA(\_\_VA\_ARGS\_\_ (/\*empty\*/)), \

87 Z\_HAS\_COMMA(Z\_TRIGGER\_PARENTHESIS\_ \_\_VA\_ARGS\_\_ (/\*empty\*/)))

88#define Z\_CAT4(\_0, \_1, \_2, \_3) \_0 ## \_1 ## \_2 ## \_3

89#define Z\_CAT5(\_0, \_1, \_2, \_3, \_4) \_0 ## \_1 ## \_2 ## \_3 ## \_4

90#define Z\_IS\_EMPTY\_\_(\_0, \_1, \_2, \_3) \

91 Z\_HAS\_COMMA(Z\_CAT5(Z\_IS\_EMPTY\_CASE\_, \_0, \_1, \_2, \_3))

92#define Z\_IS\_EMPTY\_CASE\_0001 ,

93

94/\* Used by LIST\_DROP\_EMPTY() \*/

95/\* Adding ',' after each element would add empty element at the end of

96 \* list, which is hard to remove, so instead precede each element with ',',

97 \* this way first element is empty, and this one is easy to drop.

98 \*/

99#define Z\_LIST\_ADD\_ELEM(e) EMPTY, e

100#define Z\_LIST\_DROP\_FIRST(...) GET\_ARGS\_LESS\_N(1, \_\_VA\_ARGS\_\_)

101#define Z\_LIST\_NO\_EMPTIES(e) \

102 COND\_CODE\_1(IS\_EMPTY(e), (), (Z\_LIST\_ADD\_ELEM(e)))

103

[ 104](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)#define UTIL\_CAT(a, ...) UTIL\_PRIMITIVE\_CAT(a, \_\_VA\_ARGS\_\_)

[ 105](util__internal_8h.md#a333f808696450134a9948dcc9e57e4ae)#define UTIL\_PRIMITIVE\_CAT(a, ...) a##\_\_VA\_ARGS\_\_

[ 106](util__internal_8h.md#a1f1ff51e3bda754ee9561bd6d17277a4)#define UTIL\_CHECK\_N(x, n, ...) n

[ 107](util__internal_8h.md#afc586c7e633155a0a3db1614d7c76a83)#define UTIL\_CHECK(...) UTIL\_CHECK\_N(\_\_VA\_ARGS\_\_, 0,)

[ 108](util__internal_8h.md#a5db295294795b2ecad29f585dda49c49)#define UTIL\_NOT(x) UTIL\_CHECK(UTIL\_PRIMITIVE\_CAT(UTIL\_NOT\_, x))

[ 109](util__internal_8h.md#aeb84e257f8e817fc7436d032d579853b)#define UTIL\_NOT\_0 ~, 1,

[ 110](util__internal_8h.md#ae667bfa8e06a6b3c15266db678934ef3)#define UTIL\_COMPL(b) UTIL\_PRIMITIVE\_CAT(UTIL\_COMPL\_, b)

[ 111](util__internal_8h.md#af8b84b2dc23d37616d59e8e19a5c94dd)#define UTIL\_COMPL\_0 1

[ 112](util__internal_8h.md#a69fb8790ad07ef2c00176a783c192390)#define UTIL\_COMPL\_1 0

[ 113](util__internal_8h.md#a80cbb3a182096676524d761113349bc8)#define UTIL\_BOOL(x) UTIL\_COMPL(UTIL\_NOT(x))

114

[ 115](util__internal_8h.md#a56279e773dc8d31b83161cc9526e8c56)#define UTIL\_EVAL(...) \_\_VA\_ARGS\_\_

[ 116](util__internal_8h.md#a4393cb8f894e8a32385a49fbfaf841b2)#define UTIL\_EXPAND(...) \_\_VA\_ARGS\_\_

[ 117](util__internal_8h.md#a3c54146013b856ef16ad45471b9fc7d1)#define UTIL\_REPEAT(...) UTIL\_LISTIFY(\_\_VA\_ARGS\_\_)

118

119#define \_CONCAT\_0(arg, ...) arg

120#define \_CONCAT\_1(arg, ...) UTIL\_CAT(arg, \_CONCAT\_0(\_\_VA\_ARGS\_\_))

121#define \_CONCAT\_2(arg, ...) UTIL\_CAT(arg, \_CONCAT\_1(\_\_VA\_ARGS\_\_))

122#define \_CONCAT\_3(arg, ...) UTIL\_CAT(arg, \_CONCAT\_2(\_\_VA\_ARGS\_\_))

123#define \_CONCAT\_4(arg, ...) UTIL\_CAT(arg, \_CONCAT\_3(\_\_VA\_ARGS\_\_))

124#define \_CONCAT\_5(arg, ...) UTIL\_CAT(arg, \_CONCAT\_4(\_\_VA\_ARGS\_\_))

125#define \_CONCAT\_6(arg, ...) UTIL\_CAT(arg, \_CONCAT\_5(\_\_VA\_ARGS\_\_))

126#define \_CONCAT\_7(arg, ...) UTIL\_CAT(arg, \_CONCAT\_6(\_\_VA\_ARGS\_\_))

127

128/\* Implementation details for NUM\_VA\_ARGS\_LESS\_1 \*/

[ 129](util__internal_8h.md#a70e3443886f63259dc12b14cc26c365f)#define NUM\_VA\_ARGS\_LESS\_1\_IMPL( \

130 \_ignored, \

131 \_0, \_1, \_2, \_3, \_4, \_5, \_6, \_7, \_8, \_9, \_10, \

132 \_11, \_12, \_13, \_14, \_15, \_16, \_17, \_18, \_19, \_20, \

133 \_21, \_22, \_23, \_24, \_25, \_26, \_27, \_28, \_29, \_30, \

134 \_31, \_32, \_33, \_34, \_35, \_36, \_37, \_38, \_39, \_40, \

135 \_41, \_42, \_43, \_44, \_45, \_46, \_47, \_48, \_49, \_50, \

136 \_51, \_52, \_53, \_54, \_55, \_56, \_57, \_58, \_59, \_60, \

137 \_61, \_62, N, ...) N

138

139/\* Used by MACRO\_MAP\_CAT \*/

[ 140](util__internal_8h.md#abe4f647ef2c1c706bc9d0d0e737e58bf)#define MACRO\_MAP\_CAT\_(...) \

141 /\* To make sure it works also for 2 arguments in total \*/ \

142 MACRO\_MAP\_CAT\_N(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), \_\_VA\_ARGS\_\_)

[ 143](util__internal_8h.md#a72d29784bb0a030942e2c6eb2f9d42b9)#define MACRO\_MAP\_CAT\_N\_(N, ...) UTIL\_CAT(MACRO\_MC\_, N)(\_\_VA\_ARGS\_\_,)

[ 144](util__internal_8h.md#a700a021819a2bc3bd4d9f18ebcc97579)#define MACRO\_MC\_0(...)

[ 145](util__internal_8h.md#aebb6edacecae322c4e5193e5dd50f072)#define MACRO\_MC\_1(m, a, ...) m(a)

[ 146](util__internal_8h.md#acac4b3ad7d94e0c3ebf483c056cdd9cb)#define MACRO\_MC\_2(m, a, ...) UTIL\_CAT(m(a), MACRO\_MC\_1(m, \_\_VA\_ARGS\_\_,))

[ 147](util__internal_8h.md#aebb08fb4302da40ca6964b9c4576862a)#define MACRO\_MC\_3(m, a, ...) UTIL\_CAT(m(a), MACRO\_MC\_2(m, \_\_VA\_ARGS\_\_,))

[ 148](util__internal_8h.md#ac5368a62577d74ca4e307a08bd081db4)#define MACRO\_MC\_4(m, a, ...) UTIL\_CAT(m(a), MACRO\_MC\_3(m, \_\_VA\_ARGS\_\_,))

[ 149](util__internal_8h.md#ab1fb261044e3ac3cd905aa2e57eb35c9)#define MACRO\_MC\_5(m, a, ...) UTIL\_CAT(m(a), MACRO\_MC\_4(m, \_\_VA\_ARGS\_\_,))

[ 150](util__internal_8h.md#a333330ed553dc76046eac9f5ee75a166)#define MACRO\_MC\_6(m, a, ...) UTIL\_CAT(m(a), MACRO\_MC\_5(m, \_\_VA\_ARGS\_\_,))

[ 151](util__internal_8h.md#a9f00d73d613e15afec0bd80b02f4d392)#define MACRO\_MC\_7(m, a, ...) UTIL\_CAT(m(a), MACRO\_MC\_6(m, \_\_VA\_ARGS\_\_,))

[ 152](util__internal_8h.md#aba43ed361199ce700b55cfca4c59132c)#define MACRO\_MC\_8(m, a, ...) UTIL\_CAT(m(a), MACRO\_MC\_7(m, \_\_VA\_ARGS\_\_,))

[ 153](util__internal_8h.md#a141c582a8152fb8bc3fdd9c963302528)#define MACRO\_MC\_9(m, a, ...) UTIL\_CAT(m(a), MACRO\_MC\_8(m, \_\_VA\_ARGS\_\_,))

[ 154](util__internal_8h.md#adcd5dc69004dbcf2e1a1a0f8b1e38e34)#define MACRO\_MC\_10(m, a, ...) UTIL\_CAT(m(a), MACRO\_MC\_9(m, \_\_VA\_ARGS\_\_,))

[ 155](util__internal_8h.md#aac114268287177238e8a43e9a631fea9)#define MACRO\_MC\_11(m, a, ...) UTIL\_CAT(m(a), MACRO\_MC\_10(m, \_\_VA\_ARGS\_\_,))

[ 156](util__internal_8h.md#abcf2741e7ce67d08eeaa7bfe24e54626)#define MACRO\_MC\_12(m, a, ...) UTIL\_CAT(m(a), MACRO\_MC\_11(m, \_\_VA\_ARGS\_\_,))

[ 157](util__internal_8h.md#a479b004b91499c3f580bc75fec26bbac)#define MACRO\_MC\_13(m, a, ...) UTIL\_CAT(m(a), MACRO\_MC\_12(m, \_\_VA\_ARGS\_\_,))

[ 158](util__internal_8h.md#af15fc993928b1bfd08778b73daee73cc)#define MACRO\_MC\_14(m, a, ...) UTIL\_CAT(m(a), MACRO\_MC\_13(m, \_\_VA\_ARGS\_\_,))

[ 159](util__internal_8h.md#a7e45901b614d203f7824cef9ae57b70e)#define MACRO\_MC\_15(m, a, ...) UTIL\_CAT(m(a), MACRO\_MC\_14(m, \_\_VA\_ARGS\_\_,))

160

161/\* Used by Z\_IS\_EQ \*/

162#include "[util\_internal\_is\_eq.h](util__internal__is__eq_8h.md)"

163

164/\*

165 \* Generic sparse list of odd numbers (check the implementation of

166 \* GPIO\_DT\_RESERVED\_RANGES\_NGPIOS as a usage example)

167 \*/

168#define Z\_SPARSE\_LIST\_ODD\_NUMBERS \

169 EMPTY, 1, EMPTY, 3, EMPTY, 5, EMPTY, 7, \

170 EMPTY, 9, EMPTY, 11, EMPTY, 13, EMPTY, 15, \

171 EMPTY, 17, EMPTY, 19, EMPTY, 21, EMPTY, 23, \

172 EMPTY, 25, EMPTY, 27, EMPTY, 29, EMPTY, 31, \

173 EMPTY, 33, EMPTY, 35, EMPTY, 37, EMPTY, 39, \

174 EMPTY, 41, EMPTY, 43, EMPTY, 45, EMPTY, 47, \

175 EMPTY, 49, EMPTY, 51, EMPTY, 53, EMPTY, 55, \

176 EMPTY, 57, EMPTY, 59, EMPTY, 61, EMPTY, 63

177

178/\*

179 \* Generic sparse list of even numbers (check the implementation of

180 \* GPIO\_DT\_RESERVED\_RANGES\_NGPIOS as a usage example)

181 \*/

182#define Z\_SPARSE\_LIST\_EVEN\_NUMBERS \

183 0, EMPTY, 2, EMPTY, 4, EMPTY, 6, EMPTY, \

184 8, EMPTY, 10, EMPTY, 12, EMPTY, 14, EMPTY, \

185 16, EMPTY, 18, EMPTY, 20, EMPTY, 22, EMPTY, \

186 24, EMPTY, 26, EMPTY, 28, EMPTY, 30, EMPTY, \

187 32, EMPTY, 34, EMPTY, 36, EMPTY, 38, EMPTY, \

188 40, EMPTY, 42, EMPTY, 44, EMPTY, 46, EMPTY, \

189 48, EMPTY, 50, EMPTY, 52, EMPTY, 54, EMPTY, \

190 56, EMPTY, 58, EMPTY, 60, EMPTY, 62, EMPTY

191

192/\* Used by UTIL\_INC \*/

193#include "[util\_internal\_util\_inc.h](util__internal__util__inc_8h.md)"

194

195/\* Used by UTIL\_DEC \*/

196#include "[util\_internal\_util\_dec.h](util__internal__util__dec_8h.md)"

197

198/\* Used by UTIL\_X2 \*/

199#include "[util\_internal\_util\_x2.h](util__internal__util__x2_8h.md)"

200

201#endif /\* ZEPHYR\_INCLUDE\_SYS\_UTIL\_INTERNAL\_H\_ \*/

[util\_internal\_is\_eq.h](util__internal__is__eq_8h.md)

[util\_internal\_util\_dec.h](util__internal__util__dec_8h.md)

[util\_internal\_util\_inc.h](util__internal__util__inc_8h.md)

[util\_internal\_util\_x2.h](util__internal__util__x2_8h.md)

[util\_loops.h](util__loops_8h.md)

Internals for looping macros.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [util\_internal.h](util__internal_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
