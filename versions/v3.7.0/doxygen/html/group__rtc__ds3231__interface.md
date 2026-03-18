---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__rtc__ds3231__interface.html
original_path: doxygen/html/group__rtc__ds3231__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

RTC DS3231 Interface

[Device Driver APIs](group__io__interfaces.md)

RTC DS3231 Driver-Specific API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [maxim\_ds3231\_alarm](structmaxim__ds3231__alarm.md) |
|  | Information defining the alarm configuration. [More...](structmaxim__ds3231__alarm.md#details) |
| struct | [maxim\_ds3231\_syncpoint](structmaxim__ds3231__syncpoint.md) |
|  | Register the RTC clock against system clocks. [More...](structmaxim__ds3231__syncpoint.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [maxim\_ds3231\_alarm\_callback\_handler\_t](#ga684b29dc1c11d8df698437f27e6d0403)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) syncclock, void \*user\_data) |
|  | Signature for DS3231 alarm callbacks. |
| typedef void(\* | [maxim\_ds3231\_notify\_callback](#ga59541c849327f388169ca3a15df0ba57)) (const struct [device](structdevice.md) \*dev, struct [sys\_notify](structsys__notify.md) \*notify, int res) |
|  | Signature used to notify a user of the DS3231 that an asynchronous operation has completed. |

| Functions | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [maxim\_ds3231\_read\_syncclock](#ga68e1512974db4b526a632e140fa7eed8) (const struct [device](structdevice.md) \*dev) |
|  | Read the local synchronization clock. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [maxim\_ds3231\_syncclock\_frequency](#ga6e4a3f34023be910d33fd7f89f81dba3) (const struct [device](structdevice.md) \*dev) |
|  | Get the frequency of the synchronization clock. |
| int | [maxim\_ds3231\_ctrl\_update](#ga1a41193eb70b147eb623ff07be3b3954) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) set\_bits, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clear\_bits) |
|  | Set and clear specific bits in the control register. |
| int | [maxim\_ds3231\_stat\_update](#ga1073100b5943141333de8cfd0cd8ac2b) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) set\_bits, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clear\_bits) |
|  | Read the ctrl\_stat register then set and clear bits in it. |
| int | [maxim\_ds3231\_get\_alarm](#gabc9bd9ff8a2107c08a7d9ca02c162be1) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, struct [maxim\_ds3231\_alarm](structmaxim__ds3231__alarm.md) \*cfg) |
|  | Read a DS3231 alarm configuration. |
| int | [maxim\_ds3231\_set\_alarm](#ga8f876ad2e16e88d80a2f914be3df49b1) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const struct [maxim\_ds3231\_alarm](structmaxim__ds3231__alarm.md) \*cfg) |
|  | Configure a DS3231 alarm. |
| int | [maxim\_ds3231\_synchronize](#gabdf39bc4983b12646ad3b18ccfc1a7dc) (const struct [device](structdevice.md) \*dev, struct [sys\_notify](structsys__notify.md) \*notify) |
|  | Synchronize the RTC against the local clock. |
| int | [maxim\_ds3231\_req\_syncpoint](#ga45656b5994c063b77d04f60c71d42c5b) (const struct [device](structdevice.md) \*dev, struct [k\_poll\_signal](structk__poll__signal.md) \*signal) |
|  | Request to update the synchronization point. |
| int | [maxim\_ds3231\_get\_syncpoint](#ga4e9fab406fd3b9b20c0c7011bfbb7a8a) (const struct [device](structdevice.md) \*dev, struct [maxim\_ds3231\_syncpoint](structmaxim__ds3231__syncpoint.md) \*syncpoint) |
|  | Retrieve the most recent synchronization point. |
| int | [maxim\_ds3231\_set](#ga485db29a3aca59000798d5ae16ad7041) (const struct [device](structdevice.md) \*dev, const struct [maxim\_ds3231\_syncpoint](structmaxim__ds3231__syncpoint.md) \*syncpoint, struct [sys\_notify](structsys__notify.md) \*notify) |
|  | Set the RTC to a time consistent with the provided synchronization. |
| int | [maxim\_ds3231\_check\_alarms](#gab2091298eb9b94da29ad79616b707bad) (const struct [device](structdevice.md) \*dev) |
|  | Check for and clear flags indicating that an alarm has fired. |

## Detailed Description

RTC DS3231 Driver-Specific API.

## Typedef Documentation

## [◆ ](#ga684b29dc1c11d8df698437f27e6d0403)maxim\_ds3231\_alarm\_callback\_handler\_t

| typedef void(\* maxim\_ds3231\_alarm\_callback\_handler\_t) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) syncclock, void \*user\_data) |
| --- |

`#include <[maxim_ds3231.h](maxim__ds3231_8h.md)>`

Signature for DS3231 alarm callbacks.

The alarm callback is invoked from the system work queue thread. At the point the callback is invoked the corresponding alarm flags will have been cleared from the device status register. The callback is permitted to invoke operations on the device.

Parameters
:   | dev | the device from which the callback originated |
    | --- | --- |
    | id | the alarm id |
    | syncclock | the value from [maxim\_ds3231\_read\_syncclock()](#ga68e1512974db4b526a632e140fa7eed8) at the time the alarm interrupt was processed. |
    | user\_data | the corresponding parameter from [maxim\_ds3231\_alarm::user\_data](structmaxim__ds3231__alarm.md#a192fb8c10246bfe466e74aafbb45d720 "User-provided pointer passed to alarm callback."). |

## [◆ ](#ga59541c849327f388169ca3a15df0ba57)maxim\_ds3231\_notify\_callback

| typedef void(\* maxim\_ds3231\_notify\_callback) (const struct [device](structdevice.md) \*dev, struct [sys\_notify](structsys__notify.md) \*notify, int res) |
| --- |

`#include <[maxim_ds3231.h](maxim__ds3231_8h.md)>`

Signature used to notify a user of the DS3231 that an asynchronous operation has completed.

Functions compatible with this type are subject to all the constraints of [sys\_notify\_generic\_callback](group__sys__notify__apis.md#ga2a9ffe35a5ad44fb7c5b00bb5c5c0499 "Generic signature used to notify of result completion by callback.").

Parameters
:   | dev | the DS3231 device pointer |
    | --- | --- |
    | notify | the notification structure provided in the call |
    | res | the result of the operation. |

## Function Documentation

## [◆ ](#gab2091298eb9b94da29ad79616b707bad)maxim\_ds3231\_check\_alarms()

| int maxim\_ds3231\_check\_alarms | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[maxim_ds3231.h](maxim__ds3231_8h.md)>`

Check for and clear flags indicating that an alarm has fired.

Returns a mask indicating alarms that are marked as having fired, and clears from stat the flags that it found set. Alarms that have been configured with a callback are not represented in the return value.

This API may be used when a persistent alarm has been programmed.

Note
:   This function is *supervisor*.

Parameters
:   | dev | the DS3231 device pointer. |
    | --- | --- |

Returns
:   a non-negative value that may have MAXIM\_DS3231\_ALARM1 and/or MAXIM\_DS3231\_ALARM2 set, or a negative error code.

## [◆ ](#ga1a41193eb70b147eb623ff07be3b3954)maxim\_ds3231\_ctrl\_update()

| int maxim\_ds3231\_ctrl\_update | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *set\_bits*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *clear\_bits* ) |

`#include <[maxim_ds3231.h](maxim__ds3231_8h.md)>`

Set and clear specific bits in the control register.

Note
:   This function assumes the device register cache is valid. It will not read the register value, and it will write to the device only if the value changes as a result of applying the set and clear changes.
:   Unlike [maxim\_ds3231\_stat\_update()](#ga1073100b5943141333de8cfd0cd8ac2b) the return value from this function indicates the register value after changes were made. That return value is cached for use in subsequent operations.
:   This function is *supervisor*.

Returns
:   the non-negative updated value of the register, or a negative error code from an I2C transaction.

## [◆ ](#gabc9bd9ff8a2107c08a7d9ca02c162be1)maxim\_ds3231\_get\_alarm()

| int maxim\_ds3231\_get\_alarm | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *id*, |
|  |  | struct [maxim\_ds3231\_alarm](structmaxim__ds3231__alarm.md) \* | *cfg* ) |

`#include <[maxim_ds3231.h](maxim__ds3231_8h.md)>`

Read a DS3231 alarm configuration.

The alarm configuration data is read from the device and reconstructed into the output parameter.

Note
:   This function is *supervisor*.

Parameters
:   | dev | the DS3231 device pointer. |
    | --- | --- |
    | id | the alarm index, which must be 0 (for the 1 s resolution alarm) or 1 (for the 1 min resolution alarm). |
    | cfg | a pointer to a structure into which the configured alarm data will be stored. |

Returns
:   a non-negative value indicating successful conversion, or a negative error code from an I2C transaction or invalid parameter.

## [◆ ](#ga4e9fab406fd3b9b20c0c7011bfbb7a8a)maxim\_ds3231\_get\_syncpoint()

| int maxim\_ds3231\_get\_syncpoint | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [maxim\_ds3231\_syncpoint](structmaxim__ds3231__syncpoint.md) \* | *syncpoint* ) |

`#include <[maxim_ds3231.h](maxim__ds3231_8h.md)>`

Retrieve the most recent synchronization point.

This function returns the synchronization data last captured using [maxim\_ds3231\_synchronize()](#gabdf39bc4983b12646ad3b18ccfc1a7dc).

Parameters
:   | dev | the DS3231 device pointer. |
    | --- | --- |
    | syncpoint | where to store the synchronization data. |

Return values
:   | non-negative | on success |
    | --- | --- |
    | -ENOENT | if no syncpoint has been captured |

## [◆ ](#ga68e1512974db4b526a632e140fa7eed8)maxim\_ds3231\_read\_syncclock()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) maxim\_ds3231\_read\_syncclock | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[maxim_ds3231.h](maxim__ds3231_8h.md)>`

Read the local synchronization clock.

Synchronization aligns the DS3231 real-time clock with a stable monotonic local clock which should have a frequency between 1 kHz and 1 MHz and be itself synchronized with the primary system time clock. The accuracy of the alignment and the maximum time between synchronization updates is affected by the resolution of this clock.

On some systems the hardware clock from k\_cycles\_get\_32() is suitable, but on others that clock advances too quickly. The frequency of the target-specific clock is provided by [maxim\_ds3231\_syncclock\_frequency()](#ga6e4a3f34023be910d33fd7f89f81dba3).

At this time the value is captured from [k\_uptime\_get\_32()](group__clock__apis.md#ga9253cfb7b46af4d8994349323ce9872b "Get system uptime (32-bit version)."); future kernel extensions may make a higher-resolution clock available.

Note
:   This function is *isr-ok*.

Parameters
:   | dev | the DS3231 device pointer |
    | --- | --- |

Returns
:   the current value of the synchronization clock.

## [◆ ](#ga45656b5994c063b77d04f60c71d42c5b)maxim\_ds3231\_req\_syncpoint()

| int maxim\_ds3231\_req\_syncpoint | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [k\_poll\_signal](structk__poll__signal.md) \* | *signal* ) |

`#include <[maxim_ds3231.h](maxim__ds3231_8h.md)>`

Request to update the synchronization point.

This is a variant of [maxim\_ds3231\_synchronize()](#gabdf39bc4983b12646ad3b18ccfc1a7dc) for use from user threads.

Parameters
:   | dev | the DS3231 device pointer. |
    | --- | --- |
    | signal | pointer to a valid and ready-to-be-signalled [k\_poll\_signal](structk__poll__signal.md). May be NULL to request a synchronization point be collected without notifying when it has been updated. |

Return values
:   | non-negative | on success |
    | --- | --- |
    | -EBUSY | if a synchronization or set is currently in progress |
    | -ENOTSUP | if the required interrupt is not configured |

## [◆ ](#ga485db29a3aca59000798d5ae16ad7041)maxim\_ds3231\_set()

| int maxim\_ds3231\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [maxim\_ds3231\_syncpoint](structmaxim__ds3231__syncpoint.md) \* | *syncpoint*, |
|  |  | struct [sys\_notify](structsys__notify.md) \* | *notify* ) |

`#include <[maxim_ds3231.h](maxim__ds3231_8h.md)>`

Set the RTC to a time consistent with the provided synchronization.

The RTC advances one tick per second with no access to sub-second precision, and setting the clock resets the internal countdown chain. This function implements the magic necessary to set the clock while retaining as much sub-second accuracy as possible. It requires a synchronization point that pairs sub-second resolution civil time with a local synchronization clock captured at the same instant. The set operation may take as long as 1 second to complete; notification of completion is provided through the `notify` parameter.

Note
:   This function is *supervisor*.

Parameters
:   | dev | the DS3231 device pointer. |
    | --- | --- |
    | syncpoint | the structure providing the synchronization point. |
    | notify | pointer to the object used to specify asynchronous function behavior and store completion information. |

Return values
:   | non-negative | on success |
    | --- | --- |
    | -EINVAL | if syncpoint or notify are null |
    | -ENOTSUP | if the required interrupt signal is not configured |
    | -EBUSY | if a synchronization or set is currently in progress |

## [◆ ](#ga8f876ad2e16e88d80a2f914be3df49b1)maxim\_ds3231\_set\_alarm()

| int maxim\_ds3231\_set\_alarm | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *id*, |
|  |  | const struct [maxim\_ds3231\_alarm](structmaxim__ds3231__alarm.md) \* | *cfg* ) |

`#include <[maxim_ds3231.h](maxim__ds3231_8h.md)>`

Configure a DS3231 alarm.

The alarm configuration is validated and stored into the device.

To cancel an alarm use [counter\_cancel\_channel\_alarm()](group__counter__interface.md#gade0bb97c0dfa03676d11ee47601d4cee "Cancel an alarm on a channel.").

Note
:   This function is *supervisor*.

Parameters
:   | dev | the DS3231 device pointer. |
    | --- | --- |
    | id | 0 Analog to counter index. `ALARM1` is 0 and has 1 s resolution, `ALARM2` is 1 and has 1 minute resolution. |
    | cfg | a pointer to the desired alarm configuration. Both alarms are configured; if only one is to change the application must supply the existing configuration for the other. |

Returns
:   a non-negative value on success, or a negative error code from an I2C transaction or an invalid parameter.

## [◆ ](#ga1073100b5943141333de8cfd0cd8ac2b)maxim\_ds3231\_stat\_update()

| int maxim\_ds3231\_stat\_update | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *set\_bits*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *clear\_bits* ) |

`#include <[maxim_ds3231.h](maxim__ds3231_8h.md)>`

Read the ctrl\_stat register then set and clear bits in it.

The content of the ctrl\_stat register will be read, then the set and clear bits applied and the result written back to the device (regardless of whether there appears to be a change in value).

OSF, A1F, and A2F will be written with 1s if the corresponding bits do not appear in either `set_bits` or `clear_bits`. This ensures that if any flag becomes set between the read and the write that indicator will not be cleared.

Note
:   Unlike [maxim\_ds3231\_ctrl\_update()](#ga1a41193eb70b147eb623ff07be3b3954) the return value from this function indicates the register value before any changes were made.
:   This function is *supervisor*.

Parameters
:   | dev | the DS3231 device pointer |
    | --- | --- |
    | set\_bits | bits to be set when writing back. Setting bits other than [MAXIM\_DS3231\_REG\_STAT\_EN32kHz](maxim__ds3231_8h.md#aa966f6de1e7662e66fac1d631b44d021 "MAXIM_DS3231_REG_STAT_EN32kHz") will have no effect. |
    | clear\_bits | bits to be cleared when writing back. Include the bits for the status flags you want to clear. |

Returns
:   the non-negative register value as originally read (disregarding the effect of clears and sets), or a negative error code from an I2C transaction.

## [◆ ](#ga6e4a3f34023be910d33fd7f89f81dba3)maxim\_ds3231\_syncclock\_frequency()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) maxim\_ds3231\_syncclock\_frequency | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[maxim_ds3231.h](maxim__ds3231_8h.md)>`

Get the frequency of the synchronization clock.

Provides the frequency of the clock used in [maxim\_ds3231\_read\_syncclock()](#ga68e1512974db4b526a632e140fa7eed8).

Parameters
:   | dev | the DS3231 device pointer |
    | --- | --- |

Returns
:   the frequency of the selected synchronization clock.

## [◆ ](#gabdf39bc4983b12646ad3b18ccfc1a7dc)maxim\_ds3231\_synchronize()

| int maxim\_ds3231\_synchronize | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [sys\_notify](structsys__notify.md) \* | *notify* ) |

`#include <[maxim_ds3231.h](maxim__ds3231_8h.md)>`

Synchronize the RTC against the local clock.

The RTC advances one tick per second with no access to sub-second precision. Synchronizing clocks at sub-second resolution requires enabling a 1pps signal then capturing the system clocks in a GPIO callback. This function provides that operation.

Synchronization is performed in asynchronously, and may take as long as 1 s to complete; notification of completion is provided through the `notify` parameter.

Applications should use [maxim\_ds3231\_get\_syncpoint()](#ga4e9fab406fd3b9b20c0c7011bfbb7a8a) to retrieve the synchronization data collected by this operation.

Note
:   This function is *supervisor*.

Parameters
:   | dev | the DS3231 device pointer. |
    | --- | --- |
    | notify | pointer to the object used to specify asynchronous function behavior and store completion information. |

Return values
:   | non-negative | on success |
    | --- | --- |
    | -EBUSY | if a synchronization or set is currently in progress |
    | -EINVAL | if notify is not provided |
    | -ENOTSUP | if the required interrupt is not configured |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
