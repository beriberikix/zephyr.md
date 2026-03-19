---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/simcom-sim7080_8h_source.html
original_path: doxygen/html/simcom-sim7080_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

simcom-sim7080.h

[Go to the documentation of this file.](simcom-sim7080_8h.md)

1/\*

2 \* Copyright (C) 2021 metraTec GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MODEM\_SIMCOM\_SIM7080\_H

8#define ZEPHYR\_INCLUDE\_DRIVERS\_MODEM\_SIMCOM\_SIM7080\_H

9

10#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

11

12#include <[stdint.h](stdint_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

[ 18](simcom-sim7080_8h.md#ace6ac2be37e58af15aeda674923c8201)#define SIM7080\_GNSS\_DATA\_UTC\_LEN 20

[ 19](simcom-sim7080_8h.md#ab64ab50adf37f68e036db2901dd839a7)#define SIM7080\_SMS\_MAX\_LEN 160

20

[ 21](structsim7080__gnss__data.md)struct [sim7080\_gnss\_data](structsim7080__gnss__data.md) {

[ 25](structsim7080__gnss__data.md#ab917d70a3c5adffb8aecc9e521c36599) bool [run\_status](structsim7080__gnss__data.md#ab917d70a3c5adffb8aecc9e521c36599);

[ 29](structsim7080__gnss__data.md#a881db8b7b52d481416bc5f373446bfc2) bool [fix\_status](structsim7080__gnss__data.md#a881db8b7b52d481416bc5f373446bfc2);

[ 33](structsim7080__gnss__data.md#a8a42fbb4a716a0eefe317996f8fe7a8a) char [utc](structsim7080__gnss__data.md#a8a42fbb4a716a0eefe317996f8fe7a8a)[[SIM7080\_GNSS\_DATA\_UTC\_LEN](simcom-sim7080_8h.md#ace6ac2be37e58af15aeda674923c8201)];

[ 37](structsim7080__gnss__data.md#a545077bd8eb1d6827c50b59d469bdc4a) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [lat](structsim7080__gnss__data.md#a545077bd8eb1d6827c50b59d469bdc4a);

[ 41](structsim7080__gnss__data.md#a23dc6e7aa0cc507cf5141aa5329e17ef) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [lon](structsim7080__gnss__data.md#a23dc6e7aa0cc507cf5141aa5329e17ef);

[ 45](structsim7080__gnss__data.md#aa481937aedd2817e3a301663648d9f7d) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [alt](structsim7080__gnss__data.md#aa481937aedd2817e3a301663648d9f7d);

[ 49](structsim7080__gnss__data.md#aca6603b72f8ac67a0a0084a3fc8a60a1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [hdop](structsim7080__gnss__data.md#aca6603b72f8ac67a0a0084a3fc8a60a1);

[ 53](structsim7080__gnss__data.md#a7dee72b39dc718ade2cc27bedc691d6e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cog](structsim7080__gnss__data.md#a7dee72b39dc718ade2cc27bedc691d6e);

[ 57](structsim7080__gnss__data.md#a62b8a5072942a325156a90607888612b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [kmh](structsim7080__gnss__data.md#a62b8a5072942a325156a90607888612b);

58};

59

[ 63](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20eb)enum [sim7080\_sms\_stat](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20eb) {

[ 64](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20eba60957e1589dd8ce57c45ecc5fa114f86) [SIM7080\_SMS\_STAT\_REC\_UNREAD](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20eba60957e1589dd8ce57c45ecc5fa114f86) = 0,

[ 65](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20eba403ca4efe4553c0e4a6d2b2da5be4165) [SIM7080\_SMS\_STAT\_REC\_READ](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20eba403ca4efe4553c0e4a6d2b2da5be4165),

[ 66](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20eba770fe2a07f5dbb73221ff48eaedfb669) [SIM7080\_SMS\_STAT\_STO\_UNSENT](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20eba770fe2a07f5dbb73221ff48eaedfb669),

[ 67](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20ebab5c1ccc0cf53a21abc5f4d0145c414c5) [SIM7080\_SMS\_STAT\_STO\_SENT](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20ebab5c1ccc0cf53a21abc5f4d0145c414c5),

[ 68](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20eba7afe21ab7bda162b25dc2c7daa127c35) [SIM7080\_SMS\_STAT\_ALL](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20eba7afe21ab7bda162b25dc2c7daa127c35),

69};

70

[ 74](simcom-sim7080_8h.md#a48afa6e777af6010488fbf726f467e63)enum [sim7080\_ftp\_rc](simcom-sim7080_8h.md#a48afa6e777af6010488fbf726f467e63) {

75 /\* Operation finished correctly. \*/

[ 76](simcom-sim7080_8h.md#a48afa6e777af6010488fbf726f467e63a6cc1c6e5f12101e8202deddf3667bbda) [SIM7080\_FTP\_RC\_OK](simcom-sim7080_8h.md#a48afa6e777af6010488fbf726f467e63a6cc1c6e5f12101e8202deddf3667bbda) = 0,

77 /\* Session finished. \*/

[ 78](simcom-sim7080_8h.md#a48afa6e777af6010488fbf726f467e63a6bc03b17b206166e04ec04a2638dc241) [SIM7080\_FTP\_RC\_FINISHED](simcom-sim7080_8h.md#a48afa6e777af6010488fbf726f467e63a6bc03b17b206166e04ec04a2638dc241),

79 /\* An error occurred. \*/

[ 80](simcom-sim7080_8h.md#a48afa6e777af6010488fbf726f467e63af744651290c73069148c0726bcdf95ce) [SIM7080\_FTP\_RC\_ERROR](simcom-sim7080_8h.md#a48afa6e777af6010488fbf726f467e63af744651290c73069148c0726bcdf95ce),

81};

82

[ 86](structsim7080__sms.md)struct [sim7080\_sms](structsim7080__sms.md) {

87 /\* First octet of the sms. \*/

[ 88](structsim7080__sms.md#a8c41c51b2bfaea343b5340ba8c02b56a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [first\_octet](structsim7080__sms.md#a8c41c51b2bfaea343b5340ba8c02b56a);

89 /\* Message protocol identifier. \*/

[ 90](structsim7080__sms.md#aaaa3957cf7e0597dfbf309da0b64b54f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tp\_pid](structsim7080__sms.md#aaaa3957cf7e0597dfbf309da0b64b54f);

91 /\* Status of the sms in memory. \*/

[ 92](structsim7080__sms.md#a9dc5291721c65a949a8d351b2408a253) enum [sim7080\_sms\_stat](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20eb) [stat](structsim7080__sms.md#a9dc5291721c65a949a8d351b2408a253);

93 /\* Index of the sms in memory. \*/

[ 94](structsim7080__sms.md#abd559c83ec2896660cffbe8df1be687b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [index](structsim7080__sms.md#abd559c83ec2896660cffbe8df1be687b);

95 /\* Time the sms was received. \*/

96 struct {

[ 97](structsim7080__sms.md#afdb63d3e307c3368149f6d0183541379) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [year](structsim7080__sms.md#afdb63d3e307c3368149f6d0183541379);

[ 98](structsim7080__sms.md#a3db8a08ab147d1765eec75a0b93f3cb7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [month](structsim7080__sms.md#a3db8a08ab147d1765eec75a0b93f3cb7);

[ 99](structsim7080__sms.md#a30773852fece821bd82fc97e02667bd9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [day](structsim7080__sms.md#a30773852fece821bd82fc97e02667bd9);

[ 100](structsim7080__sms.md#af207e345f8c024258c5c011a28ad28c0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hour](structsim7080__sms.md#af207e345f8c024258c5c011a28ad28c0);

[ 101](structsim7080__sms.md#a705e0cbd5654677e6b99cd6ed22767be) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [minute](structsim7080__sms.md#a705e0cbd5654677e6b99cd6ed22767be);

[ 102](structsim7080__sms.md#a343f290be0f3ca62618c47ff7e54cda2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [second](structsim7080__sms.md#a343f290be0f3ca62618c47ff7e54cda2);

[ 103](structsim7080__sms.md#ac5a04784c883710d8794bf4762bb9078) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [timezone](structsim7080__sms.md#ac5a04784c883710d8794bf4762bb9078);

[ 104](structsim7080__sms.md#af97df12fbebedf53af7cd4e505fe9342) } [time](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067);

105 /\* Buffered sms. \*/

[ 106](structsim7080__sms.md#a7dd5c165eafbf70f3e1f01efa71bf640) char [data](structsim7080__sms.md#a7dd5c165eafbf70f3e1f01efa71bf640)[[SIM7080\_SMS\_MAX\_LEN](simcom-sim7080_8h.md#ab64ab50adf37f68e036db2901dd839a7) + 1];

107 /\* Length of the sms in buffer. \*/

[ 108](structsim7080__sms.md#af9aeb3cb06325e0d1e52db6d78567feb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_len](structsim7080__sms.md#af9aeb3cb06325e0d1e52db6d78567feb);

109};

110

[ 114](structsim7080__sms__buffer.md)struct [sim7080\_sms\_buffer](structsim7080__sms__buffer.md) {

115 /\* sms structures to read to. \*/

[ 116](structsim7080__sms__buffer.md#a7477db7ff124999b95f50f3ae32aca6a) struct [sim7080\_sms](structsim7080__sms.md) \*[sms](structsim7080__sms__buffer.md#a7477db7ff124999b95f50f3ae32aca6a);

117 /\* Number of sms structures. \*/

[ 118](structsim7080__sms__buffer.md#a54e1885be2e809fd360738d11547b79f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nsms](structsim7080__sms__buffer.md#a54e1885be2e809fd360738d11547b79f);

119};

120

[ 126](simcom-sim7080_8h.md#a93395c2713539db360cdcf0170075ea1)int [mdm\_sim7080\_power\_on](simcom-sim7080_8h.md#a93395c2713539db360cdcf0170075ea1)(void);

127

[ 133](simcom-sim7080_8h.md#a35c2b87170079e5700021969d01d7f8b)int [mdm\_sim7080\_power\_off](simcom-sim7080_8h.md#a35c2b87170079e5700021969d01d7f8b)(void);

134

[ 140](simcom-sim7080_8h.md#ad857dd548490d40e6b9082c0b72e8d2b)int [mdm\_sim7080\_start\_network](simcom-sim7080_8h.md#ad857dd548490d40e6b9082c0b72e8d2b)(void);

141

[ 147](simcom-sim7080_8h.md#a6106a7d04282af2130471d26f6080ed4)int [mdm\_sim7080\_start\_gnss](simcom-sim7080_8h.md#a6106a7d04282af2130471d26f6080ed4)(void);

148

[ 155](simcom-sim7080_8h.md#acce71e254dd7854052678319227c3f5b)int [mdm\_sim7080\_query\_gnss](simcom-sim7080_8h.md#acce71e254dd7854052678319227c3f5b)(struct [sim7080\_gnss\_data](structsim7080__gnss__data.md) \*[data](structsim7080__sms.md#a7dd5c165eafbf70f3e1f01efa71bf640));

156

[ 160](simcom-sim7080_8h.md#a79837aee512ae6f2fed52f3162e39868)const char \*[mdm\_sim7080\_get\_manufacturer](simcom-sim7080_8h.md#a79837aee512ae6f2fed52f3162e39868)(void);

161

[ 165](simcom-sim7080_8h.md#a557ec2729649fd92c5588f6dd0a04f15)const char \*[mdm\_sim7080\_get\_model](simcom-sim7080_8h.md#a557ec2729649fd92c5588f6dd0a04f15)(void);

166

[ 170](simcom-sim7080_8h.md#a9759bf93bc2e8e15869858853a9499de)const char \*[mdm\_sim7080\_get\_revision](simcom-sim7080_8h.md#a9759bf93bc2e8e15869858853a9499de)(void);

171

[ 175](simcom-sim7080_8h.md#a26d1291993cdcd44982c95bad2dd7b4f)const char \*[mdm\_sim7080\_get\_imei](simcom-sim7080_8h.md#a26d1291993cdcd44982c95bad2dd7b4f)(void);

176

[ 189](simcom-sim7080_8h.md#aacf368bc85d27d49709bde170a0db2ec)int [mdm\_sim7080\_read\_sms](simcom-sim7080_8h.md#aacf368bc85d27d49709bde170a0db2ec)(struct [sim7080\_sms\_buffer](structsim7080__sms__buffer.md) \*buffer);

190

[ 197](simcom-sim7080_8h.md#ae7137523b94c96d4816e4c19cb48313c)int [mdm\_sim7080\_delete\_sms](simcom-sim7080_8h.md#ae7137523b94c96d4816e4c19cb48313c)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [index](structsim7080__sms.md#abd559c83ec2896660cffbe8df1be687b));

198

[ 209](simcom-sim7080_8h.md#a53a7c0d347cfacf0d7fadaf073fbff6c)int [mdm\_sim7080\_ftp\_get\_start](simcom-sim7080_8h.md#a53a7c0d347cfacf0d7fadaf073fbff6c)(const char \*server, const char \*user, const char \*[passwd](structpasswd.md),

210 const char \*file, const char \*path);

211

[ 220](simcom-sim7080_8h.md#a74f00c0b99f71f7340740fb199db58a5)int [mdm\_sim7080\_ftp\_get\_read](simcom-sim7080_8h.md#a74f00c0b99f71f7340740fb199db58a5)(char \*dst, size\_t \*size);

221

222#ifdef \_\_cplusplus

223}

224#endif

225

226#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MODEM\_SIMCOM\_SIM7080\_H \*/

[types.h](include_2zephyr_2types_8h.md)

[time](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067)

time\_t time(time\_t \*tloc)

[sim7080\_sms\_stat](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20eb)

sim7080\_sms\_stat

Possible sms states in memory.

**Definition** simcom-sim7080.h:63

[SIM7080\_SMS\_STAT\_REC\_READ](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20eba403ca4efe4553c0e4a6d2b2da5be4165)

@ SIM7080\_SMS\_STAT\_REC\_READ

**Definition** simcom-sim7080.h:65

[SIM7080\_SMS\_STAT\_REC\_UNREAD](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20eba60957e1589dd8ce57c45ecc5fa114f86)

@ SIM7080\_SMS\_STAT\_REC\_UNREAD

**Definition** simcom-sim7080.h:64

[SIM7080\_SMS\_STAT\_STO\_UNSENT](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20eba770fe2a07f5dbb73221ff48eaedfb669)

@ SIM7080\_SMS\_STAT\_STO\_UNSENT

**Definition** simcom-sim7080.h:66

[SIM7080\_SMS\_STAT\_ALL](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20eba7afe21ab7bda162b25dc2c7daa127c35)

@ SIM7080\_SMS\_STAT\_ALL

**Definition** simcom-sim7080.h:68

[SIM7080\_SMS\_STAT\_STO\_SENT](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20ebab5c1ccc0cf53a21abc5f4d0145c414c5)

@ SIM7080\_SMS\_STAT\_STO\_SENT

**Definition** simcom-sim7080.h:67

[mdm\_sim7080\_get\_imei](simcom-sim7080_8h.md#a26d1291993cdcd44982c95bad2dd7b4f)

const char \* mdm\_sim7080\_get\_imei(void)

Get the sim7080 imei number.

[mdm\_sim7080\_power\_off](simcom-sim7080_8h.md#a35c2b87170079e5700021969d01d7f8b)

int mdm\_sim7080\_power\_off(void)

Power off the Sim7080.

[sim7080\_ftp\_rc](simcom-sim7080_8h.md#a48afa6e777af6010488fbf726f467e63)

sim7080\_ftp\_rc

Possible ftp return codes.

**Definition** simcom-sim7080.h:74

[SIM7080\_FTP\_RC\_FINISHED](simcom-sim7080_8h.md#a48afa6e777af6010488fbf726f467e63a6bc03b17b206166e04ec04a2638dc241)

@ SIM7080\_FTP\_RC\_FINISHED

**Definition** simcom-sim7080.h:78

[SIM7080\_FTP\_RC\_OK](simcom-sim7080_8h.md#a48afa6e777af6010488fbf726f467e63a6cc1c6e5f12101e8202deddf3667bbda)

@ SIM7080\_FTP\_RC\_OK

**Definition** simcom-sim7080.h:76

[SIM7080\_FTP\_RC\_ERROR](simcom-sim7080_8h.md#a48afa6e777af6010488fbf726f467e63af744651290c73069148c0726bcdf95ce)

@ SIM7080\_FTP\_RC\_ERROR

**Definition** simcom-sim7080.h:80

[mdm\_sim7080\_ftp\_get\_start](simcom-sim7080_8h.md#a53a7c0d347cfacf0d7fadaf073fbff6c)

int mdm\_sim7080\_ftp\_get\_start(const char \*server, const char \*user, const char \*passwd, const char \*file, const char \*path)

Start a ftp get session.

[mdm\_sim7080\_get\_model](simcom-sim7080_8h.md#a557ec2729649fd92c5588f6dd0a04f15)

const char \* mdm\_sim7080\_get\_model(void)

Get the sim7080 model information.

[mdm\_sim7080\_start\_gnss](simcom-sim7080_8h.md#a6106a7d04282af2130471d26f6080ed4)

int mdm\_sim7080\_start\_gnss(void)

Starts the modem in gnss operation mode.

[mdm\_sim7080\_ftp\_get\_read](simcom-sim7080_8h.md#a74f00c0b99f71f7340740fb199db58a5)

int mdm\_sim7080\_ftp\_get\_read(char \*dst, size\_t \*size)

Read data from a ftp get session.

[mdm\_sim7080\_get\_manufacturer](simcom-sim7080_8h.md#a79837aee512ae6f2fed52f3162e39868)

const char \* mdm\_sim7080\_get\_manufacturer(void)

Get the sim7080 manufacturer.

[mdm\_sim7080\_power\_on](simcom-sim7080_8h.md#a93395c2713539db360cdcf0170075ea1)

int mdm\_sim7080\_power\_on(void)

Power on the Sim7080.

[mdm\_sim7080\_get\_revision](simcom-sim7080_8h.md#a9759bf93bc2e8e15869858853a9499de)

const char \* mdm\_sim7080\_get\_revision(void)

Get the sim7080 revision.

[mdm\_sim7080\_read\_sms](simcom-sim7080_8h.md#aacf368bc85d27d49709bde170a0db2ec)

int mdm\_sim7080\_read\_sms(struct sim7080\_sms\_buffer \*buffer)

Read sms from sim module.

[SIM7080\_SMS\_MAX\_LEN](simcom-sim7080_8h.md#ab64ab50adf37f68e036db2901dd839a7)

#define SIM7080\_SMS\_MAX\_LEN

**Definition** simcom-sim7080.h:19

[mdm\_sim7080\_query\_gnss](simcom-sim7080_8h.md#acce71e254dd7854052678319227c3f5b)

int mdm\_sim7080\_query\_gnss(struct sim7080\_gnss\_data \*data)

Query gnss position form the modem.

[SIM7080\_GNSS\_DATA\_UTC\_LEN](simcom-sim7080_8h.md#ace6ac2be37e58af15aeda674923c8201)

#define SIM7080\_GNSS\_DATA\_UTC\_LEN

**Definition** simcom-sim7080.h:18

[mdm\_sim7080\_start\_network](simcom-sim7080_8h.md#ad857dd548490d40e6b9082c0b72e8d2b)

int mdm\_sim7080\_start\_network(void)

Starts the modem in network operation mode.

[mdm\_sim7080\_delete\_sms](simcom-sim7080_8h.md#ae7137523b94c96d4816e4c19cb48313c)

int mdm\_sim7080\_delete\_sms(uint16\_t index)

Delete a sms at a given index.

[stdint.h](stdint_8h.md)

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[passwd](structpasswd.md)

**Definition** pwd.h:15

[sim7080\_gnss\_data](structsim7080__gnss__data.md)

**Definition** simcom-sim7080.h:21

[sim7080\_gnss\_data::lon](structsim7080__gnss__data.md#a23dc6e7aa0cc507cf5141aa5329e17ef)

int32\_t lon

Longitude in 10^-7 degree.

**Definition** simcom-sim7080.h:41

[sim7080\_gnss\_data::lat](structsim7080__gnss__data.md#a545077bd8eb1d6827c50b59d469bdc4a)

int32\_t lat

Latitude in 10^-7 degree.

**Definition** simcom-sim7080.h:37

[sim7080\_gnss\_data::kmh](structsim7080__gnss__data.md#a62b8a5072942a325156a90607888612b)

uint16\_t kmh

Speed in 10^-1 km/h.

**Definition** simcom-sim7080.h:57

[sim7080\_gnss\_data::cog](structsim7080__gnss__data.md#a7dee72b39dc718ade2cc27bedc691d6e)

uint16\_t cog

Course over ground un 10^-2 degree.

**Definition** simcom-sim7080.h:53

[sim7080\_gnss\_data::fix\_status](structsim7080__gnss__data.md#a881db8b7b52d481416bc5f373446bfc2)

bool fix\_status

Whether fix is acquired or not.

**Definition** simcom-sim7080.h:29

[sim7080\_gnss\_data::utc](structsim7080__gnss__data.md#a8a42fbb4a716a0eefe317996f8fe7a8a)

char utc[20]

UTC in format yyyyMMddhhmmss.sss.

**Definition** simcom-sim7080.h:33

[sim7080\_gnss\_data::alt](structsim7080__gnss__data.md#aa481937aedd2817e3a301663648d9f7d)

int32\_t alt

Altitude in mm.

**Definition** simcom-sim7080.h:45

[sim7080\_gnss\_data::run\_status](structsim7080__gnss__data.md#ab917d70a3c5adffb8aecc9e521c36599)

bool run\_status

Whether gnss is powered or not.

**Definition** simcom-sim7080.h:25

[sim7080\_gnss\_data::hdop](structsim7080__gnss__data.md#aca6603b72f8ac67a0a0084a3fc8a60a1)

uint16\_t hdop

Horizontal dilution of precision in 10^-2.

**Definition** simcom-sim7080.h:49

[sim7080\_sms\_buffer](structsim7080__sms__buffer.md)

Buffer structure for sms reads.

**Definition** simcom-sim7080.h:114

[sim7080\_sms\_buffer::nsms](structsim7080__sms__buffer.md#a54e1885be2e809fd360738d11547b79f)

uint8\_t nsms

**Definition** simcom-sim7080.h:118

[sim7080\_sms\_buffer::sms](structsim7080__sms__buffer.md#a7477db7ff124999b95f50f3ae32aca6a)

struct sim7080\_sms \* sms

**Definition** simcom-sim7080.h:116

[sim7080\_sms](structsim7080__sms.md)

Buffer structure for sms.

**Definition** simcom-sim7080.h:86

[sim7080\_sms::day](structsim7080__sms.md#a30773852fece821bd82fc97e02667bd9)

uint8\_t day

**Definition** simcom-sim7080.h:99

[sim7080\_sms::second](structsim7080__sms.md#a343f290be0f3ca62618c47ff7e54cda2)

uint8\_t second

**Definition** simcom-sim7080.h:102

[sim7080\_sms::month](structsim7080__sms.md#a3db8a08ab147d1765eec75a0b93f3cb7)

uint8\_t month

**Definition** simcom-sim7080.h:98

[sim7080\_sms::minute](structsim7080__sms.md#a705e0cbd5654677e6b99cd6ed22767be)

uint8\_t minute

**Definition** simcom-sim7080.h:101

[sim7080\_sms::data](structsim7080__sms.md#a7dd5c165eafbf70f3e1f01efa71bf640)

char data[160+1]

**Definition** simcom-sim7080.h:106

[sim7080\_sms::first\_octet](structsim7080__sms.md#a8c41c51b2bfaea343b5340ba8c02b56a)

uint8\_t first\_octet

**Definition** simcom-sim7080.h:88

[sim7080\_sms::stat](structsim7080__sms.md#a9dc5291721c65a949a8d351b2408a253)

enum sim7080\_sms\_stat stat

**Definition** simcom-sim7080.h:92

[sim7080\_sms::tp\_pid](structsim7080__sms.md#aaaa3957cf7e0597dfbf309da0b64b54f)

uint8\_t tp\_pid

**Definition** simcom-sim7080.h:90

[sim7080\_sms::index](structsim7080__sms.md#abd559c83ec2896660cffbe8df1be687b)

uint16\_t index

**Definition** simcom-sim7080.h:94

[sim7080\_sms::timezone](structsim7080__sms.md#ac5a04784c883710d8794bf4762bb9078)

uint8\_t timezone

**Definition** simcom-sim7080.h:103

[sim7080\_sms::hour](structsim7080__sms.md#af207e345f8c024258c5c011a28ad28c0)

uint8\_t hour

**Definition** simcom-sim7080.h:100

[sim7080\_sms::data\_len](structsim7080__sms.md#af9aeb3cb06325e0d1e52db6d78567feb)

uint8\_t data\_len

**Definition** simcom-sim7080.h:108

[sim7080\_sms::year](structsim7080__sms.md#afdb63d3e307c3368149f6d0183541379)

uint8\_t year

**Definition** simcom-sim7080.h:97

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [modem](dir_921fc901d44f7fec5fdbf8b941e64fce.md)
- [simcom-sim7080.h](simcom-sim7080_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
