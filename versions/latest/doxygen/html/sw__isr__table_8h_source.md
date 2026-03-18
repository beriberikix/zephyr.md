---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sw__isr__table_8h_source.html
original_path: doxygen/html/sw__isr__table_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sw\_isr\_table.h

[Go to the documentation of this file.](sw__isr__table_8h.md)

1/\*

2 \* Copyright (c) 2014, Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_SW\_ISR\_TABLE\_H\_

15#define ZEPHYR\_INCLUDE\_SW\_ISR\_TABLE\_H\_

16

17#if !defined(\_ASMLANGUAGE)

18#include <[zephyr/device.h](device_8h.md)>

19#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

20#include <[zephyr/toolchain.h](toolchain_8h.md)>

21#include <[zephyr/sys/util.h](util_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

27/\* Default vector for the IRQ vector table \*/

28void \_isr\_wrapper(void);

29

30/\* Spurious interrupt handler. Throws an error if called \*/

31void z\_irq\_spurious(const void \*unused);

32

33/\*

34 \* Note the order: arg first, then ISR. This allows a table entry to be

35 \* loaded arg -> r0, isr -> r3 in \_isr\_wrapper with one ldmia instruction,

36 \* on ARM Cortex-M (Thumb2).

37 \*/

38struct \_isr\_table\_entry {

39 const void \*arg;

40 void (\*isr)(const void \*);

41};

42

43/\* The software ISR table itself, an array of these structures indexed by the

44 \* irq line

45 \*/

46extern struct \_isr\_table\_entry \_sw\_isr\_table[];

47

48struct \_irq\_parent\_entry {

49 const struct device \*dev;

50 unsigned int irq;

51 unsigned int offset;

52};

53

54/\*

55 \* Data structure created in a special binary .intlist section for each

56 \* configured interrupt. gen\_irq\_tables.py pulls this out of the binary and

57 \* uses it to create the IRQ vector table and the \_sw\_isr\_table.

58 \*

59 \* More discussion in include/linker/intlist.ld

60 \*

61 \* This is a version used when CONFIG\_ISR\_TABLES\_LOCAL\_DECLARATION is disabled.

62 \* See \_isr\_list\_sname used otherwise.

63 \*/

64struct \_isr\_list {

66 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) irq;

68 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) flags;

70 void \*func;

72 const void \*param;

73};

74

75/\*

76 \* Data structure created in a special binary .intlist section for each

77 \* configured interrupt. gen\_isr\_tables.py pulls this out of the binary and

78 \* uses it to create linker script chunks that would place interrupt table entries

79 \* in the right place in the memory.

80 \*

81 \* This is a version used when CONFIG\_ISR\_TABLES\_LOCAL\_DECLARATION is enabled.

82 \* See \_isr\_list used otherwise.

83 \*/

84struct \_isr\_list\_sname {

86 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) irq;

88 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) flags;

90 const char sname[];

91};

92

93#ifdef CONFIG\_SHARED\_INTERRUPTS

94struct z\_shared\_isr\_table\_entry {

95 struct \_isr\_table\_entry clients[CONFIG\_SHARED\_IRQ\_MAX\_NUM\_CLIENTS];

96 size\_t client\_num;

97};

98

99void z\_shared\_isr(const void \*data);

100

101extern struct z\_shared\_isr\_table\_entry z\_shared\_sw\_isr\_table[];

102#endif /\* CONFIG\_SHARED\_INTERRUPTS \*/

103

