---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/iar__missing__defs_8h_source.html
original_path: doxygen/html/iar__missing__defs_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

iar\_missing\_defs.h

[Go to the documentation of this file.](iar__missing__defs_8h.md)

1/\*

2 \* Copyright (c) 2025 IAR Systems AB

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7/\*

8 \* Basic macro definitions that gcc and clang provide on their own

9 \* but that iccarm lacks. Only those that Zephyr requires are provided here.

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_ICCARM\_MISSING\_DEFS\_H\_

13#define ZEPHYR\_INCLUDE\_TOOLCHAIN\_ICCARM\_MISSING\_DEFS\_H\_

14

15 /\* We need to define NULL with a parenthesis around \_NULL

16 \* otherwise the DEBRACE macros won't work correctly

17 \*/

18

19#undef NULL

[ 20](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)#define NULL (\_NULL)

21

22#if defined(\_\_IAR\_SYSTEMS\_ICC\_\_)

23#ifndef \_\_CHAR\_BIT\_\_

24#define \_\_CHAR\_BIT\_\_ \_\_CHAR\_BITS\_\_

25#endif

26#define \_\_SCHAR\_MAX\_\_ \_\_SIGNED\_CHAR\_MAX\_\_

27

28#define \_\_INT\_MAX\_\_ \_\_SIGNED\_INT\_MAX\_\_

29#define \_\_INT\_WIDTH\_\_ (\_\_INT\_SIZE\_\_\*8)

30#define \_\_SIZEOF\_INT\_\_ \_\_INT\_SIZE\_\_

31

32#define \_\_SHRT\_MAX\_\_ \_\_SIGNED\_SHORT\_MAX\_\_

33#define \_\_SHRT\_WIDTH\_\_ (\_\_SHORT\_SIZE\_\_\*8)

34#define \_\_SIZEOF\_SHORT\_\_ \_\_SHORT\_SIZE\_\_

35

36#define \_\_LONG\_MAX\_\_ \_\_SIGNED\_LONG\_MAX\_\_

37#define \_\_LONG\_WIDTH\_\_ (\_\_LONG\_SIZE\_\_\*8)

38#define \_\_SIZEOF\_LONG\_\_ \_\_LONG\_SIZE\_\_

39

40#define \_\_LONG\_LONG\_MAX\_\_ \_\_SIGNED\_LONG\_LONG\_MAX\_\_

41#define \_\_LONG\_LONG\_WIDTH\_\_ (\_\_LONG\_LONG\_SIZE\_\_\*8)

42#define \_\_SIZEOF\_LONG\_LONG\_\_ \_\_LONG\_LONG\_SIZE\_\_

43

44#define \_\_INTMAX\_MAX\_\_ \_\_INTMAX\_T\_MAX\_\_

45#define \_\_SIZEOF\_INTMAX\_\_ sizeof(\_\_INTMAX\_T\_TYPE\_\_)

46#define \_\_INTMAX\_WIDTH\_\_ (\_\_SIZEOF\_INTMAX\_\_\*8)

47#define \_\_UINTMAX\_MAX\_\_ \_\_UINTMAX\_T\_MAX\_\_

48#define \_\_SIZEOF\_UINTMAX\_\_ sizeof(\_\_UINTMAX\_T\_TYPE\_\_)

49#define \_\_UINTMAX\_WIDTH\_\_ (\_\_SIZEOF\_UINTMAX\_\_\*8)

50

51#define \_\_INTPTR\_MAX\_\_ \_\_INTPTR\_T\_MAX\_\_

52#define \_\_INTPTR\_TYPE\_\_ \_\_INTPTR\_T\_TYPE\_\_

53#define \_\_INTPTR\_WIDTH\_\_ (\_\_INTPTR\_T\_SIZE\_\_\*8)

54#define \_\_SIZEOF\_POINTER\_\_ \_\_INTPTR\_T\_SIZE\_\_

55

56#define \_\_PTRDIFF\_MAX\_\_ \_\_PTRDIFF\_T\_MAX\_\_

57#define \_\_PTRDIFF\_WIDTH\_\_ (\_\_PTRDIFF\_T\_SIZE\_\_\*8)

58#define \_\_SIZEOF\_PTRDIFF\_T\_\_ \_\_PTRDIFF\_T\_SIZE\_\_

