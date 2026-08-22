---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/config_8h_source.html
original_path: doxygen/html/config_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

config.h

[Go to the documentation of this file.](config_8h.md)

1/\*

2 \* Copyright (c) 2024 Vogl Electronic GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

18

19#ifndef ZEPHYR\_INCLUDE\_MGMT\_HAWKBIT\_CONFIG\_H\_

20#define ZEPHYR\_INCLUDE\_MGMT\_HAWKBIT\_CONFIG\_H\_

21

22#include <[stdint.h](stdint_8h.md)>

23#include <[zephyr/net/tls\_credentials.h](tls__credentials_8h.md)>

24

[ 31](structhawkbit__runtime__config.md)struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) {

[ 36](structhawkbit__runtime__config.md#aee3966a3387498d726ca960663b0b291) char \*[server\_addr](structhawkbit__runtime__config.md#aee3966a3387498d726ca960663b0b291);

[ 38](structhawkbit__runtime__config.md#a3efc42d340461934b96a55ec6d5b91d2) char \*[server\_domain](structhawkbit__runtime__config.md#a3efc42d340461934b96a55ec6d5b91d2);

[ 40](structhawkbit__runtime__config.md#a33343e076372adca50c1bab528881565) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [server\_port](structhawkbit__runtime__config.md#a33343e076372adca50c1bab528881565);

[ 42](structhawkbit__runtime__config.md#a519e5dbc87d0b472b87cb3dbf01a7807) char \*[auth\_token](structhawkbit__runtime__config.md#a519e5dbc87d0b472b87cb3dbf01a7807);

[ 44](structhawkbit__runtime__config.md#a1fb0307aaeb6107428ae279108057af3) [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) [tls\_tag](structhawkbit__runtime__config.md#a1fb0307aaeb6107428ae279108057af3);

45};

46

[ 55](group__hawkbit__config.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)int [hawkbit\_set\_config](group__hawkbit__config.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)(struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) \*config);

56

[ 62](group__hawkbit__config.md#gaae46014585251b53afe726d42475d739)struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) [hawkbit\_get\_config](group__hawkbit__config.md#gaae46014585251b53afe726d42475d739)(void);

63

[ 72](group__hawkbit__config.md#ga2c6aa606a003b34538b521fda77af903)static inline int [hawkbit\_set\_server\_domain](group__hawkbit__config.md#ga2c6aa606a003b34538b521fda77af903)(char \*domain\_str)

73{

74 struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) set\_config = {

75 .server\_addr = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4),

76 .server\_domain = domain\_str,

77 .server\_port = 0,

78 .auth\_token = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4),

79 .tls\_tag = 0,

80 };

81

82 return [hawkbit\_set\_config](group__hawkbit__config.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)(&set\_config);

83}

84

[ 93](group__hawkbit__config.md#gaa49efdafe94e1d36a537aff962df41d5)static inline int [hawkbit\_set\_server\_addr](group__hawkbit__config.md#gaa49efdafe94e1d36a537aff962df41d5)(char \*addr\_str)

94{

95 struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) set\_config = {

96 .server\_addr = addr\_str,

97 .server\_domain = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4),

98 .server\_port = 0,

99 .auth\_token = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4),

100 .tls\_tag = 0,

101 };

102

103 return [hawkbit\_set\_config](group__hawkbit__config.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)(&set\_config);

104}

105

[ 113](group__hawkbit__config.md#ga78ef6a168132940040ad04498f0b462d)static inline int [hawkbit\_set\_server\_port](group__hawkbit__config.md#ga78ef6a168132940040ad04498f0b462d)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) port)

114{

115 struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) set\_config = {

116 .server\_addr = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4),

117 .server\_domain = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4),

118 .server\_port = port,

119 .auth\_token = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4),

120 .tls\_tag = 0,

121 };

122

123 return [hawkbit\_set\_config](group__hawkbit__config.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)(&set\_config);

124}

125

[ 133](group__hawkbit__config.md#gaa2799669246cc817bb8e294a8fbfb3d2)static inline int [hawkbit\_set\_ddi\_security\_token](group__hawkbit__config.md#gaa2799669246cc817bb8e294a8fbfb3d2)(char \*token)

134{

135 struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) set\_config = {

136 .server\_addr = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4),

137 .server\_domain = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4),

138 .server\_port = 0,

139 .auth\_token = token,

140 .tls\_tag = 0,

141 };

142

143 return [hawkbit\_set\_config](group__hawkbit__config.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)(&set\_config);

144}

