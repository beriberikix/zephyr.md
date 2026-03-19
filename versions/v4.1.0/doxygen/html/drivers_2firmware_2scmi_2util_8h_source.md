---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2firmware_2scmi_2util_8h_source.html
original_path: doxygen/html/drivers_2firmware_2scmi_2util_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

util.h

[Go to the documentation of this file.](drivers_2firmware_2scmi_2util_8h.md)

1/\*

2 \* Copyright 2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_UTIL\_H\_

16#define \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_UTIL\_H\_

17

[ 29](drivers_2firmware_2scmi_2util_8h.md#af302a6f14883fa949e87a6784bf965fa)#define SCMI\_PROTOCOL\_NAME(proto) CONCAT(scmi\_protocol\_, proto)

30

31#ifdef CONFIG\_ARM\_SCMI\_TRANSPORT\_HAS\_STATIC\_CHANNELS

32

33#ifdef CONFIG\_ARM\_SCMI\_MAILBOX\_TRANSPORT

47#define DT\_SCMI\_TRANSPORT\_PROTO\_HAS\_CHAN(node\_id, idx)\

48 DT\_PROP\_HAS\_IDX(node\_id, shmem, idx)

49#else /\* CONFIG\_ARM\_SCMI\_MAILBOX\_TRANSPORT \*/

50#error "Transport with static channels needs to define HAS\_CHAN macro"

51#endif /\* CONFIG\_ARM\_SCMI\_MAILBOX\_TRANSPORT \*/

52

53#define SCMI\_TRANSPORT\_CHAN\_NAME(proto, idx) CONCAT(scmi\_channel\_, proto, \_, idx)

54

66#define DT\_SCMI\_TRANSPORT\_TX\_CHAN\_DECLARE(node\_id) \

67 COND\_CODE\_1(DT\_SCMI\_TRANSPORT\_PROTO\_HAS\_CHAN(node\_id, 0), \

68 (extern struct scmi\_channel \

69 SCMI\_TRANSPORT\_CHAN\_NAME(DT\_REG\_ADDR\_RAW(node\_id), 0);), \

70 (extern struct scmi\_channel \

71 SCMI\_TRANSPORT\_CHAN\_NAME(SCMI\_PROTOCOL\_BASE, 0);)) \

72

85#define DT\_SCMI\_TRANSPORT\_CHANNELS\_DECLARE(node\_id) \

86 DT\_SCMI\_TRANSPORT\_TX\_CHAN\_DECLARE(node\_id) \

87

96#define DT\_INST\_SCMI\_TRANSPORT\_CHANNELS\_DECLARE(inst) \

97 DT\_SCMI\_TRANSPORT\_CHANNELS\_DECLARE(DT\_INST(inst, DT\_DRV\_COMPAT))

98

111#define DT\_SCMI\_TRANSPORT\_TX\_CHAN(node\_id) \

112 COND\_CODE\_1(DT\_SCMI\_TRANSPORT\_PROTO\_HAS\_CHAN(node\_id, 0), \

113 (&SCMI\_TRANSPORT\_CHAN\_NAME(DT\_REG\_ADDR\_RAW(node\_id), 0)), \

114 (&SCMI\_TRANSPORT\_CHAN\_NAME(SCMI\_PROTOCOL\_BASE, 0)))

115

128#define DT\_SCMI\_TRANSPORT\_CHAN\_DEFINE(node\_id, idx, proto, pdata) \

129 struct scmi\_channel SCMI\_TRANSPORT\_CHAN\_NAME(proto, idx) = \

130 { \

131 .data = pdata, \

132 }

133

149#define DT\_SCMI\_PROTOCOL\_DATA\_DEFINE(node\_id, proto, pdata) \

150 STRUCT\_SECTION\_ITERABLE(scmi\_protocol, SCMI\_PROTOCOL\_NAME(proto)) = \

151 { \

152 .id = proto, \

153 .tx = DT\_SCMI\_TRANSPORT\_TX\_CHAN(node\_id), \

154 .data = pdata, \

155 }

156

157#else /\* CONFIG\_ARM\_SCMI\_TRANSPORT\_HAS\_STATIC\_CHANNELS \*/

158

[ 159](drivers_2firmware_2scmi_2util_8h.md#a97f0ff25400cf66fd042c6448578e9c9)#define DT\_SCMI\_TRANSPORT\_CHANNELS\_DECLARE(node\_id)

160

[ 161](drivers_2firmware_2scmi_2util_8h.md#a3ff1291335a98908b7b39fd441240f3f)#define DT\_SCMI\_PROTOCOL\_DATA\_DEFINE(node\_id, proto, pdata) \

162 STRUCT\_SECTION\_ITERABLE(scmi\_protocol, SCMI\_PROTOCOL\_NAME(proto)) = \

163 { \

164 .id = proto, \

165 .data = pdata, \

166 }

167

168#endif /\* CONFIG\_ARM\_SCMI\_TRANSPORT\_HAS\_STATIC\_CHANNELS \*/

169

[ 182](drivers_2firmware_2scmi_2util_8h.md#aff1d7e88df451d043dc2e4e9d39288b3)#define DT\_INST\_SCMI\_TRANSPORT\_DEFINE(inst, pm, data, config, level, prio, api) \

183 DEVICE\_DT\_INST\_DEFINE(inst, &scmi\_core\_transport\_init, \

184 pm, data, config, level, prio, api)

185

[ 211](drivers_2firmware_2scmi_2util_8h.md#a49ca976673495b6c86d5ac278df6c4a6)#define DT\_SCMI\_PROTOCOL\_DEFINE(node\_id, init\_fn, pm, data, config, \

212 level, prio, api) \

213 DT\_SCMI\_TRANSPORT\_CHANNELS\_DECLARE(node\_id) \

214 DT\_SCMI\_PROTOCOL\_DATA\_DEFINE(node\_id, DT\_REG\_ADDR\_RAW(node\_id), data); \

215 DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, \

216 &SCMI\_PROTOCOL\_NAME(DT\_REG\_ADDR\_RAW(node\_id)), \

217 config, level, prio, api)

218

[ 232](drivers_2firmware_2scmi_2util_8h.md#a702464dd535b0a58f7de037bfb295f11)#define DT\_INST\_SCMI\_PROTOCOL\_DEFINE(inst, init\_fn, pm, data, config, \

233 level, prio, api) \

234 DT\_SCMI\_PROTOCOL\_DEFINE(DT\_INST(inst, DT\_DRV\_COMPAT), init\_fn, pm, \

235 data, config, level, prio, api)

236

[ 248](drivers_2firmware_2scmi_2util_8h.md#a831662a70b3055f31cb53a9460e6c3da)#define DT\_SCMI\_PROTOCOL\_DEFINE\_NODEV(node\_id, data) \

249 DT\_SCMI\_TRANSPORT\_CHANNELS\_DECLARE(node\_id) \

250 DT\_SCMI\_PROTOCOL\_DATA\_DEFINE(node\_id, DT\_REG\_ADDR\_RAW(node\_id), data)

251

[ 264](drivers_2firmware_2scmi_2util_8h.md#a21b369f9fa6d1a965ece4a589df88581)#define SCMI\_FIELD\_MAKE(x, mask, shift)\

265 (((uint32\_t)(x) & (mask)) << (shift))

266

[ 275](drivers_2firmware_2scmi_2util_8h.md#aa7d5e12c8733162b93f2131fae0b9ff2)#define SCMI\_PROTOCOL\_BASE 16

[ 276](drivers_2firmware_2scmi_2util_8h.md#a7434da13fae02cd2e32b148c77258564)#define SCMI\_PROTOCOL\_POWER\_DOMAIN 17

[ 277](drivers_2firmware_2scmi_2util_8h.md#ab54b9be92cad1d9e35c20ea578daff14)#define SCMI\_PROTOCOL\_SYSTEM 18

[ 278](drivers_2firmware_2scmi_2util_8h.md#a516870afb06683cc717cd24f5ac70065)#define SCMI\_PROTOCOL\_PERF 19

[ 279](drivers_2firmware_2scmi_2util_8h.md#a69c4e6bc3b3a76fa86a4f25cfb0d9905)#define SCMI\_PROTOCOL\_CLOCK 20

[ 280](drivers_2firmware_2scmi_2util_8h.md#a50bd05b33b2b4915bd8e784542320d74)#define SCMI\_PROTOCOL\_SENSOR 21

[ 281](drivers_2firmware_2scmi_2util_8h.md#ab15815aabeb7f45670ec346144653f0e)#define SCMI\_PROTOCOL\_RESET\_DOMAIN 22

[ 282](drivers_2firmware_2scmi_2util_8h.md#ae8f54c2faae8340a25ddfb13789c7797)#define SCMI\_PROTOCOL\_VOLTAGE\_DOMAIN 23

[ 283](drivers_2firmware_2scmi_2util_8h.md#a4c6b58ea0571f9ef6bb2af29e23b0df8)#define SCMI\_PROTOCOL\_PCAP\_MONITOR 24

[ 284](drivers_2firmware_2scmi_2util_8h.md#a48e1ebf3dbc53685127bccccc50977cb)#define SCMI\_PROTOCOL\_PINCTRL 25

285

286#endif /\* \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_UTIL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [firmware](dir_e97f19a49725d52aae6eece65b856a75.md)
- [scmi](dir_b6bd1dece7d1578165357955ca5f0079.md)
- [util.h](drivers_2firmware_2scmi_2util_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
