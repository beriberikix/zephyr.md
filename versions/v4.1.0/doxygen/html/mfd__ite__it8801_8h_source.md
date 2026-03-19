---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mfd__ite__it8801_8h_source.html
original_path: doxygen/html/mfd__ite__it8801_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mfd\_ite\_it8801.h

[Go to the documentation of this file.](mfd__ite__it8801_8h.md)

1/\*

2 \* Copyright (c) 2024 ITE Corporation. All Rights Reserved.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_ITE\_IT8801\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_ITE\_IT8801\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

14/\*

15 \* IC clock and power management controller register fields

16 \*/

17/\* 0xf9: Gather interrupt status register \*/

[ 18](mfd__ite__it8801_8h.md#af769928fba020583c1aacafc3ef3f661)#define IT8801\_REG\_GISR 0xf9

[ 19](mfd__ite__it8801_8h.md#a19097fcc347d262a8b970c447caeda8a)#define IT8801\_REG\_MASK\_GISR\_GKSIIS BIT(6)

20/\* 0xfb: Gather interrupt enable control register \*/

[ 21](mfd__ite__it8801_8h.md#abb4de1bff69302bdff8e6420eaf0bdc1)#define IT8801\_REG\_GIECR 0xfb

[ 22](mfd__ite__it8801_8h.md#a13e7af4eccface18b7e8d8fc782896b7)#define IT8801\_REG\_MASK\_GKSIIE BIT(3)

[ 23](mfd__ite__it8801_8h.md#ace92908cb46e1436279fb02216cd5021)#define IT8801\_REG\_MASK\_GGPIOIE BIT(2)

24

25/\*

26 \* General control register fields

27 \*/

[ 28](mfd__ite__it8801_8h.md#a722c1dbea588a3559edac523462dd755)#define IT8801\_REG\_LBVIDR 0xfe

[ 29](mfd__ite__it8801_8h.md#aff5dcc74423dba3bad5693ec5e7d34be)#define IT8801\_REG\_HBVIDR 0xff

30

[ 31](structit8801__vendor__id__t.md)struct [it8801\_vendor\_id\_t](structit8801__vendor__id__t.md) {

[ 32](structit8801__vendor__id__t.md#acb0a39c8e89593d6f45fe1089266bb85) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [chip\_id](structit8801__vendor__id__t.md#acb0a39c8e89593d6f45fe1089266bb85);

[ 33](structit8801__vendor__id__t.md#a384a9ea2a5d2d025473d672c2a0074ae) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reg](structit8801__vendor__id__t.md#a384a9ea2a5d2d025473d672c2a0074ae);

34};

35

[ 36](mfd__ite__it8801_8h.md#a0e013175c1b2fd6ff3b62fb6eb3512ce)static const struct [it8801\_vendor\_id\_t](structit8801__vendor__id__t.md) [it8801\_id\_verify](mfd__ite__it8801_8h.md#a0e013175c1b2fd6ff3b62fb6eb3512ce)[] = {

37 {0x12, [IT8801\_REG\_HBVIDR](mfd__ite__it8801_8h.md#aff5dcc74423dba3bad5693ec5e7d34be)},

38 {0x83, [IT8801\_REG\_LBVIDR](mfd__ite__it8801_8h.md#a722c1dbea588a3559edac523462dd755)},

39};

40

41/\*

42 \* SMbus interface register fields

43 \*/

44/\* 0xfa: SMBus control register \*/

[ 45](mfd__ite__it8801_8h.md#af823bba3625871e586765885dc88ddc1)#define IT8801\_REG\_SMBCR 0xfa

[ 46](mfd__ite__it8801_8h.md#aa974608857370407d8fcbdbda3c474bd)#define IT8801\_REG\_MASK\_ARE BIT(4)

47

48/\*

49 \* GPIO register fields

50 \*/

[ 51](mfd__ite__it8801_8h.md#aa93ce4f29ad9b4d9aeedfa3974c621b2)#define IT8801\_GPIOAFS\_FUN1 0x0

[ 52](mfd__ite__it8801_8h.md#a412905632e67c8ff0a00d6a366ad5bf2)#define IT8801\_GPIOAFS\_FUN2 0x01

[ 53](mfd__ite__it8801_8h.md#a7a49cf897e723f57f7ce6aa030f890d5)#define IT8801\_GPIOAFS\_FUN3 0x02

54/\* GPIO control register \*/

55/\* GPIO direction \*/

[ 56](mfd__ite__it8801_8h.md#a203d08ead5b60a5d51a66d550328aef6)#define IT8801\_GPIODIR BIT(5)

57/\* GPIO input and output type \*/

[ 58](mfd__ite__it8801_8h.md#afb02201d261e416846e28af181ef75b6)#define IT8801\_GPIOIOT\_OD BIT(4)

[ 59](mfd__ite__it8801_8h.md#aca84886b619af7cd79d0b9cb27e16650)#define IT8801\_GPIOIOT\_INT\_FALL BIT(4)

[ 60](mfd__ite__it8801_8h.md#ad951ae2431f554ed5582ce74fa90c9f5)#define IT8801\_GPIOIOT\_INT\_RISE BIT(3)

61/\* GPIO polarity \*/

[ 62](mfd__ite__it8801_8h.md#a6a7ab8ecd064bf59f0b0d8ab3b5b2bf8)#define IT8801\_GPIOPOL BIT(2)

63/\* GPIO pull-down enable \*/

[ 64](mfd__ite__it8801_8h.md#a1a516610506e0cbc06fe2b90748b8f19)#define IT8801\_GPIOPDE BIT(1)

65/\* GPIO pull-up enable \*/

[ 66](mfd__ite__it8801_8h.md#a526c4b693f64f9592f59221019bbb1e1)#define IT8801\_GPIOPUE BIT(0)

67

68/\*

69 \* Keyboard matrix scan controller register fields

70 \*/

71/\* 0x40: Keyboard scan out mode control register \*/

[ 72](mfd__ite__it8801_8h.md#a3ae2764c10f499cc3b9721eeb947b5b9)#define IT8801\_REG\_MASK\_KSOSDIC BIT(7)

[ 73](mfd__ite__it8801_8h.md#a7664d5e95b800c5eb1dc728f72e7c232)#define IT8801\_REG\_MASK\_KSE BIT(6)

[ 74](mfd__ite__it8801_8h.md#aa5ffc9da4d8e8ae737735d39d6c97e7a)#define IT8801\_REG\_MASK\_AKSOSC BIT(5)

75

76/\*

77 \* PWM register fields

78 \*/

[ 79](mfd__ite__it8801_8h.md#a08d8cff79844be2e179d1742222e9e3c)#define PWM\_IT8801\_FREQ 32895

80/\* Control push-pull flag \*/

[ 81](mfd__ite__it8801_8h.md#aab85a1fc0640f5eb243d098436d910fd)#define PWM\_IT8801\_PUSH\_PULL BIT(8)

82/\* 0x5f: PWM output open-drain disable register \*/

[ 83](mfd__ite__it8801_8h.md#ab6d8db36c938a43fd204fef6fc6bf28e)#define IT8801\_REG\_PWMODDSR 0x5f

84/\* PWM mode control register \*/

[ 85](mfd__ite__it8801_8h.md#af943264d205ae66f691a934dc7598f79)#define IT8801\_PWMMCR\_MCR\_MASK GENMASK(1, 0)

[ 86](mfd__ite__it8801_8h.md#adb356e532725450d445ff14258875f54)#define IT8801\_PWMMCR\_MCR\_OFF 0

[ 87](mfd__ite__it8801_8h.md#a6609e354ecb0b18e376cbc58092f537a)#define IT8801\_PWMMCR\_MCR\_BLINKING 1

[ 88](mfd__ite__it8801_8h.md#a8e3d5f1c472ce31913e4053f3a7b1d70)#define IT8801\_PWMMCR\_MCR\_BREATHING 2

[ 89](mfd__ite__it8801_8h.md#a5fda70da82cd203efa8be58d437eab8b)#define IT8801\_PWMMCR\_MCR\_ON 3

90

91/\*

92 \* For IT8801 MFD alternate function controller

93 \*/

[ 94](mfd__ite__it8801_8h.md#aa9d6f1d7fc9b16a6137e1ccaed2ae497)#define IT8801\_DT\_INST\_MFDCTRL(inst, idx) DT\_INST\_PHANDLE\_BY\_IDX(inst, mfdctrl, idx)

95

[ 96](mfd__ite__it8801_8h.md#aa16440b852beb0b839c23312d817fca1)#define IT8801\_DT\_INST\_MFDCTRL\_LEN(inst) DT\_INST\_PROP\_LEN\_OR(inst, mfdctrl, 0)

97

[ 98](mfd__ite__it8801_8h.md#a8198cb9c55c8f068192dd715099d5d92)#define IT8801\_DEV\_MFD(idx, inst) \

99 DEVICE\_DT\_GET(DT\_PHANDLE(IT8801\_DT\_INST\_MFDCTRL(inst, idx), altctrls))

[ 100](mfd__ite__it8801_8h.md#aef92aa44c116c58f283f7185167085b6)#define IT8801\_DEV\_MFD\_PIN(idx, inst) DT\_PHA(IT8801\_DT\_INST\_MFDCTRL(inst, idx), altctrls, pin)

[ 101](mfd__ite__it8801_8h.md#a7628a888ab7ba6187a7aadfb9f4af256)#define IT8801\_DEV\_MFD\_FUNC(idx, inst) DT\_PHA(IT8801\_DT\_INST\_MFDCTRL(inst, idx), altctrls, alt\_func)

102

[ 103](mfd__ite__it8801_8h.md#afa5b636e82b01d8d9c631f1ccb6823ed)#define IT8801\_DT\_MFD\_ITEMS\_FUNC(idx, inst) \

104 { \

105 .gpiocr = IT8801\_DEV\_MFD(idx, inst), \

106 .pin = IT8801\_DEV\_MFD\_PIN(idx, inst), \

107 .alt\_func = IT8801\_DEV\_MFD\_FUNC(idx, inst), \

108 }

109

[ 110](mfd__ite__it8801_8h.md#a3a2f4c469264e7dc90dc78ae22bd5147)#define IT8801\_DT\_MFD\_ITEMS\_LIST(inst) \

111 {LISTIFY(IT8801\_DT\_INST\_MFDCTRL\_LEN(inst), \

112 IT8801\_DT\_MFD\_ITEMS\_FUNC, (,), \

113 inst) }

114

115/\*

116 \* Configure alternate function pin

117 \*/

[ 118](mfd__ite__it8801_8h.md#a7273a553c04ac94c8adf244f1935b0ef)int [mfd\_it8801\_configure\_pins](mfd__ite__it8801_8h.md#a7273a553c04ac94c8adf244f1935b0ef)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*i2c\_dev, const struct [device](structdevice.md) \*dev,

119 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) func);

120

121/\* Define the IT8801 MFD interrupt callback function handler \*/

[ 122](mfd__ite__it8801_8h.md#a50e301d4cfb9211625e851b0cc40f130)typedef void (\*[it8801\_callback\_handler\_t](mfd__ite__it8801_8h.md#a50e301d4cfb9211625e851b0cc40f130))(const struct [device](structdevice.md) \*dev);

123

[ 124](structit8801__mfd__callback.md)struct [it8801\_mfd\_callback](structit8801__mfd__callback.md) {

[ 125](structit8801__mfd__callback.md#ab9b86565265e5f8c7409e44b559732ea) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structit8801__mfd__callback.md#ab9b86565265e5f8c7409e44b559732ea);

[ 126](structit8801__mfd__callback.md#a859a3813a936433024681903bc951b7d) [it8801\_callback\_handler\_t](mfd__ite__it8801_8h.md#a50e301d4cfb9211625e851b0cc40f130) [cb](structit8801__mfd__callback.md#a859a3813a936433024681903bc951b7d);

[ 127](structit8801__mfd__callback.md#a9d4df8a0ba22f560bb799a1945a73592) const struct [device](structdevice.md) \*[dev](structit8801__mfd__callback.md#a9d4df8a0ba22f560bb799a1945a73592);

128};

129/\* Register the interrupt of IT8801 MFD callback function \*/

[ 130](mfd__ite__it8801_8h.md#aeb61b0b4514fc757a016b8502ed58c09)void [mfd\_it8801\_register\_interrupt\_callback](mfd__ite__it8801_8h.md#aeb61b0b4514fc757a016b8502ed58c09)(const struct [device](structdevice.md) \*mfd,

131 struct [it8801\_mfd\_callback](structit8801__mfd__callback.md) \*callback);

132

133#ifdef \_\_cplusplus

134}

135#endif

136

137#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_ITE\_IT8801\_H\_ \*/

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[it8801\_id\_verify](mfd__ite__it8801_8h.md#a0e013175c1b2fd6ff3b62fb6eb3512ce)

static const struct it8801\_vendor\_id\_t it8801\_id\_verify[]

**Definition** mfd\_ite\_it8801.h:36

[it8801\_callback\_handler\_t](mfd__ite__it8801_8h.md#a50e301d4cfb9211625e851b0cc40f130)

void(\* it8801\_callback\_handler\_t)(const struct device \*dev)

**Definition** mfd\_ite\_it8801.h:122

[IT8801\_REG\_LBVIDR](mfd__ite__it8801_8h.md#a722c1dbea588a3559edac523462dd755)

#define IT8801\_REG\_LBVIDR

**Definition** mfd\_ite\_it8801.h:28

[mfd\_it8801\_configure\_pins](mfd__ite__it8801_8h.md#a7273a553c04ac94c8adf244f1935b0ef)

int mfd\_it8801\_configure\_pins(const struct i2c\_dt\_spec \*i2c\_dev, const struct device \*dev, uint8\_t pin, uint8\_t func)

[mfd\_it8801\_register\_interrupt\_callback](mfd__ite__it8801_8h.md#aeb61b0b4514fc757a016b8502ed58c09)

void mfd\_it8801\_register\_interrupt\_callback(const struct device \*mfd, struct it8801\_mfd\_callback \*callback)

[IT8801\_REG\_HBVIDR](mfd__ite__it8801_8h.md#aff5dcc74423dba3bad5693ec5e7d34be)

#define IT8801\_REG\_HBVIDR

**Definition** mfd\_ite\_it8801.h:29

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[i2c\_dt\_spec](structi2c__dt__spec.md)

Complete I2C DT information.

**Definition** i2c.h:77

[it8801\_mfd\_callback](structit8801__mfd__callback.md)

**Definition** mfd\_ite\_it8801.h:124

[it8801\_mfd\_callback::cb](structit8801__mfd__callback.md#a859a3813a936433024681903bc951b7d)

it8801\_callback\_handler\_t cb

**Definition** mfd\_ite\_it8801.h:126

[it8801\_mfd\_callback::dev](structit8801__mfd__callback.md#a9d4df8a0ba22f560bb799a1945a73592)

const struct device \* dev

**Definition** mfd\_ite\_it8801.h:127

[it8801\_mfd\_callback::node](structit8801__mfd__callback.md#ab9b86565265e5f8c7409e44b559732ea)

sys\_snode\_t node

**Definition** mfd\_ite\_it8801.h:125

[it8801\_vendor\_id\_t](structit8801__vendor__id__t.md)

**Definition** mfd\_ite\_it8801.h:31

[it8801\_vendor\_id\_t::reg](structit8801__vendor__id__t.md#a384a9ea2a5d2d025473d672c2a0074ae)

uint8\_t reg

**Definition** mfd\_ite\_it8801.h:33

[it8801\_vendor\_id\_t::chip\_id](structit8801__vendor__id__t.md#acb0a39c8e89593d6f45fe1089266bb85)

uint8\_t chip\_id

**Definition** mfd\_ite\_it8801.h:32

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [mfd\_ite\_it8801.h](mfd__ite__it8801_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
