---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__bap__broadcast.html
original_path: doxygen/html/group__bt__bap__broadcast.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

BAP Broadcast APIs

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md)

BAP Broadcast APIs.
[More...](#details)

| Topics | |
| --- | --- |
|  | [BAP Broadcast Sink APIs](group__bt__bap__broadcast__sink.md) |
|  | BAP Broadcast Sink APIs. |
|  | [BAP Broadcast Source APIs](group__bt__bap__broadcast__source.md) |
|  | BAP Broadcast Source APIs. |

| Data Structures | |
| --- | --- |
| struct | [bt\_bap\_base\_codec\_id](structbt__bap__base__codec__id.md) |
|  | Codec ID structure for a Broadcast Audio Source Endpoint (BASE). [More...](structbt__bap__base__codec__id.md#details) |
| struct | [bt\_bap\_base\_subgroup\_bis](structbt__bap__base__subgroup__bis.md) |
|  | BIS structure for each BIS in a Broadcast Audio Source Endpoint (BASE) subgroup. [More...](structbt__bap__base__subgroup__bis.md#details) |

| Functions | |
| --- | --- |
| const struct bt\_bap\_base \* | [bt\_bap\_base\_get\_base\_from\_ad](#ga29423a39d76ad16f0586d82a23c07ba7) (const struct [bt\_data](structbt__data.md) \*ad) |
|  | Generate a pointer to a BASE from periodic advertising data. |
| int | [bt\_bap\_base\_get\_size](#ga539f92b71ec34f0551ef6240d83b972e) (const struct bt\_bap\_base \*base) |
|  | Get the size of a BASE. |
| int | [bt\_bap\_base\_get\_pres\_delay](#gaf91f45bcf7df2f368c5abeb116b65dd0) (const struct bt\_bap\_base \*base) |
|  | Get the presentation delay value of a BASE. |
| int | [bt\_bap\_base\_get\_subgroup\_count](#gadcae0230168564da1ee8b3c577ce27d7) (const struct bt\_bap\_base \*base) |
|  | Get the subgroup count of a BASE. |
| int | [bt\_bap\_base\_get\_bis\_indexes](#ga6deab5a8b7a16ddf0c3685d4003694e1) (const struct bt\_bap\_base \*base, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*bis\_indexes) |
|  | Get all BIS indexes of a BASE. |
| int | [bt\_bap\_base\_foreach\_subgroup](#ga5e6e0b758409cbdde93c0f648ef5e5e8) (const struct bt\_bap\_base \*base, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\*func)(const struct bt\_bap\_base\_subgroup \*subgroup, void \*user\_data), void \*user\_data) |
|  | Iterate on all subgroups in the BASE. |
| int | [bt\_bap\_base\_get\_subgroup\_codec\_id](#gae75e05a002dee8336eb066ae8231ea0c) (const struct bt\_bap\_base\_subgroup \*subgroup, struct [bt\_bap\_base\_codec\_id](structbt__bap__base__codec__id.md) \*codec\_id) |
|  | Get the codec ID of a subgroup. |
| int | [bt\_bap\_base\_get\_subgroup\_codec\_data](#ga10e2e32dc2802ba55d55c77148331f6a) (const struct bt\_bap\_base\_subgroup \*subgroup, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data) |
|  | Get the codec configuration data of a subgroup. |
| int | [bt\_bap\_base\_get\_subgroup\_codec\_meta](#gafb9d9544f38c7ad2613fff1679eb1f0c) (const struct bt\_bap\_base\_subgroup \*subgroup, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*meta) |
|  | Get the codec metadata of a subgroup. |
| int | [bt\_bap\_base\_subgroup\_codec\_to\_codec\_cfg](#ga920e3409f1978b803bcf6bc8d05ac8f6) (const struct bt\_bap\_base\_subgroup \*subgroup, struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Store subgroup codec data in a [Codec config parsing APIs](group__bt__audio__codec__cfg.md "Codec config parsing APIs"). |
| int | [bt\_bap\_base\_get\_subgroup\_bis\_count](#ga051e1f8aa2faf3ba7a973356138fd2d3) (const struct bt\_bap\_base\_subgroup \*subgroup) |
|  | Get the BIS count of a subgroup. |
| int | [bt\_bap\_base\_subgroup\_get\_bis\_indexes](#ga37df3bf1e18d2d8e9388541217b2e366) (const struct bt\_bap\_base\_subgroup \*subgroup, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*bis\_indexes) |
|  | Get all BIS indexes of a subgroup. |
| int | [bt\_bap\_base\_subgroup\_foreach\_bis](#ga4f85ee43984cb2f3139b41da7b9b1aee) (const struct bt\_bap\_base\_subgroup \*subgroup, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\*func)(const struct [bt\_bap\_base\_subgroup\_bis](structbt__bap__base__subgroup__bis.md) \*bis, void \*user\_data), void \*user\_data) |
|  | Iterate on all BIS in the subgroup. |
| int | [bt\_bap\_base\_subgroup\_bis\_codec\_to\_codec\_cfg](#gaa5cb191df7807ea87f1fba1871ca8ebe) (const struct [bt\_bap\_base\_subgroup\_bis](structbt__bap__base__subgroup__bis.md) \*bis, struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Store BIS codec configuration data in a [Codec config parsing APIs](group__bt__audio__codec__cfg.md "Codec config parsing APIs"). |

## Detailed Description

BAP Broadcast APIs.

## Function Documentation

## [◆ ](#ga5e6e0b758409cbdde93c0f648ef5e5e8)bt\_bap\_base\_foreach\_subgroup()

| int bt\_bap\_base\_foreach\_subgroup | ( | const struct bt\_bap\_base \* | *base*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | *func*)(const struct bt\_bap\_base\_subgroup \*subgroup, void \*user\_data), |
|  |  | void \* | *user\_data* ) |

`#include <[bap.h](bap_8h.md)>`

Iterate on all subgroups in the BASE.

Parameters
:   | base | The BASE pointer |
    | --- | --- |
    | func | Callback function. Return true to continue iterating, or false to stop. |
    | user\_data | Userdata supplied to `func` |

Return values
:   | -EINVAL | if arguments are invalid |
    | --- | --- |
    | -ECANCELED | if iterating over the subgroups stopped prematurely by `func` |
    | 0 | if all subgroups were iterated |

## [◆ ](#ga29423a39d76ad16f0586d82a23c07ba7)bt\_bap\_base\_get\_base\_from\_ad()

| const struct bt\_bap\_base \* bt\_bap\_base\_get\_base\_from\_ad | ( | const struct [bt\_data](structbt__data.md) \* | *ad* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Generate a pointer to a BASE from periodic advertising data.

Parameters
:   | ad | The periodic advertising data |
    | --- | --- |

Return values
:   | NULL | if the data does not contain a BASE |
    | --- | --- |
    | Pointer | to a bt\_bap\_base structure |

## [◆ ](#ga6deab5a8b7a16ddf0c3685d4003694e1)bt\_bap\_base\_get\_bis\_indexes()

| int bt\_bap\_base\_get\_bis\_indexes | ( | const struct bt\_bap\_base \* | *base*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *bis\_indexes* ) |

`#include <[bap.h](bap_8h.md)>`

Get all BIS indexes of a BASE.

Parameters
:   | [in] | base | The BASE pointer |
    | --- | --- | --- |
    | [out] | bis\_indexes | 32-bit BIS index bitfield that will be populated |

Return values
:   | -EINVAL | if arguments are invalid |
    | --- | --- |
    | 0 | on success |

## [◆ ](#gaf91f45bcf7df2f368c5abeb116b65dd0)bt\_bap\_base\_get\_pres\_delay()

| int bt\_bap\_base\_get\_pres\_delay | ( | const struct bt\_bap\_base \* | *base* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Get the presentation delay value of a BASE.

Parameters
:   | base | The BASE pointer |
    | --- | --- |

Return values
:   | -EINVAL | if arguments are invalid |
    | --- | --- |
    | The | 24-bit presentation delay value |

## [◆ ](#ga539f92b71ec34f0551ef6240d83b972e)bt\_bap\_base\_get\_size()

| int bt\_bap\_base\_get\_size | ( | const struct bt\_bap\_base \* | *base* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Get the size of a BASE.

Parameters
:   | base | The BASE pointer |
    | --- | --- |

Return values
:   | -EINVAL | if arguments are invalid |
    | --- | --- |
    | The | size of the BASE |

## [◆ ](#ga051e1f8aa2faf3ba7a973356138fd2d3)bt\_bap\_base\_get\_subgroup\_bis\_count()

| int bt\_bap\_base\_get\_subgroup\_bis\_count | ( | const struct bt\_bap\_base\_subgroup \* | *subgroup* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Get the BIS count of a subgroup.

Parameters
:   | subgroup | The subgroup pointer |
    | --- | --- |

Return values
:   | -EINVAL | if arguments are invalid |
    | --- | --- |
    | The | 8-bit BIS count value |

## [◆ ](#ga10e2e32dc2802ba55d55c77148331f6a)bt\_bap\_base\_get\_subgroup\_codec\_data()

| int bt\_bap\_base\_get\_subgroup\_codec\_data | ( | const struct bt\_bap\_base\_subgroup \* | *subgroup*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *data* ) |

`#include <[bap.h](bap_8h.md)>`

Get the codec configuration data of a subgroup.

Parameters
:   | [in] | subgroup | The subgroup pointer |
    | --- | --- | --- |
    | [out] | data | Pointer that will point to the resulting codec configuration data |

Return values
:   | -EINVAL | if arguments are invalid |
    | --- | --- |
    | 0 | on success |

## [◆ ](#gae75e05a002dee8336eb066ae8231ea0c)bt\_bap\_base\_get\_subgroup\_codec\_id()

| int bt\_bap\_base\_get\_subgroup\_codec\_id | ( | const struct bt\_bap\_base\_subgroup \* | *subgroup*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_bap\_base\_codec\_id](structbt__bap__base__codec__id.md) \* | *codec\_id* ) |

`#include <[bap.h](bap_8h.md)>`

Get the codec ID of a subgroup.

Parameters
:   | [in] | subgroup | The subgroup pointer |
    | --- | --- | --- |
    | [out] | codec\_id | Pointer to the struct where the results are placed |

Return values
:   | -EINVAL | if arguments are invalid |
    | --- | --- |
    | 0 | on success |

## [◆ ](#gafb9d9544f38c7ad2613fff1679eb1f0c)bt\_bap\_base\_get\_subgroup\_codec\_meta()

| int bt\_bap\_base\_get\_subgroup\_codec\_meta | ( | const struct bt\_bap\_base\_subgroup \* | *subgroup*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *meta* ) |

`#include <[bap.h](bap_8h.md)>`

Get the codec metadata of a subgroup.

Parameters
:   | [in] | subgroup | The subgroup pointer |
    | --- | --- | --- |
    | [out] | meta | Pointer that will point to the resulting codec metadata |

Return values
:   | -EINVAL | if arguments are invalid |
    | --- | --- |
    | 0 | on success |

## [◆ ](#gadcae0230168564da1ee8b3c577ce27d7)bt\_bap\_base\_get\_subgroup\_count()

| int bt\_bap\_base\_get\_subgroup\_count | ( | const struct bt\_bap\_base \* | *base* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Get the subgroup count of a BASE.

Parameters
:   | base | The BASE pointer |
    | --- | --- |

Return values
:   | -EINVAL | if arguments are invalid |
    | --- | --- |
    | The | 8-bit subgroup count value |

## [◆ ](#gaa5cb191df7807ea87f1fba1871ca8ebe)bt\_bap\_base\_subgroup\_bis\_codec\_to\_codec\_cfg()

| int bt\_bap\_base\_subgroup\_bis\_codec\_to\_codec\_cfg | ( | const struct [bt\_bap\_base\_subgroup\_bis](structbt__bap__base__subgroup__bis.md) \* | *bis*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg* ) |

`#include <[bap.h](bap_8h.md)>`

Store BIS codec configuration data in a [Codec config parsing APIs](group__bt__audio__codec__cfg.md "Codec config parsing APIs").

This only sets the [Codec config parsing APIs](group__bt__audio__codec__cfg.md "Codec config parsing APIs") data and [Codec config parsing APIs](group__bt__audio__codec__cfg.md "Codec config parsing APIs") data\_len, but is useful to use the BIS codec configuration data with the bt\_audio\_codec\_cfg\_\* functions.

Parameters
:   | [in] | bis | The BIS pointer |
    | --- | --- | --- |
    | [out] | codec\_cfg | Pointer to the struct where the results are placed |

Return values
:   | -EINVAL | if arguments are invalid |
    | --- | --- |
    | -ENOMEM | if the `codec_cfg` cannot store the `subgroup` codec data |
    | 0 | on success |

## [◆ ](#ga920e3409f1978b803bcf6bc8d05ac8f6)bt\_bap\_base\_subgroup\_codec\_to\_codec\_cfg()

| int bt\_bap\_base\_subgroup\_codec\_to\_codec\_cfg | ( | const struct bt\_bap\_base\_subgroup \* | *subgroup*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg* ) |

`#include <[bap.h](bap_8h.md)>`

Store subgroup codec data in a [Codec config parsing APIs](group__bt__audio__codec__cfg.md "Codec config parsing APIs").

Parameters
:   | [in] | subgroup | The subgroup pointer |
    | --- | --- | --- |
    | [out] | codec\_cfg | Pointer to the struct where the results are placed |

Return values
:   | -EINVAL | if arguments are invalid |
    | --- | --- |
    | -ENOMEM | if the `codec_cfg` cannot store the `subgroup` codec data |
    | 0 | on success |

## [◆ ](#ga4f85ee43984cb2f3139b41da7b9b1aee)bt\_bap\_base\_subgroup\_foreach\_bis()

| int bt\_bap\_base\_subgroup\_foreach\_bis | ( | const struct bt\_bap\_base\_subgroup \* | *subgroup*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | *func*)(const struct [bt\_bap\_base\_subgroup\_bis](structbt__bap__base__subgroup__bis.md) \*bis, void \*user\_data), |
|  |  | void \* | *user\_data* ) |

`#include <[bap.h](bap_8h.md)>`

Iterate on all BIS in the subgroup.

Parameters
:   | subgroup | The subgroup pointer |
    | --- | --- |
    | func | Callback function. Return true to continue iterating, or false to stop. |
    | user\_data | Userdata supplied to `func` |

Return values
:   | -EINVAL | if arguments are invalid |
    | --- | --- |
    | -ECANCELED | if iterating over the subgroups stopped prematurely by `func` |
    | 0 | if all BIS were iterated |

## [◆ ](#ga37df3bf1e18d2d8e9388541217b2e366)bt\_bap\_base\_subgroup\_get\_bis\_indexes()

| int bt\_bap\_base\_subgroup\_get\_bis\_indexes | ( | const struct bt\_bap\_base\_subgroup \* | *subgroup*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *bis\_indexes* ) |

`#include <[bap.h](bap_8h.md)>`

Get all BIS indexes of a subgroup.

Parameters
:   | [in] | subgroup | The subgroup pointer |
    | --- | --- | --- |
    | [out] | bis\_indexes | 32-bit BIS index bitfield that will be populated |

Return values
:   | -EINVAL | if arguments are invalid |
    | --- | --- |
    | 0 | on success |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
