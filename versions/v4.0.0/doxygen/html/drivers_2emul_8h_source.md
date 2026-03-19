---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2emul_8h_source.html
original_path: doxygen/html/drivers_2emul_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

emul.h

[Go to the documentation of this file.](drivers_2emul_8h.md)

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

30#include <[zephyr/drivers/mspi\_emul.h](mspi__emul_8h.md)>

31#include <[zephyr/drivers/uart\_emul.h](uart__emul_8h.md)>

32#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

33

[ 37](group__io__emulators.md#ga39b7a9438507b0be95038fe9464762aa)enum [emul\_bus\_type](group__io__emulators.md#ga39b7a9438507b0be95038fe9464762aa) {

[ 38](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa37469f6df0ab808efe8d8a28f3424b5f) [EMUL\_BUS\_TYPE\_I2C](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa37469f6df0ab808efe8d8a28f3424b5f),

[ 39](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa58714c3eeb3b9828fab041bd9a9f6ec1) [EMUL\_BUS\_TYPE\_ESPI](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa58714c3eeb3b9828fab041bd9a9f6ec1),

[ 40](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa037e86fa4d585eac9420053d869b423a) [EMUL\_BUS\_TYPE\_SPI](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa037e86fa4d585eac9420053d869b423a),

[ 41](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa532ba489c52ce6919751fc1a45f70a46) [EMUL\_BUS\_TYPE\_MSPI](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa532ba489c52ce6919751fc1a45f70a46),

[ 42](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaae93177d41e38aa873c603fb606db13b6) [EMUL\_BUS\_TYPE\_UART](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaae93177d41e38aa873c603fb606db13b6),

[ 43](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa942dd8fbb58d92fc987b0b2715a4a15d) [EMUL\_BUS\_TYPE\_NONE](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa942dd8fbb58d92fc987b0b2715a4a15d),

44};

45

