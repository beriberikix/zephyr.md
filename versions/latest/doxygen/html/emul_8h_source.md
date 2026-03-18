---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/emul_8h_source.html
original_path: doxygen/html/emul_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

emul.h

[Go to the documentation of this file.](emul_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \* Copyright 2020 Google LLC

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_EMUL\_H\_

9#define ZEPHYR\_INCLUDE\_DRIVERS\_EMUL\_H\_

10

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif /\* \_\_cplusplus \*/

21

22struct [emul](structemul.md);

23

24/\* #includes required after forward-declaration of struct emul later defined in this header. \*/

25#include <[zephyr/device.h](device_8h.md)>

26#include <[zephyr/devicetree.h](devicetree_8h.md)>

27#include <[zephyr/drivers/espi\_emul.h](espi__emul_8h.md)>

28#include <[zephyr/drivers/i2c\_emul.h](i2c__emul_8h.md)>

29#include <[zephyr/drivers/spi\_emul.h](spi__emul_8h.md)>

30#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

31

[ 35](group__io__emulators.md#ga39b7a9438507b0be95038fe9464762aa)enum [emul\_bus\_type](group__io__emulators.md#ga39b7a9438507b0be95038fe9464762aa) {

[ 36](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa37469f6df0ab808efe8d8a28f3424b5f) [EMUL\_BUS\_TYPE\_I2C](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa37469f6df0ab808efe8d8a28f3424b5f),

[ 37](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa58714c3eeb3b9828fab041bd9a9f6ec1) [EMUL\_BUS\_TYPE\_ESPI](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa58714c3eeb3b9828fab041bd9a9f6ec1),

[ 38](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa037e86fa4d585eac9420053d869b423a) [EMUL\_BUS\_TYPE\_SPI](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa037e86fa4d585eac9420053d869b423a),

[ 39](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa942dd8fbb58d92fc987b0b2715a4a15d) [EMUL\_BUS\_TYPE\_NONE](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa942dd8fbb58d92fc987b0b2715a4a15d),

40};

41

[ 45](structemul__link__for__bus.md)struct [emul\_link\_for\_bus](structemul__link__for__bus.md) {

[ 46](structemul__link__for__bus.md#af81ff0873c340778030700d1cd2b7294) const struct [device](structdevice.md) \*[dev](structemul__link__for__bus.md#af81ff0873c340778030700d1cd2b7294);

47};

48

[ 50](structemul__list__for__bus.md)struct [emul\_list\_for\_bus](structemul__list__for__bus.md) {

[ 52](structemul__list__for__bus.md#a4cd116abd8480895312564dcdf3f2e03) const struct [emul\_link\_for\_bus](structemul__link__for__bus.md) \*[children](structemul__list__for__bus.md#a4cd116abd8480895312564dcdf3f2e03);

[ 54](structemul__list__for__bus.md#abcfe7bc6d82a16959c3d89b8598a8563) unsigned int [num\_children](structemul__list__for__bus.md#abcfe7bc6d82a16959c3d89b8598a8563);

55};

56

[ 64](group__io__emulators.md#gaa6129de6e0edef345242559a3dac3a50)typedef int (\*[emul\_init\_t](group__io__emulators.md#gaa6129de6e0edef345242559a3dac3a50))(const struct [emul](structemul.md) \*[emul](structemul.md), const struct [device](structdevice.md) \*parent);

65

[ 69](structno__bus__emul.md)struct [no\_bus\_emul](structno__bus__emul.md) {

[ 70](structno__bus__emul.md#a9d4274ae11784a6c6e9892b1bde89780) void \*[api](structno__bus__emul.md#a9d4274ae11784a6c6e9892b1bde89780);

[ 71](structno__bus__emul.md#aee2b4297901108a071658fa07e56043f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structno__bus__emul.md#aee2b4297901108a071658fa07e56043f);

72};

73

[ 78](structemul.md)struct [emul](structemul.md) {

[ 80](structemul.md#a5ec4e292613d2d79d6bd57fe6cd5b41b) [emul\_init\_t](group__io__emulators.md#gaa6129de6e0edef345242559a3dac3a50) [init](structemul.md#a5ec4e292613d2d79d6bd57fe6cd5b41b);

[ 82](structemul.md#a4159ce815a6b4022bf35cbd0d0102bba) const struct [device](structdevice.md) \*[dev](structemul.md#a4159ce815a6b4022bf35cbd0d0102bba);

[ 84](structemul.md#ae6f86e44a6b28296528d607124f4b812) const void \*[cfg](structemul.md#ae6f86e44a6b28296528d607124f4b812);

[ 86](structemul.md#a82f3fcaf221cd329ef1b6cb93cc7c8e6) void \*[data](structemul.md#a82f3fcaf221cd329ef1b6cb93cc7c8e6);

[ 88](structemul.md#a92a4811a8656b8f0c3f3c7873918da3c) enum [emul\_bus\_type](group__io__emulators.md#ga39b7a9438507b0be95038fe9464762aa) [bus\_type](structemul.md#a92a4811a8656b8f0c3f3c7873918da3c);

[ 90](unionemul_1_1bus.md) union [bus](unionemul_1_1bus.md) {

[ 91](unionemul_1_1bus.md#a1f2079251cce4ffa92d3f1a4315b7b42) struct [i2c\_emul](structi2c__emul.md) \*[i2c](unionemul_1_1bus.md#a1f2079251cce4ffa92d3f1a4315b7b42);

[ 92](unionemul_1_1bus.md#adbf407e15fbfe3da70b0c458e8edcf8d) struct [espi\_emul](structespi__emul.md) \*[espi](unionemul_1_1bus.md#adbf407e15fbfe3da70b0c458e8edcf8d);

[ 93](unionemul_1_1bus.md#aa9e71864d3e4a0df64ed785522f29139) struct [spi\_emul](structspi__emul.md) \*[spi](unionemul_1_1bus.md#aa9e71864d3e4a0df64ed785522f29139);

[ 94](unionemul_1_1bus.md#a6a8ad4e1e183a81c05b64b5c87cfa25a) struct [no\_bus\_emul](structno__bus__emul.md) \*[none](unionemul_1_1bus.md#a6a8ad4e1e183a81c05b64b5c87cfa25a);

[ 95](structemul.md#a9f3ec93d05fdf287069dbb0aa48cc8ac) } [bus](structemul.md#a9f3ec93d05fdf287069dbb0aa48cc8ac);

[ 96](structemul.md#a9f3ec93d05fdf287069dbb0aa48cc8ac)

[ 97](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea) const void \*[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea);

98};

99

[ 105](group__io__emulators.md#gac1638c8cad48dab50f9ebc83592236db)#define EMUL\_DT\_NAME\_GET(node\_id) \_CONCAT(\_\_emulreg\_, node\_id)

106

107/\* Get a unique identifier based on the given \_dev\_node\_id's reg property and

108 \* the bus its on. Intended for use in other internal macros when declaring {bus}\_emul

109 \* structs in peripheral emulators.

110 \*/

111#define Z\_EMUL\_REG\_BUS\_IDENTIFIER(\_dev\_node\_id) (\_CONCAT(\_CONCAT(\_\_emulreg\_, \_dev\_node\_id), \_bus))

112

113/\* Conditionally places text based on what bus \_dev\_node\_id is on. \*/

114#define Z\_EMUL\_BUS(\_dev\_node\_id, \_i2c, \_espi, \_spi, \_none) \

115 COND\_CODE\_1(DT\_ON\_BUS(\_dev\_node\_id, i2c), (\_i2c), \

116 (COND\_CODE\_1(DT\_ON\_BUS(\_dev\_node\_id, espi), (\_espi), \

117 (COND\_CODE\_1(DT\_ON\_BUS(\_dev\_node\_id, spi), (\_spi), (\_none))))))

[ 132](group__io__emulators.md#gad6292e3cd7f17a3600be396777f304c8)#define EMUL\_DT\_DEFINE(node\_id, init\_fn, data\_ptr, cfg\_ptr, bus\_api, \_backend\_api) \

133 static struct Z\_EMUL\_BUS(node\_id, i2c\_emul, espi\_emul, spi\_emul, no\_bus\_emul) \

134 Z\_EMUL\_REG\_BUS\_IDENTIFIER(node\_id) = { \

135 .api = bus\_api, \

136 .Z\_EMUL\_BUS(node\_id, addr, chipsel, chipsel, addr) = DT\_REG\_ADDR(node\_id), \

137 }; \

138 const STRUCT\_SECTION\_ITERABLE(emul, EMUL\_DT\_NAME\_GET(node\_id)) \

139 \_\_used = { \

140 .init = (init\_fn), \

141 .dev = DEVICE\_DT\_GET(node\_id), \

142 .cfg = (cfg\_ptr), \

143 .data = (data\_ptr), \

144 .bus\_type = Z\_EMUL\_BUS(node\_id, EMUL\_BUS\_TYPE\_I2C, EMUL\_BUS\_TYPE\_ESPI, \

145 EMUL\_BUS\_TYPE\_SPI, EMUL\_BUS\_TYPE\_NONE), \

146 .bus = {.Z\_EMUL\_BUS(node\_id, i2c, espi, spi, none) = \

147 &(Z\_EMUL\_REG\_BUS\_IDENTIFIER(node\_id))}, \

148 .backend\_api = (\_backend\_api), \

149 };

150

[ 159](group__io__emulators.md#gafe7f4912bcffed1366ce07d024a4f977)#define EMUL\_DT\_INST\_DEFINE(inst, ...) EMUL\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

160

[ 175](group__io__emulators.md#ga300d997df388118ae380e79b972f85cf)#define EMUL\_DT\_GET(node\_id) (&EMUL\_DT\_NAME\_GET(node\_id))

176

[ 186](group__io__emulators.md#gab37b4f8b4c434ca38f523eb6391d4e3b)#define EMUL\_DT\_GET\_OR\_NULL(node\_id) \

187 COND\_CODE\_1(DT\_NODE\_HAS\_STATUS(node\_id, okay), (EMUL\_DT\_GET(node\_id)), (NULL))

188

[ 196](group__io__emulators.md#gad587b2852a182e1a7fdcb3b056d898f1)int [emul\_init\_for\_bus](group__io__emulators.md#gad587b2852a182e1a7fdcb3b056d898f1)(const struct [device](structdevice.md) \*dev);

197

[ 210](group__io__emulators.md#gaad94c1e07998417cb9aa06d03be3b280)const struct [emul](structemul.md) \*[emul\_get\_binding](group__io__emulators.md#gaad94c1e07998417cb9aa06d03be3b280)(const char \*name);

211

215

216#define Z\_MAYBE\_EMUL\_DECLARE\_INTERNAL(node\_id) extern const struct emul EMUL\_DT\_NAME\_GET(node\_id);

217

[ 218](emul_8h.md#a6b4463d5ce37aa4a16f66e8981be6007)[DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)(Z\_MAYBE\_EMUL\_DECLARE\_INTERNAL);

219

220#ifdef \_\_cplusplus

221}

222#endif /\* \_\_cplusplus \*/

223

224#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_EMUL\_H\_ \*/

[device.h](device_8h.md)

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[espi\_emul.h](espi__emul_8h.md)

Public APIs for the eSPI emulation drivers.

[DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)

#define DT\_FOREACH\_STATUS\_OKAY\_NODE(fn)

Invokes fn for every status okay node in the tree.

**Definition** devicetree.h:2671

[emul\_bus\_type](group__io__emulators.md#ga39b7a9438507b0be95038fe9464762aa)

emul\_bus\_type

The types of supported buses.

**Definition** emul.h:35

[emul\_init\_t](group__io__emulators.md#gaa6129de6e0edef345242559a3dac3a50)

int(\* emul\_init\_t)(const struct emul \*emul, const struct device \*parent)

Standard callback for emulator initialisation providing the initialiser record and the device that ca...

**Definition** emul.h:64

[emul\_get\_binding](group__io__emulators.md#gaad94c1e07998417cb9aa06d03be3b280)

const struct emul \* emul\_get\_binding(const char \*name)

Retrieve the emul structure for an emulator by name.

[emul\_init\_for\_bus](group__io__emulators.md#gad587b2852a182e1a7fdcb3b056d898f1)

int emul\_init\_for\_bus(const struct device \*dev)

Set up a list of emulators.

[EMUL\_BUS\_TYPE\_SPI](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa037e86fa4d585eac9420053d869b423a)

@ EMUL\_BUS\_TYPE\_SPI

**Definition** emul.h:38

[EMUL\_BUS\_TYPE\_I2C](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa37469f6df0ab808efe8d8a28f3424b5f)

@ EMUL\_BUS\_TYPE\_I2C

**Definition** emul.h:36

[EMUL\_BUS\_TYPE\_ESPI](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa58714c3eeb3b9828fab041bd9a9f6ec1)

@ EMUL\_BUS\_TYPE\_ESPI

**Definition** emul.h:37

[EMUL\_BUS\_TYPE\_NONE](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa942dd8fbb58d92fc987b0b2715a4a15d)

@ EMUL\_BUS\_TYPE\_NONE

**Definition** emul.h:39

[i2c\_emul.h](i2c__emul_8h.md)

Public APIs for the I2C emulation drivers.

[spi\_emul.h](spi__emul_8h.md)

Public APIs for the SPI emulation drivers.

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[emul\_link\_for\_bus](structemul__link__for__bus.md)

Structure uniquely identifying a device to be emulated.

**Definition** emul.h:45

[emul\_link\_for\_bus::dev](structemul__link__for__bus.md#af81ff0873c340778030700d1cd2b7294)

const struct device \* dev

**Definition** emul.h:46

[emul\_list\_for\_bus](structemul__list__for__bus.md)

List of emulators attached to a bus.

**Definition** emul.h:50

[emul\_list\_for\_bus::children](structemul__list__for__bus.md#a4cd116abd8480895312564dcdf3f2e03)

const struct emul\_link\_for\_bus \* children

Identifiers for children of the node.

**Definition** emul.h:52

[emul\_list\_for\_bus::num\_children](structemul__list__for__bus.md#abcfe7bc6d82a16959c3d89b8598a8563)

unsigned int num\_children

Number of children of the node.

**Definition** emul.h:54

[emul](structemul.md)

An emulator instance - represents the target emulated device/peripheral that is interacted with throu...

**Definition** emul.h:78

[emul::dev](structemul.md#a4159ce815a6b4022bf35cbd0d0102bba)

const struct device \* dev

handle to the device for which this provides low-level emulation

**Definition** emul.h:82

[emul::init](structemul.md#a5ec4e292613d2d79d6bd57fe6cd5b41b)

emul\_init\_t init

function used to initialise the emulator state

**Definition** emul.h:80

[emul::data](structemul.md#a82f3fcaf221cd329ef1b6cb93cc7c8e6)

void \* data

Emulator-specific data.

**Definition** emul.h:86

[emul::bus\_type](structemul.md#a92a4811a8656b8f0c3f3c7873918da3c)

enum emul\_bus\_type bus\_type

The bus type that the emulator is attached to.

**Definition** emul.h:88

[emul::bus](structemul.md#a9f3ec93d05fdf287069dbb0aa48cc8ac)

union emul::bus bus

[emul::backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea)

const void \* backend\_api

Address of the API structure exposed by the emulator instance.

**Definition** emul.h:97

[emul::cfg](structemul.md#ae6f86e44a6b28296528d607124f4b812)

const void \* cfg

Emulator-specific configuration data.

**Definition** emul.h:84

[espi\_emul](structespi__emul.md)

Node in a linked list of emulators for eSPI devices.

**Definition** espi\_emul.h:111

[i2c\_emul](structi2c__emul.md)

Node in a linked list of emulators for I2C devices.

**Definition** i2c\_emul.h:37

[no\_bus\_emul](structno__bus__emul.md)

Emulator API stub when an emulator is not actually placed on a bus.

**Definition** emul.h:69

[no\_bus\_emul::api](structno__bus__emul.md#a9d4274ae11784a6c6e9892b1bde89780)

void \* api

**Definition** emul.h:70

[no\_bus\_emul::addr](structno__bus__emul.md#aee2b4297901108a071658fa07e56043f)

uint16\_t addr

**Definition** emul.h:71

[spi\_emul](structspi__emul.md)

Node in a linked list of emulators for SPI devices.

**Definition** spi\_emul.h:37

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[emul::bus](unionemul_1_1bus.md)

Pointer to the emulated bus node.

**Definition** emul.h:90

[emul::bus::i2c](unionemul_1_1bus.md#a1f2079251cce4ffa92d3f1a4315b7b42)

struct i2c\_emul \* i2c

**Definition** emul.h:91

[emul::bus::none](unionemul_1_1bus.md#a6a8ad4e1e183a81c05b64b5c87cfa25a)

struct no\_bus\_emul \* none

**Definition** emul.h:94

[emul::bus::spi](unionemul_1_1bus.md#aa9e71864d3e4a0df64ed785522f29139)

struct spi\_emul \* spi

**Definition** emul.h:93

[emul::bus::espi](unionemul_1_1bus.md#adbf407e15fbfe3da70b0c458e8edcf8d)

struct espi\_emul \* espi

**Definition** emul.h:92

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [emul.h](emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
