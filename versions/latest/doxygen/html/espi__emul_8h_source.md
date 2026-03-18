---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/espi__emul_8h_source.html
original_path: doxygen/html/espi__emul_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

espi\_emul.h

[Go to the documentation of this file.](espi__emul_8h.md)

1/\*

2 \* Copyright 2020 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_ESPI\_SPI\_EMUL\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_ESPI\_SPI\_EMUL\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <[zephyr/drivers/emul.h](emul_8h.md)>

12#include <[zephyr/drivers/espi.h](espi_8h.md)>

13#include <[zephyr/sys/slist.h](slist_8h.md)>

14#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

15

21

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 33](group__espi__emul__interface.md#ga18fb55455f95a7f7ba93fdc49de2b9c0)#define EMUL\_ESPI\_HOST\_CHIPSEL 0

34

35struct [espi\_emul](structespi__emul.md);

36

[ 48](group__espi__emul__interface.md#gab1068f48bf931fbc86668fb9108e07c7)typedef int (\*[emul\_espi\_api\_set\_vw](group__espi__emul__interface.md#gab1068f48bf931fbc86668fb9108e07c7))(const struct [emul](structemul.md) \*target, enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) vw,

49 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level);

50

[ 62](group__espi__emul__interface.md#ga06c214788ceff221e776394318517f91)typedef int (\*[emul\_espi\_api\_get\_vw](group__espi__emul__interface.md#ga06c214788ceff221e776394318517f91))(const struct [emul](structemul.md) \*target, enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) vw,

63 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*level);

64

65#ifdef CONFIG\_ESPI\_PERIPHERAL\_ACPI\_SHM\_REGION

73typedef [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) (\*emul\_espi\_api\_get\_acpi\_shm)(const struct [emul](structemul.md) \*target);

74#endif

75

87typedef struct [espi\_emul](structespi__emul.md) \*(\*emul\_find\_emul)(const struct [device](structdevice.md) \*dev, unsigned int chipsel);

88

[ 99](group__espi__emul__interface.md#ga2abff7d857738254cc4a8a939264924f)typedef int (\*[emul\_trigger\_event](group__espi__emul__interface.md#ga2abff7d857738254cc4a8a939264924f))(const struct [device](structdevice.md) \*dev, struct [espi\_event](structespi__event.md) \*evt);

100

[ 102](structemul__espi__device__api.md)struct [emul\_espi\_device\_api](structemul__espi__device__api.md) {

[ 103](structemul__espi__device__api.md#a85353662a3279444ed2a78f39b49cc3c) [emul\_espi\_api\_set\_vw](group__espi__emul__interface.md#gab1068f48bf931fbc86668fb9108e07c7) [set\_vw](structemul__espi__device__api.md#a85353662a3279444ed2a78f39b49cc3c);

[ 104](structemul__espi__device__api.md#a9d1ceef7587374ab99853eb1ab0040c4) [emul\_espi\_api\_get\_vw](group__espi__emul__interface.md#ga06c214788ceff221e776394318517f91) [get\_vw](structemul__espi__device__api.md#a9d1ceef7587374ab99853eb1ab0040c4);

105#ifdef CONFIG\_ESPI\_PERIPHERAL\_ACPI\_SHM\_REGION

106 emul\_espi\_api\_get\_acpi\_shm get\_acpi\_shm;

107#endif

108};

109

[ 111](structespi__emul.md)struct [espi\_emul](structespi__emul.md) {

[ 112](structespi__emul.md#a495cddd3fc6300f2c7eb3e98caafecd5) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structespi__emul.md#a495cddd3fc6300f2c7eb3e98caafecd5);

[ 114](structespi__emul.md#a27aa4069611f537b470a9c64d7913c91) const struct [emul](structemul.md) \*[target](structespi__emul.md#a27aa4069611f537b470a9c64d7913c91);

[ 116](structespi__emul.md#a1c80c40cdc25bb5440d57c3aef7379eb) const struct [emul\_espi\_device\_api](structemul__espi__device__api.md) \*[api](structespi__emul.md#a1c80c40cdc25bb5440d57c3aef7379eb);

[ 118](structespi__emul.md#a29554137c4ef3fbf4f7a087d01602adb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [chipsel](structespi__emul.md#a29554137c4ef3fbf4f7a087d01602adb);

119};

120

[ 122](structemul__espi__driver__api.md)struct [emul\_espi\_driver\_api](structemul__espi__driver__api.md) {

123 /\* The struct espi\_driver\_api has to be first in

124 \* struct emul\_espi\_driver\_api to make pointer casting working

125 \*/

[ 126](structemul__espi__driver__api.md#a829c405693c4ef7f558004bc8106342b) struct espi\_driver\_api [espi\_api](structemul__espi__driver__api.md#a829c405693c4ef7f558004bc8106342b);

127 /\* The rest, emulator specific functions \*/

[ 128](structemul__espi__driver__api.md#a77f9c77cbd2c66e0f8871f94deb7c154) [emul\_trigger\_event](group__espi__emul__interface.md#ga2abff7d857738254cc4a8a939264924f) [trigger\_event](structemul__espi__driver__api.md#a77f9c77cbd2c66e0f8871f94deb7c154);

[ 129](structemul__espi__driver__api.md#ac7523c429bc75a99d20a87243b9d1195) [emul\_find\_emul](group__espi__emul__interface.md#gaa9e27e6a744a73a13415e01fa2c09bca) [find\_emul](structemul__espi__driver__api.md#ac7523c429bc75a99d20a87243b9d1195);

130};

131

[ 139](group__espi__emul__interface.md#gaaccb8ef6060c0477151001af52310769)int [espi\_emul\_register](group__espi__emul__interface.md#gaaccb8ef6060c0477151001af52310769)(const struct [device](structdevice.md) \*dev, struct [espi\_emul](structespi__emul.md) \*[emul](structemul.md));

140

[ 152](group__espi__emul__interface.md#ga67deaf77a17682671ec28488ed3113fc)int [emul\_espi\_host\_send\_vw](group__espi__emul__interface.md#ga67deaf77a17682671ec28488ed3113fc)(const struct [device](structdevice.md) \*espi\_dev, enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) vw, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level);

153

[ 164](group__espi__emul__interface.md#ga16c67d1d52f94b7062144e2c2f45d15a)int [emul\_espi\_host\_port80\_write](group__espi__emul__interface.md#ga16c67d1d52f94b7062144e2c2f45d15a)(const struct [device](structdevice.md) \*espi\_dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data);

165

166#ifdef CONFIG\_ESPI\_PERIPHERAL\_ACPI\_SHM\_REGION

174[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) emul\_espi\_host\_get\_acpi\_shm(const struct [device](structdevice.md) \*espi\_dev);

175#endif

176

177#ifdef \_\_cplusplus

178}

179#endif

180

184

185#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_ESPI\_SPI\_EMUL\_H\_ \*/

[device.h](device_8h.md)

[emul.h](emul_8h.md)

[espi.h](espi_8h.md)

Public APIs for eSPI driver.

[emul\_espi\_api\_get\_vw](group__espi__emul__interface.md#ga06c214788ceff221e776394318517f91)

int(\* emul\_espi\_api\_get\_vw)(const struct emul \*target, enum espi\_vwire\_signal vw, uint8\_t \*level)

Passes eSPI virtual wires get request (virtual wire packet) to the emulator.

**Definition** espi\_emul.h:62

[emul\_espi\_host\_port80\_write](group__espi__emul__interface.md#ga16c67d1d52f94b7062144e2c2f45d15a)

int emul\_espi\_host\_port80\_write(const struct device \*espi\_dev, uint32\_t data)

Perform port80 write on the emulated host side, which will trigger a proper event(and callbacks) on t...

[emul\_trigger\_event](group__espi__emul__interface.md#ga2abff7d857738254cc4a8a939264924f)

int(\* emul\_trigger\_event)(const struct device \*dev, struct espi\_event \*evt)

Triggers an event on the emulator of eSPI controller side which causes calling specific callbacks.

**Definition** espi\_emul.h:99

[emul\_espi\_host\_send\_vw](group__espi__emul__interface.md#ga67deaf77a17682671ec28488ed3113fc)

int emul\_espi\_host\_send\_vw(const struct device \*espi\_dev, enum espi\_vwire\_signal vw, uint8\_t level)

Sets the eSPI virtual wire on the host side, which will trigger a proper event(and callbacks) on the ...

[emul\_find\_emul](group__espi__emul__interface.md#gaa9e27e6a744a73a13415e01fa2c09bca)

struct espi\_emul \*(\* emul\_find\_emul)(const struct device \*dev, unsigned int chipsel)

Find an emulator present on a eSPI bus.

**Definition** espi\_emul.h:87

[espi\_emul\_register](group__espi__emul__interface.md#gaaccb8ef6060c0477151001af52310769)

int espi\_emul\_register(const struct device \*dev, struct espi\_emul \*emul)

Register an emulated device on the controller.

[emul\_espi\_api\_set\_vw](group__espi__emul__interface.md#gab1068f48bf931fbc86668fb9108e07c7)

int(\* emul\_espi\_api\_set\_vw)(const struct emul \*target, enum espi\_vwire\_signal vw, uint8\_t level)

Passes eSPI virtual wires set request (virtual wire packet) to the emulator.

**Definition** espi\_emul.h:48

[espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35)

espi\_vwire\_signal

eSPI system platform signals that can be send or receive through virtual wire channel

**Definition** espi.h:199

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[types.h](include_2zephyr_2types_8h.md)

[slist.h](slist_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[emul\_espi\_device\_api](structemul__espi__device__api.md)

Definition of the eSPI device emulator API.

**Definition** espi\_emul.h:102

[emul\_espi\_device\_api::set\_vw](structemul__espi__device__api.md#a85353662a3279444ed2a78f39b49cc3c)

emul\_espi\_api\_set\_vw set\_vw

**Definition** espi\_emul.h:103

[emul\_espi\_device\_api::get\_vw](structemul__espi__device__api.md#a9d1ceef7587374ab99853eb1ab0040c4)

emul\_espi\_api\_get\_vw get\_vw

**Definition** espi\_emul.h:104

[emul\_espi\_driver\_api](structemul__espi__driver__api.md)

Definition of the eSPI controller emulator API.

**Definition** espi\_emul.h:122

[emul\_espi\_driver\_api::trigger\_event](structemul__espi__driver__api.md#a77f9c77cbd2c66e0f8871f94deb7c154)

emul\_trigger\_event trigger\_event

**Definition** espi\_emul.h:128

[emul\_espi\_driver\_api::espi\_api](structemul__espi__driver__api.md#a829c405693c4ef7f558004bc8106342b)

struct espi\_driver\_api espi\_api

**Definition** espi\_emul.h:126

[emul\_espi\_driver\_api::find\_emul](structemul__espi__driver__api.md#ac7523c429bc75a99d20a87243b9d1195)

emul\_find\_emul find\_emul

**Definition** espi\_emul.h:129

[emul](structemul.md)

An emulator instance - represents the target emulated device/peripheral that is interacted with throu...

**Definition** emul.h:78

[espi\_emul](structespi__emul.md)

Node in a linked list of emulators for eSPI devices.

**Definition** espi\_emul.h:111

[espi\_emul::api](structespi__emul.md#a1c80c40cdc25bb5440d57c3aef7379eb)

const struct emul\_espi\_device\_api \* api

API provided for this device.

**Definition** espi\_emul.h:116

[espi\_emul::target](structespi__emul.md#a27aa4069611f537b470a9c64d7913c91)

const struct emul \* target

Target emulator - REQUIRED for all emulated bus nodes of any type.

**Definition** espi\_emul.h:114

[espi\_emul::chipsel](structespi__emul.md#a29554137c4ef3fbf4f7a087d01602adb)

uint16\_t chipsel

eSPI chip-select of the emulated device

**Definition** espi\_emul.h:118

[espi\_emul::node](structespi__emul.md#a495cddd3fc6300f2c7eb3e98caafecd5)

sys\_snode\_t node

**Definition** espi\_emul.h:112

[espi\_event](structespi__event.md)

eSPI event

**Definition** espi.h:323

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [espi\_emul.h](espi__emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
