---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/nrf__comp_8h_source.html
original_path: doxygen/html/nrf__comp_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nrf\_comp.h

[Go to the documentation of this file.](nrf__comp_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_COMP\_NRF\_COMP\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_COMP\_NRF\_COMP\_H\_

9

10#include <[zephyr/drivers/comparator.h](comparator_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 17](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bd)enum [comp\_nrf\_comp\_psel](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bd) {

[ 19](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda2b1c2decdb25c675f1e393fa8b43977e) [COMP\_NRF\_COMP\_PSEL\_AIN0](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda2b1c2decdb25c675f1e393fa8b43977e),

[ 21](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bdac37f4b34cae292cf99a3f93b80d407d6) [COMP\_NRF\_COMP\_PSEL\_AIN1](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bdac37f4b34cae292cf99a3f93b80d407d6),

[ 23](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda5e37908bf483008126c34d25edbc137b) [COMP\_NRF\_COMP\_PSEL\_AIN2](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda5e37908bf483008126c34d25edbc137b),

[ 25](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda6a9e897dbcb2f651c454d22b9ca790e7) [COMP\_NRF\_COMP\_PSEL\_AIN3](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda6a9e897dbcb2f651c454d22b9ca790e7),

[ 27](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bdac2a45cbf6105c6f66873193db6587ea1) [COMP\_NRF\_COMP\_PSEL\_AIN4](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bdac2a45cbf6105c6f66873193db6587ea1),

[ 29](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda1432d8a42cbed9bc2db034a2a17f884a) [COMP\_NRF\_COMP\_PSEL\_AIN5](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda1432d8a42cbed9bc2db034a2a17f884a),

[ 31](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda671739cd4df3ce2ed598b32e025f4f21) [COMP\_NRF\_COMP\_PSEL\_AIN6](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda671739cd4df3ce2ed598b32e025f4f21),

[ 33](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda0c790a921c22f4c62fe57bf9ac451d18) [COMP\_NRF\_COMP\_PSEL\_AIN7](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda0c790a921c22f4c62fe57bf9ac451d18),

[ 35](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda8c21dbfce40ed06ceb4504dc027301c4) [COMP\_NRF\_COMP\_PSEL\_VDD\_DIV2](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda8c21dbfce40ed06ceb4504dc027301c4),

[ 37](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda54b4306c4934add27acdc58d408b8ccc) [COMP\_NRF\_COMP\_PSEL\_VDDH\_DIV5](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda54b4306c4934add27acdc58d408b8ccc),

38};

39

[ 41](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270)enum [comp\_nrf\_comp\_extrefsel](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270) {

[ 43](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270af4f8c27fcace2bb5d835a2abd08b9185) [COMP\_NRF\_COMP\_EXTREFSEL\_AIN0](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270af4f8c27fcace2bb5d835a2abd08b9185),

[ 45](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270aa583f7d396f0f7ad248991499990a4ed) [COMP\_NRF\_COMP\_EXTREFSEL\_AIN1](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270aa583f7d396f0f7ad248991499990a4ed),

[ 47](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270ac6308f6e909ee744f9506ed560768459) [COMP\_NRF\_COMP\_EXTREFSEL\_AIN2](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270ac6308f6e909ee744f9506ed560768459),

[ 49](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270a2c213b044a0446bb545b37f5e21a58e1) [COMP\_NRF\_COMP\_EXTREFSEL\_AIN3](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270a2c213b044a0446bb545b37f5e21a58e1),

[ 51](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270afc90e5b29390f758a14cdfdc656d0de1) [COMP\_NRF\_COMP\_EXTREFSEL\_AIN4](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270afc90e5b29390f758a14cdfdc656d0de1),

[ 53](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270a547593f189f1a0a393b5ad85f3468743) [COMP\_NRF\_COMP\_EXTREFSEL\_AIN5](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270a547593f189f1a0a393b5ad85f3468743),

[ 55](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270a7e7af9bf1f3ddffa54263ddb42d0cae5) [COMP\_NRF\_COMP\_EXTREFSEL\_AIN6](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270a7e7af9bf1f3ddffa54263ddb42d0cae5),

[ 57](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270a215961c3f17346248d64ce9b2fccadba) [COMP\_NRF\_COMP\_EXTREFSEL\_AIN7](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270a215961c3f17346248d64ce9b2fccadba),

58};

