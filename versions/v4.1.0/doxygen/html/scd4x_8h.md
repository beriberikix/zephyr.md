---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/scd4x_8h.html
original_path: doxygen/html/scd4x_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

scd4x.h File Reference

`#include <[zephyr/drivers/sensor.h](sensor_8h_source.md)>`

[Go to the source code of this file.](scd4x_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [sensor\_attribute\_scd4x](#a8cbb7f3f4cad13f36cd454073e9d344d) {     [SENSOR\_ATTR\_SCD4X\_TEMPERATURE\_OFFSET](#a8cbb7f3f4cad13f36cd454073e9d344daa8c54289d95f79519831458018ccb4ba) = SENSOR\_ATTR\_PRIV\_START , [SENSOR\_ATTR\_SCD4X\_SENSOR\_ALTITUDE](#a8cbb7f3f4cad13f36cd454073e9d344dac2697f0466ec1822fbfe82e7b5d6287e) , [SENSOR\_ATTR\_SCD4X\_AMBIENT\_PRESSURE](#a8cbb7f3f4cad13f36cd454073e9d344daa6a806666dcb476b83c1affb15c2964c) , [SENSOR\_ATTR\_SCD4X\_AUTOMATIC\_CALIB\_ENABLE](#a8cbb7f3f4cad13f36cd454073e9d344dae61b7281c3d3135bc1557e970d6b2b14) ,     [SENSOR\_ATTR\_SCD4X\_SELF\_CALIB\_INITIAL\_PERIOD](#a8cbb7f3f4cad13f36cd454073e9d344da8dccaa05552bbc5b9c474cbaa65ed7b0) , [SENSOR\_ATTR\_SCD4X\_SELF\_CALIB\_STANDARD\_PERIOD](#a8cbb7f3f4cad13f36cd454073e9d344dac54720c5cb0dce105986b8b6c7b0ea8a)   } |

| Functions | |
| --- | --- |
| int | [scd4x\_forced\_recalibration](#a9c7260e275f85836ea717186ff8aa796) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) target\_concentration, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*frc\_correction) |
|  | Performs a forced recalibration. |
| int | [scd4x\_self\_test](#a076766c7322d9b050acf5963ceba718a) (const struct [device](structdevice.md) \*dev) |
|  | Performs a self test. |
| int | [scd4x\_persist\_settings](#a91f055d3b7a4c8c70c30982cf0ceff9c) (const struct [device](structdevice.md) \*dev) |
|  | Performs a self test. |
| int | [scd4x\_factory\_reset](#aa501b89af4dbed0dc9be5d1bc1742c99) (const struct [device](structdevice.md) \*dev) |
|  | Performs a factory reset. |

## Enumeration Type Documentation

## [◆ ](#a8cbb7f3f4cad13f36cd454073e9d344d)sensor\_attribute\_scd4x

| enum [sensor\_attribute\_scd4x](#a8cbb7f3f4cad13f36cd454073e9d344d) |
| --- |

| Enumerator | |
| --- | --- |
| SENSOR\_ATTR\_SCD4X\_TEMPERATURE\_OFFSET |  |
| SENSOR\_ATTR\_SCD4X\_SENSOR\_ALTITUDE |  |
| SENSOR\_ATTR\_SCD4X\_AMBIENT\_PRESSURE |  |
| SENSOR\_ATTR\_SCD4X\_AUTOMATIC\_CALIB\_ENABLE |  |
| SENSOR\_ATTR\_SCD4X\_SELF\_CALIB\_INITIAL\_PERIOD |  |
| SENSOR\_ATTR\_SCD4X\_SELF\_CALIB\_STANDARD\_PERIOD |  |

## Function Documentation

## [◆ ](#aa501b89af4dbed0dc9be5d1bc1742c99)scd4x\_factory\_reset()

| int scd4x\_factory\_reset | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Performs a factory reset.

The perform\_factory\_reset command resets all configuration settings stored in the EEPROM and erases the FRC and ASC algorithm history.

Parameters
:   | dev | Pointer to the sensor device |
    | --- | --- |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#a9c7260e275f85836ea717186ff8aa796)scd4x\_forced\_recalibration()

| int scd4x\_forced\_recalibration | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *target\_concentration*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *frc\_correction* ) |

Performs a forced recalibration.

Operate the SCD4x in the operation mode for at least 3 minutes in an environment with a homogeneous and constant CO2 concentration. Otherwise the recalibratioin will fail. The sensor must be operated at the voltage desired for the application when performing the FRC sequence.

Parameters
:   | dev | Pointer to the sensor device |
    | --- | --- |
    | target\_concentration | Reference CO2 concentration. |
    | frc\_correction | Previous differences from the target concentration |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#a91f055d3b7a4c8c70c30982cf0ceff9c)scd4x\_persist\_settings()

| int scd4x\_persist\_settings | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Performs a self test.

The persist\_settings command can be used to save the actual configuration. This command should only be sent when persistence is required and if actual changes to the configuration have been made. The EEPROM is guaranteed to withstand at least 2000 write cycles

Parameters
:   | dev | Pointer to the sensor device |
    | --- | --- |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#a076766c7322d9b050acf5963ceba718a)scd4x\_self\_test()

| int scd4x\_self\_test | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Performs a self test.

The self\_test command can be used as an end-of-line test to check the sensor functionality

Parameters
:   | dev | Pointer to the sensor device |
    | --- | --- |

Returns
:   0 if successful, negative errno code if failure.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [scd4x.h](scd4x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
