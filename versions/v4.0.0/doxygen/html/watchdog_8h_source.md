---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/watchdog_8h_source.html
original_path: doxygen/html/watchdog_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

watchdog.h

[Go to the documentation of this file.](watchdog_8h.md)

1/\*

2 \* Copyright (c) 2017 Nordic Semiconductor ASA

3 \* Copyright (c) 2015 Intel Corporation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_WATCHDOG\_H\_

9#define ZEPHYR\_INCLUDE\_DRIVERS\_WATCHDOG\_H\_

10

19

20#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

21#include <[zephyr/sys/util.h](sys_2util_8h.md)>

22#include <[zephyr/device.h](device_8h.md)>

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

33

[ 35](group__watchdog__interface.md#gafe8472573a7d77a283974cd3843c3c01)#define WDT\_OPT\_PAUSE\_IN\_SLEEP BIT(0)

36

[ 38](group__watchdog__interface.md#ga6d6e1b7cd126a6ca55a955b783962339)#define WDT\_OPT\_PAUSE\_HALTED\_BY\_DBG BIT(1)

39

41

47

50#define WDT\_FLAG\_RESET\_SHIFT (0)

52#define WDT\_FLAG\_RESET\_MASK (0x3 << WDT\_FLAG\_RESET\_SHIFT)

54

[ 56](group__watchdog__interface.md#ga46a9d878848572cacde89a777977c86b)#define WDT\_FLAG\_RESET\_NONE (0 << WDT\_FLAG\_RESET\_SHIFT)

[ 58](group__watchdog__interface.md#ga24e1f60628198d8e763cf7ec14afed2e)#define WDT\_FLAG\_RESET\_CPU\_CORE (1 << WDT\_FLAG\_RESET\_SHIFT)

[ 60](group__watchdog__interface.md#ga71845f454594fac290599f3537d563c9)#define WDT\_FLAG\_RESET\_SOC (2 << WDT\_FLAG\_RESET\_SHIFT)

61

63

[ 74](structwdt__window.md)struct [wdt\_window](structwdt__window.md) {

[ 76](structwdt__window.md#a4e5be19373804f900aa9c1d925f0aace) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [min](structwdt__window.md#a4e5be19373804f900aa9c1d925f0aace);

[ 78](structwdt__window.md#a21195de2e42f9a183a1aba0fb0732572) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max](structwdt__window.md#a21195de2e42f9a183a1aba0fb0732572);

79};

80

[ 87](group__watchdog__interface.md#ga11a942c8e7ee7ceae87c4601dbea8486)typedef void (\*[wdt\_callback\_t](group__watchdog__interface.md#ga11a942c8e7ee7ceae87c4601dbea8486))(const struct [device](structdevice.md) \*dev, int channel\_id);

88

[ 90](structwdt__timeout__cfg.md)struct [wdt\_timeout\_cfg](structwdt__timeout__cfg.md) {

[ 92](structwdt__timeout__cfg.md#a7942c675aacd228e38ea3cde383aab41) struct [wdt\_window](structwdt__window.md) [window](structwdt__timeout__cfg.md#a7942c675aacd228e38ea3cde383aab41);

[ 94](structwdt__timeout__cfg.md#a0a3bcc1a3f2785b44c0196a7d3223aa0) [wdt\_callback\_t](group__watchdog__interface.md#ga11a942c8e7ee7ceae87c4601dbea8486) [callback](structwdt__timeout__cfg.md#a0a3bcc1a3f2785b44c0196a7d3223aa0);

95#if defined(CONFIG\_WDT\_MULTISTAGE) || defined(\_\_DOXYGEN\_\_)

[ 103](structwdt__timeout__cfg.md#a325fe7146a922f5f266537307dba6c63) struct [wdt\_timeout\_cfg](structwdt__timeout__cfg.md) \*[next](structwdt__timeout__cfg.md#a325fe7146a922f5f266537307dba6c63);

104#endif

[ 106](structwdt__timeout__cfg.md#a71aa1ffb4f9937cce8197278cc0c61ee) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structwdt__timeout__cfg.md#a71aa1ffb4f9937cce8197278cc0c61ee);

107};

108

110

115typedef int (\*wdt\_api\_setup)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) options);

116

121typedef int (\*wdt\_api\_disable)(const struct [device](structdevice.md) \*dev);

122

127typedef int (\*wdt\_api\_install\_timeout)(const struct [device](structdevice.md) \*dev,

128 const struct [wdt\_timeout\_cfg](structwdt__timeout__cfg.md) \*cfg);

129

134typedef int (\*wdt\_api\_feed)(const struct [device](structdevice.md) \*dev, int channel\_id);

135

136\_\_subsystem struct wdt\_driver\_api {

137 wdt\_api\_setup setup;

138 wdt\_api\_disable disable;

139 wdt\_api\_install\_timeout install\_timeout;

140 wdt\_api\_feed feed;

141};

145

[ 162](group__watchdog__interface.md#ga822239f3d73585e2d01312657dbbb782)\_\_syscall int [wdt\_setup](group__watchdog__interface.md#ga822239f3d73585e2d01312657dbbb782)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) options);

163

164static inline int z\_impl\_wdt\_setup(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) options)

165{

166 const struct wdt\_driver\_api \*api =

167 (const struct wdt\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

168

169 return api->setup(dev, options);

170}

171

[ 186](group__watchdog__interface.md#ga32c32cc911e6a0e20cb2dfdd3945be4e)\_\_syscall int [wdt\_disable](group__watchdog__interface.md#ga32c32cc911e6a0e20cb2dfdd3945be4e)(const struct [device](structdevice.md) \*dev);

187

188static inline int z\_impl\_wdt\_disable(const struct [device](structdevice.md) \*dev)

189{

190 const struct wdt\_driver\_api \*api =

191 (const struct wdt\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

192

193 return api->disable(dev);

194}

195

[ 218](group__watchdog__interface.md#ga5be7aa7f1987be0e69c74b62d1c126a5)static inline int [wdt\_install\_timeout](group__watchdog__interface.md#ga5be7aa7f1987be0e69c74b62d1c126a5)(const struct [device](structdevice.md) \*dev,

219 const struct [wdt\_timeout\_cfg](structwdt__timeout__cfg.md) \*cfg)

220{

221 const struct wdt\_driver\_api \*api =

222 (const struct wdt\_driver\_api \*) dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

223

224 return api->install\_timeout(dev, cfg);

225}

226

[ 240](group__watchdog__interface.md#ga87265e8988e928eaa380ea29afb6eabe)\_\_syscall int [wdt\_feed](group__watchdog__interface.md#ga87265e8988e928eaa380ea29afb6eabe)(const struct [device](structdevice.md) \*dev, int channel\_id);

241

242static inline int z\_impl\_wdt\_feed(const struct [device](structdevice.md) \*dev, int channel\_id)

243{

244 const struct wdt\_driver\_api \*api =

245 (const struct wdt\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

246

247 return api->feed(dev, channel\_id);

248}

249

250#ifdef \_\_cplusplus

251}

252#endif

253

255

256#include <zephyr/syscalls/watchdog.h>

257

258#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_WATCHDOG\_H\_ \*/

[device.h](device_8h.md)

[wdt\_callback\_t](group__watchdog__interface.md#ga11a942c8e7ee7ceae87c4601dbea8486)

void(\* wdt\_callback\_t)(const struct device \*dev, int channel\_id)

Watchdog callback.

**Definition** watchdog.h:87

[wdt\_disable](group__watchdog__interface.md#ga32c32cc911e6a0e20cb2dfdd3945be4e)

int wdt\_disable(const struct device \*dev)

Disable watchdog instance.

[wdt\_install\_timeout](group__watchdog__interface.md#ga5be7aa7f1987be0e69c74b62d1c126a5)

static int wdt\_install\_timeout(const struct device \*dev, const struct wdt\_timeout\_cfg \*cfg)

Install a new timeout.

**Definition** watchdog.h:218

[wdt\_setup](group__watchdog__interface.md#ga822239f3d73585e2d01312657dbbb782)

int wdt\_setup(const struct device \*dev, uint8\_t options)

Set up watchdog instance.

[wdt\_feed](group__watchdog__interface.md#ga87265e8988e928eaa380ea29afb6eabe)

int wdt\_feed(const struct device \*dev, int channel\_id)

Feed specified watchdog timeout.

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[wdt\_timeout\_cfg](structwdt__timeout__cfg.md)

Watchdog timeout configuration.

**Definition** watchdog.h:90

[wdt\_timeout\_cfg::callback](structwdt__timeout__cfg.md#a0a3bcc1a3f2785b44c0196a7d3223aa0)

wdt\_callback\_t callback

Timeout callback (can be NULL).

**Definition** watchdog.h:94

[wdt\_timeout\_cfg::next](structwdt__timeout__cfg.md#a325fe7146a922f5f266537307dba6c63)

struct wdt\_timeout\_cfg \* next

Pointer to the next timeout configuration.

**Definition** watchdog.h:103

[wdt\_timeout\_cfg::flags](structwdt__timeout__cfg.md#a71aa1ffb4f9937cce8197278cc0c61ee)

uint8\_t flags

Flags (see WDT\_FLAGS).

**Definition** watchdog.h:106

[wdt\_timeout\_cfg::window](structwdt__timeout__cfg.md#a7942c675aacd228e38ea3cde383aab41)

struct wdt\_window window

Timing parameters of watchdog timeout.

**Definition** watchdog.h:92

[wdt\_window](structwdt__window.md)

Watchdog timeout window.

**Definition** watchdog.h:74

[wdt\_window::max](structwdt__window.md#a21195de2e42f9a183a1aba0fb0732572)

uint32\_t max

Upper limit of watchdog feed timeout in milliseconds.

**Definition** watchdog.h:78

[wdt\_window::min](structwdt__window.md#a4e5be19373804f900aa9c1d925f0aace)

uint32\_t min

Lower limit of watchdog feed timeout in milliseconds.

**Definition** watchdog.h:76

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [watchdog.h](watchdog_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
