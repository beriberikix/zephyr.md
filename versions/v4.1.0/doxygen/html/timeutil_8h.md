---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/timeutil_8h.html
original_path: doxygen/html/timeutil_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

timeutil.h File Reference

Utilities supporting operation on time data structures.
[More...](#details)

`#include <time.h>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](timeutil_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [timeutil\_sync\_config](structtimeutil__sync__config.md) |
|  | Immutable state for synchronizing two clocks. [More...](structtimeutil__sync__config.md#details) |
| struct | [timeutil\_sync\_instant](structtimeutil__sync__instant.md) |
|  | Representation of an instant in two time scales. [More...](structtimeutil__sync__instant.md#details) |
| struct | [timeutil\_sync\_state](structtimeutil__sync__state.md) |
|  | State required to convert instants between time scales. [More...](structtimeutil__sync__state.md#details) |

| Macros | |
| --- | --- |
| #define | [TIME\_UTILS\_BASE\_YEAR](group__timeutil__repr__apis.md#gaa61359e3ffe7df1994a9265a66834385)   1900 |

| Functions | |
| --- | --- |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [timeutil\_timegm64](group__timeutil__repr__apis.md#gac4d2957df896a77eb317e10318adf481) (const struct [tm](structtm.md) \*[tm](structtm.md)) |
|  | Convert broken-down time to a POSIX epoch offset in seconds. |
| int | [timeutil\_sync\_state\_update](group__timeutil__sync__apis.md#gaa6926a23d1c4fbb61584e957d157bd62) (struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp, const struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) \*inst) |
|  | Record a new instant in the time synchronization state. |
| int | [timeutil\_sync\_state\_set\_skew](group__timeutil__sync__apis.md#ga01142931b299e848b0642634a0922be5) (struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp, float skew, const struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) \*base) |
|  | Update the state with a new skew and possibly base value. |
| float | [timeutil\_sync\_estimate\_skew](group__timeutil__sync__apis.md#gac4c25a1ed054a8a06c87d4df9c25ffc6) (const struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp) |
|  | Estimate the skew based on current state. |
| int | [timeutil\_sync\_ref\_from\_local](group__timeutil__sync__apis.md#ga75361d2bfd219f1e8107d635eb4ecc16) (const struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) local, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*refp) |
|  | Interpolate a reference timescale instant from a local instant. |
| int | [timeutil\_sync\_local\_from\_ref](group__timeutil__sync__apis.md#gad8ef92e5dc72bd26d765567134044400) (const struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ref, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*localp) |
|  | Interpolate a local timescale instant from a reference instant. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [timeutil\_sync\_skew\_to\_ppb](group__timeutil__sync__apis.md#gabe374cf629ee64b850cc49e954666d8d) (float skew) |
|  | Convert from a skew to an error in parts-per-billion. |

## Detailed Description

Utilities supporting operation on time data structures.

POSIX defines [gmtime()](lib_2libc_2minimal_2include_2time_8h.md#a4bc4ff58d4ac838a36ba939747e5833e) to convert from [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) to struct tm, but all inverse transformations are non-standard or require access to time zone information. timeutil\_timegm() implements the functionality of the GNU extension timegm() function, but changes the error value as `EOVERFLOW` is not a standard C error identifier.

[timeutil\_timegm64()](group__timeutil__repr__apis.md#gac4d2957df896a77eb317e10318adf481 "Convert broken-down time to a POSIX epoch offset in seconds.") is provided to support full precision conversion on platforms where `[time_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7)` is limited to 32 bits.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [timeutil.h](timeutil_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
