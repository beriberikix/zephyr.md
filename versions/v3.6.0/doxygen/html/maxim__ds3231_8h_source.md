---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/maxim__ds3231_8h_source.html
original_path: doxygen/html/maxim__ds3231_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

maxim\_ds3231.h

[Go to the documentation of this file.](maxim__ds3231_8h.md)

1/\*

2 \* Copyright (c) 2019 Peter Bigot Consulting, LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

32#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_RTC\_DS3231\_H\_

33#define ZEPHYR\_INCLUDE\_DRIVERS\_RTC\_DS3231\_H\_

34

35#include <time.h>

36

37#include <[zephyr/drivers/counter.h](counter_8h.md)>

38#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

39#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

40#include <[zephyr/sys/notify.h](notify_8h.md)>

41

42#ifdef \_\_cplusplus

43extern "C" {

44#endif

45

[ 47](maxim__ds3231_8h.md#aa4c7c4796b95c1565f1cbc89e3f8666c)#define MAXIM\_DS3231\_ALARM1 BIT(0)

48

[ 50](maxim__ds3231_8h.md#a6bfaaa0a0dabf27c2836d80a5b603e36)#define MAXIM\_DS3231\_ALARM2 BIT(1)

51

52/\* Constants corresponding to bits in the DS3231 control register at

53 \* 0x0E.

54 \*

55 \* See the datasheet for interpretation of these bits.

56 \*/

[ 58](maxim__ds3231_8h.md#a7a0c8cd9efebab0c1d393bbf724b48be)#define MAXIM\_DS3231\_REG\_CTRL\_A1IE MAXIM\_DS3231\_ALARM1

59

[ 61](maxim__ds3231_8h.md#a402938e78fe63caea36a719fc66a1d5a)#define MAXIM\_DS3231\_REG\_CTRL\_A2IE MAXIM\_DS3231\_ALARM2

62

[ 70](maxim__ds3231_8h.md#a3434c24e2058e8af1e5634ea81fa16d9)#define MAXIM\_DS3231\_REG\_CTRL\_INTCN BIT(2)

71

[ 76](maxim__ds3231_8h.md#a91f55e1d2e9fcc15a5a4a28b65904fc5)#define MAXIM\_DS3231\_REG\_CTRL\_RS\_Pos 3

77

[ 79](maxim__ds3231_8h.md#a81b83144c73488ae9d4bf39e5c49c383)#define MAXIM\_DS3231\_REG\_CTRL\_RS\_Msk (0x03 << MAXIM\_DS3231\_REG\_CTRL\_RS\_Pos)

80

[ 82](maxim__ds3231_8h.md#ab85257cd6a6971702dfbdeca86b39018)#define MAXIM\_DS3231\_REG\_CTRL\_RS\_1Hz 0x00

83

[ 85](maxim__ds3231_8h.md#a7e14bad3fb7439b128216effade29f5d)#define MAXIM\_DS3231\_REG\_CTRL\_RS\_1KiHz 0x01

86

[ 88](maxim__ds3231_8h.md#a21e219fe89353341f9dd4634d0be4efa)#define MAXIM\_DS3231\_REG\_CTRL\_RS\_4KiHz 0x02

89

[ 91](maxim__ds3231_8h.md#aa6069b89201545ca8c3bcdef952a1176)#define MAXIM\_DS3231\_REG\_CTRL\_RS\_8KiHz 0x03

92

[ 94](maxim__ds3231_8h.md#ab3e3e38695c5375d24c55381263cc257)#define MAXIM\_DS3231\_REG\_CTRL\_CONV BIT(5)

95

[ 97](maxim__ds3231_8h.md#aae0c76ff6e883a79a4586c275469ef96)#define MAXIM\_DS3231\_REG\_CTRL\_BBSQW BIT(6)

98

[ 100](maxim__ds3231_8h.md#aabace2215a936b246329c2519291d876)#define MAXIM\_DS3231\_REG\_CTRL\_EOSCn BIT(7),

101

[ 108](maxim__ds3231_8h.md#ac3321b05e01df54d607cec07e4f02824)#define MAXIM\_DS3231\_REG\_STAT\_A1F MAXIM\_DS3231\_ALARM1

109

[ 116](maxim__ds3231_8h.md#a81df2ff1cbf0ac6ecbe2b80dbbe1b182)#define MAXIM\_DS3231\_REG\_STAT\_A2F MAXIM\_DS3231\_ALARM2

117

[ 119](maxim__ds3231_8h.md#ad522b899503e0606a53aaf1f9c9c0d38)#define MAXIM\_DS3231\_REG\_STAT\_BSY BIT(2)

120

[ 126](maxim__ds3231_8h.md#aa966f6de1e7662e66fac1d631b44d021)#define MAXIM\_DS3231\_REG\_STAT\_EN32kHz BIT(3)

127

[ 129](maxim__ds3231_8h.md#afe205661d94e00c332404e4c7f6dd138)#define MAXIM\_DS3231\_REG\_STAT\_OSF BIT(7)

130

[ 145](maxim__ds3231_8h.md#a65bba3dabc99b5098ffe280590b2dbba)#define MAXIM\_DS3231\_ALARM\_FLAGS\_IGNSE BIT(0)

146

[ 159](maxim__ds3231_8h.md#a4be38828079d6eda3e952dee03c205e3)#define MAXIM\_DS3231\_ALARM\_FLAGS\_IGNMN BIT(1)

160

[ 172](maxim__ds3231_8h.md#a2217d1d4d37b3d116f6d0fb4f6eb5f04)#define MAXIM\_DS3231\_ALARM\_FLAGS\_IGNHR BIT(2)

173

[ 186](maxim__ds3231_8h.md#a8041898f159b2a4c2fc13d942e08058b)#define MAXIM\_DS3231\_ALARM\_FLAGS\_IGNDA BIT(3)

187

[ 196](maxim__ds3231_8h.md#a92341088a6917efe124c946faa359d57)#define MAXIM\_DS3231\_ALARM\_FLAGS\_DOW BIT(4)

197

[ 207](maxim__ds3231_8h.md#a06f65bcbdbfde80613a193b27803ed95)#define MAXIM\_DS3231\_ALARM\_FLAGS\_AUTODISABLE BIT(7)

208

215

[ 230](group__rtc__ds3231__interface.md#ga684b29dc1c11d8df698437f27e6d0403)typedef void (\*[maxim\_ds3231\_alarm\_callback\_handler\_t](group__rtc__ds3231__interface.md#ga684b29dc1c11d8df698437f27e6d0403))(const struct [device](structdevice.md) \*dev,

231 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id,

232 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) syncclock,

233 void \*user\_data);

234

[ 247](group__rtc__ds3231__interface.md#ga59541c849327f388169ca3a15df0ba57)typedef void (\*[maxim\_ds3231\_notify\_callback](group__rtc__ds3231__interface.md#ga59541c849327f388169ca3a15df0ba57))(const struct [device](structdevice.md) \*dev,

248 struct [sys\_notify](structsys__notify.md) \*notify,

249 int res);

250

[ 262](structmaxim__ds3231__alarm.md)struct [maxim\_ds3231\_alarm](structmaxim__ds3231__alarm.md) {

[ 275](structmaxim__ds3231__alarm.md#a363a2dc65517c3d00de7658ce421937f) [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) [time](structmaxim__ds3231__alarm.md#a363a2dc65517c3d00de7658ce421937f);

276

[ 294](structmaxim__ds3231__alarm.md#a9628b99ed059a64f25143291c0df1c8c) [maxim\_ds3231\_alarm\_callback\_handler\_t](group__rtc__ds3231__interface.md#ga684b29dc1c11d8df698437f27e6d0403) [handler](structmaxim__ds3231__alarm.md#a9628b99ed059a64f25143291c0df1c8c);

295

[ 297](structmaxim__ds3231__alarm.md#a192fb8c10246bfe466e74aafbb45d720) void \*[user\_data](structmaxim__ds3231__alarm.md#a192fb8c10246bfe466e74aafbb45d720);

298

[ 311](structmaxim__ds3231__alarm.md#a98ebc645761cc0d035e269fa8d3f9c68) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structmaxim__ds3231__alarm.md#a98ebc645761cc0d035e269fa8d3f9c68);

312};

313

[ 320](structmaxim__ds3231__syncpoint.md)struct [maxim\_ds3231\_syncpoint](structmaxim__ds3231__syncpoint.md) {

[ 326](structmaxim__ds3231__syncpoint.md#aff4219f350140cb6a53e73bb91815452) struct [timespec](structtimespec.md) [rtc](structmaxim__ds3231__syncpoint.md#aff4219f350140cb6a53e73bb91815452);

327

[ 334](structmaxim__ds3231__syncpoint.md#adb649c698084d6dbb83915aa6e6079b8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [syncclock](structmaxim__ds3231__syncpoint.md#adb649c698084d6dbb83915aa6e6079b8);

335};

336

[ 360](group__rtc__ds3231__interface.md#ga68e1512974db4b526a632e140fa7eed8)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [maxim\_ds3231\_read\_syncclock](group__rtc__ds3231__interface.md#ga68e1512974db4b526a632e140fa7eed8)(const struct [device](structdevice.md) \*dev)

361{

362 return [k\_uptime\_get\_32](group__clock__apis.md#ga9253cfb7b46af4d8994349323ce9872b)();

363}

364

[ 373](group__rtc__ds3231__interface.md#ga6e4a3f34023be910d33fd7f89f81dba3)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [maxim\_ds3231\_syncclock\_frequency](group__rtc__ds3231__interface.md#ga6e4a3f34023be910d33fd7f89f81dba3)(const struct [device](structdevice.md) \*dev)

374{

375 return 1000U;

376}

377

[ 395](group__rtc__ds3231__interface.md#ga1a41193eb70b147eb623ff07be3b3954)int [maxim\_ds3231\_ctrl\_update](group__rtc__ds3231__interface.md#ga1a41193eb70b147eb623ff07be3b3954)(const struct [device](structdevice.md) \*dev,

396 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) set\_bits,

397 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clear\_bits);

398

[ 428](group__rtc__ds3231__interface.md#ga1073100b5943141333de8cfd0cd8ac2b)int [maxim\_ds3231\_stat\_update](group__rtc__ds3231__interface.md#ga1073100b5943141333de8cfd0cd8ac2b)(const struct [device](structdevice.md) \*dev,

429 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) set\_bits,

430 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clear\_bits);

431

[ 450](group__rtc__ds3231__interface.md#gabc9bd9ff8a2107c08a7d9ca02c162be1)int [maxim\_ds3231\_get\_alarm](group__rtc__ds3231__interface.md#gabc9bd9ff8a2107c08a7d9ca02c162be1)(const struct [device](structdevice.md) \*dev,

451 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id,

452 struct [maxim\_ds3231\_alarm](structmaxim__ds3231__alarm.md) \*cfg);

453

[ 474](group__rtc__ds3231__interface.md#ga8f876ad2e16e88d80a2f914be3df49b1)int [maxim\_ds3231\_set\_alarm](group__rtc__ds3231__interface.md#ga8f876ad2e16e88d80a2f914be3df49b1)(const struct [device](structdevice.md) \*dev,

475 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id,

476 const struct [maxim\_ds3231\_alarm](structmaxim__ds3231__alarm.md) \*cfg);

477

[ 504](group__rtc__ds3231__interface.md#gabdf39bc4983b12646ad3b18ccfc1a7dc)int [maxim\_ds3231\_synchronize](group__rtc__ds3231__interface.md#gabdf39bc4983b12646ad3b18ccfc1a7dc)(const struct [device](structdevice.md) \*dev,

505 struct [sys\_notify](structsys__notify.md) \*notify);

506

[ 522](group__rtc__ds3231__interface.md#ga45656b5994c063b77d04f60c71d42c5b)\_\_syscall int [maxim\_ds3231\_req\_syncpoint](group__rtc__ds3231__interface.md#ga45656b5994c063b77d04f60c71d42c5b)(const struct [device](structdevice.md) \*dev,

523 struct [k\_poll\_signal](structk__poll__signal.md) \*signal);

524

[ 537](group__rtc__ds3231__interface.md#ga4e9fab406fd3b9b20c0c7011bfbb7a8a)\_\_syscall int [maxim\_ds3231\_get\_syncpoint](group__rtc__ds3231__interface.md#ga4e9fab406fd3b9b20c0c7011bfbb7a8a)(const struct [device](structdevice.md) \*dev,

538 struct [maxim\_ds3231\_syncpoint](structmaxim__ds3231__syncpoint.md) \*syncpoint);

539

[ 567](group__rtc__ds3231__interface.md#ga485db29a3aca59000798d5ae16ad7041)int [maxim\_ds3231\_set](group__rtc__ds3231__interface.md#ga485db29a3aca59000798d5ae16ad7041)(const struct [device](structdevice.md) \*dev,

568 const struct [maxim\_ds3231\_syncpoint](structmaxim__ds3231__syncpoint.md) \*syncpoint,

569 struct [sys\_notify](structsys__notify.md) \*notify);

570

[ 588](group__rtc__ds3231__interface.md#gab2091298eb9b94da29ad79616b707bad)int [maxim\_ds3231\_check\_alarms](group__rtc__ds3231__interface.md#gab2091298eb9b94da29ad79616b707bad)(const struct [device](structdevice.md) \*dev);

589

593

594#ifdef \_\_cplusplus

595}

596#endif

597

598/\* @todo this should be syscalls/drivers/rtc/maxim\_ds3231.h \*/

599#include <syscalls/maxim\_ds3231.h>

600

601#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_RTC\_DS3231\_H\_ \*/

[time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7)

\_TIME\_T\_ time\_t

**Definition** \_timespec.h:14

[counter.h](counter_8h.md)

Public API for counter and timer drivers.

[k\_uptime\_get\_32](group__clock__apis.md#ga9253cfb7b46af4d8994349323ce9872b)

static uint32\_t k\_uptime\_get\_32(void)

Get system uptime (32-bit version).

**Definition** kernel.h:1770

[maxim\_ds3231\_stat\_update](group__rtc__ds3231__interface.md#ga1073100b5943141333de8cfd0cd8ac2b)

int maxim\_ds3231\_stat\_update(const struct device \*dev, uint8\_t set\_bits, uint8\_t clear\_bits)

Read the ctrl\_stat register then set and clear bits in it.

[maxim\_ds3231\_ctrl\_update](group__rtc__ds3231__interface.md#ga1a41193eb70b147eb623ff07be3b3954)

int maxim\_ds3231\_ctrl\_update(const struct device \*dev, uint8\_t set\_bits, uint8\_t clear\_bits)

Set and clear specific bits in the control register.

[maxim\_ds3231\_req\_syncpoint](group__rtc__ds3231__interface.md#ga45656b5994c063b77d04f60c71d42c5b)

int maxim\_ds3231\_req\_syncpoint(const struct device \*dev, struct k\_poll\_signal \*signal)

Request to update the synchronization point.

[maxim\_ds3231\_set](group__rtc__ds3231__interface.md#ga485db29a3aca59000798d5ae16ad7041)

int maxim\_ds3231\_set(const struct device \*dev, const struct maxim\_ds3231\_syncpoint \*syncpoint, struct sys\_notify \*notify)

Set the RTC to a time consistent with the provided synchronization.

[maxim\_ds3231\_get\_syncpoint](group__rtc__ds3231__interface.md#ga4e9fab406fd3b9b20c0c7011bfbb7a8a)

int maxim\_ds3231\_get\_syncpoint(const struct device \*dev, struct maxim\_ds3231\_syncpoint \*syncpoint)

Retrieve the most recent synchronization point.

[maxim\_ds3231\_notify\_callback](group__rtc__ds3231__interface.md#ga59541c849327f388169ca3a15df0ba57)

void(\* maxim\_ds3231\_notify\_callback)(const struct device \*dev, struct sys\_notify \*notify, int res)

Signature used to notify a user of the DS3231 that an asynchronous operation has completed.

**Definition** maxim\_ds3231.h:247

[maxim\_ds3231\_alarm\_callback\_handler\_t](group__rtc__ds3231__interface.md#ga684b29dc1c11d8df698437f27e6d0403)

void(\* maxim\_ds3231\_alarm\_callback\_handler\_t)(const struct device \*dev, uint8\_t id, uint32\_t syncclock, void \*user\_data)

Signature for DS3231 alarm callbacks.

**Definition** maxim\_ds3231.h:230

[maxim\_ds3231\_read\_syncclock](group__rtc__ds3231__interface.md#ga68e1512974db4b526a632e140fa7eed8)

static uint32\_t maxim\_ds3231\_read\_syncclock(const struct device \*dev)

Read the local synchronization clock.

**Definition** maxim\_ds3231.h:360

[maxim\_ds3231\_syncclock\_frequency](group__rtc__ds3231__interface.md#ga6e4a3f34023be910d33fd7f89f81dba3)

static uint32\_t maxim\_ds3231\_syncclock\_frequency(const struct device \*dev)

Get the frequency of the synchronization clock.

**Definition** maxim\_ds3231.h:373

[maxim\_ds3231\_set\_alarm](group__rtc__ds3231__interface.md#ga8f876ad2e16e88d80a2f914be3df49b1)

int maxim\_ds3231\_set\_alarm(const struct device \*dev, uint8\_t id, const struct maxim\_ds3231\_alarm \*cfg)

Configure a DS3231 alarm.

[maxim\_ds3231\_check\_alarms](group__rtc__ds3231__interface.md#gab2091298eb9b94da29ad79616b707bad)

int maxim\_ds3231\_check\_alarms(const struct device \*dev)

Check for and clear flags indicating that an alarm has fired.

[maxim\_ds3231\_get\_alarm](group__rtc__ds3231__interface.md#gabc9bd9ff8a2107c08a7d9ca02c162be1)

int maxim\_ds3231\_get\_alarm(const struct device \*dev, uint8\_t id, struct maxim\_ds3231\_alarm \*cfg)

Read a DS3231 alarm configuration.

[maxim\_ds3231\_synchronize](group__rtc__ds3231__interface.md#gabdf39bc4983b12646ad3b18ccfc1a7dc)

int maxim\_ds3231\_synchronize(const struct device \*dev, struct sys\_notify \*notify)

Synchronize the RTC against the local clock.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

[notify.h](notify_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:5622

[maxim\_ds3231\_alarm](structmaxim__ds3231__alarm.md)

Information defining the alarm configuration.

**Definition** maxim\_ds3231.h:262

[maxim\_ds3231\_alarm::user\_data](structmaxim__ds3231__alarm.md#a192fb8c10246bfe466e74aafbb45d720)

void \* user\_data

User-provided pointer passed to alarm callback.

**Definition** maxim\_ds3231.h:297

[maxim\_ds3231\_alarm::time](structmaxim__ds3231__alarm.md#a363a2dc65517c3d00de7658ce421937f)

time\_t time

Time specification for an RTC alarm.

**Definition** maxim\_ds3231.h:275

[maxim\_ds3231\_alarm::handler](structmaxim__ds3231__alarm.md#a9628b99ed059a64f25143291c0df1c8c)

maxim\_ds3231\_alarm\_callback\_handler\_t handler

Handler to be invoked when alarms are signalled.

**Definition** maxim\_ds3231.h:294

[maxim\_ds3231\_alarm::flags](structmaxim__ds3231__alarm.md#a98ebc645761cc0d035e269fa8d3f9c68)

uint8\_t flags

Flags controlling configuration of the alarm alarm.

**Definition** maxim\_ds3231.h:311

[maxim\_ds3231\_syncpoint](structmaxim__ds3231__syncpoint.md)

Register the RTC clock against system clocks.

**Definition** maxim\_ds3231.h:320

[maxim\_ds3231\_syncpoint::syncclock](structmaxim__ds3231__syncpoint.md#adb649c698084d6dbb83915aa6e6079b8)

uint32\_t syncclock

Value of a local clock at the same instant as rtc.

**Definition** maxim\_ds3231.h:334

[maxim\_ds3231\_syncpoint::rtc](structmaxim__ds3231__syncpoint.md#aff4219f350140cb6a53e73bb91815452)

struct timespec rtc

Time from the DS3231.

**Definition** maxim\_ds3231.h:326

[sys\_notify](structsys__notify.md)

State associated with notification for an asynchronous operation.

**Definition** notify.h:138

[timespec](structtimespec.md)

**Definition** \_timespec.h:22

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [rtc](dir_fe6de79d2b035e3fa4834af86b312149.md)
- [maxim\_ds3231.h](maxim__ds3231_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
