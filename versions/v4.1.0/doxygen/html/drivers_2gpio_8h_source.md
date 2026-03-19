---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2gpio_8h_source.html
original_path: doxygen/html/drivers_2gpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

22#include <[zephyr/tracing/tracing.h](tracing_8h.md)>

23

24#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

25#include <stddef.h>

26#include <[zephyr/device.h](device_8h.md)>

27#include <[zephyr/dt-bindings/gpio/gpio.h](dt-bindings_2gpio_2gpio_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

41

46

[ 48](group__gpio__interface.md#ga7be6a0cc9aa65da1d4ee5751b4085853)#define GPIO\_INPUT (1U << 16)

49

[ 51](group__gpio__interface.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)#define GPIO\_OUTPUT (1U << 17)

52

[ 54](group__gpio__interface.md#gaf82306c09450f6933366c4b821db21ed)#define GPIO\_DISCONNECTED 0

55

57

58/\* Initializes output to a low state. \*/

59#define GPIO\_OUTPUT\_INIT\_LOW (1U << 18)

60

61/\* Initializes output to a high state. \*/

62#define GPIO\_OUTPUT\_INIT\_HIGH (1U << 19)

63

64/\* Initializes output based on logic level \*/

65#define GPIO\_OUTPUT\_INIT\_LOGICAL (1U << 20)

66

68

[ 70](group__gpio__interface.md#gaf85baf9f9c1ba554324b4cd7064487b0)#define GPIO\_OUTPUT\_LOW (GPIO\_OUTPUT | GPIO\_OUTPUT\_INIT\_LOW)

[ 72](group__gpio__interface.md#ga10d31f204c0e927017d571352422fb09)#define GPIO\_OUTPUT\_HIGH (GPIO\_OUTPUT | GPIO\_OUTPUT\_INIT\_HIGH)

[ 74](group__gpio__interface.md#ga1e1d6be5f2f788f89468a0ce8b854634)#define GPIO\_OUTPUT\_INACTIVE (GPIO\_OUTPUT | \

75 GPIO\_OUTPUT\_INIT\_LOW | \

76 GPIO\_OUTPUT\_INIT\_LOGICAL)

77

[ 78](group__gpio__interface.md#ga0f5cc126d6a690eb3e303eb29aa718ce)#define GPIO\_OUTPUT\_ACTIVE (GPIO\_OUTPUT | \

79 GPIO\_OUTPUT\_INIT\_HIGH | \

80 GPIO\_OUTPUT\_INIT\_LOGICAL)

81

83

99

[ 101](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a)#define GPIO\_INT\_DISABLE (1U << 21)

102

104

105/\* Enables GPIO pin interrupt. \*/

106#define GPIO\_INT\_ENABLE (1U << 22)

107

108/\* GPIO interrupt is sensitive to logical levels.

109 \*

110 \* This is a component flag that should be combined with other

111 \* `GPIO\_INT\_\*` flags to produce a meaningful configuration.

112 \*/

113#define GPIO\_INT\_LEVELS\_LOGICAL (1U << 23)

114

115/\* GPIO interrupt is edge sensitive.

116 \*

117 \* Note: by default interrupts are level sensitive.

118 \*

119 \* This is a component flag that should be combined with other

120 \* `GPIO\_INT\_\*` flags to produce a meaningful configuration.

121 \*/

122#define GPIO\_INT\_EDGE (1U << 24)

123

124/\* Trigger detection when input state is (or transitions to) physical low or

125 \* logical 0 level.

126 \*

127 \* This is a component flag that should be combined with other

128 \* `GPIO\_INT\_\*` flags to produce a meaningful configuration.

129 \*/

130#define GPIO\_INT\_LOW\_0 (1U << 25)

131

132/\* Trigger detection on input state is (or transitions to) physical high or

133 \* logical 1 level.

134 \*

135 \* This is a component flag that should be combined with other

136 \* `GPIO\_INT\_\*` flags to produce a meaningful configuration.

137 \*/

138#define GPIO\_INT\_HIGH\_1 (1U << 26)

139

140#ifdef CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT

141/\* Disable/Enable interrupt functionality without changing other interrupt

142 \* related register, such as clearing the pending register.

143 \*

144 \* This is a component flag that should be combined with `GPIO\_INT\_ENABLE` or

145 \* `GPIO\_INT\_DISABLE` flags to produce a meaningful configuration.

146 \*/

147#define GPIO\_INT\_ENABLE\_DISABLE\_ONLY (1u << 27)

148#endif /\* CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT \*/

149

150#define GPIO\_INT\_MASK (GPIO\_INT\_DISABLE | \

151 GPIO\_INT\_ENABLE | \

152 GPIO\_INT\_LEVELS\_LOGICAL | \

153 GPIO\_INT\_EDGE | \

154 GPIO\_INT\_LOW\_0 | \

155 GPIO\_INT\_HIGH\_1)

156

158

[ 161](group__gpio__interface.md#gaed642a4e482f73aa917477370d0e241b)#define GPIO\_INT\_EDGE\_RISING (GPIO\_INT\_ENABLE | \

162 GPIO\_INT\_EDGE | \

163 GPIO\_INT\_HIGH\_1)

164

[ 168](group__gpio__interface.md#ga73bed10383a27d4a03feb300e64af8e8)#define GPIO\_INT\_EDGE\_FALLING (GPIO\_INT\_ENABLE | \

169 GPIO\_INT\_EDGE | \

170 GPIO\_INT\_LOW\_0)

171

[ 175](group__gpio__interface.md#ga10fa307ab17d02819108165a09f8e08b)#define GPIO\_INT\_EDGE\_BOTH (GPIO\_INT\_ENABLE | \

176 GPIO\_INT\_EDGE | \

177 GPIO\_INT\_LOW\_0 | \

178 GPIO\_INT\_HIGH\_1)

179

[ 183](group__gpio__interface.md#gaddbb5ad576875af9c2d73b73df55c893)#define GPIO\_INT\_LEVEL\_LOW (GPIO\_INT\_ENABLE | \

184 GPIO\_INT\_LOW\_0)

185

[ 189](group__gpio__interface.md#ga233690d9a6a64bc9f804e3caa6d4a88f)#define GPIO\_INT\_LEVEL\_HIGH (GPIO\_INT\_ENABLE | \

190 GPIO\_INT\_HIGH\_1)

191

[ 195](group__gpio__interface.md#ga7b922529a3cb9396b0d82ca823e9d010)#define GPIO\_INT\_EDGE\_TO\_INACTIVE (GPIO\_INT\_ENABLE | \

196 GPIO\_INT\_LEVELS\_LOGICAL | \

197 GPIO\_INT\_EDGE | \

198 GPIO\_INT\_LOW\_0)

199

[ 203](group__gpio__interface.md#ga35d2ff0e041236d82004a4bb2b5bf634)#define GPIO\_INT\_EDGE\_TO\_ACTIVE (GPIO\_INT\_ENABLE | \

204 GPIO\_INT\_LEVELS\_LOGICAL | \

205 GPIO\_INT\_EDGE | \

206 GPIO\_INT\_HIGH\_1)

207

[ 211](group__gpio__interface.md#gacb9bb1b63f172af2da7eb193e234c4f2)#define GPIO\_INT\_LEVEL\_INACTIVE (GPIO\_INT\_ENABLE | \

212 GPIO\_INT\_LEVELS\_LOGICAL | \

213 GPIO\_INT\_LOW\_0)

214

[ 218](group__gpio__interface.md#gae51c68ff83959994bb942bb253505ca1)#define GPIO\_INT\_LEVEL\_ACTIVE (GPIO\_INT\_ENABLE | \

219 GPIO\_INT\_LEVELS\_LOGICAL | \

220 GPIO\_INT\_HIGH\_1)

221

223

225#define GPIO\_DIR\_MASK (GPIO\_INPUT | GPIO\_OUTPUT)

227

[ 234](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f);

235

[ 247](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693);

248

[ 255](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34);

256

[ 267](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2);

268

[ 275](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e);

276

[ 289](structgpio__dt__spec.md)struct [gpio\_dt\_spec](structgpio__dt__spec.md) {

[ 291](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f) const struct [device](structdevice.md) \*[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f);

[ 293](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84) [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) [pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84);

[ 295](structgpio__dt__spec.md#ae3b90e7e22708798c67da94f72ad1ab0) [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2) [dt\_flags](structgpio__dt__spec.md#ae3b90e7e22708798c67da94f72ad1ab0);

296};

297

[ 332](group__gpio__interface.md#gacb1077b77aecf8f1a9c7636ea583c4cf)#define GPIO\_DT\_SPEC\_GET\_BY\_IDX(node\_id, prop, idx) \

333 { \

334 .port = DEVICE\_DT\_GET(DT\_GPIO\_CTLR\_BY\_IDX(node\_id, prop, idx)),\

335 .pin = DT\_GPIO\_PIN\_BY\_IDX(node\_id, prop, idx), \

336 .dt\_flags = DT\_GPIO\_FLAGS\_BY\_IDX(node\_id, prop, idx), \

337 }

338

[ 356](group__gpio__interface.md#ga3db4fa464e191016287f4c4d7eb9a983)#define GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, prop, idx, default\_value) \

357 COND\_CODE\_1(DT\_PROP\_HAS\_IDX(node\_id, prop, idx), \

358 (GPIO\_DT\_SPEC\_GET\_BY\_IDX(node\_id, prop, idx)), \

359 (default\_value))

360

[ 369](group__gpio__interface.md#ga2fa6bb5880f46984f9fc29c70f7d503e)#define GPIO\_DT\_SPEC\_GET(node\_id, prop) \

370 GPIO\_DT\_SPEC\_GET\_BY\_IDX(node\_id, prop, 0)

371

[ 382](group__gpio__interface.md#ga26b2205aa82819df1d80a22761352e71)#define GPIO\_DT\_SPEC\_GET\_OR(node\_id, prop, default\_value) \

383 GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, prop, 0, default\_value)

384

[ 395](group__gpio__interface.md#gabbdbef450f14fd0af73667e2728ad084)#define GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, prop, idx) \

396 GPIO\_DT\_SPEC\_GET\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)

397

[ 409](group__gpio__interface.md#gaf07edf6bc88af18e9976c76f6c3c3bf1)#define GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, prop, idx, default\_value) \

410 COND\_CODE\_1(DT\_PROP\_HAS\_IDX(DT\_DRV\_INST(inst), prop, idx), \

411 (GPIO\_DT\_SPEC\_GET\_BY\_IDX(DT\_DRV\_INST(inst), prop, idx)), \

412 (default\_value))

413

[ 422](group__gpio__interface.md#ga168f5c6e39a0111191f606a9a0826e89)#define GPIO\_DT\_SPEC\_INST\_GET(inst, prop) \

423 GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, prop, 0)

424

[ 435](group__gpio__interface.md#gae6b4a354c3cf0e042a390aac4bc37c69)#define GPIO\_DT\_SPEC\_INST\_GET\_OR(inst, prop, default\_value) \

436 GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, prop, 0, default\_value)

437

438/\*

439 \* @cond INTERNAL\_HIDDEN

440 \*/

441

452#define Z\_GPIO\_GEN\_BITMASK\_COND(node\_id, prop, off\_idx, sz\_idx) \

453 COND\_CODE\_1(DT\_PROP\_HAS\_IDX(node\_id, prop, off\_idx), \

454 (COND\_CODE\_0(DT\_PROP\_BY\_IDX(node\_id, prop, sz\_idx), \

455 (0), \

456 (GENMASK64(DT\_PROP\_BY\_IDX(node\_id, prop, off\_idx) + \

457 DT\_PROP\_BY\_IDX(node\_id, prop, sz\_idx) - 1, \

458 DT\_PROP\_BY\_IDX(node\_id, prop, off\_idx)))) \

459 ), (0))

460

468#define Z\_GPIO\_GEN\_RESERVED\_RANGES\_COND(odd\_it, node\_id) \

469 COND\_CODE\_1(DT\_PROP\_HAS\_IDX(node\_id, gpio\_reserved\_ranges, odd\_it), \

470 (Z\_GPIO\_GEN\_BITMASK\_COND(node\_id, \

471 gpio\_reserved\_ranges, \

472 GET\_ARG\_N(odd\_it, Z\_SPARSE\_LIST\_EVEN\_NUMBERS), \

473 odd\_it)), \

474 (0))

475

479

[ 567](group__gpio__interface.md#ga439c3d29aa585b00853aba6d6416028a)#define GPIO\_DT\_RESERVED\_RANGES\_NGPIOS(node\_id, ngpios) \

568 ((gpio\_port\_pins\_t) \

569 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, gpio\_reserved\_ranges), \

570 (GENMASK64(BITS\_PER\_LONG\_LONG - 1, ngpios) \

571 | FOR\_EACH\_FIXED\_ARG(Z\_GPIO\_GEN\_RESERVED\_RANGES\_COND, \

572 (|), \

573 node\_id, \

574 LIST\_DROP\_EMPTY(Z\_SPARSE\_LIST\_ODD\_NUMBERS))), \

575 (0)))

576

[ 584](group__gpio__interface.md#ga648fcc0633d57b52d3df683efda98440)#define GPIO\_DT\_RESERVED\_RANGES(node\_id) \

585 GPIO\_DT\_RESERVED\_RANGES\_NGPIOS(node\_id, DT\_PROP(node\_id, ngpios))

586

[ 596](group__gpio__interface.md#gaebaea00f6f7649c61651e8d50c7cdf07)#define GPIO\_DT\_INST\_RESERVED\_RANGES\_NGPIOS(inst, ngpios) \

597 GPIO\_DT\_RESERVED\_RANGES\_NGPIOS(DT\_DRV\_INST(inst), ngpios)

598

[ 607](group__gpio__interface.md#ga9136b467eaddcc734bc6a0a7d8b34e14)#define GPIO\_DT\_INST\_RESERVED\_RANGES(inst) \

608 GPIO\_DT\_RESERVED\_RANGES(DT\_DRV\_INST(inst))

609

[ 658](group__gpio__interface.md#ga274e09d7082d97b2f90c6a7fd4b71d49)#define GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC(node\_id, ngpios) \

659 ((gpio\_port\_pins\_t) \

660 COND\_CODE\_0(ngpios, \

661 (0), \

662 (COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, gpio\_reserved\_ranges), \

663 ((GENMASK64(ngpios - 1, 0) & \

664 ~GPIO\_DT\_RESERVED\_RANGES\_NGPIOS(node\_id, ngpios))), \

665 (GENMASK64(ngpios - 1, 0))) \

666 ) \

667 ))

668

[ 678](group__gpio__interface.md#ga856fe8042e496a39ef3a4e19fff2c4ce)#define GPIO\_DT\_INST\_PORT\_PIN\_MASK\_NGPIOS\_EXC(inst, ngpios) \

679 GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC(DT\_DRV\_INST(inst), ngpios)

680

[ 684](group__gpio__interface.md#ga1449ba90eaec5e6144fe4faae21f2e3f)#define GPIO\_MAX\_PINS\_PER\_PORT (sizeof(gpio\_port\_pins\_t) \* \_\_CHAR\_BIT\_\_)

685

[ 691](structgpio__driver__config.md)struct [gpio\_driver\_config](structgpio__driver__config.md) {

[ 697](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) [port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052);

698};

699

[ 704](structgpio__driver__data.md)struct [gpio\_driver\_data](structgpio__driver__data.md) {

[ 710](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169) [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) [invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169);

711};

712

713struct [gpio\_callback](structgpio__callback.md);

714

[ 727](group__gpio__interface.md#gaf0aa40279d32b1b8332f2f23a39510af)typedef void (\*[gpio\_callback\_handler\_t](group__gpio__interface.md#gaf0aa40279d32b1b8332f2f23a39510af))(const struct [device](structdevice.md) \*port,

728 struct [gpio\_callback](structgpio__callback.md) \*cb,

729 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

730

[ 741](structgpio__callback.md)struct [gpio\_callback](structgpio__callback.md) {

[ 745](structgpio__callback.md#ab60e7093072964bd818d536c746211e4) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structgpio__callback.md#ab60e7093072964bd818d536c746211e4);

746

[ 748](structgpio__callback.md#af89dc41cbd610d81ac03cae7ab764ceb) [gpio\_callback\_handler\_t](group__gpio__interface.md#gaf0aa40279d32b1b8332f2f23a39510af) [handler](structgpio__callback.md#af89dc41cbd610d81ac03cae7ab764ceb);

749

[ 756](structgpio__callback.md#ace5c2b83f1d51f73877a1f2c54ba8c67) [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) [pin\_mask](structgpio__callback.md#ace5c2b83f1d51f73877a1f2c54ba8c67);

757};

758

764

765/\* Used by driver api function pin\_interrupt\_configure, these are defined

766 \* in terms of the public flags so we can just mask and pass them

767 \* through to the driver api

768 \*/

769enum gpio\_int\_mode {

770 GPIO\_INT\_MODE\_DISABLED = [GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a),

771 GPIO\_INT\_MODE\_LEVEL = GPIO\_INT\_ENABLE,

772 GPIO\_INT\_MODE\_EDGE = GPIO\_INT\_ENABLE | GPIO\_INT\_EDGE,

773#ifdef CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT

774 GPIO\_INT\_MODE\_DISABLE\_ONLY = [GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a) | GPIO\_INT\_ENABLE\_DISABLE\_ONLY,

775 GPIO\_INT\_MODE\_ENABLE\_ONLY = GPIO\_INT\_ENABLE | GPIO\_INT\_ENABLE\_DISABLE\_ONLY,

776#endif /\* CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT \*/

777};

778

779enum gpio\_int\_trig {

780 /\* Trigger detection when input state is (or transitions to)

781 \* physical low. (Edge Falling or Active Low)

782 \*/

783 GPIO\_INT\_TRIG\_LOW = GPIO\_INT\_LOW\_0,

784 /\* Trigger detection when input state is (or transitions to)

785 \* physical high. (Edge Rising or Active High) \*/

786 GPIO\_INT\_TRIG\_HIGH = GPIO\_INT\_HIGH\_1,

787 /\* Trigger detection on pin rising or falling edge. \*/

788 GPIO\_INT\_TRIG\_BOTH = GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1,

789 /\* Trigger a system wakeup. \*/

790 GPIO\_INT\_TRIG\_WAKE = [GPIO\_INT\_WAKEUP](group__gpio__interface.md#ga644109ce84c8feffe1226b9b50122a96),

791};

792

793\_\_subsystem struct gpio\_driver\_api {

794 int (\*pin\_configure)(const struct device \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

795 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

796#ifdef CONFIG\_GPIO\_GET\_CONFIG

797 int (\*pin\_get\_config)(const struct device \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

798 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

799#endif

800 int (\*port\_get\_raw)(const struct device \*port,

801 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value);

802 int (\*port\_set\_masked\_raw)(const struct device \*port,

803 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask,

804 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value);

805 int (\*port\_set\_bits\_raw)(const struct device \*port,

806 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

807 int (\*port\_clear\_bits\_raw)(const struct device \*port,

808 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

809 int (\*port\_toggle\_bits)(const struct device \*port,

810 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

811 int (\*pin\_interrupt\_configure)(const struct device \*port,

812 [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

813 enum gpio\_int\_mode mode,

814 enum gpio\_int\_trig trig);

815 int (\*manage\_callback)(const struct device \*port,

816 struct gpio\_callback \*cb,

817 bool set);

818 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*get\_pending\_int)(const struct device \*dev);

819#ifdef CONFIG\_GPIO\_GET\_DIRECTION

820 int (\*port\_get\_direction)(const struct device \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) map,

821 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*inputs, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*outputs);

822#endif /\* CONFIG\_GPIO\_GET\_DIRECTION \*/

823};

824

828

[ 837](group__gpio__interface.md#gaaec9ad17c08a0d527d66445fe82d8327)static inline bool [gpio\_is\_ready\_dt](group__gpio__interface.md#gaaec9ad17c08a0d527d66445fe82d8327)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec)

838{

839 /\* Validate port is ready \*/

840 return [device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f));

841}

842

[ 866](group__gpio__interface.md#ga9618f254365381063439a0e9c5e787cb)\_\_syscall int [gpio\_pin\_interrupt\_configure](group__gpio__interface.md#ga9618f254365381063439a0e9c5e787cb)(const struct [device](structdevice.md) \*port,

867 [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

868 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

869

870static inline int z\_impl\_gpio\_pin\_interrupt\_configure(const struct [device](structdevice.md) \*port,

871 [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

872 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

873{

874 const struct gpio\_driver\_api \*api =

875 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

876 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

877 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

878 const struct [gpio\_driver\_data](structgpio__driver__data.md) \*const data =

879 (const struct [gpio\_driver\_data](structgpio__driver__data.md) \*)port->data;

880 enum gpio\_int\_trig trig;

881 enum gpio\_int\_mode mode;

882 int ret;

883

884 [SYS\_PORT\_TRACING\_FUNC\_ENTER](group__subsys__tracing__macros.md#ga445bcac4cec53d560ddca757de17e1e3)(gpio\_pin, interrupt\_configure, port, pin, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

885

886 if (api->pin\_interrupt\_configure == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

887 [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(gpio\_pin, interrupt\_configure, port, pin, -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b));

888 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

889 }

890

891 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & ([GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a) | GPIO\_INT\_ENABLE))

892 != ([GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a) | GPIO\_INT\_ENABLE),

893 "Cannot both enable and disable interrupts");

894

895 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & ([GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a) | GPIO\_INT\_ENABLE)) != 0U,

896 "Must either enable or disable interrupts");

897

898 \_\_ASSERT((([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_INT\_ENABLE) == 0) ||

899 (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_INT\_EDGE) != 0) ||

900 (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1)) !=

901 (GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1)),

902 "Only one of GPIO\_INT\_LOW\_0, GPIO\_INT\_HIGH\_1 can be "

903 "enabled for a level interrupt.");

904

905 \_\_ASSERT((([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_INT\_ENABLE) == 0) ||

906#ifdef CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT

907 (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1)) != 0) ||

908 ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_INT\_ENABLE\_DISABLE\_ONLY) != 0,

909#else

910 (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1)) != 0),

911#endif /\* CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT \*/

912 "At least one of GPIO\_INT\_LOW\_0, GPIO\_INT\_HIGH\_1 has to be "

913 "enabled.");

914

915 \_\_ASSERT((cfg->port\_pin\_mask & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

916 "Unsupported pin");

917

918 if ((([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_INT\_LEVELS\_LOGICAL) != 0) &&

919 ((data->[invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0)) {

920 /\* Invert signal bits \*/

921 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) ^= (GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1);

922 }

923

924 trig = (enum gpio\_int\_trig)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_INT\_LOW\_0 | GPIO\_INT\_HIGH\_1 | [GPIO\_INT\_WAKEUP](group__gpio__interface.md#ga644109ce84c8feffe1226b9b50122a96)));

925#ifdef CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT

926 mode = (enum gpio\_int\_mode)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_INT\_EDGE | [GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a) | GPIO\_INT\_ENABLE |

927 GPIO\_INT\_ENABLE\_DISABLE\_ONLY));

928#else

929 mode = (enum gpio\_int\_mode)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_INT\_EDGE | [GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a) | GPIO\_INT\_ENABLE));

930#endif /\* CONFIG\_GPIO\_ENABLE\_DISABLE\_INTERRUPT \*/

931

932 ret = api->pin\_interrupt\_configure(port, pin, mode, trig);

933 [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(gpio\_pin, interrupt\_configure, port, pin, ret);

934 return ret;

935}

936

[ 952](group__gpio__interface.md#ga24f0b4ad30e6a8c81f51a2813478c793)static inline int [gpio\_pin\_interrupt\_configure\_dt](group__gpio__interface.md#ga24f0b4ad30e6a8c81f51a2813478c793)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec,

953 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

954{

955 return [gpio\_pin\_interrupt\_configure](group__gpio__interface.md#ga9618f254365381063439a0e9c5e787cb)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84), [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

956}

957

[ 973](group__gpio__interface.md#gaed4a2051d76db7eead8ed1719ce2ba33)\_\_syscall int [gpio\_pin\_configure](group__gpio__interface.md#gaed4a2051d76db7eead8ed1719ce2ba33)(const struct [device](structdevice.md) \*port,

974 [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

975 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

976

977static inline int z\_impl\_gpio\_pin\_configure(const struct [device](structdevice.md) \*port,

978 [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

979 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

980{

981 const struct gpio\_driver\_api \*api =

982 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

983 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

984 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->config;

985 struct [gpio\_driver\_data](structgpio__driver__data.md) \*data =

986 (struct [gpio\_driver\_data](structgpio__driver__data.md) \*)port->data;

987 int ret;

988

989 [SYS\_PORT\_TRACING\_FUNC\_ENTER](group__subsys__tracing__macros.md#ga445bcac4cec53d560ddca757de17e1e3)(gpio\_pin, configure, port, pin, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

990

991 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_INT\_MASK) == 0,

992 "Interrupt flags are not supported");

993

994 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & ([GPIO\_PULL\_UP](group__gpio__interface.md#gaaa7921da231fd2b96575fa522e2c1970) | [GPIO\_PULL\_DOWN](group__gpio__interface.md#gadec1802e074f3021d464da09cd66c7cf))) !=

995 ([GPIO\_PULL\_UP](group__gpio__interface.md#gaaa7921da231fd2b96575fa522e2c1970) | [GPIO\_PULL\_DOWN](group__gpio__interface.md#gadec1802e074f3021d464da09cd66c7cf)),

996 "Pull Up and Pull Down should not be enabled simultaneously");

997

998 \_\_ASSERT(!(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & [GPIO\_INPUT](group__gpio__interface.md#ga7be6a0cc9aa65da1d4ee5751b4085853)) && !([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & [GPIO\_OUTPUT](group__gpio__interface.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)) && ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_SINGLE\_ENDED)),

999 "Input cannot be enabled for 'Open Drain', 'Open Source' modes without Output");

1000

1001 \_\_ASSERT\_NO\_MSG(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_SINGLE\_ENDED) != 0 ||

1002 ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_LINE\_OPEN\_DRAIN) == 0);

1003

1004 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_OUTPUT\_INIT\_LOW | GPIO\_OUTPUT\_INIT\_HIGH)) == 0

1005 || ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & [GPIO\_OUTPUT](group__gpio__interface.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)) != 0,

1006 "Output needs to be enabled to be initialized low or high");

1007

1008 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_OUTPUT\_INIT\_LOW | GPIO\_OUTPUT\_INIT\_HIGH))

1009 != (GPIO\_OUTPUT\_INIT\_LOW | GPIO\_OUTPUT\_INIT\_HIGH),

1010 "Output cannot be initialized low and high");

1011

1012 if ((([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & GPIO\_OUTPUT\_INIT\_LOGICAL) != 0)

1013 && (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & (GPIO\_OUTPUT\_INIT\_LOW | GPIO\_OUTPUT\_INIT\_HIGH)) != 0)

1014 && (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & [GPIO\_ACTIVE\_LOW](group__gpio__interface.md#ga62cea8989df2425e5e5e712217d65f46)) != 0)) {

1015 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) ^= GPIO\_OUTPUT\_INIT\_LOW | GPIO\_OUTPUT\_INIT\_HIGH;

1016 }

1017

1018 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) &= ~GPIO\_OUTPUT\_INIT\_LOGICAL;

1019

1020 \_\_ASSERT((cfg->port\_pin\_mask & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

1021 "Unsupported pin");

1022

1023 if (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & [GPIO\_ACTIVE\_LOW](group__gpio__interface.md#ga62cea8989df2425e5e5e712217d65f46)) != 0) {

1024 data->[invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169) |= ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin);

1025 } else {

1026 data->[invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169) &= ~([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin);

1027 }

1028

1029 ret = api->pin\_configure(port, pin, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

1030 [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(gpio\_pin, configure, port, pin, ret);

1031 return ret;

1032}

1033

[ 1045](group__gpio__interface.md#ga423db4f985098ddcaa504ec430e91913)static inline int [gpio\_pin\_configure\_dt](group__gpio__interface.md#ga423db4f985098ddcaa504ec430e91913)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec,

1046 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) extra\_flags)

1047{

1048 return [gpio\_pin\_configure](group__gpio__interface.md#gaed4a2051d76db7eead8ed1719ce2ba33)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f),

1049 spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84),

1050 spec->[dt\_flags](structgpio__dt__spec.md#ae3b90e7e22708798c67da94f72ad1ab0) | extra\_flags);

1051}

1052

[ 1071](group__gpio__interface.md#gad2b2945dbe6987ac425e000721a894c4)\_\_syscall int [gpio\_port\_get\_direction](group__gpio__interface.md#gad2b2945dbe6987ac425e000721a894c4)(const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) map,

1072 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*inputs, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*outputs);

1073

1074#ifdef CONFIG\_GPIO\_GET\_DIRECTION

1075static inline int z\_impl\_gpio\_port\_get\_direction(const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) map,

1076 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*inputs,

1077 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*outputs)

1078{

1079 const struct gpio\_driver\_api \*api = (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1080 int ret;

1081

1082 [SYS\_PORT\_TRACING\_FUNC\_ENTER](group__subsys__tracing__macros.md#ga445bcac4cec53d560ddca757de17e1e3)(gpio\_port, get\_direction, port, map, inputs, outputs);

1083

1084 if (api->port\_get\_direction == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1085 [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(gpio\_port, get\_direction, port, -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b));

1086 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1087 }

1088

1089 ret = api->port\_get\_direction(port, map, inputs, outputs);

1090 [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(gpio\_port, get\_direction, port, ret);

1091 return ret;

1092}

1093#endif /\* CONFIG\_GPIO\_GET\_DIRECTION \*/

1094

[ 1107](group__gpio__interface.md#ga1454bc223fc2200aff3c4aab7d747da2)static inline int [gpio\_pin\_is\_input](group__gpio__interface.md#ga1454bc223fc2200aff3c4aab7d747da2)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin)

1108{

1109 int rv;

1110 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins;

1111 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*cfg =

1112 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1113

1114 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U, "Unsupported pin");

1115

1116 rv = [gpio\_port\_get\_direction](group__gpio__interface.md#gad2b2945dbe6987ac425e000721a894c4)(port, [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin), &pins, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

1117 if (rv < 0) {

1118 return rv;

1119 }

1120

1121 return (int)!!(([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin) & pins);

1122}

1123

[ 1135](group__gpio__interface.md#ga7aaec28a83cac63bd87fc94cc72664b1)static inline int [gpio\_pin\_is\_input\_dt](group__gpio__interface.md#ga7aaec28a83cac63bd87fc94cc72664b1)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec)

1136{

1137 return [gpio\_pin\_is\_input](group__gpio__interface.md#ga1454bc223fc2200aff3c4aab7d747da2)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84));

1138}

1139

[ 1152](group__gpio__interface.md#ga3b854d759180e222299ea445b401acc1)static inline int [gpio\_pin\_is\_output](group__gpio__interface.md#ga3b854d759180e222299ea445b401acc1)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin)

1153{

1154 int rv;

1155 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins;

1156 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*cfg =

1157 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1158

1159 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U, "Unsupported pin");

1160

1161 rv = [gpio\_port\_get\_direction](group__gpio__interface.md#gad2b2945dbe6987ac425e000721a894c4)(port, [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), &pins);

1162 if (rv < 0) {

1163 return rv;

1164 }

1165

1166 return (int)!!(([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin) & pins);

1167}

1168

[ 1180](group__gpio__interface.md#ga2255c5681d17952ab89a4b6016d8e80d)static inline int [gpio\_pin\_is\_output\_dt](group__gpio__interface.md#ga2255c5681d17952ab89a4b6016d8e80d)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec)

1181{

1182 return [gpio\_pin\_is\_output](group__gpio__interface.md#ga3b854d759180e222299ea445b401acc1)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84));

1183}

1184

[ 1200](group__gpio__interface.md#ga133284b60a13c6dc50b87c1d04259f5e)\_\_syscall int [gpio\_pin\_get\_config](group__gpio__interface.md#ga133284b60a13c6dc50b87c1d04259f5e)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

1201 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

1202

1203#ifdef CONFIG\_GPIO\_GET\_CONFIG

1204static inline int z\_impl\_gpio\_pin\_get\_config(const struct [device](structdevice.md) \*port,

1205 [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

1206 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

1207{

1208 const struct gpio\_driver\_api \*api =

1209 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1210 int ret;

1211

1212 [SYS\_PORT\_TRACING\_FUNC\_ENTER](group__subsys__tracing__macros.md#ga445bcac4cec53d560ddca757de17e1e3)(gpio\_pin, get\_config, port, pin, \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

1213

1214 if (api->pin\_get\_config == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1215 [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(gpio\_pin, get\_config, port, pin, -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b));

1216 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1217 }

1218

1219 ret = api->pin\_get\_config(port, pin, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

1220 [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(gpio\_pin, get\_config, port, pin, ret);

1221 return ret;

1222}

1223#endif

1224

[ 1237](group__gpio__interface.md#ga820448aa4be8b14839bc6a00c9f34bb4)static inline int [gpio\_pin\_get\_config\_dt](group__gpio__interface.md#ga820448aa4be8b14839bc6a00c9f34bb4)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec,

1238 [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

1239{

1240 return [gpio\_pin\_get\_config](group__gpio__interface.md#ga133284b60a13c6dc50b87c1d04259f5e)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84), [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

1241}

1242

[ 1260](group__gpio__interface.md#gae2a49b36cae2e17fc665a3bd844f50b4)\_\_syscall int [gpio\_port\_get\_raw](group__gpio__interface.md#gae2a49b36cae2e17fc665a3bd844f50b4)(const struct [device](structdevice.md) \*port,

1261 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value);

1262

1263static inline int z\_impl\_gpio\_port\_get\_raw(const struct [device](structdevice.md) \*port, [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value)

1264{

1265 const struct gpio\_driver\_api \*api = (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1266 int ret;

1267

1268 [SYS\_PORT\_TRACING\_FUNC\_ENTER](group__subsys__tracing__macros.md#ga445bcac4cec53d560ddca757de17e1e3)(gpio\_port, get\_raw, port, value);

1269

1270 ret = api->port\_get\_raw(port, value);

1271 [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(gpio\_port, get\_raw, port, ret);

1272 return ret;

1273}

1274

[ 1293](group__gpio__interface.md#gae578c8163fb8fe5600d1ca9e5d7526b1)static inline int [gpio\_port\_get](group__gpio__interface.md#gae578c8163fb8fe5600d1ca9e5d7526b1)(const struct [device](structdevice.md) \*port,

1294 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value)

1295{

1296 const struct [gpio\_driver\_data](structgpio__driver__data.md) \*const data =

1297 (const struct [gpio\_driver\_data](structgpio__driver__data.md) \*)port->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

1298 int ret;

1299

1300 ret = [gpio\_port\_get\_raw](group__gpio__interface.md#gae2a49b36cae2e17fc665a3bd844f50b4)(port, value);

1301 if (ret == 0) {

1302 \*value ^= data->[invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169);

1303 }

1304

1305 return ret;

1306}

1307

[ 1325](group__gpio__interface.md#ga9e7b50d720fda362941acc1e3b3b2922)\_\_syscall int [gpio\_port\_set\_masked\_raw](group__gpio__interface.md#ga9e7b50d720fda362941acc1e3b3b2922)(const struct [device](structdevice.md) \*port,

1326 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask,

1327 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value);

1328

1329static inline int z\_impl\_gpio\_port\_set\_masked\_raw(const struct [device](structdevice.md) \*port,

1330 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask,

1331 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value)

1332{

1333 const struct gpio\_driver\_api \*api =

1334 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1335 int ret;

1336

1337 [SYS\_PORT\_TRACING\_FUNC\_ENTER](group__subsys__tracing__macros.md#ga445bcac4cec53d560ddca757de17e1e3)(gpio\_port, set\_masked\_raw, port, mask, value);

1338

1339 ret = api->port\_set\_masked\_raw(port, mask, value);

1340 [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(gpio\_port, set\_masked\_raw, port, ret);

1341 return ret;

1342}

1343

[ 1364](group__gpio__interface.md#gac653e70270019d599732ab78693dd1fd)static inline int [gpio\_port\_set\_masked](group__gpio__interface.md#gac653e70270019d599732ab78693dd1fd)(const struct [device](structdevice.md) \*port,

1365 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask,

1366 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value)

1367{

1368 const struct [gpio\_driver\_data](structgpio__driver__data.md) \*const data =

1369 (const struct [gpio\_driver\_data](structgpio__driver__data.md) \*)port->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

1370

1371 value ^= data->[invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169);

1372

1373 return [gpio\_port\_set\_masked\_raw](group__gpio__interface.md#ga9e7b50d720fda362941acc1e3b3b2922)(port, mask, value);

1374}

1375

[ 1386](group__gpio__interface.md#ga18e6ca0df95566fecc0633efb04a075a)\_\_syscall int [gpio\_port\_set\_bits\_raw](group__gpio__interface.md#ga18e6ca0df95566fecc0633efb04a075a)(const struct [device](structdevice.md) \*port,

1387 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

1388

1389static inline int z\_impl\_gpio\_port\_set\_bits\_raw(const struct [device](structdevice.md) \*port,

1390 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins)

1391{

1392 const struct gpio\_driver\_api \*api =

1393 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1394 int ret;

1395

1396 [SYS\_PORT\_TRACING\_FUNC\_ENTER](group__subsys__tracing__macros.md#ga445bcac4cec53d560ddca757de17e1e3)(gpio\_port, set\_bits\_raw, port, pins);

1397

1398 ret = api->port\_set\_bits\_raw(port, pins);

1399 [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(gpio\_port, set\_bits\_raw, port, ret);

1400 return ret;

1401}

1402

[ 1413](group__gpio__interface.md#ga570b669af237df991c4a55cff6ec3253)static inline int [gpio\_port\_set\_bits](group__gpio__interface.md#ga570b669af237df991c4a55cff6ec3253)(const struct [device](structdevice.md) \*port,

1414 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins)

1415{

1416 return [gpio\_port\_set\_masked](group__gpio__interface.md#gac653e70270019d599732ab78693dd1fd)(port, pins, pins);

1417}

1418

[ 1429](group__gpio__interface.md#ga9d2c9daeec7ce127fc786ead566ad27f)\_\_syscall int [gpio\_port\_clear\_bits\_raw](group__gpio__interface.md#ga9d2c9daeec7ce127fc786ead566ad27f)(const struct [device](structdevice.md) \*port,

1430 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

1431

1432static inline int z\_impl\_gpio\_port\_clear\_bits\_raw(const struct [device](structdevice.md) \*port,

1433 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins)

1434{

1435 const struct gpio\_driver\_api \*api =

1436 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1437 int ret;

1438

1439 [SYS\_PORT\_TRACING\_FUNC\_ENTER](group__subsys__tracing__macros.md#ga445bcac4cec53d560ddca757de17e1e3)(gpio\_port, clear\_bits\_raw, port, pins);

1440

1441 ret = api->port\_clear\_bits\_raw(port, pins);

1442 [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(gpio\_port, clear\_bits\_raw, port, ret);

1443 return ret;

1444}

1445

[ 1456](group__gpio__interface.md#gac1660707a44cc8a3aa08b25685b4b20b)static inline int [gpio\_port\_clear\_bits](group__gpio__interface.md#gac1660707a44cc8a3aa08b25685b4b20b)(const struct [device](structdevice.md) \*port,

1457 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins)

1458{

1459 return [gpio\_port\_set\_masked](group__gpio__interface.md#gac653e70270019d599732ab78693dd1fd)(port, pins, 0);

1460}

1461

[ 1472](group__gpio__interface.md#ga82977d8706fb9f464db455bd0e9ac2e4)\_\_syscall int [gpio\_port\_toggle\_bits](group__gpio__interface.md#ga82977d8706fb9f464db455bd0e9ac2e4)(const struct [device](structdevice.md) \*port,

1473 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

1474

1475static inline int z\_impl\_gpio\_port\_toggle\_bits(const struct [device](structdevice.md) \*port,

1476 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins)

1477{

1478 const struct gpio\_driver\_api \*api =

1479 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1480 int ret;

1481

1482 [SYS\_PORT\_TRACING\_FUNC\_ENTER](group__subsys__tracing__macros.md#ga445bcac4cec53d560ddca757de17e1e3)(gpio\_port, toggle\_bits, port, pins);

1483

1484 ret = api->port\_toggle\_bits(port, pins);

1485 [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(gpio\_port, toggle\_bits, port, ret);

1486 return ret;

1487}

1488

[ 1500](group__gpio__interface.md#ga6e7ca22e83a70d3ddcf0de068b377c2d)static inline int [gpio\_port\_set\_clr\_bits\_raw](group__gpio__interface.md#ga6e7ca22e83a70d3ddcf0de068b377c2d)(const struct [device](structdevice.md) \*port,

1501 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) set\_pins,

1502 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) clear\_pins)

1503{

1504 \_\_ASSERT((set\_pins & clear\_pins) == 0, "Set and Clear pins overlap");

1505

1506 return [gpio\_port\_set\_masked\_raw](group__gpio__interface.md#ga9e7b50d720fda362941acc1e3b3b2922)(port, set\_pins | clear\_pins, set\_pins);

1507}

1508

[ 1520](group__gpio__interface.md#ga77880d217f5dd1fc1c72ce791254449b)static inline int [gpio\_port\_set\_clr\_bits](group__gpio__interface.md#ga77880d217f5dd1fc1c72ce791254449b)(const struct [device](structdevice.md) \*port,

1521 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) set\_pins,

1522 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) clear\_pins)

1523{

1524 \_\_ASSERT((set\_pins & clear\_pins) == 0, "Set and Clear pins overlap");

1525

1526 return [gpio\_port\_set\_masked](group__gpio__interface.md#gac653e70270019d599732ab78693dd1fd)(port, set\_pins | clear\_pins, set\_pins);

1527}

1528

[ 1544](group__gpio__interface.md#ga0fc52723b78019258bb306c771c430a1)static inline int [gpio\_pin\_get\_raw](group__gpio__interface.md#ga0fc52723b78019258bb306c771c430a1)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin)

1545{

1546 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

1547 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1548 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value;

1549 int ret;

1550

1551 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

1552 "Unsupported pin");

1553

1554 ret = [gpio\_port\_get\_raw](group__gpio__interface.md#gae2a49b36cae2e17fc665a3bd844f50b4)(port, &value);

1555 if (ret == 0) {

1556 ret = (value & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0 ? 1 : 0;

1557 }

1558

1559 return ret;

1560}

1561

[ 1581](group__gpio__interface.md#ga154a4ea3d3084910f02df31dc0779be6)static inline int [gpio\_pin\_get](group__gpio__interface.md#ga154a4ea3d3084910f02df31dc0779be6)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin)

1582{

1583 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

1584 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1585 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value;

1586 int ret;

1587

1588 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

1589 "Unsupported pin");

1590

1591 ret = [gpio\_port\_get](group__gpio__interface.md#gae578c8163fb8fe5600d1ca9e5d7526b1)(port, &value);

1592 if (ret == 0) {

1593 ret = (value & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0 ? 1 : 0;

1594 }

1595

1596 return ret;

1597}

1598

[ 1609](group__gpio__interface.md#gaabeb2d0d98856c7ff78be36651d6bbc1)static inline int [gpio\_pin\_get\_dt](group__gpio__interface.md#gaabeb2d0d98856c7ff78be36651d6bbc1)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec)

1610{

1611 return [gpio\_pin\_get](group__gpio__interface.md#ga154a4ea3d3084910f02df31dc0779be6)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84));

1612}

1613

[ 1629](group__gpio__interface.md#gae28f0fa2576530083aa86d819d0d5cca)static inline int [gpio\_pin\_set\_raw](group__gpio__interface.md#gae28f0fa2576530083aa86d819d0d5cca)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

1630 int value)

1631{

1632 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

1633 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1634 int ret;

1635

1636 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

1637 "Unsupported pin");

1638

1639 if (value != 0) {

1640 ret = [gpio\_port\_set\_bits\_raw](group__gpio__interface.md#ga18e6ca0df95566fecc0633efb04a075a)(port, ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin));

1641 } else {

1642 ret = [gpio\_port\_clear\_bits\_raw](group__gpio__interface.md#ga9d2c9daeec7ce127fc786ead566ad27f)(port, ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin));

1643 }

1644

1645 return ret;

1646}

1647

[ 1669](group__gpio__interface.md#gabfab69282fb99be119760436f2d18a9b)static inline int [gpio\_pin\_set](group__gpio__interface.md#gabfab69282fb99be119760436f2d18a9b)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

1670 int value)

1671{

1672 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

1673 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1674 const struct [gpio\_driver\_data](structgpio__driver__data.md) \*const data =

1675 (const struct [gpio\_driver\_data](structgpio__driver__data.md) \*)port->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

1676

1677 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

1678 "Unsupported pin");

1679

1680 if (data->[invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) {

1681 value = (value != 0) ? 0 : 1;

1682 }

1683

1684 return [gpio\_pin\_set\_raw](group__gpio__interface.md#gae28f0fa2576530083aa86d819d0d5cca)(port, pin, value);

1685}

1686

[ 1698](group__gpio__interface.md#ga541064fb9e575c0c559c101754466fa8)static inline int [gpio\_pin\_set\_dt](group__gpio__interface.md#ga541064fb9e575c0c559c101754466fa8)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec, int value)

1699{

1700 return [gpio\_pin\_set](group__gpio__interface.md#gabfab69282fb99be119760436f2d18a9b)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84), value);

1701}

1702

[ 1713](group__gpio__interface.md#gaabf948471d313ff19410f1741dd16957)static inline int [gpio\_pin\_toggle](group__gpio__interface.md#gaabf948471d313ff19410f1741dd16957)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin)

1714{

1715 \_\_unused const struct [gpio\_driver\_config](structgpio__driver__config.md) \*const cfg =

1716 (const struct [gpio\_driver\_config](structgpio__driver__config.md) \*)port->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1717

1718 \_\_ASSERT((cfg->[port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052) & ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) != 0U,

1719 "Unsupported pin");

1720

1721 return [gpio\_port\_toggle\_bits](group__gpio__interface.md#ga82977d8706fb9f464db455bd0e9ac2e4)(port, ([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin));

1722}

1723

[ 1734](group__gpio__interface.md#ga3272e866489da6c2e12c48f803c59e81)static inline int [gpio\_pin\_toggle\_dt](group__gpio__interface.md#ga3272e866489da6c2e12c48f803c59e81)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec)

1735{

1736 return [gpio\_pin\_toggle](group__gpio__interface.md#gaabf948471d313ff19410f1741dd16957)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), spec->[pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84));

1737}

1738

[ 1745](group__gpio__interface.md#ga7a7dd7c1f3a2135a9f378e1c34b6232c)static inline void [gpio\_init\_callback](group__gpio__interface.md#ga7a7dd7c1f3a2135a9f378e1c34b6232c)(struct [gpio\_callback](structgpio__callback.md) \*callback,

1746 [gpio\_callback\_handler\_t](group__gpio__interface.md#gaf0aa40279d32b1b8332f2f23a39510af) handler,

1747 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pin\_mask)

1748{

1749 [SYS\_PORT\_TRACING\_FUNC\_ENTER](group__subsys__tracing__macros.md#ga445bcac4cec53d560ddca757de17e1e3)(gpio, init\_callback, callback, handler, pin\_mask);

1750

1751 \_\_ASSERT(callback, "Callback pointer should not be NULL");

1752 \_\_ASSERT(handler, "Callback handler pointer should not be NULL");

1753

1754 callback->[handler](structgpio__callback.md#af89dc41cbd610d81ac03cae7ab764ceb) = handler;

1755 callback->[pin\_mask](structgpio__callback.md#ace5c2b83f1d51f73877a1f2c54ba8c67) = pin\_mask;

1756

1757 [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(gpio, init\_callback, callback);

1758}

1759

[ 1774](group__gpio__interface.md#ga05fd15af20386d69f9332354285b0cca)static inline int [gpio\_add\_callback](group__gpio__interface.md#ga05fd15af20386d69f9332354285b0cca)(const struct [device](structdevice.md) \*port,

1775 struct [gpio\_callback](structgpio__callback.md) \*callback)

1776{

1777 const struct gpio\_driver\_api \*api =

1778 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1779 int ret;

1780

1781 [SYS\_PORT\_TRACING\_FUNC\_ENTER](group__subsys__tracing__macros.md#ga445bcac4cec53d560ddca757de17e1e3)(gpio, add\_callback, port, callback);

1782

1783 if (api->manage\_callback == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1784 [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(gpio, add\_callback, port, -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b));

1785 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1786 }

1787

1788 ret = api->manage\_callback(port, callback, true);

1789 [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(gpio, add\_callback, port, ret);

1790 return ret;

1791}

1792

[ 1804](group__gpio__interface.md#ga54845eb95bc9636c3e6ff285300b6979)static inline int [gpio\_add\_callback\_dt](group__gpio__interface.md#ga54845eb95bc9636c3e6ff285300b6979)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec,

1805 struct [gpio\_callback](structgpio__callback.md) \*callback)

1806{

1807 return [gpio\_add\_callback](group__gpio__interface.md#ga05fd15af20386d69f9332354285b0cca)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), callback);

1808}

1809

[ 1828](group__gpio__interface.md#gac1e94ba8faac79f469447e9b5d2f8c06)static inline int [gpio\_remove\_callback](group__gpio__interface.md#gac1e94ba8faac79f469447e9b5d2f8c06)(const struct [device](structdevice.md) \*port,

1829 struct [gpio\_callback](structgpio__callback.md) \*callback)

1830{

1831 const struct gpio\_driver\_api \*api =

1832 (const struct gpio\_driver\_api \*)port->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1833 int ret;

1834

1835 [SYS\_PORT\_TRACING\_FUNC\_ENTER](group__subsys__tracing__macros.md#ga445bcac4cec53d560ddca757de17e1e3)(gpio, remove\_callback, port, callback);

1836

1837 if (api->manage\_callback == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1838 [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(gpio, remove\_callback, port, -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b));

1839 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1840 }

1841

1842 ret = api->manage\_callback(port, callback, false);

1843 [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(gpio, remove\_callback, port, ret);

1844 return ret;

1845}

1846

[ 1858](group__gpio__interface.md#ga2c9f8fee2addfc0aeeeeb011d534f304)static inline int [gpio\_remove\_callback\_dt](group__gpio__interface.md#ga2c9f8fee2addfc0aeeeeb011d534f304)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec,

1859 struct [gpio\_callback](structgpio__callback.md) \*callback)

1860{

1861 return [gpio\_remove\_callback](group__gpio__interface.md#gac1e94ba8faac79f469447e9b5d2f8c06)(spec->[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f), callback);

1862}

1863

[ 1878](group__gpio__interface.md#ga3f9e45de172a27f49c31a072c0c241e1)\_\_syscall int [gpio\_get\_pending\_int](group__gpio__interface.md#ga3f9e45de172a27f49c31a072c0c241e1)(const struct [device](structdevice.md) \*dev);

1879

1880static inline int z\_impl\_gpio\_get\_pending\_int(const struct [device](structdevice.md) \*dev)

1881{

1882 const struct gpio\_driver\_api \*api =

1883 (const struct gpio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1884 int ret;

1885

1886 [SYS\_PORT\_TRACING\_FUNC\_ENTER](group__subsys__tracing__macros.md#ga445bcac4cec53d560ddca757de17e1e3)(gpio, get\_pending\_int, dev);

1887

1888 if (api->get\_pending\_int == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1889 [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(gpio, get\_pending\_int, dev, -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b));

1890 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1891 }

1892

1893 ret = api->get\_pending\_int(dev);

1894 [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(gpio, get\_pending\_int, dev, ret);

1895 return ret;

1896}

1897

1901

1902#ifdef \_\_cplusplus

1903}

1904#endif

1905

1906#include <zephyr/syscalls/gpio.h>

1907

1908#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_H\_ \*/

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

**Definition** gpio.h:1774

[GPIO\_OUTPUT](group__gpio__interface.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)

#define GPIO\_OUTPUT

Enables pin as output, no change to the output state.

**Definition** gpio.h:51

[gpio\_pin\_get\_raw](group__gpio__interface.md#ga0fc52723b78019258bb306c771c430a1)

static int gpio\_pin\_get\_raw(const struct device \*port, gpio\_pin\_t pin)

Get physical level of an input pin.

**Definition** gpio.h:1544

[gpio\_pin\_get\_config](group__gpio__interface.md#ga133284b60a13c6dc50b87c1d04259f5e)

int gpio\_pin\_get\_config(const struct device \*port, gpio\_pin\_t pin, gpio\_flags\_t \*flags)

Get a configuration of a single pin.

[gpio\_pin\_is\_input](group__gpio__interface.md#ga1454bc223fc2200aff3c4aab7d747da2)

static int gpio\_pin\_is\_input(const struct device \*port, gpio\_pin\_t pin)

Check if pin is configured for input.

**Definition** gpio.h:1107

[gpio\_pin\_get](group__gpio__interface.md#ga154a4ea3d3084910f02df31dc0779be6)

static int gpio\_pin\_get(const struct device \*port, gpio\_pin\_t pin)

Get logical level of an input pin.

**Definition** gpio.h:1581

[gpio\_port\_set\_bits\_raw](group__gpio__interface.md#ga18e6ca0df95566fecc0633efb04a075a)

int gpio\_port\_set\_bits\_raw(const struct device \*port, gpio\_port\_pins\_t pins)

Set physical level of selected output pins to high.

[gpio\_pin\_is\_output\_dt](group__gpio__interface.md#ga2255c5681d17952ab89a4b6016d8e80d)

static int gpio\_pin\_is\_output\_dt(const struct gpio\_dt\_spec \*spec)

Check if a single pin from gpio\_dt\_spec is configured for output.

**Definition** gpio.h:1180

[gpio\_pin\_interrupt\_configure\_dt](group__gpio__interface.md#ga24f0b4ad30e6a8c81f51a2813478c793)

static int gpio\_pin\_interrupt\_configure\_dt(const struct gpio\_dt\_spec \*spec, gpio\_flags\_t flags)

Configure pin interrupts from a gpio\_dt\_spec.

**Definition** gpio.h:952

[gpio\_remove\_callback\_dt](group__gpio__interface.md#ga2c9f8fee2addfc0aeeeeb011d534f304)

static int gpio\_remove\_callback\_dt(const struct gpio\_dt\_spec \*spec, struct gpio\_callback \*callback)

Remove an application callback.

**Definition** gpio.h:1858

[gpio\_pin\_toggle\_dt](group__gpio__interface.md#ga3272e866489da6c2e12c48f803c59e81)

static int gpio\_pin\_toggle\_dt(const struct gpio\_dt\_spec \*spec)

Toggle pin level from a gpio\_dt\_spec.

**Definition** gpio.h:1734

[gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34)

uint8\_t gpio\_pin\_t

Provides a type to hold a GPIO pin index.

**Definition** gpio.h:255

[gpio\_pin\_is\_output](group__gpio__interface.md#ga3b854d759180e222299ea445b401acc1)

static int gpio\_pin\_is\_output(const struct device \*port, gpio\_pin\_t pin)

Check if pin is configured for output.

**Definition** gpio.h:1152

[gpio\_get\_pending\_int](group__gpio__interface.md#ga3f9e45de172a27f49c31a072c0c241e1)

int gpio\_get\_pending\_int(const struct device \*dev)

Function to get pending interrupts.

[gpio\_pin\_configure\_dt](group__gpio__interface.md#ga423db4f985098ddcaa504ec430e91913)

static int gpio\_pin\_configure\_dt(const struct gpio\_dt\_spec \*spec, gpio\_flags\_t extra\_flags)

Configure a single pin from a gpio\_dt\_spec and some extra flags.

**Definition** gpio.h:1045

[gpio\_pin\_set\_dt](group__gpio__interface.md#ga541064fb9e575c0c559c101754466fa8)

static int gpio\_pin\_set\_dt(const struct gpio\_dt\_spec \*spec, int value)

Set logical level of a output pin from a gpio\_dt\_spec.

**Definition** gpio.h:1698

[gpio\_add\_callback\_dt](group__gpio__interface.md#ga54845eb95bc9636c3e6ff285300b6979)

static int gpio\_add\_callback\_dt(const struct gpio\_dt\_spec \*spec, struct gpio\_callback \*callback)

Add an application callback.

**Definition** gpio.h:1804

[gpio\_port\_set\_bits](group__gpio__interface.md#ga570b669af237df991c4a55cff6ec3253)

static int gpio\_port\_set\_bits(const struct device \*port, gpio\_port\_pins\_t pins)

Set logical level of selected output pins to active.

**Definition** gpio.h:1413

[gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e)

uint32\_t gpio\_flags\_t

Provides a type to hold GPIO configuration flags.

**Definition** gpio.h:275

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

**Definition** gpio.h:1500

[gpio\_port\_set\_clr\_bits](group__gpio__interface.md#ga77880d217f5dd1fc1c72ce791254449b)

static int gpio\_port\_set\_clr\_bits(const struct device \*port, gpio\_port\_pins\_t set\_pins, gpio\_port\_pins\_t clear\_pins)

Set logical level of selected output pins.

**Definition** gpio.h:1520

[gpio\_init\_callback](group__gpio__interface.md#ga7a7dd7c1f3a2135a9f378e1c34b6232c)

static void gpio\_init\_callback(struct gpio\_callback \*callback, gpio\_callback\_handler\_t handler, gpio\_port\_pins\_t pin\_mask)

Helper to initialize a struct gpio\_callback properly.

**Definition** gpio.h:1745

[gpio\_pin\_is\_input\_dt](group__gpio__interface.md#ga7aaec28a83cac63bd87fc94cc72664b1)

static int gpio\_pin\_is\_input\_dt(const struct gpio\_dt\_spec \*spec)

Check if a single pin from gpio\_dt\_spec is configured for input.

**Definition** gpio.h:1135

[GPIO\_INPUT](group__gpio__interface.md#ga7be6a0cc9aa65da1d4ee5751b4085853)

#define GPIO\_INPUT

Enables pin as input.

**Definition** gpio.h:48

[gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f)

uint32\_t gpio\_port\_pins\_t

Identifies a set of pins associated with a port.

**Definition** gpio.h:234

[gpio\_pin\_get\_config\_dt](group__gpio__interface.md#ga820448aa4be8b14839bc6a00c9f34bb4)

static int gpio\_pin\_get\_config\_dt(const struct gpio\_dt\_spec \*spec, gpio\_flags\_t \*flags)

Get a configuration of a single pin from a gpio\_dt\_spec.

**Definition** gpio.h:1237

[gpio\_port\_toggle\_bits](group__gpio__interface.md#ga82977d8706fb9f464db455bd0e9ac2e4)

int gpio\_port\_toggle\_bits(const struct device \*port, gpio\_port\_pins\_t pins)

Toggle level of selected output pins.

[GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a)

#define GPIO\_INT\_DISABLE

Disables GPIO pin interrupt.

**Definition** gpio.h:101

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

**Definition** gpio.h:1609

[gpio\_pin\_toggle](group__gpio__interface.md#gaabf948471d313ff19410f1741dd16957)

static int gpio\_pin\_toggle(const struct device \*port, gpio\_pin\_t pin)

Toggle pin level.

**Definition** gpio.h:1713

[gpio\_is\_ready\_dt](group__gpio__interface.md#gaaec9ad17c08a0d527d66445fe82d8327)

static bool gpio\_is\_ready\_dt(const struct gpio\_dt\_spec \*spec)

Validate that GPIO port is ready.

**Definition** gpio.h:837

[gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693)

uint32\_t gpio\_port\_value\_t

Provides values for a set of pins associated with a port.

**Definition** gpio.h:247

[gpio\_pin\_set](group__gpio__interface.md#gabfab69282fb99be119760436f2d18a9b)

static int gpio\_pin\_set(const struct device \*port, gpio\_pin\_t pin, int value)

Set logical level of an output pin.

**Definition** gpio.h:1669

[gpio\_port\_clear\_bits](group__gpio__interface.md#gac1660707a44cc8a3aa08b25685b4b20b)

static int gpio\_port\_clear\_bits(const struct device \*port, gpio\_port\_pins\_t pins)

Set logical level of selected output pins to inactive.

**Definition** gpio.h:1456

[gpio\_remove\_callback](group__gpio__interface.md#gac1e94ba8faac79f469447e9b5d2f8c06)

static int gpio\_remove\_callback(const struct device \*port, struct gpio\_callback \*callback)

Remove an application callback.

**Definition** gpio.h:1828

[gpio\_port\_set\_masked](group__gpio__interface.md#gac653e70270019d599732ab78693dd1fd)

static int gpio\_port\_set\_masked(const struct device \*port, gpio\_port\_pins\_t mask, gpio\_port\_value\_t value)

Set logical level of output pins in a port.

**Definition** gpio.h:1364

[gpio\_port\_get\_direction](group__gpio__interface.md#gad2b2945dbe6987ac425e000721a894c4)

int gpio\_port\_get\_direction(const struct device \*port, gpio\_port\_pins\_t map, gpio\_port\_pins\_t \*inputs, gpio\_port\_pins\_t \*outputs)

Get direction of select pins in a port.

[gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2)

uint16\_t gpio\_dt\_flags\_t

Provides a type to hold GPIO devicetree flags.

**Definition** gpio.h:267

[GPIO\_PULL\_DOWN](group__gpio__interface.md#gadec1802e074f3021d464da09cd66c7cf)

#define GPIO\_PULL\_DOWN

Enable GPIO pin pull-down.

**Definition** gpio.h:78

[gpio\_pin\_set\_raw](group__gpio__interface.md#gae28f0fa2576530083aa86d819d0d5cca)

static int gpio\_pin\_set\_raw(const struct device \*port, gpio\_pin\_t pin, int value)

Set physical level of an output pin.

**Definition** gpio.h:1629

[gpio\_port\_get\_raw](group__gpio__interface.md#gae2a49b36cae2e17fc665a3bd844f50b4)

int gpio\_port\_get\_raw(const struct device \*port, gpio\_port\_value\_t \*value)

Get physical level of all input pins in a port.

[gpio\_port\_get](group__gpio__interface.md#gae578c8163fb8fe5600d1ca9e5d7526b1)

static int gpio\_port\_get(const struct device \*port, gpio\_port\_value\_t \*value)

Get logical level of all input pins in a port.

**Definition** gpio.h:1293

[gpio\_pin\_configure](group__gpio__interface.md#gaed4a2051d76db7eead8ed1719ce2ba33)

int gpio\_pin\_configure(const struct device \*port, gpio\_pin\_t pin, gpio\_flags\_t flags)

Configure a single pin.

[gpio\_callback\_handler\_t](group__gpio__interface.md#gaf0aa40279d32b1b8332f2f23a39510af)

void(\* gpio\_callback\_handler\_t)(const struct device \*port, struct gpio\_callback \*cb, gpio\_port\_pins\_t pins)

Define the application callback handler function signature.

**Definition** gpio.h:727

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[SYS\_PORT\_TRACING\_FUNC\_ENTER](group__subsys__tracing__macros.md#ga445bcac4cec53d560ddca757de17e1e3)

#define SYS\_PORT\_TRACING\_FUNC\_ENTER(type, func,...)

Tracing macro for the entry into a function that might or might not return a value.

**Definition** tracing\_macros.h:248

[SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)

#define SYS\_PORT\_TRACING\_FUNC\_EXIT(type, func,...)

Tracing macro for when a function ends its execution.

**Definition** tracing\_macros.h:274

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[types.h](include_2zephyr_2types_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

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

**Definition** device.h:453

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:463

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[device::config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc)

const void \* config

Address of device instance config information.

**Definition** device.h:457

[gpio\_callback](structgpio__callback.md)

GPIO callback structure.

**Definition** gpio.h:741

[gpio\_callback::node](structgpio__callback.md#ab60e7093072964bd818d536c746211e4)

sys\_snode\_t node

This is meant to be used in the driver and the user should not mess with it (see drivers/gpio/gpio\_ut...

**Definition** gpio.h:745

[gpio\_callback::pin\_mask](structgpio__callback.md#ace5c2b83f1d51f73877a1f2c54ba8c67)

gpio\_port\_pins\_t pin\_mask

A mask of pins the callback is interested in, if 0 the callback will never be called.

**Definition** gpio.h:756

[gpio\_callback::handler](structgpio__callback.md#af89dc41cbd610d81ac03cae7ab764ceb)

gpio\_callback\_handler\_t handler

Actual callback function being called when relevant.

**Definition** gpio.h:748

[gpio\_driver\_config](structgpio__driver__config.md)

This structure is common to all GPIO drivers and is expected to be the first element in the object po...

**Definition** gpio.h:691

[gpio\_driver\_config::port\_pin\_mask](structgpio__driver__config.md#af73c0d9d433b86b9d0e0c6703e737052)

gpio\_port\_pins\_t port\_pin\_mask

Mask identifying pins supported by the controller.

**Definition** gpio.h:697

[gpio\_driver\_data](structgpio__driver__data.md)

This structure is common to all GPIO drivers and is expected to be the first element in the driver's ...

**Definition** gpio.h:704

[gpio\_driver\_data::invert](structgpio__driver__data.md#ab62038a3c7c341cafda6665dfab3f169)

gpio\_port\_pins\_t invert

Mask identifying pins that are configured as active low.

**Definition** gpio.h:710

[gpio\_dt\_spec](structgpio__dt__spec.md)

Container for GPIO pin information specified in devicetree.

**Definition** gpio.h:289

[gpio\_dt\_spec::port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f)

const struct device \* port

GPIO device controlling the pin.

**Definition** gpio.h:291

[gpio\_dt\_spec::pin](structgpio__dt__spec.md#ad7e6fbb0cba0be94a47d4f2add056c84)

gpio\_pin\_t pin

The pin's number on the device.

**Definition** gpio.h:293

[gpio\_dt\_spec::dt\_flags](structgpio__dt__spec.md#ae3b90e7e22708798c67da94f72ad1ab0)

gpio\_dt\_flags\_t dt\_flags

The pin's configuration flags as specified in devicetree.

**Definition** gpio.h:295

[tracing.h](tracing_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio.h](drivers_2gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
