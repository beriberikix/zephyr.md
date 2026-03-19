---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/msos__desc_8h_source.html
original_path: doxygen/html/msos__desc_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

msos\_desc.h

[Go to the documentation of this file.](msos__desc_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_INCLUDE\_USB\_MSOS\_DESC\_H

14#define ZEPHYR\_INCLUDE\_USB\_MSOS\_DESC\_H

15

16#include <[stdint.h](stdint_8h.md)>

17

[ 18](msos__desc_8h.md#ab443ad91634b7a8fb19fc2aa7108e631)enum [msosv2\_descriptor\_index](msos__desc_8h.md#ab443ad91634b7a8fb19fc2aa7108e631) {

[ 19](msos__desc_8h.md#ab443ad91634b7a8fb19fc2aa7108e631abe0e6e00164db250e4ad900f418a57d5) [MS\_OS\_20\_DESCRIPTOR\_INDEX](msos__desc_8h.md#ab443ad91634b7a8fb19fc2aa7108e631abe0e6e00164db250e4ad900f418a57d5) = 0x07,

[ 20](msos__desc_8h.md#ab443ad91634b7a8fb19fc2aa7108e631a2ae9d4948f03b7d9623c547daa0a9116) [MS\_OS\_20\_SET\_ALT\_ENUMERATION](msos__desc_8h.md#ab443ad91634b7a8fb19fc2aa7108e631a2ae9d4948f03b7d9623c547daa0a9116) = 0x08,

21};

22

[ 23](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5)enum [msosv2\_descriptor\_type](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5) {

[ 24](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5ac74a28d4e873b255d5b027af5ffffb5d) [MS\_OS\_20\_SET\_HEADER\_DESCRIPTOR](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5ac74a28d4e873b255d5b027af5ffffb5d) = 0x00,

[ 25](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5afe117782c0101a880e152a8a1110ecbc) [MS\_OS\_20\_SUBSET\_HEADER\_CONFIGURATION](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5afe117782c0101a880e152a8a1110ecbc) = 0x01,

[ 26](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5a1200730075635cba8dea3420be41d1a7) [MS\_OS\_20\_SUBSET\_HEADER\_FUNCTION](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5a1200730075635cba8dea3420be41d1a7) = 0x02,

[ 27](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5adf3b0e226fd373b882e27ed494fba265) [MS\_OS\_20\_FEATURE\_COMPATIBLE\_ID](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5adf3b0e226fd373b882e27ed494fba265) = 0x03,

[ 28](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5ad49ae449e2e2ff519a69018612ab5e62) [MS\_OS\_20\_FEATURE\_REG\_PROPERTY](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5ad49ae449e2e2ff519a69018612ab5e62) = 0x04,

[ 29](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5a7061acf1dbbeb7e2fbb88d149d295009) [MS\_OS\_20\_FEATURE\_MIN\_RESUME\_TIME](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5a7061acf1dbbeb7e2fbb88d149d295009) = 0x05,

[ 30](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5ac7fc46a0124656e986871ae3b085536c) [MS\_OS\_20\_FEATURE\_MODEL\_ID](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5ac7fc46a0124656e986871ae3b085536c) = 0x06,

[ 31](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5ab457a91ffd658376d87d7d32ad770004) [MS\_OS\_20\_FEATURE\_CCGP\_DEVICE](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5ab457a91ffd658376d87d7d32ad770004) = 0x07,

[ 32](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5a2f7940f495e1a996692f474a456d63d6) [MS\_OS\_20\_FEATURE\_VENDOR\_REVISION](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5a2f7940f495e1a996692f474a456d63d6) = 0x08

33};

34

[ 35](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254f)enum [msosv2\_property\_data\_type](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254f) {

[ 36](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fac1e0035b4badb15f714bff249514ef17) [MS\_OS\_20\_PROPERTY\_DATA\_RESERVED](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fac1e0035b4badb15f714bff249514ef17) = 0,

[ 37](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fa404430118680c625a399662e981c4489) [MS\_OS\_20\_PROPERTY\_DATA\_REG\_SZ](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fa404430118680c625a399662e981c4489) = 1,

[ 38](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fa9245e361cbe8425c1b54958ba0c0902c) [MS\_OS\_20\_PROPERTY\_DATA\_REG\_EXPAND\_SZ](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fa9245e361cbe8425c1b54958ba0c0902c) = 2,

[ 39](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fae8bd325ca3f9cc1d33d229d0de14aba1) [MS\_OS\_20\_PROPERTY\_DATA\_REG\_BINARY](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fae8bd325ca3f9cc1d33d229d0de14aba1) = 3,

[ 40](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254faa831bf4ba88de3eb768745c41a8dee10) [MS\_OS\_20\_PROPERTY\_DATA\_REG\_DWORD\_LITTLE\_ENDIAN](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254faa831bf4ba88de3eb768745c41a8dee10) = 4,

[ 41](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fa969e1f96f1582db317bbf96d183ae670) [MS\_OS\_20\_PROPERTY\_DATA\_REG\_DWORD\_BIG\_ENDIAN](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fa969e1f96f1582db317bbf96d183ae670) = 5,

[ 42](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fa4050949a26b3a61f1aeecc996eb02d81) [MS\_OS\_20\_PROPERTY\_DATA\_REG\_LINK](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fa4050949a26b3a61f1aeecc996eb02d81) = 6,

[ 43](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fa89b2d8dfbddc343879edc14a5c9f93f5) [MS\_OS\_20\_PROPERTY\_DATA\_REG\_MULTI\_SZ](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fa89b2d8dfbddc343879edc14a5c9f93f5) = 7

44};

45

46/\* Microsoft OS 2.0 descriptor set header \*/

[ 47](structmsosv2__descriptor__set__header.md)struct [msosv2\_descriptor\_set\_header](structmsosv2__descriptor__set__header.md) {

[ 48](structmsosv2__descriptor__set__header.md#a4281eeb2128138b597fb53577ec8d57f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wLength](structmsosv2__descriptor__set__header.md#a4281eeb2128138b597fb53577ec8d57f);

[ 49](structmsosv2__descriptor__set__header.md#ae4931afed75f035e9dff4856ddee8609) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wDescriptorType](structmsosv2__descriptor__set__header.md#ae4931afed75f035e9dff4856ddee8609);

[ 50](structmsosv2__descriptor__set__header.md#acf91f874e365a7f8ef60eaa19da517b4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dwWindowsVersion](structmsosv2__descriptor__set__header.md#acf91f874e365a7f8ef60eaa19da517b4);

[ 51](structmsosv2__descriptor__set__header.md#a3bab654cec13541096f08b43adb55f40) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wTotalLength](structmsosv2__descriptor__set__header.md#a3bab654cec13541096f08b43adb55f40);

52} \_\_packed;

53

54/\* Microsoft OS 2.0 configuration subset header

55 \* This header is for composite devices with multiple configurations.

56 \*/

[ 57](structmsosv2__configuration__subset__header.md)struct [msosv2\_configuration\_subset\_header](structmsosv2__configuration__subset__header.md) {

[ 58](structmsosv2__configuration__subset__header.md#a7468f6428046553abf5e97172b52d477) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wLength](structmsosv2__configuration__subset__header.md#a7468f6428046553abf5e97172b52d477);

[ 59](structmsosv2__configuration__subset__header.md#ada03982dd6680a45d7cd2ba9e791c54e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wDescriptorType](structmsosv2__configuration__subset__header.md#ada03982dd6680a45d7cd2ba9e791c54e);

[ 60](structmsosv2__configuration__subset__header.md#a044e9d3a0ec479564406f04d895e353c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bConfigurationValue](structmsosv2__configuration__subset__header.md#a044e9d3a0ec479564406f04d895e353c);

[ 61](structmsosv2__configuration__subset__header.md#aa063ff78775c00edde1de6e274a2b817) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bReserved](structmsosv2__configuration__subset__header.md#aa063ff78775c00edde1de6e274a2b817);

[ 62](structmsosv2__configuration__subset__header.md#a044cf7d76fa93bfaa265bd5c24d8d413) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wTotalLength](structmsosv2__configuration__subset__header.md#a044cf7d76fa93bfaa265bd5c24d8d413);

63} \_\_packed;

64

65/\* Microsoft OS 2.0 function subset header

66 \* Note: This must be used if your device has multiple interfaces and cannot be used otherwise.

67 \*/

[ 68](structmsosv2__function__subset__header.md)struct [msosv2\_function\_subset\_header](structmsosv2__function__subset__header.md) {

[ 69](structmsosv2__function__subset__header.md#a10e00ccb02a6e2c9c4c5f4d634414a0c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wLength](structmsosv2__function__subset__header.md#a10e00ccb02a6e2c9c4c5f4d634414a0c);

[ 70](structmsosv2__function__subset__header.md#a4a93fdd2d9ea65b5b9097f921629c644) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wDescriptorType](structmsosv2__function__subset__header.md#a4a93fdd2d9ea65b5b9097f921629c644);

[ 71](structmsosv2__function__subset__header.md#abf8bbff467411af8f259d2f16dc73649) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bFirstInterface](structmsosv2__function__subset__header.md#abf8bbff467411af8f259d2f16dc73649);

[ 72](structmsosv2__function__subset__header.md#a07a64f2419014f41fa356fd85976985d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bReserved](structmsosv2__function__subset__header.md#a07a64f2419014f41fa356fd85976985d);

[ 73](structmsosv2__function__subset__header.md#a7c3d3e7cd0577dc4ceab66615fefbe46) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wSubsetLength](structmsosv2__function__subset__header.md#a7c3d3e7cd0577dc4ceab66615fefbe46);

74} \_\_packed;

75

76/\* Microsoft OS 2.0 compatible ID descriptor \*/

[ 77](structmsosv2__compatible__id.md)struct [msosv2\_compatible\_id](structmsosv2__compatible__id.md) {

[ 78](structmsosv2__compatible__id.md#ad2fabcbcfe86dd7f6c7e21607392ed9f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wLength](structmsosv2__compatible__id.md#ad2fabcbcfe86dd7f6c7e21607392ed9f);

[ 79](structmsosv2__compatible__id.md#adfb121211a3e2519cdbf3afa91cd48e3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wDescriptorType](structmsosv2__compatible__id.md#adfb121211a3e2519cdbf3afa91cd48e3);

[ 80](structmsosv2__compatible__id.md#a213f32b16fda92bc5526abee2d5922b5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [CompatibleID](structmsosv2__compatible__id.md#a213f32b16fda92bc5526abee2d5922b5)[8];

[ 81](structmsosv2__compatible__id.md#affc8c55b00ddcc20841054ac8d8c6844) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [SubCompatibleID](structmsosv2__compatible__id.md#affc8c55b00ddcc20841054ac8d8c6844)[8];

82} \_\_packed;

83

84/\* Microsoft OS 2.0 Registry property descriptor: DeviceInterfaceGUIDs \*/

[ 85](structmsosv2__guids__property.md)struct [msosv2\_guids\_property](structmsosv2__guids__property.md) {

[ 86](structmsosv2__guids__property.md#a500199bebfa7f8bf300be51310497a0c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wLength](structmsosv2__guids__property.md#a500199bebfa7f8bf300be51310497a0c);

[ 87](structmsosv2__guids__property.md#acaa81e6bbaaec95922a80ef5a6000cd9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wDescriptorType](structmsosv2__guids__property.md#acaa81e6bbaaec95922a80ef5a6000cd9);

[ 88](structmsosv2__guids__property.md#aee143372e2bd13a32ae61e68ab429fbe) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wPropertyDataType](structmsosv2__guids__property.md#aee143372e2bd13a32ae61e68ab429fbe);

[ 89](structmsosv2__guids__property.md#a815f24af18f726244a9ab7d9f67e1cab) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wPropertyNameLength](structmsosv2__guids__property.md#a815f24af18f726244a9ab7d9f67e1cab);

[ 90](structmsosv2__guids__property.md#ac447835ec1446a2e190228cab2b7dca8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [PropertyName](structmsosv2__guids__property.md#ac447835ec1446a2e190228cab2b7dca8)[42];

[ 91](structmsosv2__guids__property.md#a1740a7fb0134313dba90cf794f0218f1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wPropertyDataLength](structmsosv2__guids__property.md#a1740a7fb0134313dba90cf794f0218f1);

[ 92](structmsosv2__guids__property.md#abf28542190ae7fececadacd3e8dba58a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bPropertyData](structmsosv2__guids__property.md#abf28542190ae7fececadacd3e8dba58a)[80];

93} \_\_packed;

94

95/\* DeviceInterfaceGUIDs \*/

[ 96](msos__desc_8h.md#a927c65f355232352e67c60efdd293cff)#define DEVICE\_INTERFACE\_GUIDS\_PROPERTY\_NAME \

97 'D', 0x00, 'e', 0x00, 'v', 0x00, 'i', 0x00, 'c', 0x00, 'e', 0x00, \

98 'I', 0x00, 'n', 0x00, 't', 0x00, 'e', 0x00, 'r', 0x00, 'f', 0x00, \

99 'a', 0x00, 'c', 0x00, 'e', 0x00, 'G', 0x00, 'U', 0x00, 'I', 0x00, \

100 'D', 0x00, 's', 0x00, 0x00, 0x00

101

102/\* Microsoft OS 2.0 minimum USB resume time descriptor \*/

[ 103](structmsosv2__resume__time.md)struct [msosv2\_resume\_time](structmsosv2__resume__time.md) {

[ 104](structmsosv2__resume__time.md#a95a1ba0d9e5d0019dfeabfea0ddaf205) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wLength](structmsosv2__resume__time.md#a95a1ba0d9e5d0019dfeabfea0ddaf205);

[ 105](structmsosv2__resume__time.md#a22fc11df55af95324cfeb2459a544bd4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wDescriptorType](structmsosv2__resume__time.md#a22fc11df55af95324cfeb2459a544bd4);

[ 106](structmsosv2__resume__time.md#a33ff93b8c7d97dc9732158b2293cd377) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bResumeRecoveryTime](structmsosv2__resume__time.md#a33ff93b8c7d97dc9732158b2293cd377);

[ 107](structmsosv2__resume__time.md#a1a08a4ec1b884a68ffc6b52a84e747aa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bResumeSignalingTime](structmsosv2__resume__time.md#a1a08a4ec1b884a68ffc6b52a84e747aa);

108} \_\_packed;

109

110/\* Microsoft OS 2.0 model ID descriptor \*/

[ 111](structmsosv2__model__id.md)struct [msosv2\_model\_id](structmsosv2__model__id.md) {

[ 112](structmsosv2__model__id.md#a2355b2ab759e661462d61ffbdb7c29cd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wLength](structmsosv2__model__id.md#a2355b2ab759e661462d61ffbdb7c29cd);

[ 113](structmsosv2__model__id.md#af03a88860ff6086b0cda956f2ccff824) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wDescriptorType](structmsosv2__model__id.md#af03a88860ff6086b0cda956f2ccff824);

[ 114](structmsosv2__model__id.md#ae87e515d83e0f979c993ef24d2486d08) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ModelID](structmsosv2__model__id.md#ae87e515d83e0f979c993ef24d2486d08)[16];

115} \_\_packed;

116

117/\* Microsoft OS 2.0 CCGP device descriptor \*/

[ 118](structmsosv2__ccgp__device.md)struct [msosv2\_ccgp\_device](structmsosv2__ccgp__device.md) {

[ 119](structmsosv2__ccgp__device.md#a43cc94903315cb1a09418325630f936c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wLength](structmsosv2__ccgp__device.md#a43cc94903315cb1a09418325630f936c);

[ 120](structmsosv2__ccgp__device.md#af3713e6a6185c8725d21fd5f1edbf84a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wDescriptorType](structmsosv2__ccgp__device.md#af3713e6a6185c8725d21fd5f1edbf84a);

121} \_\_packed;

122

123/\* Microsoft OS 2.0 vendor revision descriptor \*/

[ 124](structmsosv2__vendor__revision.md)struct [msosv2\_vendor\_revision](structmsosv2__vendor__revision.md) {

[ 125](structmsosv2__vendor__revision.md#a4b29a145268e89c416f50cddc28f0ff4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wLength](structmsosv2__vendor__revision.md#a4b29a145268e89c416f50cddc28f0ff4);

[ 126](structmsosv2__vendor__revision.md#a6ad0f9afb827947e4e2bfca339b70ceb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wDescriptorType](structmsosv2__vendor__revision.md#a6ad0f9afb827947e4e2bfca339b70ceb);

[ 127](structmsosv2__vendor__revision.md#aebed4cce3752a96a82fb25e3071a021c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [VendorRevision](structmsosv2__vendor__revision.md#aebed4cce3752a96a82fb25e3071a021c);

128} \_\_packed;

129

130

131#endif /\* ZEPHYR\_INCLUDE\_USB\_MSOS\_DESC\_H \*/

[msosv2\_property\_data\_type](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254f)

msosv2\_property\_data\_type

**Definition** msos\_desc.h:35

[MS\_OS\_20\_PROPERTY\_DATA\_REG\_SZ](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fa404430118680c625a399662e981c4489)

@ MS\_OS\_20\_PROPERTY\_DATA\_REG\_SZ

**Definition** msos\_desc.h:37

[MS\_OS\_20\_PROPERTY\_DATA\_REG\_LINK](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fa4050949a26b3a61f1aeecc996eb02d81)

@ MS\_OS\_20\_PROPERTY\_DATA\_REG\_LINK

**Definition** msos\_desc.h:42

[MS\_OS\_20\_PROPERTY\_DATA\_REG\_MULTI\_SZ](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fa89b2d8dfbddc343879edc14a5c9f93f5)

@ MS\_OS\_20\_PROPERTY\_DATA\_REG\_MULTI\_SZ

**Definition** msos\_desc.h:43

[MS\_OS\_20\_PROPERTY\_DATA\_REG\_EXPAND\_SZ](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fa9245e361cbe8425c1b54958ba0c0902c)

@ MS\_OS\_20\_PROPERTY\_DATA\_REG\_EXPAND\_SZ

**Definition** msos\_desc.h:38

[MS\_OS\_20\_PROPERTY\_DATA\_REG\_DWORD\_BIG\_ENDIAN](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fa969e1f96f1582db317bbf96d183ae670)

@ MS\_OS\_20\_PROPERTY\_DATA\_REG\_DWORD\_BIG\_ENDIAN

**Definition** msos\_desc.h:41

[MS\_OS\_20\_PROPERTY\_DATA\_REG\_DWORD\_LITTLE\_ENDIAN](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254faa831bf4ba88de3eb768745c41a8dee10)

@ MS\_OS\_20\_PROPERTY\_DATA\_REG\_DWORD\_LITTLE\_ENDIAN

**Definition** msos\_desc.h:40

[MS\_OS\_20\_PROPERTY\_DATA\_RESERVED](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fac1e0035b4badb15f714bff249514ef17)

@ MS\_OS\_20\_PROPERTY\_DATA\_RESERVED

**Definition** msos\_desc.h:36

[MS\_OS\_20\_PROPERTY\_DATA\_REG\_BINARY](msos__desc_8h.md#a1afad4029116a837d4430a0ea976254fae8bd325ca3f9cc1d33d229d0de14aba1)

@ MS\_OS\_20\_PROPERTY\_DATA\_REG\_BINARY

**Definition** msos\_desc.h:39

[msosv2\_descriptor\_index](msos__desc_8h.md#ab443ad91634b7a8fb19fc2aa7108e631)

msosv2\_descriptor\_index

**Definition** msos\_desc.h:18

[MS\_OS\_20\_SET\_ALT\_ENUMERATION](msos__desc_8h.md#ab443ad91634b7a8fb19fc2aa7108e631a2ae9d4948f03b7d9623c547daa0a9116)

@ MS\_OS\_20\_SET\_ALT\_ENUMERATION

**Definition** msos\_desc.h:20

[MS\_OS\_20\_DESCRIPTOR\_INDEX](msos__desc_8h.md#ab443ad91634b7a8fb19fc2aa7108e631abe0e6e00164db250e4ad900f418a57d5)

@ MS\_OS\_20\_DESCRIPTOR\_INDEX

**Definition** msos\_desc.h:19

[msosv2\_descriptor\_type](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5)

msosv2\_descriptor\_type

**Definition** msos\_desc.h:23

[MS\_OS\_20\_SUBSET\_HEADER\_FUNCTION](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5a1200730075635cba8dea3420be41d1a7)

@ MS\_OS\_20\_SUBSET\_HEADER\_FUNCTION

**Definition** msos\_desc.h:26

[MS\_OS\_20\_FEATURE\_VENDOR\_REVISION](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5a2f7940f495e1a996692f474a456d63d6)

@ MS\_OS\_20\_FEATURE\_VENDOR\_REVISION

**Definition** msos\_desc.h:32

[MS\_OS\_20\_FEATURE\_MIN\_RESUME\_TIME](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5a7061acf1dbbeb7e2fbb88d149d295009)

@ MS\_OS\_20\_FEATURE\_MIN\_RESUME\_TIME

**Definition** msos\_desc.h:29

[MS\_OS\_20\_FEATURE\_CCGP\_DEVICE](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5ab457a91ffd658376d87d7d32ad770004)

@ MS\_OS\_20\_FEATURE\_CCGP\_DEVICE

**Definition** msos\_desc.h:31

[MS\_OS\_20\_SET\_HEADER\_DESCRIPTOR](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5ac74a28d4e873b255d5b027af5ffffb5d)

@ MS\_OS\_20\_SET\_HEADER\_DESCRIPTOR

**Definition** msos\_desc.h:24

[MS\_OS\_20\_FEATURE\_MODEL\_ID](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5ac7fc46a0124656e986871ae3b085536c)

@ MS\_OS\_20\_FEATURE\_MODEL\_ID

**Definition** msos\_desc.h:30

[MS\_OS\_20\_FEATURE\_REG\_PROPERTY](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5ad49ae449e2e2ff519a69018612ab5e62)

@ MS\_OS\_20\_FEATURE\_REG\_PROPERTY

**Definition** msos\_desc.h:28

[MS\_OS\_20\_FEATURE\_COMPATIBLE\_ID](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5adf3b0e226fd373b882e27ed494fba265)

@ MS\_OS\_20\_FEATURE\_COMPATIBLE\_ID

**Definition** msos\_desc.h:27

[MS\_OS\_20\_SUBSET\_HEADER\_CONFIGURATION](msos__desc_8h.md#ae46389cacf4c5cca962702fcf0f6feb5afe117782c0101a880e152a8a1110ecbc)

@ MS\_OS\_20\_SUBSET\_HEADER\_CONFIGURATION

**Definition** msos\_desc.h:25

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[msosv2\_ccgp\_device](structmsosv2__ccgp__device.md)

**Definition** msos\_desc.h:118

[msosv2\_ccgp\_device::wLength](structmsosv2__ccgp__device.md#a43cc94903315cb1a09418325630f936c)

uint16\_t wLength

**Definition** msos\_desc.h:119

[msosv2\_ccgp\_device::wDescriptorType](structmsosv2__ccgp__device.md#af3713e6a6185c8725d21fd5f1edbf84a)

uint16\_t wDescriptorType

**Definition** msos\_desc.h:120

[msosv2\_compatible\_id](structmsosv2__compatible__id.md)

**Definition** msos\_desc.h:77

[msosv2\_compatible\_id::CompatibleID](structmsosv2__compatible__id.md#a213f32b16fda92bc5526abee2d5922b5)

uint8\_t CompatibleID[8]

**Definition** msos\_desc.h:80

[msosv2\_compatible\_id::wLength](structmsosv2__compatible__id.md#ad2fabcbcfe86dd7f6c7e21607392ed9f)

uint16\_t wLength

**Definition** msos\_desc.h:78

[msosv2\_compatible\_id::wDescriptorType](structmsosv2__compatible__id.md#adfb121211a3e2519cdbf3afa91cd48e3)

uint16\_t wDescriptorType

**Definition** msos\_desc.h:79

[msosv2\_compatible\_id::SubCompatibleID](structmsosv2__compatible__id.md#affc8c55b00ddcc20841054ac8d8c6844)

uint8\_t SubCompatibleID[8]

**Definition** msos\_desc.h:81

[msosv2\_configuration\_subset\_header](structmsosv2__configuration__subset__header.md)

**Definition** msos\_desc.h:57

[msosv2\_configuration\_subset\_header::wTotalLength](structmsosv2__configuration__subset__header.md#a044cf7d76fa93bfaa265bd5c24d8d413)

uint16\_t wTotalLength

**Definition** msos\_desc.h:62

[msosv2\_configuration\_subset\_header::bConfigurationValue](structmsosv2__configuration__subset__header.md#a044e9d3a0ec479564406f04d895e353c)

uint8\_t bConfigurationValue

**Definition** msos\_desc.h:60

[msosv2\_configuration\_subset\_header::wLength](structmsosv2__configuration__subset__header.md#a7468f6428046553abf5e97172b52d477)

uint16\_t wLength

**Definition** msos\_desc.h:58

[msosv2\_configuration\_subset\_header::bReserved](structmsosv2__configuration__subset__header.md#aa063ff78775c00edde1de6e274a2b817)

uint8\_t bReserved

**Definition** msos\_desc.h:61

[msosv2\_configuration\_subset\_header::wDescriptorType](structmsosv2__configuration__subset__header.md#ada03982dd6680a45d7cd2ba9e791c54e)

uint16\_t wDescriptorType

**Definition** msos\_desc.h:59

[msosv2\_descriptor\_set\_header](structmsosv2__descriptor__set__header.md)

**Definition** msos\_desc.h:47

[msosv2\_descriptor\_set\_header::wTotalLength](structmsosv2__descriptor__set__header.md#a3bab654cec13541096f08b43adb55f40)

uint16\_t wTotalLength

**Definition** msos\_desc.h:51

[msosv2\_descriptor\_set\_header::wLength](structmsosv2__descriptor__set__header.md#a4281eeb2128138b597fb53577ec8d57f)

uint16\_t wLength

**Definition** msos\_desc.h:48

[msosv2\_descriptor\_set\_header::dwWindowsVersion](structmsosv2__descriptor__set__header.md#acf91f874e365a7f8ef60eaa19da517b4)

uint32\_t dwWindowsVersion

**Definition** msos\_desc.h:50

[msosv2\_descriptor\_set\_header::wDescriptorType](structmsosv2__descriptor__set__header.md#ae4931afed75f035e9dff4856ddee8609)

uint16\_t wDescriptorType

**Definition** msos\_desc.h:49

[msosv2\_function\_subset\_header](structmsosv2__function__subset__header.md)

**Definition** msos\_desc.h:68

[msosv2\_function\_subset\_header::bReserved](structmsosv2__function__subset__header.md#a07a64f2419014f41fa356fd85976985d)

uint8\_t bReserved

**Definition** msos\_desc.h:72

[msosv2\_function\_subset\_header::wLength](structmsosv2__function__subset__header.md#a10e00ccb02a6e2c9c4c5f4d634414a0c)

uint16\_t wLength

**Definition** msos\_desc.h:69

[msosv2\_function\_subset\_header::wDescriptorType](structmsosv2__function__subset__header.md#a4a93fdd2d9ea65b5b9097f921629c644)

uint16\_t wDescriptorType

**Definition** msos\_desc.h:70

[msosv2\_function\_subset\_header::wSubsetLength](structmsosv2__function__subset__header.md#a7c3d3e7cd0577dc4ceab66615fefbe46)

uint16\_t wSubsetLength

**Definition** msos\_desc.h:73

[msosv2\_function\_subset\_header::bFirstInterface](structmsosv2__function__subset__header.md#abf8bbff467411af8f259d2f16dc73649)

uint8\_t bFirstInterface

**Definition** msos\_desc.h:71

[msosv2\_guids\_property](structmsosv2__guids__property.md)

**Definition** msos\_desc.h:85

[msosv2\_guids\_property::wPropertyDataLength](structmsosv2__guids__property.md#a1740a7fb0134313dba90cf794f0218f1)

uint16\_t wPropertyDataLength

**Definition** msos\_desc.h:91

[msosv2\_guids\_property::wLength](structmsosv2__guids__property.md#a500199bebfa7f8bf300be51310497a0c)

uint16\_t wLength

**Definition** msos\_desc.h:86

[msosv2\_guids\_property::wPropertyNameLength](structmsosv2__guids__property.md#a815f24af18f726244a9ab7d9f67e1cab)

uint16\_t wPropertyNameLength

**Definition** msos\_desc.h:89

[msosv2\_guids\_property::bPropertyData](structmsosv2__guids__property.md#abf28542190ae7fececadacd3e8dba58a)

uint8\_t bPropertyData[80]

**Definition** msos\_desc.h:92

[msosv2\_guids\_property::PropertyName](structmsosv2__guids__property.md#ac447835ec1446a2e190228cab2b7dca8)

uint8\_t PropertyName[42]

**Definition** msos\_desc.h:90

[msosv2\_guids\_property::wDescriptorType](structmsosv2__guids__property.md#acaa81e6bbaaec95922a80ef5a6000cd9)

uint16\_t wDescriptorType

**Definition** msos\_desc.h:87

[msosv2\_guids\_property::wPropertyDataType](structmsosv2__guids__property.md#aee143372e2bd13a32ae61e68ab429fbe)

uint16\_t wPropertyDataType

**Definition** msos\_desc.h:88

[msosv2\_model\_id](structmsosv2__model__id.md)

**Definition** msos\_desc.h:111

[msosv2\_model\_id::wLength](structmsosv2__model__id.md#a2355b2ab759e661462d61ffbdb7c29cd)

uint16\_t wLength

**Definition** msos\_desc.h:112

[msosv2\_model\_id::ModelID](structmsosv2__model__id.md#ae87e515d83e0f979c993ef24d2486d08)

uint8\_t ModelID[16]

**Definition** msos\_desc.h:114

[msosv2\_model\_id::wDescriptorType](structmsosv2__model__id.md#af03a88860ff6086b0cda956f2ccff824)

uint16\_t wDescriptorType

**Definition** msos\_desc.h:113

[msosv2\_resume\_time](structmsosv2__resume__time.md)

**Definition** msos\_desc.h:103

[msosv2\_resume\_time::bResumeSignalingTime](structmsosv2__resume__time.md#a1a08a4ec1b884a68ffc6b52a84e747aa)

uint8\_t bResumeSignalingTime

**Definition** msos\_desc.h:107

[msosv2\_resume\_time::wDescriptorType](structmsosv2__resume__time.md#a22fc11df55af95324cfeb2459a544bd4)

uint16\_t wDescriptorType

**Definition** msos\_desc.h:105

[msosv2\_resume\_time::bResumeRecoveryTime](structmsosv2__resume__time.md#a33ff93b8c7d97dc9732158b2293cd377)

uint8\_t bResumeRecoveryTime

**Definition** msos\_desc.h:106

[msosv2\_resume\_time::wLength](structmsosv2__resume__time.md#a95a1ba0d9e5d0019dfeabfea0ddaf205)

uint16\_t wLength

**Definition** msos\_desc.h:104

[msosv2\_vendor\_revision](structmsosv2__vendor__revision.md)

**Definition** msos\_desc.h:124

[msosv2\_vendor\_revision::wLength](structmsosv2__vendor__revision.md#a4b29a145268e89c416f50cddc28f0ff4)

uint16\_t wLength

**Definition** msos\_desc.h:125

[msosv2\_vendor\_revision::wDescriptorType](structmsosv2__vendor__revision.md#a6ad0f9afb827947e4e2bfca339b70ceb)

uint16\_t wDescriptorType

**Definition** msos\_desc.h:126

[msosv2\_vendor\_revision::VendorRevision](structmsosv2__vendor__revision.md#aebed4cce3752a96a82fb25e3071a021c)

uint16\_t VendorRevision

**Definition** msos\_desc.h:127

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [msos\_desc.h](msos__desc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
