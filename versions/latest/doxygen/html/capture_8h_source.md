---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/capture_8h_source.html
original_path: doxygen/html/capture_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

capture.h

[Go to the documentation of this file.](capture_8h.md)

1

6

7/\*

8 \* Copyright (c) 2021 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_CAPTURE\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_CAPTURE\_H\_

15

16#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

28

30

31struct [net\_if](structnet__if.md);

32struct [net\_pkt](structnet__pkt.md);

33struct [device](structdevice.md);

34

35struct net\_capture\_interface\_api {

39 int (\*cleanup)(const struct device \*dev);

40

42 int (\*enable)(const struct device \*dev, struct net\_if \*iface);

43

45 int (\*disable)(const struct device \*dev);

46

49 [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*is\_enabled)(const struct device \*dev);

50

52 int (\*[send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d))(const struct device \*dev, struct net\_if \*iface, struct net\_pkt \*pkt);

53};

54

56

[ 72](group__net__capture.md#gab280c0c6cc607bdb07211a9450eae262)int [net\_capture\_setup](group__net__capture.md#gab280c0c6cc607bdb07211a9450eae262)(const char \*remote\_addr, const char \*my\_local\_addr, const char \*peer\_addr,

73 const struct [device](structdevice.md) \*\*dev);

74

[ 86](group__net__capture.md#ga7a56719068938c34c9c6149296074d01)static inline int [net\_capture\_cleanup](group__net__capture.md#ga7a56719068938c34c9c6149296074d01)(const struct [device](structdevice.md) \*dev)

87{

88#if defined(CONFIG\_NET\_CAPTURE)

89 const struct net\_capture\_interface\_api \*api =

90 (const struct net\_capture\_interface\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

91

92 return api->cleanup(dev);

93#else

94 ARG\_UNUSED(dev);

95

96 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

97#endif

98}

99

[ 112](group__net__capture.md#gaf449c308080dc126e2e7c03b38d2a0aa)static inline int [net\_capture\_enable](group__net__capture.md#gaf449c308080dc126e2e7c03b38d2a0aa)(const struct [device](structdevice.md) \*dev, struct [net\_if](structnet__if.md) \*iface)

113{

114#if defined(CONFIG\_NET\_CAPTURE)

115 const struct net\_capture\_interface\_api \*api =

116 (const struct net\_capture\_interface\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

117

118 return api->enable(dev, iface);

119#else

120 ARG\_UNUSED(dev);

121 ARG\_UNUSED(iface);

122

123 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

124#endif

125}

126

[ 134](group__net__capture.md#ga651987b8b1e713865cff01412934f3cc)static inline bool [net\_capture\_is\_enabled](group__net__capture.md#ga651987b8b1e713865cff01412934f3cc)(const struct [device](structdevice.md) \*dev)

135{

136#if defined(CONFIG\_NET\_CAPTURE)

137 const struct net\_capture\_interface\_api \*api =

138 (const struct net\_capture\_interface\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

139

140 return api->is\_enabled(dev);

141#else

142 ARG\_UNUSED(dev);

143

144 return false;

145#endif

146}

147

[ 155](group__net__capture.md#ga32c66260fc888dcd38b6a3cffca3b951)static inline int [net\_capture\_disable](group__net__capture.md#ga32c66260fc888dcd38b6a3cffca3b951)(const struct [device](structdevice.md) \*dev)

156{

157#if defined(CONFIG\_NET\_CAPTURE)

158 const struct net\_capture\_interface\_api \*api =

159 (const struct net\_capture\_interface\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

160

161 return api->disable(dev);

162#else

163 ARG\_UNUSED(dev);

164

165 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

166#endif

167}

168

170

180static inline int net\_capture\_send(const struct [device](structdevice.md) \*dev, struct [net\_if](structnet__if.md) \*iface,

181 struct [net\_pkt](structnet__pkt.md) \*pkt)

182{

183#if defined(CONFIG\_NET\_CAPTURE)

184 const struct net\_capture\_interface\_api \*api =

185 (const struct net\_capture\_interface\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

186

187 return api->send(dev, iface, pkt);

188#else

189 ARG\_UNUSED(dev);

190 ARG\_UNUSED(iface);

191 ARG\_UNUSED(pkt);

192

193 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

194#endif

195}

196

204#if defined(CONFIG\_NET\_CAPTURE)

205void net\_capture\_pkt(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

206#else

207static inline void net\_capture\_pkt(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt)

208{

209 ARG\_UNUSED(iface);

210 ARG\_UNUSED(pkt);

211}

212#endif

213

214struct net\_capture\_info {

215 const struct device \*capture\_dev;

216 struct net\_if \*capture\_iface;

217 struct net\_if \*tunnel\_iface;

218 struct sockaddr \*peer;

219 struct sockaddr \*local;

220 bool is\_enabled;

221};

222

230typedef void (\*net\_capture\_cb\_t)(struct net\_capture\_info \*info, void \*user\_data);

231

241#if defined(CONFIG\_NET\_CAPTURE)

242void net\_capture\_foreach(net\_capture\_cb\_t cb, void \*user\_data);

243#else

244static inline void net\_capture\_foreach(net\_capture\_cb\_t cb, void \*user\_data)

245{

246 ARG\_UNUSED(cb);

247 ARG\_UNUSED(user\_data);

248}

249#endif

250

252

256

257#ifdef \_\_cplusplus

258}

259#endif

260

261#endif /\* ZEPHYR\_INCLUDE\_NET\_CAPTURE\_H\_ \*/

[send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d)

static ssize\_t send(int sock, const void \*buf, size\_t len, int flags)

POSIX wrapper for zsock\_send.

**Definition** socket.h:882

[net\_capture\_disable](group__net__capture.md#ga32c66260fc888dcd38b6a3cffca3b951)

static int net\_capture\_disable(const struct device \*dev)

Disable network packet capturing support.

**Definition** capture.h:155

[net\_capture\_is\_enabled](group__net__capture.md#ga651987b8b1e713865cff01412934f3cc)

static bool net\_capture\_is\_enabled(const struct device \*dev)

Is network packet capture enabled or disabled.

**Definition** capture.h:134

[net\_capture\_cleanup](group__net__capture.md#ga7a56719068938c34c9c6149296074d01)

static int net\_capture\_cleanup(const struct device \*dev)

Cleanup network packet capturing support.

**Definition** capture.h:86

[net\_capture\_setup](group__net__capture.md#gab280c0c6cc607bdb07211a9450eae262)

int net\_capture\_setup(const char \*remote\_addr, const char \*my\_local\_addr, const char \*peer\_addr, const struct device \*\*dev)

Setup network packet capturing support.

[net\_capture\_enable](group__net__capture.md#gaf449c308080dc126e2e7c03b38d2a0aa)

static int net\_capture\_enable(const struct device \*dev, struct net\_if \*iface)

Enable network packet capturing support.

**Definition** capture.h:112

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:115

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:615

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:63

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [capture.h](capture_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
