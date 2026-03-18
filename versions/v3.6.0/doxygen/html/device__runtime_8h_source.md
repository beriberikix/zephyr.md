---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/device__runtime_8h_source.html
original_path: doxygen/html/device__runtime_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

device\_runtime.h

[Go to the documentation of this file.](device__runtime_8h.md)

1/\*

2 \* Copyright (c) 2015 Intel Corporation.

3 \* Copyright (c) 2021 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_PM\_DEVICE\_RUNTIME\_H\_

9#define ZEPHYR\_INCLUDE\_PM\_DEVICE\_RUNTIME\_H\_

10

11#include <[zephyr/device.h](device_8h.md)>

12#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

24

25#if defined(CONFIG\_PM\_DEVICE\_RUNTIME) || defined(\_\_DOXYGEN\_\_)

[ 38](group__subsys__pm__device__runtime.md#gadc36f344b2cb40c33d5b37eefd120c98)int [pm\_device\_runtime\_auto\_enable](group__subsys__pm__device__runtime.md#gadc36f344b2cb40c33d5b37eefd120c98)(const struct [device](structdevice.md) \*dev);

39

[ 57](group__subsys__pm__device__runtime.md#gaabcd2cc694c9e201dd87bf42f02b454c)int [pm\_device\_runtime\_enable](group__subsys__pm__device__runtime.md#gaabcd2cc694c9e201dd87bf42f02b454c)(const struct [device](structdevice.md) \*dev);

58

[ 72](group__subsys__pm__device__runtime.md#gaa7fc78138e282b0eae7da67876baee80)int [pm\_device\_runtime\_disable](group__subsys__pm__device__runtime.md#gaa7fc78138e282b0eae7da67876baee80)(const struct [device](structdevice.md) \*dev);

73

[ 97](group__subsys__pm__device__runtime.md#ga530d4be65757fb2276ab6f631953e045)int [pm\_device\_runtime\_get](group__subsys__pm__device__runtime.md#ga530d4be65757fb2276ab6f631953e045)(const struct [device](structdevice.md) \*dev);

98

[ 119](group__subsys__pm__device__runtime.md#ga98daba53a992fb6bd2c2b31cb445844f)int [pm\_device\_runtime\_put](group__subsys__pm__device__runtime.md#ga98daba53a992fb6bd2c2b31cb445844f)(const struct [device](structdevice.md) \*dev);

120

[ 145](group__subsys__pm__device__runtime.md#ga9e90089b0ab78f365905418646e196c6)int [pm\_device\_runtime\_put\_async](group__subsys__pm__device__runtime.md#ga9e90089b0ab78f365905418646e196c6)(const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) delay);

146

[ 159](group__subsys__pm__device__runtime.md#ga605cd2a3d0ea31efe6bd0b9a6f723219)bool [pm\_device\_runtime\_is\_enabled](group__subsys__pm__device__runtime.md#ga605cd2a3d0ea31efe6bd0b9a6f723219)(const struct [device](structdevice.md) \*dev);

160

161#else

162

163static inline int [pm\_device\_runtime\_auto\_enable](group__subsys__pm__device__runtime.md#gadc36f344b2cb40c33d5b37eefd120c98)(const struct [device](structdevice.md) \*dev)

164{

165 ARG\_UNUSED(dev);

166 return 0;

167}

168

169static inline int [pm\_device\_runtime\_enable](group__subsys__pm__device__runtime.md#gaabcd2cc694c9e201dd87bf42f02b454c)(const struct [device](structdevice.md) \*dev)

170{

171 ARG\_UNUSED(dev);

172 return 0;

173}

174

175static inline int [pm\_device\_runtime\_disable](group__subsys__pm__device__runtime.md#gaa7fc78138e282b0eae7da67876baee80)(const struct [device](structdevice.md) \*dev)

176{

177 ARG\_UNUSED(dev);

178 return 0;

179}

180

181static inline int [pm\_device\_runtime\_get](group__subsys__pm__device__runtime.md#ga530d4be65757fb2276ab6f631953e045)(const struct [device](structdevice.md) \*dev)

182{

183 ARG\_UNUSED(dev);

184 return 0;

185}

186

187static inline int [pm\_device\_runtime\_put](group__subsys__pm__device__runtime.md#ga98daba53a992fb6bd2c2b31cb445844f)(const struct [device](structdevice.md) \*dev)

188{

189 ARG\_UNUSED(dev);

190 return 0;

191}

192

193static inline int [pm\_device\_runtime\_put\_async](group__subsys__pm__device__runtime.md#ga9e90089b0ab78f365905418646e196c6)(const struct [device](structdevice.md) \*dev,

194 [k\_timeout\_t](structk__timeout__t.md) delay)

195{

196 ARG\_UNUSED(dev);

197 ARG\_UNUSED(delay);

198 return 0;

199}

200

201static inline bool [pm\_device\_runtime\_is\_enabled](group__subsys__pm__device__runtime.md#ga605cd2a3d0ea31efe6bd0b9a6f723219)(const struct [device](structdevice.md) \*dev)

202{

203 ARG\_UNUSED(dev);

204 return false;

205}

206

207#endif

208

210

211#ifdef \_\_cplusplus

212}

213#endif

214

215#endif /\* ZEPHYR\_INCLUDE\_PM\_DEVICE\_RUNTIME\_H\_ \*/

[device.h](device_8h.md)

[pm\_device\_runtime\_get](group__subsys__pm__device__runtime.md#ga530d4be65757fb2276ab6f631953e045)

int pm\_device\_runtime\_get(const struct device \*dev)

Resume a device based on usage count.

[pm\_device\_runtime\_is\_enabled](group__subsys__pm__device__runtime.md#ga605cd2a3d0ea31efe6bd0b9a6f723219)

bool pm\_device\_runtime\_is\_enabled(const struct device \*dev)

Check if device runtime is enabled for a given device.

[pm\_device\_runtime\_put](group__subsys__pm__device__runtime.md#ga98daba53a992fb6bd2c2b31cb445844f)

int pm\_device\_runtime\_put(const struct device \*dev)

Suspend a device based on usage count.

[pm\_device\_runtime\_put\_async](group__subsys__pm__device__runtime.md#ga9e90089b0ab78f365905418646e196c6)

int pm\_device\_runtime\_put\_async(const struct device \*dev, k\_timeout\_t delay)

Suspend a device based on usage count (asynchronously).

[pm\_device\_runtime\_disable](group__subsys__pm__device__runtime.md#gaa7fc78138e282b0eae7da67876baee80)

int pm\_device\_runtime\_disable(const struct device \*dev)

Disable device runtime PM.

[pm\_device\_runtime\_enable](group__subsys__pm__device__runtime.md#gaabcd2cc694c9e201dd87bf42f02b454c)

int pm\_device\_runtime\_enable(const struct device \*dev)

Enable device runtime PM.

[pm\_device\_runtime\_auto\_enable](group__subsys__pm__device__runtime.md#gadc36f344b2cb40c33d5b37eefd120c98)

int pm\_device\_runtime\_auto\_enable(const struct device \*dev)

Automatically enable device runtime based on devicetree properties.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [pm](dir_7e6ac69b960794fd0df7b746be7e9a24.md)
- [device\_runtime.h](device__runtime_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
