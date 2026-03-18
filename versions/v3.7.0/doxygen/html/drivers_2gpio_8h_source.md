---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2gpio_8h_source.html
original_path: doxygen/html/drivers_2gpio_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio.h

[Go to the documentation of this file.](drivers_2gpio_8h.md)

1/\*

2 \* Copyright (c) 2019-2020 Nordic Semiconductor ASA

3 \* Copyright (c) 2019 Piotr Mienkowski

4 \* Copyright (c) 2017 ARM Ltd

5 \* Copyright (c) 2015-2016 Intel Corporation.

6 \*

7 \* SPDX-License-Identifier: Apache-2.0

8 \*/

9

14

15#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_H\_

16#define ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_H\_

17

18#include <[errno.h](errno_8h.md)>

19

20#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

21#include <[zephyr/sys/slist.h](slist_8h.md)>

22

23#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

24#include <stddef.h>

25#include <[zephyr/device.h](device_8h.md)>

26#include <[zephyr/dt-bindings/gpio/gpio.h](dt-bindings_2gpio_2gpio_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

40

45

[ 47](group__gpio__interface.md#ga7be6a0cc9aa65da1d4ee5751b4085853)#define GPIO\_INPUT (1U << 16)

48

[ 50](group__gpio__interface.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)#define GPIO\_OUTPUT (1U << 17)

51

[ 53](group__gpio__interface.md#gaf82306c09450f6933366c4b821db21ed)#define GPIO\_DISCONNECTED 0

54

56

57/\* Initializes output to a low state. \*/

58#define GPIO\_OUTPUT\_INIT\_LOW (1U << 18)

59

60/\* Initializes output to a high state. \*/

61#define GPIO\_OUTPUT\_INIT\_HIGH (1U << 19)

62

63/\* Initializes output based on logic level \*/

64#define GPIO\_OUTPUT\_INIT\_LOGICAL (1U << 20)

65

67

[ 69](group__gpio__interface.md#gaf85baf9f9c1ba554324b4cd7064487b0)#define GPIO\_OUTPUT\_LOW (GPIO\_OUTPUT | GPIO\_OUTPUT\_INIT\_LOW)

[ 71](group__gpio__interface.md#ga10d31f204c0e927017d571352422fb09)#define GPIO\_OUTPUT\_HIGH (GPIO\_OUTPUT | GPIO\_OUTPUT\_INIT\_HIGH)

[ 73](group__gpio__interface.md#ga1e1d6be5f2f788f89468a0ce8b854634)#define GPIO\_OUTPUT\_INACTIVE (GPIO\_OUTPUT | \

74 GPIO\_OUTPUT\_INIT\_LOW | \

75 GPIO\_OUTPUT\_INIT\_LOGICAL)

76

[ 77](group__gpio__interface.md#ga0f5cc126d6a690eb3e303eb29aa718ce)#define GPIO\_OUTPUT\_ACTIVE (GPIO\_OUTPUT | \

78 GPIO\_OUTPUT\_INIT\_HIGH | \

79 GPIO\_OUTPUT\_INIT\_LOGICAL)

80

82

98

[ 100](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a)#define GPIO\_INT\_DISABLE (1U << 21)

101

103

104/\* Enables GPIO pin interrupt. \*/

105#define GPIO\_INT\_ENABLE (1U << 22)

106

107/\* GPIO interrupt is sensitive to logical levels.

108 \*

109 \* This is a component flag that should be combined with other

110 \* `GPIO\_INT\_\*` flags to produce a meaningful configuration.

111 \*/

112#define GPIO\_INT\_LEVELS\_LOGICAL (1U << 23)

113

114/\* GPIO interrupt is edge sensitive.

115 \*

116 \* Note: by default interrupts are level sensitive.

117 \*

118 \* This is a component flag that should be combined with other

119 \* `GPIO\_INT\_\*` flags to produce a meaningful configuration.

120 \*/

121#define GPIO\_INT\_EDGE (1U << 24)

122

123/\* Trigger detection when input state is (or transitions to) physical low or

124 \* logical 0 level.

125 \*

126 \* This is a component flag that should be combined with other

127 \* `GPIO\_INT\_\*` flags to produce a meaningful configuration.

128 \*/

129#define GPIO\_INT\_LOW\_0 (1U << 25)

130

131/\* Trigger detection on input state is (or transitions to) physical high or

132 \* logical 1 level.

133 \*

134 \* This is a component flag that should be combined with other

135 \* `GPIO\_INT\_\*` flags to produce a meaningful configuration.

136 \*/

137#define GPIO\_INT\_HIGH\_1 (1U << 26)

138

139#ifdef CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT

140/\* Disable/Enable interrupt functionality without changing other interrupt

141 \* related register, such as clearing the pending register.

142 \*

143 \* This is a component flag that should be combined with `GPIO\_INT\_ENABLE` or

144 \* `GPIO\_INT\_DISABLE` flags to produce a meaningful configuration.

145 \*/

146#define GPIO\_INT\_ENABLE\_DISABLE\_ONLY (1u << 27)

147#endif /\* CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT \*/

148

149#define GPIO\_INT\_MASK (GPIO\_INT\_DISABLE | \

150 GPIO\_INT\_ENABLE | \

151 GPIO\_INT\_LEVELS\_LOGICAL | \

152 GPIO\_INT\_EDGE | \

153 GPIO\_INT\_LOW\_0 | \

154 GPIO\_INT\_HIGH\_1)

155

157

[ 160](group__gpio__interface.md#gaed642a4e482f73aa917477370d0e241b)#define GPIO\_INT\_EDGE\_RISING (GPIO\_INT\_ENABLE | \

161 GPIO\_INT\_EDGE | \

162 GPIO\_INT\_HIGH\_1)

163

[ 167](group__gpio__interface.md#ga73bed10383a27d4a03feb300e64af8e8)#define GPIO\_INT\_EDGE\_FALLING (GPIO\_INT\_ENABLE | \

168 GPIO\_INT\_EDGE | \

169 GPIO\_INT\_LOW\_0)

170

[ 174](group__gpio__interface.md#ga10fa307ab17d02819108165a09f8e08b)#define GPIO\_INT\_EDGE\_BOTH (GPIO\_INT\_ENABLE | \

175 GPIO\_INT\_EDGE | \

176 GPIO\_INT\_LOW\_0 | \

177 GPIO\_INT\_HIGH\_1)

178

[ 182](group__gpio__interface.md#gaddbb5ad576875af9c2d73b73df55c893)#define GPIO\_INT\_LEVEL\_LOW (GPIO\_INT\_ENABLE | \

183 GPIO\_INT\_LOW\_0)

184

[ 188](group__gpio__interface.md#ga233690d9a6a64bc9f804e3caa6d4a88f)#define GPIO\_INT\_LEVEL\_HIGH (GPIO\_INT\_ENABLE | \

189 GPIO\_INT\_HIGH\_1)

190

[ 194](group__gpio__interface.md#ga7b922529a3cb9396b0d82ca823e9d010)#define GPIO\_INT\_EDGE\_TO\_INACTIVE (GPIO\_INT\_ENABLE | \

195 GPIO\_INT\_LEVELS\_LOGICAL | \

196 GPIO\_INT\_EDGE | \

197 GPIO\_INT\_LOW\_0)

198

[ 202](group__gpio__interface.md#ga35d2ff0e041236d82004a4bb2b5bf634)#define GPIO\_INT\_EDGE\_TO\_ACTIVE (GPIO\_INT\_ENABLE | \

203 GPIO\_INT\_LEVELS\_LOGICAL | \

204 GPIO\_INT\_EDGE | \

205 GPIO\_INT\_HIGH\_1)

206

[ 210](group__gpio__interface.md#gacb9bb1b63f172af2da7eb193e234c4f2)#define GPIO\_INT\_LEVEL\_INACTIVE (GPIO\_INT\_ENABLE | \

211 GPIO\_INT\_LEVELS\_LOGICAL | \

212 GPIO\_INT\_LOW\_0)

213

[ 217](group__gpio__interface.md#gae51c68ff83959994bb942bb253505ca1)#define GPIO\_INT\_LEVEL\_ACTIVE (GPIO\_INT\_ENABLE | \

218 GPIO\_INT\_LEVELS\_LOGICAL | \

219 GPIO\_INT\_HIGH\_1)

220

222

224#define GPIO\_DIR\_MASK (GPIO\_INPUT | GPIO\_OUTPUT)

226

[ 233](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f);

234

[ 246](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693);

247

[ 254](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34);

255

[ 266](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2);

267

[ 274](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e);

275

[ 288](structgpio__dt__spec.md)struct [gpio\_dt\_spec](structgpio__dt__spec.md) {

[ 290](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f) const struct [device](structdevice.md) \*[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f);

[ 292](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84) [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) [pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84);

[ 294](structgpio__dt__spec.md#ae3b90e7e22708798c67da94f72ad1ab0) [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2) [dt\_flags](structgpio__dt__spec.md#ae3b90e7e22708798c67da94f72ad1ab0);

295};

296

[ 331](group__gpio__interface.md#gacb1077b77aecf8f1a9c7636ea583c4cf)#define GPIO\_DT\_SPEC\_GET\_BY\_IDX(node\_id, prop, idx) \

332 { \

333 .port = DEVICE\_DT\_GET(DT\_GPIO\_CTLR\_BY\_IDX(node\_id, prop, idx)),\

334 .pin = DT\_GPIO\_PIN\_BY\_IDX(node\_id, prop, idx), \

335 .dt\_flags = DT\_GPIO\_FLAGS\_BY\_IDX(node\_id, prop, idx), \

336 }

337

[ 355](group__gpio__interface.md#ga3db4fa464e191016287f4c4d7eb9a983)#define GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, prop, idx, default\_value) \

356 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

357 (GPIO\_DT\_SPEC\_GET\_BY\_IDX(node\_id, prop, idx)), \

358 (default\_value))

359

[ 368](group__gpio__interface.md#ga2fa6bb5880f46984f9fc29c70f7d503e)#define GPIO\_DT\_SPEC\_GET(node\_id, prop) \

369 GPIO\_DT\_SPEC\_GET\_BY\_IDX(node\_id, prop, 0)

370

[ 381](group__gpio__interface.md#ga26b2205aa82819df1d80a22761352e71)#define GPIO\_DT\_SPEC\_GET\_OR(node\_id, prop, default\_value) \

382 GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, prop, 0, default\_value)

383

[ 394](group__gpio__interface.md#gabbdbef450f14fd0af73667e2728ad084)#define GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, prop, idx) \

395 GPIO\_DT\_SPEC\_GET\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

396

[ 408](group__gpio__interface.md#gaf07edf6bc88af18e9976c76f6c3c3bf1)#define GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, prop, idx, default\_value) \

409 COND\_CODE\_1(DT\_PROP\_HAS\_IDX(DT\_DRV\_INST(inst), prop, idx), \

410 (GPIO\_DT\_SPEC\_GET\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)), \

411 (default\_value))

412

[ 421](group__gpio__interface.md#ga168f5c6e39a0111191f606a9a0826e89)#define GPIO\_DT\_SPEC\_INST\_GET(inst, prop) \

422 GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, prop, 0)

423

[ 434](group__gpio__interface.md#gae6b4a354c3cf0e042a390aac4bc37c69)#define GPIO\_DT\_SPEC\_INST\_GET\_OR(inst, prop, default\_value) \

435 GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, prop, 0, default\_value)

436

437/\*

438 \* @cond INTERNAL\_HIDDEN

439 \*/

440

451#define Z\_GPIO\_GEN\_BITMASK\_COND(node\_id, prop, off\_idx, sz\_idx) \

452 COND\_CODE\_1(DT\_PROP\_HAS\_IDX(node\_id, prop, off\_idx), \

453 (COND\_CODE\_0(DT\_PROP\_BY\_IDX(node\_id, prop, sz\_idx), \

454 (0), \

455 (GENMASK64(DT\_PROP\_BY\_IDX(node\_id, prop, off\_idx) + \

456 DT\_PROP\_BY\_IDX(node\_id, prop, sz\_idx) - 1, \

457 DT\_PROP\_BY\_IDX(node\_id, prop, off\_idx)))) \

458 ), (0))

459

467#define Z\_GPIO\_GEN\_RESERVED\_RANGES\_COND(odd\_it, node\_id) \

468 COND\_CODE\_1(DT\_PROP\_HAS\_IDX(node\_id, gpio\_reserved\_ranges, odd\_it), \

469 (Z\_GPIO\_GEN\_BITMASK\_COND(node\_id, \

470 gpio\_reserved\_ranges, \

471 GET\_ARG\_N(odd\_it, Z\_SPARSE\_LIST\_EVEN\_NUMBERS), \

472 odd\_it)), \

473 (0))

474

478

[ 566](group__gpio__interface.md#ga439c3d29aa585b00853aba6d6416028a)#define GPIO\_DT\_RESERVED\_RANGES\_NGPIOS(node\_id, ngpios) \

567 ((gpio\_port\_pins\_t) \

568 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, gpio\_reserved\_ranges), \

569 (GENMASK64(BITS\_PER\_LONG\_LONG - 1, ngpios) \

570 | FOR\_EACH\_FIXED\_ARG(Z\_GPIO\_GEN\_RESERVED\_RANGES\_COND, \

571 (|), \

572 node\_id, \

573 LIST\_DROP\_EMPTY(Z\_SPARSE\_LIST\_ODD\_NUMBERS))), \

574 (0)))

575

[ 583](group__gpio__interface.md#ga648fcc0633d57b52d3df683efda98440)#define GPIO\_DT\_RESERVED\_RANGES(node\_id) \

584 GPIO\_DT\_RESERVED\_RANGES\_NGPIOS(node\_id, DT\_PROP(node\_id, ngpios))

585

[ 595](group__gpio__interface.md#gaebaea00f6f7649c61651e8d50c7cdf07)#define GPIO\_DT\_INST\_RESERVED\_RANGES\_NGPIOS(inst, ngpios) \

596 GPIO\_DT\_RESERVED\_RANGES\_NGPIOS(DT\_DRV\_INST(inst), ngpios)

597

[ 606](group__gpio__interface.md#ga9136b467eaddcc734bc6a0a7d8b34e14)#define GPIO\_DT\_INST\_RESERVED\_RANGES(inst) \

607 GPIO\_DT\_RESERVED\_RANGES(DT\_DRV\_INST(inst))

608

[ 657](group__gpio__interface.md#ga274e09d7082d97b2f90c6a7fd4b71d49)#define GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC(node\_id, ngpios) \

658 ((gpio\_port\_pins\_t) \

659 COND\_CODE\_0(ngpios, \

660 (0), \

661 (COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, gpio\_reserved\_ranges), \

662 ((GENMASK64(ngpios - 1, 0) & \

663 ~GPIO\_DT\_RESERVED\_RANGES\_NGPIOS(node\_id, ngpios))), \

664 (GENMASK64(ngpios - 1, 0))) \

665 ) \

666 ))

667

[ 677](group__gpio__interface.md#ga856fe8042e496a39ef3a4e19fff2c4ce)#define GPIO\_DT\_INST\_PORT\_PIN\_MASK\_NGPIOS\_EXC(inst, ngpios) \

678 GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC(DT\_DRV\_INST(inst), ngpios)

679

[ 683](group__gpio__interface.md#ga1449ba90eaec5e6144fe4faae21f2e3f)#define GPIO\_MAX\_PINS\_PER\_PORT (sizeof(gpio\_port\_pins\_t) \* \_\_CHAR\_BIT\_\_)

684

[ 690](structgpio__driver__config.md)struct [gpio\_driver\_config](structgpio__driver__config.md) {

[ 696](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) [port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052);

697};

698

[ 703](structgpio__driver__data.md)struct [gpio\_driver\_data](structgpio__driver__data.md) {

[ 709](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169) [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) [invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169);

710};

711

712struct [gpio\_callback](structgpio__callback.md);

713

[ 726](group__gpio__interface.md#gaf0aa40279d32b1b8332f2f23a39510af)typedef void (\*[gpio\_callback\_handler\_t](group__gpio__interface.md#gaf0aa40279d32b1b8332f2f23a39510af))(const struct [device](structdevice.md) \*port,

727 struct [gpio\_callback](structgpio__callback.md) \*cb,

728 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

729

[ 740](structgpio__callback.md)struct [gpio\_callback](structgpio__callback.md) {

[ 744](structgpio__callback.md#ab60e7093072964bd818d536c746211e4) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structgpio__callback.md#ab60e7093072964bd818d536c746211e4);

745

[ 747](structgpio__callback.md#af89dc41cbd610d81ac03cae7ab764ceb) [gpio\_callback\_handler\_t](group__gpio__interface.md#gaf0aa40279d32b1b8332f2f23a39510af) [handler](structgpio__callback.md#af89dc41cbd610d81ac03cae7ab764ceb);

748

[ 755](structgpio__callback.md#ace5c2b83f1d51f73877a1f2c54ba8c67) [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) [pin\_mask](structgpio__callback.md#ace5c2b83f1d51f73877a1f2c54ba8c67);

756};

757

763

764/\* Used by driver api function pin\_interrupt\_configure, these are defined

765 \* in terms of the public flags so we can just mask and pass them

766 \* through to the driver api

767 \*/

768enum gpio\_int\_mode {

769 GPIO\_INT\_MODE\_DISABLED = [GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a),

770 GPIO\_INT\_MODE\_LEVEL = GPIO\_INT\_ENABLE,

771 GPIO\_INT\_MODE\_EDGE = GPIO\_INT\_ENABLE | GPIO\_INT\_EDGE,

772#ifdef CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT

773 GPIO\_INT\_MODE\_DISABLE\_ONLY = [GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a) | GPIO\_INT\_ENABLE\_DISABLE\_ONLY,

774 GPIO\_INT\_MODE\_ENABLE\_ONLY = GPIO\_INT\_ENABLE | GPIO\_INT\_ENABLE\_DISABLE\_ONLY,

775#endif /\* CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT \*/

776};

777

778enum gpio\_int\_trig {

779 /\* Trigger detection when input state is (or transitions to)

780 \* physical low. (Edge Falling or Active Low)

781 \*/

782 GPIO\_INT\_TRIG\_LOW = GPIO\_INT\_LOW\_0,

783 /\* Trigger detection when input state is (or transitions to)

784 \* physical high. (Edge Rising or Active High) \*/

785 GPIO\_INT\_TRIG\_HIGH = GPIO\_INT\_HIGH\_1,

786 /\* Trigger detection on pin rising or falling edge. \*/

787 GPIO\_INT\_TRIG\_BOTH = GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1,

788 /\* Trigger a system wakeup. \*/

789 GPIO\_INT\_TRIG\_WAKE = [GPIO\_INT\_WAKEUP](group__gpio__interface.md#ga644109ce84c8feffe1226b9b50122a96),

790};

791

792\_\_subsystem struct gpio\_driver\_api {

793 int (\*pin\_configure)(const struct device \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

794 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

795#ifdef CONFIG\_GPIO\_GET\_CONFIG

796 int (\*pin\_get\_config)(const struct device \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

797 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

798#endif

799 int (\*port\_get\_raw)(const struct device \*port,

800 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value);

801 int (\*port\_set\_masked\_raw)(const struct device \*port,

802 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask,

803 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value);

804 int (\*port\_set\_bits\_raw)(const struct device \*port,

805 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

806 int (\*port\_clear\_bits\_raw)(const struct device \*port,

807 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

808 int (\*port\_toggle\_bits)(const struct device \*port,

809 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

810 int (\*pin\_interrupt\_configure)(const struct device \*port,

811 [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

812 enum gpio\_int\_mode, enum gpio\_int\_trig);

813 int (\*manage\_callback)(const struct device \*port,

814 struct gpio\_callback \*cb,

815 bool set);

816 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*get\_pending\_int)(const struct device \*dev);

817#ifdef CONFIG\_GPIO\_GET\_DIRECTION

818 int (\*port\_get\_direction)(const struct device \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) map,

819 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*inputs, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*outputs);

820#endif /\* CONFIG\_GPIO\_GET\_DIRECTION \*/

821};

822

826

[ 835](group__gpio__interface.md#gaaec9ad17c08a0d527d66445fe82d8327)static inline bool [gpio\_is\_ready\_dt](group__gpio__interface.md#gaaec9ad17c08a0d527d66445fe82d8327)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec)

836{

837 /\* Validate port is ready \*/

838 return [device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f));

839}

840

[ 862](group__gpio__interface.md#ga9618f254365381063439a0e9c5e787cb)\_\_syscall int [gpio\_pin\_interrupt\_configure](group__gpio__interface.md#ga9618f254365381063439a0e9c5e787cb)(const struct [device](structdevice.md) \*port,

863 [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

864 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

865

866static inline int z\_impl\_gpio\_pin\_interrupt\_configure(const struct [device](structdevice.md) \*port,

867 [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

868 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

869{

870 const struct gpio\_driver\_api \*api =

871 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

872 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

873 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

874 const struct [gpio\_driver\_data](structgpio__driver__data.md) \*const data =

875 (const struct [gpio\_driver\_data](structgpio__driver__data.md) \*)port->data;

876 enum gpio\_int\_trig trig;

877 enum gpio\_int\_mode mode;

878

879 if (api->pin\_interrupt\_configure == NULL) {

880 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

881 }

882

883 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & ([GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a) | GPIO\_INT\_ENABLE))

884 != ([GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a) | GPIO\_INT\_ENABLE),

885 "Cannot both enable and disable interrupts");

886

887 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & ([GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a) | GPIO\_INT\_ENABLE)) != 0U,

888 "Must either enable or disable interrupts");

889

890 \_\_ASSERT((([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_INT\_ENABLE) == 0) ||

891 (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_INT\_EDGE) != 0) ||

892 (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1)) !=

893 (GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1)),

894 "Only one of GPIO\_INT\_LOW\_0, GPIO\_INT\_HIGH\_1 can be "

895 "enabled for a level interrupt.");

896

897 \_\_ASSERT((([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_INT\_ENABLE) == 0) ||

898#ifdef CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT

899 (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1)) != 0) ||

900 ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_INT\_ENABLE\_DISABLE\_ONLY) != 0,

901#else

902 (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1)) != 0),

903#endif /\* CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT \*/

904 "At least one of GPIO\_INT\_LOW\_0, GPIO\_INT\_HIGH\_1 has to be "

905 "enabled.");

906

907 \_\_ASSERT((cfg->port\_pin\_mask & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

908 "Unsupported pin");

909

910 if ((([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_INT\_LEVELS\_LOGICAL) != 0) &&

911 ((data->[invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0)) {

912 /\* Invert signal bits \*/

913 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) ^= (GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1);

914 }

915

916 trig = (enum gpio\_int\_trig)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1 | [GPIO\_INT\_WAKEUP](group__gpio__interface.md#ga644109ce84c8feffe1226b9b50122a96)));

917#ifdef CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT

918 mode = (enum gpio\_int\_mode)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_INT\_EDGE | [GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a) | GPIO\_INT\_ENABLE |

919 GPIO\_INT\_ENABLE\_DISABLE\_ONLY));

920#else

921 mode = (enum gpio\_int\_mode)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_INT\_EDGE | [GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a) | GPIO\_INT\_ENABLE));

922#endif /\* CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT \*/

923

924 return api->pin\_interrupt\_configure(port, pin, mode, trig);

925}

926

[ 940](group__gpio__interface.md#ga24f0b4ad30e6a8c81f51a2813478c793)static inline int [gpio\_pin\_interrupt\_configure\_dt](group__gpio__interface.md#ga24f0b4ad30e6a8c81f51a2813478c793)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec,

941 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

942{

943 return [gpio\_pin\_interrupt\_configure](group__gpio__interface.md#ga9618f254365381063439a0e9c5e787cb)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84), [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

944}

945

[ 961](group__gpio__interface.md#gaed4a2051d76db7eead8ed1719ce2ba33)\_\_syscall int [gpio\_pin\_configure](group__gpio__interface.md#gaed4a2051d76db7eead8ed1719ce2ba33)(const struct [device](structdevice.md) \*port,

962 [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

963 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

964

965static inline int z\_impl\_gpio\_pin\_configure(const struct [device](structdevice.md) \*port,

966 [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

967 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

968{

969 const struct gpio\_driver\_api \*api =

970 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

971 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

972 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->config;

973 struct [gpio\_driver\_data](structgpio__driver__data.md) \*data =

974 (struct [gpio\_driver\_data](structgpio__driver__data.md) \*)port->data;

975

976 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_INT\_MASK) == 0,

977 "Interrupt flags are not supported");

978

979 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & ([GPIO\_PULL\_UP](group__gpio__interface.md#gaaa7921da231fd2b96575fa522e2c1970) | [GPIO\_PULL\_DOWN](group__gpio__interface.md#gadec1802e074f3021d464da09cd66c7cf))) !=

980 ([GPIO\_PULL\_UP](group__gpio__interface.md#gaaa7921da231fd2b96575fa522e2c1970) | [GPIO\_PULL\_DOWN](group__gpio__interface.md#gadec1802e074f3021d464da09cd66c7cf)),

981 "Pull Up and Pull Down should not be enabled simultaneously");

982

983 \_\_ASSERT(!(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & [GPIO\_INPUT](group__gpio__interface.md#ga7be6a0cc9aa65da1d4ee5751b4085853)) && !([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & [GPIO\_OUTPUT](group__gpio__interface.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)) && ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_SINGLE\_ENDED)),

984 "Input cannot be enabled for 'Open Drain', 'Open Source' modes without Output");

985

986 \_\_ASSERT\_NO\_MSG(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_SINGLE\_ENDED) != 0 ||

987 ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_LINE\_OPEN\_DRAIN) == 0);

988

989 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_OUTPUT\_INIT\_LOW | GPIO\_OUTPUT\_INIT\_HIGH)) == 0

990 || ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & [GPIO\_OUTPUT](group__gpio__interface.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)) != 0,

991 "Output needs to be enabled to be initialized low or high");

992

993 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_OUTPUT\_INIT\_LOW | GPIO\_OUTPUT\_INIT\_HIGH))

994 != (GPIO\_OUTPUT\_INIT\_LOW | GPIO\_OUTPUT\_INIT\_HIGH),

995 "Output cannot be initialized low and high");

996

997 if ((([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_OUTPUT\_INIT\_LOGICAL) != 0)

998 && (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_OUTPUT\_INIT\_LOW | GPIO\_OUTPUT\_INIT\_HIGH)) != 0)

999 && (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & [GPIO\_ACTIVE\_LOW](group__gpio__interface.md#ga62cea8989df2425e5e5e712217d65f46)) != 0)) {

1000 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) ^= GPIO\_OUTPUT\_INIT\_LOW | GPIO\_OUTPUT\_INIT\_HIGH;

1001 }

1002

1003 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) &= ~GPIO\_OUTPUT\_INIT\_LOGICAL;

1004

1005 \_\_ASSERT((cfg->port\_pin\_mask & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

1006 "Unsupported pin");

1007

1008 if (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & [GPIO\_ACTIVE\_LOW](group__gpio__interface.md#ga62cea8989df2425e5e5e712217d65f46)) != 0) {

1009 data->[invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169) |= ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin);

1010 } else {

1011 data->[invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169) &= ~([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin);

1012 }

1013

1014 return api->pin\_configure(port, pin, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

1015}

1016

[ 1028](group__gpio__interface.md#ga423db4f985098ddcaa504ec430e91913)static inline int [gpio\_pin\_configure\_dt](group__gpio__interface.md#ga423db4f985098ddcaa504ec430e91913)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec,

1029 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) extra\_flags)

1030{

1031 return [gpio\_pin\_configure](group__gpio__interface.md#gaed4a2051d76db7eead8ed1719ce2ba33)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f),

1032 spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84),

1033 spec->[dt\_flags](structgpio__dt__spec.md#ae3b90e7e22708798c67da94f72ad1ab0) | extra\_flags);

1034}

1035

[ 1054](group__gpio__interface.md#gad2b2945dbe6987ac425e000721a894c4)\_\_syscall int [gpio\_port\_get\_direction](group__gpio__interface.md#gad2b2945dbe6987ac425e000721a894c4)(const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) map,

1055 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*inputs, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*outputs);

1056

1057#ifdef CONFIG\_GPIO\_GET\_DIRECTION

1058static inline int z\_impl\_gpio\_port\_get\_direction(const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) map,

1059 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*inputs,

1060 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*outputs)

1061{

1062 const struct gpio\_driver\_api \*api = (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1063

1064 if (api->port\_get\_direction == NULL) {

1065 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1066 }

1067

1068 return api->port\_get\_direction(port, map, inputs, outputs);

1069}

1070#endif /\* CONFIG\_GPIO\_GET\_DIRECTION \*/

1071

[ 1084](group__gpio__interface.md#ga1454bc223fc2200aff3c4aab7d747da2)static inline int [gpio\_pin\_is\_input](group__gpio__interface.md#ga1454bc223fc2200aff3c4aab7d747da2)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin)

1085{

1086 int rv;

1087 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins;

1088 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*cfg =

1089 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1090

1091 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U, "Unsupported pin");

1092

1093 rv = [gpio\_port\_get\_direction](group__gpio__interface.md#gad2b2945dbe6987ac425e000721a894c4)(port, [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin), &pins, NULL);

1094 if (rv < 0) {

1095 return rv;

1096 }

1097

1098 return (int)!!(([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin) & pins);

1099}

1100

[ 1112](group__gpio__interface.md#ga7aaec28a83cac63bd87fc94cc72664b1)static inline int [gpio\_pin\_is\_input\_dt](group__gpio__interface.md#ga7aaec28a83cac63bd87fc94cc72664b1)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec)

1113{

1114 return [gpio\_pin\_is\_input](group__gpio__interface.md#ga1454bc223fc2200aff3c4aab7d747da2)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84));

1115}

1116

[ 1129](group__gpio__interface.md#ga3b854d759180e222299ea445b401acc1)static inline int [gpio\_pin\_is\_output](group__gpio__interface.md#ga3b854d759180e222299ea445b401acc1)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin)

1130{

1131 int rv;

1132 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins;

1133 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*cfg =

1134 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1135

1136 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U, "Unsupported pin");

1137

1138 rv = [gpio\_port\_get\_direction](group__gpio__interface.md#gad2b2945dbe6987ac425e000721a894c4)(port, [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin), NULL, &pins);

1139 if (rv < 0) {

1140 return rv;

1141 }

1142

1143 return (int)!!(([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin) & pins);

1144}

1145

[ 1157](group__gpio__interface.md#ga2255c5681d17952ab89a4b6016d8e80d)static inline int [gpio\_pin\_is\_output\_dt](group__gpio__interface.md#ga2255c5681d17952ab89a4b6016d8e80d)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec)

1158{

1159 return [gpio\_pin\_is\_output](group__gpio__interface.md#ga3b854d759180e222299ea445b401acc1)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84));

1160}

1161

[ 1177](group__gpio__interface.md#ga133284b60a13c6dc50b87c1d04259f5e)\_\_syscall int [gpio\_pin\_get\_config](group__gpio__interface.md#ga133284b60a13c6dc50b87c1d04259f5e)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

1178 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

1179

1180#ifdef CONFIG\_GPIO\_GET\_CONFIG

1181static inline int z\_impl\_gpio\_pin\_get\_config(const struct [device](structdevice.md) \*port,

1182 [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

1183 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

1184{

1185 const struct gpio\_driver\_api \*api =

1186 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1187

1188 if (api->pin\_get\_config == NULL)

1189 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1190

1191 return api->pin\_get\_config(port, pin, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

1192}

1193#endif

1194

[ 1207](group__gpio__interface.md#ga820448aa4be8b14839bc6a00c9f34bb4)static inline int [gpio\_pin\_get\_config\_dt](group__gpio__interface.md#ga820448aa4be8b14839bc6a00c9f34bb4)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec,

1208 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

1209{

1210 return [gpio\_pin\_get\_config](group__gpio__interface.md#ga133284b60a13c6dc50b87c1d04259f5e)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84), [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

1211}

1212

[ 1230](group__gpio__interface.md#gae2a49b36cae2e17fc665a3bd844f50b4)\_\_syscall int [gpio\_port\_get\_raw](group__gpio__interface.md#gae2a49b36cae2e17fc665a3bd844f50b4)(const struct [device](structdevice.md) \*port,

1231 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value);

1232

1233static inline int z\_impl\_gpio\_port\_get\_raw(const struct [device](structdevice.md) \*port,

1234 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value)

1235{

1236 const struct gpio\_driver\_api \*api =

1237 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1238

1239 return api->port\_get\_raw(port, value);

1240}

1241

[ 1260](group__gpio__interface.md#gae578c8163fb8fe5600d1ca9e5d7526b1)static inline int [gpio\_port\_get](group__gpio__interface.md#gae578c8163fb8fe5600d1ca9e5d7526b1)(const struct [device](structdevice.md) \*port,

1261 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value)

1262{

1263 const struct [gpio\_driver\_data](structgpio__driver__data.md) \*const data =

1264 (const struct [gpio\_driver\_data](structgpio__driver__data.md) \*)port->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

1265 int ret;

1266

1267 ret = [gpio\_port\_get\_raw](group__gpio__interface.md#gae2a49b36cae2e17fc665a3bd844f50b4)(port, value);

1268 if (ret == 0) {

1269 \*value ^= data->[invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169);

1270 }

1271

1272 return ret;

1273}

1274

[ 1292](group__gpio__interface.md#ga9e7b50d720fda362941acc1e3b3b2922)\_\_syscall int [gpio\_port\_set\_masked\_raw](group__gpio__interface.md#ga9e7b50d720fda362941acc1e3b3b2922)(const struct [device](structdevice.md) \*port,

1293 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask,

1294 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value);

1295

1296static inline int z\_impl\_gpio\_port\_set\_masked\_raw(const struct [device](structdevice.md) \*port,

1297 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask,

1298 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value)

1299{

1300 const struct gpio\_driver\_api \*api =

1301 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1302

1303 return api->port\_set\_masked\_raw(port, mask, value);

1304}

1305

[ 1326](group__gpio__interface.md#gac653e70270019d599732ab78693dd1fd)static inline int [gpio\_port\_set\_masked](group__gpio__interface.md#gac653e70270019d599732ab78693dd1fd)(const struct [device](structdevice.md) \*port,

1327 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask,

1328 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value)

1329{

1330 const struct [gpio\_driver\_data](structgpio__driver__data.md) \*const data =

1331 (const struct [gpio\_driver\_data](structgpio__driver__data.md) \*)port->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

1332

1333 value ^= data->[invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169);

1334

1335 return [gpio\_port\_set\_masked\_raw](group__gpio__interface.md#ga9e7b50d720fda362941acc1e3b3b2922)(port, mask, value);

1336}

1337

[ 1348](group__gpio__interface.md#ga18e6ca0df95566fecc0633efb04a075a)\_\_syscall int [gpio\_port\_set\_bits\_raw](group__gpio__interface.md#ga18e6ca0df95566fecc0633efb04a075a)(const struct [device](structdevice.md) \*port,

1349 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

1350

1351static inline int z\_impl\_gpio\_port\_set\_bits\_raw(const struct [device](structdevice.md) \*port,

1352 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins)

1353{

1354 const struct gpio\_driver\_api \*api =

1355 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1356

1357 return api->port\_set\_bits\_raw(port, pins);

1358}

1359

[ 1370](group__gpio__interface.md#ga570b669af237df991c4a55cff6ec3253)static inline int [gpio\_port\_set\_bits](group__gpio__interface.md#ga570b669af237df991c4a55cff6ec3253)(const struct [device](structdevice.md) \*port,

1371 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins)

1372{

1373 return [gpio\_port\_set\_masked](group__gpio__interface.md#gac653e70270019d599732ab78693dd1fd)(port, pins, pins);

1374}

1375

[ 1386](group__gpio__interface.md#ga9d2c9daeec7ce127fc786ead566ad27f)\_\_syscall int [gpio\_port\_clear\_bits\_raw](group__gpio__interface.md#ga9d2c9daeec7ce127fc786ead566ad27f)(const struct [device](structdevice.md) \*port,

1387 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

1388

1389static inline int z\_impl\_gpio\_port\_clear\_bits\_raw(const struct [device](structdevice.md) \*port,

1390 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins)

1391{

1392 const struct gpio\_driver\_api \*api =

1393 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1394

1395 return api->port\_clear\_bits\_raw(port, pins);

1396}

1397

[ 1408](group__gpio__interface.md#gac1660707a44cc8a3aa08b25685b4b20b)static inline int [gpio\_port\_clear\_bits](group__gpio__interface.md#gac1660707a44cc8a3aa08b25685b4b20b)(const struct [device](structdevice.md) \*port,

1409 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins)

1410{

1411 return [gpio\_port\_set\_masked](group__gpio__interface.md#gac653e70270019d599732ab78693dd1fd)(port, pins, 0);

1412}

1413

[ 1424](group__gpio__interface.md#ga82977d8706fb9f464db455bd0e9ac2e4)\_\_syscall int [gpio\_port\_toggle\_bits](group__gpio__interface.md#ga82977d8706fb9f464db455bd0e9ac2e4)(const struct [device](structdevice.md) \*port,

1425 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

1426

1427static inline int z\_impl\_gpio\_port\_toggle\_bits(const struct [device](structdevice.md) \*port,

1428 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins)

1429{

1430 const struct gpio\_driver\_api \*api =

1431 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1432

1433 return api->port\_toggle\_bits(port, pins);

1434}

1435

[ 1447](group__gpio__interface.md#ga6e7ca22e83a70d3ddcf0de068b377c2d)static inline int [gpio\_port\_set\_clr\_bits\_raw](group__gpio__interface.md#ga6e7ca22e83a70d3ddcf0de068b377c2d)(const struct [device](structdevice.md) \*port,

1448 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) set\_pins,

1449 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) clear\_pins)

1450{

1451 \_\_ASSERT((set\_pins & clear\_pins) == 0, "Set and Clear pins overlap");

1452

1453 return [gpio\_port\_set\_masked\_raw](group__gpio__interface.md#ga9e7b50d720fda362941acc1e3b3b2922)(port, set\_pins | clear\_pins, set\_pins);

1454}

1455

[ 1467](group__gpio__interface.md#ga77880d217f5dd1fc1c72ce791254449b)static inline int [gpio\_port\_set\_clr\_bits](group__gpio__interface.md#ga77880d217f5dd1fc1c72ce791254449b)(const struct [device](structdevice.md) \*port,

1468 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) set\_pins,

1469 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) clear\_pins)

1470{

1471 \_\_ASSERT((set\_pins & clear\_pins) == 0, "Set and Clear pins overlap");

1472

1473 return [gpio\_port\_set\_masked](group__gpio__interface.md#gac653e70270019d599732ab78693dd1fd)(port, set\_pins | clear\_pins, set\_pins);

1474}

1475

[ 1491](group__gpio__interface.md#ga0fc52723b78019258bb306c771c430a1)static inline int [gpio\_pin\_get\_raw](group__gpio__interface.md#ga0fc52723b78019258bb306c771c430a1)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin)

1492{

1493 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

1494 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1495 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value;

1496 int ret;

1497

1498 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

1499 "Unsupported pin");

1500

1501 ret = [gpio\_port\_get\_raw](group__gpio__interface.md#gae2a49b36cae2e17fc665a3bd844f50b4)(port, &value);

1502 if (ret == 0) {

1503 ret = (value & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0 ? 1 : 0;

1504 }

1505

1506 return ret;

1507}

1508

[ 1528](group__gpio__interface.md#ga154a4ea3d3084910f02df31dc0779be6)static inline int [gpio\_pin\_get](group__gpio__interface.md#ga154a4ea3d3084910f02df31dc0779be6)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin)

1529{

1530 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

1531 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1532 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value;

1533 int ret;

1534

1535 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

1536 "Unsupported pin");

1537

1538 ret = [gpio\_port\_get](group__gpio__interface.md#gae578c8163fb8fe5600d1ca9e5d7526b1)(port, &value);

1539 if (ret == 0) {

1540 ret = (value & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0 ? 1 : 0;

1541 }

1542

1543 return ret;

1544}

1545

[ 1556](group__gpio__interface.md#gaabeb2d0d98856c7ff78be36651d6bbc1)static inline int [gpio\_pin\_get\_dt](group__gpio__interface.md#gaabeb2d0d98856c7ff78be36651d6bbc1)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec)

1557{

1558 return [gpio\_pin\_get](group__gpio__interface.md#ga154a4ea3d3084910f02df31dc0779be6)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84));

1559}

1560

[ 1576](group__gpio__interface.md#gae28f0fa2576530083aa86d819d0d5cca)static inline int [gpio\_pin\_set\_raw](group__gpio__interface.md#gae28f0fa2576530083aa86d819d0d5cca)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

1577 int value)

1578{

1579 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

1580 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1581 int ret;

1582

1583 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

1584 "Unsupported pin");

1585

1586 if (value != 0) {

1587 ret = [gpio\_port\_set\_bits\_raw](group__gpio__interface.md#ga18e6ca0df95566fecc0633efb04a075a)(port, ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin));

1588 } else {

1589 ret = [gpio\_port\_clear\_bits\_raw](group__gpio__interface.md#ga9d2c9daeec7ce127fc786ead566ad27f)(port, ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin));

1590 }

1591

1592 return ret;

1593}

1594

[ 1616](group__gpio__interface.md#gabfab69282fb99be119760436f2d18a9b)static inline int [gpio\_pin\_set](group__gpio__interface.md#gabfab69282fb99be119760436f2d18a9b)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

1617 int value)

1618{

1619 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

1620 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1621 const struct [gpio\_driver\_data](structgpio__driver__data.md) \*const data =

1622 (const struct [gpio\_driver\_data](structgpio__driver__data.md) \*)port->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

1623

1624 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

1625 "Unsupported pin");

1626

1627 if (data->[invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) {

1628 value = (value != 0) ? 0 : 1;

1629 }

1630

1631 return [gpio\_pin\_set\_raw](group__gpio__interface.md#gae28f0fa2576530083aa86d819d0d5cca)(port, pin, value);

1632}

1633

[ 1645](group__gpio__interface.md#ga541064fb9e575c0c559c101754466fa8)static inline int [gpio\_pin\_set\_dt](group__gpio__interface.md#ga541064fb9e575c0c559c101754466fa8)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec, int value)

1646{

1647 return [gpio\_pin\_set](group__gpio__interface.md#gabfab69282fb99be119760436f2d18a9b)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84), value);

1648}

1649

[ 1660](group__gpio__interface.md#gaabf948471d313ff19410f1741dd16957)static inline int [gpio\_pin\_toggle](group__gpio__interface.md#gaabf948471d313ff19410f1741dd16957)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin)

1661{

1662 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

1663 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1664

1665 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

1666 "Unsupported pin");

1667

1668 return [gpio\_port\_toggle\_bits](group__gpio__interface.md#ga82977d8706fb9f464db455bd0e9ac2e4)(port, ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin));

1669}

1670

[ 1681](group__gpio__interface.md#ga3272e866489da6c2e12c48f803c59e81)static inline int [gpio\_pin\_toggle\_dt](group__gpio__interface.md#ga3272e866489da6c2e12c48f803c59e81)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec)

1682{

1683 return [gpio\_pin\_toggle](group__gpio__interface.md#gaabf948471d313ff19410f1741dd16957)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84));

1684}

1685

[ 1692](group__gpio__interface.md#ga7a7dd7c1f3a2135a9f378e1c34b6232c)static inline void [gpio\_init\_callback](group__gpio__interface.md#ga7a7dd7c1f3a2135a9f378e1c34b6232c)(struct [gpio\_callback](structgpio__callback.md) \*callback,

1693 [gpio\_callback\_handler\_t](group__gpio__interface.md#gaf0aa40279d32b1b8332f2f23a39510af) handler,

1694 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pin\_mask)

1695{

1696 \_\_ASSERT(callback, "Callback pointer should not be NULL");

1697 \_\_ASSERT(handler, "Callback handler pointer should not be NULL");

1698

1699 callback->[handler](structgpio__callback.md#af89dc41cbd610d81ac03cae7ab764ceb) = handler;

1700 callback->[pin\_mask](structgpio__callback.md#ace5c2b83f1d51f73877a1f2c54ba8c67) = pin\_mask;

1701}

1702

[ 1717](group__gpio__interface.md#ga05fd15af20386d69f9332354285b0cca)static inline int [gpio\_add\_callback](group__gpio__interface.md#ga05fd15af20386d69f9332354285b0cca)(const struct [device](structdevice.md) \*port,

1718 struct [gpio\_callback](structgpio__callback.md) \*callback)

1719{

1720 const struct gpio\_driver\_api \*api =

1721 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1722

1723 if (api->manage\_callback == NULL) {

1724 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1725 }

1726

1727 return api->manage\_callback(port, callback, true);

1728}

1729

[ 1741](group__gpio__interface.md#ga54845eb95bc9636c3e6ff285300b6979)static inline int [gpio\_add\_callback\_dt](group__gpio__interface.md#ga54845eb95bc9636c3e6ff285300b6979)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec,

1742 struct [gpio\_callback](structgpio__callback.md) \*callback)

1743{

1744 return [gpio\_add\_callback](group__gpio__interface.md#ga05fd15af20386d69f9332354285b0cca)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), callback);

1745}

1746

[ 1765](group__gpio__interface.md#gac1e94ba8faac79f469447e9b5d2f8c06)static inline int [gpio\_remove\_callback](group__gpio__interface.md#gac1e94ba8faac79f469447e9b5d2f8c06)(const struct [device](structdevice.md) \*port,

1766 struct [gpio\_callback](structgpio__callback.md) \*callback)

1767{

1768 const struct gpio\_driver\_api \*api =

1769 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1770

1771 if (api->manage\_callback == NULL) {

1772 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1773 }

1774

1775 return api->manage\_callback(port, callback, false);

1776}

1777

[ 1789](group__gpio__interface.md#ga2c9f8fee2addfc0aeeeeb011d534f304)static inline int [gpio\_remove\_callback\_dt](group__gpio__interface.md#ga2c9f8fee2addfc0aeeeeb011d534f304)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec,

1790 struct [gpio\_callback](structgpio__callback.md) \*callback)

1791{

1792 return [gpio\_remove\_callback](group__gpio__interface.md#gac1e94ba8faac79f469447e9b5d2f8c06)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), callback);

1793}

1794

[ 1809](group__gpio__interface.md#ga3f9e45de172a27f49c31a072c0c241e1)\_\_syscall int [gpio\_get\_pending\_int](group__gpio__interface.md#ga3f9e45de172a27f49c31a072c0c241e1)(const struct [device](structdevice.md) \*dev);

1810

1811static inline int z\_impl\_gpio\_get\_pending\_int(const struct [device](structdevice.md) \*dev)

1812{

1813 const struct gpio\_driver\_api \*api =

1814 (const struct gpio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1815

1816 if (api->get\_pending\_int == NULL) {

1817 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1818 }

1819

1820 return api->get\_pending\_int(dev);

1821}

1822

1826

1827#ifdef \_\_cplusplus

1828}

1829#endif

1830

1831#include <zephyr/syscalls/gpio.h>

1832

1833#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[device.h](device_8h.md)

[gpio.h](dt-bindings_2gpio_2gpio_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)

bool device\_is\_ready(const struct device \*dev)

Verify that a device is ready for use.

[gpio\_add\_callback](group__gpio__interface.md#ga05fd15af20386d69f9332354285b0cca)

static int gpio\_add\_callback(const struct device \*port, struct gpio\_callback \*callback)

Add an application callback.

**Definition** gpio.h:1717

[GPIO\_OUTPUT](group__gpio__interface.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)

#define GPIO\_OUTPUT

Enables pin as output, no change to the output state.

**Definition** gpio.h:50

[gpio\_pin\_get\_raw](group__gpio__interface.md#ga0fc52723b78019258bb306c771c430a1)

static int gpio\_pin\_get\_raw(const struct device \*port, gpio\_pin\_t pin)

Get physical level of an input pin.

**Definition** gpio.h:1491

[gpio\_pin\_get\_config](group__gpio__interface.md#ga133284b60a13c6dc50b87c1d04259f5e)

int gpio\_pin\_get\_config(const struct device \*port, gpio\_pin\_t pin, gpio\_flags\_t \*flags)

Get a configuration of a single pin.

[gpio\_pin\_is\_input](group__gpio__interface.md#ga1454bc223fc2200aff3c4aab7d747da2)

static int gpio\_pin\_is\_input(const struct device \*port, gpio\_pin\_t pin)

Check if pin is configured for input.

**Definition** gpio.h:1084

[gpio\_pin\_get](group__gpio__interface.md#ga154a4ea3d3084910f02df31dc0779be6)

static int gpio\_pin\_get(const struct device \*port, gpio\_pin\_t pin)

Get logical level of an input pin.

**Definition** gpio.h:1528

[gpio\_port\_set\_bits\_raw](group__gpio__interface.md#ga18e6ca0df95566fecc0633efb04a075a)

int gpio\_port\_set\_bits\_raw(const struct device \*port, gpio\_port\_pins\_t pins)

Set physical level of selected output pins to high.

[gpio\_pin\_is\_output\_dt](group__gpio__interface.md#ga2255c5681d17952ab89a4b6016d8e80d)

static int gpio\_pin\_is\_output\_dt(const struct gpio\_dt\_spec \*spec)

Check if a single pin from gpio\_dt\_spec is configured for output.

**Definition** gpio.h:1157

[gpio\_pin\_interrupt\_configure\_dt](group__gpio__interface.md#ga24f0b4ad30e6a8c81f51a2813478c793)

static int gpio\_pin\_interrupt\_configure\_dt(const struct gpio\_dt\_spec \*spec, gpio\_flags\_t flags)

Configure pin interrupts from a gpio\_dt\_spec.

**Definition** gpio.h:940

[gpio\_remove\_callback\_dt](group__gpio__interface.md#ga2c9f8fee2addfc0aeeeeb011d534f304)

static int gpio\_remove\_callback\_dt(const struct gpio\_dt\_spec \*spec, struct gpio\_callback \*callback)

Remove an application callback.

**Definition** gpio.h:1789

[gpio\_pin\_toggle\_dt](group__gpio__interface.md#ga3272e866489da6c2e12c48f803c59e81)

static int gpio\_pin\_toggle\_dt(const struct gpio\_dt\_spec \*spec)

Toggle pin level from a gpio\_dt\_spec.

**Definition** gpio.h:1681

[gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34)

uint8\_t gpio\_pin\_t

Provides a type to hold a GPIO pin index.

**Definition** gpio.h:254

[gpio\_pin\_is\_output](group__gpio__interface.md#ga3b854d759180e222299ea445b401acc1)

static int gpio\_pin\_is\_output(const struct device \*port, gpio\_pin\_t pin)

Check if pin is configured for output.

**Definition** gpio.h:1129

[gpio\_get\_pending\_int](group__gpio__interface.md#ga3f9e45de172a27f49c31a072c0c241e1)

int gpio\_get\_pending\_int(const struct device \*dev)

Function to get pending interrupts.

[gpio\_pin\_configure\_dt](group__gpio__interface.md#ga423db4f985098ddcaa504ec430e91913)

static int gpio\_pin\_configure\_dt(const struct gpio\_dt\_spec \*spec, gpio\_flags\_t extra\_flags)

Configure a single pin from a gpio\_dt\_spec and some extra flags.

**Definition** gpio.h:1028

[gpio\_pin\_set\_dt](group__gpio__interface.md#ga541064fb9e575c0c559c101754466fa8)

static int gpio\_pin\_set\_dt(const struct gpio\_dt\_spec \*spec, int value)

Set logical level of a output pin from a gpio\_dt\_spec.

**Definition** gpio.h:1645

[gpio\_add\_callback\_dt](group__gpio__interface.md#ga54845eb95bc9636c3e6ff285300b6979)

static int gpio\_add\_callback\_dt(const struct gpio\_dt\_spec \*spec, struct gpio\_callback \*callback)

Add an application callback.

**Definition** gpio.h:1741

[gpio\_port\_set\_bits](group__gpio__interface.md#ga570b669af237df991c4a55cff6ec3253)

static int gpio\_port\_set\_bits(const struct device \*port, gpio\_port\_pins\_t pins)

Set logical level of selected output pins to active.

**Definition** gpio.h:1370

[gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e)

uint32\_t gpio\_flags\_t

Provides a type to hold GPIO configuration flags.

**Definition** gpio.h:274

[GPIO\_ACTIVE\_LOW](group__gpio__interface.md#ga62cea8989df2425e5e5e712217d65f46)

#define GPIO\_ACTIVE\_LOW

GPIO pin is active (has logical value '1') in low state.

**Definition** gpio.h:26

[GPIO\_INT\_WAKEUP](group__gpio__interface.md#ga644109ce84c8feffe1226b9b50122a96)

#define GPIO\_INT\_WAKEUP

Configures GPIO interrupt to wakeup the system from low power mode.

**Definition** gpio.h:85

[gpio\_port\_set\_clr\_bits\_raw](group__gpio__interface.md#ga6e7ca22e83a70d3ddcf0de068b377c2d)

static int gpio\_port\_set\_clr\_bits\_raw(const struct device \*port, gpio\_port\_pins\_t set\_pins, gpio\_port\_pins\_t clear\_pins)

Set physical level of selected output pins.

**Definition** gpio.h:1447

[gpio\_port\_set\_clr\_bits](group__gpio__interface.md#ga77880d217f5dd1fc1c72ce791254449b)

static int gpio\_port\_set\_clr\_bits(const struct device \*port, gpio\_port\_pins\_t set\_pins, gpio\_port\_pins\_t clear\_pins)

Set logical level of selected output pins.

**Definition** gpio.h:1467

[gpio\_init\_callback](group__gpio__interface.md#ga7a7dd7c1f3a2135a9f378e1c34b6232c)

static void gpio\_init\_callback(struct gpio\_callback \*callback, gpio\_callback\_handler\_t handler, gpio\_port\_pins\_t pin\_mask)

Helper to initialize a struct gpio\_callback properly.

**Definition** gpio.h:1692

[gpio\_pin\_is\_input\_dt](group__gpio__interface.md#ga7aaec28a83cac63bd87fc94cc72664b1)

static int gpio\_pin\_is\_input\_dt(const struct gpio\_dt\_spec \*spec)

Check if a single pin from gpio\_dt\_spec is configured for input.

**Definition** gpio.h:1112

[GPIO\_INPUT](group__gpio__interface.md#ga7be6a0cc9aa65da1d4ee5751b4085853)

#define GPIO\_INPUT

Enables pin as input.

**Definition** gpio.h:47

[gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f)

uint32\_t gpio\_port\_pins\_t

Identifies a set of pins associated with a port.

**Definition** gpio.h:233

[gpio\_pin\_get\_config\_dt](group__gpio__interface.md#ga820448aa4be8b14839bc6a00c9f34bb4)

static int gpio\_pin\_get\_config\_dt(const struct gpio\_dt\_spec \*spec, gpio\_flags\_t \*flags)

Get a configuration of a single pin from a gpio\_dt\_spec.

**Definition** gpio.h:1207

[gpio\_port\_toggle\_bits](group__gpio__interface.md#ga82977d8706fb9f464db455bd0e9ac2e4)

int gpio\_port\_toggle\_bits(const struct device \*port, gpio\_port\_pins\_t pins)

Toggle level of selected output pins.

[GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a)

#define GPIO\_INT\_DISABLE

Disables GPIO pin interrupt.

**Definition** gpio.h:100

[gpio\_pin\_interrupt\_configure](group__gpio__interface.md#ga9618f254365381063439a0e9c5e787cb)

int gpio\_pin\_interrupt\_configure(const struct device \*port, gpio\_pin\_t pin, gpio\_flags\_t flags)

Configure pin interrupt.

[gpio\_port\_clear\_bits\_raw](group__gpio__interface.md#ga9d2c9daeec7ce127fc786ead566ad27f)

int gpio\_port\_clear\_bits\_raw(const struct device \*port, gpio\_port\_pins\_t pins)

Set physical level of selected output pins to low.

[gpio\_port\_set\_masked\_raw](group__gpio__interface.md#ga9e7b50d720fda362941acc1e3b3b2922)

int gpio\_port\_set\_masked\_raw(const struct device \*port, gpio\_port\_pins\_t mask, gpio\_port\_value\_t value)

Set physical level of output pins in a port.

[GPIO\_PULL\_UP](group__gpio__interface.md#gaaa7921da231fd2b96575fa522e2c1970)

#define GPIO\_PULL\_UP

Enables GPIO pin pull-up.

**Definition** gpio.h:75

[gpio\_pin\_get\_dt](group__gpio__interface.md#gaabeb2d0d98856c7ff78be36651d6bbc1)

static int gpio\_pin\_get\_dt(const struct gpio\_dt\_spec \*spec)

Get logical level of an input pin from a gpio\_dt\_spec.

**Definition** gpio.h:1556

[gpio\_pin\_toggle](group__gpio__interface.md#gaabf948471d313ff19410f1741dd16957)

static int gpio\_pin\_toggle(const struct device \*port, gpio\_pin\_t pin)

Toggle pin level.

**Definition** gpio.h:1660

[gpio\_is\_ready\_dt](group__gpio__interface.md#gaaec9ad17c08a0d527d66445fe82d8327)

static bool gpio\_is\_ready\_dt(const struct gpio\_dt\_spec \*spec)

Validate that GPIO port is ready.

**Definition** gpio.h:835

[gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693)

uint32\_t gpio\_port\_value\_t

Provides values for a set of pins associated with a port.

**Definition** gpio.h:246

[gpio\_pin\_set](group__gpio__interface.md#gabfab69282fb99be119760436f2d18a9b)

static int gpio\_pin\_set(const struct device \*port, gpio\_pin\_t pin, int value)

Set logical level of an output pin.

**Definition** gpio.h:1616

[gpio\_port\_clear\_bits](group__gpio__interface.md#gac1660707a44cc8a3aa08b25685b4b20b)

static int gpio\_port\_clear\_bits(const struct device \*port, gpio\_port\_pins\_t pins)

Set logical level of selected output pins to inactive.

**Definition** gpio.h:1408

[gpio\_remove\_callback](group__gpio__interface.md#gac1e94ba8faac79f469447e9b5d2f8c06)

static int gpio\_remove\_callback(const struct device \*port, struct gpio\_callback \*callback)

Remove an application callback.

**Definition** gpio.h:1765

[gpio\_port\_set\_masked](group__gpio__interface.md#gac653e70270019d599732ab78693dd1fd)

static int gpio\_port\_set\_masked(const struct device \*port, gpio\_port\_pins\_t mask, gpio\_port\_value\_t value)

Set logical level of output pins in a port.

**Definition** gpio.h:1326

[gpio\_port\_get\_direction](group__gpio__interface.md#gad2b2945dbe6987ac425e000721a894c4)

int gpio\_port\_get\_direction(const struct device \*port, gpio\_port\_pins\_t map, gpio\_port\_pins\_t \*inputs, gpio\_port\_pins\_t \*outputs)

Get direction of select pins in a port.

[gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2)

uint16\_t gpio\_dt\_flags\_t

Provides a type to hold GPIO devicetree flags.

**Definition** gpio.h:266

[GPIO\_PULL\_DOWN](group__gpio__interface.md#gadec1802e074f3021d464da09cd66c7cf)

#define GPIO\_PULL\_DOWN

Enable GPIO pin pull-down.

**Definition** gpio.h:78

[gpio\_pin\_set\_raw](group__gpio__interface.md#gae28f0fa2576530083aa86d819d0d5cca)

static int gpio\_pin\_set\_raw(const struct device \*port, gpio\_pin\_t pin, int value)

Set physical level of an output pin.

**Definition** gpio.h:1576

[gpio\_port\_get\_raw](group__gpio__interface.md#gae2a49b36cae2e17fc665a3bd844f50b4)

int gpio\_port\_get\_raw(const struct device \*port, gpio\_port\_value\_t \*value)

Get physical level of all input pins in a port.

[gpio\_port\_get](group__gpio__interface.md#gae578c8163fb8fe5600d1ca9e5d7526b1)

static int gpio\_port\_get(const struct device \*port, gpio\_port\_value\_t \*value)

Get logical level of all input pins in a port.

**Definition** gpio.h:1260

[gpio\_pin\_configure](group__gpio__interface.md#gaed4a2051d76db7eead8ed1719ce2ba33)

int gpio\_pin\_configure(const struct device \*port, gpio\_pin\_t pin, gpio\_flags\_t flags)

Configure a single pin.

[gpio\_callback\_handler\_t](group__gpio__interface.md#gaf0aa40279d32b1b8332f2f23a39510af)

void(\* gpio\_callback\_handler\_t)(const struct device \*port, struct gpio\_callback \*cb, gpio\_port\_pins\_t pins)

Define the application callback handler function signature.

**Definition** gpio.h:726

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[types.h](include_2zephyr_2types_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[slist.h](slist_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:413

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[device::config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc)

const void \* config

Address of device instance config information.

**Definition** device.h:407

[gpio\_callback](structgpio__callback.md)

GPIO callback structure.

**Definition** gpio.h:740

[gpio\_callback::node](structgpio__callback.md#ab60e7093072964bd818d536c746211e4)

sys\_snode\_t node

This is meant to be used in the driver and the user should not mess with it (see drivers/gpio/gpio\_ut...

**Definition** gpio.h:744

[gpio\_callback::pin\_mask](structgpio__callback.md#ace5c2b83f1d51f73877a1f2c54ba8c67)

gpio\_port\_pins\_t pin\_mask

A mask of pins the callback is interested in, if 0 the callback will never be called.

**Definition** gpio.h:755

[gpio\_callback::handler](structgpio__callback.md#af89dc41cbd610d81ac03cae7ab764ceb)

gpio\_callback\_handler\_t handler

Actual callback function being called when relevant.

**Definition** gpio.h:747

[gpio\_driver\_config](structgpio__driver__config.md)

This structure is common to all GPIO drivers and is expected to be the first element in the object po...

**Definition** gpio.h:690

[gpio\_driver\_config::port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052)

gpio\_port\_pins\_t port\_pin\_mask

Mask identifying pins supported by the controller.

**Definition** gpio.h:696

[gpio\_driver\_data](structgpio__driver__data.md)

This structure is common to all GPIO drivers and is expected to be the first element in the driver's ...

**Definition** gpio.h:703

[gpio\_driver\_data::invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169)

gpio\_port\_pins\_t invert

Mask identifying pins that are configured as active low.

**Definition** gpio.h:709

[gpio\_dt\_spec](structgpio__dt__spec.md)

Container for GPIO pin information specified in devicetree.

**Definition** gpio.h:288

[gpio\_dt\_spec::port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f)

const struct device \* port

GPIO device controlling the pin.

**Definition** gpio.h:290

[gpio\_dt\_spec::pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84)

gpio\_pin\_t pin

The pin's number on the device.

**Definition** gpio.h:292

[gpio\_dt\_spec::dt\_flags](structgpio__dt__spec.md#ae3b90e7e22708798c67da94f72ad1ab0)

gpio\_dt\_flags\_t dt\_flags

The pin's configuration flags as specified in devicetree.

**Definition** gpio.h:294

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio.h](drivers_2gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
