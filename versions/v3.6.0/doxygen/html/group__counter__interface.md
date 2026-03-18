---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__counter__interface.html
original_path: doxygen/html/group__counter__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Counter Interface

[Device Driver APIs](group__io__interfaces.md)

Counter Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [counter\_alarm\_cfg](structcounter__alarm__cfg.md) |
|  | Alarm callback structure. [More...](structcounter__alarm__cfg.md#details) |
| struct | [counter\_top\_cfg](structcounter__top__cfg.md) |
|  | Top value configuration structure. [More...](structcounter__top__cfg.md#details) |
| struct | [counter\_config\_info](structcounter__config__info.md) |
|  | Structure with generic counter features. [More...](structcounter__config__info.md#details) |
| struct | [counter\_driver\_api](structcounter__driver__api.md) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [counter\_alarm\_callback\_t](#ga36c570c3e57e635753d163400e437b77)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks, void \*user\_data) |
|  | Alarm callback. |
| typedef void(\* | [counter\_top\_callback\_t](#ga3686fe1f86a53469659f79897e4e1baf)) (const struct [device](structdevice.md) \*dev, void \*user\_data) |
|  | Callback called when counter turns around. |
| typedef int(\* | [counter\_api\_start](#gab06ed037f6b0fb78ce04b7e7da989e81)) (const struct [device](structdevice.md) \*dev) |
| typedef int(\* | [counter\_api\_stop](#ga25ac7589f6501dada1e10b1980fca7de)) (const struct [device](structdevice.md) \*dev) |
| typedef int(\* | [counter\_api\_get\_value](#gac7a80581c4bda7dc76baeb6f6949ae5f)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ticks) |
| typedef int(\* | [counter\_api\_get\_value\_64](#gac7a403978e24becda59727790ba3ee8e)) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ticks) |
| typedef int(\* | [counter\_api\_set\_alarm](#gae3821860fa8a5c1197d6e304d2a4f387)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id, const struct [counter\_alarm\_cfg](structcounter__alarm__cfg.md) \*alarm\_cfg) |
| typedef int(\* | [counter\_api\_cancel\_alarm](#gac368afac6de0fe1f782fdb90e6f7c266)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id) |
| typedef int(\* | [counter\_api\_set\_top\_value](#gaa41eff3e6546583cc526830f9419aea8)) (const struct [device](structdevice.md) \*dev, const struct [counter\_top\_cfg](structcounter__top__cfg.md) \*cfg) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [counter\_api\_get\_pending\_int](#ga9224eba6be975e0747b4e13479b103ba)) (const struct [device](structdevice.md) \*dev) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [counter\_api\_get\_top\_value](#ga08ca9b32fbc96da83b75844f7b6218b2)) (const struct [device](structdevice.md) \*dev) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [counter\_api\_get\_guard\_period](#ga90b573190980a935d3984029831739a9)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| typedef int(\* | [counter\_api\_set\_guard\_period](#ga89822ff9da840421bbd59ab13664245d)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [counter\_api\_get\_freq](#ga939a7b305379577b3e10b315b89a4024)) (const struct [device](structdevice.md) \*dev) |

| Functions | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [counter\_is\_counting\_up](#gab95ae0e8d89e35e477cbf7d67e18016d) (const struct [device](structdevice.md) \*dev) |
|  | Function to check if counter is counting up. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [counter\_get\_num\_of\_channels](#ga0c9801b13275de0e1b93650bb1ca6a9d) (const struct [device](structdevice.md) \*dev) |
|  | Function to get number of alarm channels. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [counter\_get\_frequency](#ga8d3d6f856eef27a80cc2697931341af2) (const struct [device](structdevice.md) \*dev) |
|  | Function to get counter frequency. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [counter\_us\_to\_ticks](#gab73238b8d52ed763ff7abf91013b601b) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) us) |
|  | Function to convert microseconds to ticks. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [counter\_ticks\_to\_us](#ga9fbcb710091084e638c45f62c25d954c) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks) |
|  | Function to convert ticks to microseconds. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [counter\_get\_max\_top\_value](#gafab2a55048349e33c821a7f826615ea3) (const struct [device](structdevice.md) \*dev) |
|  | Function to retrieve maximum top value that can be set. |
| int | [counter\_start](#ga103e0673e31475adcd173601058c72cd) (const struct [device](structdevice.md) \*dev) |
|  | Start counter device in free running mode. |
| int | [counter\_stop](#gafaa8198ccff5ffc0491a1424d090c82d) (const struct [device](structdevice.md) \*dev) |
|  | Stop counter device. |
| int | [counter\_get\_value](#ga8f6b1b4ee7dc20e6230a22bfcb0e6f9d) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ticks) |
|  | Get current counter value. |
| int | [counter\_get\_value\_64](#ga2dcd0eb10d49c4e5e5024ed75a8e3e86) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ticks) |
|  | Get current counter 64-bit value. |
| int | [counter\_set\_channel\_alarm](#ga00a2857d993a84a56e8e222727f3d85e) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id, const struct [counter\_alarm\_cfg](structcounter__alarm__cfg.md) \*alarm\_cfg) |
|  | Set a single shot alarm on a channel. |
| int | [counter\_cancel\_channel\_alarm](#gade0bb97c0dfa03676d11ee47601d4cee) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id) |
|  | Cancel an alarm on a channel. |
| int | [counter\_set\_top\_value](#ga2d92f5564cdd1ecc56029c3a45e666f0) (const struct [device](structdevice.md) \*dev, const struct [counter\_top\_cfg](structcounter__top__cfg.md) \*cfg) |
|  | Set counter top value. |
| int | [counter\_get\_pending\_int](#ga3b74a79a09cbe3849658a746e7417a06) (const struct [device](structdevice.md) \*dev) |
|  | Function to get pending interrupts. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [counter\_get\_top\_value](#ga13d14903a03ab10062002a81b8302424) (const struct [device](structdevice.md) \*dev) |
|  | Function to retrieve current top value. |
| int | [counter\_set\_guard\_period](#gab6851411dabf191d3391715d632111b0) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Set guard period in counter ticks. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [counter\_get\_guard\_period](#ga55a101d237c8472ad5cacf65363c536f) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Return guard period. |

| Counter device capabilities | |
| --- | --- |
|  | |
| #define | [COUNTER\_CONFIG\_INFO\_COUNT\_UP](#ga8fa40ff6404936e5b05bb9c67871f70c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Counter count up flag. |

| Flags used by counter\_top\_cfg. | |
| --- | --- |
|  | |
| #define | [COUNTER\_TOP\_CFG\_DONT\_RESET](#ga9a30c647361912c2ce8e0566cf53dea7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Flag preventing counter reset when top value is changed. |
| #define | [COUNTER\_TOP\_CFG\_RESET\_WHEN\_LATE](#ga45562a4ddd743f74213a03d83a774b11)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Flag instructing counter to reset itself if changing top value results in counter going out of new top value bound. |

| Alarm configuration flags | |
| --- | --- |
| Used in alarm configuration structure ([counter\_alarm\_cfg](structcounter__alarm__cfg.md "counter_alarm_cfg")). | |
| #define | [COUNTER\_ALARM\_CFG\_ABSOLUTE](#ga4842d212424f92c5a3b39116ec6c2fd2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Counter alarm absolute value flag. |
| #define | [COUNTER\_ALARM\_CFG\_EXPIRE\_WHEN\_LATE](#ga87dffd2a1cadedfc30e7d39af547c336)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Alarm flag enabling immediate expiration when driver detects that absolute alarm was set too late. |

| Counter guard period flags | |
| --- | --- |
| Used by [counter\_set\_guard\_period](#gab6851411dabf191d3391715d632111b0) and [counter\_get\_guard\_period](#ga55a101d237c8472ad5cacf65363c536f). | |
| #define | [COUNTER\_GUARD\_PERIOD\_LATE\_TO\_SET](#ga6d955e603067b5c50e0fd9761e2e611d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Identifies guard period needed for detection of late setting of absolute alarm (see [counter\_set\_channel\_alarm](#ga00a2857d993a84a56e8e222727f3d85e)). |

## Detailed Description

Counter Interface.

## Macro Definition Documentation

## [◆ ](#ga4842d212424f92c5a3b39116ec6c2fd2)COUNTER\_ALARM\_CFG\_ABSOLUTE

| #define COUNTER\_ALARM\_CFG\_ABSOLUTE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[counter.h](counter_8h.md)>`

Counter alarm absolute value flag.

Ticks relation to counter value. If set ticks are treated as absolute value, else it is relative to the counter reading performed during the call.

## [◆ ](#ga87dffd2a1cadedfc30e7d39af547c336)COUNTER\_ALARM\_CFG\_EXPIRE\_WHEN\_LATE

| #define COUNTER\_ALARM\_CFG\_EXPIRE\_WHEN\_LATE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[counter.h](counter_8h.md)>`

Alarm flag enabling immediate expiration when driver detects that absolute alarm was set too late.

Alarm callback must be called from the same context as if it was set on time.

## [◆ ](#ga8fa40ff6404936e5b05bb9c67871f70c)COUNTER\_CONFIG\_INFO\_COUNT\_UP

| #define COUNTER\_CONFIG\_INFO\_COUNT\_UP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[counter.h](counter_8h.md)>`

Counter count up flag.

## [◆ ](#ga6d955e603067b5c50e0fd9761e2e611d)COUNTER\_GUARD\_PERIOD\_LATE\_TO\_SET

| #define COUNTER\_GUARD\_PERIOD\_LATE\_TO\_SET   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[counter.h](counter_8h.md)>`

Identifies guard period needed for detection of late setting of absolute alarm (see [counter\_set\_channel\_alarm](#ga00a2857d993a84a56e8e222727f3d85e)).

## [◆ ](#ga9a30c647361912c2ce8e0566cf53dea7)COUNTER\_TOP\_CFG\_DONT\_RESET

| #define COUNTER\_TOP\_CFG\_DONT\_RESET   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[counter.h](counter_8h.md)>`

Flag preventing counter reset when top value is changed.

If flags is set then counter is free running while top value is updated, otherwise counter is reset (see [counter\_set\_top\_value()](#ga2d92f5564cdd1ecc56029c3a45e666f0)).

## [◆ ](#ga45562a4ddd743f74213a03d83a774b11)COUNTER\_TOP\_CFG\_RESET\_WHEN\_LATE

| #define COUNTER\_TOP\_CFG\_RESET\_WHEN\_LATE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[counter.h](counter_8h.md)>`

Flag instructing counter to reset itself if changing top value results in counter going out of new top value bound.

See [COUNTER\_TOP\_CFG\_DONT\_RESET](#ga9a30c647361912c2ce8e0566cf53dea7).

## Typedef Documentation

## [◆ ](#ga36c570c3e57e635753d163400e437b77)counter\_alarm\_callback\_t

| typedef void(\* counter\_alarm\_callback\_t) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks, void \*user\_data) |
| --- |

`#include <[counter.h](counter_8h.md)>`

Alarm callback.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | chan\_id | Channel ID. |
    | ticks | Counter value that triggered the alarm. |
    | user\_data | User data. |

## [◆ ](#gac368afac6de0fe1f782fdb90e6f7c266)counter\_api\_cancel\_alarm

| typedef int(\* counter\_api\_cancel\_alarm) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id) |
| --- |

`#include <[counter.h](counter_8h.md)>`

## [◆ ](#ga939a7b305379577b3e10b315b89a4024)counter\_api\_get\_freq

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* counter\_api\_get\_freq) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[counter.h](counter_8h.md)>`

## [◆ ](#ga90b573190980a935d3984029831739a9)counter\_api\_get\_guard\_period

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* counter\_api\_get\_guard\_period) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| --- |

`#include <[counter.h](counter_8h.md)>`

## [◆ ](#ga9224eba6be975e0747b4e13479b103ba)counter\_api\_get\_pending\_int

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* counter\_api\_get\_pending\_int) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[counter.h](counter_8h.md)>`

## [◆ ](#ga08ca9b32fbc96da83b75844f7b6218b2)counter\_api\_get\_top\_value

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* counter\_api\_get\_top\_value) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[counter.h](counter_8h.md)>`

## [◆ ](#gac7a80581c4bda7dc76baeb6f6949ae5f)counter\_api\_get\_value

| typedef int(\* counter\_api\_get\_value) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ticks) |
| --- |

`#include <[counter.h](counter_8h.md)>`

## [◆ ](#gac7a403978e24becda59727790ba3ee8e)counter\_api\_get\_value\_64

| typedef int(\* counter\_api\_get\_value\_64) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ticks) |
| --- |

`#include <[counter.h](counter_8h.md)>`

## [◆ ](#gae3821860fa8a5c1197d6e304d2a4f387)counter\_api\_set\_alarm

| typedef int(\* counter\_api\_set\_alarm) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id, const struct [counter\_alarm\_cfg](structcounter__alarm__cfg.md) \*alarm\_cfg) |
| --- |

`#include <[counter.h](counter_8h.md)>`

## [◆ ](#ga89822ff9da840421bbd59ab13664245d)counter\_api\_set\_guard\_period

| typedef int(\* counter\_api\_set\_guard\_period) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| --- |

`#include <[counter.h](counter_8h.md)>`

## [◆ ](#gaa41eff3e6546583cc526830f9419aea8)counter\_api\_set\_top\_value

| typedef int(\* counter\_api\_set\_top\_value) (const struct [device](structdevice.md) \*dev, const struct [counter\_top\_cfg](structcounter__top__cfg.md) \*cfg) |
| --- |

`#include <[counter.h](counter_8h.md)>`

## [◆ ](#gab06ed037f6b0fb78ce04b7e7da989e81)counter\_api\_start

| typedef int(\* counter\_api\_start) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[counter.h](counter_8h.md)>`

## [◆ ](#ga25ac7589f6501dada1e10b1980fca7de)counter\_api\_stop

| typedef int(\* counter\_api\_stop) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[counter.h](counter_8h.md)>`

## [◆ ](#ga3686fe1f86a53469659f79897e4e1baf)counter\_top\_callback\_t

| typedef void(\* counter\_top\_callback\_t) (const struct [device](structdevice.md) \*dev, void \*user\_data) |
| --- |

`#include <[counter.h](counter_8h.md)>`

Callback called when counter turns around.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | user\_data | User data provided in [counter\_set\_top\_value](#ga2d92f5564cdd1ecc56029c3a45e666f0). |

## Function Documentation

## [◆ ](#gade0bb97c0dfa03676d11ee47601d4cee)counter\_cancel\_channel\_alarm()

| int counter\_cancel\_channel\_alarm | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *chan\_id* ) |

`#include <[counter.h](counter_8h.md)>`

Cancel an alarm on a channel.

Note
:   API is not thread safe.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | chan\_id | Channel ID. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | if request is not supported or the counter was not started yet. |

## [◆ ](#ga8d3d6f856eef27a80cc2697931341af2)counter\_get\_frequency()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) counter\_get\_frequency | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[counter.h](counter_8h.md)>`

Function to get counter frequency.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |

Returns
:   Frequency of the counter in Hz, or zero if the counter does not have a fixed frequency.

## [◆ ](#ga55a101d237c8472ad5cacf65363c536f)counter\_get\_guard\_period()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) counter\_get\_guard\_period | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

`#include <[counter.h](counter_8h.md)>`

Return guard period.

See also
:   [counter\_set\_guard\_period](#gab6851411dabf191d3391715d632111b0).

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | See [COUNTER\_GUARD\_PERIOD\_FLAGS](#COUNTER_GUARD_PERIOD_FLAGS). |

Returns
:   Guard period given in counter ticks or 0 if function or flags are not supported.

## [◆ ](#gafab2a55048349e33c821a7f826615ea3)counter\_get\_max\_top\_value()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) counter\_get\_max\_top\_value | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[counter.h](counter_8h.md)>`

Function to retrieve maximum top value that can be set.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |

Returns
:   Max top value.

## [◆ ](#ga0c9801b13275de0e1b93650bb1ca6a9d)counter\_get\_num\_of\_channels()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) counter\_get\_num\_of\_channels | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[counter.h](counter_8h.md)>`

Function to get number of alarm channels.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |

Returns
:   Number of alarm channels.

## [◆ ](#ga3b74a79a09cbe3849658a746e7417a06)counter\_get\_pending\_int()

| int counter\_get\_pending\_int | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[counter.h](counter_8h.md)>`

Function to get pending interrupts.

The purpose of this function is to return the interrupt status register for the device. This is especially useful when waking up from low power states to check the wake up source.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Return values
:   | 1 | if any counter interrupt is pending. |
    | --- | --- |
    | 0 | if no counter interrupt is pending. |

## [◆ ](#ga13d14903a03ab10062002a81b8302424)counter\_get\_top\_value()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) counter\_get\_top\_value | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[counter.h](counter_8h.md)>`

Function to retrieve current top value.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |

Returns
:   Top value.

## [◆ ](#ga8f6b1b4ee7dc20e6230a22bfcb0e6f9d)counter\_get\_value()

| int counter\_get\_value | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *ticks* ) |

`#include <[counter.h](counter_8h.md)>`

Get current counter value.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | ticks | Pointer to where to store the current counter value |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | Negative | error code on failure getting the counter value |

## [◆ ](#ga2dcd0eb10d49c4e5e5024ed75a8e3e86)counter\_get\_value\_64()

| int counter\_get\_value\_64 | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *ticks* ) |

`#include <[counter.h](counter_8h.md)>`

Get current counter 64-bit value.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | ticks | Pointer to where to store the current counter value |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | Negative | error code on failure getting the counter value |

## [◆ ](#gab95ae0e8d89e35e477cbf7d67e18016d)counter\_is\_counting\_up()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) counter\_is\_counting\_up | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[counter.h](counter_8h.md)>`

Function to check if counter is counting up.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if counter is counting up. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if counter is counting down. |

## [◆ ](#ga00a2857d993a84a56e8e222727f3d85e)counter\_set\_channel\_alarm()

| int counter\_set\_channel\_alarm | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *chan\_id*, |
|  |  | const struct [counter\_alarm\_cfg](structcounter__alarm__cfg.md) \* | *alarm\_cfg* ) |

`#include <[counter.h](counter_8h.md)>`

Set a single shot alarm on a channel.

After expiration alarm can be set again, disabling is not needed. When alarm expiration handler is called, channel is considered available and can be set again in that context.

Note
:   API is not thread safe.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | chan\_id | Channel ID. |
    | alarm\_cfg | Alarm configuration. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | if request is not supported (device does not support interrupts or requested channel). |
    | -EINVAL | if alarm settings are invalid. |
    | -ETIME | if absolute alarm was set too late. |
    | -EBUSY | if alarm is already active. |

## [◆ ](#gab6851411dabf191d3391715d632111b0)counter\_set\_guard\_period()

| int counter\_set\_guard\_period | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *ticks*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

`#include <[counter.h](counter_8h.md)>`

Set guard period in counter ticks.

When setting an absolute alarm value close to the current counter value there is a risk that the counter will have counted past the given absolute value before the driver manages to activate the alarm. If this would go unnoticed then the alarm would only expire after the timer has wrapped and reached the given absolute value again after a full timer period. This could take a long time in case of a 32 bit timer. Setting a sufficiently large guard period will help the driver detect unambiguously whether it is late or not.

The guard period should be as many counter ticks as the driver will need at most to actually activate the alarm after the driver API has been called. If the driver finds that the counter has just passed beyond the given absolute tick value but is still close enough to fall within the guard period, it will assume that it is "late", i.e. that the intended expiry time has already passed. Depending on the [COUNTER\_ALARM\_CFG\_EXPIRE\_WHEN\_LATE](#ga87dffd2a1cadedfc30e7d39af547c336) flag the driver will either ignore the alarm or expire it immediately in such a case.

If, however, the counter is past the given absolute tick value but outside the guard period, then the driver will assume that this is intentional and let the counter wrap around to/from zero before it expires.

More precisely:

- When counting upwards (see [COUNTER\_CONFIG\_INFO\_COUNT\_UP](#ga8fa40ff6404936e5b05bb9c67871f70c)) the given absolute tick value must be above (now + guard\_period) % top\_value to be accepted by the driver.
- When counting downwards, the given absolute tick value must be less than (now + top\_value - guard\_period) % top\_value to be accepted.

Examples:

- counting upwards, now = 4950, top value = 5000, guard period = 100: absolute tick value >= (4950 + 100) % 5000 = 50
- counting downwards, now = 50, top value = 5000, guard period = 100: absolute tick value <= (50 + 5000 - \* 100) % 5000 = 4950

If you need only short alarm periods, you can set the guard period very high (e.g. half of the counter top value) which will make it highly unlikely that the counter will ever unintentionally wrap.

The guard period is set to 0 on initialization (no protection).

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | ticks | Guard period in counter ticks. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | See [COUNTER\_GUARD\_PERIOD\_FLAGS](#COUNTER_GUARD_PERIOD_FLAGS). |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | -ENOTSUP | if function or flags are not supported. |
    | -EINVAL | if ticks value is invalid. |

## [◆ ](#ga2d92f5564cdd1ecc56029c3a45e666f0)counter\_set\_top\_value()

| int counter\_set\_top\_value | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [counter\_top\_cfg](structcounter__top__cfg.md) \* | *cfg* ) |

`#include <[counter.h](counter_8h.md)>`

Set counter top value.

Function sets top value and optionally resets the counter to 0 or top value depending on counter direction. On turnaround, counter can be reset and optional callback is periodically called. Top value can only be changed when there is no active channel alarm.

[COUNTER\_TOP\_CFG\_DONT\_RESET](#ga9a30c647361912c2ce8e0566cf53dea7) prevents counter reset. When counter is running while top value is updated, it is possible that counter progresses outside the new top value. In that case, error is returned and optionally driver can reset the counter (see [COUNTER\_TOP\_CFG\_RESET\_WHEN\_LATE](#ga45562a4ddd743f74213a03d83a774b11)).

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | cfg | Configuration. Cannot be NULL. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | if request is not supported (e.g. top value cannot be changed or counter cannot/must be reset during top value update). |
    | -EBUSY | if any alarm is active. |
    | -ETIME | if [COUNTER\_TOP\_CFG\_DONT\_RESET](#ga9a30c647361912c2ce8e0566cf53dea7) was set and new top value is smaller than current counter value (counter counting up). |

## [◆ ](#ga103e0673e31475adcd173601058c72cd)counter\_start()

| int counter\_start | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[counter.h](counter_8h.md)>`

Start counter device in free running mode.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | Negative | errno code if failure. |

## [◆ ](#gafaa8198ccff5ffc0491a1424d090c82d)counter\_stop()

| int counter\_stop | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[counter.h](counter_8h.md)>`

Stop counter device.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | if the device doesn't support stopping the counter. |

## [◆ ](#ga9fbcb710091084e638c45f62c25d954c)counter\_ticks\_to\_us()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) counter\_ticks\_to\_us | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *ticks* ) |

`#include <[counter.h](counter_8h.md)>`

Function to convert ticks to microseconds.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    | [in] | ticks | Ticks. |

Returns
:   Converted microseconds.

## [◆ ](#gab73238b8d52ed763ff7abf91013b601b)counter\_us\_to\_ticks()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) counter\_us\_to\_ticks | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *us* ) |

`#include <[counter.h](counter_8h.md)>`

Function to convert microseconds to ticks.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    | [in] | us | Microseconds. |

Returns
:   Converted ticks. Ticks will be saturated if exceed 32 bits.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