145

[ 153](group__hawkbit__config.md#ga5c73e9ba4dd9788e22fdb11f1f2b81ee)static inline int [hawkbit\_set\_tls\_tag](group__hawkbit__config.md#ga5c73e9ba4dd9788e22fdb11f1f2b81ee)([sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) tag)

154{

155 struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) set\_config = {

156 .server\_addr = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4),

157 .server\_domain = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4),

158 .server\_port = 0,

159 .auth\_token = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4),

160 .tls\_tag = tag,

161 };

162

163 return [hawkbit\_set\_config](group__hawkbit__config.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)(&set\_config);

164}

165

[ 171](group__hawkbit__config.md#gacbbaed38e2ace7d8dcc78e40b286b5e9)static inline char \*[hawkbit\_get\_server\_addr](group__hawkbit__config.md#gacbbaed38e2ace7d8dcc78e40b286b5e9)(void)

172{

173 return [hawkbit\_get\_config](group__hawkbit__config.md#gaae46014585251b53afe726d42475d739)().[server\_addr](structhawkbit__runtime__config.md#aee3966a3387498d726ca960663b0b291);

174}

175

[ 181](group__hawkbit__config.md#gafd9f30b2acab65c34bcb5edaa3da8738)static inline char \*[hawkbit\_get\_server\_domain](group__hawkbit__config.md#gafd9f30b2acab65c34bcb5edaa3da8738)(void)

182{

183 return [hawkbit\_get\_config](group__hawkbit__config.md#gaae46014585251b53afe726d42475d739)().[server\_domain](structhawkbit__runtime__config.md#a3efc42d340461934b96a55ec6d5b91d2);

184}

185

[ 191](group__hawkbit__config.md#ga3674fc406aa20fe4770ff0c729817b7c)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [hawkbit\_get\_server\_port](group__hawkbit__config.md#ga3674fc406aa20fe4770ff0c729817b7c)(void)

192{

193 return [hawkbit\_get\_config](group__hawkbit__config.md#gaae46014585251b53afe726d42475d739)().[server\_port](structhawkbit__runtime__config.md#a33343e076372adca50c1bab528881565);

194}

195

[ 201](group__hawkbit__config.md#gadc4aea2dac4915a434a10e6e055f54f7)static inline char \*[hawkbit\_get\_ddi\_security\_token](group__hawkbit__config.md#gadc4aea2dac4915a434a10e6e055f54f7)(void)

202{

203 return [hawkbit\_get\_config](group__hawkbit__config.md#gaae46014585251b53afe726d42475d739)().[auth\_token](structhawkbit__runtime__config.md#a519e5dbc87d0b472b87cb3dbf01a7807);

204}

205

[ 211](group__hawkbit__config.md#ga694e5f4fbcae451eb90a019f6d1f3b81)static inline [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) [hawkbit\_get\_tls\_tag](group__hawkbit__config.md#ga694e5f4fbcae451eb90a019f6d1f3b81)(void)

212{

213 return [hawkbit\_get\_config](group__hawkbit__config.md#gaae46014585251b53afe726d42475d739)().[tls\_tag](structhawkbit__runtime__config.md#a1fb0307aaeb6107428ae279108057af3);

214}

215

[ 221](group__hawkbit__config.md#ga0ca5f633e902137ecda068ab312d52db)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [hawkbit\_get\_action\_id](group__hawkbit__config.md#ga0ca5f633e902137ecda068ab312d52db)(void);

222

[ 228](group__hawkbit__config.md#ga46c56cee1a89abd81a328ef3f91648bb)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [hawkbit\_get\_poll\_interval](group__hawkbit__config.md#ga46c56cee1a89abd81a328ef3f91648bb)(void);

229

233

234#endif /\* ZEPHYR\_INCLUDE\_MGMT\_HAWKBIT\_CONFIG\_H\_ \*/

[hawkbit\_get\_action\_id](group__hawkbit__config.md#ga0ca5f633e902137ecda068ab312d52db)

int32\_t hawkbit\_get\_action\_id(void)

Get the hawkBit action id.

[hawkbit\_set\_server\_domain](group__hawkbit__config.md#ga2c6aa606a003b34538b521fda77af903)

static int hawkbit\_set\_server\_domain(char \*domain\_str)

Set the hawkBit server hostname.

**Definition** config.h:72

[hawkbit\_get\_server\_port](group__hawkbit__config.md#ga3674fc406aa20fe4770ff0c729817b7c)

static uint16\_t hawkbit\_get\_server\_port(void)

Get the hawkBit server port.

**Definition** config.h:191

[hawkbit\_get\_poll\_interval](group__hawkbit__config.md#ga46c56cee1a89abd81a328ef3f91648bb)

uint32\_t hawkbit\_get\_poll\_interval(void)

Get the hawkBit poll interval.

[hawkbit\_set\_tls\_tag](group__hawkbit__config.md#ga5c73e9ba4dd9788e22fdb11f1f2b81ee)

static int hawkbit\_set\_tls\_tag(sec\_tag\_t tag)

Set the hawkBit TLS tag.

**Definition** config.h:153

[hawkbit\_set\_config](group__hawkbit__config.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)

int hawkbit\_set\_config(struct hawkbit\_runtime\_config \*config)

Set the hawkBit server configuration settings.

[hawkbit\_get\_tls\_tag](group__hawkbit__config.md#ga694e5f4fbcae451eb90a019f6d1f3b81)

static sec\_tag\_t hawkbit\_get\_tls\_tag(void)

Get the hawkBit TLS tag.

**Definition** config.h:211

[hawkbit\_set\_server\_port](group__hawkbit__config.md#ga78ef6a168132940040ad04498f0b462d)

static int hawkbit\_set\_server\_port(uint16\_t port)

Set the hawkBit server port.

**Definition** config.h:113

[hawkbit\_set\_ddi\_security\_token](group__hawkbit__config.md#gaa2799669246cc817bb8e294a8fbfb3d2)

static int hawkbit\_set\_ddi\_security\_token(char \*token)

Set the hawkBit security token.

**Definition** config.h:133

[hawkbit\_set\_server\_addr](group__hawkbit__config.md#gaa49efdafe94e1d36a537aff962df41d5)

static int hawkbit\_set\_server\_addr(char \*addr\_str)

Set the hawkBit server address.

**Definition** config.h:93

[hawkbit\_get\_config](group__hawkbit__config.md#gaae46014585251b53afe726d42475d739)

struct hawkbit\_runtime\_config hawkbit\_get\_config(void)

Get the hawkBit server configuration settings.

[hawkbit\_get\_server\_addr](group__hawkbit__config.md#gacbbaed38e2ace7d8dcc78e40b286b5e9)

static char \* hawkbit\_get\_server\_addr(void)

Get the hawkBit server address.

**Definition** config.h:171

[hawkbit\_get\_ddi\_security\_token](group__hawkbit__config.md#gadc4aea2dac4915a434a10e6e055f54f7)

static char \* hawkbit\_get\_ddi\_security\_token(void)

Get the hawkBit security token.

**Definition** config.h:201

[hawkbit\_get\_server\_domain](group__hawkbit__config.md#gafd9f30b2acab65c34bcb5edaa3da8738)

static char \* hawkbit\_get\_server\_domain(void)

Get the hawkBit server hostname.

**Definition** config.h:181

[sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3)

int sec\_tag\_t

Secure tag, a reference to TLS credential.

**Definition** tls\_credentials.h:80

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[hawkbit\_runtime\_config](structhawkbit__runtime__config.md)

hawkBit configuration structure.

**Definition** config.h:31

[hawkbit\_runtime\_config::tls\_tag](structhawkbit__runtime__config.md#a1fb0307aaeb6107428ae279108057af3)

sec\_tag\_t tls\_tag

TLS tag.

**Definition** config.h:44

[hawkbit\_runtime\_config::server\_port](structhawkbit__runtime__config.md#a33343e076372adca50c1bab528881565)

uint16\_t server\_port

Server port.

**Definition** config.h:40

[hawkbit\_runtime\_config::server\_domain](structhawkbit__runtime__config.md#a3efc42d340461934b96a55ec6d5b91d2)

char \* server\_domain

Server domain name.

**Definition** config.h:38

[hawkbit\_runtime\_config::auth\_token](structhawkbit__runtime__config.md#a519e5dbc87d0b472b87cb3dbf01a7807)

char \* auth\_token

Security token.

**Definition** config.h:42

[hawkbit\_runtime\_config::server\_addr](structhawkbit__runtime__config.md#aee3966a3387498d726ca960663b0b291)

char \* server\_addr

Server address (domain name or IP address if CONFIG\_HAWKBIT\_USE\_DOMAIN\_NAME is enabled).

**Definition** config.h:36

[tls\_credentials.h](tls__credentials_8h.md)

TLS credentials management.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [hawkbit](dir_a48dfaa3f142fb7c063e17169510ae85.md)
- [config.h](config_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
