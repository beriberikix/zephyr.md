---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/xcc__missing__defs_8h_source.html
original_path: doxygen/html/xcc__missing__defs_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xcc\_missing\_defs.h

[Go to the documentation of this file.](xcc__missing__defs_8h.md)

1/\*

2 \* Copyright (c) 2019 BayLibre SAS

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7/\*

8 \* Basic macro definitions that gcc and clang provide on their own

9 \* but that xcc lacks. Only those that Zephyr requires are provided here.

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_XCC\_MISSING\_DEFS\_H\_

13#define ZEPHYR\_INCLUDE\_TOOLCHAIN\_XCC\_MISSING\_DEFS\_H\_

14

15#if \_\_CHAR\_BIT\_\_ == 8

16#define \_\_SCHAR\_WIDTH\_\_ 8

17#else

18#error "unexpected \_\_CHAR\_BIT\_\_ value"

19#endif

20

21#if \_\_SHRT\_MAX\_\_ == 32767

22#define \_\_SHRT\_WIDTH\_\_ 16

23#define \_\_SIZEOF\_SHORT\_\_ 2

24#else

25#error "unexpected \_\_SHRT\_WIDTH\_\_ value"

26#endif

27

28#if \_\_INT\_MAX\_\_ == 2147483647

29#define \_\_INT\_WIDTH\_\_ 32

30#define \_\_SIZEOF\_INT\_\_ 4

31#else

32#error "unexpected \_\_INT\_MAX\_\_ value"

33#endif

34

35#if \_\_LONG\_MAX\_\_ == 2147483647L

36#define \_\_LONG\_WIDTH\_\_ 32

37#define \_\_SIZEOF\_LONG\_\_ 4

38#else

39#error "unexpected \_\_LONG\_MAX\_\_ value"

40#endif

41

42#if \_\_LONG\_LONG\_MAX\_\_ == 9223372036854775807LL

43#define \_\_LONG\_LONG\_WIDTH\_\_ 64

44#define \_\_SIZEOF\_LONG\_LONG\_\_ 8

45#else

46#error "unexpected \_\_LONG\_LONG\_MAX\_\_ value"

47#endif

48

49#if \_\_INTMAX\_MAX\_\_ == 9223372036854775807LL

50#define \_\_INTMAX\_WIDTH\_\_ 64

51#define \_\_SIZEOF\_INTMAX\_\_ 8

52#define \_\_UINTMAX\_MAX\_\_ 0xffffffffffffffffULL

53#define \_\_UINTMAX\_WIDTH\_\_ 64

54#define \_\_SIZEOF\_UINTMAX\_\_ 8

55#else

56#error "unexpected \_\_INTMAX\_MAX\_\_ value"

57#endif

58

59/\*

60 \* No xcc provided definitions related to pointers, so let's just enforce

61 \* the Zephyr expected type.

62 \*/

63

64#define \_\_INTPTR\_MAX\_\_ 0x7fffffffL

65#define \_\_INTPTR\_TYPE\_\_ long int

66#define \_\_INTPTR\_WIDTH\_\_ 32

67#define \_\_SIZEOF\_POINTER\_\_ 4

68

69#define \_\_PTRDIFF\_MAX\_\_ 0x7fffffffL

70#define \_\_PTRDIFF\_WIDTH\_\_ 32

71#define \_\_SIZEOF\_PTRDIFF\_T\_\_ 4

72

73#define \_\_UINTPTR\_MAX\_\_ 0xffffffffLU

74#define \_\_UINTPTR\_TYPE\_\_ long unsigned int

75

76/\*

77 \* xcc already defines \_\_SIZE\_TYPE\_\_ as "unsigned int" but there is no way

78 \* to safeguard that here with preprocessor equality.

79 \*/

80

81#define \_\_SIZE\_MAX\_\_ 0xffffffffU

82#define \_\_SIZE\_WIDTH\_\_ 32

83#define \_\_SIZEOF\_SIZE\_T\_\_ 4

84

85/\*

86 \* The following defines are inferred from the xcc provided defines

87 \* already tested above.

88 \*/

89

90#define \_\_INT8\_MAX\_\_ 0x7f

91#define \_\_INT8\_TYPE\_\_ signed char

92

93#define \_\_INT16\_MAX\_\_ 0x7fff

94#define \_\_INT16\_TYPE\_\_ short int

95