59

[ 61](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553)enum [comp\_nrf\_comp\_refsel](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553) {

[ 63](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553abfa40254064295fec8c5882402f7f0d2) [COMP\_NRF\_COMP\_REFSEL\_INT\_1V2](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553abfa40254064295fec8c5882402f7f0d2),

[ 65](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553abf7088360f68099140b06de7d3f4b4e7) [COMP\_NRF\_COMP\_REFSEL\_INT\_1V8](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553abf7088360f68099140b06de7d3f4b4e7),

[ 67](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553a3670bac3f83f144ca1373a4ea6c0107c) [COMP\_NRF\_COMP\_REFSEL\_INT\_2V4](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553a3670bac3f83f144ca1373a4ea6c0107c),

[ 69](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553a87eba8036aea56146b734ee47a9cd6ca) [COMP\_NRF\_COMP\_REFSEL\_AVDDAO1V8](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553a87eba8036aea56146b734ee47a9cd6ca),

[ 71](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553a0e8f3057261749e3a15333d42e49512f) [COMP\_NRF\_COMP\_REFSEL\_VDD](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553a0e8f3057261749e3a15333d42e49512f),

[ 73](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553ab0ae8de9e72cf723645691166e9fbb2e) [COMP\_NRF\_COMP\_REFSEL\_AREF](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553ab0ae8de9e72cf723645691166e9fbb2e),

74};

75

