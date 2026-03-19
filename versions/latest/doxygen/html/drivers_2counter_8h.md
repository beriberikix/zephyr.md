---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2counter_8h.html
original_path: doxygen/html/drivers_2counter_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

counter.h File Reference

Public API for counter and timer drivers.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/sys_clock.h](sys__clock_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <zephyr/syscalls/counter.h>`

[Go to the source code of this file.](drivers_2counter_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [counter\_alarm\_cfg](structcounter__alarm__cfg.md) |
|  | Alarm callback structure. [More...](structcounter__alarm__cfg.md#details) |
| struct | [counter\_top\_cfg](structcounter__top__cfg.md) |
|  | Top value configuration structure. [More...](structcounter__top__cfg.md#details) |
| struct | [counter\_config\_info](structcounter__config__info.md) |
|  | Structure with generic counter features. [More...](structcounter__config__info.md#details) |
| struct | [counter\_driver\_api](structcounter__driver__api.md) |

| Macros | |
| --- | --- |
| Counter device capabilities | |
|  | |
| #define | [COUNTER\_CONFIG\_INFO\_COUNT\_UP](group__counter__interface.md#ga8fa40ff6404936e5b05bb9c67871f70c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Counter count up flag. |
| Flags used by counter\_top\_cfg. | |
|  | |
| #define | [COUNTER\_TOP\_CFG\_DONT\_RESET](group__counter__interface.md#ga9a30c647361912c2ce8e0566cf53dea7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Flag preventing counter reset when top value is changed. |
| #define | [COUNTER\_TOP\_CFG\_RESET\_WHEN\_LATE](group__counter__interface.md#ga45562a4ddd743f74213a03d83a774b11)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Flag instructing counter to reset itself if changing top value results in counter going out of new top value bound. |
| Alarm configuration flags | |
| Used in alarm configuration structure ([counter\_alarm\_cfg](structcounter__alarm__cfg.md "counter_alarm_cfg")). | |
| #define | [COUNTER\_ALARM\_CFG\_ABSOLUTE](group__counter__interface.md#ga4842d212424f92c5a3b39116ec6c2fd2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Counter alarm absolute value flag. |
| #define | [COUNTER\_ALARM\_CFG\_EXPIRE\_WHEN\_LATE](group__counter__interface.md#ga87dffd2a1cadedfc30e7d39af547c336)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Alarm flag enabling immediate expiration when driver detects that absolute alarm was set too late. |
| Counter guard period flags | |
| Used by [counter\_set\_guard\_period](group__counter__interface.md#gab6851411dabf191d3391715d632111b0 "counter_set_guard_period") and [counter\_get\_guard\_period](group__counter__interface.md#ga55a101d237c8472ad5cacf65363c536f "counter_get_guard_period"). | |
| #define | [COUNTER\_GUARD\_PERIOD\_LATE\_TO\_SET](group__counter__interface.md#ga6d955e603067b5c50e0fd9761e2e611d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Identifies guard period needed for detection of late setting of absolute alarm (see [counter\_set\_channel\_alarm](group__counter__interface.md#ga00a2857d993a84a56e8e222727f3d85e "counter_set_channel_alarm")). |

| Typedefs | |
| --- | --- |
| typedef void(\* | [counter\_alarm\_callback\_t](group__counter__interface.md#ga36c570c3e57e635753d163400e437b77)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks, void \*user\_data) |
|  | Alarm callback. |
| typedef void(\* | [counter\_top\_callback\_t](group__counter__interface.md#ga3686fe1f86a53469659f79897e4e1baf)) (const struct [device](structdevice.md) \*dev, void \*user\_data) |
|  | Callback called when counter turns around. |
| typedef int(\* | [counter\_api\_start](group__counter__interface.md#gab06ed037f6b0fb78ce04b7e7da989e81)) (const struct [device](structdevice.md) \*dev) |
| typedef int(\* | [counter\_api\_stop](group__counter__interface.md#ga25ac7589f6501dada1e10b1980fca7de)) (const struct [device](structdevice.md) \*dev) |
| typedef int(\* | [counter\_api\_get\_value](group__counter__interface.md#gac7a80581c4bda7dc76baeb6f6949ae5f)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ticks) |
| typedef int(\* | [counter\_api\_get\_value\_64](group__counter__interface.md#gac7a403978e24becda59727790ba3ee8e)) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ticks) |
| typedef int(\* | [counter\_api\_set\_alarm](group__counter__interface.md#gae3821860fa8a5c1197d6e304d2a4f387)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id, const struct [counter\_alarm\_cfg](structcounter__alarm__cfg.md) \*alarm\_cfg) |
| typedef int(\* | [counter\_api\_cancel\_alarm](group__counter__interface.md#gac368afac6de0fe1f782fdb90e6f7c266)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id) |
| typedef int(\* | [counter\_api\_set\_top\_value](group__counter__interface.md#gaa41eff3e6546583cc526830f9419aea8)) (const struct [device](structdevice.md) \*dev, const struct [counter\_top\_cfg](structcounter__top__cfg.md) \*cfg) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [counter\_api\_get\_pending\_int](group__counter__interface.md#ga9224eba6be975e0747b4e13479b103ba)) (const struct [device](structdevice.md) \*dev) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [counter\_api\_get\_top\_value](group__counter__interface.md#ga08ca9b32fbc96da83b75844f7b6218b2)) (const struct [device](structdevice.md) \*dev) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [counter\_api\_get\_guard\_period](group__counter__interface.md#ga90b573190980a935d3984029831739a9)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| typedef int(\* | [counter\_api\_set\_guard\_period](group__counter__interface.md#ga89822ff9da840421bbd59ab13664245d)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [counter\_api\_get\_freq](group__counter__interface.md#ga939a7b305379577b3e10b315b89a4024)) (const struct [device](structdevice.md) \*dev) |

| Functions | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [counter\_is\_counting\_up](group__counter__interface.md#gab95ae0e8d89e35e477cbf7d67e18016d) (const struct [device](structdevice.md) \*dev) |
|  | Function to check if counter is counting up. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [counter\_get\_num\_of\_channels](group__counter__interface.md#ga0c9801b13275de0e1b93650bb1ca6a9d) (const struct [device](structdevice.md) \*dev) |
|  | Function to get number of alarm channels. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [counter\_get\_frequency](group__counter__interface.md#ga8d3d6f856eef27a80cc2697931341af2) (const struct [device](structdevice.md) \*dev) |
|  | Function to get counter frequency. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [counter\_us\_to\_ticks](group__counter__interface.md#gab73238b8d52ed763ff7abf91013b601b) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) us) |
|  | Function to convert microseconds to ticks. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [counter\_ticks\_to\_us](group__counter__interface.md#ga9fbcb710091084e638c45f62c25d954c) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks) |
|  | Function to convert ticks to microseconds. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [counter\_get\_max\_top\_value](group__counter__interface.md#gafab2a55048349e33c821a7f826615ea3) (const struct [device](structdevice.md) \*dev) |
|  | Function to retrieve maximum top value that can be set. |
| int | [counter\_start](group__counter__interface.md#ga103e0673e31475adcd173601058c72cd) (const struct [device](structdevice.md) \*dev) |
|  | Start counter device in free running mode. |
| int | [counter\_stop](group__counter__interface.md#gafaa8198ccff5ffc0491a1424d090c82d) (const struct [device](structdevice.md) \*dev) |
|  | Stop counter device. |
| int | [counter\_get\_value](group__counter__interface.md#ga8f6b1b4ee7dc20e6230a22bfcb0e6f9d) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ticks) |
|  | Get current counter value. |
| int | [counter\_get\_value\_64](group__counter__interface.md#ga2dcd0eb10d49c4e5e5024ed75a8e3e86) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ticks) |
|  | Get current counter 64-bit value. |
| int | [counter\_set\_channel\_alarm](group__counter__interface.md#ga00a2857d993a84a56e8e222727f3d85e) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id, const struct [counter\_alarm\_cfg](structcounter__alarm__cfg.md) \*alarm\_cfg) |
|  | Set a single shot alarm on a channel. |
| int | [counter\_cancel\_channel\_alarm](group__counter__interface.md#gade0bb97c0dfa03676d11ee47601d4cee) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id) |
|  | Cancel an alarm on a channel. |
| int | [counter\_set\_top\_value](group__counter__interface.md#ga2d92f5564cdd1ecc56029c3a45e666f0) (const struct [device](structdevice.md) \*dev, const struct [counter\_top\_cfg](structcounter__top__cfg.md) \*cfg) |
|  | Set counter top value. |
| int | [counter\_get\_pending\_int](group__counter__interface.md#ga3b74a79a09cbe3849658a746e7417a06) (const struct [device](structdevice.md) \*dev) |
|  | Function to get pending interrupts. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [counter\_get\_top\_value](group__counter__interface.md#ga13d14903a03ab10062002a81b8302424) (const struct [device](structdevice.md) \*dev) |
|  | Function to retrieve current top value. |
| int | [counter\_set\_guard\_period](group__counter__interface.md#gab6851411dabf191d3391715d632111b0) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Set guard period in counter ticks. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [counter\_get\_guard\_period](group__counter__interface.md#ga55a101d237c8472ad5cacf65363c536f) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Return guard period. |

## Detailed Description

Public API for counter and timer drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [counter.h](drivers_2counter_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