96#define \_\_INT32\_MAX\_\_ 0x7fffffff

97#define \_\_INT32\_TYPE\_\_ int

98

99#define \_\_INT64\_MAX\_\_ 0x7fffffffffffffffLL

100#define \_\_INT64\_TYPE\_\_ long long int

101

102#define \_\_INT\_FAST8\_MAX\_\_ 0x7f

103#define \_\_INT\_FAST8\_TYPE\_\_ signed char

104#define \_\_INT\_FAST8\_WIDTH\_\_ 8

105

106#define \_\_INT\_FAST16\_MAX\_\_ 0x7fffffff

107#define \_\_INT\_FAST16\_TYPE\_\_ int

108#define \_\_INT\_FAST16\_WIDTH\_\_ 32

109

110#define \_\_INT\_FAST32\_MAX\_\_ 0x7fffffff

111#define \_\_INT\_FAST32\_TYPE\_\_ int

112#define \_\_INT\_FAST32\_WIDTH\_\_ 32

113

114#define \_\_INT\_FAST64\_MAX\_\_ 0x7fffffffffffffffLL

115#define \_\_INT\_FAST64\_TYPE\_\_ long long int

116#define \_\_INT\_FAST64\_WIDTH\_\_ 64

117

118#define \_\_INT\_LEAST8\_MAX\_\_ 0x7f

119#define \_\_INT\_LEAST8\_TYPE\_\_ signed char

120#define \_\_INT\_LEAST8\_WIDTH\_\_ 8

121

122#define \_\_INT\_LEAST16\_MAX\_\_ 0x7fff

123#define \_\_INT\_LEAST16\_TYPE\_\_ short int

124#define \_\_INT\_LEAST16\_WIDTH\_\_ 16

125

126#define \_\_INT\_LEAST32\_MAX\_\_ 0x7fffffff

127#define \_\_INT\_LEAST32\_TYPE\_\_ int

128#define \_\_INT\_LEAST32\_WIDTH\_\_ 32

129

130#define \_\_INT\_LEAST64\_MAX\_\_ 0x7fffffffffffffffLL

131#define \_\_INT\_LEAST64\_TYPE\_\_ long long int

132#define \_\_INT\_LEAST64\_WIDTH\_\_ 64

133

134#define \_\_UINT8\_MAX\_\_ 0xffU

135#define \_\_UINT8\_TYPE\_\_ unsigned char

136

137#define \_\_UINT16\_MAX\_\_ 0xffffU

138#define \_\_UINT16\_TYPE\_\_ short unsigned int

139

140#define \_\_UINT32\_MAX\_\_ 0xffffffffU

141#define \_\_UINT32\_TYPE\_\_ unsigned int

142

143#define \_\_UINT64\_MAX\_\_ 0xffffffffffffffffULL

144#define \_\_UINT64\_TYPE\_\_ long long unsigned int

145

146#define \_\_UINT\_FAST8\_MAX\_\_ 0xffU

147#define \_\_UINT\_FAST8\_TYPE\_\_ unsigned char

148

149#define \_\_UINT\_FAST16\_MAX\_\_ 0xffffffffU

150#define \_\_UINT\_FAST16\_TYPE\_\_ unsigned int

151

152#define \_\_UINT\_FAST32\_MAX\_\_ 0xffffffffU

153#define \_\_UINT\_FAST32\_TYPE\_\_ unsigned int

154

155#define \_\_UINT\_FAST64\_MAX\_\_ 0xffffffffffffffffULL

156#define \_\_UINT\_FAST64\_TYPE\_\_ long long unsigned int

157

158#define \_\_UINT\_LEAST8\_MAX\_\_ 0xffU

159#define \_\_UINT\_LEAST8\_TYPE\_\_ unsigned char

160

161#define \_\_UINT\_LEAST16\_MAX\_\_ 0xffffU

162#define \_\_UINT\_LEAST16\_TYPE\_\_ short unsigned int

163

164#define \_\_UINT\_LEAST32\_MAX\_\_ 0xffffffffU

165#define \_\_UINT\_LEAST32\_TYPE\_\_ unsigned int

166

167#define \_\_UINT\_LEAST64\_MAX\_\_ 0xffffffffffffffffULL

168#define \_\_UINT\_LEAST64\_TYPE\_\_ long long unsigned int

169

170#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [xcc\_missing\_defs.h](xcc__missing__defs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