[ 105](sw__isr__table_8h.md#a1376eec61303fcd20e7656175ddbaf19)#define ISR\_FLAG\_DIRECT BIT(0)

106

107#define \_MK\_ISR\_NAME(x, y) \_\_MK\_ISR\_NAME(x, y)

108#define \_\_MK\_ISR\_NAME(x, y) \_\_isr\_ ## x ## \_irq\_ ## y

109

110

111#if IS\_ENABLED(CONFIG\_ISR\_TABLES\_LOCAL\_DECLARATION)

112

113#define \_MK\_ISR\_ELEMENT\_NAME(func, id) \_\_MK\_ISR\_ELEMENT\_NAME(func, id)

114#define \_\_MK\_ISR\_ELEMENT\_NAME(func, id) \_\_isr\_table\_entry\_ ## func ## \_irq\_ ## id

115

116#define \_MK\_IRQ\_ELEMENT\_NAME(func, id) \_\_MK\_ISR\_ELEMENT\_NAME(func, id)

117#define \_\_MK\_IRQ\_ELEMENT\_NAME(func, id) \_\_irq\_table\_entry\_ ## func ## \_irq\_ ## id

118

119#define \_MK\_ISR\_SECTION\_NAME(prefix, file, counter) \

120 "." Z\_STRINGIFY(prefix)"."file"." Z\_STRINGIFY(counter)

121

122#define \_MK\_ISR\_ELEMENT\_SECTION(counter) \_MK\_ISR\_SECTION\_NAME(irq, \_\_FILE\_\_, counter)

123#define \_MK\_IRQ\_ELEMENT\_SECTION(counter) \_MK\_ISR\_SECTION\_NAME(isr, \_\_FILE\_\_, counter)

124

125/\* Separated macro to create ISR table entry only.

126 \* Used by Z\_ISR\_DECLARE and ISR tables generation script.

127 \*/

128#define \_Z\_ISR\_TABLE\_ENTRY(irq, func, param, sect) \

129 static Z\_DECL\_ALIGN(struct \_isr\_table\_entry) \

130 \_\_attribute\_\_((section(sect))) \

131 \_\_used \_MK\_ISR\_ELEMENT\_NAME(func, \_\_COUNTER\_\_) = { \

132 .arg = (const void \*)(param), \

133 .isr = (void (\*)(const void \*))(void \*)(func) \

134 }

135

136#define Z\_ISR\_DECLARE\_C(irq, flags, func, param, counter) \

137 \_Z\_ISR\_DECLARE\_C(irq, flags, func, param, counter)

138

139#define \_Z\_ISR\_DECLARE\_C(irq, flags, func, param, counter) \

140 \_Z\_ISR\_TABLE\_ENTRY(irq, func, param, \_MK\_ISR\_ELEMENT\_SECTION(counter)); \

141 static struct \_isr\_list\_sname Z\_GENERIC\_SECTION(.intList) \

142 \_\_used \_MK\_ISR\_NAME(func, counter) = \

143 {irq, flags, \_MK\_ISR\_ELEMENT\_SECTION(counter)}

144

145/\* Create an entry for \_isr\_table to be then placed by the linker.

146 \* An instance of struct \_isr\_list which gets put in the .intList

147 \* section is created with the name of the section where \_isr\_table entry is placed to be then

148 \* used by isr generation script to create linker script chunk.

149 \*/

150#define Z\_ISR\_DECLARE(irq, flags, func, param) \

151 BUILD\_ASSERT(((flags) & ISR\_FLAG\_DIRECT) == 0, "Use Z\_ISR\_DECLARE\_DIRECT macro"); \

152 Z\_ISR\_DECLARE\_C(irq, flags, func, param, \_\_COUNTER\_\_)

153

154

155/\* Separated macro to create ISR Direct table entry only.

156 \* Used by Z\_ISR\_DECLARE\_DIRECT and ISR tables generation script.

157 \*/

158#define \_Z\_ISR\_DIRECT\_TABLE\_ENTRY(irq, func, sect) \

159 COND\_CODE\_1(CONFIG\_IRQ\_VECTOR\_TABLE\_JUMP\_BY\_ADDRESS, ( \

160 static Z\_DECL\_ALIGN(uintptr\_t) \

161 \_\_attribute\_\_((section(sect))) \

162 \_\_used \_MK\_IRQ\_ELEMENT\_NAME(func, \_\_COUNTER\_\_) = ((uintptr\_t)(func)); \

163 ), ( \

164 static void \_\_attribute\_\_((section(sect))) \_\_attribute\_\_((naked)) \

165 \_\_used \_MK\_IRQ\_ELEMENT\_NAME(func, \_\_COUNTER\_\_)(void) { \

166 \_\_asm(ARCH\_IRQ\_VECTOR\_JUMP\_CODE(func)); \

167 } \

168 ))

169

170#define Z\_ISR\_DECLARE\_DIRECT\_C(irq, flags, func, counter) \

171 \_Z\_ISR\_DECLARE\_DIRECT\_C(irq, flags, func, counter)

172

173#define \_Z\_ISR\_DECLARE\_DIRECT\_C(irq, flags, func, counter) \

174 \_Z\_ISR\_DIRECT\_TABLE\_ENTRY(irq, func, \_MK\_IRQ\_ELEMENT\_SECTION(counter)); \

175 static struct \_isr\_list\_sname Z\_GENERIC\_SECTION(.intList) \

176 \_\_used \_MK\_ISR\_NAME(func, counter) = { \

177 irq, \

178 ISR\_FLAG\_DIRECT | (flags), \

179 \_MK\_IRQ\_ELEMENT\_SECTION(counter)}

180

181/\* Create an entry to irq table and place it in specific section which name is then placed

182 \* in an instance of struct \_isr\_list to be then used by the isr generation script to create

183 \* the linker script chunks.

184 \*/

185#define Z\_ISR\_DECLARE\_DIRECT(irq, flags, func) \

186 BUILD\_ASSERT(IS\_ENABLED(CONFIG\_IRQ\_VECTOR\_TABLE\_JUMP\_BY\_ADDRESS) || \

187 IS\_ENABLED(CONFIG\_IRQ\_VECTOR\_TABLE\_JUMP\_BY\_CODE), \

188 "CONFIG\_IRQ\_VECTOR\_TABLE\_JUMP\_BY\_{ADDRESS,CODE} not set"); \

189 Z\_ISR\_DECLARE\_DIRECT\_C(irq, flags, func, \_\_COUNTER\_\_)

190

191

192#else /\* IS\_ENABLED(CONFIG\_ISR\_TABLES\_LOCAL\_DECLARATION) \*/

193

194/\* Create an instance of struct \_isr\_list which gets put in the .intList

195 \* section. This gets consumed by gen\_isr\_tables.py which creates the vector

196 \* and/or SW ISR tables.

197 \*/

198#define Z\_ISR\_DECLARE(irq, flags, func, param) \

199 static Z\_DECL\_ALIGN(struct \_isr\_list) Z\_GENERIC\_SECTION(.intList) \

200 \_\_used \_MK\_ISR\_NAME(func, \_\_COUNTER\_\_) = \

201 {irq, flags, (void \*)&func, (const void \*)param}

202

203/\* The version of the Z\_ISR\_DECLARE that should be used for direct ISR declaration.

204 \* It is here for the API match the version with CONFIG\_ISR\_TABLES\_LOCAL\_DECLARATION enabled.

205 \*/

206#define Z\_ISR\_DECLARE\_DIRECT(irq, flags, func) \

207 Z\_ISR\_DECLARE(irq, ISR\_FLAG\_DIRECT | (flags), func, NULL)

208

209#endif

210

[ 211](sw__isr__table_8h.md#af36594d0586be77420bfe6eaf9f96a2c)#define IRQ\_TABLE\_SIZE (CONFIG\_NUM\_IRQS - CONFIG\_GEN\_IRQ\_START\_VECTOR)

212

213#ifdef CONFIG\_DYNAMIC\_INTERRUPTS

214void z\_isr\_install(unsigned int irq, void (\*routine)(const void \*),

215 const void \*param);

216

217#ifdef CONFIG\_SHARED\_INTERRUPTS

218int z\_isr\_uninstall(unsigned int irq, void (\*routine)(const void \*),

219 const void \*param);

220#endif /\* CONFIG\_SHARED\_INTERRUPTS \*/

221#endif

222

223#ifdef \_\_cplusplus

224}

225#endif

226

227#endif /\* \_ASMLANGUAGE \*/

228

229#endif /\* ZEPHYR\_INCLUDE\_SW\_ISR\_TABLE\_H\_ \*/

[device.h](device_8h.md)

[types.h](include_2zephyr_2types_8h.md)

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sw\_isr\_table.h](sw__isr__table_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
