---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ztest__mock_8h_source.html
original_path: doxygen/html/ztest__mock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ztest\_mock.h

[Go to the documentation of this file.](ztest__mock_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_TESTSUITE\_ZTEST\_MOCK\_H\_

14#define ZEPHYR\_TESTSUITE\_ZTEST\_MOCK\_H\_

15

25

[ 36](group__ztest__mock.md#ga58c2f0c0e628e73a2268a3d18b0440d6)#define ztest\_expect\_value(func, param, value) \

37 z\_ztest\_expect\_value(STRINGIFY(func), STRINGIFY(param), \

38 (uintptr\_t)(value))

39

[ 51](group__ztest__mock.md#gae9af6ba8e51738e938763c896f17ea8f)#define ztest\_check\_expected\_value(param) \

52 z\_ztest\_check\_expected\_value(\_\_func\_\_, STRINGIFY(param), \

53 (uintptr\_t)(param))

54

[ 67](group__ztest__mock.md#gac1a64d8bf9c877e8666e0c6d93b0dbab)#define ztest\_expect\_data(func, param, data) \

68 z\_ztest\_expect\_data(STRINGIFY(func), STRINGIFY(param), (void \*)(data))

69

[ 82](group__ztest__mock.md#ga805cf99272f147beeeee5ad6ca2553f5)#define ztest\_check\_expected\_data(param, length) \

83 z\_ztest\_check\_expected\_data(\_\_func\_\_, STRINGIFY(param), \

84 (void \*)(param), (length))

85

[ 97](group__ztest__mock.md#gac79d097a6b274b25286f2b0e80fbd6e9)#define ztest\_return\_data(func, param, data) \

98 z\_ztest\_return\_data(STRINGIFY(func), STRINGIFY(param), (void \*)(data))

99

[ 110](group__ztest__mock.md#ga12872a3d783d53d564ed94583bc490b0)#define ztest\_copy\_return\_data(param, length) \

111 z\_ztest\_copy\_return\_data(\_\_func\_\_, STRINGIFY(param), \

112 (void \*)(param), (length))

113

[ 119](group__ztest__mock.md#ga2ec539b4c0f3e4efb695213b4fd08c2c)#define ztest\_returns\_value(func, value) \

120 z\_ztest\_returns\_value(STRINGIFY(func), (uintptr\_t)(value))

121

[ 130](group__ztest__mock.md#ga31dcd5b5a3596a7404a771a2d32f3a39)#define ztest\_get\_return\_value() z\_ztest\_get\_return\_value(\_\_func\_\_)

131

[ 140](group__ztest__mock.md#gaa2df2eaeba49019b7a83ac769ea95968)#define ztest\_get\_return\_value\_ptr() \

141 ((void \*)z\_ztest\_get\_return\_value(\_\_func\_\_))

142

146

147#ifdef CONFIG\_ZTEST\_MOCKING

148

149#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

150

151#ifdef \_\_cplusplus

152extern "C" {

153#endif

154

155void z\_init\_mock(void);

156int z\_cleanup\_mock(void);

157

158void z\_ztest\_expect\_value(const char \*fn, const char \*name, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) value);

159void z\_ztest\_check\_expected\_value(const char \*fn, const char \*param,

160 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) value);

161

162void z\_ztest\_expect\_data(const char \*fn, const char \*name, void \*val);

163void z\_ztest\_check\_expected\_data(const char \*fn, const char \*name, void \*data,

164 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) length);

165

166void z\_ztest\_return\_data(const char \*fn, const char \*name, void \*val);

167void z\_ztest\_copy\_return\_data(const char \*fn, const char \*name, void \*data,

168 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) length);

169

170void z\_ztest\_returns\_value(const char \*fn, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) value);

171[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) z\_ztest\_get\_return\_value(const char \*fn);

172

173#ifdef \_\_cplusplus

174}

175#endif

176

177#else /\* !CONFIG\_ZTEST\_MOCKING \*/

178

179#define z\_init\_mock()

180#define z\_cleanup\_mock() 0

181

182#endif /\* CONFIG\_ZTEST\_MOCKING \*/

183

184#endif /\* ZEPHYR\_TESTSUITE\_ZTEST\_MOCK\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [ztest](dir_baac9b2eb462986e22d73d5689d3a238.md)
- [include](dir_c3f97f6cb043cb2f48a1d98a4dc6b6bd.md)
- [zephyr](dir_7f004fc53e18f085dec56f1200601760.md)
- [ztest\_mock.h](ztest__mock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
