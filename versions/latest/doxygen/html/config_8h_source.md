---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/config_8h_source.html
original_path: doxygen/html/config_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

[ 33](structhawkbit__runtime__config.md#aee3966a3387498d726ca960663b0b291) char \*[server\_addr](structhawkbit__runtime__config.md#aee3966a3387498d726ca960663b0b291);

[ 35](structhawkbit__runtime__config.md#a33343e076372adca50c1bab528881565) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [server\_port](structhawkbit__runtime__config.md#a33343e076372adca50c1bab528881565);

[ 37](structhawkbit__runtime__config.md#a519e5dbc87d0b472b87cb3dbf01a7807) char \*[auth\_token](structhawkbit__runtime__config.md#a519e5dbc87d0b472b87cb3dbf01a7807);

[ 39](structhawkbit__runtime__config.md#a1fb0307aaeb6107428ae279108057af3) [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) [tls\_tag](structhawkbit__runtime__config.md#a1fb0307aaeb6107428ae279108057af3);

40};

41

[ 49](group__hawkbit__config.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)int [hawkbit\_set\_config](group__hawkbit__config.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)(struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) \*config);

50

[ 56](group__hawkbit__config.md#gaae46014585251b53afe726d42475d739)struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) [hawkbit\_get\_config](group__hawkbit__config.md#gaae46014585251b53afe726d42475d739)(void);

57

[ 65](group__hawkbit__config.md#gaa49efdafe94e1d36a537aff962df41d5)static inline int [hawkbit\_set\_server\_addr](group__hawkbit__config.md#gaa49efdafe94e1d36a537aff962df41d5)(char \*addr\_str)

66{

67 struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) set\_config = {

68 .server\_addr = addr\_str,

69 .server\_port = 0,

70 .auth\_token = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4),

71 .tls\_tag = 0,

72 };

73

74 return [hawkbit\_set\_config](group__hawkbit__config.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)(&set\_config);

75}

76

[ 84](group__hawkbit__config.md#ga78ef6a168132940040ad04498f0b462d)static inline int [hawkbit\_set\_server\_port](group__hawkbit__config.md#ga78ef6a168132940040ad04498f0b462d)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) port)

85{

86 struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) set\_config = {

87 .server\_addr = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4),

88 .server\_port = port,

89 .auth\_token = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4),

90 .tls\_tag = 0,

91 };

92

93 return [hawkbit\_set\_config](group__hawkbit__config.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)(&set\_config);

94}

95

[ 103](group__hawkbit__config.md#gaa2799669246cc817bb8e294a8fbfb3d2)static inline int [hawkbit\_set\_ddi\_security\_token](group__hawkbit__config.md#gaa2799669246cc817bb8e294a8fbfb3d2)(char \*token)

104{

105 struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) set\_config = {

106 .server\_addr = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4),

107 .server\_port = 0,

108 .auth\_token = token,

109 .tls\_tag = 0,

110 };

111

112 return [hawkbit\_set\_config](group__hawkbit__config.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)(&set\_config);

113}

114

[ 122](group__hawkbit__config.md#ga5c73e9ba4dd9788e22fdb11f1f2b81ee)static inline int [hawkbit\_set\_tls\_tag](group__hawkbit__config.md#ga5c73e9ba4dd9788e22fdb11f1f2b81ee)([sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) tag)

123{

124 struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) set\_config = {

125 .server\_addr = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4),

126 .server\_port = 0,

127 .auth\_token = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4),

128 .tls\_tag = tag,

129 };

130

131 return [hawkbit\_set\_config](group__hawkbit__config.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)(&set\_config);

132}

133