[ 77](nrf__comp_8h.md#ad13baf7c262d5fb2321ea5140180b3b1)enum [comp\_nrf\_comp\_sp\_mode](nrf__comp_8h.md#ad13baf7c262d5fb2321ea5140180b3b1) {

[ 79](nrf__comp_8h.md#ad13baf7c262d5fb2321ea5140180b3b1a108433aa9b89eeca9a706e67d5eb8826) [COMP\_NRF\_COMP\_SP\_MODE\_LOW](nrf__comp_8h.md#ad13baf7c262d5fb2321ea5140180b3b1a108433aa9b89eeca9a706e67d5eb8826),

[ 81](nrf__comp_8h.md#ad13baf7c262d5fb2321ea5140180b3b1a1fb59dd0aa818e279c5e4d15b620fac5) [COMP\_NRF\_COMP\_SP\_MODE\_NORMAL](nrf__comp_8h.md#ad13baf7c262d5fb2321ea5140180b3b1a1fb59dd0aa818e279c5e4d15b620fac5),

[ 83](nrf__comp_8h.md#ad13baf7c262d5fb2321ea5140180b3b1aeb3aad272a4b6cd1269180306357bd98) [COMP\_NRF\_COMP\_SP\_MODE\_HIGH](nrf__comp_8h.md#ad13baf7c262d5fb2321ea5140180b3b1aeb3aad272a4b6cd1269180306357bd98),

84};

85

[ 87](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010)enum [comp\_nrf\_comp\_isource](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010) {

[ 89](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010a3d47ebd769b9d4b9668d7c6502294043) [COMP\_NRF\_COMP\_ISOURCE\_DISABLED](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010a3d47ebd769b9d4b9668d7c6502294043),

[ 91](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010ab413c10f12cbfb5b2e550f8fa07992c2) [COMP\_NRF\_COMP\_ISOURCE\_2UA5](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010ab413c10f12cbfb5b2e550f8fa07992c2),

[ 93](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010a1890799d7f32b44f1a870ed67a8707a0) [COMP\_NRF\_COMP\_ISOURCE\_5UA](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010a1890799d7f32b44f1a870ed67a8707a0),

[ 95](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010a16df414be65b65763e5938bc37bb392f) [COMP\_NRF\_COMP\_ISOURCE\_10UA](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010a16df414be65b65763e5938bc37bb392f),

96};

97

[ 105](structcomp__nrf__comp__se__config.md)struct [comp\_nrf\_comp\_se\_config](structcomp__nrf__comp__se__config.md) {

[ 107](structcomp__nrf__comp__se__config.md#ab8508ca57b1a7e3b4c129a6f16a26342) enum [comp\_nrf\_comp\_psel](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bd) [psel](structcomp__nrf__comp__se__config.md#ab8508ca57b1a7e3b4c129a6f16a26342);

[ 109](structcomp__nrf__comp__se__config.md#a484cc2b4c38c7b5a8c05e87e560c7b5e) enum [comp\_nrf\_comp\_sp\_mode](nrf__comp_8h.md#ad13baf7c262d5fb2321ea5140180b3b1) [sp\_mode](structcomp__nrf__comp__se__config.md#a484cc2b4c38c7b5a8c05e87e560c7b5e);

[ 111](structcomp__nrf__comp__se__config.md#a3ffb95afd621727dedbc617e3072cfd9) enum [comp\_nrf\_comp\_isource](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010) [isource](structcomp__nrf__comp__se__config.md#a3ffb95afd621727dedbc617e3072cfd9);

[ 113](structcomp__nrf__comp__se__config.md#a48c793942f10f04ec6fa8ea54ae9f8ac) enum [comp\_nrf\_comp\_extrefsel](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270) [extrefsel](structcomp__nrf__comp__se__config.md#a48c793942f10f04ec6fa8ea54ae9f8ac);

[ 115](structcomp__nrf__comp__se__config.md#a3a7c4e624cb7e34624732dbe4b5ab4f8) enum [comp\_nrf\_comp\_refsel](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553) [refsel](structcomp__nrf__comp__se__config.md#a3a7c4e624cb7e34624732dbe4b5ab4f8);

[ 117](structcomp__nrf__comp__se__config.md#ad4c0e1711565c3bd05c08a6eaf593aad) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [th\_down](structcomp__nrf__comp__se__config.md#ad4c0e1711565c3bd05c08a6eaf593aad);

[ 119](structcomp__nrf__comp__se__config.md#a72dcaac8a0508b8859397b7926238112) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [th\_up](structcomp__nrf__comp__se__config.md#a72dcaac8a0508b8859397b7926238112);

120};

121

[ 131](nrf__comp_8h.md#aca8ca4ea25fbfbe962f754ef79bcb356)int [comp\_nrf\_comp\_configure\_se](nrf__comp_8h.md#aca8ca4ea25fbfbe962f754ef79bcb356)(const struct [device](structdevice.md) \*dev,

132 const struct [comp\_nrf\_comp\_se\_config](structcomp__nrf__comp__se__config.md) \*config);

133

[ 135](structcomp__nrf__comp__diff__config.md)struct [comp\_nrf\_comp\_diff\_config](structcomp__nrf__comp__diff__config.md) {

[ 137](structcomp__nrf__comp__diff__config.md#ae3807c40d36de257f2bae07787cc6cd7) enum [comp\_nrf\_comp\_psel](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bd) [psel](structcomp__nrf__comp__diff__config.md#ae3807c40d36de257f2bae07787cc6cd7);

[ 139](structcomp__nrf__comp__diff__config.md#a9a9b95f993a1a193292eb940c0550e1f) enum [comp\_nrf\_comp\_sp\_mode](nrf__comp_8h.md#ad13baf7c262d5fb2321ea5140180b3b1) [sp\_mode](structcomp__nrf__comp__diff__config.md#a9a9b95f993a1a193292eb940c0550e1f);

[ 141](structcomp__nrf__comp__diff__config.md#ac1aada8c9bceab130cd6ffdf294ce52f) enum [comp\_nrf\_comp\_isource](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010) [isource](structcomp__nrf__comp__diff__config.md#ac1aada8c9bceab130cd6ffdf294ce52f);

[ 143](structcomp__nrf__comp__diff__config.md#a9ea88f6afb084054ad8579d32b2ed947) enum [comp\_nrf\_comp\_extrefsel](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270) [extrefsel](structcomp__nrf__comp__diff__config.md#a9ea88f6afb084054ad8579d32b2ed947);

[ 145](structcomp__nrf__comp__diff__config.md#ae597d46f83c77923541e73cf254bc4ee) bool [enable\_hyst](structcomp__nrf__comp__diff__config.md#ae597d46f83c77923541e73cf254bc4ee);

146};

147

[ 157](nrf__comp_8h.md#a63ca5bf56504df5c9d0904609c433e11)int [comp\_nrf\_comp\_configure\_diff](nrf__comp_8h.md#a63ca5bf56504df5c9d0904609c433e11)(const struct [device](structdevice.md) \*dev,

158 const struct [comp\_nrf\_comp\_diff\_config](structcomp__nrf__comp__diff__config.md) \*config);

159

160#ifdef \_\_cplusplus

161}

162#endif

163

164#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_COMP\_NRF\_COMP\_H\_ \*/

[comparator.h](comparator_8h.md)

[comp\_nrf\_comp\_extrefsel](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270)

comp\_nrf\_comp\_extrefsel

External reference selection.

**Definition** nrf\_comp.h:41

[COMP\_NRF\_COMP\_EXTREFSEL\_AIN7](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270a215961c3f17346248d64ce9b2fccadba)

@ COMP\_NRF\_COMP\_EXTREFSEL\_AIN7

AIN7 external input.

**Definition** nrf\_comp.h:57

[COMP\_NRF\_COMP\_EXTREFSEL\_AIN3](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270a2c213b044a0446bb545b37f5e21a58e1)

@ COMP\_NRF\_COMP\_EXTREFSEL\_AIN3

AIN3 external input.

**Definition** nrf\_comp.h:49

[COMP\_NRF\_COMP\_EXTREFSEL\_AIN5](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270a547593f189f1a0a393b5ad85f3468743)

@ COMP\_NRF\_COMP\_EXTREFSEL\_AIN5

AIN5 external input.

**Definition** nrf\_comp.h:53

[COMP\_NRF\_COMP\_EXTREFSEL\_AIN6](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270a7e7af9bf1f3ddffa54263ddb42d0cae5)

@ COMP\_NRF\_COMP\_EXTREFSEL\_AIN6

AIN6 external input.

**Definition** nrf\_comp.h:55

[COMP\_NRF\_COMP\_EXTREFSEL\_AIN1](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270aa583f7d396f0f7ad248991499990a4ed)

@ COMP\_NRF\_COMP\_EXTREFSEL\_AIN1

AIN1 external input.

**Definition** nrf\_comp.h:45

[COMP\_NRF\_COMP\_EXTREFSEL\_AIN2](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270ac6308f6e909ee744f9506ed560768459)

@ COMP\_NRF\_COMP\_EXTREFSEL\_AIN2

AIN2 external input.

**Definition** nrf\_comp.h:47

[COMP\_NRF\_COMP\_EXTREFSEL\_AIN0](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270af4f8c27fcace2bb5d835a2abd08b9185)

@ COMP\_NRF\_COMP\_EXTREFSEL\_AIN0

AIN0 external input.

**Definition** nrf\_comp.h:43

[COMP\_NRF\_COMP\_EXTREFSEL\_AIN4](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270afc90e5b29390f758a14cdfdc656d0de1)

@ COMP\_NRF\_COMP\_EXTREFSEL\_AIN4

AIN4 external input.

**Definition** nrf\_comp.h:51

[comp\_nrf\_comp\_configure\_diff](nrf__comp_8h.md#a63ca5bf56504df5c9d0904609c433e11)

int comp\_nrf\_comp\_configure\_diff(const struct device \*dev, const struct comp\_nrf\_comp\_diff\_config \*config)

Configure comparator in differential mode.

[comp\_nrf\_comp\_refsel](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553)

comp\_nrf\_comp\_refsel

Reference selection.

**Definition** nrf\_comp.h:61

[COMP\_NRF\_COMP\_REFSEL\_VDD](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553a0e8f3057261749e3a15333d42e49512f)

@ COMP\_NRF\_COMP\_REFSEL\_VDD

VDD reference.

**Definition** nrf\_comp.h:71

[COMP\_NRF\_COMP\_REFSEL\_INT\_2V4](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553a3670bac3f83f144ca1373a4ea6c0107c)

@ COMP\_NRF\_COMP\_REFSEL\_INT\_2V4

Internal 2.4V reference.

**Definition** nrf\_comp.h:67

[COMP\_NRF\_COMP\_REFSEL\_AVDDAO1V8](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553a87eba8036aea56146b734ee47a9cd6ca)

@ COMP\_NRF\_COMP\_REFSEL\_AVDDAO1V8

AVDD 1.8V reference.

**Definition** nrf\_comp.h:69

[COMP\_NRF\_COMP\_REFSEL\_AREF](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553ab0ae8de9e72cf723645691166e9fbb2e)

@ COMP\_NRF\_COMP\_REFSEL\_AREF

Use external analog reference.

**Definition** nrf\_comp.h:73

[COMP\_NRF\_COMP\_REFSEL\_INT\_1V8](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553abf7088360f68099140b06de7d3f4b4e7)

@ COMP\_NRF\_COMP\_REFSEL\_INT\_1V8

Internal 1.8V reference.

**Definition** nrf\_comp.h:65

[COMP\_NRF\_COMP\_REFSEL\_INT\_1V2](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553abfa40254064295fec8c5882402f7f0d2)

@ COMP\_NRF\_COMP\_REFSEL\_INT\_1V2

Internal 1.2V reference.

**Definition** nrf\_comp.h:63

[comp\_nrf\_comp\_isource](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010)

comp\_nrf\_comp\_isource

Current source configuration.

**Definition** nrf\_comp.h:87

[COMP\_NRF\_COMP\_ISOURCE\_10UA](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010a16df414be65b65763e5938bc37bb392f)

@ COMP\_NRF\_COMP\_ISOURCE\_10UA

10uA current source enabled

**Definition** nrf\_comp.h:95

[COMP\_NRF\_COMP\_ISOURCE\_5UA](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010a1890799d7f32b44f1a870ed67a8707a0)

@ COMP\_NRF\_COMP\_ISOURCE\_5UA

5uA current source enabled

**Definition** nrf\_comp.h:93

[COMP\_NRF\_COMP\_ISOURCE\_DISABLED](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010a3d47ebd769b9d4b9668d7c6502294043)

@ COMP\_NRF\_COMP\_ISOURCE\_DISABLED

Current source disabled.

**Definition** nrf\_comp.h:89

[COMP\_NRF\_COMP\_ISOURCE\_2UA5](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010ab413c10f12cbfb5b2e550f8fa07992c2)

@ COMP\_NRF\_COMP\_ISOURCE\_2UA5

2.5uA current source enabled

**Definition** nrf\_comp.h:91

[comp\_nrf\_comp\_psel](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bd)

comp\_nrf\_comp\_psel

Positive input selection.

**Definition** nrf\_comp.h:17

[COMP\_NRF\_COMP\_PSEL\_AIN7](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda0c790a921c22f4c62fe57bf9ac451d18)

@ COMP\_NRF\_COMP\_PSEL\_AIN7

AIN7 external input.

**Definition** nrf\_comp.h:33

[COMP\_NRF\_COMP\_PSEL\_AIN5](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda1432d8a42cbed9bc2db034a2a17f884a)

@ COMP\_NRF\_COMP\_PSEL\_AIN5

AIN5 external input.

**Definition** nrf\_comp.h:29

[COMP\_NRF\_COMP\_PSEL\_AIN0](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda2b1c2decdb25c675f1e393fa8b43977e)

@ COMP\_NRF\_COMP\_PSEL\_AIN0

AIN0 external input.

**Definition** nrf\_comp.h:19

[COMP\_NRF\_COMP\_PSEL\_VDDH\_DIV5](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda54b4306c4934add27acdc58d408b8ccc)

@ COMP\_NRF\_COMP\_PSEL\_VDDH\_DIV5

VDDH / 5.

**Definition** nrf\_comp.h:37

[COMP\_NRF\_COMP\_PSEL\_AIN2](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda5e37908bf483008126c34d25edbc137b)

@ COMP\_NRF\_COMP\_PSEL\_AIN2

AIN2 external input.

**Definition** nrf\_comp.h:23

[COMP\_NRF\_COMP\_PSEL\_AIN6](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda671739cd4df3ce2ed598b32e025f4f21)

@ COMP\_NRF\_COMP\_PSEL\_AIN6

AIN6 external input.

**Definition** nrf\_comp.h:31

[COMP\_NRF\_COMP\_PSEL\_AIN3](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda6a9e897dbcb2f651c454d22b9ca790e7)

@ COMP\_NRF\_COMP\_PSEL\_AIN3

AIN3 external input.

**Definition** nrf\_comp.h:25

[COMP\_NRF\_COMP\_PSEL\_VDD\_DIV2](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bda8c21dbfce40ed06ceb4504dc027301c4)

@ COMP\_NRF\_COMP\_PSEL\_VDD\_DIV2

VDD / 2.

**Definition** nrf\_comp.h:35

[COMP\_NRF\_COMP\_PSEL\_AIN4](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bdac2a45cbf6105c6f66873193db6587ea1)

@ COMP\_NRF\_COMP\_PSEL\_AIN4

AIN4 external input.

**Definition** nrf\_comp.h:27

[COMP\_NRF\_COMP\_PSEL\_AIN1](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bdac37f4b34cae292cf99a3f93b80d407d6)

@ COMP\_NRF\_COMP\_PSEL\_AIN1

AIN1 external input.

**Definition** nrf\_comp.h:21

[comp\_nrf\_comp\_configure\_se](nrf__comp_8h.md#aca8ca4ea25fbfbe962f754ef79bcb356)

int comp\_nrf\_comp\_configure\_se(const struct device \*dev, const struct comp\_nrf\_comp\_se\_config \*config)

Configure comparator in single-ended mode.

[comp\_nrf\_comp\_sp\_mode](nrf__comp_8h.md#ad13baf7c262d5fb2321ea5140180b3b1)

comp\_nrf\_comp\_sp\_mode

Speed mode selection.

**Definition** nrf\_comp.h:77

[COMP\_NRF\_COMP\_SP\_MODE\_LOW](nrf__comp_8h.md#ad13baf7c262d5fb2321ea5140180b3b1a108433aa9b89eeca9a706e67d5eb8826)

@ COMP\_NRF\_COMP\_SP\_MODE\_LOW

Low-power mode.

**Definition** nrf\_comp.h:79

[COMP\_NRF\_COMP\_SP\_MODE\_NORMAL](nrf__comp_8h.md#ad13baf7c262d5fb2321ea5140180b3b1a1fb59dd0aa818e279c5e4d15b620fac5)

@ COMP\_NRF\_COMP\_SP\_MODE\_NORMAL

Normal mode.

**Definition** nrf\_comp.h:81

[COMP\_NRF\_COMP\_SP\_MODE\_HIGH](nrf__comp_8h.md#ad13baf7c262d5fb2321ea5140180b3b1aeb3aad272a4b6cd1269180306357bd98)

@ COMP\_NRF\_COMP\_SP\_MODE\_HIGH

High-speed mode.

**Definition** nrf\_comp.h:83

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[comp\_nrf\_comp\_diff\_config](structcomp__nrf__comp__diff__config.md)

Differential mode configuration structure.

**Definition** nrf\_comp.h:135

[comp\_nrf\_comp\_diff\_config::sp\_mode](structcomp__nrf__comp__diff__config.md#a9a9b95f993a1a193292eb940c0550e1f)

enum comp\_nrf\_comp\_sp\_mode sp\_mode

Speed mode selection.

**Definition** nrf\_comp.h:139

[comp\_nrf\_comp\_diff\_config::extrefsel](structcomp__nrf__comp__diff__config.md#a9ea88f6afb084054ad8579d32b2ed947)

enum comp\_nrf\_comp\_extrefsel extrefsel

Negative input selection.

**Definition** nrf\_comp.h:143

[comp\_nrf\_comp\_diff\_config::isource](structcomp__nrf__comp__diff__config.md#ac1aada8c9bceab130cd6ffdf294ce52f)

enum comp\_nrf\_comp\_isource isource

Current source configuration.

**Definition** nrf\_comp.h:141

[comp\_nrf\_comp\_diff\_config::psel](structcomp__nrf__comp__diff__config.md#ae3807c40d36de257f2bae07787cc6cd7)

enum comp\_nrf\_comp\_psel psel

Positive input selection.

**Definition** nrf\_comp.h:137

[comp\_nrf\_comp\_diff\_config::enable\_hyst](structcomp__nrf__comp__diff__config.md#ae597d46f83c77923541e73cf254bc4ee)

bool enable\_hyst

Hysteresis configuration.

**Definition** nrf\_comp.h:145

[comp\_nrf\_comp\_se\_config](structcomp__nrf__comp__se__config.md)

Single-ended mode configuration structure.

**Definition** nrf\_comp.h:105

[comp\_nrf\_comp\_se\_config::refsel](structcomp__nrf__comp__se__config.md#a3a7c4e624cb7e34624732dbe4b5ab4f8)

enum comp\_nrf\_comp\_refsel refsel

Reference selection.

**Definition** nrf\_comp.h:115

[comp\_nrf\_comp\_se\_config::isource](structcomp__nrf__comp__se__config.md#a3ffb95afd621727dedbc617e3072cfd9)

enum comp\_nrf\_comp\_isource isource

Current source configuration.

**Definition** nrf\_comp.h:111

[comp\_nrf\_comp\_se\_config::sp\_mode](structcomp__nrf__comp__se__config.md#a484cc2b4c38c7b5a8c05e87e560c7b5e)

enum comp\_nrf\_comp\_sp\_mode sp\_mode

Speed mode selection.

**Definition** nrf\_comp.h:109

[comp\_nrf\_comp\_se\_config::extrefsel](structcomp__nrf__comp__se__config.md#a48c793942f10f04ec6fa8ea54ae9f8ac)

enum comp\_nrf\_comp\_extrefsel extrefsel

External reference selection.

**Definition** nrf\_comp.h:113

[comp\_nrf\_comp\_se\_config::th\_up](structcomp__nrf__comp__se__config.md#a72dcaac8a0508b8859397b7926238112)

uint8\_t th\_up

Hysteresis up threshold configuration.

**Definition** nrf\_comp.h:119

[comp\_nrf\_comp\_se\_config::psel](structcomp__nrf__comp__se__config.md#ab8508ca57b1a7e3b4c129a6f16a26342)

enum comp\_nrf\_comp\_psel psel

Positive input selection.

**Definition** nrf\_comp.h:107

[comp\_nrf\_comp\_se\_config::th\_down](structcomp__nrf__comp__se__config.md#ad4c0e1711565c3bd05c08a6eaf593aad)

uint8\_t th\_down

Hysteresis down threshold configuration.

**Definition** nrf\_comp.h:117

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [comparator](dir_25be445c737a80f4854b3956f06e1693.md)
- [nrf\_comp.h](nrf__comp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
