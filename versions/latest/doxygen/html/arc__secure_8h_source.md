---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arc__secure_8h_source.html
original_path: doxygen/html/arc__secure_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arc\_secure.h

[Go to the documentation of this file.](arc__secure_8h.md)

1/\*

2 \* Copyright (c) 2018 Synopsys, Inc. All rights reserved.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7

8#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_SJLI\_H

9#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_SJLI\_H

10

[ 11](arc__secure_8h.md#a6e757e1dc0c8149d3491df2ff038bdea)#define SJLI\_CALL\_ARC\_SECURE 0

12

[ 13](arc__secure_8h.md#a7d64353fd2cbf804771090d4310a15b5)#define ARC\_S\_CALL\_AUX\_READ 0

[ 14](arc__secure_8h.md#a1d4d7c124a5ec3508fb3a7729dd6178e)#define ARC\_S\_CALL\_AUX\_WRITE 1

[ 15](arc__secure_8h.md#afa6fae9a7ed92cc75dd71e70471898b4)#define ARC\_S\_CALL\_IRQ\_ALLOC 2

[ 16](arc__secure_8h.md#a28c873e308b53950680842fde7016be3)#define ARC\_S\_CALL\_CLRI 3

[ 17](arc__secure_8h.md#af0f3d548c3a14b8cf81da4e7c7276e8d)#define ARC\_S\_CALL\_SETI 4

[ 18](arc__secure_8h.md#a1c174d5e43e7da15eb77c7c2d6f9daf8)#define ARC\_S\_CALL\_LIMIT 5

19

20

21

[ 22](arc__secure_8h.md#a3edfd794bb6ea1db197006312d448402)#define ARC\_N\_IRQ\_START\_LEVEL ((CONFIG\_NUM\_IRQ\_PRIO\_LEVELS + 1) / 2)

23

24#ifndef \_ASMLANGUAGE

25

26#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

27#include <[stdbool.h](stdbool_8h.md)>

28

29#include <[zephyr/arch/arc/v2/aux\_regs.h](aux__regs_8h.md)>

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

35

[ 36](arc__secure_8h.md#a0c39c8bb33dd287c51cca9614b1f08fd)#define arc\_sjli(id) \

37 (\_\_asm\_\_ volatile("sjli %[sjli\_id]\n" :: [sjli\_id] "i" (id)))

38

39#ifdef CONFIG\_ARC\_SECURE\_FIRMWARE

40typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*\_arc\_s\_call\_handler\_t)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg1, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg2, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg3,

41 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg4, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg5, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg6);

42

43

44extern void arc\_go\_to\_normal([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr);

45extern void \_arc\_do\_secure\_call(void);

46extern const \_arc\_s\_call\_handler\_t arc\_s\_call\_table[[ARC\_S\_CALL\_LIMIT](arc__secure_8h.md#a1c174d5e43e7da15eb77c7c2d6f9daf8)];

47

48#endif

49

50

51#ifdef CONFIG\_ARC\_NORMAL\_FIRMWARE

52

53static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_arc\_s\_call\_invoke6([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg1, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg2, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg3,

54 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg4, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg5, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg6,

55 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) call\_id)

56{

57 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0") = arg1;

58 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r1 \_\_asm\_\_("r1") = arg2;

59 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r2 \_\_asm\_\_("r2") = arg3;

60 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r3 \_\_asm\_\_("r3") = arg4;

61 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r4 \_\_asm\_\_("r4") = arg5;

62 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r5 \_\_asm\_\_("r5") = arg6;

63 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

64

65 compiler\_barrier();

66

67 \_\_asm\_\_ volatile(

68 "sjli %[id]\n"

69 : "=r"(ret)

70 : [id] "i" ([SJLI\_CALL\_ARC\_SECURE](arc__secure_8h.md#a6e757e1dc0c8149d3491df2ff038bdea)),

71 "r" (ret), "r" (r1), "r" (r2), "r" (r3),

72 "r" (r4), "r" (r5), "r" (r6));

73

74 return ret;

75}

76

77static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_arc\_s\_call\_invoke5([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg1, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg2, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg3,

78 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg4, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg5, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) call\_id)

79{

80 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0") = arg1;

81 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r1 \_\_asm\_\_("r1") = arg2;

82 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r2 \_\_asm\_\_("r2") = arg3;

83 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r3 \_\_asm\_\_("r3") = arg4;

84 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r4 \_\_asm\_\_("r4") = arg5;

85 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

86

87 compiler\_barrier();

88

89 \_\_asm\_\_ volatile(

90 "sjli %[id]\n"

91 : "=r"(ret)

92 : [id] "i" ([SJLI\_CALL\_ARC\_SECURE](arc__secure_8h.md#a6e757e1dc0c8149d3491df2ff038bdea)),

93 "r" (ret), "r" (r1), "r" (r2), "r" (r3),

94 "r" (r4), "r" (r6));

95

96 return ret;

97}

98

99static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_arc\_s\_call\_invoke4([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg1, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg2, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg3,

100 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg4, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) call\_id)

101{

102 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0") = arg1;

103 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r1 \_\_asm\_\_("r1") = arg2;

104 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r2 \_\_asm\_\_("r2") = arg3;

105 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r3 \_\_asm\_\_("r3") = arg4;

106 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

107

108 compiler\_barrier();

109

110 \_\_asm\_\_ volatile(

111 "sjli %[id]\n"

112 : "=r"(ret)

113 : [id] "i" ([SJLI\_CALL\_ARC\_SECURE](arc__secure_8h.md#a6e757e1dc0c8149d3491df2ff038bdea)),

114 "r" (ret), "r" (r1), "r" (r2), "r" (r3),

115 "r" (r6));

116

117 return ret;

118}

119

120static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_arc\_s\_call\_invoke3([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg1, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg2, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg3,

121 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) call\_id)

122{

123 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0") = arg1;

124 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r1 \_\_asm\_\_("r1") = arg2;

125 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r2 \_\_asm\_\_("r2") = arg3;

126 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

127

128 compiler\_barrier();

129

130 \_\_asm\_\_ volatile(

131 "sjli %[id]\n"

132 : "=r"(ret)

133 : [id] "i" ([SJLI\_CALL\_ARC\_SECURE](arc__secure_8h.md#a6e757e1dc0c8149d3491df2ff038bdea)),

134 "r" (ret), "r" (r1), "r" (r2), "r" (r6));

135

136 return ret;

137}

138

139static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_arc\_s\_call\_invoke2([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg1, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg2, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) call\_id)

140{

141 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0") = arg1;

142 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r1 \_\_asm\_\_("r1") = arg2;

143 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

144

145 compiler\_barrier();

146

147 \_\_asm\_\_ volatile(

148 "sjli %[id]\n"

149 : "=r"(ret)

150 : [id] "i" ([SJLI\_CALL\_ARC\_SECURE](arc__secure_8h.md#a6e757e1dc0c8149d3491df2ff038bdea)),

151 "r" (ret), "r" (r1), "r" (r6));

152

153 return ret;

154}

155

156static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_arc\_s\_call\_invoke1([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg1, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) call\_id)

157{

158 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0") = arg1;

159 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

160

161 compiler\_barrier();

162

163 \_\_asm\_\_ volatile(

164 "sjli %[id]\n"

165 : "=r"(ret)

166 : [id] "i" ([SJLI\_CALL\_ARC\_SECURE](arc__secure_8h.md#a6e757e1dc0c8149d3491df2ff038bdea)),

167 "r" (ret), "r" (r6));

168

169 return ret;

170}

171

172static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_arc\_s\_call\_invoke0([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) call\_id)

173{

174 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0");

175 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

176

177 compiler\_barrier();

178

179 \_\_asm\_\_ volatile(

180 "sjli %[id]\n"

181 : "=r"(ret)

182 : [id] "i" ([SJLI\_CALL\_ARC\_SECURE](arc__secure_8h.md#a6e757e1dc0c8149d3491df2ff038bdea)),

183 "r" (ret), "r" (r6));

184

185 return ret;

186}

187

188static inline bool \_arch\_is\_user\_context(void)

189{

190 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) status;

191

192 compiler\_barrier();

193

194 \_\_asm\_\_ volatile("lr %0, [%[status32]]\n"

195 : "=r"(status)

196 : [status32] "i" (\_ARC\_V2\_STATUS32));

197

198 return !(status & \_ARC\_V2\_STATUS32\_US) ? true : [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727);

199}

200

201

202

203

204#endif /\* CONFIG\_ARC\_NORMAL\_FIRMWARE \*/

205

206#ifdef \_\_cplusplus

207}

208#endif

209

210#endif /\* \_ASMLANGUAGE \*/

211

212#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_SECURE\_H \*/

[ARC\_S\_CALL\_LIMIT](arc__secure_8h.md#a1c174d5e43e7da15eb77c7c2d6f9daf8)

#define ARC\_S\_CALL\_LIMIT

**Definition** arc\_secure.h:18

[SJLI\_CALL\_ARC\_SECURE](arc__secure_8h.md#a6e757e1dc0c8149d3491df2ff038bdea)

#define SJLI\_CALL\_ARC\_SECURE

**Definition** arc\_secure.h:11

[aux\_regs.h](aux__regs_8h.md)

ARCv2 auxiliary registers definitions.

[types.h](include_2zephyr_2types_8h.md)

[stdbool.h](stdbool_8h.md)

[false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727)

#define false

**Definition** stdbool.h:15

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [secureshield](dir_edc7d92000172b2927e4f8467a5c7046.md)
- [arc\_secure.h](arc__secure_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