[ 139](group__hawkbit__config.md#gacbbaed38e2ace7d8dcc78e40b286b5e9)static inline char \*[hawkbit\_get\_server\_addr](group__hawkbit__config.md#gacbbaed38e2ace7d8dcc78e40b286b5e9)(void)

140{

141 return [hawkbit\_get\_config](group__hawkbit__config.md#gaae46014585251b53afe726d42475d739)().[server\_addr](structhawkbit__runtime__config.md#aee3966a3387498d726ca960663b0b291);

142}

143

[ 149](group__hawkbit__config.md#ga3674fc406aa20fe4770ff0c729817b7c)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [hawkbit\_get\_server\_port](group__hawkbit__config.md#ga3674fc406aa20fe4770ff0c729817b7c)(void)

150{

151 return [hawkbit\_get\_config](group__hawkbit__config.md#gaae46014585251b53afe726d42475d739)().[server\_port](structhawkbit__runtime__config.md#a33343e076372adca50c1bab528881565);

152}

153

[ 159](group__hawkbit__config.md#gadc4aea2dac4915a434a10e6e055f54f7)static inline char \*[hawkbit\_get\_ddi\_security\_token](group__hawkbit__config.md#gadc4aea2dac4915a434a10e6e055f54f7)(void)

160{

161 return [hawkbit\_get\_config](group__hawkbit__config.md#gaae46014585251b53afe726d42475d739)().[auth\_token](structhawkbit__runtime__config.md#a519e5dbc87d0b472b87cb3dbf01a7807);

162}

163

[ 169](group__hawkbit__config.md#ga694e5f4fbcae451eb90a019f6d1f3b81)static inline [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) [hawkbit\_get\_tls\_tag](group__hawkbit__config.md#ga694e5f4fbcae451eb90a019f6d1f3b81)(void)

170{

171 return [hawkbit\_get\_config](group__hawkbit__config.md#gaae46014585251b53afe726d42475d739)().[tls\_tag](structhawkbit__runtime__config.md#a1fb0307aaeb6107428ae279108057af3);

172}

173

[ 179](group__hawkbit__config.md#ga0ca5f633e902137ecda068ab312d52db)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [hawkbit\_get\_action\_id](group__hawkbit__config.md#ga0ca5f633e902137ecda068ab312d52db)(void);

180

[ 186](group__hawkbit__config.md#ga46c56cee1a89abd81a328ef3f91648bb)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [hawkbit\_get\_poll\_interval](group__hawkbit__config.md#ga46c56cee1a89abd81a328ef3f91648bb)(void);

187

191

192#endif /\* ZEPHYR\_INCLUDE\_MGMT\_HAWKBIT\_CONFIG\_H\_ \*/

[hawkbit\_get\_action\_id](group__hawkbit__config.md#ga0ca5f633e902137ecda068ab312d52db)

int32\_t hawkbit\_get\_action\_id(void)

Get the hawkBit action id.

[hawkbit\_get\_server\_port](group__hawkbit__config.md#ga3674fc406aa20fe4770ff0c729817b7c)

static uint16\_t hawkbit\_get\_server\_port(void)

Get the hawkBit server port.

**Definition** config.h:149

[hawkbit\_get\_poll\_interval](group__hawkbit__config.md#ga46c56cee1a89abd81a328ef3f91648bb)

uint32\_t hawkbit\_get\_poll\_interval(void)

Get the hawkBit poll interval.

[hawkbit\_set\_tls\_tag](group__hawkbit__config.md#ga5c73e9ba4dd9788e22fdb11f1f2b81ee)

static int hawkbit\_set\_tls\_tag(sec\_tag\_t tag)

Set the hawkBit TLS tag.

**Definition** config.h:122

[hawkbit\_set\_config](group__hawkbit__config.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)

int hawkbit\_set\_config(struct hawkbit\_runtime\_config \*config)

Set the hawkBit server configuration settings.

[hawkbit\_get\_tls\_tag](group__hawkbit__config.md#ga694e5f4fbcae451eb90a019f6d1f3b81)

static sec\_tag\_t hawkbit\_get\_tls\_tag(void)

Get the hawkBit TLS tag.

**Definition** config.h:169

[hawkbit\_set\_server\_port](group__hawkbit__config.md#ga78ef6a168132940040ad04498f0b462d)

static int hawkbit\_set\_server\_port(uint16\_t port)

Set the hawkBit server port.

**Definition** config.h:84

[hawkbit\_set\_ddi\_security\_token](group__hawkbit__config.md#gaa2799669246cc817bb8e294a8fbfb3d2)

static int hawkbit\_set\_ddi\_security\_token(char \*token)

Set the hawkBit security token.

**Definition** config.h:103

[hawkbit\_set\_server\_addr](group__hawkbit__config.md#gaa49efdafe94e1d36a537aff962df41d5)

static int hawkbit\_set\_server\_addr(char \*addr\_str)

Set the hawkBit server address.

**Definition** config.h:65

[hawkbit\_get\_config](group__hawkbit__config.md#gaae46014585251b53afe726d42475d739)

struct hawkbit\_runtime\_config hawkbit\_get\_config(void)

Get the hawkBit server configuration settings.

[hawkbit\_get\_server\_addr](group__hawkbit__config.md#gacbbaed38e2ace7d8dcc78e40b286b5e9)

static char \* hawkbit\_get\_server\_addr(void)

Get the hawkBit server address.

**Definition** config.h:139

[hawkbit\_get\_ddi\_security\_token](group__hawkbit__config.md#gadc4aea2dac4915a434a10e6e055f54f7)

static char \* hawkbit\_get\_ddi\_security\_token(void)

Get the hawkBit security token.

**Definition** config.h:159

[sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3)

int sec\_tag\_t

Secure tag, a reference to TLS credential.

**Definition** tls\_credentials.h:74

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

**Definition** config.h:39

[hawkbit\_runtime\_config::server\_port](structhawkbit__runtime__config.md#a33343e076372adca50c1bab528881565)

uint16\_t server\_port

Server port.

**Definition** config.h:35

[hawkbit\_runtime\_config::auth\_token](structhawkbit__runtime__config.md#a519e5dbc87d0b472b87cb3dbf01a7807)

char \* auth\_token

Security token.

**Definition** config.h:37

[hawkbit\_runtime\_config::server\_addr](structhawkbit__runtime__config.md#aee3966a3387498d726ca960663b0b291)

char \* server\_addr

Server address.

**Definition** config.h:33

[tls\_credentials.h](tls__credentials_8h.md)

TLS credentials management.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [hawkbit](dir_a48dfaa3f142fb7c063e17169510ae85.md)
- [config.h](config_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