[ 49](structemul__link__for__bus.md)struct [emul\_link\_for\_bus](structemul__link__for__bus.md) {

[ 50](structemul__link__for__bus.md#af81ff0873c340778030700d1cd2b7294) const struct [device](structdevice.md) \*[dev](structemul__link__for__bus.md#af81ff0873c340778030700d1cd2b7294);

51};

52

[ 54](structemul__list__for__bus.md)struct [emul\_list\_for\_bus](structemul__list__for__bus.md) {

[ 56](structemul__list__for__bus.md#a4cd116abd8480895312564dcdf3f2e03) const struct [emul\_link\_for\_bus](structemul__link__for__bus.md) \*[children](structemul__list__for__bus.md#a4cd116abd8480895312564dcdf3f2e03);

[ 58](structemul__list__for__bus.md#abcfe7bc6d82a16959c3d89b8598a8563) unsigned int [num\_children](structemul__list__for__bus.md#abcfe7bc6d82a16959c3d89b8598a8563);

59};

60

[ 68](group__io__emulators.md#gaa6129de6e0edef345242559a3dac3a50)typedef int (\*[emul\_init\_t](group__io__emulators.md#gaa6129de6e0edef345242559a3dac3a50))(const struct [emul](structemul.md) \*[emul](structemul.md), const struct [device](structdevice.md) \*parent);

69

[ 73](structno__bus__emul.md)struct [no\_bus\_emul](structno__bus__emul.md) {

[ 74](structno__bus__emul.md#a9d4274ae11784a6c6e9892b1bde89780) void \*[api](structno__bus__emul.md#a9d4274ae11784a6c6e9892b1bde89780);

[ 75](structno__bus__emul.md#aee2b4297901108a071658fa07e56043f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structno__bus__emul.md#aee2b4297901108a071658fa07e56043f);

76};

77

[ 82](structemul.md)struct [emul](structemul.md) {

[ 84](structemul.md#a5ec4e292613d2d79d6bd57fe6cd5b41b) [emul\_init\_t](group__io__emulators.md#gaa6129de6e0edef345242559a3dac3a50) [init](structemul.md#a5ec4e292613d2d79d6bd57fe6cd5b41b);

[ 86](structemul.md#a4159ce815a6b4022bf35cbd0d0102bba) const struct [device](structdevice.md) \*[dev](structemul.md#a4159ce815a6b4022bf35cbd0d0102bba);

[ 88](structemul.md#ae6f86e44a6b28296528d607124f4b812) const void \*[cfg](structemul.md#ae6f86e44a6b28296528d607124f4b812);

[ 90](structemul.md#a82f3fcaf221cd329ef1b6cb93cc7c8e6) void \*[data](structemul.md#a82f3fcaf221cd329ef1b6cb93cc7c8e6);

[ 92](structemul.md#a92a4811a8656b8f0c3f3c7873918da3c) enum [emul\_bus\_type](group__io__emulators.md#ga39b7a9438507b0be95038fe9464762aa) [bus\_type](structemul.md#a92a4811a8656b8f0c3f3c7873918da3c);

[ 94](unionemul_1_1bus.md) union [bus](unionemul_1_1bus.md) {

[ 95](unionemul_1_1bus.md#a1f2079251cce4ffa92d3f1a4315b7b42) struct [i2c\_emul](structi2c__emul.md) \*[i2c](unionemul_1_1bus.md#a1f2079251cce4ffa92d3f1a4315b7b42);

[ 96](unionemul_1_1bus.md#adbf407e15fbfe3da70b0c458e8edcf8d) struct [espi\_emul](structespi__emul.md) \*[espi](unionemul_1_1bus.md#adbf407e15fbfe3da70b0c458e8edcf8d);

[ 97](unionemul_1_1bus.md#aa9e71864d3e4a0df64ed785522f29139) struct [spi\_emul](structspi__emul.md) \*[spi](unionemul_1_1bus.md#aa9e71864d3e4a0df64ed785522f29139);

[ 98](unionemul_1_1bus.md#ab88888ce5358ad5fa016cc5fe01ed98c) struct [mspi\_emul](structmspi__emul.md) \*[mspi](unionemul_1_1bus.md#ab88888ce5358ad5fa016cc5fe01ed98c);

[ 99](unionemul_1_1bus.md#a4201a6d0980f539343936df40a5f7ca9) struct [uart\_emul](structuart__emul.md) \*[uart](unionemul_1_1bus.md#a4201a6d0980f539343936df40a5f7ca9);

[ 100](unionemul_1_1bus.md#a6a8ad4e1e183a81c05b64b5c87cfa25a) struct [no\_bus\_emul](structno__bus__emul.md) \*[none](unionemul_1_1bus.md#a6a8ad4e1e183a81c05b64b5c87cfa25a);

[ 101](structemul.md#a9f3ec93d05fdf287069dbb0aa48cc8ac) } [bus](structemul.md#a9f3ec93d05fdf287069dbb0aa48cc8ac);

[ 102](structemul.md#a9f3ec93d05fdf287069dbb0aa48cc8ac)

[ 103](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea) const void \*[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea);

104};

105

[ 111](group__io__emulators.md#gac1638c8cad48dab50f9ebc83592236db)#define EMUL\_DT\_NAME\_GET(node\_id) \_CONCAT(\_\_emulreg\_, node\_id)

112

113/\* Get a unique identifier based on the given \_dev\_node\_id's reg property and

114 \* the bus its on. Intended for use in other internal macros when declaring {bus}\_emul

115 \* structs in peripheral emulators.

116 \*/

117#define Z\_EMUL\_REG\_BUS\_IDENTIFIER(\_dev\_node\_id) \_CONCAT(\_CONCAT(\_\_emulreg\_, \_dev\_node\_id), \_bus)

118

119/\* Conditionally places text based on what bus \_dev\_node\_id is on. \*/

120#define Z\_EMUL\_BUS(\_dev\_node\_id, \_i2c, \_espi, \_spi, \_mspi, \_uart, \_none) \

121 COND\_CODE\_1(DT\_ON\_BUS(\_dev\_node\_id, i2c), (\_i2c), \

122 (COND\_CODE\_1(DT\_ON\_BUS(\_dev\_node\_id, espi), (\_espi), \

123 (COND\_CODE\_1(DT\_ON\_BUS(\_dev\_node\_id, spi), (\_spi), \

124 (COND\_CODE\_1(DT\_ON\_BUS(\_dev\_node\_id, mspi), (\_mspi), \

125 (COND\_CODE\_1(DT\_ON\_BUS(\_dev\_node\_id, uart), (\_uart), \

126 (\_none))))))))))

127

[ 142](group__io__emulators.md#gad6292e3cd7f17a3600be396777f304c8)#define EMUL\_DT\_DEFINE(node\_id, init\_fn, data\_ptr, cfg\_ptr, bus\_api, \_backend\_api) \

143 static struct Z\_EMUL\_BUS(node\_id, i2c\_emul, espi\_emul, spi\_emul, mspi\_emul, uart\_emul, \

144 no\_bus\_emul) Z\_EMUL\_REG\_BUS\_IDENTIFIER(node\_id) = { \

145 .api = bus\_api, \

146 IF\_ENABLED(DT\_NODE\_HAS\_PROP(node\_id, reg), \

147 (.Z\_EMUL\_BUS(node\_id, addr, chipsel, chipsel, dev\_idx, dummy, addr) = \

148 DT\_REG\_ADDR(node\_id),))}; \

149 const STRUCT\_SECTION\_ITERABLE(emul, EMUL\_DT\_NAME\_GET(node\_id)) \_\_used = { \

150 .init = (init\_fn), \

151 .dev = DEVICE\_DT\_GET(node\_id), \

152 .cfg = (cfg\_ptr), \

153 .data = (data\_ptr), \

154 .bus\_type = Z\_EMUL\_BUS(node\_id, EMUL\_BUS\_TYPE\_I2C, EMUL\_BUS\_TYPE\_ESPI, \

155 EMUL\_BUS\_TYPE\_SPI, EMUL\_BUS\_TYPE\_MSPI, EMUL\_BUS\_TYPE\_UART, \

156 EMUL\_BUS\_TYPE\_NONE), \

157 .bus = {.Z\_EMUL\_BUS(node\_id, i2c, espi, spi, mspi, uart, none) = \

158 &(Z\_EMUL\_REG\_BUS\_IDENTIFIER(node\_id))}, \

159 .backend\_api = (\_backend\_api), \

160 };

161

[ 170](group__io__emulators.md#gafe7f4912bcffed1366ce07d024a4f977)#define EMUL\_DT\_INST\_DEFINE(inst, ...) EMUL\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

171

[ 186](group__io__emulators.md#ga300d997df388118ae380e79b972f85cf)#define EMUL\_DT\_GET(node\_id) (&EMUL\_DT\_NAME\_GET(node\_id))

187

[ 197](group__io__emulators.md#gab37b4f8b4c434ca38f523eb6391d4e3b)#define EMUL\_DT\_GET\_OR\_NULL(node\_id) \

198 COND\_CODE\_1(DT\_NODE\_HAS\_STATUS\_OKAY(node\_id), (EMUL\_DT\_GET(node\_id)), (NULL))

199

[ 207](group__io__emulators.md#gad587b2852a182e1a7fdcb3b056d898f1)int [emul\_init\_for\_bus](group__io__emulators.md#gad587b2852a182e1a7fdcb3b056d898f1)(const struct [device](structdevice.md) \*dev);

208

[ 221](group__io__emulators.md#gaad94c1e07998417cb9aa06d03be3b280)const struct [emul](structemul.md) \*[emul\_get\_binding](group__io__emulators.md#gaad94c1e07998417cb9aa06d03be3b280)(const char \*name);

222

226

227#define Z\_MAYBE\_EMUL\_DECLARE\_INTERNAL(node\_id) extern const struct emul EMUL\_DT\_NAME\_GET(node\_id);

228

[ 229](drivers_2emul_8h.md#a6b4463d5ce37aa4a16f66e8981be6007)[DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)(Z\_MAYBE\_EMUL\_DECLARE\_INTERNAL);

230

231#ifdef \_\_cplusplus

232}

233#endif /\* \_\_cplusplus \*/

234

235#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_EMUL\_H\_ \*/

[device.h](device_8h.md)

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[espi\_emul.h](espi__emul_8h.md)

Public APIs for the eSPI emulation drivers.

[DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)

#define DT\_FOREACH\_STATUS\_OKAY\_NODE(fn)

Invokes fn for every status okay node in the tree.

**Definition** devicetree.h:2942

[emul\_bus\_type](group__io__emulators.md#ga39b7a9438507b0be95038fe9464762aa)

emul\_bus\_type

The types of supported buses.

**Definition** emul.h:37

[emul\_init\_t](group__io__emulators.md#gaa6129de6e0edef345242559a3dac3a50)

int(\* emul\_init\_t)(const struct emul \*emul, const struct device \*parent)

Standard callback for emulator initialisation providing the initialiser record and the device that ca...

**Definition** emul.h:68

[emul\_get\_binding](group__io__emulators.md#gaad94c1e07998417cb9aa06d03be3b280)

const struct emul \* emul\_get\_binding(const char \*name)

Retrieve the emul structure for an emulator by name.

[emul\_init\_for\_bus](group__io__emulators.md#gad587b2852a182e1a7fdcb3b056d898f1)

int emul\_init\_for\_bus(const struct device \*dev)

Set up a list of emulators.

[EMUL\_BUS\_TYPE\_SPI](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa037e86fa4d585eac9420053d869b423a)

@ EMUL\_BUS\_TYPE\_SPI

**Definition** emul.h:40

[EMUL\_BUS\_TYPE\_I2C](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa37469f6df0ab808efe8d8a28f3424b5f)

@ EMUL\_BUS\_TYPE\_I2C

**Definition** emul.h:38

[EMUL\_BUS\_TYPE\_MSPI](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa532ba489c52ce6919751fc1a45f70a46)

@ EMUL\_BUS\_TYPE\_MSPI

**Definition** emul.h:41

[EMUL\_BUS\_TYPE\_ESPI](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa58714c3eeb3b9828fab041bd9a9f6ec1)

@ EMUL\_BUS\_TYPE\_ESPI

**Definition** emul.h:39

[EMUL\_BUS\_TYPE\_NONE](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa942dd8fbb58d92fc987b0b2715a4a15d)

@ EMUL\_BUS\_TYPE\_NONE

**Definition** emul.h:43

[EMUL\_BUS\_TYPE\_UART](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaae93177d41e38aa873c603fb606db13b6)

@ EMUL\_BUS\_TYPE\_UART

**Definition** emul.h:42

[i2c\_emul.h](i2c__emul_8h.md)

Public APIs for the I2C emulation drivers.

[mspi\_emul.h](mspi__emul_8h.md)

Public APIs for the MSPI emulation drivers.

[spi\_emul.h](spi__emul_8h.md)

Public APIs for the SPI emulation drivers.

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[emul\_link\_for\_bus](structemul__link__for__bus.md)

Structure uniquely identifying a device to be emulated.

**Definition** emul.h:49

[emul\_link\_for\_bus::dev](structemul__link__for__bus.md#af81ff0873c340778030700d1cd2b7294)

const struct device \* dev

**Definition** emul.h:50

[emul\_list\_for\_bus](structemul__list__for__bus.md)

List of emulators attached to a bus.

**Definition** emul.h:54

[emul\_list\_for\_bus::children](structemul__list__for__bus.md#a4cd116abd8480895312564dcdf3f2e03)

const struct emul\_link\_for\_bus \* children

Identifiers for children of the node.

**Definition** emul.h:56

[emul\_list\_for\_bus::num\_children](structemul__list__for__bus.md#abcfe7bc6d82a16959c3d89b8598a8563)

unsigned int num\_children

Number of children of the node.

**Definition** emul.h:58

[emul](structemul.md)

An emulator instance - represents the target emulated device/peripheral that is interacted with throu...

**Definition** emul.h:82

[emul::dev](structemul.md#a4159ce815a6b4022bf35cbd0d0102bba)

const struct device \* dev

handle to the device for which this provides low-level emulation

**Definition** emul.h:86

[emul::init](structemul.md#a5ec4e292613d2d79d6bd57fe6cd5b41b)

emul\_init\_t init

function used to initialise the emulator state

**Definition** emul.h:84

[emul::data](structemul.md#a82f3fcaf221cd329ef1b6cb93cc7c8e6)

void \* data

Emulator-specific data.

**Definition** emul.h:90

[emul::bus\_type](structemul.md#a92a4811a8656b8f0c3f3c7873918da3c)

enum emul\_bus\_type bus\_type

The bus type that the emulator is attached to.

**Definition** emul.h:92

[emul::bus](structemul.md#a9f3ec93d05fdf287069dbb0aa48cc8ac)

union emul::bus bus

[emul::backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea)

const void \* backend\_api

Address of the API structure exposed by the emulator instance.

**Definition** emul.h:103

[emul::cfg](structemul.md#ae6f86e44a6b28296528d607124f4b812)

const void \* cfg

Emulator-specific configuration data.

**Definition** emul.h:88

[espi\_emul](structespi__emul.md)

Node in a linked list of emulators for eSPI devices.

**Definition** espi\_emul.h:111

[i2c\_emul](structi2c__emul.md)

Node in a linked list of emulators for I2C devices.

**Definition** i2c\_emul.h:37

[mspi\_emul](structmspi__emul.md)

Node in a linked list of emulators for MSPI devices.

**Definition** mspi\_emul.h:87

[no\_bus\_emul](structno__bus__emul.md)

Emulator API stub when an emulator is not actually placed on a bus.

**Definition** emul.h:73

[no\_bus\_emul::api](structno__bus__emul.md#a9d4274ae11784a6c6e9892b1bde89780)

void \* api

**Definition** emul.h:74

[no\_bus\_emul::addr](structno__bus__emul.md#aee2b4297901108a071658fa07e56043f)

uint16\_t addr

**Definition** emul.h:75

[spi\_emul](structspi__emul.md)

Node in a linked list of emulators for SPI devices.

**Definition** spi\_emul.h:37

[uart\_emul](structuart__emul.md)

Node in a linked list of emulators for UART devices.

**Definition** uart\_emul.h:46

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[uart\_emul.h](uart__emul_8h.md)

Public APIs for the UART device emulation drivers.

[emul::bus](unionemul_1_1bus.md)

Pointer to the emulated bus node.

**Definition** emul.h:94

[emul::bus::i2c](unionemul_1_1bus.md#a1f2079251cce4ffa92d3f1a4315b7b42)

struct i2c\_emul \* i2c

**Definition** emul.h:95

[emul::bus::uart](unionemul_1_1bus.md#a4201a6d0980f539343936df40a5f7ca9)

struct uart\_emul \* uart

**Definition** emul.h:99

[emul::bus::none](unionemul_1_1bus.md#a6a8ad4e1e183a81c05b64b5c87cfa25a)

struct no\_bus\_emul \* none

**Definition** emul.h:100

[emul::bus::spi](unionemul_1_1bus.md#aa9e71864d3e4a0df64ed785522f29139)

struct spi\_emul \* spi

**Definition** emul.h:97

[emul::bus::mspi](unionemul_1_1bus.md#ab88888ce5358ad5fa016cc5fe01ed98c)

struct mspi\_emul \* mspi

**Definition** emul.h:98

[emul::bus::espi](unionemul_1_1bus.md#adbf407e15fbfe3da70b0c458e8edcf8d)

struct espi\_emul \* espi

**Definition** emul.h:96

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [emul.h](drivers_2emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
