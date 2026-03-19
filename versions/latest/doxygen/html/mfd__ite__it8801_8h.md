---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mfd__ite__it8801_8h.html
original_path: doxygen/html/mfd__ite__it8801_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mfd\_ite\_it8801.h File Reference

[Go to the source code of this file.](mfd__ite__it8801_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [it8801\_vendor\_id\_t](structit8801__vendor__id__t.md) |
| struct | [it8801\_mfd\_callback](structit8801__mfd__callback.md) |

| Macros | |
| --- | --- |
| #define | [IT8801\_REG\_GISR](#af769928fba020583c1aacafc3ef3f661)   0xf9 |
| #define | [IT8801\_REG\_MASK\_GISR\_GKSIIS](#a19097fcc347d262a8b970c447caeda8a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [IT8801\_REG\_GIECR](#abb4de1bff69302bdff8e6420eaf0bdc1)   0xfb |
| #define | [IT8801\_REG\_MASK\_GKSIIE](#a13e7af4eccface18b7e8d8fc782896b7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [IT8801\_REG\_MASK\_GGPIOIE](#ace92908cb46e1436279fb02216cd5021)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [IT8801\_REG\_LBVIDR](#a722c1dbea588a3559edac523462dd755)   0xfe |
| #define | [IT8801\_REG\_HBVIDR](#aff5dcc74423dba3bad5693ec5e7d34be)   0xff |
| #define | [IT8801\_REG\_SMBCR](#af823bba3625871e586765885dc88ddc1)   0xfa |
| #define | [IT8801\_REG\_MASK\_ARE](#aa974608857370407d8fcbdbda3c474bd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [IT8801\_GPIOAFS\_FUN1](#aa93ce4f29ad9b4d9aeedfa3974c621b2)   0x0 |
| #define | [IT8801\_GPIOAFS\_FUN2](#a412905632e67c8ff0a00d6a366ad5bf2)   0x01 |
| #define | [IT8801\_GPIOAFS\_FUN3](#a7a49cf897e723f57f7ce6aa030f890d5)   0x02 |
| #define | [IT8801\_GPIODIR](#a203d08ead5b60a5d51a66d550328aef6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [IT8801\_GPIOIOT\_OD](#afb02201d261e416846e28af181ef75b6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [IT8801\_GPIOIOT\_INT\_FALL](#aca84886b619af7cd79d0b9cb27e16650)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [IT8801\_GPIOIOT\_INT\_RISE](#ad951ae2431f554ed5582ce74fa90c9f5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [IT8801\_GPIOPOL](#a6a7ab8ecd064bf59f0b0d8ab3b5b2bf8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [IT8801\_GPIOPDE](#a1a516610506e0cbc06fe2b90748b8f19)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [IT8801\_GPIOPUE](#a526c4b693f64f9592f59221019bbb1e1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [IT8801\_REG\_MASK\_KSOSDIC](#a3ae2764c10f499cc3b9721eeb947b5b9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [IT8801\_REG\_MASK\_KSE](#a7664d5e95b800c5eb1dc728f72e7c232)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [IT8801\_REG\_MASK\_AKSOSC](#aa5ffc9da4d8e8ae737735d39d6c97e7a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [PWM\_IT8801\_FREQ](#a08d8cff79844be2e179d1742222e9e3c)   32895 |
| #define | [PWM\_IT8801\_PUSH\_PULL](#aab85a1fc0640f5eb243d098436d910fd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| #define | [IT8801\_REG\_PWMODDSR](#ab6d8db36c938a43fd204fef6fc6bf28e)   0x5f |
| #define | [IT8801\_PWMMCR\_MCR\_MASK](#af943264d205ae66f691a934dc7598f79)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(1, 0) |
| #define | [IT8801\_PWMMCR\_MCR\_OFF](#adb356e532725450d445ff14258875f54)   0 |
| #define | [IT8801\_PWMMCR\_MCR\_BLINKING](#a6609e354ecb0b18e376cbc58092f537a)   1 |
| #define | [IT8801\_PWMMCR\_MCR\_BREATHING](#a8e3d5f1c472ce31913e4053f3a7b1d70)   2 |
| #define | [IT8801\_PWMMCR\_MCR\_ON](#a5fda70da82cd203efa8be58d437eab8b)   3 |
| #define | [IT8801\_DT\_INST\_MFDCTRL](#aa9d6f1d7fc9b16a6137e1ccaed2ae497)(inst, idx) |
| #define | [IT8801\_DT\_INST\_MFDCTRL\_LEN](#aa16440b852beb0b839c23312d817fca1)(inst) |
| #define | [IT8801\_DEV\_MFD](#a8198cb9c55c8f068192dd715099d5d92)(idx, inst) |
| #define | [IT8801\_DEV\_MFD\_PIN](#aef92aa44c116c58f283f7185167085b6)(idx, inst) |
| #define | [IT8801\_DEV\_MFD\_FUNC](#a7628a888ab7ba6187a7aadfb9f4af256)(idx, inst) |
| #define | [IT8801\_DT\_MFD\_ITEMS\_FUNC](#afa5b636e82b01d8d9c631f1ccb6823ed)(idx, inst) |
| #define | [IT8801\_DT\_MFD\_ITEMS\_LIST](#a3a2f4c469264e7dc90dc78ae22bd5147)(inst) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [it8801\_callback\_handler\_t](#a50e301d4cfb9211625e851b0cc40f130)) (const struct [device](structdevice.md) \*dev) |

| Functions | |
| --- | --- |
| int | [mfd\_it8801\_configure\_pins](#a7273a553c04ac94c8adf244f1935b0ef) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*i2c\_dev, const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) func) |
| void | [mfd\_it8801\_register\_interrupt\_callback](#aeb61b0b4514fc757a016b8502ed58c09) (const struct [device](structdevice.md) \*mfd, struct [it8801\_mfd\_callback](structit8801__mfd__callback.md) \*callback) |

| Variables | |
| --- | --- |
| static const struct [it8801\_vendor\_id\_t](structit8801__vendor__id__t.md) | [it8801\_id\_verify](#a0e013175c1b2fd6ff3b62fb6eb3512ce) [] |

## Macro Definition Documentation

## [◆ ](#a8198cb9c55c8f068192dd715099d5d92)IT8801\_DEV\_MFD

| #define IT8801\_DEV\_MFD | ( |  | *idx*, |
| --- | --- | --- | --- |
|  |  |  | *inst* ) |

**Value:**

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_PHANDLE](group__devicetree-generic-prop.md#ga7bd77c49472ba4547d87f00f40fd7171)([IT8801\_DT\_INST\_MFDCTRL](#aa9d6f1d7fc9b16a6137e1ccaed2ae497)(inst, idx), altctrls))

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:280

[DT\_PHANDLE](group__devicetree-generic-prop.md#ga7bd77c49472ba4547d87f00f40fd7171)

#define DT\_PHANDLE(node\_id, prop)

Get a node identifier for a phandle property's value.

**Definition** devicetree.h:1799

[IT8801\_DT\_INST\_MFDCTRL](#aa9d6f1d7fc9b16a6137e1ccaed2ae497)

#define IT8801\_DT\_INST\_MFDCTRL(inst, idx)

**Definition** mfd\_ite\_it8801.h:94

## [◆ ](#a7628a888ab7ba6187a7aadfb9f4af256)IT8801\_DEV\_MFD\_FUNC

| #define IT8801\_DEV\_MFD\_FUNC | ( |  | *idx*, |
| --- | --- | --- | --- |
|  |  |  | *inst* ) |

**Value:**

[DT\_PHA](group__devicetree-generic-prop.md#gacef5921973a55433161fe0be3f8f628d)([IT8801\_DT\_INST\_MFDCTRL](#aa9d6f1d7fc9b16a6137e1ccaed2ae497)(inst, idx), altctrls, alt\_func)

[DT\_PHA](group__devicetree-generic-prop.md#gacef5921973a55433161fe0be3f8f628d)

#define DT\_PHA(node\_id, pha, cell)

Equivalent to DT\_PHA\_BY\_IDX(node\_id, pha, 0, cell).

**Definition** devicetree.h:1600

## [◆ ](#aef92aa44c116c58f283f7185167085b6)IT8801\_DEV\_MFD\_PIN

| #define IT8801\_DEV\_MFD\_PIN | ( |  | *idx*, |
| --- | --- | --- | --- |
|  |  |  | *inst* ) |

**Value:**

[DT\_PHA](group__devicetree-generic-prop.md#gacef5921973a55433161fe0be3f8f628d)([IT8801\_DT\_INST\_MFDCTRL](#aa9d6f1d7fc9b16a6137e1ccaed2ae497)(inst, idx), altctrls, pin)

## [◆ ](#aa9d6f1d7fc9b16a6137e1ccaed2ae497)IT8801\_DT\_INST\_MFDCTRL

| #define IT8801\_DT\_INST\_MFDCTRL | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

**Value:**

[DT\_INST\_PHANDLE\_BY\_IDX](group__devicetree-inst.md#ga10d93a1f9a9f5e225508c4c383654b1c)(inst, mfdctrl, idx)

[DT\_INST\_PHANDLE\_BY\_IDX](group__devicetree-inst.md#ga10d93a1f9a9f5e225508c4c383654b1c)

#define DT\_INST\_PHANDLE\_BY\_IDX(inst, prop, idx)

Get a DT\_DRV\_COMPAT instance's node identifier for a phandle in a property.

**Definition** devicetree.h:4426

## [◆ ](#aa16440b852beb0b839c23312d817fca1)IT8801\_DT\_INST\_MFDCTRL\_LEN

| #define IT8801\_DT\_INST\_MFDCTRL\_LEN | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_INST\_PROP\_LEN\_OR](group__devicetree-inst.md#ga9be8fdcc8c4032748b47f497efa19173)(inst, mfdctrl, 0)

[DT\_INST\_PROP\_LEN\_OR](group__devicetree-inst.md#ga9be8fdcc8c4032748b47f497efa19173)

#define DT\_INST\_PROP\_LEN\_OR(inst, prop, default\_value)

Like DT\_INST\_PROP\_LEN(), but with a fallback to default\_value.

**Definition** devicetree.h:4247

## [◆ ](#afa5b636e82b01d8d9c631f1ccb6823ed)IT8801\_DT\_MFD\_ITEMS\_FUNC

| #define IT8801\_DT\_MFD\_ITEMS\_FUNC | ( |  | *idx*, |
| --- | --- | --- | --- |
|  |  |  | *inst* ) |

**Value:**

{ \

.gpiocr = [IT8801\_DEV\_MFD](#a8198cb9c55c8f068192dd715099d5d92)(idx, inst), \

.pin = [IT8801\_DEV\_MFD\_PIN](#aef92aa44c116c58f283f7185167085b6)(idx, inst), \

.alt\_func = [IT8801\_DEV\_MFD\_FUNC](#a7628a888ab7ba6187a7aadfb9f4af256)(idx, inst), \

}

[IT8801\_DEV\_MFD\_FUNC](#a7628a888ab7ba6187a7aadfb9f4af256)

#define IT8801\_DEV\_MFD\_FUNC(idx, inst)

**Definition** mfd\_ite\_it8801.h:101

[IT8801\_DEV\_MFD](#a8198cb9c55c8f068192dd715099d5d92)

#define IT8801\_DEV\_MFD(idx, inst)

**Definition** mfd\_ite\_it8801.h:98

[IT8801\_DEV\_MFD\_PIN](#aef92aa44c116c58f283f7185167085b6)

#define IT8801\_DEV\_MFD\_PIN(idx, inst)

**Definition** mfd\_ite\_it8801.h:100

## [◆ ](#a3a2f4c469264e7dc90dc78ae22bd5147)IT8801\_DT\_MFD\_ITEMS\_LIST

| #define IT8801\_DT\_MFD\_ITEMS\_LIST | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{[LISTIFY](group__sys-util.md#ga81cbc0233cf73048d65b76f716653af6)([IT8801\_DT\_INST\_MFDCTRL\_LEN](#aa16440b852beb0b839c23312d817fca1)(inst), \

[IT8801\_DT\_MFD\_ITEMS\_FUNC](#afa5b636e82b01d8d9c631f1ccb6823ed), (,), \

inst) }

[LISTIFY](group__sys-util.md#ga81cbc0233cf73048d65b76f716653af6)

#define LISTIFY(LEN, F, sep,...)

Generates a sequence of code with configurable separator.

**Definition** util\_macro.h:478

[IT8801\_DT\_INST\_MFDCTRL\_LEN](#aa16440b852beb0b839c23312d817fca1)

#define IT8801\_DT\_INST\_MFDCTRL\_LEN(inst)

**Definition** mfd\_ite\_it8801.h:96

[IT8801\_DT\_MFD\_ITEMS\_FUNC](#afa5b636e82b01d8d9c631f1ccb6823ed)

#define IT8801\_DT\_MFD\_ITEMS\_FUNC(idx, inst)

**Definition** mfd\_ite\_it8801.h:103

## [◆ ](#aa93ce4f29ad9b4d9aeedfa3974c621b2)IT8801\_GPIOAFS\_FUN1

| #define IT8801\_GPIOAFS\_FUN1   0x0 |
| --- |

## [◆ ](#a412905632e67c8ff0a00d6a366ad5bf2)IT8801\_GPIOAFS\_FUN2

| #define IT8801\_GPIOAFS\_FUN2   0x01 |
| --- |

## [◆ ](#a7a49cf897e723f57f7ce6aa030f890d5)IT8801\_GPIOAFS\_FUN3

| #define IT8801\_GPIOAFS\_FUN3   0x02 |
| --- |

## [◆ ](#a203d08ead5b60a5d51a66d550328aef6)IT8801\_GPIODIR

| #define IT8801\_GPIODIR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#aca84886b619af7cd79d0b9cb27e16650)IT8801\_GPIOIOT\_INT\_FALL

| #define IT8801\_GPIOIOT\_INT\_FALL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#ad951ae2431f554ed5582ce74fa90c9f5)IT8801\_GPIOIOT\_INT\_RISE

| #define IT8801\_GPIOIOT\_INT\_RISE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#afb02201d261e416846e28af181ef75b6)IT8801\_GPIOIOT\_OD

| #define IT8801\_GPIOIOT\_OD   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a1a516610506e0cbc06fe2b90748b8f19)IT8801\_GPIOPDE

| #define IT8801\_GPIOPDE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a6a7ab8ecd064bf59f0b0d8ab3b5b2bf8)IT8801\_GPIOPOL

| #define IT8801\_GPIOPOL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a526c4b693f64f9592f59221019bbb1e1)IT8801\_GPIOPUE

| #define IT8801\_GPIOPUE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a6609e354ecb0b18e376cbc58092f537a)IT8801\_PWMMCR\_MCR\_BLINKING

| #define IT8801\_PWMMCR\_MCR\_BLINKING   1 |
| --- |

## [◆ ](#a8e3d5f1c472ce31913e4053f3a7b1d70)IT8801\_PWMMCR\_MCR\_BREATHING

| #define IT8801\_PWMMCR\_MCR\_BREATHING   2 |
| --- |

## [◆ ](#af943264d205ae66f691a934dc7598f79)IT8801\_PWMMCR\_MCR\_MASK

| #define IT8801\_PWMMCR\_MCR\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(1, 0) |
| --- |

## [◆ ](#adb356e532725450d445ff14258875f54)IT8801\_PWMMCR\_MCR\_OFF

| #define IT8801\_PWMMCR\_MCR\_OFF   0 |
| --- |

## [◆ ](#a5fda70da82cd203efa8be58d437eab8b)IT8801\_PWMMCR\_MCR\_ON

| #define IT8801\_PWMMCR\_MCR\_ON   3 |
| --- |

## [◆ ](#abb4de1bff69302bdff8e6420eaf0bdc1)IT8801\_REG\_GIECR

| #define IT8801\_REG\_GIECR   0xfb |
| --- |

## [◆ ](#af769928fba020583c1aacafc3ef3f661)IT8801\_REG\_GISR

| #define IT8801\_REG\_GISR   0xf9 |
| --- |

## [◆ ](#aff5dcc74423dba3bad5693ec5e7d34be)IT8801\_REG\_HBVIDR

| #define IT8801\_REG\_HBVIDR   0xff |
| --- |

## [◆ ](#a722c1dbea588a3559edac523462dd755)IT8801\_REG\_LBVIDR

| #define IT8801\_REG\_LBVIDR   0xfe |
| --- |

## [◆ ](#aa5ffc9da4d8e8ae737735d39d6c97e7a)IT8801\_REG\_MASK\_AKSOSC

| #define IT8801\_REG\_MASK\_AKSOSC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#aa974608857370407d8fcbdbda3c474bd)IT8801\_REG\_MASK\_ARE

| #define IT8801\_REG\_MASK\_ARE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#ace92908cb46e1436279fb02216cd5021)IT8801\_REG\_MASK\_GGPIOIE

| #define IT8801\_REG\_MASK\_GGPIOIE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a19097fcc347d262a8b970c447caeda8a)IT8801\_REG\_MASK\_GISR\_GKSIIS

| #define IT8801\_REG\_MASK\_GISR\_GKSIIS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#a13e7af4eccface18b7e8d8fc782896b7)IT8801\_REG\_MASK\_GKSIIE

| #define IT8801\_REG\_MASK\_GKSIIE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a7664d5e95b800c5eb1dc728f72e7c232)IT8801\_REG\_MASK\_KSE

| #define IT8801\_REG\_MASK\_KSE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#a3ae2764c10f499cc3b9721eeb947b5b9)IT8801\_REG\_MASK\_KSOSDIC

| #define IT8801\_REG\_MASK\_KSOSDIC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#ab6d8db36c938a43fd204fef6fc6bf28e)IT8801\_REG\_PWMODDSR

| #define IT8801\_REG\_PWMODDSR   0x5f |
| --- |

## [◆ ](#af823bba3625871e586765885dc88ddc1)IT8801\_REG\_SMBCR

| #define IT8801\_REG\_SMBCR   0xfa |
| --- |

## [◆ ](#a08d8cff79844be2e179d1742222e9e3c)PWM\_IT8801\_FREQ

| #define PWM\_IT8801\_FREQ   32895 |
| --- |

## [◆ ](#aab85a1fc0640f5eb243d098436d910fd)PWM\_IT8801\_PUSH\_PULL

| #define PWM\_IT8801\_PUSH\_PULL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

## Typedef Documentation

## [◆ ](#a50e301d4cfb9211625e851b0cc40f130)it8801\_callback\_handler\_t

| typedef void(\* it8801\_callback\_handler\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

## Function Documentation

## [◆ ](#a7273a553c04ac94c8adf244f1935b0ef)mfd\_it8801\_configure\_pins()

| int mfd\_it8801\_configure\_pins | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *i2c\_dev*, |
| --- | --- | --- | --- |
|  |  | const struct [device](structdevice.md) \* | *dev*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *func* ) |

## [◆ ](#aeb61b0b4514fc757a016b8502ed58c09)mfd\_it8801\_register\_interrupt\_callback()

| void mfd\_it8801\_register\_interrupt\_callback | ( | const struct [device](structdevice.md) \* | *mfd*, |
| --- | --- | --- | --- |
|  |  | struct [it8801\_mfd\_callback](structit8801__mfd__callback.md) \* | *callback* ) |

## Variable Documentation

## [◆ ](#a0e013175c1b2fd6ff3b62fb6eb3512ce)it8801\_id\_verify

| | const struct [it8801\_vendor\_id\_t](structit8801__vendor__id__t.md) it8801\_id\_verify[] | | --- | | static |
| --- | --- | --- |

**Initial value:**

= {

{0x12, 0xff },

{0x83, 0xfe },

}

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [mfd\_ite\_it8801.h](mfd__ite__it8801_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
