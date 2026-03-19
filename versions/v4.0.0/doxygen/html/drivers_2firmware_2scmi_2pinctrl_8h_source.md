---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2firmware_2scmi_2pinctrl_8h_source.html
original_path: doxygen/html/drivers_2firmware_2scmi_2pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl.h

[Go to the documentation of this file.](drivers_2firmware_2scmi_2pinctrl_8h.md)

1/\*

2 \* Copyright 2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_PINCTRL\_H\_

13#define \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_PINCTRL\_H\_

14

15#include <[zephyr/drivers/firmware/scmi/protocol.h](protocol_8h.md)>

16

[ 17](drivers_2firmware_2scmi_2pinctrl_8h.md#a5856f69a41daebeb67bc675549a94082)#define ARM\_SCMI\_PINCTRL\_MAX\_CONFIG\_SIZE (10 \* 2)

18

[ 19](drivers_2firmware_2scmi_2pinctrl_8h.md#ad3e2c57ca0d05f266c13ad5efda5f822)#define SCMI\_PINCTRL\_NO\_FUNCTION 0xFFFFFFFF

20

[ 21](drivers_2firmware_2scmi_2pinctrl_8h.md#a8a504f804ca89f1fc7c7c2f8298f5b9e)#define SCMI\_PINCTRL\_CONFIG\_ATTRIBUTES(fid\_valid, cfg\_num, selector) \

22 (SCMI\_FIELD\_MAKE(fid\_valid, BIT(1), 10) | \

23 SCMI\_FIELD\_MAKE(cfg\_num, GENMASK(7, 0), 2) | \

24 SCMI\_FIELD\_MAKE(selector, GENMASK(1, 0), 0))

25

[ 26](drivers_2firmware_2scmi_2pinctrl_8h.md#a563b6183eda65630c1883af094585095)#define SCMI\_PINCTRL\_SELECTOR\_PIN 0x0

[ 27](drivers_2firmware_2scmi_2pinctrl_8h.md#a2d4fff080b1f6c62d3afb6de24c925ae)#define SCMI\_PINCTRL\_SELECTOR\_GROUP 0x1

28

[ 29](drivers_2firmware_2scmi_2pinctrl_8h.md#add032f5989f91f734db10ca382cb6c11)#define SCMI\_PINCTRL\_ATTRIBUTES\_CONFIG\_NUM(attributes)\

30 (((attributes) & GENMASK(9, 2)) >> 2)

31

[ 35](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040)enum [scmi\_pinctrl\_message](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040) {

[ 36](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a74c556d431c1daa009db6d7f133adce0) [SCMI\_PINCTRL\_MSG\_PROTOCOL\_VERSION](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a74c556d431c1daa009db6d7f133adce0) = 0x0,

[ 37](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a5750d532aaaf18855ba611fa2197bef7) [SCMI\_PINCTRL\_MSG\_PROTOCOL\_ATTRIBUTES](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a5750d532aaaf18855ba611fa2197bef7) = 0x1,

[ 38](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a0f6442f1fdf46aec420297d1bd340f3b) [SCMI\_PINCTRL\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a0f6442f1fdf46aec420297d1bd340f3b) = 0x2,

[ 39](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a3c572f184df374efa4ac8f436eabc498) [SCMI\_PINCTRL\_MSG\_PINCTRL\_ATTRIBUTES](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a3c572f184df374efa4ac8f436eabc498) = 0x3,

[ 40](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a66b23f486ea16616599da97fa5e43b68) [SCMI\_PINCTRL\_MSG\_PINCTRL\_LIST\_ASSOCIATIONS](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a66b23f486ea16616599da97fa5e43b68) = 0x4,

[ 41](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a0effe64140e7a763f794cdee9347e59d) [SCMI\_PINCTRL\_MSG\_PINCTRL\_SETTINGS\_GET](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a0effe64140e7a763f794cdee9347e59d) = 0x5,

[ 42](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040af5075bd9399cc8c125866873df3aee50) [SCMI\_PINCTRL\_MSG\_PINCTRL\_SETTINGS\_CONFIGURE](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040af5075bd9399cc8c125866873df3aee50) = 0x6,

[ 43](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040af3750c500bb9c42ba94b6c9b4e4c01b8) [SCMI\_PINCTRL\_MSG\_PINCTRL\_REQUEST](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040af3750c500bb9c42ba94b6c9b4e4c01b8) = 0x7,

[ 44](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a1d9cc26a5f89eefea7ccdae7cde4f16b) [SCMI\_PINCTRL\_MSG\_PINCTRL\_RELEASE](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a1d9cc26a5f89eefea7ccdae7cde4f16b) = 0x8,

[ 45](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a5ce8e341575f24e17c1031ca3cb4e6b1) [SCMI\_PINCTRL\_MSG\_PINCTRL\_NAME\_GET](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a5ce8e341575f24e17c1031ca3cb4e6b1) = 0x9,

[ 46](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a169968862f7c722cbf47528750e40e67) [SCMI\_PINCTRL\_MSG\_PINCTRL\_SET\_PERMISSIONS](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a169968862f7c722cbf47528750e40e67) = 0xa,

[ 47](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040aba332b64c35581ad5799818004d282e8) [SCMI\_PINCTRL\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040aba332b64c35581ad5799818004d282e8) = 0x10,

48};

49

[ 53](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96b)enum [scmi\_pinctrl\_config](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96b) {

[ 54](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba3c62801c73f96b5854edd952ce6e729b) [SCMI\_PINCTRL\_DEFAULT](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba3c62801c73f96b5854edd952ce6e729b) = 0,

[ 55](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba4600bb6538330e7b0228e78c8b8c5e55) [SCMI\_PINCTRL\_BIAS\_BUS\_HOLD](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba4600bb6538330e7b0228e78c8b8c5e55) = 1,

[ 56](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba8f3390e1a61d025c3682d23ed13725e8) [SCMI\_PINCTRL\_BIAS\_DISABLE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba8f3390e1a61d025c3682d23ed13725e8) = 2,

[ 57](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba18ecf549efbf006475f3c0205bbea432) [SCMI\_PINCTRL\_BIAS\_HIGH\_Z](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba18ecf549efbf006475f3c0205bbea432) = 3,

[ 58](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba88232491b6ec4dfc73d5c945413c860e) [SCMI\_PINCTRL\_BIAS\_PULL\_UP](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba88232491b6ec4dfc73d5c945413c860e) = 4,

[ 59](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba02ef96841a54b7f55b784d4b5c8685d2) [SCMI\_PINCTRL\_BIAS\_PULL\_DEFAULT](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba02ef96841a54b7f55b784d4b5c8685d2) = 5,

[ 60](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96bae991c77daff7720e03c45b7738ec7692) [SCMI\_PINCTRL\_BIAS\_PULL\_DOWN](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96bae991c77daff7720e03c45b7738ec7692) = 6,

[ 61](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96baed811778f8586aeca201119a5b05fd1d) [SCMI\_PINCTRL\_DRIVE\_OPEN\_DRAIN](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96baed811778f8586aeca201119a5b05fd1d) = 7,

[ 62](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba9a3efde347233010b1a21f7c2c244e54) [SCMI\_PINCTRL\_DRIVE\_OPEN\_SOURCE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba9a3efde347233010b1a21f7c2c244e54) = 8,

[ 63](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96bafcdffbc64f9648ae15f8bfa1d4d97227) [SCMI\_PCINTRL\_DRIVE\_PUSH\_PULL](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96bafcdffbc64f9648ae15f8bfa1d4d97227) = 9,

[ 64](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96baf0dd0db5fb4cdab56e4d580e0da2a0a3) [SCMI\_PCINTRL\_DRIVE\_STRENGTH](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96baf0dd0db5fb4cdab56e4d580e0da2a0a3) = 10,

[ 65](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba709f0e20f862af2b2886825731125bf4) [SCMI\_PINCTRL\_INPUT\_DEBOUNCE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba709f0e20f862af2b2886825731125bf4) = 11,

[ 66](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba264ed5f09078fdd145effc6d0fe705d4) [SCMI\_PINCTRL\_INPUT\_MODE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba264ed5f09078fdd145effc6d0fe705d4) = 12,

[ 67](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96bac93aa772bcf931acdd3532774270db65) [SCMI\_PINCTRL\_PULL\_MODE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96bac93aa772bcf931acdd3532774270db65) = 13,

[ 68](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba2668c9faec52f0cf124af5af3e62cbd5) [SCMI\_PINCTRL\_INPUT\_VALUE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba2668c9faec52f0cf124af5af3e62cbd5) = 14,

[ 69](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96baac8d42ee60b4251cb506b9c724d458be) [SCMI\_PINCTRL\_INPUT\_SCHMITT](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96baac8d42ee60b4251cb506b9c724d458be) = 15,

[ 70](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba84ceb297de86593719a88cfd3aaa4691) [SCMI\_PINCTRL\_LP\_MODE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba84ceb297de86593719a88cfd3aaa4691) = 16,

[ 71](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba4c93a8dcc239793359a5d49087b6d378) [SCMI\_PINCTRL\_OUTPUT\_MODE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba4c93a8dcc239793359a5d49087b6d378) = 17,

[ 72](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96babb038fbaa33b735fc8bb749f0cc59359) [SCMI\_PINCTRL\_OUTPUT\_VALUE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96babb038fbaa33b735fc8bb749f0cc59359) = 18,

[ 73](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba464371220816dbe642caf696e3b9b905) [SCMI\_PINCTRL\_POWER\_SOURCE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba464371220816dbe642caf696e3b9b905) = 19,

[ 74](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96baefcb24ff6ca583f7925db6b962951629) [SCMI\_PINCTRL\_SLEW\_RATE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96baefcb24ff6ca583f7925db6b962951629) = 20,

[ 75](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba051880c89ea312541c87324c4d641727) [SCMI\_PINCTRL\_RESERVED\_START](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba051880c89ea312541c87324c4d641727) = 21,

[ 76](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba3c5302df7906c502eb31e0956a982171) [SCMI\_PINCTRL\_RESERVED\_END](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba3c5302df7906c502eb31e0956a982171) = 191,

[ 77](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba0a19f087055a6d331b3a20a83e39c696) [SCMI\_PINCTRL\_VENDOR\_START](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba0a19f087055a6d331b3a20a83e39c696) = 192,

78};

79

[ 86](structscmi__pinctrl__settings.md)struct [scmi\_pinctrl\_settings](structscmi__pinctrl__settings.md) {

[ 87](structscmi__pinctrl__settings.md#a36c8e49a42cb89d4117b9e90fe1a044e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structscmi__pinctrl__settings.md#a36c8e49a42cb89d4117b9e90fe1a044e);

[ 88](structscmi__pinctrl__settings.md#ade79b6c3efc5b069f74ad6e12088d6c2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [function](structscmi__pinctrl__settings.md#ade79b6c3efc5b069f74ad6e12088d6c2);

[ 89](structscmi__pinctrl__settings.md#a7c206eaf1a88e0d1e54d0d19c79e25c6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [attributes](structscmi__pinctrl__settings.md#a7c206eaf1a88e0d1e54d0d19c79e25c6);

[ 90](structscmi__pinctrl__settings.md#a5e92a3755d6dc8ccfecf696ca5eb8bd1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [config](structscmi__pinctrl__settings.md#a5e92a3755d6dc8ccfecf696ca5eb8bd1)[[ARM\_SCMI\_PINCTRL\_MAX\_CONFIG\_SIZE](drivers_2firmware_2scmi_2pinctrl_8h.md#a5856f69a41daebeb67bc675549a94082)];

91};

92

[ 101](drivers_2firmware_2scmi_2pinctrl_8h.md#ad7d9ca78b75cc32edefc1ea8e0e0c09e)int [scmi\_pinctrl\_settings\_configure](drivers_2firmware_2scmi_2pinctrl_8h.md#ad7d9ca78b75cc32edefc1ea8e0e0c09e)(struct [scmi\_pinctrl\_settings](structscmi__pinctrl__settings.md) \*settings);

102

103#endif /\* \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_PINCTRL\_H\_ \*/

[scmi\_pinctrl\_message](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040)

scmi\_pinctrl\_message

Pinctrl protocol command message IDs.

**Definition** pinctrl.h:35

[SCMI\_PINCTRL\_MSG\_PINCTRL\_SETTINGS\_GET](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a0effe64140e7a763f794cdee9347e59d)

@ SCMI\_PINCTRL\_MSG\_PINCTRL\_SETTINGS\_GET

**Definition** pinctrl.h:41

[SCMI\_PINCTRL\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a0f6442f1fdf46aec420297d1bd340f3b)

@ SCMI\_PINCTRL\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES

**Definition** pinctrl.h:38

[SCMI\_PINCTRL\_MSG\_PINCTRL\_SET\_PERMISSIONS](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a169968862f7c722cbf47528750e40e67)

@ SCMI\_PINCTRL\_MSG\_PINCTRL\_SET\_PERMISSIONS

**Definition** pinctrl.h:46

[SCMI\_PINCTRL\_MSG\_PINCTRL\_RELEASE](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a1d9cc26a5f89eefea7ccdae7cde4f16b)

@ SCMI\_PINCTRL\_MSG\_PINCTRL\_RELEASE

**Definition** pinctrl.h:44

[SCMI\_PINCTRL\_MSG\_PINCTRL\_ATTRIBUTES](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a3c572f184df374efa4ac8f436eabc498)

@ SCMI\_PINCTRL\_MSG\_PINCTRL\_ATTRIBUTES

**Definition** pinctrl.h:39

[SCMI\_PINCTRL\_MSG\_PROTOCOL\_ATTRIBUTES](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a5750d532aaaf18855ba611fa2197bef7)

@ SCMI\_PINCTRL\_MSG\_PROTOCOL\_ATTRIBUTES

**Definition** pinctrl.h:37

[SCMI\_PINCTRL\_MSG\_PINCTRL\_NAME\_GET](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a5ce8e341575f24e17c1031ca3cb4e6b1)

@ SCMI\_PINCTRL\_MSG\_PINCTRL\_NAME\_GET

**Definition** pinctrl.h:45

[SCMI\_PINCTRL\_MSG\_PINCTRL\_LIST\_ASSOCIATIONS](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a66b23f486ea16616599da97fa5e43b68)

@ SCMI\_PINCTRL\_MSG\_PINCTRL\_LIST\_ASSOCIATIONS

**Definition** pinctrl.h:40

[SCMI\_PINCTRL\_MSG\_PROTOCOL\_VERSION](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040a74c556d431c1daa009db6d7f133adce0)

@ SCMI\_PINCTRL\_MSG\_PROTOCOL\_VERSION

**Definition** pinctrl.h:36

[SCMI\_PINCTRL\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040aba332b64c35581ad5799818004d282e8)

@ SCMI\_PINCTRL\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION

**Definition** pinctrl.h:47

[SCMI\_PINCTRL\_MSG\_PINCTRL\_REQUEST](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040af3750c500bb9c42ba94b6c9b4e4c01b8)

@ SCMI\_PINCTRL\_MSG\_PINCTRL\_REQUEST

**Definition** pinctrl.h:43

[SCMI\_PINCTRL\_MSG\_PINCTRL\_SETTINGS\_CONFIGURE](drivers_2firmware_2scmi_2pinctrl_8h.md#a370af36974b0819b68749a3c30f6e040af5075bd9399cc8c125866873df3aee50)

@ SCMI\_PINCTRL\_MSG\_PINCTRL\_SETTINGS\_CONFIGURE

**Definition** pinctrl.h:42

[ARM\_SCMI\_PINCTRL\_MAX\_CONFIG\_SIZE](drivers_2firmware_2scmi_2pinctrl_8h.md#a5856f69a41daebeb67bc675549a94082)

#define ARM\_SCMI\_PINCTRL\_MAX\_CONFIG\_SIZE

**Definition** pinctrl.h:17

[scmi\_pinctrl\_config](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96b)

scmi\_pinctrl\_config

Pinctrl configurations.

**Definition** pinctrl.h:53

[SCMI\_PINCTRL\_BIAS\_PULL\_DEFAULT](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba02ef96841a54b7f55b784d4b5c8685d2)

@ SCMI\_PINCTRL\_BIAS\_PULL\_DEFAULT

**Definition** pinctrl.h:59

[SCMI\_PINCTRL\_RESERVED\_START](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba051880c89ea312541c87324c4d641727)

@ SCMI\_PINCTRL\_RESERVED\_START

**Definition** pinctrl.h:75

[SCMI\_PINCTRL\_VENDOR\_START](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba0a19f087055a6d331b3a20a83e39c696)

@ SCMI\_PINCTRL\_VENDOR\_START

**Definition** pinctrl.h:77

[SCMI\_PINCTRL\_BIAS\_HIGH\_Z](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba18ecf549efbf006475f3c0205bbea432)

@ SCMI\_PINCTRL\_BIAS\_HIGH\_Z

**Definition** pinctrl.h:57

[SCMI\_PINCTRL\_INPUT\_MODE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba264ed5f09078fdd145effc6d0fe705d4)

@ SCMI\_PINCTRL\_INPUT\_MODE

**Definition** pinctrl.h:66

[SCMI\_PINCTRL\_INPUT\_VALUE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba2668c9faec52f0cf124af5af3e62cbd5)

@ SCMI\_PINCTRL\_INPUT\_VALUE

**Definition** pinctrl.h:68

[SCMI\_PINCTRL\_RESERVED\_END](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba3c5302df7906c502eb31e0956a982171)

@ SCMI\_PINCTRL\_RESERVED\_END

**Definition** pinctrl.h:76

[SCMI\_PINCTRL\_DEFAULT](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba3c62801c73f96b5854edd952ce6e729b)

@ SCMI\_PINCTRL\_DEFAULT

**Definition** pinctrl.h:54

[SCMI\_PINCTRL\_BIAS\_BUS\_HOLD](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba4600bb6538330e7b0228e78c8b8c5e55)

@ SCMI\_PINCTRL\_BIAS\_BUS\_HOLD

**Definition** pinctrl.h:55

[SCMI\_PINCTRL\_POWER\_SOURCE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba464371220816dbe642caf696e3b9b905)

@ SCMI\_PINCTRL\_POWER\_SOURCE

**Definition** pinctrl.h:73

[SCMI\_PINCTRL\_OUTPUT\_MODE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba4c93a8dcc239793359a5d49087b6d378)

@ SCMI\_PINCTRL\_OUTPUT\_MODE

**Definition** pinctrl.h:71

[SCMI\_PINCTRL\_INPUT\_DEBOUNCE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba709f0e20f862af2b2886825731125bf4)

@ SCMI\_PINCTRL\_INPUT\_DEBOUNCE

**Definition** pinctrl.h:65

[SCMI\_PINCTRL\_LP\_MODE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba84ceb297de86593719a88cfd3aaa4691)

@ SCMI\_PINCTRL\_LP\_MODE

**Definition** pinctrl.h:70

[SCMI\_PINCTRL\_BIAS\_PULL\_UP](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba88232491b6ec4dfc73d5c945413c860e)

@ SCMI\_PINCTRL\_BIAS\_PULL\_UP

**Definition** pinctrl.h:58

[SCMI\_PINCTRL\_BIAS\_DISABLE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba8f3390e1a61d025c3682d23ed13725e8)

@ SCMI\_PINCTRL\_BIAS\_DISABLE

**Definition** pinctrl.h:56

[SCMI\_PINCTRL\_DRIVE\_OPEN\_SOURCE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96ba9a3efde347233010b1a21f7c2c244e54)

@ SCMI\_PINCTRL\_DRIVE\_OPEN\_SOURCE

**Definition** pinctrl.h:62

[SCMI\_PINCTRL\_INPUT\_SCHMITT](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96baac8d42ee60b4251cb506b9c724d458be)

@ SCMI\_PINCTRL\_INPUT\_SCHMITT

**Definition** pinctrl.h:69

[SCMI\_PINCTRL\_OUTPUT\_VALUE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96babb038fbaa33b735fc8bb749f0cc59359)

@ SCMI\_PINCTRL\_OUTPUT\_VALUE

**Definition** pinctrl.h:72

[SCMI\_PINCTRL\_PULL\_MODE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96bac93aa772bcf931acdd3532774270db65)

@ SCMI\_PINCTRL\_PULL\_MODE

**Definition** pinctrl.h:67

[SCMI\_PINCTRL\_BIAS\_PULL\_DOWN](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96bae991c77daff7720e03c45b7738ec7692)

@ SCMI\_PINCTRL\_BIAS\_PULL\_DOWN

**Definition** pinctrl.h:60

[SCMI\_PINCTRL\_DRIVE\_OPEN\_DRAIN](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96baed811778f8586aeca201119a5b05fd1d)

@ SCMI\_PINCTRL\_DRIVE\_OPEN\_DRAIN

**Definition** pinctrl.h:61

[SCMI\_PINCTRL\_SLEW\_RATE](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96baefcb24ff6ca583f7925db6b962951629)

@ SCMI\_PINCTRL\_SLEW\_RATE

**Definition** pinctrl.h:74

[SCMI\_PCINTRL\_DRIVE\_STRENGTH](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96baf0dd0db5fb4cdab56e4d580e0da2a0a3)

@ SCMI\_PCINTRL\_DRIVE\_STRENGTH

**Definition** pinctrl.h:64

[SCMI\_PCINTRL\_DRIVE\_PUSH\_PULL](drivers_2firmware_2scmi_2pinctrl_8h.md#ab5208b8108578e82acfa5dd0c8a2a96bafcdffbc64f9648ae15f8bfa1d4d97227)

@ SCMI\_PCINTRL\_DRIVE\_PUSH\_PULL

**Definition** pinctrl.h:63

[scmi\_pinctrl\_settings\_configure](drivers_2firmware_2scmi_2pinctrl_8h.md#ad7d9ca78b75cc32edefc1ea8e0e0c09e)

int scmi\_pinctrl\_settings\_configure(struct scmi\_pinctrl\_settings \*settings)

Send the PINCTRL\_SETTINGS\_CONFIGURE command and get its reply.

[protocol.h](protocol_8h.md)

SCMI protocol generic functions and structures.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[scmi\_pinctrl\_settings](structscmi__pinctrl__settings.md)

Describes the parameters for the PINCTRL\_SETTINGS\_CONFIGURE command.

**Definition** pinctrl.h:86

[scmi\_pinctrl\_settings::id](structscmi__pinctrl__settings.md#a36c8e49a42cb89d4117b9e90fe1a044e)

uint32\_t id

**Definition** pinctrl.h:87

[scmi\_pinctrl\_settings::config](structscmi__pinctrl__settings.md#a5e92a3755d6dc8ccfecf696ca5eb8bd1)

uint32\_t config[(10 \*2)]

**Definition** pinctrl.h:90

[scmi\_pinctrl\_settings::attributes](structscmi__pinctrl__settings.md#a7c206eaf1a88e0d1e54d0d19c79e25c6)

uint32\_t attributes

**Definition** pinctrl.h:89

[scmi\_pinctrl\_settings::function](structscmi__pinctrl__settings.md#ade79b6c3efc5b069f74ad6e12088d6c2)

uint32\_t function

**Definition** pinctrl.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [firmware](dir_e97f19a49725d52aae6eece65b856a75.md)
- [scmi](dir_b6bd1dece7d1578165357955ca5f0079.md)
- [pinctrl.h](drivers_2firmware_2scmi_2pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