59

60#define \_\_UINTPTR\_MAX\_\_ \_\_UINTPTR\_T\_MAX\_\_

61#define \_\_UINTPTR\_TYPE\_\_ \_\_UINTPTR\_T\_TYPE\_\_

62

63/\*

64 \* ICCARM already defines \_\_SIZE\_T\_MAX\_\_ as "unsigned int" but there is no way

65 \* to safeguard that here with preprocessor equality.

66 \*/

67

68#define \_\_SIZE\_TYPE\_\_ \_\_SIZE\_T\_TYPE\_\_

69#define \_\_SIZE\_MAX\_\_ \_\_SIZE\_T\_MAX\_\_

70#define \_\_SIZE\_WIDTH\_\_ ((\_\_SIZEOF\_SIZE\_T\_\_)\*8)

71/\* #define \_\_SIZEOF\_SIZE\_T\_\_ 4 \*/

72

73/\*

74 \* The following defines are inferred from the ICCARM provided defines

75 \* already tested above.

76 \*/

77

78

79#define \_\_INT8\_MAX\_\_ \_\_INT8\_T\_MAX\_\_

80#define \_\_INT8\_TYPE\_\_ \_\_INT8\_T\_TYPE\_\_

81

82#define \_\_UINT8\_MAX\_\_ \_\_UINT8\_T\_MAX\_\_

83#define \_\_UINT8\_TYPE\_\_ \_\_UINT8\_T\_TYPE\_\_

84

85#define \_\_INT16\_MAX\_\_ \_\_INT16\_T\_MAX\_\_

86#define \_\_INT16\_TYPE\_\_ \_\_INT16\_T\_TYPE\_\_

87

88#define \_\_UINT16\_MAX\_\_ \_\_UINT16\_T\_MAX\_\_

89#define \_\_UINT16\_TYPE\_\_ \_\_UINT16\_T\_TYPE\_\_

90

91#define \_\_INT32\_MAX\_\_ \_\_INT32\_T\_MAX\_\_

92#define \_\_INT32\_TYPE\_\_ \_\_INT32\_T\_TYPE\_\_

93

94#define \_\_UINT32\_MAX\_\_ \_\_UINT32\_T\_MAX\_\_

95#define \_\_UINT32\_TYPE\_\_ \_\_UINT32\_T\_TYPE\_\_

96

97#define \_\_INT64\_MAX\_\_ \_\_INT64\_T\_MAX\_\_

98#define \_\_INT64\_TYPE\_\_ \_\_INT64\_T\_TYPE\_\_

99

100#define \_\_UINT64\_MAX\_\_ \_\_UINT64\_T\_MAX\_\_

101#define \_\_UINT64\_TYPE\_\_ \_\_UINT64\_T\_TYPE\_\_

102

103#define \_\_INT\_FAST8\_MAX\_\_ \_\_INT\_FAST8\_T\_MAX\_\_

104#define \_\_INT\_FAST8\_TYPE\_\_ \_\_INT\_FAST8\_T\_TYPE\_\_

105#define \_\_INT\_FAST8\_WIDTH\_\_ (\_\_INT\_FAST8\_T\_SIZE\_\_\*8)

106

107#define \_\_INT\_FAST16\_MAX\_\_ \_\_INT\_FAST16\_T\_MAX\_\_

108#define \_\_INT\_FAST16\_TYPE\_\_ \_\_INT\_FAST16\_T\_TYPE\_\_

109#define \_\_INT\_FAST16\_WIDTH\_\_ (\_\_INT\_FAST16\_T\_SIZE\_\_\*8)

110

111#define \_\_INT\_FAST32\_MAX\_\_ \_\_INT\_FAST32\_T\_MAX\_\_

112#define \_\_INT\_FAST32\_TYPE\_\_ \_\_INT\_FAST32\_T\_TYPE\_\_

113#define \_\_INT\_FAST32\_WIDTH\_\_ (\_\_INT\_FAST32\_T\_SIZE\_\_\*8)

114

115#define \_\_INT\_FAST64\_MAX\_\_ \_\_INT\_FAST64\_T\_MAX\_\_

116#define \_\_INT\_FAST64\_TYPE\_\_ \_\_INT\_FAST64\_T\_TYPE\_\_

