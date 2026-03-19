---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ipc__service_8h_source.html
original_path: doxygen/html/ipc__service_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipc\_service.h

[Go to the documentation of this file.](ipc__service_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_IPC\_IPC\_SERVICE\_H\_

8#define ZEPHYR\_INCLUDE\_IPC\_IPC\_SERVICE\_H\_

9

10#include <[stdio.h](stdio_8h.md)>

11#include <[zephyr/device.h](device_8h.md)>

12#include <[zephyr/kernel.h](kernel_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

25

32

39

135

139

[ 145](structipc__service__cb.md)struct [ipc\_service\_cb](structipc__service__cb.md) {

[ 152](structipc__service__cb.md#a76be12bf8a7964977b5d7512dd010110) void (\*[bound](structipc__service__cb.md#a76be12bf8a7964977b5d7512dd010110))(void \*priv);

153

[ 166](structipc__service__cb.md#a7b67edec6902fd6d8254ebfec4ee9fb5) void (\*[received](structipc__service__cb.md#a7b67edec6902fd6d8254ebfec4ee9fb5))(const void \*data, size\_t len, void \*priv);

167

[ 173](structipc__service__cb.md#ac40fd19ae5263f1880df1fe3dca55647) void (\*[error](structipc__service__cb.md#ac40fd19ae5263f1880df1fe3dca55647))(const char \*message, void \*priv);

174};

175

[ 181](structipc__ept.md)struct [ipc\_ept](structipc__ept.md) {

182

[ 184](structipc__ept.md#a4f043fd1ed7df3e1774ba7639c2caf1d) const struct [device](structdevice.md) \*[instance](structipc__ept.md#a4f043fd1ed7df3e1774ba7639c2caf1d);

185

[ 187](structipc__ept.md#a234002020af2b8a2f31ff3727ecf0964) void \*[token](structipc__ept.md#a234002020af2b8a2f31ff3727ecf0964);

188};

189

[ 191](structipc__ept__cfg.md)struct [ipc\_ept\_cfg](structipc__ept__cfg.md) {

192

[ 194](structipc__ept__cfg.md#a6008673337256dc8a71052e121d2d0c6) const char \*[name](structipc__ept__cfg.md#a6008673337256dc8a71052e121d2d0c6);

195

[ 197](structipc__ept__cfg.md#a8a85a116e7c0069121d4ef5dc9b55a4d) int [prio](structipc__ept__cfg.md#a8a85a116e7c0069121d4ef5dc9b55a4d);

198

[ 200](structipc__ept__cfg.md#a0cd24dc49dbfe7f8cda02ee37d36529c) struct [ipc\_service\_cb](structipc__service__cb.md) [cb](structipc__ept__cfg.md#a0cd24dc49dbfe7f8cda02ee37d36529c);

201

[ 203](structipc__ept__cfg.md#a4b14515e74e5429d62e13c0478070893) void \*[priv](structipc__ept__cfg.md#a4b14515e74e5429d62e13c0478070893);

204};

205

[ 220](group__ipc__service__api.md#gafef0b817299aedc870a004ab223bd20a)int [ipc\_service\_open\_instance](group__ipc__service__api.md#gafef0b817299aedc870a004ab223bd20a)(const struct [device](structdevice.md) \*instance);

221

[ 239](group__ipc__service__api.md#ga78c837d30cfd8989efe63e0a397148a7)int [ipc\_service\_close\_instance](group__ipc__service__api.md#ga78c837d30cfd8989efe63e0a397148a7)(const struct [device](structdevice.md) \*instance);

240

[ 261](group__ipc__service__api.md#gabfb8bab2e2e8cfe8908a050d4844666b)int [ipc\_service\_register\_endpoint](group__ipc__service__api.md#gabfb8bab2e2e8cfe8908a050d4844666b)(const struct [device](structdevice.md) \*instance,

262 struct [ipc\_ept](structipc__ept.md) \*ept,

263 const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \*cfg);

264

[ 281](group__ipc__service__api.md#ga35c788240922fbca7b49af265100b68b)int [ipc\_service\_deregister\_endpoint](group__ipc__service__api.md#ga35c788240922fbca7b49af265100b68b)(struct [ipc\_ept](structipc__ept.md) \*ept);

282

[ 301](group__ipc__service__api.md#gac002253b7436902c6a3e0c93933d23fc)int [ipc\_service\_send](group__ipc__service__api.md#gac002253b7436902c6a3e0c93933d23fc)(struct [ipc\_ept](structipc__ept.md) \*ept, const void \*data, size\_t len);

302

[ 319](group__ipc__service__api.md#ga5bcce96a208b4282e3eceb6e0ff451e4)int [ipc\_service\_get\_tx\_buffer\_size](group__ipc__service__api.md#ga5bcce96a208b4282e3eceb6e0ff451e4)(struct [ipc\_ept](structipc__ept.md) \*ept);

320

[ 368](group__ipc__service__api.md#gab2371bd26ad85b5dffac3b4000e51191)int [ipc\_service\_get\_tx\_buffer](group__ipc__service__api.md#gab2371bd26ad85b5dffac3b4000e51191)(struct [ipc\_ept](structipc__ept.md) \*ept, void \*\*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*size, [k\_timeout\_t](structk__timeout__t.md) wait);

369

[ 390](group__ipc__service__api.md#ga3eb7168f73f5bc45fdced3af6d374860)int [ipc\_service\_drop\_tx\_buffer](group__ipc__service__api.md#ga3eb7168f73f5bc45fdced3af6d374860)(struct [ipc\_ept](structipc__ept.md) \*ept, const void \*data);

391

[ 424](group__ipc__service__api.md#ga72aa5da1530908230478c49b5a012dc1)int [ipc\_service\_send\_nocopy](group__ipc__service__api.md#ga72aa5da1530908230478c49b5a012dc1)(struct [ipc\_ept](structipc__ept.md) \*ept, const void \*data, size\_t len);

425

[ 449](group__ipc__service__api.md#gadd957653c3e2bc32c494a9d643c0a0bd)int [ipc\_service\_hold\_rx\_buffer](group__ipc__service__api.md#gadd957653c3e2bc32c494a9d643c0a0bd)(struct [ipc\_ept](structipc__ept.md) \*ept, void \*data);

450

[ 475](group__ipc__service__api.md#gaf4fd99716e7c83006a76f7f1bc85f228)int [ipc\_service\_release\_rx\_buffer](group__ipc__service__api.md#gaf4fd99716e7c83006a76f7f1bc85f228)(struct [ipc\_ept](structipc__ept.md) \*ept, void \*data);

476

480

481#ifdef \_\_cplusplus

482}

483#endif

484

485#endif /\* ZEPHYR\_INCLUDE\_IPC\_IPC\_SERVICE\_H\_ \*/

[device.h](device_8h.md)

[ipc\_service\_deregister\_endpoint](group__ipc__service__api.md#ga35c788240922fbca7b49af265100b68b)

int ipc\_service\_deregister\_endpoint(struct ipc\_ept \*ept)

Deregister an IPC endpoint from its instance.

[ipc\_service\_drop\_tx\_buffer](group__ipc__service__api.md#ga3eb7168f73f5bc45fdced3af6d374860)

int ipc\_service\_drop\_tx\_buffer(struct ipc\_ept \*ept, const void \*data)

Drop and release a TX buffer.

[ipc\_service\_get\_tx\_buffer\_size](group__ipc__service__api.md#ga5bcce96a208b4282e3eceb6e0ff451e4)

int ipc\_service\_get\_tx\_buffer\_size(struct ipc\_ept \*ept)

Get the TX buffer size.

[ipc\_service\_send\_nocopy](group__ipc__service__api.md#ga72aa5da1530908230478c49b5a012dc1)

int ipc\_service\_send\_nocopy(struct ipc\_ept \*ept, const void \*data, size\_t len)

Send data in a TX buffer reserved by ipc\_service\_get\_tx\_buffer using the given IPC endpoint.

[ipc\_service\_close\_instance](group__ipc__service__api.md#ga78c837d30cfd8989efe63e0a397148a7)

int ipc\_service\_close\_instance(const struct device \*instance)

Close an instance.

[ipc\_service\_get\_tx\_buffer](group__ipc__service__api.md#gab2371bd26ad85b5dffac3b4000e51191)

int ipc\_service\_get\_tx\_buffer(struct ipc\_ept \*ept, void \*\*data, uint32\_t \*size, k\_timeout\_t wait)

Get an empty TX buffer to be sent using ipc\_service\_send\_nocopy.

[ipc\_service\_register\_endpoint](group__ipc__service__api.md#gabfb8bab2e2e8cfe8908a050d4844666b)

int ipc\_service\_register\_endpoint(const struct device \*instance, struct ipc\_ept \*ept, const struct ipc\_ept\_cfg \*cfg)

Register IPC endpoint onto an instance.

[ipc\_service\_send](group__ipc__service__api.md#gac002253b7436902c6a3e0c93933d23fc)

int ipc\_service\_send(struct ipc\_ept \*ept, const void \*data, size\_t len)

Send data using given IPC endpoint.

[ipc\_service\_hold\_rx\_buffer](group__ipc__service__api.md#gadd957653c3e2bc32c494a9d643c0a0bd)

int ipc\_service\_hold\_rx\_buffer(struct ipc\_ept \*ept, void \*data)

Holds the RX buffer for usage outside the receive callback.

[ipc\_service\_release\_rx\_buffer](group__ipc__service__api.md#gaf4fd99716e7c83006a76f7f1bc85f228)

int ipc\_service\_release\_rx\_buffer(struct ipc\_ept \*ept, void \*data)

Release the RX buffer for future reuse.

[ipc\_service\_open\_instance](group__ipc__service__api.md#gafef0b817299aedc870a004ab223bd20a)

int ipc\_service\_open\_instance(const struct device \*instance)

Open an instance.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[stdio.h](stdio_8h.md)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[ipc\_ept\_cfg](structipc__ept__cfg.md)

Endpoint configuration structure.

**Definition** ipc\_service.h:191

[ipc\_ept\_cfg::cb](structipc__ept__cfg.md#a0cd24dc49dbfe7f8cda02ee37d36529c)

struct ipc\_service\_cb cb

Event callback structure.

**Definition** ipc\_service.h:200

[ipc\_ept\_cfg::priv](structipc__ept__cfg.md#a4b14515e74e5429d62e13c0478070893)

void \* priv

Private user data.

**Definition** ipc\_service.h:203

[ipc\_ept\_cfg::name](structipc__ept__cfg.md#a6008673337256dc8a71052e121d2d0c6)

const char \* name

Name of the endpoint.

**Definition** ipc\_service.h:194

[ipc\_ept\_cfg::prio](structipc__ept__cfg.md#a8a85a116e7c0069121d4ef5dc9b55a4d)

int prio

Endpoint priority.

**Definition** ipc\_service.h:197

[ipc\_ept](structipc__ept.md)

Endpoint instance.

**Definition** ipc\_service.h:181

[ipc\_ept::token](structipc__ept.md#a234002020af2b8a2f31ff3727ecf0964)

void \* token

Backend-specific token used to identify an endpoint in an instance.

**Definition** ipc\_service.h:187

[ipc\_ept::instance](structipc__ept.md#a4f043fd1ed7df3e1774ba7639c2caf1d)

const struct device \* instance

Instance this endpoint belongs to.

**Definition** ipc\_service.h:184

[ipc\_service\_cb](structipc__service__cb.md)

Event callback structure.

**Definition** ipc\_service.h:145

[ipc\_service\_cb::bound](structipc__service__cb.md#a76be12bf8a7964977b5d7512dd010110)

void(\* bound)(void \*priv)

Bind was successful.

**Definition** ipc\_service.h:152

[ipc\_service\_cb::received](structipc__service__cb.md#a7b67edec6902fd6d8254ebfec4ee9fb5)

void(\* received)(const void \*data, size\_t len, void \*priv)

New packet arrived.

**Definition** ipc\_service.h:166

[ipc\_service\_cb::error](structipc__service__cb.md#ac40fd19ae5263f1880df1fe3dca55647)

void(\* error)(const char \*message, void \*priv)

An error occurred.

**Definition** ipc\_service.h:173

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [ipc](dir_a601f58076b93c8a02c94df35dc60a45.md)
- [ipc\_service.h](ipc__service_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
