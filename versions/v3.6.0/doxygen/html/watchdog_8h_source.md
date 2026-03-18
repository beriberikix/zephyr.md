---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/watchdog_8h_source.html
original_path: doxygen/html/watchdog_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

17

18#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

19#include <[zephyr/sys/util.h](util_8h.md)>

20#include <[zephyr/device.h](device_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

31

[ 33](group__watchdog__interface.md#gafe8472573a7d77a283974cd3843c3c01)#define WDT\_OPT\_PAUSE\_IN\_SLEEP BIT(0)

34

[ 36](group__watchdog__interface.md#ga6d6e1b7cd126a6ca55a955b783962339)#define WDT\_OPT\_PAUSE\_HALTED\_BY\_DBG BIT(1)

37

39

45

48#define WDT\_FLAG\_RESET\_SHIFT (0)

50#define WDT\_FLAG\_RESET\_MASK (0x3 << WDT\_FLAG\_RESET\_SHIFT)

52

[ 54](group__watchdog__interface.md#ga46a9d878848572cacde89a777977c86b)#define WDT\_FLAG\_RESET\_NONE (0 << WDT\_FLAG\_RESET\_SHIFT)

[ 56](group__watchdog__interface.md#ga24e1f60628198d8e763cf7ec14afed2e)#define WDT\_FLAG\_RESET\_CPU\_CORE (1 << WDT\_FLAG\_RESET\_SHIFT)

[ 58](group__watchdog__interface.md#ga71845f454594fac290599f3537d563c9)#define WDT\_FLAG\_RESET\_SOC (2 << WDT\_FLAG\_RESET\_SHIFT)

59

61

[ 72](structwdt__window.md)struct [wdt\_window](structwdt__window.md) {

[ 74](structwdt__window.md#a4e5be19373804f900aa9c1d925f0aace) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [min](structwdt__window.md#a4e5be19373804f900aa9c1d925f0aace);

[ 76](structwdt__window.md#a21195de2e42f9a183a1aba0fb0732572) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max](structwdt__window.md#a21195de2e42f9a183a1aba0fb0732572);

77};

78

[ 85](group__watchdog__interface.md#ga11a942c8e7ee7ceae87c4601dbea8486)typedef void (\*[wdt\_callback\_t](group__watchdog__interface.md#ga11a942c8e7ee7ceae87c4601dbea8486))(const struct [device](structdevice.md) \*dev, int channel\_id);

86

[ 88](structwdt__timeout__cfg.md)struct [wdt\_timeout\_cfg](structwdt__timeout__cfg.md) {

[ 90](structwdt__timeout__cfg.md#a7942c675aacd228e38ea3cde383aab41) struct [wdt\_window](structwdt__window.md) [window](structwdt__timeout__cfg.md#a7942c675aacd228e38ea3cde383aab41);

[ 92](structwdt__timeout__cfg.md#a0a3bcc1a3f2785b44c0196a7d3223aa0) [wdt\_callback\_t](group__watchdog__interface.md#ga11a942c8e7ee7ceae87c4601dbea8486) [callback](structwdt__timeout__cfg.md#a0a3bcc1a3f2785b44c0196a7d3223aa0);

93#if defined(CONFIG\_WDT\_MULTISTAGE) || defined(\_\_DOXYGEN\_\_)

[ 101](structwdt__timeout__cfg.md#a325fe7146a922f5f266537307dba6c63) struct [wdt\_timeout\_cfg](structwdt__timeout__cfg.md) \*[next](structwdt__timeout__cfg.md#a325fe7146a922f5f266537307dba6c63);

102#endif

[ 104](structwdt__timeout__cfg.md#a71aa1ffb4f9937cce8197278cc0c61ee) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structwdt__timeout__cfg.md#a71aa1ffb4f9937cce8197278cc0c61ee);

105};

106

108

113typedef int (\*wdt\_api\_setup)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) options);

114

119typedef int (\*wdt\_api\_disable)(const struct [device](structdevice.md) \*dev);

120

125typedef int (\*wdt\_api\_install\_timeout)(const struct [device](structdevice.md) \*dev,

126 const struct [wdt\_timeout\_cfg](structwdt__timeout__cfg.md) \*cfg);

127

132typedef int (\*wdt\_api\_feed)(const struct [device](structdevice.md) \*dev, int channel\_id);

133

134\_\_subsystem struct wdt\_driver\_api {

135 wdt\_api\_setup setup;

136 wdt\_api\_disable disable;

137 wdt\_api\_install\_timeout install\_timeout;

138 wdt\_api\_feed feed;

139};

143

[ 160](group__watchdog__interface.md#ga822239f3d73585e2d01312657dbbb782)\_\_syscall int [wdt\_setup](group__watchdog__interface.md#ga822239f3d73585e2d01312657dbbb782)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) options);

161

162static inline int z\_impl\_wdt\_setup(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) options)

163{

164 const struct wdt\_driver\_api \*api =

165 (const struct wdt\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

166

167 return api->setup(dev, options);

168}

169

[ 184](group__watchdog__interface.md#ga32c32cc911e6a0e20cb2dfdd3945be4e)\_\_syscall int [wdt\_disable](group__watchdog__interface.md#ga32c32cc911e6a0e20cb2dfdd3945be4e)(const struct [device](structdevice.md) \*dev);

185

186static inline int z\_impl\_wdt\_disable(const struct [device](structdevice.md) \*dev)

187{

188 const struct wdt\_driver\_api \*api =

189 (const struct wdt\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

190

191 return api->disable(dev);

192}

193

[ 216](group__watchdog__interface.md#ga5be7aa7f1987be0e69c74b62d1c126a5)static inline int [wdt\_install\_timeout](group__watchdog__interface.md#ga5be7aa7f1987be0e69c74b62d1c126a5)(const struct [device](structdevice.md) \*dev,

217 const struct [wdt\_timeout\_cfg](structwdt__timeout__cfg.md) \*cfg)

218{

219 const struct wdt\_driver\_api \*api =

220 (const struct wdt\_driver\_api \*) dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

221

222 return api->install\_timeout(dev, cfg);

223}

224

[ 238](group__watchdog__interface.md#ga87265e8988e928eaa380ea29afb6eabe)\_\_syscall int [wdt\_feed](group__watchdog__interface.md#ga87265e8988e928eaa380ea29afb6eabe)(const struct [device](structdevice.md) \*dev, int channel\_id);

239

240static inline int z\_impl\_wdt\_feed(const struct [device](structdevice.md) \*dev, int channel\_id)

241{

242 const struct wdt\_driver\_api \*api =

243 (const struct wdt\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

244

245 return api->feed(dev, channel\_id);

246}

247

248#ifdef \_\_cplusplus

249}

250#endif

251

253

254#include <syscalls/watchdog.h>

255

256#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_WATCHDOG\_H\_ \*/

[device.h](device_8h.md)

[wdt\_callback\_t](group__watchdog__interface.md#ga11a942c8e7ee7ceae87c4601dbea8486)

void(\* wdt\_callback\_t)(const struct device \*dev, int channel\_id)

Watchdog callback.

**Definition** watchdog.h:85

[wdt\_disable](group__watchdog__interface.md#ga32c32cc911e6a0e20cb2dfdd3945be4e)

int wdt\_disable(const struct device \*dev)

Disable watchdog instance.

[wdt\_install\_timeout](group__watchdog__interface.md#ga5be7aa7f1987be0e69c74b62d1c126a5)

static int wdt\_install\_timeout(const struct device \*dev, const struct wdt\_timeout\_cfg \*cfg)

Install a new timeout.

**Definition** watchdog.h:216

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

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[wdt\_timeout\_cfg](structwdt__timeout__cfg.md)

Watchdog timeout configuration.

**Definition** watchdog.h:88

[wdt\_timeout\_cfg::callback](structwdt__timeout__cfg.md#a0a3bcc1a3f2785b44c0196a7d3223aa0)

wdt\_callback\_t callback

Timeout callback (can be NULL).

**Definition** watchdog.h:92

[wdt\_timeout\_cfg::next](structwdt__timeout__cfg.md#a325fe7146a922f5f266537307dba6c63)

struct wdt\_timeout\_cfg \* next

Pointer to the next timeout configuration.

**Definition** watchdog.h:101

[wdt\_timeout\_cfg::flags](structwdt__timeout__cfg.md#a71aa1ffb4f9937cce8197278cc0c61ee)

uint8\_t flags

Flags (see WDT\_FLAGS).

**Definition** watchdog.h:104

[wdt\_timeout\_cfg::window](structwdt__timeout__cfg.md#a7942c675aacd228e38ea3cde383aab41)

struct wdt\_window window

Timing parameters of watchdog timeout.

**Definition** watchdog.h:90

[wdt\_window](structwdt__window.md)

Watchdog timeout window.

**Definition** watchdog.h:72

[wdt\_window::max](structwdt__window.md#a21195de2e42f9a183a1aba0fb0732572)

uint32\_t max

Upper limit of watchdog feed timeout in milliseconds.

**Definition** watchdog.h:76

[wdt\_window::min](structwdt__window.md#a4e5be19373804f900aa9c1d925f0aace)

uint32\_t min

Lower limit of watchdog feed timeout in milliseconds.

**Definition** watchdog.h:74

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [watchdog.h](watchdog_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
