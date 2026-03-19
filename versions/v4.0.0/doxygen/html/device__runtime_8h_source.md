---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/device__runtime_8h_source.html
original_path: doxygen/html/device__runtime_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

12#include <[zephyr/kernel.h](kernel_8h.md)>

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

[ 170](group__subsys__pm__device__runtime.md#gad643d0c63b7091cdfa68d6e99b6048a0)int [pm\_device\_runtime\_usage](group__subsys__pm__device__runtime.md#gad643d0c63b7091cdfa68d6e99b6048a0)(const struct [device](structdevice.md) \*dev);

171

172#else

173

174static inline int [pm\_device\_runtime\_auto\_enable](group__subsys__pm__device__runtime.md#gadc36f344b2cb40c33d5b37eefd120c98)(const struct [device](structdevice.md) \*dev)

175{

176 ARG\_UNUSED(dev);

177 return 0;

178}

179

180static inline int [pm\_device\_runtime\_enable](group__subsys__pm__device__runtime.md#gaabcd2cc694c9e201dd87bf42f02b454c)(const struct [device](structdevice.md) \*dev)

181{

182 ARG\_UNUSED(dev);

183 return 0;

184}

185

186static inline int [pm\_device\_runtime\_disable](group__subsys__pm__device__runtime.md#gaa7fc78138e282b0eae7da67876baee80)(const struct [device](structdevice.md) \*dev)

187{

188 ARG\_UNUSED(dev);

189 return 0;

190}

191

192static inline int [pm\_device\_runtime\_get](group__subsys__pm__device__runtime.md#ga530d4be65757fb2276ab6f631953e045)(const struct [device](structdevice.md) \*dev)

193{

194 ARG\_UNUSED(dev);

195 return 0;

196}

197

198static inline int [pm\_device\_runtime\_put](group__subsys__pm__device__runtime.md#ga98daba53a992fb6bd2c2b31cb445844f)(const struct [device](structdevice.md) \*dev)

199{

200 ARG\_UNUSED(dev);

201 return 0;

202}

203

204static inline int [pm\_device\_runtime\_put\_async](group__subsys__pm__device__runtime.md#ga9e90089b0ab78f365905418646e196c6)(const struct [device](structdevice.md) \*dev,

205 [k\_timeout\_t](structk__timeout__t.md) delay)

206{

207 ARG\_UNUSED(dev);

208 ARG\_UNUSED(delay);

209 return 0;

210}

211

212static inline bool [pm\_device\_runtime\_is\_enabled](group__subsys__pm__device__runtime.md#ga605cd2a3d0ea31efe6bd0b9a6f723219)(const struct [device](structdevice.md) \*dev)

213{

214 ARG\_UNUSED(dev);

215 return false;

216}

217

218static inline int [pm\_device\_runtime\_usage](group__subsys__pm__device__runtime.md#gad643d0c63b7091cdfa68d6e99b6048a0)(const struct [device](structdevice.md) \*dev)

219{

220 ARG\_UNUSED(dev);

221 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

222}

223

224#endif

225

227

228#ifdef \_\_cplusplus

229}

230#endif

231

232#endif /\* ZEPHYR\_INCLUDE\_PM\_DEVICE\_RUNTIME\_H\_ \*/

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

[pm\_device\_runtime\_usage](group__subsys__pm__device__runtime.md#gad643d0c63b7091cdfa68d6e99b6048a0)

int pm\_device\_runtime\_usage(const struct device \*dev)

Return the current device usage counter.

[pm\_device\_runtime\_auto\_enable](group__subsys__pm__device__runtime.md#gadc36f344b2cb40c33d5b37eefd120c98)

int pm\_device\_runtime\_auto\_enable(const struct device \*dev)

Automatically enable device runtime based on devicetree properties.

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[kernel.h](kernel_8h.md)

Public kernel APIs.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [pm](dir_7e6ac69b960794fd0df7b746be7e9a24.md)
- [device\_runtime.h](device__runtime_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
