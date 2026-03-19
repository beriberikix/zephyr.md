---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ipc__service__backend_8h_source.html
original_path: doxygen/html/ipc__service__backend_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipc\_service\_backend.h

[Go to the documentation of this file.](ipc__service__backend_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_IPC\_SERVICE\_IPC\_SERVICE\_BACKEND\_H\_

8#define ZEPHYR\_INCLUDE\_IPC\_SERVICE\_IPC\_SERVICE\_BACKEND\_H\_

9

10#include <[zephyr/ipc/ipc\_service.h](ipc__service_8h.md)>

11#include <[zephyr/kernel.h](kernel_8h.md)>

12#include <[stdio.h](stdio_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

24

[ 29](structipc__service__backend.md)struct [ipc\_service\_backend](structipc__service__backend.md) {

[ 40](structipc__service__backend.md#ab8e9231fcff8f695af8ba396556af130) int (\*[open\_instance](structipc__service__backend.md#ab8e9231fcff8f695af8ba396556af130))(const struct [device](structdevice.md) \*instance);

41

[ 52](structipc__service__backend.md#a1368ba1e7e6f77650ef000688e79391f) int (\*[close\_instance](structipc__service__backend.md#a1368ba1e7e6f77650ef000688e79391f))(const struct [device](structdevice.md) \*instance);

53

[ 71](structipc__service__backend.md#a67d72d3331319fb966e31814c6bdec36) int (\*[send](structipc__service__backend.md#a67d72d3331319fb966e31814c6bdec36))(const struct [device](structdevice.md) \*instance, void \*token,

72 const void \*data, size\_t len);

73

[ 87](structipc__service__backend.md#ada6207ad7e97e415eeb7518b7163dc7e) int (\*[register\_endpoint](structipc__service__backend.md#ada6207ad7e97e415eeb7518b7163dc7e))(const struct [device](structdevice.md) \*instance,

88 void \*\*token,

89 const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \*cfg);

90

[ 104](structipc__service__backend.md#a275ede93b1a9f43da01fe40cfab5842c) int (\*[deregister\_endpoint](structipc__service__backend.md#a275ede93b1a9f43da01fe40cfab5842c))(const struct [device](structdevice.md) \*instance, void \*token);

105

[ 119](structipc__service__backend.md#a9d0a1aa2226a3370f1e0472aa2b0da3f) int (\*[get\_tx\_buffer\_size](structipc__service__backend.md#a9d0a1aa2226a3370f1e0472aa2b0da3f))(const struct [device](structdevice.md) \*instance, void \*token);

120

[ 141](structipc__service__backend.md#a915ae94af5acfd7c5dd9e9b9ac041970) int (\*[get\_tx\_buffer](structipc__service__backend.md#a915ae94af5acfd7c5dd9e9b9ac041970))(const struct [device](structdevice.md) \*instance, void \*token,

142 void \*\*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*len, [k\_timeout\_t](structk__timeout__t.md) wait);

143

[ 159](structipc__service__backend.md#ac05bbe12196b2d2de86b560770fad511) int (\*[drop\_tx\_buffer](structipc__service__backend.md#ac05bbe12196b2d2de86b560770fad511))(const struct [device](structdevice.md) \*instance, void \*token,

160 const void \*data);

161

[ 181](structipc__service__backend.md#a840aa60a50cfb6a3aae3b9f6c18c956d) int (\*[send\_nocopy](structipc__service__backend.md#a840aa60a50cfb6a3aae3b9f6c18c956d))(const struct [device](structdevice.md) \*instance, void \*token,

182 const void \*data, size\_t len);

183

[ 199](structipc__service__backend.md#a7a5e38fcadf2cc1b6ba9a30f8eed87e9) int (\*[hold\_rx\_buffer](structipc__service__backend.md#a7a5e38fcadf2cc1b6ba9a30f8eed87e9))(const struct [device](structdevice.md) \*instance, void \*token,

200 void \*data);

201

[ 217](structipc__service__backend.md#a9397c0497ef289c96701db8d0e3bdf26) int (\*[release\_rx\_buffer](structipc__service__backend.md#a9397c0497ef289c96701db8d0e3bdf26))(const struct [device](structdevice.md) \*instance, void \*token,

218 void \*data);

219};

220

224

225#ifdef \_\_cplusplus

226}

227#endif

228

229#endif /\* ZEPHYR\_INCLUDE\_IPC\_SERVICE\_IPC\_SERVICE\_BACKEND\_H\_ \*/

[ipc\_service.h](ipc__service_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[stdio.h](stdio_8h.md)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[ipc\_ept\_cfg](structipc__ept__cfg.md)

Endpoint configuration structure.

**Definition** ipc\_service.h:206

[ipc\_service\_backend](structipc__service__backend.md)

IPC backend configuration structure.

**Definition** ipc\_service\_backend.h:29

[ipc\_service\_backend::close\_instance](structipc__service__backend.md#a1368ba1e7e6f77650ef000688e79391f)

int(\* close\_instance)(const struct device \*instance)

Pointer to the function that will be used to close an instance.

**Definition** ipc\_service\_backend.h:52

[ipc\_service\_backend::deregister\_endpoint](structipc__service__backend.md#a275ede93b1a9f43da01fe40cfab5842c)

int(\* deregister\_endpoint)(const struct device \*instance, void \*token)

Pointer to the function that will be used to deregister endpoints.

**Definition** ipc\_service\_backend.h:104

[ipc\_service\_backend::send](structipc__service__backend.md#a67d72d3331319fb966e31814c6bdec36)

int(\* send)(const struct device \*instance, void \*token, const void \*data, size\_t len)

Pointer to the function that will be used to send data to the endpoint.

**Definition** ipc\_service\_backend.h:71

[ipc\_service\_backend::hold\_rx\_buffer](structipc__service__backend.md#a7a5e38fcadf2cc1b6ba9a30f8eed87e9)

int(\* hold\_rx\_buffer)(const struct device \*instance, void \*token, void \*data)

Pointer to the function that will hold the RX buffer.

**Definition** ipc\_service\_backend.h:199

[ipc\_service\_backend::send\_nocopy](structipc__service__backend.md#a840aa60a50cfb6a3aae3b9f6c18c956d)

int(\* send\_nocopy)(const struct device \*instance, void \*token, const void \*data, size\_t len)

Pointer to the function that will be used to send data to the endpoint when the TX buffer has been ob...

**Definition** ipc\_service\_backend.h:181

[ipc\_service\_backend::get\_tx\_buffer](structipc__service__backend.md#a915ae94af5acfd7c5dd9e9b9ac041970)

int(\* get\_tx\_buffer)(const struct device \*instance, void \*token, void \*\*data, uint32\_t \*len, k\_timeout\_t wait)

Pointer to the function that will return an empty TX buffer.

**Definition** ipc\_service\_backend.h:141

[ipc\_service\_backend::release\_rx\_buffer](structipc__service__backend.md#a9397c0497ef289c96701db8d0e3bdf26)

int(\* release\_rx\_buffer)(const struct device \*instance, void \*token, void \*data)

Pointer to the function that will release the RX buffer.

**Definition** ipc\_service\_backend.h:217

[ipc\_service\_backend::get\_tx\_buffer\_size](structipc__service__backend.md#a9d0a1aa2226a3370f1e0472aa2b0da3f)

int(\* get\_tx\_buffer\_size)(const struct device \*instance, void \*token)

Pointer to the function that will return the TX buffer size.

**Definition** ipc\_service\_backend.h:119

[ipc\_service\_backend::open\_instance](structipc__service__backend.md#ab8e9231fcff8f695af8ba396556af130)

int(\* open\_instance)(const struct device \*instance)

Pointer to the function that will be used to open an instance.

**Definition** ipc\_service\_backend.h:40

[ipc\_service\_backend::drop\_tx\_buffer](structipc__service__backend.md#ac05bbe12196b2d2de86b560770fad511)

int(\* drop\_tx\_buffer)(const struct device \*instance, void \*token, const void \*data)

Pointer to the function that will drop a TX buffer.

**Definition** ipc\_service\_backend.h:159

[ipc\_service\_backend::register\_endpoint](structipc__service__backend.md#ada6207ad7e97e415eeb7518b7163dc7e)

int(\* register\_endpoint)(const struct device \*instance, void \*\*token, const struct ipc\_ept\_cfg \*cfg)

Pointer to the function that will be used to register endpoints.

**Definition** ipc\_service\_backend.h:87

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [ipc](dir_a601f58076b93c8a02c94df35dc60a45.md)
- [ipc\_service\_backend.h](ipc__service__backend_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
