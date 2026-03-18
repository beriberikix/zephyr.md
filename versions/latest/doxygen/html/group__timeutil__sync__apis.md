---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__timeutil__sync__apis.html
original_path: doxygen/html/group__timeutil__sync__apis.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Time Synchronization APIs

[Utilities](group__utilities.md) » [Time Utility APIs](group__timeutil__apis.md)

| Data Structures | |
| --- | --- |
| struct | [timeutil\_sync\_config](structtimeutil__sync__config.md) |
|  | Immutable state for synchronizing two clocks. [More...](structtimeutil__sync__config.md#details) |
| struct | [timeutil\_sync\_instant](structtimeutil__sync__instant.md) |
|  | Representation of an instant in two time scales. [More...](structtimeutil__sync__instant.md#details) |
| struct | [timeutil\_sync\_state](structtimeutil__sync__state.md) |
|  | State required to convert instants between time scales. [More...](structtimeutil__sync__state.md#details) |

| Functions | |
| --- | --- |
| int | [timeutil\_sync\_state\_update](#gaa6926a23d1c4fbb61584e957d157bd62) (struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp, const struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) \*inst) |
|  | Record a new instant in the time synchronization state. |
| int | [timeutil\_sync\_state\_set\_skew](#ga01142931b299e848b0642634a0922be5) (struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp, float skew, const struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) \*base) |
|  | Update the state with a new skew and possibly base value. |
| float | [timeutil\_sync\_estimate\_skew](#gac4c25a1ed054a8a06c87d4df9c25ffc6) (const struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp) |
|  | Estimate the skew based on current state. |
| int | [timeutil\_sync\_ref\_from\_local](#ga75361d2bfd219f1e8107d635eb4ecc16) (const struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) local, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*refp) |
|  | Interpolate a reference timescale instant from a local instant. |
| int | [timeutil\_sync\_local\_from\_ref](#gad8ef92e5dc72bd26d765567134044400) (const struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ref, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*localp) |
|  | Interpolate a local timescale instant from a reference instant. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [timeutil\_sync\_skew\_to\_ppb](#gabe374cf629ee64b850cc49e954666d8d) (float skew) |
|  | Convert from a skew to an error in parts-per-billion. |

## Detailed Description

## Function Documentation

## [◆ ](#gac4c25a1ed054a8a06c87d4df9c25ffc6)timeutil\_sync\_estimate\_skew()

| float timeutil\_sync\_estimate\_skew | ( | const struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \* | *tsp* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[timeutil.h](timeutil_8h.md)>`

Estimate the skew based on current state.

Using the base and latest syncpoints from the state determine the skew of the local clock relative to the reference clock. See [timeutil\_sync\_state::skew](structtimeutil__sync__state.md#a39454807d207dddb2564d766c8ec2ea3 "The scale factor used to correct for clock skew.").

Parameters
:   | tsp | pointer to a time synchronization state. The base and latest syncpoints must be present and the latest syncpoint must be after the base point in the local time scale. |
    | --- | --- |

Returns
:   the estimated skew, or zero if skew could not be estimated.

## [◆ ](#gad8ef92e5dc72bd26d765567134044400)timeutil\_sync\_local\_from\_ref()

| int timeutil\_sync\_local\_from\_ref | ( | const struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \* | *tsp*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *ref*, |
|  |  | [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \* | *localp* ) |

`#include <[timeutil.h](timeutil_8h.md)>`

Interpolate a local timescale instant from a reference instant.

Parameters
:   | tsp | pointer to a time synchronization state. This must have a base and a skew installed. |
    | --- | --- |
    | ref | an instant measured in the reference timescale. This may be before or after the base instant. |
    | localp | where the corresponding instant in the local timescale should be stored. An interpolated value before local time 0 is provided without error. If interpolation fails the referenced object is not modified. |

Return values
:   | 0 | if successful with a skew of 1 |
    | --- | --- |
    | 1 | if successful with a skew not equal to 1 |
    | -EINVAL | - the time synchronization state is not adequately initialized - `refp` is null |

## [◆ ](#ga75361d2bfd219f1e8107d635eb4ecc16)timeutil\_sync\_ref\_from\_local()

| int timeutil\_sync\_ref\_from\_local | ( | const struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \* | *tsp*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *local*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *refp* ) |

`#include <[timeutil.h](timeutil_8h.md)>`

Interpolate a reference timescale instant from a local instant.

Parameters
:   | tsp | pointer to a time synchronization state. This must have a base and a skew installed. |
    | --- | --- |
    | local | an instant measured in the local timescale. This may be before or after the base instant. |
    | refp | where the corresponding instant in the reference timescale should be stored. A negative interpolated reference time produces an error. If interpolation fails the referenced object is not modified. |

Return values
:   | 0 | if interpolated using a skew of 1 |
    | --- | --- |
    | 1 | if interpolated using a skew not equal to 1 |
    | -EINVAL | - the times synchronization state is not adequately initialized - `refp` is null |
    | -ERANGE | the interpolated reference time would be negative |

## [◆ ](#gabe374cf629ee64b850cc49e954666d8d)timeutil\_sync\_skew\_to\_ppb()

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeutil\_sync\_skew\_to\_ppb | ( | float | *skew* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[timeutil.h](timeutil_8h.md)>`

Convert from a skew to an error in parts-per-billion.

A skew of 1.0 has zero error. A skew less than 1 has a positive error (clock is faster than it should be). A skew greater than one has a negative error (clock is slower than it should be).

Note that due to the limited precision of `float` compared with `double` the smallest error that can be represented is about 120 ppb. A "precise" time source may have error on the order of 2000 ppb.

A skew greater than 3.14748 may underflow the 32-bit representation; this represents a clock running at less than 1/3 its nominal rate.

Returns
:   skew error represented as parts-per-billion, or INT32\_MIN if the skew cannot be represented in the return type.

## [◆ ](#ga01142931b299e848b0642634a0922be5)timeutil\_sync\_state\_set\_skew()

| int timeutil\_sync\_state\_set\_skew | ( | struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \* | *tsp*, |
| --- | --- | --- | --- |
|  |  | float | *skew*, |
|  |  | const struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) \* | *base* ) |

`#include <[timeutil.h](timeutil_8h.md)>`

Update the state with a new skew and possibly base value.

Set the skew from a value retrieved from persistent storage, or calculated based on recent skew estimations including from [timeutil\_sync\_estimate\_skew()](#gac4c25a1ed054a8a06c87d4df9c25ffc6).

Optionally update the base timestamp. If the base is replaced the latest instant will be cleared until [timeutil\_sync\_state\_update()](#gaa6926a23d1c4fbb61584e957d157bd62) is invoked.

Parameters
:   | tsp | pointer to a time synchronization state. |
    | --- | --- |
    | skew | the skew to be used. The value must be positive and shouldn't be too far away from 1. |
    | base | optional new base to be set. If provided this becomes the base timestamp that will be used along with skew to convert between reference and local timescale instants. Setting the base clears the captured latest value. |

Returns
:   0 if skew was updated
:   -EINVAL if skew was not valid

## [◆ ](#gaa6926a23d1c4fbb61584e957d157bd62)timeutil\_sync\_state\_update()

| int timeutil\_sync\_state\_update | ( | struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \* | *tsp*, |
| --- | --- | --- | --- |
|  |  | const struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) \* | *inst* ) |

`#include <[timeutil.h](timeutil_8h.md)>`

Record a new instant in the time synchronization state.

Note that this updates only the latest persisted instant. The skew is not adjusted automatically.

Parameters
:   | tsp | pointer to a [timeutil\_sync\_state](structtimeutil__sync__state.md "State required to convert instants between time scales.") object. |
    | --- | --- |
    | inst | the new instant to be recorded. This becomes the base instant if there is no base instant, otherwise the value must be strictly after the base instant in both the reference and local time scales. |

Return values
:   | 0 | if installation succeeded in providing a new base |
    | --- | --- |
    | 1 | if installation provided a new latest instant |
    | -EINVAL | if the new instant is not compatible with the base instant |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
