---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structtimeutil__sync__state.html
original_path: doxygen/html/structtimeutil__sync__state.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

timeutil\_sync\_state Struct Reference

[Utilities](group__utilities.md) » [Time Utility APIs](group__timeutil__apis.md) » [Time Synchronization APIs](group__timeutil__sync__apis.md)

State required to convert instants between time scales.
[More...](#details)

`#include <[timeutil.h](timeutil_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [timeutil\_sync\_config](structtimeutil__sync__config.md) \* | [cfg](#a2a22936f3ba24fcfb7704e2157ae3e96) |
|  | Pointer to reference and local rate information. |
| struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) | [base](#aadbd2ecd98197865e3a71daa8967ce99) |
|  | The base instant in both time scales. |
| struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) | [latest](#a49dc5405c4818a339a68ad6ef33aa4e8) |
|  | The most recent instant in both time scales. |
| float | [skew](#a39454807d207dddb2564d766c8ec2ea3) |
|  | The scale factor used to correct for clock skew. |

## Detailed Description

State required to convert instants between time scales.

This state in conjunction with functions that manipulate it capture the offset information necessary to convert between two timescales along with information that corrects for skew due to inaccuracies in clock rates.

State objects should be zero-initialized before use.

## Field Documentation

## [◆ ](#aadbd2ecd98197865e3a71daa8967ce99)base

| struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) timeutil\_sync\_state::base |
| --- |

The base instant in both time scales.

## [◆ ](#a2a22936f3ba24fcfb7704e2157ae3e96)cfg

| const struct [timeutil\_sync\_config](structtimeutil__sync__config.md)\* timeutil\_sync\_state::cfg |
| --- |

Pointer to reference and local rate information.

## [◆ ](#a49dc5405c4818a339a68ad6ef33aa4e8)latest

| struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) timeutil\_sync\_state::latest |
| --- |

The most recent instant in both time scales.

This is captured here to provide data for skew calculation.

## [◆ ](#a39454807d207dddb2564d766c8ec2ea3)skew

| float timeutil\_sync\_state::skew |
| --- |

The scale factor used to correct for clock skew.

The nominal rate for the local counter is assumed to be inaccurate but stable, i.e. it will generally be some parts-per-million faster or slower than specified.

A duration in observed local clock ticks must be multiplied by this value to produce a duration in ticks of a clock operating at the nominal local rate.

A zero value indicates that the skew has not been initialized. If the value is zero when [base](#aadbd2ecd98197865e3a71daa8967ce99) is initialized the skew will be set to 1. Otherwise the skew is assigned through [timeutil\_sync\_state\_set\_skew()](group__timeutil__sync__apis.md#ga01142931b299e848b0642634a0922be5 "Update the state with a new skew and possibly base value.").

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[timeutil.h](timeutil_8h_source.md)

- [timeutil\_sync\_state](structtimeutil__sync__state.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
