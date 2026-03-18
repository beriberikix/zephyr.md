---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2gpio_8h_source.html
original_path: doxygen/html/drivers_2gpio_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

38

43

[ 45](group__gpio__interface.md#ga7be6a0cc9aa65da1d4ee5751b4085853)#define GPIO\_INPUT (1U << 16)

46

[ 48](group__gpio__interface.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)#define GPIO\_OUTPUT (1U << 17)

49

[ 51](group__gpio__interface.md#gaf82306c09450f6933366c4b821db21ed)#define GPIO\_DISCONNECTED 0

52

54

55/\* Initializes output to a low state. \*/

56#define GPIO\_OUTPUT\_INIT\_LOW (1U << 18)

57

58/\* Initializes output to a high state. \*/

59#define GPIO\_OUTPUT\_INIT\_HIGH (1U << 19)

60

61/\* Initializes output based on logic level \*/

62#define GPIO\_OUTPUT\_INIT\_LOGICAL (1U << 20)

63

65

[ 67](group__gpio__interface.md#gaf85baf9f9c1ba554324b4cd7064487b0)#define GPIO\_OUTPUT\_LOW (GPIO\_OUTPUT | GPIO\_OUTPUT\_INIT\_LOW)

[ 69](group__gpio__interface.md#ga10d31f204c0e927017d571352422fb09)#define GPIO\_OUTPUT\_HIGH (GPIO\_OUTPUT | GPIO\_OUTPUT\_INIT\_HIGH)

[ 71](group__gpio__interface.md#ga1e1d6be5f2f788f89468a0ce8b854634)#define GPIO\_OUTPUT\_INACTIVE (GPIO\_OUTPUT | \

72 GPIO\_OUTPUT\_INIT\_LOW | \

73 GPIO\_OUTPUT\_INIT\_LOGICAL)

74

[ 75](group__gpio__interface.md#ga0f5cc126d6a690eb3e303eb29aa718ce)#define GPIO\_OUTPUT\_ACTIVE (GPIO\_OUTPUT | \

76 GPIO\_OUTPUT\_INIT\_HIGH | \

77 GPIO\_OUTPUT\_INIT\_LOGICAL)

78

80

96

[ 98](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a)#define GPIO\_INT\_DISABLE (1U << 21)

99

101

102/\* Enables GPIO pin interrupt. \*/

103#define GPIO\_INT\_ENABLE (1U << 22)

104

105/\* GPIO interrupt is sensitive to logical levels.

106 \*

107 \* This is a component flag that should be combined with other

108 \* `GPIO\_INT\_\*` flags to produce a meaningful configuration.

109 \*/

110#define GPIO\_INT\_LEVELS\_LOGICAL (1U << 23)

111

112/\* GPIO interrupt is edge sensitive.

113 \*

114 \* Note: by default interrupts are level sensitive.

115 \*

116 \* This is a component flag that should be combined with other

117 \* `GPIO\_INT\_\*` flags to produce a meaningful configuration.

118 \*/

119#define GPIO\_INT\_EDGE (1U << 24)

120

121/\* Trigger detection when input state is (or transitions to) physical low or

122 \* logical 0 level.

123 \*

124 \* This is a component flag that should be combined with other

125 \* `GPIO\_INT\_\*` flags to produce a meaningful configuration.

126 \*/

127#define GPIO\_INT\_LOW\_0 (1U << 25)

128

129/\* Trigger detection on input state is (or transitions to) physical high or

130 \* logical 1 level.

131 \*

132 \* This is a component flag that should be combined with other

133 \* `GPIO\_INT\_\*` flags to produce a meaningful configuration.

134 \*/

135#define GPIO\_INT\_HIGH\_1 (1U << 26)

136

137#ifdef CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT

138/\* Disable/Enable interrupt functionality without changing other interrupt

139 \* related register, such as clearing the pending register.

140 \*

141 \* This is a component flag that should be combined with `GPIO\_INT\_ENABLE` or

142 \* `GPIO\_INT\_DISABLE` flags to produce a meaningful configuration.

143 \*/

144#define GPIO\_INT\_ENABLE\_DISABLE\_ONLY (1u << 27)

145#endif /\* CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT \*/

146

147#define GPIO\_INT\_MASK (GPIO\_INT\_DISABLE | \

148 GPIO\_INT\_ENABLE | \

149 GPIO\_INT\_LEVELS\_LOGICAL | \

150 GPIO\_INT\_EDGE | \

151 GPIO\_INT\_LOW\_0 | \

152 GPIO\_INT\_HIGH\_1)

153

155

[ 158](group__gpio__interface.md#gaed642a4e482f73aa917477370d0e241b)#define GPIO\_INT\_EDGE\_RISING (GPIO\_INT\_ENABLE | \

159 GPIO\_INT\_EDGE | \

160 GPIO\_INT\_HIGH\_1)

161

[ 165](group__gpio__interface.md#ga73bed10383a27d4a03feb300e64af8e8)#define GPIO\_INT\_EDGE\_FALLING (GPIO\_INT\_ENABLE | \

166 GPIO\_INT\_EDGE | \

167 GPIO\_INT\_LOW\_0)

168

[ 172](group__gpio__interface.md#ga10fa307ab17d02819108165a09f8e08b)#define GPIO\_INT\_EDGE\_BOTH (GPIO\_INT\_ENABLE | \

173 GPIO\_INT\_EDGE | \

174 GPIO\_INT\_LOW\_0 | \

175 GPIO\_INT\_HIGH\_1)

176

[ 180](group__gpio__interface.md#gaddbb5ad576875af9c2d73b73df55c893)#define GPIO\_INT\_LEVEL\_LOW (GPIO\_INT\_ENABLE | \

181 GPIO\_INT\_LOW\_0)

182

[ 186](group__gpio__interface.md#ga233690d9a6a64bc9f804e3caa6d4a88f)#define GPIO\_INT\_LEVEL\_HIGH (GPIO\_INT\_ENABLE | \

187 GPIO\_INT\_HIGH\_1)

188

[ 192](group__gpio__interface.md#ga7b922529a3cb9396b0d82ca823e9d010)#define GPIO\_INT\_EDGE\_TO\_INACTIVE (GPIO\_INT\_ENABLE | \

193 GPIO\_INT\_LEVELS\_LOGICAL | \

194 GPIO\_INT\_EDGE | \

195 GPIO\_INT\_LOW\_0)

196

[ 200](group__gpio__interface.md#ga35d2ff0e041236d82004a4bb2b5bf634)#define GPIO\_INT\_EDGE\_TO\_ACTIVE (GPIO\_INT\_ENABLE | \

201 GPIO\_INT\_LEVELS\_LOGICAL | \

202 GPIO\_INT\_EDGE | \

203 GPIO\_INT\_HIGH\_1)

204

[ 208](group__gpio__interface.md#gacb9bb1b63f172af2da7eb193e234c4f2)#define GPIO\_INT\_LEVEL\_INACTIVE (GPIO\_INT\_ENABLE | \

209 GPIO\_INT\_LEVELS\_LOGICAL | \

210 GPIO\_INT\_LOW\_0)

211

[ 215](group__gpio__interface.md#gae51c68ff83959994bb942bb253505ca1)#define GPIO\_INT\_LEVEL\_ACTIVE (GPIO\_INT\_ENABLE | \

216 GPIO\_INT\_LEVELS\_LOGICAL | \

217 GPIO\_INT\_HIGH\_1)

218

220

222#define GPIO\_DIR\_MASK (GPIO\_INPUT | GPIO\_OUTPUT)

224

[ 231](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f);

232

[ 244](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693);

245

[ 252](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34);

253

[ 264](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2);

265

[ 272](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e);

273

[ 286](structgpio__dt__spec.md)struct [gpio\_dt\_spec](structgpio__dt__spec.md) {

[ 288](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f) const struct [device](structdevice.md) \*[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f);

[ 290](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84) [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) [pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84);

[ 292](structgpio__dt__spec.md#ae3b90e7e22708798c67da94f72ad1ab0) [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2) [dt\_flags](structgpio__dt__spec.md#ae3b90e7e22708798c67da94f72ad1ab0);

293};

294

[ 329](group__gpio__interface.md#gacb1077b77aecf8f1a9c7636ea583c4cf)#define GPIO\_DT\_SPEC\_GET\_BY\_IDX(node\_id, prop, idx) \

330 { \

331 .port = DEVICE\_DT\_GET(DT\_GPIO\_CTLR\_BY\_IDX(node\_id, prop, idx)),\

332 .pin = DT\_GPIO\_PIN\_BY\_IDX(node\_id, prop, idx), \

333 .dt\_flags = DT\_GPIO\_FLAGS\_BY\_IDX(node\_id, prop, idx), \

334 }

335

[ 353](group__gpio__interface.md#ga3db4fa464e191016287f4c4d7eb9a983)#define GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, prop, idx, default\_value) \

354 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, prop), \

355 (GPIO\_DT\_SPEC\_GET\_BY\_IDX(node\_id, prop, idx)), \

356 (default\_value))

357

[ 366](group__gpio__interface.md#ga2fa6bb5880f46984f9fc29c70f7d503e)#define GPIO\_DT\_SPEC\_GET(node\_id, prop) \

367 GPIO\_DT\_SPEC\_GET\_BY\_IDX(node\_id, prop, 0)

368

[ 379](group__gpio__interface.md#ga26b2205aa82819df1d80a22761352e71)#define GPIO\_DT\_SPEC\_GET\_OR(node\_id, prop, default\_value) \

380 GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, prop, 0, default\_value)

381

[ 392](group__gpio__interface.md#gabbdbef450f14fd0af73667e2728ad084)#define GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, prop, idx) \

393 GPIO\_DT\_SPEC\_GET\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

394

[ 406](group__gpio__interface.md#gaf07edf6bc88af18e9976c76f6c3c3bf1)#define GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, prop, idx, default\_value) \

407 COND\_CODE\_1(DT\_PROP\_HAS\_IDX(DT\_DRV\_INST(inst), prop, idx), \

408 (GPIO\_DT\_SPEC\_GET\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)), \

409 (default\_value))

410

[ 419](group__gpio__interface.md#ga168f5c6e39a0111191f606a9a0826e89)#define GPIO\_DT\_SPEC\_INST\_GET(inst, prop) \

420 GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, prop, 0)

421

[ 432](group__gpio__interface.md#gae6b4a354c3cf0e042a390aac4bc37c69)#define GPIO\_DT\_SPEC\_INST\_GET\_OR(inst, prop, default\_value) \

433 GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, prop, 0, default\_value)

434

435/\*

436 \* @cond INTERNAL\_HIDDEN

437 \*/

438

449#define Z\_GPIO\_GEN\_BITMASK\_COND(node\_id, prop, off\_idx, sz\_idx) \

450 COND\_CODE\_1(DT\_PROP\_HAS\_IDX(node\_id, prop, off\_idx), \

451 (COND\_CODE\_0(DT\_PROP\_BY\_IDX(node\_id, prop, sz\_idx), \

452 (0), \

453 (GENMASK64(DT\_PROP\_BY\_IDX(node\_id, prop, off\_idx) + \

454 DT\_PROP\_BY\_IDX(node\_id, prop, sz\_idx) - 1, \

455 DT\_PROP\_BY\_IDX(node\_id, prop, off\_idx)))) \

456 ), (0))

457

465#define Z\_GPIO\_GEN\_RESERVED\_RANGES\_COND(odd\_it, node\_id) \

466 COND\_CODE\_1(DT\_PROP\_HAS\_IDX(node\_id, gpio\_reserved\_ranges, odd\_it), \

467 (Z\_GPIO\_GEN\_BITMASK\_COND(node\_id, \

468 gpio\_reserved\_ranges, \

469 GET\_ARG\_N(odd\_it, Z\_SPARSE\_LIST\_EVEN\_NUMBERS), \

470 odd\_it)), \

471 (0))

472

476

[ 564](group__gpio__interface.md#ga439c3d29aa585b00853aba6d6416028a)#define GPIO\_DT\_RESERVED\_RANGES\_NGPIOS(node\_id, ngpios) \

565 ((gpio\_port\_pins\_t) \

566 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, gpio\_reserved\_ranges), \

567 (GENMASK64(BITS\_PER\_LONG\_LONG - 1, ngpios) \

568 | FOR\_EACH\_FIXED\_ARG(Z\_GPIO\_GEN\_RESERVED\_RANGES\_COND, \

569 (|), \

570 node\_id, \

571 LIST\_DROP\_EMPTY(Z\_SPARSE\_LIST\_ODD\_NUMBERS))), \

572 (0)))

573

[ 581](group__gpio__interface.md#ga648fcc0633d57b52d3df683efda98440)#define GPIO\_DT\_RESERVED\_RANGES(node\_id) \

582 GPIO\_DT\_RESERVED\_RANGES\_NGPIOS(node\_id, DT\_PROP(node\_id, ngpios))

583

[ 593](group__gpio__interface.md#gaebaea00f6f7649c61651e8d50c7cdf07)#define GPIO\_DT\_INST\_RESERVED\_RANGES\_NGPIOS(inst, ngpios) \

594 GPIO\_DT\_RESERVED\_RANGES\_NGPIOS(DT\_DRV\_INST(inst), ngpios)

595

[ 604](group__gpio__interface.md#ga9136b467eaddcc734bc6a0a7d8b34e14)#define GPIO\_DT\_INST\_RESERVED\_RANGES(inst) \

605 GPIO\_DT\_RESERVED\_RANGES(DT\_DRV\_INST(inst))

606

[ 655](group__gpio__interface.md#ga274e09d7082d97b2f90c6a7fd4b71d49)#define GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC(node\_id, ngpios) \

656 ((gpio\_port\_pins\_t) \

657 COND\_CODE\_0(ngpios, \

658 (0), \

659 (COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, gpio\_reserved\_ranges), \

660 ((GENMASK64(ngpios - 1, 0) & \

661 ~GPIO\_DT\_RESERVED\_RANGES\_NGPIOS(node\_id, ngpios))), \

662 (GENMASK64(ngpios - 1, 0))) \

663 ) \

664 ))

665

[ 675](group__gpio__interface.md#ga856fe8042e496a39ef3a4e19fff2c4ce)#define GPIO\_DT\_INST\_PORT\_PIN\_MASK\_NGPIOS\_EXC(inst, ngpios) \

676 GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC(DT\_DRV\_INST(inst), ngpios)

677

[ 681](group__gpio__interface.md#ga1449ba90eaec5e6144fe4faae21f2e3f)#define GPIO\_MAX\_PINS\_PER\_PORT (sizeof(gpio\_port\_pins\_t) \* \_\_CHAR\_BIT\_\_)

682

[ 688](structgpio__driver__config.md)struct [gpio\_driver\_config](structgpio__driver__config.md) {

[ 694](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) [port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052);

695};

696

[ 701](structgpio__driver__data.md)struct [gpio\_driver\_data](structgpio__driver__data.md) {

[ 707](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169) [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) [invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169);

708};

709

710struct [gpio\_callback](structgpio__callback.md);

711

[ 724](group__gpio__interface.md#gaf0aa40279d32b1b8332f2f23a39510af)typedef void (\*[gpio\_callback\_handler\_t](group__gpio__interface.md#gaf0aa40279d32b1b8332f2f23a39510af))(const struct [device](structdevice.md) \*port,

725 struct [gpio\_callback](structgpio__callback.md) \*cb,

726 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

727

[ 738](structgpio__callback.md)struct [gpio\_callback](structgpio__callback.md) {

[ 742](structgpio__callback.md#ab60e7093072964bd818d536c746211e4) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structgpio__callback.md#ab60e7093072964bd818d536c746211e4);

743

[ 745](structgpio__callback.md#af89dc41cbd610d81ac03cae7ab764ceb) [gpio\_callback\_handler\_t](group__gpio__interface.md#gaf0aa40279d32b1b8332f2f23a39510af) [handler](structgpio__callback.md#af89dc41cbd610d81ac03cae7ab764ceb);

746

[ 753](structgpio__callback.md#ace5c2b83f1d51f73877a1f2c54ba8c67) [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) [pin\_mask](structgpio__callback.md#ace5c2b83f1d51f73877a1f2c54ba8c67);

754};

755

761

762/\* Used by driver api function pin\_interrupt\_configure, these are defined

763 \* in terms of the public flags so we can just mask and pass them

764 \* through to the driver api

765 \*/

766enum gpio\_int\_mode {

767 GPIO\_INT\_MODE\_DISABLED = [GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a),

768 GPIO\_INT\_MODE\_LEVEL = GPIO\_INT\_ENABLE,

769 GPIO\_INT\_MODE\_EDGE = GPIO\_INT\_ENABLE | GPIO\_INT\_EDGE,

770#ifdef CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT

771 GPIO\_INT\_MODE\_DISABLE\_ONLY = [GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a) | GPIO\_INT\_ENABLE\_DISABLE\_ONLY,

772 GPIO\_INT\_MODE\_ENABLE\_ONLY = GPIO\_INT\_ENABLE | GPIO\_INT\_ENABLE\_DISABLE\_ONLY,

773#endif /\* CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT \*/

774};

775

776enum gpio\_int\_trig {

777 /\* Trigger detection when input state is (or transitions to)

778 \* physical low. (Edge Falling or Active Low)

779 \*/

780 GPIO\_INT\_TRIG\_LOW = GPIO\_INT\_LOW\_0,

781 /\* Trigger detection when input state is (or transitions to)

782 \* physical high. (Edge Rising or Active High) \*/

783 GPIO\_INT\_TRIG\_HIGH = GPIO\_INT\_HIGH\_1,

784 /\* Trigger detection on pin rising or falling edge. \*/

785 GPIO\_INT\_TRIG\_BOTH = GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1,

786};

787

788\_\_subsystem struct gpio\_driver\_api {

789 int (\*pin\_configure)(const struct device \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

790 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

791#ifdef CONFIG\_GPIO\_GET\_CONFIG

792 int (\*pin\_get\_config)(const struct device \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

793 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

794#endif

795 int (\*port\_get\_raw)(const struct device \*port,

796 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value);

797 int (\*port\_set\_masked\_raw)(const struct device \*port,

798 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask,

799 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value);

800 int (\*port\_set\_bits\_raw)(const struct device \*port,

801 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

802 int (\*port\_clear\_bits\_raw)(const struct device \*port,

803 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

804 int (\*port\_toggle\_bits)(const struct device \*port,

805 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

806 int (\*pin\_interrupt\_configure)(const struct device \*port,

807 [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

808 enum gpio\_int\_mode, enum gpio\_int\_trig);

809 int (\*manage\_callback)(const struct device \*port,

810 struct gpio\_callback \*cb,

811 bool set);

812 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*get\_pending\_int)(const struct device \*dev);

813#ifdef CONFIG\_GPIO\_GET\_DIRECTION

814 int (\*port\_get\_direction)(const struct device \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) map,

815 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*inputs, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*outputs);

816#endif /\* CONFIG\_GPIO\_GET\_DIRECTION \*/

817};

818

822

[ 831](group__gpio__interface.md#gaaec9ad17c08a0d527d66445fe82d8327)static inline bool [gpio\_is\_ready\_dt](group__gpio__interface.md#gaaec9ad17c08a0d527d66445fe82d8327)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec)

832{

833 /\* Validate port is ready \*/

834 return [device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f));

835}

836

[ 858](group__gpio__interface.md#ga9618f254365381063439a0e9c5e787cb)\_\_syscall int [gpio\_pin\_interrupt\_configure](group__gpio__interface.md#ga9618f254365381063439a0e9c5e787cb)(const struct [device](structdevice.md) \*port,

859 [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

860 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

861

862static inline int z\_impl\_gpio\_pin\_interrupt\_configure(const struct [device](structdevice.md) \*port,

863 [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

864 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

865{

866 const struct gpio\_driver\_api \*api =

867 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

868 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

869 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

870 const struct [gpio\_driver\_data](structgpio__driver__data.md) \*const data =

871 (const struct [gpio\_driver\_data](structgpio__driver__data.md) \*)port->data;

872 enum gpio\_int\_trig trig;

873 enum gpio\_int\_mode mode;

874

875 if (api->pin\_interrupt\_configure == NULL) {

876 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

877 }

878

879 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & ([GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a) | GPIO\_INT\_ENABLE))

880 != ([GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a) | GPIO\_INT\_ENABLE),

881 "Cannot both enable and disable interrupts");

882

883 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & ([GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a) | GPIO\_INT\_ENABLE)) != 0U,

884 "Must either enable or disable interrupts");

885

886 \_\_ASSERT((([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_INT\_ENABLE) == 0) ||

887 (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_INT\_EDGE) != 0) ||

888 (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1)) !=

889 (GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1)),

890 "Only one of GPIO\_INT\_LOW\_0, GPIO\_INT\_HIGH\_1 can be "

891 "enabled for a level interrupt.");

892

893 \_\_ASSERT((([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_INT\_ENABLE) == 0) ||

894#ifdef CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT

895 (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1)) != 0) ||

896 ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_INT\_ENABLE\_DISABLE\_ONLY) != 0,

897#else

898 (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1)) != 0),

899#endif /\* CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT \*/

900 "At least one of GPIO\_INT\_LOW\_0, GPIO\_INT\_HIGH\_1 has to be "

901 "enabled.");

902

903 \_\_ASSERT((cfg->port\_pin\_mask & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

904 "Unsupported pin");

905

906 if ((([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_INT\_LEVELS\_LOGICAL) != 0) &&

907 ((data->[invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0)) {

908 /\* Invert signal bits \*/

909 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) ^= (GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1);

910 }

911

912 trig = (enum gpio\_int\_trig)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1));

913#ifdef CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT

914 mode = (enum gpio\_int\_mode)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_INT\_EDGE | [GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a) | GPIO\_INT\_ENABLE |

915 GPIO\_INT\_ENABLE\_DISABLE\_ONLY));

916#else

917 mode = (enum gpio\_int\_mode)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_INT\_EDGE | [GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a) | GPIO\_INT\_ENABLE));

918#endif /\* CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT \*/

919

920 return api->pin\_interrupt\_configure(port, pin, mode, trig);

921}

922

[ 936](group__gpio__interface.md#ga24f0b4ad30e6a8c81f51a2813478c793)static inline int [gpio\_pin\_interrupt\_configure\_dt](group__gpio__interface.md#ga24f0b4ad30e6a8c81f51a2813478c793)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec,

937 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

938{

939 return [gpio\_pin\_interrupt\_configure](group__gpio__interface.md#ga9618f254365381063439a0e9c5e787cb)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84), [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

940}

941

[ 957](group__gpio__interface.md#gaed4a2051d76db7eead8ed1719ce2ba33)\_\_syscall int [gpio\_pin\_configure](group__gpio__interface.md#gaed4a2051d76db7eead8ed1719ce2ba33)(const struct [device](structdevice.md) \*port,

958 [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

959 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

960

961static inline int z\_impl\_gpio\_pin\_configure(const struct [device](structdevice.md) \*port,

962 [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

963 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

964{

965 const struct gpio\_driver\_api \*api =

966 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

967 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

968 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->config;

969 struct [gpio\_driver\_data](structgpio__driver__data.md) \*data =

970 (struct [gpio\_driver\_data](structgpio__driver__data.md) \*)port->data;

971

972 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_INT\_MASK) == 0,

973 "Interrupt flags are not supported");

974

975 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & ([GPIO\_PULL\_UP](group__gpio__interface.md#gaaa7921da231fd2b96575fa522e2c1970) | [GPIO\_PULL\_DOWN](group__gpio__interface.md#gadec1802e074f3021d464da09cd66c7cf))) !=

976 ([GPIO\_PULL\_UP](group__gpio__interface.md#gaaa7921da231fd2b96575fa522e2c1970) | [GPIO\_PULL\_DOWN](group__gpio__interface.md#gadec1802e074f3021d464da09cd66c7cf)),

977 "Pull Up and Pull Down should not be enabled simultaneously");

978

979 \_\_ASSERT(!(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & [GPIO\_INPUT](group__gpio__interface.md#ga7be6a0cc9aa65da1d4ee5751b4085853)) && !([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & [GPIO\_OUTPUT](group__gpio__interface.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)) && ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_SINGLE\_ENDED)),

980 "Input cannot be enabled for 'Open Drain', 'Open Source' modes without Output");

981

982 \_\_ASSERT\_NO\_MSG(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_SINGLE\_ENDED) != 0 ||

983 ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_LINE\_OPEN\_DRAIN) == 0);

984

985 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_OUTPUT\_INIT\_LOW | GPIO\_OUTPUT\_INIT\_HIGH)) == 0

986 || ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & [GPIO\_OUTPUT](group__gpio__interface.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)) != 0,

987 "Output needs to be enabled to be initialized low or high");

988

989 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_OUTPUT\_INIT\_LOW | GPIO\_OUTPUT\_INIT\_HIGH))

990 != (GPIO\_OUTPUT\_INIT\_LOW | GPIO\_OUTPUT\_INIT\_HIGH),

991 "Output cannot be initialized low and high");

992

993 if ((([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_OUTPUT\_INIT\_LOGICAL) != 0)

994 && (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_OUTPUT\_INIT\_LOW | GPIO\_OUTPUT\_INIT\_HIGH)) != 0)

995 && (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & [GPIO\_ACTIVE\_LOW](group__gpio__interface.md#ga62cea8989df2425e5e5e712217d65f46)) != 0)) {

996 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) ^= GPIO\_OUTPUT\_INIT\_LOW | GPIO\_OUTPUT\_INIT\_HIGH;

997 }

998

999 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) &= ~GPIO\_OUTPUT\_INIT\_LOGICAL;

1000

1001 \_\_ASSERT((cfg->port\_pin\_mask & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

1002 "Unsupported pin");

1003

1004 if (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & [GPIO\_ACTIVE\_LOW](group__gpio__interface.md#ga62cea8989df2425e5e5e712217d65f46)) != 0) {

1005 data->[invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169) |= ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin);

1006 } else {

1007 data->[invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169) &= ~([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin);

1008 }

1009

1010 return api->pin\_configure(port, pin, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

1011}

1012

[ 1024](group__gpio__interface.md#ga423db4f985098ddcaa504ec430e91913)static inline int [gpio\_pin\_configure\_dt](group__gpio__interface.md#ga423db4f985098ddcaa504ec430e91913)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec,

1025 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) extra\_flags)

1026{

1027 return [gpio\_pin\_configure](group__gpio__interface.md#gaed4a2051d76db7eead8ed1719ce2ba33)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f),

1028 spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84),

1029 spec->[dt\_flags](structgpio__dt__spec.md#ae3b90e7e22708798c67da94f72ad1ab0) | extra\_flags);

1030}

1031

[ 1050](group__gpio__interface.md#gad2b2945dbe6987ac425e000721a894c4)\_\_syscall int [gpio\_port\_get\_direction](group__gpio__interface.md#gad2b2945dbe6987ac425e000721a894c4)(const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) map,

1051 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*inputs, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*outputs);

1052

1053#ifdef CONFIG\_GPIO\_GET\_DIRECTION

1054static inline int z\_impl\_gpio\_port\_get\_direction(const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) map,

1055 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*inputs,

1056 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*outputs)

1057{

1058 const struct gpio\_driver\_api \*api = (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1059

1060 if (api->port\_get\_direction == NULL) {

1061 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1062 }

1063

1064 return api->port\_get\_direction(port, map, inputs, outputs);

1065}

1066#endif /\* CONFIG\_GPIO\_GET\_DIRECTION \*/

1067

[ 1080](group__gpio__interface.md#ga1454bc223fc2200aff3c4aab7d747da2)static inline int [gpio\_pin\_is\_input](group__gpio__interface.md#ga1454bc223fc2200aff3c4aab7d747da2)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin)

1081{

1082 int rv;

1083 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins;

1084 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*cfg =

1085 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1086

1087 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U, "Unsupported pin");

1088

1089 rv = [gpio\_port\_get\_direction](group__gpio__interface.md#gad2b2945dbe6987ac425e000721a894c4)(port, [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin), &pins, NULL);

1090 if (rv < 0) {

1091 return rv;

1092 }

1093

1094 return (int)!!(([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin) & pins);

1095}

1096

[ 1108](group__gpio__interface.md#ga7aaec28a83cac63bd87fc94cc72664b1)static inline int [gpio\_pin\_is\_input\_dt](group__gpio__interface.md#ga7aaec28a83cac63bd87fc94cc72664b1)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec)

1109{

1110 return [gpio\_pin\_is\_input](group__gpio__interface.md#ga1454bc223fc2200aff3c4aab7d747da2)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84));

1111}

1112

[ 1125](group__gpio__interface.md#ga3b854d759180e222299ea445b401acc1)static inline int [gpio\_pin\_is\_output](group__gpio__interface.md#ga3b854d759180e222299ea445b401acc1)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin)

1126{

1127 int rv;

1128 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins;

1129 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*cfg =

1130 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1131

1132 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U, "Unsupported pin");

1133

1134 rv = [gpio\_port\_get\_direction](group__gpio__interface.md#gad2b2945dbe6987ac425e000721a894c4)(port, [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin), NULL, &pins);

1135 if (rv < 0) {

1136 return rv;

1137 }

1138

1139 return (int)!!(([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin) & pins);

1140}

1141

[ 1153](group__gpio__interface.md#ga2255c5681d17952ab89a4b6016d8e80d)static inline int [gpio\_pin\_is\_output\_dt](group__gpio__interface.md#ga2255c5681d17952ab89a4b6016d8e80d)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec)

1154{

1155 return [gpio\_pin\_is\_output](group__gpio__interface.md#ga3b854d759180e222299ea445b401acc1)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84));

1156}

1157

[ 1173](group__gpio__interface.md#ga133284b60a13c6dc50b87c1d04259f5e)\_\_syscall int [gpio\_pin\_get\_config](group__gpio__interface.md#ga133284b60a13c6dc50b87c1d04259f5e)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

1174 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

1175

1176#ifdef CONFIG\_GPIO\_GET\_CONFIG

1177static inline int z\_impl\_gpio\_pin\_get\_config(const struct [device](structdevice.md) \*port,

1178 [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

1179 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

1180{

1181 const struct gpio\_driver\_api \*api =

1182 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1183

1184 if (api->pin\_get\_config == NULL)

1185 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1186

1187 return api->pin\_get\_config(port, pin, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

1188}

1189#endif

1190

[ 1203](group__gpio__interface.md#ga820448aa4be8b14839bc6a00c9f34bb4)static inline int [gpio\_pin\_get\_config\_dt](group__gpio__interface.md#ga820448aa4be8b14839bc6a00c9f34bb4)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec,

1204 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

1205{

1206 return [gpio\_pin\_get\_config](group__gpio__interface.md#ga133284b60a13c6dc50b87c1d04259f5e)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84), [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

1207}

1208

[ 1226](group__gpio__interface.md#gae2a49b36cae2e17fc665a3bd844f50b4)\_\_syscall int [gpio\_port\_get\_raw](group__gpio__interface.md#gae2a49b36cae2e17fc665a3bd844f50b4)(const struct [device](structdevice.md) \*port,

1227 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value);

1228

1229static inline int z\_impl\_gpio\_port\_get\_raw(const struct [device](structdevice.md) \*port,

1230 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value)

1231{

1232 const struct gpio\_driver\_api \*api =

1233 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1234

1235 return api->port\_get\_raw(port, value);

1236}

1237

[ 1256](group__gpio__interface.md#gae578c8163fb8fe5600d1ca9e5d7526b1)static inline int [gpio\_port\_get](group__gpio__interface.md#gae578c8163fb8fe5600d1ca9e5d7526b1)(const struct [device](structdevice.md) \*port,

1257 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value)

1258{

1259 const struct [gpio\_driver\_data](structgpio__driver__data.md) \*const data =

1260 (const struct [gpio\_driver\_data](structgpio__driver__data.md) \*)port->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

1261 int ret;

1262

1263 ret = [gpio\_port\_get\_raw](group__gpio__interface.md#gae2a49b36cae2e17fc665a3bd844f50b4)(port, value);

1264 if (ret == 0) {

1265 \*value ^= data->[invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169);

1266 }

1267

1268 return ret;

1269}

1270

[ 1288](group__gpio__interface.md#ga9e7b50d720fda362941acc1e3b3b2922)\_\_syscall int [gpio\_port\_set\_masked\_raw](group__gpio__interface.md#ga9e7b50d720fda362941acc1e3b3b2922)(const struct [device](structdevice.md) \*port,

1289 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask,

1290 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value);

1291

1292static inline int z\_impl\_gpio\_port\_set\_masked\_raw(const struct [device](structdevice.md) \*port,

1293 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask,

1294 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value)

1295{

1296 const struct gpio\_driver\_api \*api =

1297 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1298

1299 return api->port\_set\_masked\_raw(port, mask, value);

1300}

1301

[ 1322](group__gpio__interface.md#gac653e70270019d599732ab78693dd1fd)static inline int [gpio\_port\_set\_masked](group__gpio__interface.md#gac653e70270019d599732ab78693dd1fd)(const struct [device](structdevice.md) \*port,

1323 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask,

1324 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value)

1325{

1326 const struct [gpio\_driver\_data](structgpio__driver__data.md) \*const data =

1327 (const struct [gpio\_driver\_data](structgpio__driver__data.md) \*)port->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

1328

1329 value ^= data->[invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169);

1330

1331 return [gpio\_port\_set\_masked\_raw](group__gpio__interface.md#ga9e7b50d720fda362941acc1e3b3b2922)(port, mask, value);

1332}

1333

[ 1344](group__gpio__interface.md#ga18e6ca0df95566fecc0633efb04a075a)\_\_syscall int [gpio\_port\_set\_bits\_raw](group__gpio__interface.md#ga18e6ca0df95566fecc0633efb04a075a)(const struct [device](structdevice.md) \*port,

1345 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

1346

1347static inline int z\_impl\_gpio\_port\_set\_bits\_raw(const struct [device](structdevice.md) \*port,

1348 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins)

1349{

1350 const struct gpio\_driver\_api \*api =

1351 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1352

1353 return api->port\_set\_bits\_raw(port, pins);

1354}

1355

[ 1366](group__gpio__interface.md#ga570b669af237df991c4a55cff6ec3253)static inline int [gpio\_port\_set\_bits](group__gpio__interface.md#ga570b669af237df991c4a55cff6ec3253)(const struct [device](structdevice.md) \*port,

1367 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins)

1368{

1369 return [gpio\_port\_set\_masked](group__gpio__interface.md#gac653e70270019d599732ab78693dd1fd)(port, pins, pins);

1370}

1371

[ 1382](group__gpio__interface.md#ga9d2c9daeec7ce127fc786ead566ad27f)\_\_syscall int [gpio\_port\_clear\_bits\_raw](group__gpio__interface.md#ga9d2c9daeec7ce127fc786ead566ad27f)(const struct [device](structdevice.md) \*port,

1383 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

1384

1385static inline int z\_impl\_gpio\_port\_clear\_bits\_raw(const struct [device](structdevice.md) \*port,

1386 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins)

1387{

1388 const struct gpio\_driver\_api \*api =

1389 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1390

1391 return api->port\_clear\_bits\_raw(port, pins);

1392}

1393

[ 1404](group__gpio__interface.md#gac1660707a44cc8a3aa08b25685b4b20b)static inline int [gpio\_port\_clear\_bits](group__gpio__interface.md#gac1660707a44cc8a3aa08b25685b4b20b)(const struct [device](structdevice.md) \*port,

1405 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins)

1406{

1407 return [gpio\_port\_set\_masked](group__gpio__interface.md#gac653e70270019d599732ab78693dd1fd)(port, pins, 0);

1408}

1409

[ 1420](group__gpio__interface.md#ga82977d8706fb9f464db455bd0e9ac2e4)\_\_syscall int [gpio\_port\_toggle\_bits](group__gpio__interface.md#ga82977d8706fb9f464db455bd0e9ac2e4)(const struct [device](structdevice.md) \*port,

1421 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

1422

1423static inline int z\_impl\_gpio\_port\_toggle\_bits(const struct [device](structdevice.md) \*port,

1424 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins)

1425{

1426 const struct gpio\_driver\_api \*api =

1427 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1428

1429 return api->port\_toggle\_bits(port, pins);

1430}

1431

[ 1443](group__gpio__interface.md#ga6e7ca22e83a70d3ddcf0de068b377c2d)static inline int [gpio\_port\_set\_clr\_bits\_raw](group__gpio__interface.md#ga6e7ca22e83a70d3ddcf0de068b377c2d)(const struct [device](structdevice.md) \*port,

1444 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) set\_pins,

1445 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) clear\_pins)

1446{

1447 \_\_ASSERT((set\_pins & clear\_pins) == 0, "Set and Clear pins overlap");

1448

1449 return [gpio\_port\_set\_masked\_raw](group__gpio__interface.md#ga9e7b50d720fda362941acc1e3b3b2922)(port, set\_pins | clear\_pins, set\_pins);

1450}

1451

[ 1463](group__gpio__interface.md#ga77880d217f5dd1fc1c72ce791254449b)static inline int [gpio\_port\_set\_clr\_bits](group__gpio__interface.md#ga77880d217f5dd1fc1c72ce791254449b)(const struct [device](structdevice.md) \*port,

1464 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) set\_pins,

1465 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) clear\_pins)

1466{

1467 \_\_ASSERT((set\_pins & clear\_pins) == 0, "Set and Clear pins overlap");

1468

1469 return [gpio\_port\_set\_masked](group__gpio__interface.md#gac653e70270019d599732ab78693dd1fd)(port, set\_pins | clear\_pins, set\_pins);

1470}

1471

[ 1487](group__gpio__interface.md#ga0fc52723b78019258bb306c771c430a1)static inline int [gpio\_pin\_get\_raw](group__gpio__interface.md#ga0fc52723b78019258bb306c771c430a1)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin)

1488{

1489 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

1490 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1491 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value;

1492 int ret;

1493

1494 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

1495 "Unsupported pin");

1496

1497 ret = [gpio\_port\_get\_raw](group__gpio__interface.md#gae2a49b36cae2e17fc665a3bd844f50b4)(port, &value);

1498 if (ret == 0) {

1499 ret = (value & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0 ? 1 : 0;

1500 }

1501

1502 return ret;

1503}

1504

[ 1524](group__gpio__interface.md#ga154a4ea3d3084910f02df31dc0779be6)static inline int [gpio\_pin\_get](group__gpio__interface.md#ga154a4ea3d3084910f02df31dc0779be6)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin)

1525{

1526 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

1527 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1528 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value;

1529 int ret;

1530

1531 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

1532 "Unsupported pin");

1533

1534 ret = [gpio\_port\_get](group__gpio__interface.md#gae578c8163fb8fe5600d1ca9e5d7526b1)(port, &value);

1535 if (ret == 0) {

1536 ret = (value & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0 ? 1 : 0;

1537 }

1538

1539 return ret;

1540}

1541

[ 1552](group__gpio__interface.md#gaabeb2d0d98856c7ff78be36651d6bbc1)static inline int [gpio\_pin\_get\_dt](group__gpio__interface.md#gaabeb2d0d98856c7ff78be36651d6bbc1)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec)

1553{

1554 return [gpio\_pin\_get](group__gpio__interface.md#ga154a4ea3d3084910f02df31dc0779be6)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84));

1555}

1556

[ 1572](group__gpio__interface.md#gae28f0fa2576530083aa86d819d0d5cca)static inline int [gpio\_pin\_set\_raw](group__gpio__interface.md#gae28f0fa2576530083aa86d819d0d5cca)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

1573 int value)

1574{

1575 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

1576 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1577 int ret;

1578

1579 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

1580 "Unsupported pin");

1581

1582 if (value != 0) {

1583 ret = [gpio\_port\_set\_bits\_raw](group__gpio__interface.md#ga18e6ca0df95566fecc0633efb04a075a)(port, ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin));

1584 } else {

1585 ret = [gpio\_port\_clear\_bits\_raw](group__gpio__interface.md#ga9d2c9daeec7ce127fc786ead566ad27f)(port, ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin));

1586 }

1587

1588 return ret;

1589}

1590

[ 1612](group__gpio__interface.md#gabfab69282fb99be119760436f2d18a9b)static inline int [gpio\_pin\_set](group__gpio__interface.md#gabfab69282fb99be119760436f2d18a9b)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

1613 int value)

1614{

1615 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

1616 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1617 const struct [gpio\_driver\_data](structgpio__driver__data.md) \*const data =

1618 (const struct [gpio\_driver\_data](structgpio__driver__data.md) \*)port->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

1619

1620 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

1621 "Unsupported pin");

1622

1623 if (data->[invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) {

1624 value = (value != 0) ? 0 : 1;

1625 }

1626

1627 return [gpio\_pin\_set\_raw](group__gpio__interface.md#gae28f0fa2576530083aa86d819d0d5cca)(port, pin, value);

1628}

1629

[ 1641](group__gpio__interface.md#ga541064fb9e575c0c559c101754466fa8)static inline int [gpio\_pin\_set\_dt](group__gpio__interface.md#ga541064fb9e575c0c559c101754466fa8)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec, int value)

1642{

1643 return [gpio\_pin\_set](group__gpio__interface.md#gabfab69282fb99be119760436f2d18a9b)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84), value);

1644}

1645

[ 1656](group__gpio__interface.md#gaabf948471d313ff19410f1741dd16957)static inline int [gpio\_pin\_toggle](group__gpio__interface.md#gaabf948471d313ff19410f1741dd16957)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin)

1657{

1658 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

1659 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1660

1661 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

1662 "Unsupported pin");

1663

1664 return [gpio\_port\_toggle\_bits](group__gpio__interface.md#ga82977d8706fb9f464db455bd0e9ac2e4)(port, ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin));

1665}

1666

[ 1677](group__gpio__interface.md#ga3272e866489da6c2e12c48f803c59e81)static inline int [gpio\_pin\_toggle\_dt](group__gpio__interface.md#ga3272e866489da6c2e12c48f803c59e81)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec)

1678{

1679 return [gpio\_pin\_toggle](group__gpio__interface.md#gaabf948471d313ff19410f1741dd16957)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84));

1680}

1681

[ 1688](group__gpio__interface.md#ga7a7dd7c1f3a2135a9f378e1c34b6232c)static inline void [gpio\_init\_callback](group__gpio__interface.md#ga7a7dd7c1f3a2135a9f378e1c34b6232c)(struct [gpio\_callback](structgpio__callback.md) \*callback,

1689 [gpio\_callback\_handler\_t](group__gpio__interface.md#gaf0aa40279d32b1b8332f2f23a39510af) handler,

1690 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pin\_mask)

1691{

1692 \_\_ASSERT(callback, "Callback pointer should not be NULL");

1693 \_\_ASSERT(handler, "Callback handler pointer should not be NULL");

1694

1695 callback->[handler](structgpio__callback.md#af89dc41cbd610d81ac03cae7ab764ceb) = handler;

1696 callback->[pin\_mask](structgpio__callback.md#ace5c2b83f1d51f73877a1f2c54ba8c67) = pin\_mask;

1697}

1698

[ 1713](group__gpio__interface.md#ga05fd15af20386d69f9332354285b0cca)static inline int [gpio\_add\_callback](group__gpio__interface.md#ga05fd15af20386d69f9332354285b0cca)(const struct [device](structdevice.md) \*port,

1714 struct [gpio\_callback](structgpio__callback.md) \*callback)

1715{

1716 const struct gpio\_driver\_api \*api =

1717 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1718

1719 if (api->manage\_callback == NULL) {

1720 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1721 }

1722

1723 return api->manage\_callback(port, callback, true);

1724}

1725

[ 1737](group__gpio__interface.md#ga54845eb95bc9636c3e6ff285300b6979)static inline int [gpio\_add\_callback\_dt](group__gpio__interface.md#ga54845eb95bc9636c3e6ff285300b6979)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec,

1738 struct [gpio\_callback](structgpio__callback.md) \*callback)

1739{

1740 return [gpio\_add\_callback](group__gpio__interface.md#ga05fd15af20386d69f9332354285b0cca)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), callback);

1741}

1742

[ 1761](group__gpio__interface.md#gac1e94ba8faac79f469447e9b5d2f8c06)static inline int [gpio\_remove\_callback](group__gpio__interface.md#gac1e94ba8faac79f469447e9b5d2f8c06)(const struct [device](structdevice.md) \*port,

1762 struct [gpio\_callback](structgpio__callback.md) \*callback)

1763{

1764 const struct gpio\_driver\_api \*api =

1765 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1766

1767 if (api->manage\_callback == NULL) {

1768 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1769 }

1770

1771 return api->manage\_callback(port, callback, false);

1772}

1773

[ 1785](group__gpio__interface.md#ga2c9f8fee2addfc0aeeeeb011d534f304)static inline int [gpio\_remove\_callback\_dt](group__gpio__interface.md#ga2c9f8fee2addfc0aeeeeb011d534f304)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec,

1786 struct [gpio\_callback](structgpio__callback.md) \*callback)

1787{

1788 return [gpio\_remove\_callback](group__gpio__interface.md#gac1e94ba8faac79f469447e9b5d2f8c06)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), callback);

1789}

1790

[ 1805](group__gpio__interface.md#ga3f9e45de172a27f49c31a072c0c241e1)\_\_syscall int [gpio\_get\_pending\_int](group__gpio__interface.md#ga3f9e45de172a27f49c31a072c0c241e1)(const struct [device](structdevice.md) \*dev);

1806

1807static inline int z\_impl\_gpio\_get\_pending\_int(const struct [device](structdevice.md) \*dev)

1808{

1809 const struct gpio\_driver\_api \*api =

1810 (const struct gpio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1811

1812 if (api->get\_pending\_int == NULL) {

1813 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1814 }

1815

1816 return api->get\_pending\_int(dev);

1817}

1818

1822

1823#ifdef \_\_cplusplus

1824}

1825#endif

1826

1827#include <syscalls/gpio.h>

1828

1829#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_H\_ \*/

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

**Definition** gpio.h:1713

[GPIO\_OUTPUT](group__gpio__interface.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)

#define GPIO\_OUTPUT

Enables pin as output, no change to the output state.

**Definition** gpio.h:48

[gpio\_pin\_get\_raw](group__gpio__interface.md#ga0fc52723b78019258bb306c771c430a1)

static int gpio\_pin\_get\_raw(const struct device \*port, gpio\_pin\_t pin)

Get physical level of an input pin.

**Definition** gpio.h:1487

[gpio\_pin\_get\_config](group__gpio__interface.md#ga133284b60a13c6dc50b87c1d04259f5e)

int gpio\_pin\_get\_config(const struct device \*port, gpio\_pin\_t pin, gpio\_flags\_t \*flags)

Get a configuration of a single pin.

[gpio\_pin\_is\_input](group__gpio__interface.md#ga1454bc223fc2200aff3c4aab7d747da2)

static int gpio\_pin\_is\_input(const struct device \*port, gpio\_pin\_t pin)

Check if pin is configured for input.

**Definition** gpio.h:1080

[gpio\_pin\_get](group__gpio__interface.md#ga154a4ea3d3084910f02df31dc0779be6)

static int gpio\_pin\_get(const struct device \*port, gpio\_pin\_t pin)

Get logical level of an input pin.

**Definition** gpio.h:1524

[gpio\_port\_set\_bits\_raw](group__gpio__interface.md#ga18e6ca0df95566fecc0633efb04a075a)

int gpio\_port\_set\_bits\_raw(const struct device \*port, gpio\_port\_pins\_t pins)

Set physical level of selected output pins to high.

[gpio\_pin\_is\_output\_dt](group__gpio__interface.md#ga2255c5681d17952ab89a4b6016d8e80d)

static int gpio\_pin\_is\_output\_dt(const struct gpio\_dt\_spec \*spec)

Check if a single pin from gpio\_dt\_spec is configured for output.

**Definition** gpio.h:1153

[gpio\_pin\_interrupt\_configure\_dt](group__gpio__interface.md#ga24f0b4ad30e6a8c81f51a2813478c793)

static int gpio\_pin\_interrupt\_configure\_dt(const struct gpio\_dt\_spec \*spec, gpio\_flags\_t flags)

Configure pin interrupts from a gpio\_dt\_spec.

**Definition** gpio.h:936

[gpio\_remove\_callback\_dt](group__gpio__interface.md#ga2c9f8fee2addfc0aeeeeb011d534f304)

static int gpio\_remove\_callback\_dt(const struct gpio\_dt\_spec \*spec, struct gpio\_callback \*callback)

Remove an application callback.

**Definition** gpio.h:1785

[gpio\_pin\_toggle\_dt](group__gpio__interface.md#ga3272e866489da6c2e12c48f803c59e81)

static int gpio\_pin\_toggle\_dt(const struct gpio\_dt\_spec \*spec)

Toggle pin level from a gpio\_dt\_spec.

**Definition** gpio.h:1677

[gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34)

uint8\_t gpio\_pin\_t

Provides a type to hold a GPIO pin index.

**Definition** gpio.h:252

[gpio\_pin\_is\_output](group__gpio__interface.md#ga3b854d759180e222299ea445b401acc1)

static int gpio\_pin\_is\_output(const struct device \*port, gpio\_pin\_t pin)

Check if pin is configured for output.

**Definition** gpio.h:1125

[gpio\_get\_pending\_int](group__gpio__interface.md#ga3f9e45de172a27f49c31a072c0c241e1)

int gpio\_get\_pending\_int(const struct device \*dev)

Function to get pending interrupts.

[gpio\_pin\_configure\_dt](group__gpio__interface.md#ga423db4f985098ddcaa504ec430e91913)

static int gpio\_pin\_configure\_dt(const struct gpio\_dt\_spec \*spec, gpio\_flags\_t extra\_flags)

Configure a single pin from a gpio\_dt\_spec and some extra flags.

**Definition** gpio.h:1024

[gpio\_pin\_set\_dt](group__gpio__interface.md#ga541064fb9e575c0c559c101754466fa8)

static int gpio\_pin\_set\_dt(const struct gpio\_dt\_spec \*spec, int value)

Set logical level of a output pin from a gpio\_dt\_spec.

**Definition** gpio.h:1641

[gpio\_add\_callback\_dt](group__gpio__interface.md#ga54845eb95bc9636c3e6ff285300b6979)

static int gpio\_add\_callback\_dt(const struct gpio\_dt\_spec \*spec, struct gpio\_callback \*callback)

Add an application callback.

**Definition** gpio.h:1737

[gpio\_port\_set\_bits](group__gpio__interface.md#ga570b669af237df991c4a55cff6ec3253)

static int gpio\_port\_set\_bits(const struct device \*port, gpio\_port\_pins\_t pins)

Set logical level of selected output pins to active.

**Definition** gpio.h:1366

[gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e)

uint32\_t gpio\_flags\_t

Provides a type to hold GPIO configuration flags.

**Definition** gpio.h:272

[GPIO\_ACTIVE\_LOW](group__gpio__interface.md#ga62cea8989df2425e5e5e712217d65f46)

#define GPIO\_ACTIVE\_LOW

GPIO pin is active (has logical value '1') in low state.

**Definition** gpio.h:26

[gpio\_port\_set\_clr\_bits\_raw](group__gpio__interface.md#ga6e7ca22e83a70d3ddcf0de068b377c2d)

static int gpio\_port\_set\_clr\_bits\_raw(const struct device \*port, gpio\_port\_pins\_t set\_pins, gpio\_port\_pins\_t clear\_pins)

Set physical level of selected output pins.

**Definition** gpio.h:1443

[gpio\_port\_set\_clr\_bits](group__gpio__interface.md#ga77880d217f5dd1fc1c72ce791254449b)

static int gpio\_port\_set\_clr\_bits(const struct device \*port, gpio\_port\_pins\_t set\_pins, gpio\_port\_pins\_t clear\_pins)

Set logical level of selected output pins.

**Definition** gpio.h:1463

[gpio\_init\_callback](group__gpio__interface.md#ga7a7dd7c1f3a2135a9f378e1c34b6232c)

static void gpio\_init\_callback(struct gpio\_callback \*callback, gpio\_callback\_handler\_t handler, gpio\_port\_pins\_t pin\_mask)

Helper to initialize a struct gpio\_callback properly.

**Definition** gpio.h:1688

[gpio\_pin\_is\_input\_dt](group__gpio__interface.md#ga7aaec28a83cac63bd87fc94cc72664b1)

static int gpio\_pin\_is\_input\_dt(const struct gpio\_dt\_spec \*spec)

Check if a single pin from gpio\_dt\_spec is configured for input.

**Definition** gpio.h:1108

[GPIO\_INPUT](group__gpio__interface.md#ga7be6a0cc9aa65da1d4ee5751b4085853)

#define GPIO\_INPUT

Enables pin as input.

**Definition** gpio.h:45

[gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f)

uint32\_t gpio\_port\_pins\_t

Identifies a set of pins associated with a port.

**Definition** gpio.h:231

[gpio\_pin\_get\_config\_dt](group__gpio__interface.md#ga820448aa4be8b14839bc6a00c9f34bb4)

static int gpio\_pin\_get\_config\_dt(const struct gpio\_dt\_spec \*spec, gpio\_flags\_t \*flags)

Get a configuration of a single pin from a gpio\_dt\_spec.

**Definition** gpio.h:1203

[gpio\_port\_toggle\_bits](group__gpio__interface.md#ga82977d8706fb9f464db455bd0e9ac2e4)

int gpio\_port\_toggle\_bits(const struct device \*port, gpio\_port\_pins\_t pins)

Toggle level of selected output pins.

[GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a)

#define GPIO\_INT\_DISABLE

Disables GPIO pin interrupt.

**Definition** gpio.h:98

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

**Definition** gpio.h:1552

[gpio\_pin\_toggle](group__gpio__interface.md#gaabf948471d313ff19410f1741dd16957)

static int gpio\_pin\_toggle(const struct device \*port, gpio\_pin\_t pin)

Toggle pin level.

**Definition** gpio.h:1656

[gpio\_is\_ready\_dt](group__gpio__interface.md#gaaec9ad17c08a0d527d66445fe82d8327)

static bool gpio\_is\_ready\_dt(const struct gpio\_dt\_spec \*spec)

Validate that GPIO port is ready.

**Definition** gpio.h:831

[gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693)

uint32\_t gpio\_port\_value\_t

Provides values for a set of pins associated with a port.

**Definition** gpio.h:244

[gpio\_pin\_set](group__gpio__interface.md#gabfab69282fb99be119760436f2d18a9b)

static int gpio\_pin\_set(const struct device \*port, gpio\_pin\_t pin, int value)

Set logical level of an output pin.

**Definition** gpio.h:1612

[gpio\_port\_clear\_bits](group__gpio__interface.md#gac1660707a44cc8a3aa08b25685b4b20b)

static int gpio\_port\_clear\_bits(const struct device \*port, gpio\_port\_pins\_t pins)

Set logical level of selected output pins to inactive.

**Definition** gpio.h:1404

[gpio\_remove\_callback](group__gpio__interface.md#gac1e94ba8faac79f469447e9b5d2f8c06)

static int gpio\_remove\_callback(const struct device \*port, struct gpio\_callback \*callback)

Remove an application callback.

**Definition** gpio.h:1761

[gpio\_port\_set\_masked](group__gpio__interface.md#gac653e70270019d599732ab78693dd1fd)

static int gpio\_port\_set\_masked(const struct device \*port, gpio\_port\_pins\_t mask, gpio\_port\_value\_t value)

Set logical level of output pins in a port.

**Definition** gpio.h:1322

[gpio\_port\_get\_direction](group__gpio__interface.md#gad2b2945dbe6987ac425e000721a894c4)

int gpio\_port\_get\_direction(const struct device \*port, gpio\_port\_pins\_t map, gpio\_port\_pins\_t \*inputs, gpio\_port\_pins\_t \*outputs)

Get direction of select pins in a port.

[gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2)

uint16\_t gpio\_dt\_flags\_t

Provides a type to hold GPIO devicetree flags.

**Definition** gpio.h:264

[GPIO\_PULL\_DOWN](group__gpio__interface.md#gadec1802e074f3021d464da09cd66c7cf)

#define GPIO\_PULL\_DOWN

Enable GPIO pin pull-down.

**Definition** gpio.h:78

[gpio\_pin\_set\_raw](group__gpio__interface.md#gae28f0fa2576530083aa86d819d0d5cca)

static int gpio\_pin\_set\_raw(const struct device \*port, gpio\_pin\_t pin, int value)

Set physical level of an output pin.

**Definition** gpio.h:1572

[gpio\_port\_get\_raw](group__gpio__interface.md#gae2a49b36cae2e17fc665a3bd844f50b4)

int gpio\_port\_get\_raw(const struct device \*port, gpio\_port\_value\_t \*value)

Get physical level of all input pins in a port.

[gpio\_port\_get](group__gpio__interface.md#gae578c8163fb8fe5600d1ca9e5d7526b1)

static int gpio\_port\_get(const struct device \*port, gpio\_port\_value\_t \*value)

Get logical level of all input pins in a port.

**Definition** gpio.h:1256

[gpio\_pin\_configure](group__gpio__interface.md#gaed4a2051d76db7eead8ed1719ce2ba33)

int gpio\_pin\_configure(const struct device \*port, gpio\_pin\_t pin, gpio\_flags\_t flags)

Configure a single pin.

[gpio\_callback\_handler\_t](group__gpio__interface.md#gaf0aa40279d32b1b8332f2f23a39510af)

void(\* gpio\_callback\_handler\_t)(const struct device \*port, struct gpio\_callback \*cb, gpio\_port\_pins\_t pins)

Define the application callback handler function signature.

**Definition** gpio.h:724

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

**Definition** errno.h:83

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

**Definition** device.h:387

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:397

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[device::config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc)

const void \* config

Address of device instance config information.

**Definition** device.h:391

[gpio\_callback](structgpio__callback.md)

GPIO callback structure.

**Definition** gpio.h:738

[gpio\_callback::node](structgpio__callback.md#ab60e7093072964bd818d536c746211e4)

sys\_snode\_t node

This is meant to be used in the driver and the user should not mess with it (see drivers/gpio/gpio\_ut...

**Definition** gpio.h:742

[gpio\_callback::pin\_mask](structgpio__callback.md#ace5c2b83f1d51f73877a1f2c54ba8c67)

gpio\_port\_pins\_t pin\_mask

A mask of pins the callback is interested in, if 0 the callback will never be called.

**Definition** gpio.h:753

[gpio\_callback::handler](structgpio__callback.md#af89dc41cbd610d81ac03cae7ab764ceb)

gpio\_callback\_handler\_t handler

Actual callback function being called when relevant.

**Definition** gpio.h:745

[gpio\_driver\_config](structgpio__driver__config.md)

This structure is common to all GPIO drivers and is expected to be the first element in the object po...

**Definition** gpio.h:688

[gpio\_driver\_config::port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052)

gpio\_port\_pins\_t port\_pin\_mask

Mask identifying pins supported by the controller.

**Definition** gpio.h:694

[gpio\_driver\_data](structgpio__driver__data.md)

This structure is common to all GPIO drivers and is expected to be the first element in the driver's ...

**Definition** gpio.h:701

[gpio\_driver\_data::invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169)

gpio\_port\_pins\_t invert

Mask identifying pins that are configured as active low.

**Definition** gpio.h:707

[gpio\_dt\_spec](structgpio__dt__spec.md)

Container for GPIO pin information specified in devicetree.

**Definition** gpio.h:286

[gpio\_dt\_spec::port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f)

const struct device \* port

GPIO device controlling the pin.

**Definition** gpio.h:288

[gpio\_dt\_spec::pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84)

gpio\_pin\_t pin

The pin's number on the device.

**Definition** gpio.h:290

[gpio\_dt\_spec::dt\_flags](structgpio__dt__spec.md#ae3b90e7e22708798c67da94f72ad1ab0)

gpio\_dt\_flags\_t dt\_flags

The pin's configuration flags as specified in devicetree.

**Definition** gpio.h:292

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio.h](drivers_2gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
