---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.html
original_path: doxygen/html/structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data Struct Reference

`#include <[sensor_data_types.h](sensor__data__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [timestamp\_delta](#af453e301f5d1fdacf86daddc0c683498) |
| union { |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [values](#a7e34b93a4d3393b0c7c5918e6f6acb93) [4] |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [v](#a44471cf8b4de7faa0f4abf94e9fbb36e) [4] |  |
| struct { |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [x](#a3ff5782e8544602eb858e034a67667b6) |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [y](#a8631568f550497620734f27f2a96553d) |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [z](#acb44311f2b7bc97dae7b26a8256905cf) |  |
| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)   [w](#ad5fcab0aaca689606cbfacb7f6b13887) |  |
| } |  |
| }; |  |

## Field Documentation

## [◆ ](#a236fbdcaffa5456494b301a9e33a4271)[union]

| union { ... } [sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md) |
| --- |

## [◆ ](#af453e301f5d1fdacf86daddc0c683498)timestamp\_delta

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data::timestamp\_delta |
| --- |

## [◆ ](#a44471cf8b4de7faa0f4abf94e9fbb36e)v

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data::v[4] |
| --- |

## [◆ ](#a7e34b93a4d3393b0c7c5918e6f6acb93)values

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data::values[4] |
| --- |

## [◆ ](#ad5fcab0aaca689606cbfacb7f6b13887)w

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data::w |
| --- |

## [◆ ](#a3ff5782e8544602eb858e034a67667b6)x

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data::x |
| --- |

## [◆ ](#a8631568f550497620734f27f2a96553d)y

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data::y |
| --- |

## [◆ ](#acb44311f2b7bc97dae7b26a8256905cf)z

| [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data::z |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sensor\_data\_types.h](sensor__data__types_8h_source.md)

- [sensor\_game\_rotation\_vector\_data](structsensor__game__rotation__vector__data.md)
- [sensor\_game\_rotation\_vector\_sample\_data](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
