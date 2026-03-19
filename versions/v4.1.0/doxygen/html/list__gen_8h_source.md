---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/list__gen_8h_source.html
original_path: doxygen/html/list__gen_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

list\_gen.h

[Go to the documentation of this file.](list__gen_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_LIST\_GEN\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_LIST\_GEN\_H\_

9

10#include <stddef.h>

11#include <[stdbool.h](stdbool_8h.md)>

12#include <[zephyr/sys/util.h](sys_2util_8h.md)>

13

14#define Z\_GENLIST\_FOR\_EACH\_NODE(\_\_lname, \_\_l, \_\_sn) \

15 for ((\_\_sn) = sys\_ ## \_\_lname ## \_peek\_head(\_\_l); (\_\_sn) != NULL; \

16 (\_\_sn) = sys\_ ## \_\_lname ## \_peek\_next(\_\_sn))

17

18

19#define Z\_GENLIST\_ITERATE\_FROM\_NODE(\_\_lname, \_\_l, \_\_sn) \

20 for ((\_\_sn) = (\_\_sn) ? sys\_ ## \_\_lname ## \_peek\_next\_no\_check(\_\_sn) \

21 : sys\_ ## \_\_lname ## \_peek\_head(\_\_l); \

22 (\_\_sn) != NULL; \

23 (\_\_sn) = sys\_ ## \_\_lname ## \_peek\_next(\_\_sn))

24

25#define Z\_GENLIST\_FOR\_EACH\_NODE\_SAFE(\_\_lname, \_\_l, \_\_sn, \_\_sns) \

26 for ((\_\_sn) = sys\_ ## \_\_lname ## \_peek\_head(\_\_l), \

27 (\_\_sns) = sys\_ ## \_\_lname ## \_peek\_next(\_\_sn); \

28 (\_\_sn) != NULL ; (\_\_sn) = (\_\_sns), \

29 (\_\_sns) = sys\_ ## \_\_lname ## \_peek\_next(\_\_sn))

30

31#define Z\_GENLIST\_CONTAINER(\_\_ln, \_\_cn, \_\_n) \

32 ((\_\_ln) ? CONTAINER\_OF((\_\_ln), \_\_typeof\_\_(\*(\_\_cn)), \_\_n) : NULL)

33

34#define Z\_GENLIST\_PEEK\_HEAD\_CONTAINER(\_\_lname, \_\_l, \_\_cn, \_\_n) \

35 Z\_GENLIST\_CONTAINER(sys\_ ## \_\_lname ## \_peek\_head(\_\_l), \_\_cn, \_\_n)

36

37#define Z\_GENLIST\_PEEK\_TAIL\_CONTAINER(\_\_lname, \_\_l, \_\_cn, \_\_n) \

38 Z\_GENLIST\_CONTAINER(sys\_ ## \_\_lname ## \_peek\_tail(\_\_l), \_\_cn, \_\_n)

39

40#define Z\_GENLIST\_PEEK\_NEXT\_CONTAINER(\_\_lname, \_\_cn, \_\_n) \

41 ((\_\_cn) ? Z\_GENLIST\_CONTAINER( \

42 sys\_ ## \_\_lname ## \_peek\_next(&((\_\_cn)->\_\_n)), \

43 \_\_cn, \_\_n) : NULL)

44

45#define Z\_GENLIST\_FOR\_EACH\_CONTAINER(\_\_lname, \_\_l, \_\_cn, \_\_n) \

46 for ((\_\_cn) = Z\_GENLIST\_PEEK\_HEAD\_CONTAINER(\_\_lname, \_\_l, \_\_cn, \

47 \_\_n); \

48 (\_\_cn) != NULL; \

49 (\_\_cn) = Z\_GENLIST\_PEEK\_NEXT\_CONTAINER(\_\_lname, \_\_cn, \_\_n))

50

51#define Z\_GENLIST\_FOR\_EACH\_CONTAINER\_SAFE(\_\_lname, \_\_l, \_\_cn, \_\_cns, \_\_n) \

52 for ((\_\_cn) = Z\_GENLIST\_PEEK\_HEAD\_CONTAINER(\_\_lname, \_\_l, \_\_cn, \_\_n), \

53 (\_\_cns) = Z\_GENLIST\_PEEK\_NEXT\_CONTAINER(\_\_lname, \_\_cn, \_\_n); \

54 (\_\_cn) != NULL; (\_\_cn) = (\_\_cns), \

55 (\_\_cns) = Z\_GENLIST\_PEEK\_NEXT\_CONTAINER(\_\_lname, \_\_cn, \_\_n))

56

57#define Z\_GENLIST\_IS\_EMPTY(\_\_lname) \

58 static inline bool \

59 sys\_ ## \_\_lname ## \_is\_empty(sys\_ ## \_\_lname ## \_t \*list) \

60 { \

61 return (sys\_ ## \_\_lname ## \_peek\_head(list) == NULL); \

62 }

63

64#define Z\_GENLIST\_PEEK\_NEXT\_NO\_CHECK(\_\_lname, \_\_nname) \

65 static inline sys\_ ## \_\_nname ## \_t \* \

66 sys\_ ## \_\_lname ## \_peek\_next\_no\_check(sys\_ ## \_\_nname ## \_t \*node) \

67 { \

68 return z\_ ## \_\_nname ## \_next\_peek(node); \

69 }

70

71#define Z\_GENLIST\_PEEK\_NEXT(\_\_lname, \_\_nname) \

72 static inline sys\_ ## \_\_nname ## \_t \* \

73 sys\_ ## \_\_lname ## \_peek\_next(sys\_ ## \_\_nname ## \_t \*node) \

74 { \

75 return (node != NULL) ? \

76 sys\_ ## \_\_lname ## \_peek\_next\_no\_check(node) : \

77 NULL; \

78 }

79

80#define Z\_GENLIST\_PREPEND(\_\_lname, \_\_nname) \

81 static inline void \

82 sys\_ ## \_\_lname ## \_prepend(sys\_ ## \_\_lname ## \_t \*list, \

83 sys\_ ## \_\_nname ## \_t \*node) \

84 { \

85 z\_ ## \_\_nname ## \_next\_set(node, \

86 sys\_ ## \_\_lname ## \_peek\_head(list)); \

87 z\_ ## \_\_lname ## \_head\_set(list, node); \

88 \

89 if (sys\_ ## \_\_lname ## \_peek\_tail(list) == NULL) { \

90 z\_ ## \_\_lname ## \_tail\_set(list, \

91 sys\_ ## \_\_lname ## \_peek\_head(list)); \

92 } \

93 }

94

95#define Z\_GENLIST\_APPEND(\_\_lname, \_\_nname) \

96 static inline void \

97 sys\_ ## \_\_lname ## \_append(sys\_ ## \_\_lname ## \_t \*list, \

98 sys\_ ## \_\_nname ## \_t \*node) \

99 { \

100 z\_ ## \_\_nname ## \_next\_set(node, NULL); \

101 \

102 if (sys\_ ## \_\_lname ## \_peek\_tail(list) == NULL) { \

103 z\_ ## \_\_lname ## \_tail\_set(list, node); \

104 z\_ ## \_\_lname ## \_head\_set(list, node); \

105 } else { \

106 z\_ ## \_\_nname ## \_next\_set( \

107 sys\_ ## \_\_lname ## \_peek\_tail(list), \

108 node); \

109 z\_ ## \_\_lname ## \_tail\_set(list, node); \

110 } \

111 }

112

113#define Z\_GENLIST\_APPEND\_LIST(\_\_lname, \_\_nname) \

114 static inline void \

115 sys\_ ## \_\_lname ## \_append\_list(sys\_ ## \_\_lname ## \_t \*list, \

116 void \*head, void \*tail) \

117{ \

118 if (head != NULL && tail != NULL) { \

119 if (sys\_ ## \_\_lname ## \_peek\_tail(list) == NULL) { \

120 z\_ ## \_\_lname ## \_head\_set(list, \

121 (sys\_ ## \_\_nname ## \_t \*)head); \

122 } else { \

123 z\_ ## \_\_nname ## \_next\_set( \

124 sys\_ ## \_\_lname ## \_peek\_tail(list), \

125 (sys\_ ## \_\_nname ## \_t \*)head); \

126 } \

127 z\_ ## \_\_lname ## \_tail\_set(list, \

128 (sys\_ ## \_\_nname ## \_t \*)tail); \

129 } \

130}

131

132#define Z\_GENLIST\_MERGE\_LIST(\_\_lname, \_\_nname) \

133 static inline void \

134 sys\_ ## \_\_lname ## \_merge\_ ## \_\_lname ( \

135 sys\_ ## \_\_lname ## \_t \*list, \

136 sys\_ ## \_\_lname ## \_t \*list\_to\_append) \

137 { \

138 sys\_ ## \_\_nname ## \_t \*head, \*tail; \

139 head = sys\_ ## \_\_lname ## \_peek\_head(list\_to\_append); \

140 tail = sys\_ ## \_\_lname ## \_peek\_tail(list\_to\_append); \

141 sys\_ ## \_\_lname ## \_append\_list(list, head, tail); \

142 sys\_ ## \_\_lname ## \_init(list\_to\_append); \

143 }

144

145#define Z\_GENLIST\_INSERT(\_\_lname, \_\_nname) \

146 static inline void \

147 sys\_ ## \_\_lname ## \_insert(sys\_ ## \_\_lname ## \_t \*list, \

148 sys\_ ## \_\_nname ## \_t \*prev, \

149 sys\_ ## \_\_nname ## \_t \*node) \

150 { \

151 if (prev == NULL) { \

152 sys\_ ## \_\_lname ## \_prepend(list, node); \

153 } else if (z\_ ## \_\_nname ## \_next\_peek(prev) == NULL) { \

154 sys\_ ## \_\_lname ## \_append(list, node); \

155 } else { \

156 z\_ ## \_\_nname ## \_next\_set(node, \

157 z\_ ## \_\_nname ## \_next\_peek(prev)); \

158 z\_ ## \_\_nname ## \_next\_set(prev, node); \

159 } \

160 }

161

162#define Z\_GENLIST\_GET\_NOT\_EMPTY(\_\_lname, \_\_nname) \

163 static inline sys\_ ## \_\_nname ## \_t \* \

164 sys\_ ## \_\_lname ## \_get\_not\_empty(sys\_ ## \_\_lname ## \_t \*list) \

165 { \

166 sys\_ ## \_\_nname ## \_t \*node = \

167 sys\_ ## \_\_lname ## \_peek\_head(list); \

168 \

169 z\_ ## \_\_lname ## \_head\_set(list, \

170 z\_ ## \_\_nname ## \_next\_peek(node)); \

171 if (sys\_ ## \_\_lname ## \_peek\_tail(list) == node) { \

172 z\_ ## \_\_lname ## \_tail\_set(list, \

173 sys\_ ## \_\_lname ## \_peek\_head(list)); \

174 } \

175 \

176 return node; \

177 }

178

179#define Z\_GENLIST\_GET(\_\_lname, \_\_nname) \

180 static inline sys\_ ## \_\_nname ## \_t \* \

181 sys\_ ## \_\_lname ## \_get(sys\_ ## \_\_lname ## \_t \*list) \

182 { \

183 return sys\_ ## \_\_lname ## \_is\_empty(list) ? NULL : \

184 sys\_ ## \_\_lname ## \_get\_not\_empty(list); \

185 }

186

187#define Z\_GENLIST\_REMOVE(\_\_lname, \_\_nname) \

188 static inline void \

189 sys\_ ## \_\_lname ## \_remove(sys\_ ## \_\_lname ## \_t \*list, \

190 sys\_ ## \_\_nname ## \_t \*prev\_node, \

191 sys\_ ## \_\_nname ## \_t \*node) \

192 { \

193 if (prev\_node == NULL) { \

194 z\_ ## \_\_lname ## \_head\_set(list, \

195 z\_ ## \_\_nname ## \_next\_peek(node)); \

196 \

197 /\* Was node also the tail? \*/ \

198 if (sys\_ ## \_\_lname ## \_peek\_tail(list) == node) { \

199 z\_ ## \_\_lname ## \_tail\_set(list, \

200 sys\_ ## \_\_lname ## \_peek\_head(list)); \

201 } \

202 } else { \

203 z\_ ## \_\_nname ## \_next\_set(prev\_node, \

204 z\_ ## \_\_nname ## \_next\_peek(node)); \

205 \

206 /\* Was node the tail? \*/ \

207 if (sys\_ ## \_\_lname ## \_peek\_tail(list) == node) { \

208 z\_ ## \_\_lname ## \_tail\_set(list, \

209 prev\_node); \

210 } \

211 } \

212 \

213 z\_ ## \_\_nname ## \_next\_set(node, NULL); \

214 }

215

216#define Z\_GENLIST\_FIND\_AND\_REMOVE(\_\_lname, \_\_nname) \

217 static inline bool \

218 sys\_ ## \_\_lname ## \_find\_and\_remove(sys\_ ## \_\_lname ## \_t \*list, \

219 sys\_ ## \_\_nname ## \_t \*node) \

220 { \

221 sys\_ ## \_\_nname ## \_t \*prev = NULL; \

222 sys\_ ## \_\_nname ## \_t \*test; \

223 \

224 Z\_GENLIST\_FOR\_EACH\_NODE(\_\_lname, list, test) { \

225 if (test == node) { \

226 sys\_ ## \_\_lname ## \_remove(list, prev, \

227 node); \

228 return true; \

229 } \

230 \

231 prev = test; \

232 } \

233 \

234 return false; \

235 }

236

237#define Z\_GENLIST\_FIND(\_\_lname, \_\_nname) \

238 static inline bool sys\_##\_\_lname##\_find( \

239 sys\_##\_\_lname##\_t \*list, sys\_##\_\_nname##\_t \*node, sys\_##\_\_nname##\_t \*\*prev) \

240 { \

241 sys\_##\_\_nname##\_t \*current = NULL; \

242 sys\_##\_\_nname##\_t \*previous = NULL; \

243 \

244 Z\_GENLIST\_FOR\_EACH\_NODE(\_\_lname, list, current) { \

245 if (current == node) { \

246 if (prev != NULL) { \

247 \*prev = previous; \

248 } \

249 return true; \

250 } \

251 \

252 previous = current; \

253 } \

254 \

255 if (prev != NULL) { \

256 \*prev = previous; \

257 } \

258 \

259 return false; \

260 }

261

262#define Z\_GENLIST\_LEN(\_\_lname, \_\_nname) \

263 static inline size\_t sys\_##\_\_lname##\_len(sys\_##\_\_lname##\_t \* list) \

264 { \

265 size\_t len = 0; \

266 static sys\_##\_\_nname##\_t \* node; \

267 Z\_GENLIST\_FOR\_EACH\_NODE(\_\_lname, list, node) { \

268 len++; \

269 } \

270 return len; \

271 }

272

273#endif /\* ZEPHYR\_INCLUDE\_SYS\_LIST\_GEN\_H\_ \*/

[stdbool.h](stdbool_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [list\_gen.h](list__gen_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
