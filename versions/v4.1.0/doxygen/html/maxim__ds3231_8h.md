---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/maxim__ds3231_8h.html
original_path: doxygen/html/maxim__ds3231_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

maxim\_ds3231.h File Reference

Real-time clock control based on the DS3231 counter API.
[More...](#details)

`#include <time.h>`  
`#include <[zephyr/drivers/counter.h](drivers_2counter_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/notify.h](notify_8h_source.md)>`  
`#include <zephyr/syscalls/maxim_ds3231.h>`

[Go to the source code of this file.](maxim__ds3231_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [maxim\_ds3231\_alarm](structmaxim__ds3231__alarm.md) |
|  | Information defining the alarm configuration. [More...](structmaxim__ds3231__alarm.md#details) |
| struct | [maxim\_ds3231\_syncpoint](structmaxim__ds3231__syncpoint.md) |
|  | Register the RTC clock against system clocks. [More...](structmaxim__ds3231__syncpoint.md#details) |

| Macros | |
| --- | --- |
| #define | [MAXIM\_DS3231\_ALARM1](#aa4c7c4796b95c1565f1cbc89e3f8666c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Bit in ctrl or ctrl\_stat associated with alarm 1. |
| #define | [MAXIM\_DS3231\_ALARM2](#a6bfaaa0a0dabf27c2836d80a5b603e36)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Bit in ctrl or ctrl\_stat associated with alarm 2. |
| #define | [MAXIM\_DS3231\_REG\_CTRL\_A1IE](#a7a0c8cd9efebab0c1d393bbf724b48be)   [MAXIM\_DS3231\_ALARM1](#aa4c7c4796b95c1565f1cbc89e3f8666c) |
|  | ctrl bit for alarm 1 interrupt enable. |
| #define | [MAXIM\_DS3231\_REG\_CTRL\_A2IE](#a402938e78fe63caea36a719fc66a1d5a)   [MAXIM\_DS3231\_ALARM2](#a6bfaaa0a0dabf27c2836d80a5b603e36) |
|  | ctrl bit for alarm 2 interrupt enable. |
| #define | [MAXIM\_DS3231\_REG\_CTRL\_INTCN](#a3434c24e2058e8af1e5634ea81fa16d9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | ctrl bit for ISQ functionality. |
| #define | [MAXIM\_DS3231\_REG\_CTRL\_RS\_Pos](#a91f55e1d2e9fcc15a5a4a28b65904fc5)   3 |
|  | ctrl bit offset for square wave output frequency. |
| #define | [MAXIM\_DS3231\_REG\_CTRL\_RS\_Msk](#a81b83144c73488ae9d4bf39e5c49c383)   (0x03 << [MAXIM\_DS3231\_REG\_CTRL\_RS\_Pos](#a91f55e1d2e9fcc15a5a4a28b65904fc5)) |
|  | ctrl mask to isolate RS bits. |
| #define | [MAXIM\_DS3231\_REG\_CTRL\_RS\_1Hz](#ab85257cd6a6971702dfbdeca86b39018)   0x00 |
|  | ctrl RS field value for 1 Hz square wave. |
| #define | [MAXIM\_DS3231\_REG\_CTRL\_RS\_1KiHz](#a7e14bad3fb7439b128216effade29f5d)   0x01 |
|  | ctrl RS field value for 1024 Hz square wave. |
| #define | [MAXIM\_DS3231\_REG\_CTRL\_RS\_4KiHz](#a21e219fe89353341f9dd4634d0be4efa)   0x02 |
|  | ctrl RS field value for 4096 Hz square wave. |
| #define | [MAXIM\_DS3231\_REG\_CTRL\_RS\_8KiHz](#aa6069b89201545ca8c3bcdef952a1176)   0x03 |
|  | ctrl RS field value for 8192 Hz square wave. |
| #define | [MAXIM\_DS3231\_REG\_CTRL\_CONV](#ab3e3e38695c5375d24c55381263cc257)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | ctrl bit to write to trigger temperature conversion. |
| #define | [MAXIM\_DS3231\_REG\_CTRL\_BBSQW](#aae0c76ff6e883a79a4586c275469ef96)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | ctrl bit to write to enable square wave output in battery mode. |
| #define | [MAXIM\_DS3231\_REG\_CTRL\_EOSCn](#aabace2215a936b246329c2519291d876)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7), |
|  | ctrl bit to write to disable the oscillator. |
| #define | [MAXIM\_DS3231\_REG\_STAT\_A1F](#ac3321b05e01df54d607cec07e4f02824)   [MAXIM\_DS3231\_ALARM1](#aa4c7c4796b95c1565f1cbc89e3f8666c) |
|  | ctrl\_stat bit indicating alarm1 has triggered. |
| #define | [MAXIM\_DS3231\_REG\_STAT\_A2F](#a81df2ff1cbf0ac6ecbe2b80dbbe1b182)   [MAXIM\_DS3231\_ALARM2](#a6bfaaa0a0dabf27c2836d80a5b603e36) |
|  | ctrl\_stat bit indicating alarm2 has triggered. |
| #define | [MAXIM\_DS3231\_REG\_STAT\_BSY](#ad522b899503e0606a53aaf1f9c9c0d38)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Flag indicating a temperature conversion is in progress. |
| #define | [MAXIM\_DS3231\_REG\_STAT\_EN32kHz](#aa966f6de1e7662e66fac1d631b44d021)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Set to enable 32 KiHz open drain signal. |
| #define | [MAXIM\_DS3231\_REG\_STAT\_OSF](#afe205661d94e00c332404e4c7f6dd138)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Flag indicating the oscillator has been off since last cleared. |
| #define | [MAXIM\_DS3231\_ALARM\_FLAGS\_IGNSE](#a65bba3dabc99b5098ffe280590b2dbba)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Control alarm behavior on match in seconds field. |
| #define | [MAXIM\_DS3231\_ALARM\_FLAGS\_IGNMN](#a4be38828079d6eda3e952dee03c205e3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Control alarm behavior on match in minutes field. |
| #define | [MAXIM\_DS3231\_ALARM\_FLAGS\_IGNHR](#a2217d1d4d37b3d116f6d0fb4f6eb5f04)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Control alarm behavior on match in hours field. |
| #define | [MAXIM\_DS3231\_ALARM\_FLAGS\_IGNDA](#a8041898f159b2a4c2fc13d942e08058b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Control alarm behavior on match in day/date field. |
| #define | [MAXIM\_DS3231\_ALARM\_FLAGS\_DOW](#a92341088a6917efe124c946faa359d57)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Control match on day of week versus day of month. |
| #define | [MAXIM\_DS3231\_ALARM\_FLAGS\_AUTODISABLE](#a06f65bcbdbfde80613a193b27803ed95)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Indicates that the alarm should be disabled once it fires. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [maxim\_ds3231\_alarm\_callback\_handler\_t](group__rtc__ds3231__interface.md#ga684b29dc1c11d8df698437f27e6d0403)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) syncclock, void \*user\_data) |
|  | Signature for DS3231 alarm callbacks. |
| typedef void(\* | [maxim\_ds3231\_notify\_callback](group__rtc__ds3231__interface.md#ga59541c849327f388169ca3a15df0ba57)) (const struct [device](structdevice.md) \*dev, struct [sys\_notify](structsys__notify.md) \*notify, int res) |
|  | Signature used to notify a user of the DS3231 that an asynchronous operation has completed. |

| Functions | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [maxim\_ds3231\_read\_syncclock](group__rtc__ds3231__interface.md#ga68e1512974db4b526a632e140fa7eed8) (const struct [device](structdevice.md) \*dev) |
|  | Read the local synchronization clock. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [maxim\_ds3231\_syncclock\_frequency](group__rtc__ds3231__interface.md#ga6e4a3f34023be910d33fd7f89f81dba3) (const struct [device](structdevice.md) \*dev) |
|  | Get the frequency of the synchronization clock. |
| int | [maxim\_ds3231\_ctrl\_update](group__rtc__ds3231__interface.md#ga1a41193eb70b147eb623ff07be3b3954) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) set\_bits, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clear\_bits) |
|  | Set and clear specific bits in the control register. |
| int | [maxim\_ds3231\_stat\_update](group__rtc__ds3231__interface.md#ga1073100b5943141333de8cfd0cd8ac2b) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) set\_bits, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clear\_bits) |
|  | Read the ctrl\_stat register then set and clear bits in it. |
| int | [maxim\_ds3231\_get\_alarm](group__rtc__ds3231__interface.md#gabc9bd9ff8a2107c08a7d9ca02c162be1) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, struct [maxim\_ds3231\_alarm](structmaxim__ds3231__alarm.md) \*cfg) |
|  | Read a DS3231 alarm configuration. |
| int | [maxim\_ds3231\_set\_alarm](group__rtc__ds3231__interface.md#ga8f876ad2e16e88d80a2f914be3df49b1) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const struct [maxim\_ds3231\_alarm](structmaxim__ds3231__alarm.md) \*cfg) |
|  | Configure a DS3231 alarm. |
| int | [maxim\_ds3231\_synchronize](group__rtc__ds3231__interface.md#gabdf39bc4983b12646ad3b18ccfc1a7dc) (const struct [device](structdevice.md) \*dev, struct [sys\_notify](structsys__notify.md) \*notify) |
|  | Synchronize the RTC against the local clock. |
| int | [maxim\_ds3231\_req\_syncpoint](group__rtc__ds3231__interface.md#ga45656b5994c063b77d04f60c71d42c5b) (const struct [device](structdevice.md) \*dev, struct [k\_poll\_signal](structk__poll__signal.md) \*[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)) |
|  | Request to update the synchronization point. |
| int | [maxim\_ds3231\_get\_syncpoint](group__rtc__ds3231__interface.md#ga4e9fab406fd3b9b20c0c7011bfbb7a8a) (const struct [device](structdevice.md) \*dev, struct [maxim\_ds3231\_syncpoint](structmaxim__ds3231__syncpoint.md) \*syncpoint) |
|  | Retrieve the most recent synchronization point. |
| int | [maxim\_ds3231\_set](group__rtc__ds3231__interface.md#ga485db29a3aca59000798d5ae16ad7041) (const struct [device](structdevice.md) \*dev, const struct [maxim\_ds3231\_syncpoint](structmaxim__ds3231__syncpoint.md) \*syncpoint, struct [sys\_notify](structsys__notify.md) \*notify) |
|  | Set the RTC to a time consistent with the provided synchronization. |
| int | [maxim\_ds3231\_check\_alarms](group__rtc__ds3231__interface.md#gab2091298eb9b94da29ad79616b707bad) (const struct [device](structdevice.md) \*dev) |
|  | Check for and clear flags indicating that an alarm has fired. |

## Detailed Description

Real-time clock control based on the DS3231 counter API.

The [Maxim DS3231](https://www.maximintegrated.com/en/products/analog/real-time-clocks/DS3231.html) is a high-precision real-time clock with temperature-compensated crystal oscillator and support for configurable alarms.

The core Zephyr API to this device is as a counter, with the following limitations:

- counter\_read() and counter\_\*\_alarm() cannot be invoked from interrupt context, as they require communication with the device over an I2C bus.
- many other counter APIs, such as start/stop/set\_top\_value are not supported as the clock is always running.
- two alarm channels are supported but are not equally capable: channel 0 supports alarms at 1 s resolution, while channel 1 supports alarms at 1 minute resolution.

Most applications for this device will need to use the extended functionality exposed by this header to access the real-time-clock features. The majority of these functions must be invoked from supervisor mode.

## Macro Definition Documentation

## [◆ ](#aa4c7c4796b95c1565f1cbc89e3f8666c)MAXIM\_DS3231\_ALARM1

| #define MAXIM\_DS3231\_ALARM1   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Bit in ctrl or ctrl\_stat associated with alarm 1.

## [◆ ](#a6bfaaa0a0dabf27c2836d80a5b603e36)MAXIM\_DS3231\_ALARM2

| #define MAXIM\_DS3231\_ALARM2   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Bit in ctrl or ctrl\_stat associated with alarm 2.

## [◆ ](#a06f65bcbdbfde80613a193b27803ed95)MAXIM\_DS3231\_ALARM\_FLAGS\_AUTODISABLE

| #define MAXIM\_DS3231\_ALARM\_FLAGS\_AUTODISABLE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

Indicates that the alarm should be disabled once it fires.

Set the flag in the maxim\_ds3231\_alarm\_configuration::alarm\_flags field to cause the alarm to be disabled when the interrupt fires, prior to invoking the corresponding handler.

Leave false to allow the alarm to remain enabled so it will fire again on the next match.

## [◆ ](#a92341088a6917efe124c946faa359d57)MAXIM\_DS3231\_ALARM\_FLAGS\_DOW

| #define MAXIM\_DS3231\_ALARM\_FLAGS\_DOW   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

Control match on day of week versus day of month.

Set the flag to match on day of week; clear it to match on day of month.

Bit maps to DY/DTn in corresponding maxim\_ds3231\_alarm\_configuration::alarm\_flags.

## [◆ ](#a8041898f159b2a4c2fc13d942e08058b)MAXIM\_DS3231\_ALARM\_FLAGS\_IGNDA

| #define MAXIM\_DS3231\_ALARM\_FLAGS\_IGNDA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

Control alarm behavior on match in day/date field.

If clear the alarm fires only when the RTC day/date matches the alarm day/date, mediated by MAXIM\_DS3231\_ALARM\_FLAGS\_DAY. The bits for IGNHR, IGNMN, and IGNSE must be clear

If set the alarm day/date field is ignored and an alarm will be triggered based on IGNHR, IGNMN, and IGNSE.

Bit maps to A1M4 or A2M4 and is used in maxim\_ds3231\_alarm\_configuration::alarm\_flags.

## [◆ ](#a2217d1d4d37b3d116f6d0fb4f6eb5f04)MAXIM\_DS3231\_ALARM\_FLAGS\_IGNHR

| #define MAXIM\_DS3231\_ALARM\_FLAGS\_IGNHR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

Control alarm behavior on match in hours field.

If clear the alarm fires only when the RTC hours matches the alarm hours. The bits for IGNMN and IGNSE must be clear.

If set the alarm hours field is ignored and alarms will be triggered based on IGNMN and IGNSE. The bit for IGNDA must be set.

Bit maps to A1M3 or A2M3 and is used in maxim\_ds3231\_alarm\_configuration::alarm\_flags.

## [◆ ](#a4be38828079d6eda3e952dee03c205e3)MAXIM\_DS3231\_ALARM\_FLAGS\_IGNMN

| #define MAXIM\_DS3231\_ALARM\_FLAGS\_IGNMN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Control alarm behavior on match in minutes field.

If clear the alarm fires only when the RTC minutes matches the alarm minutes. The bit for IGNSE must be clear.

If set the alarm minutes field is ignored and alarms will be triggered based on IGNSE. The bits for IGNHR and IGNDA must both be set.

Bit maps to A1M2 or A2M2 and is used in maxim\_ds3231\_alarm\_configuration::alarm\_flags.

## [◆ ](#a65bba3dabc99b5098ffe280590b2dbba)MAXIM\_DS3231\_ALARM\_FLAGS\_IGNSE

| #define MAXIM\_DS3231\_ALARM\_FLAGS\_IGNSE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Control alarm behavior on match in seconds field.

If clear the alarm fires only when the RTC seconds matches the alarm seconds.

If set the alarm seconds field is ignored and an alarm will be triggered every second. The bits for IGNMN, IGNHR, and IGNDA must all be set.

This bit must be clear for the second alarm instance.

Bit maps to A1M1 and is used in maxim\_ds3231\_alarm\_configuration::alarm\_flags.

## [◆ ](#a7a0c8cd9efebab0c1d393bbf724b48be)MAXIM\_DS3231\_REG\_CTRL\_A1IE

| #define MAXIM\_DS3231\_REG\_CTRL\_A1IE   [MAXIM\_DS3231\_ALARM1](#aa4c7c4796b95c1565f1cbc89e3f8666c) |
| --- |

ctrl bit for alarm 1 interrupt enable.

## [◆ ](#a402938e78fe63caea36a719fc66a1d5a)MAXIM\_DS3231\_REG\_CTRL\_A2IE

| #define MAXIM\_DS3231\_REG\_CTRL\_A2IE   [MAXIM\_DS3231\_ALARM2](#a6bfaaa0a0dabf27c2836d80a5b603e36) |
| --- |

ctrl bit for alarm 2 interrupt enable.

## [◆ ](#aae0c76ff6e883a79a4586c275469ef96)MAXIM\_DS3231\_REG\_CTRL\_BBSQW

| #define MAXIM\_DS3231\_REG\_CTRL\_BBSQW   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

ctrl bit to write to enable square wave output in battery mode.

## [◆ ](#ab3e3e38695c5375d24c55381263cc257)MAXIM\_DS3231\_REG\_CTRL\_CONV

| #define MAXIM\_DS3231\_REG\_CTRL\_CONV   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

ctrl bit to write to trigger temperature conversion.

## [◆ ](#aabace2215a936b246329c2519291d876)MAXIM\_DS3231\_REG\_CTRL\_EOSCn

| #define MAXIM\_DS3231\_REG\_CTRL\_EOSCn   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7), |
| --- |

ctrl bit to write to disable the oscillator.

## [◆ ](#a3434c24e2058e8af1e5634ea81fa16d9)MAXIM\_DS3231\_REG\_CTRL\_INTCN

| #define MAXIM\_DS3231\_REG\_CTRL\_INTCN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

ctrl bit for ISQ functionality.

When clear the ISW signal provides a square wave. When set the ISW signal indicates alarm events.

Note
:   The driver expects to be able to control this bit.

## [◆ ](#ab85257cd6a6971702dfbdeca86b39018)MAXIM\_DS3231\_REG\_CTRL\_RS\_1Hz

| #define MAXIM\_DS3231\_REG\_CTRL\_RS\_1Hz   0x00 |
| --- |

ctrl RS field value for 1 Hz square wave.

## [◆ ](#a7e14bad3fb7439b128216effade29f5d)MAXIM\_DS3231\_REG\_CTRL\_RS\_1KiHz

| #define MAXIM\_DS3231\_REG\_CTRL\_RS\_1KiHz   0x01 |
| --- |

ctrl RS field value for 1024 Hz square wave.

## [◆ ](#a21e219fe89353341f9dd4634d0be4efa)MAXIM\_DS3231\_REG\_CTRL\_RS\_4KiHz

| #define MAXIM\_DS3231\_REG\_CTRL\_RS\_4KiHz   0x02 |
| --- |

ctrl RS field value for 4096 Hz square wave.

## [◆ ](#aa6069b89201545ca8c3bcdef952a1176)MAXIM\_DS3231\_REG\_CTRL\_RS\_8KiHz

| #define MAXIM\_DS3231\_REG\_CTRL\_RS\_8KiHz   0x03 |
| --- |

ctrl RS field value for 8192 Hz square wave.

## [◆ ](#a81b83144c73488ae9d4bf39e5c49c383)MAXIM\_DS3231\_REG\_CTRL\_RS\_Msk

| #define MAXIM\_DS3231\_REG\_CTRL\_RS\_Msk   (0x03 << [MAXIM\_DS3231\_REG\_CTRL\_RS\_Pos](#a91f55e1d2e9fcc15a5a4a28b65904fc5)) |
| --- |

ctrl mask to isolate RS bits.

## [◆ ](#a91f55e1d2e9fcc15a5a4a28b65904fc5)MAXIM\_DS3231\_REG\_CTRL\_RS\_Pos

| #define MAXIM\_DS3231\_REG\_CTRL\_RS\_Pos   3 |
| --- |

ctrl bit offset for square wave output frequency.

Note
:   The driver will control the content of this field.

## [◆ ](#ac3321b05e01df54d607cec07e4f02824)MAXIM\_DS3231\_REG\_STAT\_A1F

| #define MAXIM\_DS3231\_REG\_STAT\_A1F   [MAXIM\_DS3231\_ALARM1](#aa4c7c4796b95c1565f1cbc89e3f8666c) |
| --- |

ctrl\_stat bit indicating alarm1 has triggered.

If an alarm callback handler is registered this bit is cleared prior to invoking the callback with the flags indicating which alarms are ready.

## [◆ ](#a81df2ff1cbf0ac6ecbe2b80dbbe1b182)MAXIM\_DS3231\_REG\_STAT\_A2F

| #define MAXIM\_DS3231\_REG\_STAT\_A2F   [MAXIM\_DS3231\_ALARM2](#a6bfaaa0a0dabf27c2836d80a5b603e36) |
| --- |

ctrl\_stat bit indicating alarm2 has triggered.

If an alarm callback handler is registered this bit is cleared prior to invoking the callback with the flags indicating which alarms are ready.

## [◆ ](#ad522b899503e0606a53aaf1f9c9c0d38)MAXIM\_DS3231\_REG\_STAT\_BSY

| #define MAXIM\_DS3231\_REG\_STAT\_BSY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

Flag indicating a temperature conversion is in progress.

## [◆ ](#aa966f6de1e7662e66fac1d631b44d021)MAXIM\_DS3231\_REG\_STAT\_EN32kHz

| #define MAXIM\_DS3231\_REG\_STAT\_EN32kHz   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

Set to enable 32 KiHz open drain signal.

Note
:   This is a control bit, though it is positioned within the ctrl\_stat register which otherwise contains status bits.

## [◆ ](#afe205661d94e00c332404e4c7f6dd138)MAXIM\_DS3231\_REG\_STAT\_OSF

| #define MAXIM\_DS3231\_REG\_STAT\_OSF   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

Flag indicating the oscillator has been off since last cleared.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [rtc](dir_fe6de79d2b035e3fa4834af86b312149.md)
- [maxim\_ds3231.h](maxim__ds3231_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
