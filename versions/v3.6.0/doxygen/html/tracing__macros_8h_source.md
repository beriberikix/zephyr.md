---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/tracing__macros_8h_source.html
original_path: doxygen/html/tracing__macros_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tracing\_macros.h

[Go to the documentation of this file.](tracing__macros_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_TRACING\_TRACING\_MACROS\_H\_

7#define ZEPHYR\_INCLUDE\_TRACING\_TRACING\_MACROS\_H\_

8

9#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

10

11#if !defined(CONFIG\_TRACING) && !defined(\_\_DOXYGEN\_\_)

12

13#define SYS\_PORT\_TRACING\_FUNC(type, func, ...) do { } while (false)

14#define SYS\_PORT\_TRACING\_FUNC\_ENTER(type, func, ...) do { } while (false)

15#define SYS\_PORT\_TRACING\_FUNC\_BLOCKING(type, func, ...) do { } while (false)

16#define SYS\_PORT\_TRACING\_FUNC\_EXIT(type, func, ...) do { } while (false)

17#define SYS\_PORT\_TRACING\_OBJ\_INIT(obj\_type, obj, ...) do { } while (false)

18#define SYS\_PORT\_TRACING\_OBJ\_FUNC(obj\_type, func, obj, ...) do { } while (false)

19#define SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(obj\_type, func, obj, ...) do { } while (false)

20#define SYS\_PORT\_TRACING\_OBJ\_FUNC\_BLOCKING(obj\_type, func, obj, ...) do { } while (false)

21#define SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(obj\_type, func, obj, ...) do { } while (false)

22

23#define SYS\_PORT\_TRACING\_TRACKING\_FIELD(type)

24

25#else

26

33

35

36/\*

37 \* Helper macros used by the extended tracing system

38 \*/

39

40#define \_SYS\_PORT\_TRACING\_TYPE\_MASK(type) \

41 sys\_port\_trace\_type\_mask\_ ## type

42#define \_SYS\_PORT\_TRACING\_FUNC(name, func) \

43 sys\_port\_trace\_ ## name ## \_ ## func

44#define \_SYS\_PORT\_TRACING\_FUNC\_ENTER(name, func) \

45 sys\_port\_trace\_ ## name ## \_ ## func ## \_enter

46#define \_SYS\_PORT\_TRACING\_FUNC\_BLOCKING(name, func) \

47 sys\_port\_trace\_ ## name ## \_ ## func ## \_blocking

48#define \_SYS\_PORT\_TRACING\_FUNC\_EXIT(name, func) \

49 sys\_port\_trace\_ ## name ## \_ ## func ## \_exit

50#define \_SYS\_PORT\_TRACING\_OBJ\_INIT(name) \

51 sys\_port\_trace\_ ## name ## \_init

52#define \_SYS\_PORT\_TRACING\_OBJ\_FUNC(name, func) \

53 sys\_port\_trace\_ ## name ## \_ ## func

54#define \_SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(name, func) \

55 sys\_port\_trace\_ ## name ## \_ ## func ## \_enter

56#define \_SYS\_PORT\_TRACING\_OBJ\_FUNC\_BLOCKING(name, func) \

57 sys\_port\_trace\_ ## name ## \_ ## func ## \_blocking

58#define \_SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(name, func) \

59 sys\_port\_trace\_ ## name ## \_ ## func ## \_exit

60

61/\*

62 \* Helper macros for the object tracking system

63 \*/

64

65#define \_SYS\_PORT\_TRACKING\_OBJ\_INIT(name) \

66 sys\_port\_track\_ ## name ## \_init

67#define \_SYS\_PORT\_TRACKING\_OBJ\_FUNC(name, func) \

68 sys\_port\_track\_ ## name ## \_ ## func

69

70/\*

71 \* Object trace macros part of the system for checking if certain

72 \* objects should be traced or not depending on the tracing configuration.

73 \*/

74#if defined(CONFIG\_TRACING\_THREAD)

75 #define sys\_port\_trace\_type\_mask\_k\_thread(trace\_call) trace\_call

76#else

77 #define sys\_port\_trace\_type\_mask\_k\_thread(trace\_call)

78 #define sys\_port\_trace\_k\_thread\_is\_disabled 1

79#endif

80

81#if defined(CONFIG\_TRACING\_WORK)

82 #define sys\_port\_trace\_type\_mask\_k\_work(trace\_call) trace\_call

83 #define sys\_port\_trace\_type\_mask\_k\_work\_queue(trace\_call) trace\_call

84 #define sys\_port\_trace\_type\_mask\_k\_work\_delayable(trace\_call) trace\_call

85 #define sys\_port\_trace\_type\_mask\_k\_work\_poll(trace\_call) trace\_call

86#else

87 #define sys\_port\_trace\_type\_mask\_k\_work(trace\_call)

88 #define sys\_port\_trace\_type\_mask\_k\_work\_queue(trace\_call)

89 #define sys\_port\_trace\_type\_mask\_k\_work\_delayable(trace\_call)

90 #define sys\_port\_trace\_type\_mask\_k\_work\_poll(trace\_call)

91#endif

92

93#if defined(CONFIG\_TRACING\_SEMAPHORE)

94 #define sys\_port\_trace\_type\_mask\_k\_sem(trace\_call) trace\_call

95#else

96 #define sys\_port\_trace\_type\_mask\_k\_sem(trace\_call)

97#endif

98

99#if defined(CONFIG\_TRACING\_MUTEX)

100 #define sys\_port\_trace\_type\_mask\_k\_mutex(trace\_call) trace\_call

101#else

102 #define sys\_port\_trace\_type\_mask\_k\_mutex(trace\_call)

103#endif

104

105#if defined(CONFIG\_TRACING\_CONDVAR)

106 #define sys\_port\_trace\_type\_mask\_k\_condvar(trace\_call) trace\_call

107#else

108 #define sys\_port\_trace\_type\_mask\_k\_condvar(trace\_call)

109#endif

110

111#if defined(CONFIG\_TRACING\_QUEUE)

112 #define sys\_port\_trace\_type\_mask\_k\_queue(trace\_call) trace\_call

113#else

114 #define sys\_port\_trace\_type\_mask\_k\_queue(trace\_call)

115#endif

116

117#if defined(CONFIG\_TRACING\_FIFO)

118 #define sys\_port\_trace\_type\_mask\_k\_fifo(trace\_call) trace\_call

119#else

120 #define sys\_port\_trace\_type\_mask\_k\_fifo(trace\_call)

121#endif

122

123#if defined(CONFIG\_TRACING\_LIFO)

124 #define sys\_port\_trace\_type\_mask\_k\_lifo(trace\_call) trace\_call

125#else

126 #define sys\_port\_trace\_type\_mask\_k\_lifo(trace\_call)

127#endif

128

129#if defined(CONFIG\_TRACING\_STACK)

130 #define sys\_port\_trace\_type\_mask\_k\_stack(trace\_call) trace\_call

131#else

132 #define sys\_port\_trace\_type\_mask\_k\_stack(trace\_call)

133#endif

134

135#if defined(CONFIG\_TRACING\_MESSAGE\_QUEUE)

136 #define sys\_port\_trace\_type\_mask\_k\_msgq(trace\_call) trace\_call

137#else

138 #define sys\_port\_trace\_type\_mask\_k\_msgq(trace\_call)

139#endif

140

141#if defined(CONFIG\_TRACING\_MAILBOX)

142 #define sys\_port\_trace\_type\_mask\_k\_mbox(trace\_call) trace\_call

143#else

144 #define sys\_port\_trace\_type\_mask\_k\_mbox(trace\_call)

145#endif

146

147#if defined(CONFIG\_TRACING\_PIPE)

148 #define sys\_port\_trace\_type\_mask\_k\_pipe(trace\_call) trace\_call

149#else

150 #define sys\_port\_trace\_type\_mask\_k\_pipe(trace\_call)

151#endif

152

153#if defined(CONFIG\_TRACING\_HEAP)

154 #define sys\_port\_trace\_type\_mask\_k\_heap(trace\_call) trace\_call

155 #define sys\_port\_trace\_type\_mask\_k\_heap\_sys(trace\_call) trace\_call

156#else

157 #define sys\_port\_trace\_type\_mask\_k\_heap(trace\_call)

158 #define sys\_port\_trace\_type\_mask\_k\_heap\_sys(trace\_call)

159#endif

160

161#if defined(CONFIG\_TRACING\_MEMORY\_SLAB)

162 #define sys\_port\_trace\_type\_mask\_k\_mem\_slab(trace\_call) trace\_call

163#else

164 #define sys\_port\_trace\_type\_mask\_k\_mem\_slab(trace\_call)

165#endif

166

167#if defined(CONFIG\_TRACING\_TIMER)

168 #define sys\_port\_trace\_type\_mask\_k\_timer(trace\_call) trace\_call

169#else

170 #define sys\_port\_trace\_type\_mask\_k\_timer(trace\_call)

171#endif

172

173#if defined(CONFIG\_TRACING\_EVENT)

174 #define sys\_port\_trace\_type\_mask\_k\_event(trace\_call) trace\_call

175#else

176 #define sys\_port\_trace\_type\_mask\_k\_event(trace\_call)

177#endif

178

179#ifndef CONFIG\_TRACING\_POLLING

180 #define sys\_port\_trace\_k\_poll\_api\_is\_disabled 1

181 #define sys\_port\_trace\_k\_work\_poll\_is\_disabled 1

182#endif

183

184#ifndef CONFIG\_TRACING\_PM

185 #define sys\_port\_trace\_pm\_is\_disabled 1

186#endif

187

188/\*

189 \* We cannot positively enumerate all traced APIs, as applications may trace

190 \* arbitrary custom APIs we know nothing about. Therefore we demand that tracing

191 \* of an API must be actively disabled.

192 \*

193 \* This contrasts with object tracing/tracking as all traceable objects are well

194 \* known, see the SYS\_PORT\_TRACING\_TYPE\_MASK approach below.

195 \*/

196#define \_SYS\_PORT\_TRACE\_IS\_DISABLED(type) sys\_port\_trace\_##type##\_is\_disabled

197#define \_SYS\_PORT\_TRACE\_WRAP(func, ...) do { func(\_\_VA\_ARGS\_\_); } while (false)

198#define \_SYS\_PORT\_TRACE\_IF\_NOT\_DISABLED(type, func, ...) \

199 COND\_CODE\_1(\_SYS\_PORT\_TRACE\_IS\_DISABLED(type), (), \

200 (\_SYS\_PORT\_TRACE\_WRAP(func, \_\_VA\_ARGS\_\_)))

201

203

[ 210](group__subsys__tracing__macros.md#ga7c3ff6c93f71cdd1a35e3a656885fb50)#define SYS\_PORT\_TRACING\_TYPE\_MASK(type, trace\_call) \

211 \_SYS\_PORT\_TRACING\_TYPE\_MASK(type)(trace\_call)

212

[ 223](group__subsys__tracing__macros.md#gadce691eea44f211b804ce44b51b2e71d)#define SYS\_PORT\_TRACING\_FUNC(type, func, ...) \

224 \_SYS\_PORT\_TRACE\_IF\_NOT\_DISABLED(type, \_SYS\_PORT\_TRACING\_FUNC(type, func), \_\_VA\_ARGS\_\_)

225

[ 236](group__subsys__tracing__macros.md#ga445bcac4cec53d560ddca757de17e1e3)#define SYS\_PORT\_TRACING\_FUNC\_ENTER(type, func, ...) \

237 \_SYS\_PORT\_TRACE\_IF\_NOT\_DISABLED(type, \_SYS\_PORT\_TRACING\_FUNC\_ENTER(type, func), \_\_VA\_ARGS\_\_)

238

[ 248](group__subsys__tracing__macros.md#ga17c6029a89e3e1539dbac019dc9ee50b)#define SYS\_PORT\_TRACING\_FUNC\_BLOCKING(type, func, ...) \

249 \_SYS\_PORT\_TRACE\_IF\_NOT\_DISABLED(type, \_SYS\_PORT\_TRACING\_FUNC\_BLOCKING(type, func), \

250 \_\_VA\_ARGS\_\_)

251

[ 262](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)#define SYS\_PORT\_TRACING\_FUNC\_EXIT(type, func, ...) \

263 \_SYS\_PORT\_TRACE\_IF\_NOT\_DISABLED(type, \_SYS\_PORT\_TRACING\_FUNC\_EXIT(type, func), \_\_VA\_ARGS\_\_)

264

[ 271](group__subsys__tracing__macros.md#ga19606657deb4b8902314fe11eb8bfb24)#define SYS\_PORT\_TRACING\_OBJ\_INIT(obj\_type, obj, ...) \

272 do { \

273 SYS\_PORT\_TRACING\_TYPE\_MASK(obj\_type, \

274 \_SYS\_PORT\_TRACING\_OBJ\_INIT(obj\_type)(obj, ##\_\_VA\_ARGS\_\_)); \

275 SYS\_PORT\_TRACING\_TYPE\_MASK(obj\_type, \

276 \_SYS\_PORT\_TRACKING\_OBJ\_INIT(obj\_type)(obj, ##\_\_VA\_ARGS\_\_)); \

277 } while (false)

278

[ 289](group__subsys__tracing__macros.md#gaca007b62a20872de436533f26e5b1c55)#define SYS\_PORT\_TRACING\_OBJ\_FUNC(obj\_type, func, obj, ...) \

290 do { \

291 SYS\_PORT\_TRACING\_TYPE\_MASK(obj\_type, \

292 \_SYS\_PORT\_TRACING\_OBJ\_FUNC(obj\_type, func)(obj, ##\_\_VA\_ARGS\_\_)); \

293 SYS\_PORT\_TRACING\_TYPE\_MASK(obj\_type, \

294 \_SYS\_PORT\_TRACKING\_OBJ\_FUNC(obj\_type, func)(obj, ##\_\_VA\_ARGS\_\_)); \

295 } while (false)

296

[ 308](group__subsys__tracing__macros.md#ga4ce3846263099a197c043f25ebe4a253)#define SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(obj\_type, func, obj, ...) \

309 do { \

310 SYS\_PORT\_TRACING\_TYPE\_MASK(obj\_type, \

311 \_SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(obj\_type, func)(obj, ##\_\_VA\_ARGS\_\_)); \

312 } while (false)

313

[ 325](group__subsys__tracing__macros.md#ga8e98afd586a77d158acb103b94d9cd3f)#define SYS\_PORT\_TRACING\_OBJ\_FUNC\_BLOCKING(obj\_type, func, obj, timeout, ...) \

326 do { \

327 SYS\_PORT\_TRACING\_TYPE\_MASK(obj\_type, \

328 \_SYS\_PORT\_TRACING\_OBJ\_FUNC\_BLOCKING(obj\_type, func) \

329 (obj, timeout, ##\_\_VA\_ARGS\_\_)); \

330 } while (false)

331

[ 343](group__subsys__tracing__macros.md#ga94bd54c03c68d60e1c0879ce43e08730)#define SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(obj\_type, func, obj, ...) \

344 do { \

345 SYS\_PORT\_TRACING\_TYPE\_MASK(obj\_type, \

346 \_SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(obj\_type, func)(obj, ##\_\_VA\_ARGS\_\_)); \

347 } while (false)

348

[ 354](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)#define SYS\_PORT\_TRACING\_TRACKING\_FIELD(type) \

355 SYS\_PORT\_TRACING\_TYPE\_MASK(type, struct type \*\_obj\_track\_next;)

356 /\* end of subsys\_tracing\_macros \*/

358

359#endif /\* CONFIG\_TRACING \*/

360

361#endif /\* ZEPHYR\_INCLUDE\_TRACING\_TRACING\_MACROS\_H\_ \*/

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [tracing](dir_c5f5a3ad31e756e37640fc6557a06392.md)
- [tracing\_macros.h](tracing__macros_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
