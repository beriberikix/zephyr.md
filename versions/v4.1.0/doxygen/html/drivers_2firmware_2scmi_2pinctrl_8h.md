---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2firmware_2scmi_2pinctrl_8h.html
original_path: doxygen/html/drivers_2firmware_2scmi_2pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl.h File Reference

SCMI pinctrl protocol helpers.
[More...](#details)

`#include <[zephyr/drivers/firmware/scmi/protocol.h](protocol_8h_source.md)>`

[Go to the source code of this file.](drivers_2firmware_2scmi_2pinctrl_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [scmi\_pinctrl\_settings](structscmi__pinctrl__settings.md) |
|  | Describes the parameters for the PINCTRL\_SETTINGS\_CONFIGURE command. [More...](structscmi__pinctrl__settings.md#details) |

| Macros | |
| --- | --- |
| #define | [ARM\_SCMI\_PINCTRL\_MAX\_CONFIG\_SIZE](#a5856f69a41daebeb67bc675549a94082)   (10 \* 2) |
| #define | [SCMI\_PINCTRL\_NO\_FUNCTION](#ad3e2c57ca0d05f266c13ad5efda5f822)   0xFFFFFFFF |
| #define | [SCMI\_PINCTRL\_CONFIG\_ATTRIBUTES](#a8a504f804ca89f1fc7c7c2f8298f5b9e)(fid\_valid, cfg\_num, selector) |
| #define | [SCMI\_PINCTRL\_SELECTOR\_PIN](#a563b6183eda65630c1883af094585095)   0x0 |
| #define | [SCMI\_PINCTRL\_SELECTOR\_GROUP](#a2d4fff080b1f6c62d3afb6de24c925ae)   0x1 |
| #define | [SCMI\_PINCTRL\_ATTRIBUTES\_CONFIG\_NUM](#add032f5989f91f734db10ca382cb6c11)(attributes) |

| Enumerations | |
| --- | --- |
| enum | [scmi\_pinctrl\_message](#a370af36974b0819b68749a3c30f6e040) {     [SCMI\_PINCTRL\_MSG\_PROTOCOL\_VERSION](#a370af36974b0819b68749a3c30f6e040a74c556d431c1daa009db6d7f133adce0) = 0x0 , [SCMI\_PINCTRL\_MSG\_PROTOCOL\_ATTRIBUTES](#a370af36974b0819b68749a3c30f6e040a5750d532aaaf18855ba611fa2197bef7) = 0x1 , [SCMI\_PINCTRL\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES](#a370af36974b0819b68749a3c30f6e040a0f6442f1fdf46aec420297d1bd340f3b) = 0x2 , [SCMI\_PINCTRL\_MSG\_PINCTRL\_ATTRIBUTES](#a370af36974b0819b68749a3c30f6e040a3c572f184df374efa4ac8f436eabc498) = 0x3 ,     [SCMI\_PINCTRL\_MSG\_PINCTRL\_LIST\_ASSOCIATIONS](#a370af36974b0819b68749a3c30f6e040a66b23f486ea16616599da97fa5e43b68) = 0x4 , [SCMI\_PINCTRL\_MSG\_PINCTRL\_SETTINGS\_GET](#a370af36974b0819b68749a3c30f6e040a0effe64140e7a763f794cdee9347e59d) = 0x5 , [SCMI\_PINCTRL\_MSG\_PINCTRL\_SETTINGS\_CONFIGURE](#a370af36974b0819b68749a3c30f6e040af5075bd9399cc8c125866873df3aee50) = 0x6 , [SCMI\_PINCTRL\_MSG\_PINCTRL\_REQUEST](#a370af36974b0819b68749a3c30f6e040af3750c500bb9c42ba94b6c9b4e4c01b8) = 0x7 ,     [SCMI\_PINCTRL\_MSG\_PINCTRL\_RELEASE](#a370af36974b0819b68749a3c30f6e040a1d9cc26a5f89eefea7ccdae7cde4f16b) = 0x8 , [SCMI\_PINCTRL\_MSG\_PINCTRL\_NAME\_GET](#a370af36974b0819b68749a3c30f6e040a5ce8e341575f24e17c1031ca3cb4e6b1) = 0x9 , [SCMI\_PINCTRL\_MSG\_PINCTRL\_SET\_PERMISSIONS](#a370af36974b0819b68749a3c30f6e040a169968862f7c722cbf47528750e40e67) = 0xa , [SCMI\_PINCTRL\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION](#a370af36974b0819b68749a3c30f6e040aba332b64c35581ad5799818004d282e8) = 0x10   } |
|  | Pinctrl protocol command message IDs. [More...](#a370af36974b0819b68749a3c30f6e040) |
| enum | [scmi\_pinctrl\_config](#ab5208b8108578e82acfa5dd0c8a2a96b) {     [SCMI\_PINCTRL\_DEFAULT](#ab5208b8108578e82acfa5dd0c8a2a96ba3c62801c73f96b5854edd952ce6e729b) = 0 , [SCMI\_PINCTRL\_BIAS\_BUS\_HOLD](#ab5208b8108578e82acfa5dd0c8a2a96ba4600bb6538330e7b0228e78c8b8c5e55) = 1 , [SCMI\_PINCTRL\_BIAS\_DISABLE](#ab5208b8108578e82acfa5dd0c8a2a96ba8f3390e1a61d025c3682d23ed13725e8) = 2 , [SCMI\_PINCTRL\_BIAS\_HIGH\_Z](#ab5208b8108578e82acfa5dd0c8a2a96ba18ecf549efbf006475f3c0205bbea432) = 3 ,     [SCMI\_PINCTRL\_BIAS\_PULL\_UP](#ab5208b8108578e82acfa5dd0c8a2a96ba88232491b6ec4dfc73d5c945413c860e) = 4 , [SCMI\_PINCTRL\_BIAS\_PULL\_DEFAULT](#ab5208b8108578e82acfa5dd0c8a2a96ba02ef96841a54b7f55b784d4b5c8685d2) = 5 , [SCMI\_PINCTRL\_BIAS\_PULL\_DOWN](#ab5208b8108578e82acfa5dd0c8a2a96bae991c77daff7720e03c45b7738ec7692) = 6 , [SCMI\_PINCTRL\_DRIVE\_OPEN\_DRAIN](#ab5208b8108578e82acfa5dd0c8a2a96baed811778f8586aeca201119a5b05fd1d) = 7 ,     [SCMI\_PINCTRL\_DRIVE\_OPEN\_SOURCE](#ab5208b8108578e82acfa5dd0c8a2a96ba9a3efde347233010b1a21f7c2c244e54) = 8 , [SCMI\_PCINTRL\_DRIVE\_PUSH\_PULL](#ab5208b8108578e82acfa5dd0c8a2a96bafcdffbc64f9648ae15f8bfa1d4d97227) = 9 , [SCMI\_PCINTRL\_DRIVE\_STRENGTH](#ab5208b8108578e82acfa5dd0c8a2a96baf0dd0db5fb4cdab56e4d580e0da2a0a3) = 10 , [SCMI\_PINCTRL\_INPUT\_DEBOUNCE](#ab5208b8108578e82acfa5dd0c8a2a96ba709f0e20f862af2b2886825731125bf4) = 11 ,     [SCMI\_PINCTRL\_INPUT\_MODE](#ab5208b8108578e82acfa5dd0c8a2a96ba264ed5f09078fdd145effc6d0fe705d4) = 12 , [SCMI\_PINCTRL\_PULL\_MODE](#ab5208b8108578e82acfa5dd0c8a2a96bac93aa772bcf931acdd3532774270db65) = 13 , [SCMI\_PINCTRL\_INPUT\_VALUE](#ab5208b8108578e82acfa5dd0c8a2a96ba2668c9faec52f0cf124af5af3e62cbd5) = 14 , [SCMI\_PINCTRL\_INPUT\_SCHMITT](#ab5208b8108578e82acfa5dd0c8a2a96baac8d42ee60b4251cb506b9c724d458be) = 15 ,     [SCMI\_PINCTRL\_LP\_MODE](#ab5208b8108578e82acfa5dd0c8a2a96ba84ceb297de86593719a88cfd3aaa4691) = 16 , [SCMI\_PINCTRL\_OUTPUT\_MODE](#ab5208b8108578e82acfa5dd0c8a2a96ba4c93a8dcc239793359a5d49087b6d378) = 17 , [SCMI\_PINCTRL\_OUTPUT\_VALUE](#ab5208b8108578e82acfa5dd0c8a2a96babb038fbaa33b735fc8bb749f0cc59359) = 18 , [SCMI\_PINCTRL\_POWER\_SOURCE](#ab5208b8108578e82acfa5dd0c8a2a96ba464371220816dbe642caf696e3b9b905) = 19 ,     [SCMI\_PINCTRL\_SLEW\_RATE](#ab5208b8108578e82acfa5dd0c8a2a96baefcb24ff6ca583f7925db6b962951629) = 20 , [SCMI\_PINCTRL\_RESERVED\_START](#ab5208b8108578e82acfa5dd0c8a2a96ba051880c89ea312541c87324c4d641727) = 21 , [SCMI\_PINCTRL\_RESERVED\_END](#ab5208b8108578e82acfa5dd0c8a2a96ba3c5302df7906c502eb31e0956a982171) = 191 , [SCMI\_PINCTRL\_VENDOR\_START](#ab5208b8108578e82acfa5dd0c8a2a96ba0a19f087055a6d331b3a20a83e39c696) = 192   } |
|  | Pinctrl configurations. [More...](#ab5208b8108578e82acfa5dd0c8a2a96b) |

| Functions | |
| --- | --- |
| int | [scmi\_pinctrl\_settings\_configure](#ad7d9ca78b75cc32edefc1ea8e0e0c09e) (struct [scmi\_pinctrl\_settings](structscmi__pinctrl__settings.md) \*settings) |
|  | Send the PINCTRL\_SETTINGS\_CONFIGURE command and get its reply. |

## Detailed Description

SCMI pinctrl protocol helpers.

## Macro Definition Documentation

## [◆ ](#a5856f69a41daebeb67bc675549a94082)ARM\_SCMI\_PINCTRL\_MAX\_CONFIG\_SIZE

| #define ARM\_SCMI\_PINCTRL\_MAX\_CONFIG\_SIZE   (10 \* 2) |
| --- |

## [◆ ](#add032f5989f91f734db10ca382cb6c11)SCMI\_PINCTRL\_ATTRIBUTES\_CONFIG\_NUM

| #define SCMI\_PINCTRL\_ATTRIBUTES\_CONFIG\_NUM | ( |  | *attributes* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((attributes) & [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(9, 2)) >> 2)

[GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)

#define GENMASK(h, l)

Create a contiguous bitmask starting at bit position l and ending at position h.

**Definition** util.h:79

## [◆ ](#a8a504f804ca89f1fc7c7c2f8298f5b9e)SCMI\_PINCTRL\_CONFIG\_ATTRIBUTES

| #define SCMI\_PINCTRL\_CONFIG\_ATTRIBUTES | ( |  | *fid\_valid*, |
| --- | --- | --- | --- |
|  |  |  | *cfg\_num*, |
|  |  |  | *selector* ) |

**Value:**

([SCMI\_FIELD\_MAKE](drivers_2firmware_2scmi_2util_8h.md#a21b369f9fa6d1a965ece4a589df88581)(fid\_valid, [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1), 10) | \

SCMI\_FIELD\_MAKE(cfg\_num, [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 0), 2) | \

SCMI\_FIELD\_MAKE(selector, [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(1, 0), 0))

[SCMI\_FIELD\_MAKE](drivers_2firmware_2scmi_2util_8h.md#a21b369f9fa6d1a965ece4a589df88581)

#define SCMI\_FIELD\_MAKE(x, mask, shift)

Create an SCMI message field.

**Definition** util.h:264

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

## [◆ ](#ad3e2c57ca0d05f266c13ad5efda5f822)SCMI\_PINCTRL\_NO\_FUNCTION

| #define SCMI\_PINCTRL\_NO\_FUNCTION   0xFFFFFFFF |
| --- |

## [◆ ](#a2d4fff080b1f6c62d3afb6de24c925ae)SCMI\_PINCTRL\_SELECTOR\_GROUP

| #define SCMI\_PINCTRL\_SELECTOR\_GROUP   0x1 |
| --- |

## [◆ ](#a563b6183eda65630c1883af094585095)SCMI\_PINCTRL\_SELECTOR\_PIN

| #define SCMI\_PINCTRL\_SELECTOR\_PIN   0x0 |
| --- |

## Enumeration Type Documentation

## [◆ ](#ab5208b8108578e82acfa5dd0c8a2a96b)scmi\_pinctrl\_config

| enum [scmi\_pinctrl\_config](#ab5208b8108578e82acfa5dd0c8a2a96b) |
| --- |

Pinctrl configurations.

| Enumerator | |
| --- | --- |
| SCMI\_PINCTRL\_DEFAULT |  |
| SCMI\_PINCTRL\_BIAS\_BUS\_HOLD |  |
| SCMI\_PINCTRL\_BIAS\_DISABLE |  |
| SCMI\_PINCTRL\_BIAS\_HIGH\_Z |  |
| SCMI\_PINCTRL\_BIAS\_PULL\_UP |  |
| SCMI\_PINCTRL\_BIAS\_PULL\_DEFAULT |  |
| SCMI\_PINCTRL\_BIAS\_PULL\_DOWN |  |
| SCMI\_PINCTRL\_DRIVE\_OPEN\_DRAIN |  |
| SCMI\_PINCTRL\_DRIVE\_OPEN\_SOURCE |  |
| SCMI\_PCINTRL\_DRIVE\_PUSH\_PULL |  |
| SCMI\_PCINTRL\_DRIVE\_STRENGTH |  |
| SCMI\_PINCTRL\_INPUT\_DEBOUNCE |  |
| SCMI\_PINCTRL\_INPUT\_MODE |  |
| SCMI\_PINCTRL\_PULL\_MODE |  |
| SCMI\_PINCTRL\_INPUT\_VALUE |  |
| SCMI\_PINCTRL\_INPUT\_SCHMITT |  |
| SCMI\_PINCTRL\_LP\_MODE |  |
| SCMI\_PINCTRL\_OUTPUT\_MODE |  |
| SCMI\_PINCTRL\_OUTPUT\_VALUE |  |
| SCMI\_PINCTRL\_POWER\_SOURCE |  |
| SCMI\_PINCTRL\_SLEW\_RATE |  |
| SCMI\_PINCTRL\_RESERVED\_START |  |
| SCMI\_PINCTRL\_RESERVED\_END |  |
| SCMI\_PINCTRL\_VENDOR\_START |  |

## [◆ ](#a370af36974b0819b68749a3c30f6e040)scmi\_pinctrl\_message

| enum [scmi\_pinctrl\_message](#a370af36974b0819b68749a3c30f6e040) |
| --- |

Pinctrl protocol command message IDs.

| Enumerator | |
| --- | --- |
| SCMI\_PINCTRL\_MSG\_PROTOCOL\_VERSION |  |
| SCMI\_PINCTRL\_MSG\_PROTOCOL\_ATTRIBUTES |  |
| SCMI\_PINCTRL\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES |  |
| SCMI\_PINCTRL\_MSG\_PINCTRL\_ATTRIBUTES |  |
| SCMI\_PINCTRL\_MSG\_PINCTRL\_LIST\_ASSOCIATIONS |  |
| SCMI\_PINCTRL\_MSG\_PINCTRL\_SETTINGS\_GET |  |
| SCMI\_PINCTRL\_MSG\_PINCTRL\_SETTINGS\_CONFIGURE |  |
| SCMI\_PINCTRL\_MSG\_PINCTRL\_REQUEST |  |
| SCMI\_PINCTRL\_MSG\_PINCTRL\_RELEASE |  |
| SCMI\_PINCTRL\_MSG\_PINCTRL\_NAME\_GET |  |
| SCMI\_PINCTRL\_MSG\_PINCTRL\_SET\_PERMISSIONS |  |
| SCMI\_PINCTRL\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION |  |

## Function Documentation

## [◆ ](#ad7d9ca78b75cc32edefc1ea8e0e0c09e)scmi\_pinctrl\_settings\_configure()

| int scmi\_pinctrl\_settings\_configure | ( | struct [scmi\_pinctrl\_settings](structscmi__pinctrl__settings.md) \* | *settings* | ) |  |
| --- | --- | --- | --- | --- | --- |

Send the PINCTRL\_SETTINGS\_CONFIGURE command and get its reply.

Parameters
:   | [Settings](group__settings.md) | pointer to settings to be applied |
    | --- | --- |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | errno if failure |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [firmware](dir_e97f19a49725d52aae6eece65b856a75.md)
- [scmi](dir_b6bd1dece7d1578165357955ca5f0079.md)
- [pinctrl.h](drivers_2firmware_2scmi_2pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
