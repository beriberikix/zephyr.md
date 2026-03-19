---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/scd4x_8h_source.html
original_path: doxygen/html/scd4x_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

scd4x.h

[Go to the documentation of this file.](scd4x_8h.md)

1/\*

2 \* Copyright (c) 2024 Jan Fäh

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_SCD4X\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_SCD4X\_H\_

9

10#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

11

[ 12](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344d)enum [sensor\_attribute\_scd4x](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344d) {

13 /\* Offset temperature: Toffset\_actual = Tscd4x – Treference + Toffset\_previous

14 \* 0 - 20°C

15 \*/

[ 16](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344daa8c54289d95f79519831458018ccb4ba) [SENSOR\_ATTR\_SCD4X\_TEMPERATURE\_OFFSET](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344daa8c54289d95f79519831458018ccb4ba) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

17 /\* Altidude of the sensor;

18 \* 0 - 3000m

19 \*/

[ 20](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344dac2697f0466ec1822fbfe82e7b5d6287e) [SENSOR\_ATTR\_SCD4X\_SENSOR\_ALTITUDE](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344dac2697f0466ec1822fbfe82e7b5d6287e),

21 /\* Ambient pressure in hPa

22 \* 700 - 1200hPa

23 \*/

[ 24](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344daa6a806666dcb476b83c1affb15c2964c) [SENSOR\_ATTR\_SCD4X\_AMBIENT\_PRESSURE](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344daa6a806666dcb476b83c1affb15c2964c),

25 /\* Set the current state (enabled: 1 / disabled: 0).

26 \* Default: enabled.

27 \*/

[ 28](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344dae61b7281c3d3135bc1557e970d6b2b14) [SENSOR\_ATTR\_SCD4X\_AUTOMATIC\_CALIB\_ENABLE](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344dae61b7281c3d3135bc1557e970d6b2b14),

29 /\* Set the initial period for automatic self calibration correction in hours. Allowed values

30 \* are integer multiples of 4 hours.

31 \* Default: 44

32 \*/

[ 33](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344da8dccaa05552bbc5b9c474cbaa65ed7b0) [SENSOR\_ATTR\_SCD4X\_SELF\_CALIB\_INITIAL\_PERIOD](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344da8dccaa05552bbc5b9c474cbaa65ed7b0),

34 /\* Set the standard period for automatic self calibration correction in hours. Allowed

35 \* values are integer multiples of 4 hours. Default: 156

36 \*/

[ 37](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344dac54720c5cb0dce105986b8b6c7b0ea8a) [SENSOR\_ATTR\_SCD4X\_SELF\_CALIB\_STANDARD\_PERIOD](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344dac54720c5cb0dce105986b8b6c7b0ea8a),

38};

39

[ 53](scd4x_8h.md#a9c7260e275f85836ea717186ff8aa796)int [scd4x\_forced\_recalibration](scd4x_8h.md#a9c7260e275f85836ea717186ff8aa796)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) target\_concentration,

54 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*frc\_correction);

55

[ 65](scd4x_8h.md#a076766c7322d9b050acf5963ceba718a)int [scd4x\_self\_test](scd4x_8h.md#a076766c7322d9b050acf5963ceba718a)(const struct [device](structdevice.md) \*dev);

66

[ 78](scd4x_8h.md#a91f055d3b7a4c8c70c30982cf0ceff9c)int [scd4x\_persist\_settings](scd4x_8h.md#a91f055d3b7a4c8c70c30982cf0ceff9c)(const struct [device](structdevice.md) \*dev);

79

[ 90](scd4x_8h.md#aa501b89af4dbed0dc9be5d1bc1742c99)int [scd4x\_factory\_reset](scd4x_8h.md#aa501b89af4dbed0dc9be5d1bc1742c99)(const struct [device](structdevice.md) \*dev);

91

92#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_SCD4X\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:368

[scd4x\_self\_test](scd4x_8h.md#a076766c7322d9b050acf5963ceba718a)

int scd4x\_self\_test(const struct device \*dev)

Performs a self test.

[sensor\_attribute\_scd4x](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344d)

sensor\_attribute\_scd4x

**Definition** scd4x.h:12

[SENSOR\_ATTR\_SCD4X\_SELF\_CALIB\_INITIAL\_PERIOD](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344da8dccaa05552bbc5b9c474cbaa65ed7b0)

@ SENSOR\_ATTR\_SCD4X\_SELF\_CALIB\_INITIAL\_PERIOD

**Definition** scd4x.h:33

[SENSOR\_ATTR\_SCD4X\_AMBIENT\_PRESSURE](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344daa6a806666dcb476b83c1affb15c2964c)

@ SENSOR\_ATTR\_SCD4X\_AMBIENT\_PRESSURE

**Definition** scd4x.h:24

[SENSOR\_ATTR\_SCD4X\_TEMPERATURE\_OFFSET](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344daa8c54289d95f79519831458018ccb4ba)

@ SENSOR\_ATTR\_SCD4X\_TEMPERATURE\_OFFSET

**Definition** scd4x.h:16

[SENSOR\_ATTR\_SCD4X\_SENSOR\_ALTITUDE](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344dac2697f0466ec1822fbfe82e7b5d6287e)

@ SENSOR\_ATTR\_SCD4X\_SENSOR\_ALTITUDE

**Definition** scd4x.h:20

[SENSOR\_ATTR\_SCD4X\_SELF\_CALIB\_STANDARD\_PERIOD](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344dac54720c5cb0dce105986b8b6c7b0ea8a)

@ SENSOR\_ATTR\_SCD4X\_SELF\_CALIB\_STANDARD\_PERIOD

**Definition** scd4x.h:37

[SENSOR\_ATTR\_SCD4X\_AUTOMATIC\_CALIB\_ENABLE](scd4x_8h.md#a8cbb7f3f4cad13f36cd454073e9d344dae61b7281c3d3135bc1557e970d6b2b14)

@ SENSOR\_ATTR\_SCD4X\_AUTOMATIC\_CALIB\_ENABLE

**Definition** scd4x.h:28

[scd4x\_persist\_settings](scd4x_8h.md#a91f055d3b7a4c8c70c30982cf0ceff9c)

int scd4x\_persist\_settings(const struct device \*dev)

Performs a self test.

[scd4x\_forced\_recalibration](scd4x_8h.md#a9c7260e275f85836ea717186ff8aa796)

int scd4x\_forced\_recalibration(const struct device \*dev, uint16\_t target\_concentration, uint16\_t \*frc\_correction)

Performs a forced recalibration.

[scd4x\_factory\_reset](scd4x_8h.md#aa501b89af4dbed0dc9be5d1bc1742c99)

int scd4x\_factory\_reset(const struct device \*dev)

Performs a factory reset.

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [scd4x.h](scd4x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
