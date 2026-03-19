---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/grow__r502a_8h_source.html
original_path: doxygen/html/grow__r502a_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

grow\_r502a.h

[Go to the documentation of this file.](grow__r502a_8h.md)

1/\*

2 \* Copyright (c) 2022 Linumiz

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_GROW\_R502A\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_GROW\_R502A\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

14#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

15

16/\*LED color code\*/

[ 17](grow__r502a_8h.md#a843fa88a16ab6b47c4e517ddbc01b4a8)enum [r502a\_led\_color\_idx](grow__r502a_8h.md#a843fa88a16ab6b47c4e517ddbc01b4a8) {

[ 18](grow__r502a_8h.md#a843fa88a16ab6b47c4e517ddbc01b4a8a667a844dde544590ab7b6e3defd4016c) [R502A\_LED\_COLOR\_RED](grow__r502a_8h.md#a843fa88a16ab6b47c4e517ddbc01b4a8a667a844dde544590ab7b6e3defd4016c) = 0x01,

[ 19](grow__r502a_8h.md#a843fa88a16ab6b47c4e517ddbc01b4a8a0685eb3e0e4de6faa0577fb5f7d0f845) [R502A\_LED\_COLOR\_BLUE](grow__r502a_8h.md#a843fa88a16ab6b47c4e517ddbc01b4a8a0685eb3e0e4de6faa0577fb5f7d0f845),

[ 20](grow__r502a_8h.md#a843fa88a16ab6b47c4e517ddbc01b4a8ad477284ea70fb76c43a386ed3537be6c) [R502A\_LED\_COLOR\_PURPLE](grow__r502a_8h.md#a843fa88a16ab6b47c4e517ddbc01b4a8ad477284ea70fb76c43a386ed3537be6c),

21};

22

[ 23](grow__r502a_8h.md#aaab815dc7de2a1ff5596ad6fdc1e28c2)#define R502A\_BAUD\_9600 1

[ 24](grow__r502a_8h.md#a102611233e481e26c8cdafe97efe77b0)#define R502A\_BAUD\_19200 2

[ 25](grow__r502a_8h.md#aab799d94bd0dd10ea55c47cd66ba74fb)#define R502A\_BAUD\_38400 4

[ 26](grow__r502a_8h.md#a19ab94871e6e51660432c29130c183fb)#define R502A\_BAUD\_57600 6

[ 27](grow__r502a_8h.md#aa0f6b1beacb3a3e57f1bd6ab3951ba6b)#define R502A\_BAUD\_115200 12

28

[ 29](grow__r502a_8h.md#a48154de53541aced1e78537f10f2f3d1)enum [r502a\_sec\_level](grow__r502a_8h.md#a48154de53541aced1e78537f10f2f3d1) {

[ 30](grow__r502a_8h.md#a48154de53541aced1e78537f10f2f3d1a2220c963d396a7d6604ff0b47e3b6db7) [R502A\_SEC\_LEVEL\_1](grow__r502a_8h.md#a48154de53541aced1e78537f10f2f3d1a2220c963d396a7d6604ff0b47e3b6db7) = 1,

[ 31](grow__r502a_8h.md#a48154de53541aced1e78537f10f2f3d1a9fbe3bed318932b9fab282aee7e823ef) [R502A\_SEC\_LEVEL\_2](grow__r502a_8h.md#a48154de53541aced1e78537f10f2f3d1a9fbe3bed318932b9fab282aee7e823ef),

[ 32](grow__r502a_8h.md#a48154de53541aced1e78537f10f2f3d1adb0e8b2e0242be58c32cf1fb8c3c00fa) [R502A\_SEC\_LEVEL\_3](grow__r502a_8h.md#a48154de53541aced1e78537f10f2f3d1adb0e8b2e0242be58c32cf1fb8c3c00fa),

[ 33](grow__r502a_8h.md#a48154de53541aced1e78537f10f2f3d1a1e579d5283fb984a555f918828b3e1e9) [R502A\_SEC\_LEVEL\_4](grow__r502a_8h.md#a48154de53541aced1e78537f10f2f3d1a1e579d5283fb984a555f918828b3e1e9),

[ 34](grow__r502a_8h.md#a48154de53541aced1e78537f10f2f3d1abcb8f9a6447757b0fcb8ef4f63979dc1) [R502A\_SEC\_LEVEL\_5](grow__r502a_8h.md#a48154de53541aced1e78537f10f2f3d1abcb8f9a6447757b0fcb8ef4f63979dc1)

35};

36

[ 37](grow__r502a_8h.md#a3298eb4d591ba56131bae8137888dcd8)enum [r502a\_data\_len](grow__r502a_8h.md#a3298eb4d591ba56131bae8137888dcd8) {

[ 38](grow__r502a_8h.md#a3298eb4d591ba56131bae8137888dcd8a6be1d185636994b69006b14188d003cf) [R502A\_PKG\_LEN\_32](grow__r502a_8h.md#a3298eb4d591ba56131bae8137888dcd8a6be1d185636994b69006b14188d003cf),

[ 39](grow__r502a_8h.md#a3298eb4d591ba56131bae8137888dcd8a61ab7cac6d6613f3465157f1ee09b2ee) [R502A\_PKG\_LEN\_64](grow__r502a_8h.md#a3298eb4d591ba56131bae8137888dcd8a61ab7cac6d6613f3465157f1ee09b2ee),

[ 40](grow__r502a_8h.md#a3298eb4d591ba56131bae8137888dcd8ad5a47c82dd3733cad5a2da69f33735fe) [R502A\_PKG\_LEN\_128](grow__r502a_8h.md#a3298eb4d591ba56131bae8137888dcd8ad5a47c82dd3733cad5a2da69f33735fe),

[ 41](grow__r502a_8h.md#a3298eb4d591ba56131bae8137888dcd8a4fa6ae11c8e8f44101a729c4149a1101) [R502A\_PKG\_LEN\_256](grow__r502a_8h.md#a3298eb4d591ba56131bae8137888dcd8a4fa6ae11c8e8f44101a729c4149a1101)

42};

43

[ 44](grow__r502a_8h.md#a16242f27a53b430ea3cf165fbc7ce70b)enum [r502a\_sys\_param\_set](grow__r502a_8h.md#a16242f27a53b430ea3cf165fbc7ce70b) {

[ 45](grow__r502a_8h.md#a16242f27a53b430ea3cf165fbc7ce70bacef6f845b078fffb0f5f10a93cba3721) [R502A\_BAUD\_RATE](grow__r502a_8h.md#a16242f27a53b430ea3cf165fbc7ce70bacef6f845b078fffb0f5f10a93cba3721) = 4,

[ 46](grow__r502a_8h.md#a16242f27a53b430ea3cf165fbc7ce70ba2795f5eb1ee8feeba7f57d0bdc4ec519) [R502A\_SECURITY\_LEVEL](grow__r502a_8h.md#a16242f27a53b430ea3cf165fbc7ce70ba2795f5eb1ee8feeba7f57d0bdc4ec519),

[ 47](grow__r502a_8h.md#a16242f27a53b430ea3cf165fbc7ce70baa356f4aea69d118b8283d347b816bca1) [R502A\_DATA\_PKG\_LEN](grow__r502a_8h.md#a16242f27a53b430ea3cf165fbc7ce70baa356f4aea69d118b8283d347b816bca1)

48};

49

[ 50](structr502a__sys__param.md)struct [r502a\_sys\_param](structr502a__sys__param.md) {

[ 51](structr502a__sys__param.md#adb966712020f826ecc646c04a93edd5f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [status\_reg](structr502a__sys__param.md#adb966712020f826ecc646c04a93edd5f);

[ 52](structr502a__sys__param.md#aaa11e04312322afa3f406f872763d8be) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [system\_id](structr502a__sys__param.md#aaa11e04312322afa3f406f872763d8be);

[ 53](structr502a__sys__param.md#a4cc85b5b8ec7a511f9fc5dd3912c0a39) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [lib\_size](structr502a__sys__param.md#a4cc85b5b8ec7a511f9fc5dd3912c0a39);

[ 54](structr502a__sys__param.md#a076a36d66a6908eee2131a8f652fefa4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sec\_level](structr502a__sys__param.md#a076a36d66a6908eee2131a8f652fefa4);

[ 55](structr502a__sys__param.md#ac3f2dc2456a29eeda55417ba91a29f62) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [addr](structr502a__sys__param.md#ac3f2dc2456a29eeda55417ba91a29f62);

[ 56](structr502a__sys__param.md#a8c3470762665d940a3ec2dc214150bf8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [data\_pkt\_size](structr502a__sys__param.md#a8c3470762665d940a3ec2dc214150bf8);

[ 57](structr502a__sys__param.md#adf5a91c5972af06d1bf9beb6a9040bac) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [baud](structr502a__sys__param.md#adf5a91c5972af06d1bf9beb6a9040bac);

58} \_\_packed;

59

[ 60](structr502a__template.md)struct [r502a\_template](structr502a__template.md) {

[ 61](structr502a__template.md#aca6dc417fc7e1de22da94e4d4e2b96a9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structr502a__template.md#aca6dc417fc7e1de22da94e4d4e2b96a9);

[ 62](structr502a__template.md#a2d4ab0b0ea4e4cf8b061705910639ae4) size\_t [len](structr502a__template.md#a2d4ab0b0ea4e4cf8b061705910639ae4);

63};

[ 64](grow__r502a_8h.md#a8ff24814059dda20e6b36fe8cc0be30c)enum [sensor\_channel\_grow\_r502a](grow__r502a_8h.md#a8ff24814059dda20e6b36fe8cc0be30c) {

[ 66](grow__r502a_8h.md#a8ff24814059dda20e6b36fe8cc0be30ca51abf7335f93117c01052a641a5f5cf2) [SENSOR\_CHAN\_FINGERPRINT](grow__r502a_8h.md#a8ff24814059dda20e6b36fe8cc0be30ca51abf7335f93117c01052a641a5f5cf2) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12),

67};

68

[ 69](grow__r502a_8h.md#a721dcba985d9010bb1f48e82b0027eb4)enum [sensor\_trigger\_type\_grow\_r502a](grow__r502a_8h.md#a721dcba985d9010bb1f48e82b0027eb4) {

[ 71](grow__r502a_8h.md#a721dcba985d9010bb1f48e82b0027eb4a5cf35bed5ff3c6f55b00f19cde2fc0e4) [SENSOR\_TRIG\_TOUCH](grow__r502a_8h.md#a721dcba985d9010bb1f48e82b0027eb4a5cf35bed5ff3c6f55b00f19cde2fc0e4) = [SENSOR\_TRIG\_PRIV\_START](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921),

72};

73

[ 74](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684b)enum [sensor\_attribute\_grow\_r502a](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684b) {

[ 78](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684baa499ad10253a3f3e1ad571c3a149dadd) [SENSOR\_ATTR\_R502A\_CAPTURE](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684baa499ad10253a3f3e1ad571c3a149dadd) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

[ 83](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba773495d23834e9fd2eb9ee02909be965) [SENSOR\_ATTR\_R502A\_TEMPLATE\_CREATE](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba773495d23834e9fd2eb9ee02909be965),

[ 90](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba21f7eeb2a0f277f65eb36c389fbb28eb) [SENSOR\_ATTR\_R502A\_RECORD\_ADD](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba21f7eeb2a0f277f65eb36c389fbb28eb),

[ 96](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684baea17f5a55989ccfbbc946ec0283a2922) [SENSOR\_ATTR\_R502A\_RECORD\_FIND](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684baea17f5a55989ccfbbc946ec0283a2922),

[ 102](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba316c52d77ed8be366c5a2736d93da1ef) [SENSOR\_ATTR\_R502A\_RECORD\_DEL](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba316c52d77ed8be366c5a2736d93da1ef),

[ 104](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684bac485d08e7a02d6c21fd428b9d846e9df) [SENSOR\_ATTR\_R502A\_RECORD\_FREE\_IDX](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684bac485d08e7a02d6c21fd428b9d846e9df),

[ 106](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684bad40eb32ad584064c261e666712f97e7b) [SENSOR\_ATTR\_R502A\_RECORD\_EMPTY](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684bad40eb32ad584064c261e666712f97e7b),

[ 112](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba2edb55a7c3ece4a382d19a951f5cbe13) [SENSOR\_ATTR\_R502A\_RECORD\_LOAD](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba2edb55a7c3ece4a382d19a951f5cbe13),

[ 121](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba7258864588bd700f50f9572d5532c689) [SENSOR\_ATTR\_R502A\_COMPARE](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba7258864588bd700f50f9572d5532c689),

[ 130](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba8e7d9545ee722f94e33af5335b52f3e0) [SENSOR\_ATTR\_R502A\_SYS\_PARAM](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba8e7d9545ee722f94e33af5335b52f3e0),

131};

132

[ 133](grow__r502a_8h.md#a3dbc5cd5f5295741e99735ec0279b48d)int [r502a\_read\_sys\_param](grow__r502a_8h.md#a3dbc5cd5f5295741e99735ec0279b48d)(const struct [device](structdevice.md) \*dev, struct [r502a\_sys\_param](structr502a__sys__param.md) \*val);

[ 134](grow__r502a_8h.md#ad16b787e54f20627c4bf15b1732c05ae)int [fps\_upload\_char\_buf](grow__r502a_8h.md#ad16b787e54f20627c4bf15b1732c05ae)(const struct [device](structdevice.md) \*dev, struct [r502a\_template](structr502a__template.md) \*temp);

[ 135](grow__r502a_8h.md#a3b6f1ea1024c0d855a7bbf05f79c19c8)int [fps\_download\_char\_buf](grow__r502a_8h.md#a3b6f1ea1024c0d855a7bbf05f79c19c8)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) char\_buf\_id,

136 const struct [r502a\_template](structr502a__template.md) \*temp);

137

138#ifdef \_\_cplusplus

139}

140#endif

141

142#endif /\* ZEPHYR\_INCLUDE\_ZEPHYR\_DRIVERS\_SENSOR\_GROW\_R502A\_H\_ \*/

[SENSOR\_TRIG\_PRIV\_START](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921)

@ SENSOR\_TRIG\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:284

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:368

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:217

[r502a\_sys\_param\_set](grow__r502a_8h.md#a16242f27a53b430ea3cf165fbc7ce70b)

r502a\_sys\_param\_set

**Definition** grow\_r502a.h:44

[R502A\_SECURITY\_LEVEL](grow__r502a_8h.md#a16242f27a53b430ea3cf165fbc7ce70ba2795f5eb1ee8feeba7f57d0bdc4ec519)

@ R502A\_SECURITY\_LEVEL

**Definition** grow\_r502a.h:46

[R502A\_DATA\_PKG\_LEN](grow__r502a_8h.md#a16242f27a53b430ea3cf165fbc7ce70baa356f4aea69d118b8283d347b816bca1)

@ R502A\_DATA\_PKG\_LEN

**Definition** grow\_r502a.h:47

[R502A\_BAUD\_RATE](grow__r502a_8h.md#a16242f27a53b430ea3cf165fbc7ce70bacef6f845b078fffb0f5f10a93cba3721)

@ R502A\_BAUD\_RATE

**Definition** grow\_r502a.h:45

[r502a\_data\_len](grow__r502a_8h.md#a3298eb4d591ba56131bae8137888dcd8)

r502a\_data\_len

**Definition** grow\_r502a.h:37

[R502A\_PKG\_LEN\_256](grow__r502a_8h.md#a3298eb4d591ba56131bae8137888dcd8a4fa6ae11c8e8f44101a729c4149a1101)

@ R502A\_PKG\_LEN\_256

**Definition** grow\_r502a.h:41

[R502A\_PKG\_LEN\_64](grow__r502a_8h.md#a3298eb4d591ba56131bae8137888dcd8a61ab7cac6d6613f3465157f1ee09b2ee)

@ R502A\_PKG\_LEN\_64

**Definition** grow\_r502a.h:39

[R502A\_PKG\_LEN\_32](grow__r502a_8h.md#a3298eb4d591ba56131bae8137888dcd8a6be1d185636994b69006b14188d003cf)

@ R502A\_PKG\_LEN\_32

**Definition** grow\_r502a.h:38

[R502A\_PKG\_LEN\_128](grow__r502a_8h.md#a3298eb4d591ba56131bae8137888dcd8ad5a47c82dd3733cad5a2da69f33735fe)

@ R502A\_PKG\_LEN\_128

**Definition** grow\_r502a.h:40

[fps\_download\_char\_buf](grow__r502a_8h.md#a3b6f1ea1024c0d855a7bbf05f79c19c8)

int fps\_download\_char\_buf(const struct device \*dev, uint8\_t char\_buf\_id, const struct r502a\_template \*temp)

[r502a\_read\_sys\_param](grow__r502a_8h.md#a3dbc5cd5f5295741e99735ec0279b48d)

int r502a\_read\_sys\_param(const struct device \*dev, struct r502a\_sys\_param \*val)

[r502a\_sec\_level](grow__r502a_8h.md#a48154de53541aced1e78537f10f2f3d1)

r502a\_sec\_level

**Definition** grow\_r502a.h:29

[R502A\_SEC\_LEVEL\_4](grow__r502a_8h.md#a48154de53541aced1e78537f10f2f3d1a1e579d5283fb984a555f918828b3e1e9)

@ R502A\_SEC\_LEVEL\_4

**Definition** grow\_r502a.h:33

[R502A\_SEC\_LEVEL\_1](grow__r502a_8h.md#a48154de53541aced1e78537f10f2f3d1a2220c963d396a7d6604ff0b47e3b6db7)

@ R502A\_SEC\_LEVEL\_1

**Definition** grow\_r502a.h:30

[R502A\_SEC\_LEVEL\_2](grow__r502a_8h.md#a48154de53541aced1e78537f10f2f3d1a9fbe3bed318932b9fab282aee7e823ef)

@ R502A\_SEC\_LEVEL\_2

**Definition** grow\_r502a.h:31

[R502A\_SEC\_LEVEL\_5](grow__r502a_8h.md#a48154de53541aced1e78537f10f2f3d1abcb8f9a6447757b0fcb8ef4f63979dc1)

@ R502A\_SEC\_LEVEL\_5

**Definition** grow\_r502a.h:34

[R502A\_SEC\_LEVEL\_3](grow__r502a_8h.md#a48154de53541aced1e78537f10f2f3d1adb0e8b2e0242be58c32cf1fb8c3c00fa)

@ R502A\_SEC\_LEVEL\_3

**Definition** grow\_r502a.h:32

[sensor\_attribute\_grow\_r502a](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684b)

sensor\_attribute\_grow\_r502a

**Definition** grow\_r502a.h:74

[SENSOR\_ATTR\_R502A\_RECORD\_ADD](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba21f7eeb2a0f277f65eb36c389fbb28eb)

@ SENSOR\_ATTR\_R502A\_RECORD\_ADD

Add template to the sensor record storage.

**Definition** grow\_r502a.h:90

[SENSOR\_ATTR\_R502A\_RECORD\_LOAD](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba2edb55a7c3ece4a382d19a951f5cbe13)

@ SENSOR\_ATTR\_R502A\_RECORD\_LOAD

To load template from storage to RAM buffer of sensor.

**Definition** grow\_r502a.h:112

[SENSOR\_ATTR\_R502A\_RECORD\_DEL](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba316c52d77ed8be366c5a2736d93da1ef)

@ SENSOR\_ATTR\_R502A\_RECORD\_DEL

To delete mentioned data from record storage.

**Definition** grow\_r502a.h:102

[SENSOR\_ATTR\_R502A\_COMPARE](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba7258864588bd700f50f9572d5532c689)

@ SENSOR\_ATTR\_R502A\_COMPARE

To template data stored in sensor's RAM buffer.

**Definition** grow\_r502a.h:121

[SENSOR\_ATTR\_R502A\_TEMPLATE\_CREATE](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba773495d23834e9fd2eb9ee02909be965)

@ SENSOR\_ATTR\_R502A\_TEMPLATE\_CREATE

create template from feature files at RAM buffers char\_buf\_1 & char\_buf\_2 and store a template data b...

**Definition** grow\_r502a.h:83

[SENSOR\_ATTR\_R502A\_SYS\_PARAM](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684ba8e7d9545ee722f94e33af5335b52f3e0)

@ SENSOR\_ATTR\_R502A\_SYS\_PARAM

To read and write device's system parameters.

**Definition** grow\_r502a.h:130

[SENSOR\_ATTR\_R502A\_CAPTURE](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684baa499ad10253a3f3e1ad571c3a149dadd)

@ SENSOR\_ATTR\_R502A\_CAPTURE

To capture finger and store as feature file in RAM buffers char\_buf\_1 and char\_buf\_2.

**Definition** grow\_r502a.h:78

[SENSOR\_ATTR\_R502A\_RECORD\_FREE\_IDX](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684bac485d08e7a02d6c21fd428b9d846e9df)

@ SENSOR\_ATTR\_R502A\_RECORD\_FREE\_IDX

To get available position to store data on record storage.

**Definition** grow\_r502a.h:104

[SENSOR\_ATTR\_R502A\_RECORD\_EMPTY](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684bad40eb32ad584064c261e666712f97e7b)

@ SENSOR\_ATTR\_R502A\_RECORD\_EMPTY

To empty the storage record.

**Definition** grow\_r502a.h:106

[SENSOR\_ATTR\_R502A\_RECORD\_FIND](grow__r502a_8h.md#a638da7a83d9339b17e5d9c8ce92b684baea17f5a55989ccfbbc946ec0283a2922)

@ SENSOR\_ATTR\_R502A\_RECORD\_FIND

To find requested data in record storage.

**Definition** grow\_r502a.h:96

[sensor\_trigger\_type\_grow\_r502a](grow__r502a_8h.md#a721dcba985d9010bb1f48e82b0027eb4)

sensor\_trigger\_type\_grow\_r502a

**Definition** grow\_r502a.h:69

[SENSOR\_TRIG\_TOUCH](grow__r502a_8h.md#a721dcba985d9010bb1f48e82b0027eb4a5cf35bed5ff3c6f55b00f19cde2fc0e4)

@ SENSOR\_TRIG\_TOUCH

Trigger fires when a touch is detected.

**Definition** grow\_r502a.h:71

[r502a\_led\_color\_idx](grow__r502a_8h.md#a843fa88a16ab6b47c4e517ddbc01b4a8)

r502a\_led\_color\_idx

**Definition** grow\_r502a.h:17

[R502A\_LED\_COLOR\_BLUE](grow__r502a_8h.md#a843fa88a16ab6b47c4e517ddbc01b4a8a0685eb3e0e4de6faa0577fb5f7d0f845)

@ R502A\_LED\_COLOR\_BLUE

**Definition** grow\_r502a.h:19

[R502A\_LED\_COLOR\_RED](grow__r502a_8h.md#a843fa88a16ab6b47c4e517ddbc01b4a8a667a844dde544590ab7b6e3defd4016c)

@ R502A\_LED\_COLOR\_RED

**Definition** grow\_r502a.h:18

[R502A\_LED\_COLOR\_PURPLE](grow__r502a_8h.md#a843fa88a16ab6b47c4e517ddbc01b4a8ad477284ea70fb76c43a386ed3537be6c)

@ R502A\_LED\_COLOR\_PURPLE

**Definition** grow\_r502a.h:20

[sensor\_channel\_grow\_r502a](grow__r502a_8h.md#a8ff24814059dda20e6b36fe8cc0be30c)

sensor\_channel\_grow\_r502a

**Definition** grow\_r502a.h:64

[SENSOR\_CHAN\_FINGERPRINT](grow__r502a_8h.md#a8ff24814059dda20e6b36fe8cc0be30ca51abf7335f93117c01052a641a5f5cf2)

@ SENSOR\_CHAN\_FINGERPRINT

Fingerprint template count, ID number for enrolling and searching.

**Definition** grow\_r502a.h:66

[fps\_upload\_char\_buf](grow__r502a_8h.md#ad16b787e54f20627c4bf15b1732c05ae)

int fps\_upload\_char\_buf(const struct device \*dev, struct r502a\_template \*temp)

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

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

[r502a\_sys\_param](structr502a__sys__param.md)

**Definition** grow\_r502a.h:50

[r502a\_sys\_param::sec\_level](structr502a__sys__param.md#a076a36d66a6908eee2131a8f652fefa4)

uint16\_t sec\_level

**Definition** grow\_r502a.h:54

[r502a\_sys\_param::lib\_size](structr502a__sys__param.md#a4cc85b5b8ec7a511f9fc5dd3912c0a39)

uint16\_t lib\_size

**Definition** grow\_r502a.h:53

[r502a\_sys\_param::data\_pkt\_size](structr502a__sys__param.md#a8c3470762665d940a3ec2dc214150bf8)

uint16\_t data\_pkt\_size

**Definition** grow\_r502a.h:56

[r502a\_sys\_param::system\_id](structr502a__sys__param.md#aaa11e04312322afa3f406f872763d8be)

uint16\_t system\_id

**Definition** grow\_r502a.h:52

[r502a\_sys\_param::addr](structr502a__sys__param.md#ac3f2dc2456a29eeda55417ba91a29f62)

uint32\_t addr

**Definition** grow\_r502a.h:55

[r502a\_sys\_param::status\_reg](structr502a__sys__param.md#adb966712020f826ecc646c04a93edd5f)

uint16\_t status\_reg

**Definition** grow\_r502a.h:51

[r502a\_sys\_param::baud](structr502a__sys__param.md#adf5a91c5972af06d1bf9beb6a9040bac)

uint32\_t baud

**Definition** grow\_r502a.h:57

[r502a\_template](structr502a__template.md)

**Definition** grow\_r502a.h:60

[r502a\_template::len](structr502a__template.md#a2d4ab0b0ea4e4cf8b061705910639ae4)

size\_t len

**Definition** grow\_r502a.h:62

[r502a\_template::data](structr502a__template.md#aca6dc417fc7e1de22da94e4d4e2b96a9)

uint8\_t \* data

**Definition** grow\_r502a.h:61

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [grow\_r502a.h](grow__r502a_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
