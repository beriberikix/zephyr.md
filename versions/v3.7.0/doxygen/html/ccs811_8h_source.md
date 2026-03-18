---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ccs811_8h_source.html
original_path: doxygen/html/ccs811_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ccs811.h

[Go to the documentation of this file.](ccs811_8h.md)

1/\*

2 \* Copyright (c) 2018 Peter Bigot Consulting, LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_CCS811\_H\_

16#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_CCS811\_H\_

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

22#include <[zephyr/device.h](device_8h.md)>

23#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

24

25/\* Status register fields \*/

[ 26](ccs811_8h.md#a20384d881a191499e059822188096a3f)#define CCS811\_STATUS\_ERROR BIT(0)

[ 27](ccs811_8h.md#a6020157cec1ebbae138262d0c0f4de88)#define CCS811\_STATUS\_DATA\_READY BIT(3)

[ 28](ccs811_8h.md#a30dbcc60ace45a6deeb4d7b4254713e6)#define CCS811\_STATUS\_APP\_VALID BIT(4)

[ 29](ccs811_8h.md#afb4bbabdc1c3df8fae10986f14974cdf)#define CCS811\_STATUS\_FW\_MODE BIT(7)

30

31/\* Error register fields \*/

[ 32](ccs811_8h.md#aea6a55c33babbec3613074233ed59e87)#define CCS811\_ERROR\_WRITE\_REG\_INVALID BIT(0)

[ 33](ccs811_8h.md#a362e9ebd07dd4e3b08e19b51ef1e80c3)#define CCS811\_ERROR\_READ\_REG\_INVALID BIT(1)

[ 34](ccs811_8h.md#a86174804458c701304aac10e0f79395d)#define CCS811\_ERROR\_MEASMODE\_INVALID BIT(2)

[ 35](ccs811_8h.md#a8df212e550d4722a9588d2afb0353423)#define CCS811\_ERROR\_MAX\_RESISTANCE BIT(3)

[ 36](ccs811_8h.md#aaf6643eca6856def154c5c3b27a47722)#define CCS811\_ERROR\_HEATER\_FAULT BIT(4)

[ 37](ccs811_8h.md#add1eea491f4fa321455bf450de9523ff)#define CCS811\_ERROR\_HEATER\_SUPPLY BIT(5)

38

39/\* Measurement mode constants \*/

[ 40](ccs811_8h.md#aaf3104eccd057fb02e2e3bd690d033bf)#define CCS811\_MODE\_IDLE 0x00

[ 41](ccs811_8h.md#a0ae923f15a5dff2eeb9bb6a4c322a846)#define CCS811\_MODE\_IAQ\_1SEC 0x10

[ 42](ccs811_8h.md#a50ba73c3faf9be67ca8503185212d646)#define CCS811\_MODE\_IAQ\_10SEC 0x20

[ 43](ccs811_8h.md#aba48acebce3be106f2baf4d138ba10ae)#define CCS811\_MODE\_IAQ\_60SEC 0x30

[ 44](ccs811_8h.md#a7f2d13d60b58cd38d2e1faed34783e8f)#define CCS811\_MODE\_IAQ\_250MSEC 0x40

[ 45](ccs811_8h.md#a2da34b0adb925734239288c97ec1224a)#define CCS811\_MODE\_MSK 0x70

46

[ 48](structccs811__result__type.md)struct [ccs811\_result\_type](structccs811__result__type.md) {

[ 50](structccs811__result__type.md#a07b71c653136f3afb9d8e0d594cf7c24) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [co2](structccs811__result__type.md#a07b71c653136f3afb9d8e0d594cf7c24);

51

[ 56](structccs811__result__type.md#ad3fef69b83fa1f67f0a3cf7ab1f36f12) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [voc](structccs811__result__type.md#ad3fef69b83fa1f67f0a3cf7ab1f36f12);

57

[ 59](structccs811__result__type.md#a5ddde08ed2992dcd24a283f781775da2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [raw](structccs811__result__type.md#a5ddde08ed2992dcd24a283f781775da2);

60

[ 62](structccs811__result__type.md#adf50f8b7e4eb0b45b61a00fb4e2ae8f5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structccs811__result__type.md#adf50f8b7e4eb0b45b61a00fb4e2ae8f5);

63

[ 69](structccs811__result__type.md#a00426f8ba17dcbf696b70a5adb6ff5a4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [error](structccs811__result__type.md#a00426f8ba17dcbf696b70a5adb6ff5a4);

70};

71

[ 83](ccs811_8h.md#a96979437b70cdab86a9a09a6e8876c0b)const struct [ccs811\_result\_type](structccs811__result__type.md) \*[ccs811\_result](ccs811_8h.md#a96979437b70cdab86a9a09a6e8876c0b)(const struct [device](structdevice.md) \*dev);

84

[ 91](structccs811__configver__type.md)struct [ccs811\_configver\_type](structccs811__configver__type.md) {

[ 92](structccs811__configver__type.md#a78d15d9b7695cc7dd4251cecd573a18a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [fw\_boot\_version](structccs811__configver__type.md#a78d15d9b7695cc7dd4251cecd573a18a);

[ 93](structccs811__configver__type.md#add87f032fef47ad3c4b6415a9aeb829d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [fw\_app\_version](structccs811__configver__type.md#add87f032fef47ad3c4b6415a9aeb829d);

[ 94](structccs811__configver__type.md#ad76906d24bd14e63dd7a4c1628fd81cc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hw\_version](structccs811__configver__type.md#ad76906d24bd14e63dd7a4c1628fd81cc);

[ 95](structccs811__configver__type.md#aa8dad67bbdd286a54749e421967d228d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structccs811__configver__type.md#aa8dad67bbdd286a54749e421967d228d);

96};

97

[ 107](ccs811_8h.md#a89d51f90a25cfa3437eed843f0f3da20)int [ccs811\_configver\_fetch](ccs811_8h.md#a89d51f90a25cfa3437eed843f0f3da20)(const struct [device](structdevice.md) \*dev,

108 struct [ccs811\_configver\_type](structccs811__configver__type.md) \*ptr);

109

[ 124](ccs811_8h.md#a313fc541226b986eb098b88355c75ab0)int [ccs811\_baseline\_fetch](ccs811_8h.md#a313fc541226b986eb098b88355c75ab0)(const struct [device](structdevice.md) \*dev);

125

[ 138](ccs811_8h.md#af6ed9f060f3bda5e867a772caf8cd333)int [ccs811\_baseline\_update](ccs811_8h.md#af6ed9f060f3bda5e867a772caf8cd333)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) baseline);

139

[ 154](ccs811_8h.md#ac50d59a4f6ed8af7b62cb381c2aa7b22)int [ccs811\_envdata\_update](ccs811_8h.md#ac50d59a4f6ed8af7b62cb381c2aa7b22)(const struct [device](structdevice.md) \*dev,

155 const struct [sensor\_value](structsensor__value.md) \*temperature,

156 const struct [sensor\_value](structsensor__value.md) \*humidity);

157

158#ifdef \_\_cplusplus

159}

160#endif

161

162#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_CCS811\_H\_ \*/

[ccs811\_baseline\_fetch](ccs811_8h.md#a313fc541226b986eb098b88355c75ab0)

int ccs811\_baseline\_fetch(const struct device \*dev)

Fetch the current value of the BASELINE register.

[ccs811\_configver\_fetch](ccs811_8h.md#a89d51f90a25cfa3437eed843f0f3da20)

int ccs811\_configver\_fetch(const struct device \*dev, struct ccs811\_configver\_type \*ptr)

Fetch operating mode and version information.

[ccs811\_result](ccs811_8h.md#a96979437b70cdab86a9a09a6e8876c0b)

const struct ccs811\_result\_type \* ccs811\_result(const struct device \*dev)

Access storage for the most recent data read from the sensor.

[ccs811\_envdata\_update](ccs811_8h.md#ac50d59a4f6ed8af7b62cb381c2aa7b22)

int ccs811\_envdata\_update(const struct device \*dev, const struct sensor\_value \*temperature, const struct sensor\_value \*humidity)

Update the ENV\_DATA register.

[ccs811\_baseline\_update](ccs811_8h.md#af6ed9f060f3bda5e867a772caf8cd333)

int ccs811\_baseline\_update(const struct device \*dev, uint16\_t baseline)

Update the BASELINE register.

[device.h](device_8h.md)

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[ccs811\_configver\_type](structccs811__configver__type.md)

Get information about static CCS811 state.

**Definition** ccs811.h:91

[ccs811\_configver\_type::fw\_boot\_version](structccs811__configver__type.md#a78d15d9b7695cc7dd4251cecd573a18a)

uint16\_t fw\_boot\_version

**Definition** ccs811.h:92

[ccs811\_configver\_type::mode](structccs811__configver__type.md#aa8dad67bbdd286a54749e421967d228d)

uint8\_t mode

**Definition** ccs811.h:95

[ccs811\_configver\_type::hw\_version](structccs811__configver__type.md#ad76906d24bd14e63dd7a4c1628fd81cc)

uint8\_t hw\_version

**Definition** ccs811.h:94

[ccs811\_configver\_type::fw\_app\_version](structccs811__configver__type.md#add87f032fef47ad3c4b6415a9aeb829d)

uint16\_t fw\_app\_version

**Definition** ccs811.h:93

[ccs811\_result\_type](structccs811__result__type.md)

Information collected from the sensor on each fetch.

**Definition** ccs811.h:48

[ccs811\_result\_type::error](structccs811__result__type.md#a00426f8ba17dcbf696b70a5adb6ff5a4)

uint8\_t error

Sensor error flags at completion of most recent fetch.

**Definition** ccs811.h:69

[ccs811\_result\_type::co2](structccs811__result__type.md#a07b71c653136f3afb9d8e0d594cf7c24)

uint16\_t co2

Equivalent carbon dioxide in parts-per-million volume (ppmv).

**Definition** ccs811.h:50

[ccs811\_result\_type::raw](structccs811__result__type.md#a5ddde08ed2992dcd24a283f781775da2)

uint16\_t raw

Raw voltage and current measured by sensor.

**Definition** ccs811.h:59

[ccs811\_result\_type::voc](structccs811__result__type.md#ad3fef69b83fa1f67f0a3cf7ab1f36f12)

uint16\_t voc

Equivalent total volatile organic compounds in parts-per-billion volume.

**Definition** ccs811.h:56

[ccs811\_result\_type::status](structccs811__result__type.md#adf50f8b7e4eb0b45b61a00fb4e2ae8f5)

uint8\_t status

Sensor status at completion of most recent fetch.

**Definition** ccs811.h:62

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[sensor\_value](structsensor__value.md)

Representation of a sensor readout value.

**Definition** sensor.h:51

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [ccs811.h](ccs811_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