117#define \_\_INT\_FAST64\_WIDTH\_\_ (\_\_INT\_FAST64\_T\_SIZE\_\_\*8)

118

119#define \_\_INT\_LEAST8\_MAX\_\_ \_\_INT\_LEAST8\_T\_MAX\_\_

120#define \_\_INT\_LEAST8\_TYPE\_\_ \_\_INT\_LEAST8\_T\_TYPE\_\_

121#define \_\_INT\_LEAST8\_WIDTH\_\_ (\_\_INT\_LEAST8\_T\_SIZE\_\_\*8)

122

123#define \_\_INT\_LEAST16\_MAX\_\_ \_\_INT\_LEAST16\_T\_MAX\_\_

124#define \_\_INT\_LEAST16\_TYPE\_\_ \_\_INT\_LEAST16\_T\_TYPE\_\_

125#define \_\_INT\_LEAST16\_WIDTH\_\_ (\_\_INT\_LEAST16\_T\_SIZE\_\_\*8)

126

127#define \_\_INT\_LEAST32\_MAX\_\_ \_\_INT\_LEAST32\_T\_MAX\_\_

128#define \_\_INT\_LEAST32\_TYPE\_\_ \_\_INT\_LEAST32\_T\_TYPE\_\_

129#define \_\_INT\_LEAST32\_WIDTH\_\_ (\_\_INT\_LEAST32\_T\_SIZE\_\_\*8)

130

131#define \_\_INT\_LEAST64\_MAX\_\_ \_\_INT\_LEAST64\_T\_MAX\_\_

132#define \_\_INT\_LEAST64\_TYPE\_\_ \_\_INT\_LEAST64\_T\_TYPE\_\_

133#define \_\_INT\_LEAST64\_WIDTH\_\_ (\_\_INT\_LEAST64\_T\_SIZE\_\_\*8)

134

135#define \_\_UINT\_FAST8\_MAX\_\_ \_\_UINT\_FAST8\_T\_MAX\_\_

136#define \_\_UINT\_FAST8\_TYPE\_\_ \_\_UINT\_FAST8\_T\_TYPE\_\_

137

138#define \_\_UINT\_FAST16\_MAX\_\_ \_\_UINT\_FAST16\_T\_MAX\_\_

139#define \_\_UINT\_FAST16\_TYPE\_\_ \_\_UINT\_FAST16\_T\_TYPE\_\_

140

141#define \_\_UINT\_FAST32\_MAX\_\_ \_\_UINT\_FAST32\_T\_MAX\_\_

142#define \_\_UINT\_FAST32\_TYPE\_\_ \_\_UINT\_FAST32\_T\_TYPE\_\_

143

144#define \_\_UINT\_FAST64\_MAX\_\_ \_\_UINT\_FAST64\_T\_MAX\_\_

145#define \_\_UINT\_FAST64\_TYPE\_\_ \_\_UINT\_FAST64\_T\_TYPE\_\_

146

147#define \_\_UINT\_LEAST8\_MAX\_\_ \_\_UINT\_LEAST8\_T\_MAX\_\_

148#define \_\_UINT\_LEAST8\_TYPE\_\_ \_\_UINT\_LEAST8\_T\_TYPE\_\_

149

150#define \_\_UINT\_LEAST16\_MAX\_\_ \_\_UINT\_LEAST16\_T\_MAX\_\_

151#define \_\_UINT\_LEAST16\_TYPE\_\_ \_\_UINT\_LEAST16\_T\_TYPE\_\_

152

153#define \_\_UINT\_LEAST32\_MAX\_\_ \_\_UINT\_LEAST32\_T\_MAX\_\_

154#define \_\_UINT\_LEAST32\_TYPE\_\_ \_\_UINT\_LEAST32\_T\_TYPE\_\_

155

156#define \_\_UINT\_LEAST64\_MAX\_\_ \_\_UINT\_LEAST64\_T\_MAX\_\_

157#define \_\_UINT\_LEAST64\_TYPE\_\_ \_\_UINT\_LEAST64\_T\_TYPE\_\_

158

159#endif /\* \_\_IAR\_SYSTEMS\_ICC\_\_ \*/

160

161#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [iar](dir_cb961a4998504dcfcaac26ca40155226.md)
- [iar\_missing\_defs.h](iar__missing__defs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
