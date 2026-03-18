---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/hawkbit_8h_source.html
original_path: doxygen/html/hawkbit_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hawkbit.h

[Go to the documentation of this file.](hawkbit_8h.md)

1/\*

2 \* Copyright (c) 2020 Linumiz

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13#ifndef ZEPHYR\_INCLUDE\_MGMT\_HAWKBIT\_H\_

14#define ZEPHYR\_INCLUDE\_MGMT\_HAWKBIT\_H\_

15

16#include <[zephyr/net/tls\_credentials.h](tls__credentials_8h.md)>

17

[ 18](group__hawkbit.md#gae2550864ddf596fe544052af73dc1dba)#define HAWKBIT\_JSON\_URL "/default/controller/v1"

19

[ 28](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b)enum [hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b) {

[ 29](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba5a36eadcadc43c1fd0936a8546fb15e8) [HAWKBIT\_NETWORKING\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba5a36eadcadc43c1fd0936a8546fb15e8),

[ 30](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bad4b0587da0bdfd829d0d08ed2407357d) [HAWKBIT\_UNCONFIRMED\_IMAGE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bad4b0587da0bdfd829d0d08ed2407357d),

[ 31](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba1d79e6fe8487cc4dc36c6c91bcabd124) [HAWKBIT\_PERMISSION\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba1d79e6fe8487cc4dc36c6c91bcabd124),

[ 32](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba2b7d188d8c28a3373d9b8a7f831b1e3a) [HAWKBIT\_METADATA\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba2b7d188d8c28a3373d9b8a7f831b1e3a),

[ 33](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220baf1a448b0addfc769515c725ce5b1bab9) [HAWKBIT\_DOWNLOAD\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220baf1a448b0addfc769515c725ce5b1bab9),

[ 34](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba6af6cd1b834d74a5298f4b3626b48ad3) [HAWKBIT\_OK](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba6af6cd1b834d74a5298f4b3626b48ad3),

[ 35](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba9f5a200928474863a88d170c11594048) [HAWKBIT\_UPDATE\_INSTALLED](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba9f5a200928474863a88d170c11594048),

[ 36](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bac73c46deb3e54dba690f814a2fb9db71) [HAWKBIT\_NO\_UPDATE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bac73c46deb3e54dba690f814a2fb9db71),

[ 37](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba9d677899d5ff00957dfeab70f484863f) [HAWKBIT\_CANCEL\_UPDATE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba9d677899d5ff00957dfeab70f484863f),

[ 38](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bac4ba42120229e92b52c82d4a4d4cd708) [HAWKBIT\_NOT\_INITIALIZED](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bac4ba42120229e92b52c82d4a4d4cd708),

[ 39](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba28ccbb4060d41592884829cf205414f6) [HAWKBIT\_PROBE\_IN\_PROGRESS](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba28ccbb4060d41592884829cf205414f6),

40};

41

[ 48](structhawkbit__runtime__config.md)struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) {

[ 49](structhawkbit__runtime__config.md#aee3966a3387498d726ca960663b0b291) char \*[server\_addr](structhawkbit__runtime__config.md#aee3966a3387498d726ca960663b0b291);

[ 50](structhawkbit__runtime__config.md#a33343e076372adca50c1bab528881565) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [server\_port](structhawkbit__runtime__config.md#a33343e076372adca50c1bab528881565);

[ 51](structhawkbit__runtime__config.md#a519e5dbc87d0b472b87cb3dbf01a7807) char \*[auth\_token](structhawkbit__runtime__config.md#a519e5dbc87d0b472b87cb3dbf01a7807);

[ 52](structhawkbit__runtime__config.md#a1fb0307aaeb6107428ae279108057af3) [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) [tls\_tag](structhawkbit__runtime__config.md#a1fb0307aaeb6107428ae279108057af3);

53};

54

[ 66](group__hawkbit.md#ga2774769ec44f2793895b5d783b4dceda)typedef int (\*[hawkbit\_config\_device\_data\_cb\_handler\_t](group__hawkbit.md#ga2774769ec44f2793895b5d783b4dceda))(const char \*device\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer,

67 const size\_t buffer\_size);

68

[ 80](group__hawkbit.md#gad8e83255a969eb61244b1edfd0b95e5d)int [hawkbit\_set\_custom\_data\_cb](group__hawkbit.md#gad8e83255a969eb61244b1edfd0b95e5d)([hawkbit\_config\_device\_data\_cb\_handler\_t](group__hawkbit.md#ga2774769ec44f2793895b5d783b4dceda) cb);

81

[ 88](group__hawkbit.md#ga0ef6151f205088405de242e012984ca6)int [hawkbit\_init](group__hawkbit.md#ga0ef6151f205088405de242e012984ca6)(void);

89

[ 96](group__hawkbit.md#gac077f546d8947d6b55dcb9276ce98283)void [hawkbit\_autohandler](group__hawkbit.md#gac077f546d8947d6b55dcb9276ce98283)(void);

97

[ 113](group__hawkbit.md#ga525173f0c3d0ca4e26124a34d098d0b9)enum [hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b) [hawkbit\_probe](group__hawkbit.md#ga525173f0c3d0ca4e26124a34d098d0b9)(void);

114

[ 118](group__hawkbit.md#ga03631b12a4107d660bac14bfd33bfebd)void [hawkbit\_reboot](group__hawkbit.md#ga03631b12a4107d660bac14bfd33bfebd)(void);

119

[ 126](group__hawkbit.md#ga154220c632a7594c0630cdcd79385055)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[hawkbit\_get\_device\_identity\_cb\_handler\_t](group__hawkbit.md#ga154220c632a7594c0630cdcd79385055))(char \*id, int id\_max\_len);

127

[ 138](group__hawkbit.md#ga4ce085b8f2bb46af2c2e9f3f2879d633)int [hawkbit\_set\_device\_identity\_cb](group__hawkbit.md#ga4ce085b8f2bb46af2c2e9f3f2879d633)([hawkbit\_get\_device\_identity\_cb\_handler\_t](group__hawkbit.md#ga154220c632a7594c0630cdcd79385055) cb);

139

[ 147](group__hawkbit.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)int [hawkbit\_set\_config](group__hawkbit.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)(struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) \*config);

148

[ 154](group__hawkbit.md#gaae46014585251b53afe726d42475d739)struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) [hawkbit\_get\_config](group__hawkbit.md#gaae46014585251b53afe726d42475d739)(void);

155

[ 163](group__hawkbit.md#gaa49efdafe94e1d36a537aff962df41d5)static inline int [hawkbit\_set\_server\_addr](group__hawkbit.md#gaa49efdafe94e1d36a537aff962df41d5)(char \*addr\_str)

164{

165 struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) set\_config = {

166 .server\_addr = addr\_str, .server\_port = 0, .auth\_token = NULL, .tls\_tag = 0};

167

168 return [hawkbit\_set\_config](group__hawkbit.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)(&set\_config);

169}

170

[ 178](group__hawkbit.md#ga78ef6a168132940040ad04498f0b462d)static inline int [hawkbit\_set\_server\_port](group__hawkbit.md#ga78ef6a168132940040ad04498f0b462d)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) port)

179{

180 struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) set\_config = {

181 .server\_addr = NULL, .server\_port = port, .auth\_token = NULL, .tls\_tag = 0};

182

183 return [hawkbit\_set\_config](group__hawkbit.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)(&set\_config);

184}

185

[ 193](group__hawkbit.md#gaa2799669246cc817bb8e294a8fbfb3d2)static inline int [hawkbit\_set\_ddi\_security\_token](group__hawkbit.md#gaa2799669246cc817bb8e294a8fbfb3d2)(char \*token)

194{

195 struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) set\_config = {

196 .server\_addr = NULL, .server\_port = 0, .auth\_token = token, .tls\_tag = 0};

197

198 return [hawkbit\_set\_config](group__hawkbit.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)(&set\_config);

199}

200

[ 208](group__hawkbit.md#ga5c73e9ba4dd9788e22fdb11f1f2b81ee)static inline int [hawkbit\_set\_tls\_tag](group__hawkbit.md#ga5c73e9ba4dd9788e22fdb11f1f2b81ee)([sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) tag)

209{

210 struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) set\_config = {

211 .server\_addr = NULL, .server\_port = 0, .auth\_token = NULL, .tls\_tag = tag};

212

213 return [hawkbit\_set\_config](group__hawkbit.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)(&set\_config);

214}

215

[ 221](group__hawkbit.md#gacbbaed38e2ace7d8dcc78e40b286b5e9)static inline char \*[hawkbit\_get\_server\_addr](group__hawkbit.md#gacbbaed38e2ace7d8dcc78e40b286b5e9)(void)

222{

223 return [hawkbit\_get\_config](group__hawkbit.md#gaae46014585251b53afe726d42475d739)().[server\_addr](structhawkbit__runtime__config.md#aee3966a3387498d726ca960663b0b291);

224}

225

[ 231](group__hawkbit.md#ga3674fc406aa20fe4770ff0c729817b7c)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [hawkbit\_get\_server\_port](group__hawkbit.md#ga3674fc406aa20fe4770ff0c729817b7c)(void)

232{

233 return [hawkbit\_get\_config](group__hawkbit.md#gaae46014585251b53afe726d42475d739)().[server\_port](structhawkbit__runtime__config.md#a33343e076372adca50c1bab528881565);

234}

235

[ 241](group__hawkbit.md#gadc4aea2dac4915a434a10e6e055f54f7)static inline char \*[hawkbit\_get\_ddi\_security\_token](group__hawkbit.md#gadc4aea2dac4915a434a10e6e055f54f7)(void)

242{

243 return [hawkbit\_get\_config](group__hawkbit.md#gaae46014585251b53afe726d42475d739)().[auth\_token](structhawkbit__runtime__config.md#a519e5dbc87d0b472b87cb3dbf01a7807);

244}

245

[ 251](group__hawkbit.md#ga694e5f4fbcae451eb90a019f6d1f3b81)static inline [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) [hawkbit\_get\_tls\_tag](group__hawkbit.md#ga694e5f4fbcae451eb90a019f6d1f3b81)(void)

252{

253 return [hawkbit\_get\_config](group__hawkbit.md#gaae46014585251b53afe726d42475d739)().[tls\_tag](structhawkbit__runtime__config.md#a1fb0307aaeb6107428ae279108057af3);

254}

255

[ 262](group__hawkbit.md#ga0ca5f633e902137ecda068ab312d52db)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [hawkbit\_get\_action\_id](group__hawkbit.md#ga0ca5f633e902137ecda068ab312d52db)(void);

263

[ 274](group__hawkbit.md#ga26f0066c87c57b500170ac377b560bb4)int [hawkbit\_reset\_action\_id](group__hawkbit.md#ga26f0066c87c57b500170ac377b560bb4)(void);

275

279

280#endif /\* \_HAWKBIT\_H\_ \*/

[hawkbit\_reboot](group__hawkbit.md#ga03631b12a4107d660bac14bfd33bfebd)

void hawkbit\_reboot(void)

Request system to reboot.

[hawkbit\_get\_action\_id](group__hawkbit.md#ga0ca5f633e902137ecda068ab312d52db)

int32\_t hawkbit\_get\_action\_id(void)

Get the hawkBit action id.

[hawkbit\_init](group__hawkbit.md#ga0ef6151f205088405de242e012984ca6)

int hawkbit\_init(void)

Init the flash partition.

[hawkbit\_get\_device\_identity\_cb\_handler\_t](group__hawkbit.md#ga154220c632a7594c0630cdcd79385055)

bool(\* hawkbit\_get\_device\_identity\_cb\_handler\_t)(char \*id, int id\_max\_len)

Callback to get the device identity.

**Definition** hawkbit.h:126

[hawkbit\_reset\_action\_id](group__hawkbit.md#ga26f0066c87c57b500170ac377b560bb4)

int hawkbit\_reset\_action\_id(void)

Resets the hawkBit action id, that is saved in settings.

[hawkbit\_config\_device\_data\_cb\_handler\_t](group__hawkbit.md#ga2774769ec44f2793895b5d783b4dceda)

int(\* hawkbit\_config\_device\_data\_cb\_handler\_t)(const char \*device\_id, uint8\_t \*buffer, const size\_t buffer\_size)

Callback to provide the custom data to the hawkBit server.

**Definition** hawkbit.h:66

[hawkbit\_get\_server\_port](group__hawkbit.md#ga3674fc406aa20fe4770ff0c729817b7c)

static uint16\_t hawkbit\_get\_server\_port(void)

Get the hawkBit server port.

**Definition** hawkbit.h:231

[hawkbit\_set\_device\_identity\_cb](group__hawkbit.md#ga4ce085b8f2bb46af2c2e9f3f2879d633)

int hawkbit\_set\_device\_identity\_cb(hawkbit\_get\_device\_identity\_cb\_handler\_t cb)

Set the device identity callback.

[hawkbit\_probe](group__hawkbit.md#ga525173f0c3d0ca4e26124a34d098d0b9)

enum hawkbit\_response hawkbit\_probe(void)

The hawkBit probe verify if there is some update to be performed.

[hawkbit\_set\_tls\_tag](group__hawkbit.md#ga5c73e9ba4dd9788e22fdb11f1f2b81ee)

static int hawkbit\_set\_tls\_tag(sec\_tag\_t tag)

Set the hawkBit TLS tag.

**Definition** hawkbit.h:208

[hawkbit\_set\_config](group__hawkbit.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)

int hawkbit\_set\_config(struct hawkbit\_runtime\_config \*config)

Set the hawkBit server configuration settings.

[hawkbit\_get\_tls\_tag](group__hawkbit.md#ga694e5f4fbcae451eb90a019f6d1f3b81)

static sec\_tag\_t hawkbit\_get\_tls\_tag(void)

Get the hawkBit TLS tag.

**Definition** hawkbit.h:251

[hawkbit\_set\_server\_port](group__hawkbit.md#ga78ef6a168132940040ad04498f0b462d)

static int hawkbit\_set\_server\_port(uint16\_t port)

Set the hawkBit server port.

**Definition** hawkbit.h:178

[hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b)

hawkbit\_response

Response message from hawkBit.

**Definition** hawkbit.h:28

[hawkbit\_set\_ddi\_security\_token](group__hawkbit.md#gaa2799669246cc817bb8e294a8fbfb3d2)

static int hawkbit\_set\_ddi\_security\_token(char \*token)

Set the hawkBit security token.

**Definition** hawkbit.h:193

[hawkbit\_set\_server\_addr](group__hawkbit.md#gaa49efdafe94e1d36a537aff962df41d5)

static int hawkbit\_set\_server\_addr(char \*addr\_str)

Set the hawkBit server address.

**Definition** hawkbit.h:163

[hawkbit\_get\_config](group__hawkbit.md#gaae46014585251b53afe726d42475d739)

struct hawkbit\_runtime\_config hawkbit\_get\_config(void)

Get the hawkBit server configuration settings.

[hawkbit\_autohandler](group__hawkbit.md#gac077f546d8947d6b55dcb9276ce98283)

void hawkbit\_autohandler(void)

Runs hawkBit probe and hawkBit update automatically.

[hawkbit\_get\_server\_addr](group__hawkbit.md#gacbbaed38e2ace7d8dcc78e40b286b5e9)

static char \* hawkbit\_get\_server\_addr(void)

Get the hawkBit server address.

**Definition** hawkbit.h:221

[hawkbit\_set\_custom\_data\_cb](group__hawkbit.md#gad8e83255a969eb61244b1edfd0b95e5d)

int hawkbit\_set\_custom\_data\_cb(hawkbit\_config\_device\_data\_cb\_handler\_t cb)

Set the custom data callback.

[hawkbit\_get\_ddi\_security\_token](group__hawkbit.md#gadc4aea2dac4915a434a10e6e055f54f7)

static char \* hawkbit\_get\_ddi\_security\_token(void)

Get the hawkBit security token.

**Definition** hawkbit.h:241

[HAWKBIT\_PERMISSION\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba1d79e6fe8487cc4dc36c6c91bcabd124)

@ HAWKBIT\_PERMISSION\_ERROR

**Definition** hawkbit.h:31

[HAWKBIT\_PROBE\_IN\_PROGRESS](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba28ccbb4060d41592884829cf205414f6)

@ HAWKBIT\_PROBE\_IN\_PROGRESS

**Definition** hawkbit.h:39

[HAWKBIT\_METADATA\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba2b7d188d8c28a3373d9b8a7f831b1e3a)

@ HAWKBIT\_METADATA\_ERROR

**Definition** hawkbit.h:32

[HAWKBIT\_NETWORKING\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba5a36eadcadc43c1fd0936a8546fb15e8)

@ HAWKBIT\_NETWORKING\_ERROR

**Definition** hawkbit.h:29

[HAWKBIT\_OK](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba6af6cd1b834d74a5298f4b3626b48ad3)

@ HAWKBIT\_OK

**Definition** hawkbit.h:34

[HAWKBIT\_CANCEL\_UPDATE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba9d677899d5ff00957dfeab70f484863f)

@ HAWKBIT\_CANCEL\_UPDATE

**Definition** hawkbit.h:37

[HAWKBIT\_UPDATE\_INSTALLED](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba9f5a200928474863a88d170c11594048)

@ HAWKBIT\_UPDATE\_INSTALLED

**Definition** hawkbit.h:35

[HAWKBIT\_NOT\_INITIALIZED](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bac4ba42120229e92b52c82d4a4d4cd708)

@ HAWKBIT\_NOT\_INITIALIZED

**Definition** hawkbit.h:38

[HAWKBIT\_NO\_UPDATE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bac73c46deb3e54dba690f814a2fb9db71)

@ HAWKBIT\_NO\_UPDATE

**Definition** hawkbit.h:36

[HAWKBIT\_UNCONFIRMED\_IMAGE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bad4b0587da0bdfd829d0d08ed2407357d)

@ HAWKBIT\_UNCONFIRMED\_IMAGE

**Definition** hawkbit.h:30

[HAWKBIT\_DOWNLOAD\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220baf1a448b0addfc769515c725ce5b1bab9)

@ HAWKBIT\_DOWNLOAD\_ERROR

**Definition** hawkbit.h:33

[sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3)

int sec\_tag\_t

Secure tag, a reference to TLS credential.

**Definition** tls\_credentials.h:72

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[hawkbit\_runtime\_config](structhawkbit__runtime__config.md)

hawkBit configuration structure.

**Definition** hawkbit.h:48

[hawkbit\_runtime\_config::tls\_tag](structhawkbit__runtime__config.md#a1fb0307aaeb6107428ae279108057af3)

sec\_tag\_t tls\_tag

**Definition** hawkbit.h:52

[hawkbit\_runtime\_config::server\_port](structhawkbit__runtime__config.md#a33343e076372adca50c1bab528881565)

uint16\_t server\_port

**Definition** hawkbit.h:50

[hawkbit\_runtime\_config::auth\_token](structhawkbit__runtime__config.md#a519e5dbc87d0b472b87cb3dbf01a7807)

char \* auth\_token

**Definition** hawkbit.h:51

[hawkbit\_runtime\_config::server\_addr](structhawkbit__runtime__config.md#aee3966a3387498d726ca960663b0b291)

char \* server\_addr

**Definition** hawkbit.h:49

[tls\_credentials.h](tls__credentials_8h.md)

TLS credentials management.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [hawkbit.h](hawkbit_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
