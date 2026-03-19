---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__mspi__configure__api.html
original_path: doxygen/html/group__mspi__configure__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MSPI Configure API

[Device Driver APIs](group__io__interfaces.md) » [MSPI Driver APIs](group__mspi__interface.md)

MSPI Configure API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [mspi\_timing\_cfg](structmspi__timing__cfg.md) |
|  | Stub for struct timing\_cfg. [More...](structmspi__timing__cfg.md#details) |
| struct | [mspi\_dev\_id](structmspi__dev__id.md) |
|  | MSPI device ID The controller can identify its devices and determine whether the access is allowed in a multiple device scheme. [More...](structmspi__dev__id.md#details) |
| struct | [mspi\_cfg](structmspi__cfg.md) |
|  | MSPI controller configuration. [More...](structmspi__cfg.md#details) |
| struct | [mspi\_dt\_spec](structmspi__dt__spec.md) |
|  | MSPI DT information. [More...](structmspi__dt__spec.md#details) |
| struct | [mspi\_dev\_cfg](structmspi__dev__cfg.md) |
|  | MSPI controller device specific configuration. [More...](structmspi__dev__cfg.md#details) |
| struct | [mspi\_xip\_cfg](structmspi__xip__cfg.md) |
|  | MSPI controller XIP configuration. [More...](structmspi__xip__cfg.md#details) |
| struct | [mspi\_scramble\_cfg](structmspi__scramble__cfg.md) |
|  | MSPI controller scramble configuration. [More...](structmspi__scramble__cfg.md#details) |

| Enumerations | |
| --- | --- |
| enum | [mspi\_timing\_param](#gaa25a7f97ab3437d4544832a0e7474f4a) { [MSPI\_TIMING\_PARAM\_DUMMY](#ggaa25a7f97ab3437d4544832a0e7474f4aafae0ccedcd3b8f05e798037bf5414237) } |
|  | Stub for timing parameter. [More...](#gaa25a7f97ab3437d4544832a0e7474f4a) |

| Functions | |
| --- | --- |
| int | [mspi\_config](#ga46c2b98e99ecea045c1ecac4bdf3f087) (const struct [mspi\_dt\_spec](structmspi__dt__spec.md) \*spec) |
|  | Configure a MSPI controller. |
| int | [mspi\_dev\_config](#gaa3c1eae8b3000c9bafcc26f14a8beb8b) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const enum [mspi\_dev\_cfg\_mask](group__mspi__interface.md#ga71c447d059acf7a8055c380243f3a647) param\_mask, const struct [mspi\_dev\_cfg](structmspi__dev__cfg.md) \*cfg) |
|  | Configure a MSPI controller with device specific parameters. |
| int | [mspi\_get\_channel\_status](#ga957b6ecd96c9f942f75bbe500898930d) (const struct [device](structdevice.md) \*controller, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ch) |
|  | Query to see if it a channel is ready. |
| int | [mspi\_xip\_config](#gab9d9104636d3c8167b5876b1bc4348ea) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const struct [mspi\_xip\_cfg](structmspi__xip__cfg.md) \*cfg) |
|  | Configure a MSPI XIP settings. |
| int | [mspi\_scramble\_config](#gacf287e08b6ce4898524884e8de22b806) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md) \*cfg) |
|  | Configure a MSPI scrambling settings. |
| int | [mspi\_timing\_config](#gaff82af1cfc99b9e78cec17ea27f79ab6) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) param\_mask, void \*cfg) |
|  | Configure a MSPI timing settings. |

## Detailed Description

MSPI Configure API.

## Enumeration Type Documentation

## [◆ ](#gaa25a7f97ab3437d4544832a0e7474f4a)mspi\_timing\_param

| enum [mspi\_timing\_param](#gaa25a7f97ab3437d4544832a0e7474f4a) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

Stub for timing parameter.

| Enumerator | |
| --- | --- |
| MSPI\_TIMING\_PARAM\_DUMMY |  |

## Function Documentation

## [◆ ](#ga46c2b98e99ecea045c1ecac4bdf3f087)mspi\_config()

| int mspi\_config | ( | const struct [mspi\_dt\_spec](structmspi__dt__spec.md) \* | *spec* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mspi.h](mspi_8h.md)>`

Configure a MSPI controller.

This routine provides a generic interface to override MSPI controller capabilities.

In the controller driver, one may implement this API to initialize or re-initialize their controller hardware. Additional SoC platform specific settings that are not in struct [mspi\_cfg](structmspi__cfg.md "MSPI controller configuration.") may be added to one's own binding(xxx,mspi-controller.yaml) so that one may derive the settings from DTS and configure it in this API. In general, these settings should not change during run-time. The bindings for

See also
:   [mspi\_cfg](structmspi__cfg.md "MSPI controller configuration.") can be found in mspi-controller.yaml.

Parameters
:   | spec | Pointer to MSPI DT information. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error, failed to configure device. |
    | -EINVAL | invalid capabilities, failed to configure device. |
    | -ENOTSUP | capability not supported by MSPI peripheral. |

## [◆ ](#gaa3c1eae8b3000c9bafcc26f14a8beb8b)mspi\_dev\_config()

| int mspi\_dev\_config | ( | const struct [device](structdevice.md) \* | *controller*, |
| --- | --- | --- | --- |
|  |  | const struct [mspi\_dev\_id](structmspi__dev__id.md) \* | *dev\_id*, |
|  |  | const enum [mspi\_dev\_cfg\_mask](group__mspi__interface.md#ga71c447d059acf7a8055c380243f3a647) | *param\_mask*, |
|  |  | const struct [mspi\_dev\_cfg](structmspi__dev__cfg.md) \* | *cfg* ) |

`#include <[mspi.h](mspi_8h.md)>`

Configure a MSPI controller with device specific parameters.

This routine provides a generic interface to override MSPI controller device specific settings that should be derived from device datasheets.

With

See also
:   [mspi\_dev\_id](structmspi__dev__id.md "MSPI device ID The controller can identify its devices and determine whether the access is allowed in...") defined [as](asm-macro-32-bit-gnu_8h.md#ac93d5f4341d561a6bd9864e880cffcf4) the [device](structdevice.md "Runtime device structure (in ROM) per driver instance.") index and CE GPIO from [device](structdevice.md "Runtime device structure (in ROM) per driver instance.") tree, the API supports multiple devices on the same controller instance. It is up to the controller driver implementation whether to support [device](structdevice.md "Runtime device structure (in ROM) per driver instance.") switching either by software or by hardware or not at all. If by software, the switching should be done in this API'[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) implementation. The implementation may also support individual parameter configurations specified by
:   [mspi\_dev\_cfg\_mask](group__mspi__interface.md#ga71c447d059acf7a8055c380243f3a647 "MSPI controller device specific configuration mask."). The [Settings](group__settings.md) within
:   [mspi\_dev\_cfg](structmspi__dev__cfg.md "MSPI controller device specific configuration.") don't typically change once the mode of operation is determined after the [device](structdevice.md "Runtime device structure (in ROM) per driver instance.") initialization. The bindings for
:   [mspi\_dev\_cfg](structmspi__dev__cfg.md "MSPI controller device specific configuration.") can be found in mspi-device.yaml.

Parameters
:   | controller | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | dev\_id | Pointer to the device ID structure from a device. |
    | param\_mask | Macro definition of what to be configured in cfg. |
    | cfg | The device runtime configuration for the MSPI controller. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error, failed to configure device. |
    | -EINVAL | invalid capabilities, failed to configure device. |
    | -ENOTSUP | capability not supported by MSPI peripheral. |

## [◆ ](#ga957b6ecd96c9f942f75bbe500898930d)mspi\_get\_channel\_status()

| int mspi\_get\_channel\_status | ( | const struct [device](structdevice.md) \* | *controller*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ch* ) |

`#include <[mspi.h](mspi_8h.md)>`

Query to see if it a channel is ready.

This routine allows to check if logical channel is ready before use. Note that queries for channels not supported will always return false.

Parameters
:   | controller | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | ch | the MSPI channel for which status is to be retrieved. |

Return values
:   | 0 | If MSPI channel is ready. |
    | --- | --- |

## [◆ ](#gacf287e08b6ce4898524884e8de22b806)mspi\_scramble\_config()

| int mspi\_scramble\_config | ( | const struct [device](structdevice.md) \* | *controller*, |
| --- | --- | --- | --- |
|  |  | const struct [mspi\_dev\_id](structmspi__dev__id.md) \* | *dev\_id*, |
|  |  | const struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md) \* | *cfg* ) |

`#include <[mspi.h](mspi_8h.md)>`

Configure a MSPI scrambling settings.

This routine provides a generic interface to configure the scrambling feature.

Parameters
:   | controller | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | dev\_id | Pointer to the device ID structure from a device. |
    | cfg | The controller scramble configuration for MSPI. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error, failed to configure device. |
    | -EINVAL | invalid capabilities, failed to configure device. |
    | -ENOTSUP | capability not supported by MSPI peripheral. |

## [◆ ](#gaff82af1cfc99b9e78cec17ea27f79ab6)mspi\_timing\_config()

| int mspi\_timing\_config | ( | const struct [device](structdevice.md) \* | *controller*, |
| --- | --- | --- | --- |
|  |  | const struct [mspi\_dev\_id](structmspi__dev__id.md) \* | *dev\_id*, |
|  |  | const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *param\_mask*, |
|  |  | void \* | *cfg* ) |

`#include <[mspi.h](mspi_8h.md)>`

Configure a MSPI timing settings.

This routine provides a generic interface to configure MSPI controller timing if necessary.

Parameters
:   | controller | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | dev\_id | Pointer to the device ID structure from a device. |
    | param\_mask | The macro definition of what should be configured in cfg. |
    | cfg | The controller timing configuration for MSPI. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error, failed to configure device. |
    | -EINVAL | invalid capabilities, failed to configure device. |
    | -ENOTSUP | capability not supported by MSPI peripheral. |

## [◆ ](#gab9d9104636d3c8167b5876b1bc4348ea)mspi\_xip\_config()

| int mspi\_xip\_config | ( | const struct [device](structdevice.md) \* | *controller*, |
| --- | --- | --- | --- |
|  |  | const struct [mspi\_dev\_id](structmspi__dev__id.md) \* | *dev\_id*, |
|  |  | const struct [mspi\_xip\_cfg](structmspi__xip__cfg.md) \* | *cfg* ) |

`#include <[mspi.h](mspi_8h.md)>`

Configure a MSPI XIP settings.

This routine provides a generic interface to configure the XIP feature.

Parameters
:   | controller | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | dev\_id | Pointer to the device ID structure from a device. |
    | cfg | The controller XIP configuration for MSPI. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error, failed to configure device. |
    | -EINVAL | invalid capabilities, failed to configure device. |
    | -ENOTSUP | capability not supported by MSPI peripheral. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
