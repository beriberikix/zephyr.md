---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsensor__q31__data_1_1sensor__q31__sample__data.html
original_path: doxygen/html/structsensor__q31__data_1_1sensor__q31__sample__data.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_q31\_data::sensor\_q31\_sample\_data Struct Reference

`#include <[sensor_data_types.h](sensor__data__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [timestamp\_delta](#afdf41c27c4f3f55c3ed18c73ab8b6183) |
| union { |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [value](#afd73a2b1b6e4e262e89e242853f4ef23) |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [light](#a7ae2d145a778a72322a78ed433781a0d) |  |
|  | Unit: lux. [More...](#a7ae2d145a778a72322a78ed433781a0d) |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [pressure](#ae07081204f6c01334ea9f2e970879b72) |  |
|  | Unit: kilopascal. [More...](#ae07081204f6c01334ea9f2e970879b72) |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [temperature](#a8101423f27270dcee7a356cabcc4d9dd) |  |
|  | Unit: degrees Celsius. [More...](#a8101423f27270dcee7a356cabcc4d9dd) |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [percent](#a39f4f4bf64dd49ff2fe027f6e8f8a04d) |  |
|  | Unit: percent. [More...](#a39f4f4bf64dd49ff2fe027f6e8f8a04d) |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [distance](#ad5d6a48016d474635c0f8a829915a8d2) |  |
|  | Unit: meters. [More...](#ad5d6a48016d474635c0f8a829915a8d2) |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [density](#a2ed468c4be6417f0ea2bb324560e622d) |  |
|  | Unit: ug/m^3. [More...](#a2ed468c4be6417f0ea2bb324560e622d) |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [density\_ppm](#a1493dc66c9d6e4782aed2ddadd74e178) |  |
|  | Unit: parts per million. [More...](#a1493dc66c9d6e4782aed2ddadd74e178) |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [density\_ppb](#a215aab449c2b5ee8cf32d971aa5e7708) |  |
|  | Unit: parts per billion. [More...](#a215aab449c2b5ee8cf32d971aa5e7708) |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [resistance](#aeb66bf289c9e17ac6473eb69c22d4eb3) |  |
|  | Unit: ohms. [More...](#aeb66bf289c9e17ac6473eb69c22d4eb3) |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [voltage](#af63a2f7a618c8ff17be31a0543920525) |  |
|  | Unit: volts. [More...](#af63a2f7a618c8ff17be31a0543920525) |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [current](#a60f0af8beb207f90ed916fe445525fed) |  |
|  | Unit: amps. [More...](#a60f0af8beb207f90ed916fe445525fed) |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [power](#a428adc52033ba50b871c8986e55b06af) |  |
|  | Unit: watts. [More...](#a428adc52033ba50b871c8986e55b06af) |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [angle](#a9e58a7ea902e27b02b34cc8f619aca96) |  |
|  | Unit: degrees. [More...](#a9e58a7ea902e27b02b34cc8f619aca96) |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [electric\_charge](#aafb3c0aa55c129b310525f7181b59d51) |  |
|  | Unit: mAh. [More...](#aafb3c0aa55c129b310525f7181b59d51) |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [humidity](#ac0d247952ae488af354fa1462a014d1d) |  |
|  | Unit: RH. [More...](#ac0d247952ae488af354fa1462a014d1d) |
| }; |  |

## Field Documentation

## [◆ ](#ad573c7c15520712fce7d6789fd68df04)[union]

| union { ... } [sensor\_q31\_data::sensor\_q31\_sample\_data](structsensor__q31__data_1_1sensor__q31__sample__data.md) |
| --- |

## [◆ ](#a9e58a7ea902e27b02b34cc8f619aca96)angle

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_q31\_data::sensor\_q31\_sample\_data::angle |
| --- |

Unit: degrees.

## [◆ ](#a60f0af8beb207f90ed916fe445525fed)current

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_q31\_data::sensor\_q31\_sample\_data::current |
| --- |

Unit: amps.

## [◆ ](#a2ed468c4be6417f0ea2bb324560e622d)density

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_q31\_data::sensor\_q31\_sample\_data::density |
| --- |

Unit: ug/m^3.

## [◆ ](#a215aab449c2b5ee8cf32d971aa5e7708)density\_ppb

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_q31\_data::sensor\_q31\_sample\_data::density\_ppb |
| --- |

Unit: parts per billion.

## [◆ ](#a1493dc66c9d6e4782aed2ddadd74e178)density\_ppm

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_q31\_data::sensor\_q31\_sample\_data::density\_ppm |
| --- |

Unit: parts per million.

## [◆ ](#ad5d6a48016d474635c0f8a829915a8d2)distance

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_q31\_data::sensor\_q31\_sample\_data::distance |
| --- |

Unit: meters.

## [◆ ](#aafb3c0aa55c129b310525f7181b59d51)electric\_charge

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_q31\_data::sensor\_q31\_sample\_data::electric\_charge |
| --- |

Unit: mAh.

## [◆ ](#ac0d247952ae488af354fa1462a014d1d)humidity

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_q31\_data::sensor\_q31\_sample\_data::humidity |
| --- |

Unit: RH.

## [◆ ](#a7ae2d145a778a72322a78ed433781a0d)light

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_q31\_data::sensor\_q31\_sample\_data::light |
| --- |

Unit: lux.

## [◆ ](#a39f4f4bf64dd49ff2fe027f6e8f8a04d)percent

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_q31\_data::sensor\_q31\_sample\_data::percent |
| --- |

Unit: percent.

## [◆ ](#a428adc52033ba50b871c8986e55b06af)power

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_q31\_data::sensor\_q31\_sample\_data::power |
| --- |

Unit: watts.

## [◆ ](#ae07081204f6c01334ea9f2e970879b72)pressure

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_q31\_data::sensor\_q31\_sample\_data::pressure |
| --- |

Unit: kilopascal.

## [◆ ](#aeb66bf289c9e17ac6473eb69c22d4eb3)resistance

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_q31\_data::sensor\_q31\_sample\_data::resistance |
| --- |

Unit: ohms.

## [◆ ](#a8101423f27270dcee7a356cabcc4d9dd)temperature

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_q31\_data::sensor\_q31\_sample\_data::temperature |
| --- |

Unit: degrees Celsius.

## [◆ ](#afdf41c27c4f3f55c3ed18c73ab8b6183)timestamp\_delta

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sensor\_q31\_data::sensor\_q31\_sample\_data::timestamp\_delta |
| --- |

## [◆ ](#afd73a2b1b6e4e262e89e242853f4ef23)value

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_q31\_data::sensor\_q31\_sample\_data::value |
| --- |

## [◆ ](#af63a2f7a618c8ff17be31a0543920525)voltage

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_q31\_data::sensor\_q31\_sample\_data::voltage |
| --- |

Unit: volts.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sensor\_data\_types.h](sensor__data__types_8h_source.md)

- [sensor\_q31\_data](structsensor__q31__data.md)
- [sensor\_q31\_sample\_data](structsensor__q31__data_1_1sensor__q31__sample__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
