---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arc__connect_8h_source.html
original_path: doxygen/html/arc__connect_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arc\_connect.h

[Go to the documentation of this file.](arc__connect_8h.md)

1/\*

2 \* Copyright (c) 2019 Synopsys.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_ARC\_CONNECT\_H\_

15#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_ARC\_CONNECT\_H\_

16

17#ifndef \_ASMLANGUAGE

18#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

19#include <[zephyr/arch/arc/v2/aux\_regs.h](aux__regs_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

25#define \_ARC\_V2\_CONNECT\_BCR 0x0d0

26#define \_ARC\_V2\_CONNECT\_IDU\_BCR 0x0d5

27#define \_ARC\_V2\_CONNECT\_GFRC\_BCR 0x0d6

28#define \_ARC\_V2\_CONNECT\_CMD 0x600

29#define \_ARC\_V2\_CONNECT\_WDATA 0x601

30#define \_ARC\_V2\_CONNECT\_READBACK 0x602

31

32

[ 33](arc__connect_8h.md#aa0916ff664e0555cca8d89a91a97f0af)#define ARC\_CONNECT\_CMD\_CHECK\_CORE\_ID 0x0

34

[ 35](arc__connect_8h.md#a60b0ff098e6b3b90844e9114b736e850)#define ARC\_CONNECT\_CMD\_INTRPT\_GENERATE\_IRQ 0x1

[ 36](arc__connect_8h.md#a96eb8f0b5182143b5d4e9837a28cbe96)#define ARC\_CONNECT\_CMD\_INTRPT\_GENERATE\_ACK 0x2

[ 37](arc__connect_8h.md#af4d24daffda05ed8dff95fe6b8ebb54d)#define ARC\_CONNECT\_CMD\_INTRPT\_READ\_STATUS 0x3

[ 38](arc__connect_8h.md#a4385db77797902d33cdd68040b4e44d5)#define ARC\_CONNECT\_CMD\_INTRPT\_CHECK\_SOURCE 0x4

39

[ 40](arc__connect_8h.md#ad371fa315bc739421c302d9f5836aea0)#define ARC\_CONNECT\_CMD\_SEMA\_CLAIM\_AND\_READ 0x11

[ 41](arc__connect_8h.md#aeb3a29644bb96b3ae1466c65573310a5)#define ARC\_CONNECT\_CMD\_SEMA\_RELEASE 0x12

[ 42](arc__connect_8h.md#a98224c548cd6a21711c65a14a7e1f7ea)#define ARC\_CONNECT\_CMD\_SEMA\_FORCE\_RELEASE 0x13

43

[ 44](arc__connect_8h.md#a6a0cc8aafee6d4234f461f38653ff86b)#define ARC\_CONNECT\_CMD\_MSG\_SRAM\_SET\_ADDR 0x21

[ 45](arc__connect_8h.md#a079317281d49d8e57f2a08ce5b396aa4)#define ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_ADDR 0x22

[ 46](arc__connect_8h.md#abf3ca67becaed32adec81175a393aa25)#define ARC\_CONNECT\_CMD\_MSG\_SRAM\_SET\_ADDR\_OFFSET 0x23

[ 47](arc__connect_8h.md#a4a09502754de405e3ed9f1459865281c)#define ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_ADDR\_OFFSET 0x24

[ 48](arc__connect_8h.md#a19e19e783ad81f6738e01cdaf551910a)#define ARC\_CONNECT\_CMD\_MSG\_SRAM\_WRITE 0x25

[ 49](arc__connect_8h.md#ad9c105f0ec703aaccaefa51e058b8e66)#define ARC\_CONNECT\_CMD\_MSG\_SRAM\_WRITE\_INC 0x26

[ 50](arc__connect_8h.md#a7ef798f2fb76d2376233b2ac4563bda4)#define ARC\_CONNECT\_CMD\_MSG\_SRAM\_WRITE\_IMM 0x27

[ 51](arc__connect_8h.md#a95abc6ae373160a7fdd95eeeaffbf068)#define ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ 0x28

[ 52](arc__connect_8h.md#a1fa49a1bd5740431b7e1031ec3f4e3a5)#define ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_INC 0x29

[ 53](arc__connect_8h.md#a2291642fff8644955ed8c91dd5459f58)#define ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_IMM 0x2a

[ 54](arc__connect_8h.md#abfa2e40196acb76717e6ac5d7d2ccea2)#define ARC\_CONNECT\_CMD\_MSG\_SRAM\_SET\_ECC\_CTRL 0x2b

[ 55](arc__connect_8h.md#a250624ed309ab3ce6158dfd472c7e62b)#define ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_ECC\_CTRL 0x2c

56

[ 57](arc__connect_8h.md#a5de7138d686356bf695c73f7991a5cd2)#define ARC\_CONNECT\_CMD\_DEBUG\_RESET 0x31

[ 58](arc__connect_8h.md#a79d027948ada6f25c40858a1842a3165)#define ARC\_CONNECT\_CMD\_DEBUG\_HALT 0x32

[ 59](arc__connect_8h.md#a9f9f9f414b3dda3487078154993fa4b9)#define ARC\_CONNECT\_CMD\_DEBUG\_RUN 0x33

[ 60](arc__connect_8h.md#af4560d50adc746f660695b60e5a534ef)#define ARC\_CONNECT\_CMD\_DEBUG\_SET\_MASK 0x34

[ 61](arc__connect_8h.md#a1e1efe68fe11446d8c54685e820f2dd0)#define ARC\_CONNECT\_CMD\_DEBUG\_READ\_MASK 0x35

[ 62](arc__connect_8h.md#a1c22504f72eccdd532d39525c3a3938e)#define ARC\_CONNECT\_CMD\_DEBUG\_SET\_SELECT 0x36

[ 63](arc__connect_8h.md#ad825597a6a0948fa0e8c6d8d16169c93)#define ARC\_CONNECT\_CMD\_DEBUG\_READ\_SELECT 0x37

[ 64](arc__connect_8h.md#a09feefc3b1b8d7f818dcdc7fe817a594)#define ARC\_CONNECT\_CMD\_DEBUG\_READ\_EN 0x38

[ 65](arc__connect_8h.md#aaf0860d01aca22d2c057418603bed930)#define ARC\_CONNECT\_CMD\_DEBUG\_READ\_CMD 0x39

[ 66](arc__connect_8h.md#a2e5ddca1dfc8e24cb5cb7825e9be9ba1)#define ARC\_CONNECT\_CMD\_DEBUG\_READ\_CORE 0x3a

67

[ 68](arc__connect_8h.md#a286b79aaff7ec2eb5df86927abf2fa0f)#define ARC\_CONNECT\_CMD\_DEBUG\_MASK\_SH 0x08 /\* if a self-halt occurs, a global halt is triggered \*/

[ 69](arc__connect_8h.md#af109c1e8746d8f33d170db073cc2df9e)#define ARC\_CONNECT\_CMD\_DEBUG\_MASK\_BH 0x04 /\* if a breakpoint caused halt occurs, a global halt is triggered \*/

[ 70](arc__connect_8h.md#a677a6e9abbd1ff3657f17bf5f272ad9a)#define ARC\_CONNECT\_CMD\_DEBUG\_MASK\_AH 0x02 /\* if an actionpoint caused halt occurs, a global halt is triggered \*/

[ 71](arc__connect_8h.md#a9f2c6449b60ac3123e4ef3b98c12c4f1)#define ARC\_CONNECT\_CMD\_DEBUG\_MASK\_H 0x01 /\* whenever the core is halted, a global halt is triggered \*/

72

[ 73](arc__connect_8h.md#a32332ac2356d0b7bc1f2d2f8642f8bd0)#define ARC\_CONNECT\_CMD\_GFRC\_CLEAR 0x41

[ 74](arc__connect_8h.md#aa8a28e07e540f418bf016538d42bde82)#define ARC\_CONNECT\_CMD\_GFRC\_READ\_LO 0x42

[ 75](arc__connect_8h.md#a706c63576dd21a2b924911fb121782f4)#define ARC\_CONNECT\_CMD\_GFRC\_READ\_HI 0x43

[ 76](arc__connect_8h.md#a14c5bf6c6fbea0b73204f147411efb19)#define ARC\_CONNECT\_CMD\_GFRC\_ENABLE 0x44

[ 77](arc__connect_8h.md#ab1a780f10bb9cc5718607b4e8cdbbba4)#define ARC\_CONNECT\_CMD\_GFRC\_DISABLE 0x45

[ 78](arc__connect_8h.md#a886660fefc56e449dfdb1f0db3047730)#define ARC\_CONNECT\_CMD\_GFRC\_READ\_DISABLE 0x46

[ 79](arc__connect_8h.md#a0944e99eebe084f942bdb7c22b74bfc0)#define ARC\_CONNECT\_CMD\_GFRC\_SET\_CORE 0x47

[ 80](arc__connect_8h.md#a588d0b3b5272afd4164920b468e4bf31)#define ARC\_CONNECT\_CMD\_GFRC\_READ\_CORE 0x48

[ 81](arc__connect_8h.md#aaf7a4f5122847621acb233e7849a6b6d)#define ARC\_CONNECT\_CMD\_GFRC\_READ\_HALT 0x49

82

[ 83](arc__connect_8h.md#a497ee266769c5ca951a402895dead4a8)#define ARC\_CONNECT\_CMD\_PDM\_SET\_PM 0x81

[ 84](arc__connect_8h.md#afd8a691965ed96ac3e5949f529598450)#define ARC\_CONNECT\_CMD\_PDM\_READ\_PSTATUS 0x82

85

[ 86](arc__connect_8h.md#a187e3d3614537efd81bff08788f083b9)#define ARC\_CONNECT\_CMD\_PMU\_SET\_PUCNT 0x51

[ 87](arc__connect_8h.md#a1028729196bcc91e5d16341d78ad97ee)#define ARC\_CONNECT\_CMD\_PMU\_READ\_PUCNT 0x52

[ 88](arc__connect_8h.md#a0f819573b0c71f6719813ca40d181d2a)#define ARC\_CONNECT\_CMD\_PMU\_SET\_RSTCNT 0x53

[ 89](arc__connect_8h.md#ae3f58528546b78730f9e48a024927913)#define ARC\_CONNECT\_CMD\_PMU\_READ\_RSTCNT 0x54

[ 90](arc__connect_8h.md#a756ac1596057df9ffc4a12d048a678d1)#define ARC\_CONNECT\_CMD\_PMU\_SET\_PDCNT 0x55

[ 91](arc__connect_8h.md#a22c2df120423e7243719d223130ec0d3)#define ARC\_CONNECT\_CMD\_PMU\_READ\_PDCNT 0x56

92

[ 93](arc__connect_8h.md#afcc229c691acfb72afc9ab344ff0fc07)#define ARC\_CONNECT\_CMD\_IDU\_ENABLE 0x71

[ 94](arc__connect_8h.md#a22292ad920b7222e1bf3d057cee6a9c0)#define ARC\_CONNECT\_CMD\_IDU\_DISABLE 0x72

[ 95](arc__connect_8h.md#a99f1e171858a67934a83ecc5f96b367d)#define ARC\_CONNECT\_CMD\_IDU\_READ\_ENABLE 0x73

[ 96](arc__connect_8h.md#a0ac262572bd76b18d6a36c96557a8880)#define ARC\_CONNECT\_CMD\_IDU\_SET\_MODE 0x74

[ 97](arc__connect_8h.md#a7a699283d26fe84104ed4d57d09657e2)#define ARC\_CONNECT\_CMD\_IDU\_READ\_MODE 0x75

[ 98](arc__connect_8h.md#afb2d3ade8e16c9f302fa245c5a27b186)#define ARC\_CONNECT\_CMD\_IDU\_SET\_DEST 0x76

[ 99](arc__connect_8h.md#adf49a1317a314ac6c2fc9b796f9577c8)#define ARC\_CONNECT\_CMD\_IDU\_READ\_DEST 0x77

[ 100](arc__connect_8h.md#a20b34806c9402e938874f0fb9cbe42d9)#define ARC\_CONNECT\_CMD\_IDU\_GEN\_CIRQ 0x78

[ 101](arc__connect_8h.md#abe7202c5a016c9a94eeb6d8995eea03c)#define ARC\_CONNECT\_CMD\_IDU\_ACK\_CIRQ 0x79

[ 102](arc__connect_8h.md#a4c3da41b3dec1043ad46607d945895a9)#define ARC\_CONNECT\_CMD\_IDU\_CHECK\_STATUS 0x7a

[ 103](arc__connect_8h.md#a8a306828e1fef2bbf7aa30a95c2b2359)#define ARC\_CONNECT\_CMD\_IDU\_CHECK\_SOURCE 0x7b

[ 104](arc__connect_8h.md#a066d1063d46301167e19ae2a9011c5f8)#define ARC\_CONNECT\_CMD\_IDU\_SET\_MASK 0x7c

[ 105](arc__connect_8h.md#a45b6e97825dccc8b73943a9eaa2a876c)#define ARC\_CONNECT\_CMD\_IDU\_READ\_MASK 0x7d

[ 106](arc__connect_8h.md#ae6a517147194f518687ad0ac8eb107a6)#define ARC\_CONNECT\_CMD\_IDU\_CHECK\_FIRST 0x7e

107

108/\* the start intno of common interrupt managed by IDU \*/

[ 109](arc__connect_8h.md#a4e5782d78d6200b217740c83be9ac9de)#define ARC\_CONNECT\_IDU\_IRQ\_START 24

110

[ 111](arc__connect_8h.md#ad1978b6fef840e5f15b239d995a1d9d4)#define ARC\_CONNECT\_INTRPT\_TRIGGER\_LEVEL 0

[ 112](arc__connect_8h.md#a75b642dd17f8851fb7cb2109fafd7578)#define ARC\_CONNECT\_INTRPT\_TRIGGER\_EDGE 1

113

114

[ 115](arc__connect_8h.md#af3566e4fd9229da92068284811608f5b)#define ARC\_CONNECT\_DISTRI\_MODE\_ROUND\_ROBIN 0

[ 116](arc__connect_8h.md#aff9e1c8c2e14244286702d8038d4dc9b)#define ARC\_CONNECT\_DISTRI\_MODE\_FIRST\_ACK 1

[ 117](arc__connect_8h.md#a26667f2090d8ebd9229ca02964491644)#define ARC\_CONNECT\_DISTRI\_ALL\_DEST 2

118

[ 119](structarc__connect__cmd.md)struct [arc\_connect\_cmd](structarc__connect__cmd.md) {

120 union {

121 struct {

122#ifdef CONFIG\_BIG\_ENDIAN

123 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pad](structarc__connect__cmd.md#afc0086f899ec7e4ea7ae5ea33a6971cf):8, [param](structarc__connect__cmd.md#a6c03654eda9c5074ea9012cfa8bb18a3):16, [cmd](structarc__connect__cmd.md#a83c7cc807f7e5f8593574715cc60fb4d):8;

124#else

[ 125](structarc__connect__cmd.md#a83c7cc807f7e5f8593574715cc60fb4d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](structarc__connect__cmd.md#a83c7cc807f7e5f8593574715cc60fb4d):8, [param](structarc__connect__cmd.md#a6c03654eda9c5074ea9012cfa8bb18a3):16, [pad](structarc__connect__cmd.md#afc0086f899ec7e4ea7ae5ea33a6971cf):8;

126#endif

127 };

[ 128](structarc__connect__cmd.md#afb90551e0d8ad5acb910559dabff1471) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [val](structarc__connect__cmd.md#afb90551e0d8ad5acb910559dabff1471);

129 };

130};

131

[ 132](structarc__connect__bcr.md)struct [arc\_connect\_bcr](structarc__connect__bcr.md) {

133 union {

134 struct {

135#ifdef CONFIG\_BIG\_ENDIAN

136 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pad4](structarc__connect__bcr.md#a82d4bdda236354afdf404095357fdae9):6, [pw\_dom](structarc__connect__bcr.md#a6b1b8a15f8a0810cfcea6d8dd9be6472):1, [pad3](structarc__connect__bcr.md#a88a11fb3a63c29bc3b3aee257dc06a00):1,

137 [idu](structarc__connect__bcr.md#a071473060cc797f07597a4ca045aef45):1, [pad2](structarc__connect__bcr.md#a6c8a939a2f64fb6b3d380ab1307f5e65):1, [num\_cores](structarc__connect__bcr.md#a54c7c0f5a72bacf8cd3d75a3cc72e97f):6,

138 [pad](structarc__connect__bcr.md#a6e7ea65b84ff34f654378ffac1e96ec2):1, [gfrc](structarc__connect__bcr.md#a0b8c138e13adbdc8b52f1175695de118):1, [dbg](structarc__connect__bcr.md#af2ff782f9553c40f60327b71775501d1):1, [pw](structarc__connect__bcr.md#a003fa1c240a59c8f71da9db4b9a3479f):1,

139 [msg](structarc__connect__bcr.md#a806d475e167702366f283ce1d8afaa8c):1, [sem](structarc__connect__bcr.md#acfe524a8fd38e21dd3dce1c58e285f62):1, [ipi](structarc__connect__bcr.md#a6a6b3eb2c8074cdd860508dbcad455e9):1, [slv](structarc__connect__bcr.md#a64144525d109f4b425b0814352f7e46f):1,

140 [ver](structarc__connect__bcr.md#aba1da6026b038bb551466402c3ee4f14):8;

141#else

[ 142](structarc__connect__bcr.md#aba1da6026b038bb551466402c3ee4f14) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ver](structarc__connect__bcr.md#aba1da6026b038bb551466402c3ee4f14):8,

[ 143](structarc__connect__bcr.md#a6a6b3eb2c8074cdd860508dbcad455e9) [slv](structarc__connect__bcr.md#a64144525d109f4b425b0814352f7e46f):1, [ipi](structarc__connect__bcr.md#a6a6b3eb2c8074cdd860508dbcad455e9):1, [sem](structarc__connect__bcr.md#acfe524a8fd38e21dd3dce1c58e285f62):1, [msg](structarc__connect__bcr.md#a806d475e167702366f283ce1d8afaa8c):1,

[ 144](structarc__connect__bcr.md#af2ff782f9553c40f60327b71775501d1) [pw](structarc__connect__bcr.md#a003fa1c240a59c8f71da9db4b9a3479f):1, [dbg](structarc__connect__bcr.md#af2ff782f9553c40f60327b71775501d1):1, [gfrc](structarc__connect__bcr.md#a0b8c138e13adbdc8b52f1175695de118):1, [pad](structarc__connect__bcr.md#a6e7ea65b84ff34f654378ffac1e96ec2):1,

[ 145](structarc__connect__bcr.md#a071473060cc797f07597a4ca045aef45) [num\_cores](structarc__connect__bcr.md#a54c7c0f5a72bacf8cd3d75a3cc72e97f):6, [pad2](structarc__connect__bcr.md#a6c8a939a2f64fb6b3d380ab1307f5e65):1, [idu](structarc__connect__bcr.md#a071473060cc797f07597a4ca045aef45):1,

[ 146](structarc__connect__bcr.md#a88a11fb3a63c29bc3b3aee257dc06a00) [pad3](structarc__connect__bcr.md#a88a11fb3a63c29bc3b3aee257dc06a00):1, [pw\_dom](structarc__connect__bcr.md#a6b1b8a15f8a0810cfcea6d8dd9be6472):1, [pad4](structarc__connect__bcr.md#a82d4bdda236354afdf404095357fdae9):6;

147#endif

148 };

[ 149](structarc__connect__bcr.md#a00ec9d596b6b1e508321907e59060f8e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [val](structarc__connect__bcr.md#a00ec9d596b6b1e508321907e59060f8e);

150 };

151};

152

[ 153](structarc__connect__idu__bcr.md)struct [arc\_connect\_idu\_bcr](structarc__connect__idu__bcr.md) {

154 union {

155 struct {

156#ifdef CONFIG\_BIG\_ENDIAN

157 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pad](structarc__connect__idu__bcr.md#a1c6fe3452ad5188cfa778631b3e0af83):21, [cirqnum](structarc__connect__idu__bcr.md#af812a1c84d91f57915eba4656b2a4204):3, [ver](structarc__connect__idu__bcr.md#afc8b571a896aa33c6f009fe5a3794058):8;

158#else

[ 159](structarc__connect__idu__bcr.md#af812a1c84d91f57915eba4656b2a4204) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ver](structarc__connect__idu__bcr.md#afc8b571a896aa33c6f009fe5a3794058):8, [cirqnum](structarc__connect__idu__bcr.md#af812a1c84d91f57915eba4656b2a4204):3, [pad](structarc__connect__idu__bcr.md#a1c6fe3452ad5188cfa778631b3e0af83):21;

160#endif

161 };

[ 162](structarc__connect__idu__bcr.md#aeef8bbdd06ac006c6f9f910671a993e6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [val](structarc__connect__idu__bcr.md#aeef8bbdd06ac006c6f9f910671a993e6);

163 };

164};

165

166static inline void z\_arc\_connect\_cmd([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) param)

167{

168 struct [arc\_connect\_cmd](structarc__connect__cmd.md) regval;

169

170 regval.[pad](structarc__connect__cmd.md#afc0086f899ec7e4ea7ae5ea33a6971cf) = 0;

171 regval.[cmd](structarc__connect__cmd.md#a83c7cc807f7e5f8593574715cc60fb4d) = [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615);

172 regval.[param](structarc__connect__cmd.md#a6c03654eda9c5074ea9012cfa8bb18a3) = [param](structarc__connect__cmd.md#a6c03654eda9c5074ea9012cfa8bb18a3);

173

174 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_CONNECT\_CMD, regval.[val](structarc__connect__cmd.md#afb90551e0d8ad5acb910559dabff1471));

175}

176

177static inline void z\_arc\_connect\_cmd\_data([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [param](structarc__connect__cmd.md#a6c03654eda9c5074ea9012cfa8bb18a3),

178 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data)

179{

180 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_CONNECT\_WDATA, data);

181 z\_arc\_connect\_cmd([cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [param](structarc__connect__cmd.md#a6c03654eda9c5074ea9012cfa8bb18a3));

182}

183

184static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arc\_connect\_cmd\_readback(void)

185{

186 return z\_arc\_v2\_aux\_reg\_read(\_ARC\_V2\_CONNECT\_READBACK);

187}

188

189

190/\* inter-core interrupt related functions \*/

191extern void z\_arc\_connect\_ici\_generate([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) core\_id);

192extern void z\_arc\_connect\_ici\_ack([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) core\_id);

193extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arc\_connect\_ici\_read\_status([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) core\_id);

194extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arc\_connect\_ici\_check\_src(void);

195extern void z\_arc\_connect\_ici\_clear(void);

196

197/\* inter-core debug related functions \*/

198extern void z\_arc\_connect\_debug\_reset([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) core\_mask);

199extern void z\_arc\_connect\_debug\_halt([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) core\_mask);

200extern void z\_arc\_connect\_debug\_run([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) core\_mask);

201extern void z\_arc\_connect\_debug\_mask\_set([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) core\_mask, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask);

202extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arc\_connect\_debug\_mask\_read([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) core\_mask);

203extern void z\_arc\_connect\_debug\_select\_set([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) core\_mask);

204extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arc\_connect\_debug\_select\_read(void);

205extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arc\_connect\_debug\_en\_read(void);

206extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arc\_connect\_debug\_cmd\_read(void);

207extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arc\_connect\_debug\_core\_read(void);

208

209/\* global free-running counter(gfrc) related functions \*/

210extern void z\_arc\_connect\_gfrc\_clear(void);

211extern [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) z\_arc\_connect\_gfrc\_read(void);

212extern void z\_arc\_connect\_gfrc\_enable(void);

213extern void z\_arc\_connect\_gfrc\_disable(void);

214extern void z\_arc\_connect\_gfrc\_core\_set([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) core\_mask);

215extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arc\_connect\_gfrc\_halt\_read(void);

216extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arc\_connect\_gfrc\_core\_read(void);

217

218/\* interrupt distribute unit related functions \*/

219extern void z\_arc\_connect\_idu\_enable(void);

220extern void z\_arc\_connect\_idu\_disable(void);

221extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arc\_connect\_idu\_read\_enable(void);

222extern void z\_arc\_connect\_idu\_set\_mode([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq\_num,

223 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) trigger\_mode, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) distri\_mode);

224extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arc\_connect\_idu\_read\_mode([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq\_num);

225extern void z\_arc\_connect\_idu\_set\_dest([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq\_num, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) core\_mask);

226extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arc\_connect\_idu\_read\_dest([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq\_num);

227extern void z\_arc\_connect\_idu\_gen\_cirq([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq\_num);

228extern void z\_arc\_connect\_idu\_ack\_cirq([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq\_num);

229extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arc\_connect\_idu\_check\_status([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq\_num);

230extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arc\_connect\_idu\_check\_source([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq\_num);

231extern void z\_arc\_connect\_idu\_set\_mask([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq\_num, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask);

232extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arc\_connect\_idu\_read\_mask([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq\_num);

233extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arc\_connect\_idu\_check\_first([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq\_num);

234

235#ifdef \_\_cplusplus

236}

237#endif

238

239#endif /\* \_ASMLANGUAGE \*/

240

241#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_ARC\_CONNECT\_H\_ \*/

[aux\_regs.h](aux__regs_8h.md)

ARCv2 auxiliary registers definitions.

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[arc\_connect\_bcr](structarc__connect__bcr.md)

**Definition** arc\_connect.h:132

[arc\_connect\_bcr::pw](structarc__connect__bcr.md#a003fa1c240a59c8f71da9db4b9a3479f)

uint32\_t pw

**Definition** arc\_connect.h:144

[arc\_connect\_bcr::val](structarc__connect__bcr.md#a00ec9d596b6b1e508321907e59060f8e)

uint32\_t val

**Definition** arc\_connect.h:149

[arc\_connect\_bcr::idu](structarc__connect__bcr.md#a071473060cc797f07597a4ca045aef45)

uint32\_t idu

**Definition** arc\_connect.h:145

[arc\_connect\_bcr::gfrc](structarc__connect__bcr.md#a0b8c138e13adbdc8b52f1175695de118)

uint32\_t gfrc

**Definition** arc\_connect.h:144

[arc\_connect\_bcr::num\_cores](structarc__connect__bcr.md#a54c7c0f5a72bacf8cd3d75a3cc72e97f)

uint32\_t num\_cores

**Definition** arc\_connect.h:145

[arc\_connect\_bcr::slv](structarc__connect__bcr.md#a64144525d109f4b425b0814352f7e46f)

uint32\_t slv

**Definition** arc\_connect.h:143

[arc\_connect\_bcr::ipi](structarc__connect__bcr.md#a6a6b3eb2c8074cdd860508dbcad455e9)

uint32\_t ipi

**Definition** arc\_connect.h:143

[arc\_connect\_bcr::pw\_dom](structarc__connect__bcr.md#a6b1b8a15f8a0810cfcea6d8dd9be6472)

uint32\_t pw\_dom

**Definition** arc\_connect.h:146

[arc\_connect\_bcr::pad2](structarc__connect__bcr.md#a6c8a939a2f64fb6b3d380ab1307f5e65)

uint32\_t pad2

**Definition** arc\_connect.h:145

[arc\_connect\_bcr::pad](structarc__connect__bcr.md#a6e7ea65b84ff34f654378ffac1e96ec2)

uint32\_t pad

**Definition** arc\_connect.h:144

[arc\_connect\_bcr::msg](structarc__connect__bcr.md#a806d475e167702366f283ce1d8afaa8c)

uint32\_t msg

**Definition** arc\_connect.h:143

[arc\_connect\_bcr::pad4](structarc__connect__bcr.md#a82d4bdda236354afdf404095357fdae9)

uint32\_t pad4

**Definition** arc\_connect.h:146

[arc\_connect\_bcr::pad3](structarc__connect__bcr.md#a88a11fb3a63c29bc3b3aee257dc06a00)

uint32\_t pad3

**Definition** arc\_connect.h:146

[arc\_connect\_bcr::ver](structarc__connect__bcr.md#aba1da6026b038bb551466402c3ee4f14)

uint32\_t ver

**Definition** arc\_connect.h:142

[arc\_connect\_bcr::sem](structarc__connect__bcr.md#acfe524a8fd38e21dd3dce1c58e285f62)

uint32\_t sem

**Definition** arc\_connect.h:143

[arc\_connect\_bcr::dbg](structarc__connect__bcr.md#af2ff782f9553c40f60327b71775501d1)

uint32\_t dbg

**Definition** arc\_connect.h:144

[arc\_connect\_cmd](structarc__connect__cmd.md)

**Definition** arc\_connect.h:119

[arc\_connect\_cmd::param](structarc__connect__cmd.md#a6c03654eda9c5074ea9012cfa8bb18a3)

uint32\_t param

**Definition** arc\_connect.h:125

[arc\_connect\_cmd::cmd](structarc__connect__cmd.md#a83c7cc807f7e5f8593574715cc60fb4d)

uint32\_t cmd

**Definition** arc\_connect.h:125

[arc\_connect\_cmd::val](structarc__connect__cmd.md#afb90551e0d8ad5acb910559dabff1471)

uint32\_t val

**Definition** arc\_connect.h:128

[arc\_connect\_cmd::pad](structarc__connect__cmd.md#afc0086f899ec7e4ea7ae5ea33a6971cf)

uint32\_t pad

**Definition** arc\_connect.h:125

[arc\_connect\_idu\_bcr](structarc__connect__idu__bcr.md)

**Definition** arc\_connect.h:153

[arc\_connect\_idu\_bcr::pad](structarc__connect__idu__bcr.md#a1c6fe3452ad5188cfa778631b3e0af83)

uint32\_t pad

**Definition** arc\_connect.h:159

[arc\_connect\_idu\_bcr::val](structarc__connect__idu__bcr.md#aeef8bbdd06ac006c6f9f910671a993e6)

uint32\_t val

**Definition** arc\_connect.h:162

[arc\_connect\_idu\_bcr::cirqnum](structarc__connect__idu__bcr.md#af812a1c84d91f57915eba4656b2a4204)

uint32\_t cirqnum

**Definition** arc\_connect.h:159

[arc\_connect\_idu\_bcr::ver](structarc__connect__idu__bcr.md#afc8b571a896aa33c6f009fe5a3794058)

uint32\_t ver

**Definition** arc\_connect.h:159

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [arc\_connect.h](arc__connect_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
