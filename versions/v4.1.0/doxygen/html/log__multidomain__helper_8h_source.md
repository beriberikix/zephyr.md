---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/log__multidomain__helper_8h_source.html
original_path: doxygen/html/log__multidomain__helper_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_multidomain\_helper.h

[Go to the documentation of this file.](log__multidomain__helper_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_LOGGING\_LOG\_MULTIDOMAIN\_HELPER\_H\_

8#define ZEPHYR\_INCLUDE\_LOGGING\_LOG\_MULTIDOMAIN\_HELPER\_H\_

9

22

28

30#define Z\_LOG\_MULTIDOMAIN\_ID\_MSG 0

31

33#define Z\_LOG\_MULTIDOMAIN\_ID\_GET\_DOMAIN\_CNT 1

34

36#define Z\_LOG\_MULTIDOMAIN\_ID\_GET\_SOURCE\_CNT 2

37

39#define Z\_LOG\_MULTIDOMAIN\_ID\_GET\_DOMAIN\_NAME 3

40

42#define Z\_LOG\_MULTIDOMAIN\_ID\_GET\_SOURCE\_NAME 4

43

45#define Z\_LOG\_MULTIDOMAIN\_ID\_GET\_LEVELS 5

46

48#define Z\_LOG\_MULTIDOMAIN\_ID\_SET\_RUNTIME\_LEVEL 6

49

51#define Z\_LOG\_MULTIDOMAIN\_ID\_DROPPED 7

52

54#define Z\_LOG\_MULTIDOMAIN\_ID\_READY 8

55

57

63

65#define Z\_LOG\_MULTIDOMAIN\_STATUS\_OK 0

67#define Z\_LOG\_MULTIDOMAIN\_STATUS\_ERR 1

68

70

[ 72](structlog__multidomain__log__msg.md)struct [log\_multidomain\_log\_msg](structlog__multidomain__log__msg.md) {

[ 73](structlog__multidomain__log__msg.md#a9192cb5ed413d8bee8ff6ea9ea755914) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structlog__multidomain__log__msg.md#a9192cb5ed413d8bee8ff6ea9ea755914)[0];

74} \_\_packed;

75

[ 77](structlog__multidomain__domain__cnt.md)struct [log\_multidomain\_domain\_cnt](structlog__multidomain__domain__cnt.md) {

[ 78](structlog__multidomain__domain__cnt.md#aaac7aa93d9eee3b0560b03e0a918d87c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [count](structlog__multidomain__domain__cnt.md#aaac7aa93d9eee3b0560b03e0a918d87c);

79} \_\_packed;

80

[ 82](structlog__multidomain__source__cnt.md)struct [log\_multidomain\_source\_cnt](structlog__multidomain__source__cnt.md) {

[ 83](structlog__multidomain__source__cnt.md#a49120909ad3dde80fae3b9aa2517208c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [domain\_id](structlog__multidomain__source__cnt.md#a49120909ad3dde80fae3b9aa2517208c);

[ 84](structlog__multidomain__source__cnt.md#a4f7846d6e474e0165471bdfa858eec81) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [count](structlog__multidomain__source__cnt.md#a4f7846d6e474e0165471bdfa858eec81);

85} \_\_packed;

86

[ 88](structlog__multidomain__domain__name.md)struct [log\_multidomain\_domain\_name](structlog__multidomain__domain__name.md) {

[ 89](structlog__multidomain__domain__name.md#a856105619a22120eba6da2cdcdbc9861) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [domain\_id](structlog__multidomain__domain__name.md#a856105619a22120eba6da2cdcdbc9861);

[ 90](structlog__multidomain__domain__name.md#a7098a0d882d0e4b900866d86231b2671) char [name](structlog__multidomain__domain__name.md#a7098a0d882d0e4b900866d86231b2671)[0];

91} \_\_packed;

92

[ 94](structlog__multidomain__source__name.md)struct [log\_multidomain\_source\_name](structlog__multidomain__source__name.md) {

[ 95](structlog__multidomain__source__name.md#a4a89f856d19bb122e8db88ecc98c5c11) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [domain\_id](structlog__multidomain__source__name.md#a4a89f856d19bb122e8db88ecc98c5c11);

[ 96](structlog__multidomain__source__name.md#aca793d56690b18a2fd33ca191ae4d186) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [source\_id](structlog__multidomain__source__name.md#aca793d56690b18a2fd33ca191ae4d186);

[ 97](structlog__multidomain__source__name.md#af49c1f590284e7b8da65801e062c83de) char [name](structlog__multidomain__source__name.md#af49c1f590284e7b8da65801e062c83de)[0];

98} \_\_packed;

99

[ 101](structlog__multidomain__levels.md)struct [log\_multidomain\_levels](structlog__multidomain__levels.md) {

[ 102](structlog__multidomain__levels.md#aaf98df3f72ba16ead6b087aeb05d7861) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [domain\_id](structlog__multidomain__levels.md#aaf98df3f72ba16ead6b087aeb05d7861);

[ 103](structlog__multidomain__levels.md#a7033cf517c4166ef31649e99a23e5459) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [source\_id](structlog__multidomain__levels.md#a7033cf517c4166ef31649e99a23e5459);

[ 104](structlog__multidomain__levels.md#abc21eda27ec20f85721d8d03ee7bdc5a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [level](structlog__multidomain__levels.md#abc21eda27ec20f85721d8d03ee7bdc5a);

[ 105](structlog__multidomain__levels.md#a9d50693b380f28c9c6738a32d9688068) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [runtime\_level](structlog__multidomain__levels.md#a9d50693b380f28c9c6738a32d9688068);

106} \_\_packed;

107

[ 109](structlog__multidomain__set__runtime__level.md)struct [log\_multidomain\_set\_runtime\_level](structlog__multidomain__set__runtime__level.md) {

[ 110](structlog__multidomain__set__runtime__level.md#ae259c42a8cc2ef7dae8fe82104733d47) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [domain\_id](structlog__multidomain__set__runtime__level.md#ae259c42a8cc2ef7dae8fe82104733d47);

[ 111](structlog__multidomain__set__runtime__level.md#a7e59a0573f101053d4f73166a97ba834) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [source\_id](structlog__multidomain__set__runtime__level.md#a7e59a0573f101053d4f73166a97ba834);

[ 112](structlog__multidomain__set__runtime__level.md#a8afa5236860ceea88847e36ca8fcf72c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [runtime\_level](structlog__multidomain__set__runtime__level.md#a8afa5236860ceea88847e36ca8fcf72c);

113} \_\_packed;

114

[ 116](structlog__multidomain__dropped.md)struct [log\_multidomain\_dropped](structlog__multidomain__dropped.md) {

[ 117](structlog__multidomain__dropped.md#a25bd97d00fa531028315e2fd4352d70e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dropped](structlog__multidomain__dropped.md#a25bd97d00fa531028315e2fd4352d70e);

118} \_\_packed;

119

[ 121](unionlog__multidomain__msg__data.md)union [log\_multidomain\_msg\_data](unionlog__multidomain__msg__data.md) {

[ 122](unionlog__multidomain__msg__data.md#a80c35854603c64c5ee60e5a0e30164b6) struct [log\_multidomain\_log\_msg](structlog__multidomain__log__msg.md) [log\_msg](unionlog__multidomain__msg__data.md#a80c35854603c64c5ee60e5a0e30164b6);

[ 123](unionlog__multidomain__msg__data.md#a8668d1a976506c3b07a700ac690375e8) struct [log\_multidomain\_domain\_cnt](structlog__multidomain__domain__cnt.md) [domain\_cnt](unionlog__multidomain__msg__data.md#a8668d1a976506c3b07a700ac690375e8);

[ 124](unionlog__multidomain__msg__data.md#a35da6c6681a216548d39701faa088bbd) struct [log\_multidomain\_source\_cnt](structlog__multidomain__source__cnt.md) [source\_cnt](unionlog__multidomain__msg__data.md#a35da6c6681a216548d39701faa088bbd);

[ 125](unionlog__multidomain__msg__data.md#ab1481ec75f3951cb961cd9afbc557ba4) struct [log\_multidomain\_domain\_name](structlog__multidomain__domain__name.md) [domain\_name](unionlog__multidomain__msg__data.md#ab1481ec75f3951cb961cd9afbc557ba4);

[ 126](unionlog__multidomain__msg__data.md#aa6e542307344fab6b680c61e2706fdcd) struct [log\_multidomain\_source\_name](structlog__multidomain__source__name.md) [source\_name](unionlog__multidomain__msg__data.md#aa6e542307344fab6b680c61e2706fdcd);

[ 127](unionlog__multidomain__msg__data.md#ac34206c874a0fe122262e2fb3a016cf1) struct [log\_multidomain\_levels](structlog__multidomain__levels.md) [levels](unionlog__multidomain__msg__data.md#ac34206c874a0fe122262e2fb3a016cf1);

[ 128](unionlog__multidomain__msg__data.md#ace983b529bdc0871ea5e6a7b3bda928f) struct [log\_multidomain\_set\_runtime\_level](structlog__multidomain__set__runtime__level.md) [set\_rt\_level](unionlog__multidomain__msg__data.md#ace983b529bdc0871ea5e6a7b3bda928f);

[ 129](unionlog__multidomain__msg__data.md#ab31567cd19b076ba80a284903349837f) struct [log\_multidomain\_dropped](structlog__multidomain__dropped.md) [dropped](unionlog__multidomain__msg__data.md#ab31567cd19b076ba80a284903349837f);

130};

131

[ 133](structlog__multidomain__msg.md)struct [log\_multidomain\_msg](structlog__multidomain__msg.md) {

[ 134](structlog__multidomain__msg.md#a87d6e66eea288c0505acce44d6358cf0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structlog__multidomain__msg.md#a87d6e66eea288c0505acce44d6358cf0);

[ 135](structlog__multidomain__msg.md#a032ef0893b06fe0b414305948ca3efa7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structlog__multidomain__msg.md#a032ef0893b06fe0b414305948ca3efa7);

[ 136](structlog__multidomain__msg.md#a83b96cb88a0ed6fccb7c451bb79bc12f) union [log\_multidomain\_msg\_data](unionlog__multidomain__msg__data.md) [data](structlog__multidomain__msg.md#a83b96cb88a0ed6fccb7c451bb79bc12f);

137} \_\_packed;

138

140struct [log\_multidomain\_link](structlog__multidomain__link.md);

141

[ 143](structlog__multidomain__link__transport__api.md)struct [log\_multidomain\_link\_transport\_api](structlog__multidomain__link__transport__api.md) {

[ 144](structlog__multidomain__link__transport__api.md#ad452b214d16947dd46ae8700792bd40c) int (\*[init](structlog__multidomain__link__transport__api.md#ad452b214d16947dd46ae8700792bd40c))(struct [log\_multidomain\_link](structlog__multidomain__link.md) \*link);

[ 145](structlog__multidomain__link__transport__api.md#adf02696742ac70a1c4e53d97f21b2bd1) int (\*[send](structlog__multidomain__link__transport__api.md#adf02696742ac70a1c4e53d97f21b2bd1))(struct [log\_multidomain\_link](structlog__multidomain__link.md) \*link, void \*data, size\_t len);

146};

147

[ 149](unionlog__multidomain__link__dst.md)union [log\_multidomain\_link\_dst](unionlog__multidomain__link__dst.md) {

[ 150](unionlog__multidomain__link__dst.md#a0935ff85447ef4fa199946783ba39add) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [count](unionlog__multidomain__link__dst.md#a0935ff85447ef4fa199946783ba39add);

151

152 struct {

[ 153](unionlog__multidomain__link__dst.md#aef0b581f40c3fcf86215ab12a32f456b) char \*[dst](unionlog__multidomain__link__dst.md#aef0b581f40c3fcf86215ab12a32f456b);

[ 154](unionlog__multidomain__link__dst.md#ab03fb4ded05aae2300455d1270bd7d1e) size\_t \*[len](unionlog__multidomain__link__dst.md#ab03fb4ded05aae2300455d1270bd7d1e);

[ 155](unionlog__multidomain__link__dst.md#af4ed3dcb76571ed5bdb94ba57822332c) } [name](unionlog__multidomain__link__dst.md#af4ed3dcb76571ed5bdb94ba57822332c);

156

157 struct {

[ 158](unionlog__multidomain__link__dst.md#ac92526ad2eafde97e6a18b8432594e15) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [level](unionlog__multidomain__link__dst.md#ac92526ad2eafde97e6a18b8432594e15);

[ 159](unionlog__multidomain__link__dst.md#acf6e86f74700d62d1b00f7feed7648a4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [runtime\_level](unionlog__multidomain__link__dst.md#acf6e86f74700d62d1b00f7feed7648a4);

[ 160](unionlog__multidomain__link__dst.md#a2fc43ada44365dfdc44914b4f77cb9e3) } [levels](unionlog__multidomain__link__dst.md#a2fc43ada44365dfdc44914b4f77cb9e3);

161

162 struct {

163 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [level](unionlog__multidomain__link__dst.md#ac92526ad2eafde97e6a18b8432594e15);

[ 164](unionlog__multidomain__link__dst.md#ad2c1c1e1c456e6e9643f884b73a6bbb1) } [set\_runtime\_level](unionlog__multidomain__link__dst.md#ad2c1c1e1c456e6e9643f884b73a6bbb1);

165};

166

168extern struct [log\_link\_api](structlog__link__api.md) [log\_multidomain\_link\_api](group__log__backend__multidomain.md#ga64e0fb3d32e2aa1e3353ffe28c05befa);

169

[ 171](structlog__multidomain__link.md)struct [log\_multidomain\_link](structlog__multidomain__link.md) {

[ 172](structlog__multidomain__link.md#a4e7e588f666952942191da56aac35e5c) const struct [log\_multidomain\_link\_transport\_api](structlog__multidomain__link__transport__api.md) \*[transport\_api](structlog__multidomain__link.md#a4e7e588f666952942191da56aac35e5c);

[ 173](structlog__multidomain__link.md#a17e4202830edfafe9ca27b1431d3f0f0) struct k\_sem [rdy\_sem](structlog__multidomain__link.md#a17e4202830edfafe9ca27b1431d3f0f0);

[ 174](structlog__multidomain__link.md#a42c7fc83f2e30e1b63a353915d8cc5af) const struct [log\_link](structlog__link.md) \*[link](structlog__multidomain__link.md#a42c7fc83f2e30e1b63a353915d8cc5af);

[ 175](structlog__multidomain__link.md#a60eb6654d6a53e1cbf0d5cb207c62188) union [log\_multidomain\_link\_dst](unionlog__multidomain__link__dst.md) [dst](structlog__multidomain__link.md#a60eb6654d6a53e1cbf0d5cb207c62188);

[ 176](structlog__multidomain__link.md#ae98c1ed7276d518c037acf65d1c953d3) int [status](structlog__multidomain__link.md#ae98c1ed7276d518c037acf65d1c953d3);

[ 177](structlog__multidomain__link.md#aabc75deb5b28fb76c7915586ad38b082) bool [ready](structlog__multidomain__link.md#aabc75deb5b28fb76c7915586ad38b082);

178};

179

181struct [log\_multidomain\_backend](structlog__multidomain__backend.md);

182

[ 184](structlog__multidomain__backend__transport__api.md)struct [log\_multidomain\_backend\_transport\_api](structlog__multidomain__backend__transport__api.md) {

[ 185](structlog__multidomain__backend__transport__api.md#aa46c6422f1a5972f6ec139a65abf129e) int (\*[init](structlog__multidomain__backend__transport__api.md#aa46c6422f1a5972f6ec139a65abf129e))(struct [log\_multidomain\_backend](structlog__multidomain__backend.md) \*backend);

[ 186](structlog__multidomain__backend__transport__api.md#a95be75d8eb9e6efae986679b3a250dbe) int (\*[send](structlog__multidomain__backend__transport__api.md#a95be75d8eb9e6efae986679b3a250dbe))(struct [log\_multidomain\_backend](structlog__multidomain__backend.md) \*backend, void \*data, size\_t len);

187};

188

190extern const struct [log\_backend\_api](structlog__backend__api.md) [log\_multidomain\_backend\_api](group__log__backend__multidomain.md#ga8e4e6908b6533b11d8cc351f67a5f976);

191

[ 193](structlog__multidomain__backend.md)struct [log\_multidomain\_backend](structlog__multidomain__backend.md) {

[ 194](structlog__multidomain__backend.md#a0208bacfc4ef3f7a97d6c21cb285a802) const struct [log\_multidomain\_backend\_transport\_api](structlog__multidomain__backend__transport__api.md) \*[transport\_api](structlog__multidomain__backend.md#a0208bacfc4ef3f7a97d6c21cb285a802);

[ 195](structlog__multidomain__backend.md#af69ce1d65d227bf3c44451351d0c763d) const struct [log\_backend](structlog__multidomain__backend.md#af69ce1d65d227bf3c44451351d0c763d) \*[log\_backend](structlog__multidomain__backend.md#af69ce1d65d227bf3c44451351d0c763d);

[ 196](structlog__multidomain__backend.md#a831975a0c04da8d3aff75d8775fddad6) struct k\_sem [rdy\_sem](structlog__multidomain__backend.md#a831975a0c04da8d3aff75d8775fddad6);

[ 197](structlog__multidomain__backend.md#a073949c15827b039772a00d31dbc9cf9) bool [panic](structlog__multidomain__backend.md#a073949c15827b039772a00d31dbc9cf9);

[ 198](structlog__multidomain__backend.md#a42f76ae7ee8bf4aaf24c18743b9b92fa) int [status](structlog__multidomain__backend.md#a42f76ae7ee8bf4aaf24c18743b9b92fa);

[ 199](structlog__multidomain__backend.md#afe4ae23396d02875f7865adc349496e4) bool [ready](structlog__multidomain__backend.md#afe4ae23396d02875f7865adc349496e4);

200};

201

[ 208](group__log__backend__multidomain.md#ga887c2f6f7d6a6d65aef2fe63aa4b6d99)void [log\_multidomain\_link\_on\_recv\_cb](group__log__backend__multidomain.md#ga887c2f6f7d6a6d65aef2fe63aa4b6d99)(struct [log\_multidomain\_link](structlog__multidomain__link.md) \*link,

209 const void \*data, size\_t len);

210

[ 216](group__log__backend__multidomain.md#gafb21f03e5f562358babd50ac8d7c1b48)void [log\_multidomain\_link\_on\_error](group__log__backend__multidomain.md#gafb21f03e5f562358babd50ac8d7c1b48)(struct [log\_multidomain\_link](structlog__multidomain__link.md) \*link, int err);

217

[ 223](group__log__backend__multidomain.md#gad045bde79b043dfc38e807f90b9ab5f6)void [log\_multidomain\_link\_on\_started](group__log__backend__multidomain.md#gad045bde79b043dfc38e807f90b9ab5f6)(struct [log\_multidomain\_link](structlog__multidomain__link.md) \*link, int err);

224

[ 231](group__log__backend__multidomain.md#ga2aabae271c90e5475356d5aaad5bd2cf)void [log\_multidomain\_backend\_on\_recv\_cb](group__log__backend__multidomain.md#ga2aabae271c90e5475356d5aaad5bd2cf)(struct [log\_multidomain\_backend](structlog__multidomain__backend.md) \*backend,

232 const void \*data, size\_t len);

233

[ 239](group__log__backend__multidomain.md#ga29a29c0e7a373f055fcbbdbed6ba24e5)void [log\_multidomain\_backend\_on\_error](group__log__backend__multidomain.md#ga29a29c0e7a373f055fcbbdbed6ba24e5)(struct [log\_multidomain\_backend](structlog__multidomain__backend.md) \*backend, int err);

240

[ 246](group__log__backend__multidomain.md#gada2e91cb204ba8e09a6f3a0e69b40d4d)void [log\_multidomain\_backend\_on\_started](group__log__backend__multidomain.md#gada2e91cb204ba8e09a6f3a0e69b40d4d)(struct [log\_multidomain\_backend](structlog__multidomain__backend.md) \*backend, int err);

247

249

250#endif /\* ZEPHYR\_INCLUDE\_LOGGING\_LOG\_MULTIDOMAIN\_HELPER\_H\_ \*/

[log\_multidomain\_backend\_on\_error](group__log__backend__multidomain.md#ga29a29c0e7a373f055fcbbdbed6ba24e5)

void log\_multidomain\_backend\_on\_error(struct log\_multidomain\_backend \*backend, int err)

Function called on error reported by transport layer.

[log\_multidomain\_backend\_on\_recv\_cb](group__log__backend__multidomain.md#ga2aabae271c90e5475356d5aaad5bd2cf)

void log\_multidomain\_backend\_on\_recv\_cb(struct log\_multidomain\_backend \*backend, const void \*data, size\_t len)

Function to be called when data is received from remote.

[log\_multidomain\_link\_api](group__log__backend__multidomain.md#ga64e0fb3d32e2aa1e3353ffe28c05befa)

struct log\_link\_api log\_multidomain\_link\_api

Remote link API.

[log\_multidomain\_link\_on\_recv\_cb](group__log__backend__multidomain.md#ga887c2f6f7d6a6d65aef2fe63aa4b6d99)

void log\_multidomain\_link\_on\_recv\_cb(struct log\_multidomain\_link \*link, const void \*data, size\_t len)

Function to be called when data is received from remote.

[log\_multidomain\_backend\_api](group__log__backend__multidomain.md#ga8e4e6908b6533b11d8cc351f67a5f976)

const struct log\_backend\_api log\_multidomain\_backend\_api

Remote backend API.

[log\_multidomain\_link\_on\_started](group__log__backend__multidomain.md#gad045bde79b043dfc38e807f90b9ab5f6)

void log\_multidomain\_link\_on\_started(struct log\_multidomain\_link \*link, int err)

Function called when connection with remote is established.

[log\_multidomain\_backend\_on\_started](group__log__backend__multidomain.md#gada2e91cb204ba8e09a6f3a0e69b40d4d)

void log\_multidomain\_backend\_on\_started(struct log\_multidomain\_backend \*backend, int err)

Function called when connection with remote is established.

[log\_multidomain\_link\_on\_error](group__log__backend__multidomain.md#gafb21f03e5f562358babd50ac8d7c1b48)

void log\_multidomain\_link\_on\_error(struct log\_multidomain\_link \*link, int err)

Function called on error reported by transport layer.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[log\_backend\_api](structlog__backend__api.md)

Logger backend API.

**Definition** log\_backend.h:63

[log\_link\_api](structlog__link__api.md)

**Definition** log\_link.h:39

[log\_link](structlog__link.md)

**Definition** log\_link.h:62

[log\_multidomain\_backend\_transport\_api](structlog__multidomain__backend__transport__api.md)

Backend transport API.

**Definition** log\_multidomain\_helper.h:184

[log\_multidomain\_backend\_transport\_api::send](structlog__multidomain__backend__transport__api.md#a95be75d8eb9e6efae986679b3a250dbe)

int(\* send)(struct log\_multidomain\_backend \*backend, void \*data, size\_t len)

**Definition** log\_multidomain\_helper.h:186

[log\_multidomain\_backend\_transport\_api::init](structlog__multidomain__backend__transport__api.md#aa46c6422f1a5972f6ec139a65abf129e)

int(\* init)(struct log\_multidomain\_backend \*backend)

**Definition** log\_multidomain\_helper.h:185

[log\_multidomain\_backend](structlog__multidomain__backend.md)

Remote backend structure.

**Definition** log\_multidomain\_helper.h:193

[log\_multidomain\_backend::transport\_api](structlog__multidomain__backend.md#a0208bacfc4ef3f7a97d6c21cb285a802)

const struct log\_multidomain\_backend\_transport\_api \* transport\_api

**Definition** log\_multidomain\_helper.h:194

[log\_multidomain\_backend::panic](structlog__multidomain__backend.md#a073949c15827b039772a00d31dbc9cf9)

bool panic

**Definition** log\_multidomain\_helper.h:197

[log\_multidomain\_backend::status](structlog__multidomain__backend.md#a42f76ae7ee8bf4aaf24c18743b9b92fa)

int status

**Definition** log\_multidomain\_helper.h:198

[log\_multidomain\_backend::rdy\_sem](structlog__multidomain__backend.md#a831975a0c04da8d3aff75d8775fddad6)

struct k\_sem rdy\_sem

**Definition** log\_multidomain\_helper.h:196

[log\_multidomain\_backend::log\_backend](structlog__multidomain__backend.md#af69ce1d65d227bf3c44451351d0c763d)

const struct log\_backend \* log\_backend

**Definition** log\_multidomain\_helper.h:195

[log\_multidomain\_backend::ready](structlog__multidomain__backend.md#afe4ae23396d02875f7865adc349496e4)

bool ready

**Definition** log\_multidomain\_helper.h:199

[log\_multidomain\_domain\_cnt](structlog__multidomain__domain__cnt.md)

Content of the domain count message.

**Definition** log\_multidomain\_helper.h:77

[log\_multidomain\_domain\_cnt::count](structlog__multidomain__domain__cnt.md#aaac7aa93d9eee3b0560b03e0a918d87c)

uint16\_t count

**Definition** log\_multidomain\_helper.h:78

[log\_multidomain\_domain\_name](structlog__multidomain__domain__name.md)

Content of the domain name message.

**Definition** log\_multidomain\_helper.h:88

[log\_multidomain\_domain\_name::name](structlog__multidomain__domain__name.md#a7098a0d882d0e4b900866d86231b2671)

char name[0]

**Definition** log\_multidomain\_helper.h:90

[log\_multidomain\_domain\_name::domain\_id](structlog__multidomain__domain__name.md#a856105619a22120eba6da2cdcdbc9861)

uint8\_t domain\_id

**Definition** log\_multidomain\_helper.h:89

[log\_multidomain\_dropped](structlog__multidomain__dropped.md)

Content of the message for getting amount of dropped messages.

**Definition** log\_multidomain\_helper.h:116

[log\_multidomain\_dropped::dropped](structlog__multidomain__dropped.md#a25bd97d00fa531028315e2fd4352d70e)

uint32\_t dropped

**Definition** log\_multidomain\_helper.h:117

[log\_multidomain\_levels](structlog__multidomain__levels.md)

Content of the message for getting logging levels.

**Definition** log\_multidomain\_helper.h:101

[log\_multidomain\_levels::source\_id](structlog__multidomain__levels.md#a7033cf517c4166ef31649e99a23e5459)

uint16\_t source\_id

**Definition** log\_multidomain\_helper.h:103

[log\_multidomain\_levels::runtime\_level](structlog__multidomain__levels.md#a9d50693b380f28c9c6738a32d9688068)

uint8\_t runtime\_level

**Definition** log\_multidomain\_helper.h:105

[log\_multidomain\_levels::domain\_id](structlog__multidomain__levels.md#aaf98df3f72ba16ead6b087aeb05d7861)

uint8\_t domain\_id

**Definition** log\_multidomain\_helper.h:102

[log\_multidomain\_levels::level](structlog__multidomain__levels.md#abc21eda27ec20f85721d8d03ee7bdc5a)

uint8\_t level

**Definition** log\_multidomain\_helper.h:104

[log\_multidomain\_link\_transport\_api](structlog__multidomain__link__transport__api.md)

Structure with link transport API.

**Definition** log\_multidomain\_helper.h:143

[log\_multidomain\_link\_transport\_api::init](structlog__multidomain__link__transport__api.md#ad452b214d16947dd46ae8700792bd40c)

int(\* init)(struct log\_multidomain\_link \*link)

**Definition** log\_multidomain\_helper.h:144

[log\_multidomain\_link\_transport\_api::send](structlog__multidomain__link__transport__api.md#adf02696742ac70a1c4e53d97f21b2bd1)

int(\* send)(struct log\_multidomain\_link \*link, void \*data, size\_t len)

**Definition** log\_multidomain\_helper.h:145

[log\_multidomain\_link](structlog__multidomain__link.md)

Remote link structure.

**Definition** log\_multidomain\_helper.h:171

[log\_multidomain\_link::rdy\_sem](structlog__multidomain__link.md#a17e4202830edfafe9ca27b1431d3f0f0)

struct k\_sem rdy\_sem

**Definition** log\_multidomain\_helper.h:173

[log\_multidomain\_link::link](structlog__multidomain__link.md#a42c7fc83f2e30e1b63a353915d8cc5af)

const struct log\_link \* link

**Definition** log\_multidomain\_helper.h:174

[log\_multidomain\_link::transport\_api](structlog__multidomain__link.md#a4e7e588f666952942191da56aac35e5c)

const struct log\_multidomain\_link\_transport\_api \* transport\_api

**Definition** log\_multidomain\_helper.h:172

[log\_multidomain\_link::dst](structlog__multidomain__link.md#a60eb6654d6a53e1cbf0d5cb207c62188)

union log\_multidomain\_link\_dst dst

**Definition** log\_multidomain\_helper.h:175

[log\_multidomain\_link::ready](structlog__multidomain__link.md#aabc75deb5b28fb76c7915586ad38b082)

bool ready

**Definition** log\_multidomain\_helper.h:177

[log\_multidomain\_link::status](structlog__multidomain__link.md#ae98c1ed7276d518c037acf65d1c953d3)

int status

**Definition** log\_multidomain\_helper.h:176

[log\_multidomain\_log\_msg](structlog__multidomain__log__msg.md)

Content of the logging message.

**Definition** log\_multidomain\_helper.h:72

[log\_multidomain\_log\_msg::data](structlog__multidomain__log__msg.md#a9192cb5ed413d8bee8ff6ea9ea755914)

uint8\_t data[0]

**Definition** log\_multidomain\_helper.h:73

[log\_multidomain\_msg](structlog__multidomain__msg.md)

Message.

**Definition** log\_multidomain\_helper.h:133

[log\_multidomain\_msg::status](structlog__multidomain__msg.md#a032ef0893b06fe0b414305948ca3efa7)

uint8\_t status

**Definition** log\_multidomain\_helper.h:135

[log\_multidomain\_msg::data](structlog__multidomain__msg.md#a83b96cb88a0ed6fccb7c451bb79bc12f)

union log\_multidomain\_msg\_data data

**Definition** log\_multidomain\_helper.h:136

[log\_multidomain\_msg::id](structlog__multidomain__msg.md#a87d6e66eea288c0505acce44d6358cf0)

uint8\_t id

**Definition** log\_multidomain\_helper.h:134

[log\_multidomain\_set\_runtime\_level](structlog__multidomain__set__runtime__level.md)

Content of the message for setting logging level.

**Definition** log\_multidomain\_helper.h:109

[log\_multidomain\_set\_runtime\_level::source\_id](structlog__multidomain__set__runtime__level.md#a7e59a0573f101053d4f73166a97ba834)

uint16\_t source\_id

**Definition** log\_multidomain\_helper.h:111

[log\_multidomain\_set\_runtime\_level::runtime\_level](structlog__multidomain__set__runtime__level.md#a8afa5236860ceea88847e36ca8fcf72c)

uint8\_t runtime\_level

**Definition** log\_multidomain\_helper.h:112

[log\_multidomain\_set\_runtime\_level::domain\_id](structlog__multidomain__set__runtime__level.md#ae259c42a8cc2ef7dae8fe82104733d47)

uint8\_t domain\_id

**Definition** log\_multidomain\_helper.h:110

[log\_multidomain\_source\_cnt](structlog__multidomain__source__cnt.md)

Content of the source count message.

**Definition** log\_multidomain\_helper.h:82

[log\_multidomain\_source\_cnt::domain\_id](structlog__multidomain__source__cnt.md#a49120909ad3dde80fae3b9aa2517208c)

uint8\_t domain\_id

**Definition** log\_multidomain\_helper.h:83

[log\_multidomain\_source\_cnt::count](structlog__multidomain__source__cnt.md#a4f7846d6e474e0165471bdfa858eec81)

uint16\_t count

**Definition** log\_multidomain\_helper.h:84

[log\_multidomain\_source\_name](structlog__multidomain__source__name.md)

Content of the source name message.

**Definition** log\_multidomain\_helper.h:94

[log\_multidomain\_source\_name::domain\_id](structlog__multidomain__source__name.md#a4a89f856d19bb122e8db88ecc98c5c11)

uint8\_t domain\_id

**Definition** log\_multidomain\_helper.h:95

[log\_multidomain\_source\_name::source\_id](structlog__multidomain__source__name.md#aca793d56690b18a2fd33ca191ae4d186)

uint16\_t source\_id

**Definition** log\_multidomain\_helper.h:96

[log\_multidomain\_source\_name::name](structlog__multidomain__source__name.md#af49c1f590284e7b8da65801e062c83de)

char name[0]

**Definition** log\_multidomain\_helper.h:97

[log\_multidomain\_link\_dst](unionlog__multidomain__link__dst.md)

Union for holding data returned by associated remote backend.

**Definition** log\_multidomain\_helper.h:149

[log\_multidomain\_link\_dst::count](unionlog__multidomain__link__dst.md#a0935ff85447ef4fa199946783ba39add)

uint16\_t count

**Definition** log\_multidomain\_helper.h:150

[log\_multidomain\_link\_dst::levels](unionlog__multidomain__link__dst.md#a2fc43ada44365dfdc44914b4f77cb9e3)

struct log\_multidomain\_link\_dst::@307207160255267002013306257344066014035041345300 levels

[log\_multidomain\_link\_dst::len](unionlog__multidomain__link__dst.md#ab03fb4ded05aae2300455d1270bd7d1e)

size\_t \* len

**Definition** log\_multidomain\_helper.h:154

[log\_multidomain\_link\_dst::level](unionlog__multidomain__link__dst.md#ac92526ad2eafde97e6a18b8432594e15)

uint8\_t level

**Definition** log\_multidomain\_helper.h:158

[log\_multidomain\_link\_dst::runtime\_level](unionlog__multidomain__link__dst.md#acf6e86f74700d62d1b00f7feed7648a4)

uint8\_t runtime\_level

**Definition** log\_multidomain\_helper.h:159

[log\_multidomain\_link\_dst::set\_runtime\_level](unionlog__multidomain__link__dst.md#ad2c1c1e1c456e6e9643f884b73a6bbb1)

struct log\_multidomain\_link\_dst::@337065147132354057101006263357350243263170326373 set\_runtime\_level

[log\_multidomain\_link\_dst::dst](unionlog__multidomain__link__dst.md#aef0b581f40c3fcf86215ab12a32f456b)

char \* dst

**Definition** log\_multidomain\_helper.h:153

[log\_multidomain\_link\_dst::name](unionlog__multidomain__link__dst.md#af4ed3dcb76571ed5bdb94ba57822332c)

struct log\_multidomain\_link\_dst::@006126307004354304273237373124206066101211353062 name

[log\_multidomain\_msg\_data](unionlog__multidomain__msg__data.md)

Union with all message types.

**Definition** log\_multidomain\_helper.h:121

[log\_multidomain\_msg\_data::source\_cnt](unionlog__multidomain__msg__data.md#a35da6c6681a216548d39701faa088bbd)

struct log\_multidomain\_source\_cnt source\_cnt

**Definition** log\_multidomain\_helper.h:124

[log\_multidomain\_msg\_data::log\_msg](unionlog__multidomain__msg__data.md#a80c35854603c64c5ee60e5a0e30164b6)

struct log\_multidomain\_log\_msg log\_msg

**Definition** log\_multidomain\_helper.h:122

[log\_multidomain\_msg\_data::domain\_cnt](unionlog__multidomain__msg__data.md#a8668d1a976506c3b07a700ac690375e8)

struct log\_multidomain\_domain\_cnt domain\_cnt

**Definition** log\_multidomain\_helper.h:123

[log\_multidomain\_msg\_data::source\_name](unionlog__multidomain__msg__data.md#aa6e542307344fab6b680c61e2706fdcd)

struct log\_multidomain\_source\_name source\_name

**Definition** log\_multidomain\_helper.h:126

[log\_multidomain\_msg\_data::domain\_name](unionlog__multidomain__msg__data.md#ab1481ec75f3951cb961cd9afbc557ba4)

struct log\_multidomain\_domain\_name domain\_name

**Definition** log\_multidomain\_helper.h:125

[log\_multidomain\_msg\_data::dropped](unionlog__multidomain__msg__data.md#ab31567cd19b076ba80a284903349837f)

struct log\_multidomain\_dropped dropped

**Definition** log\_multidomain\_helper.h:129

[log\_multidomain\_msg\_data::levels](unionlog__multidomain__msg__data.md#ac34206c874a0fe122262e2fb3a016cf1)

struct log\_multidomain\_levels levels

**Definition** log\_multidomain\_helper.h:127

[log\_multidomain\_msg\_data::set\_rt\_level](unionlog__multidomain__msg__data.md#ace983b529bdc0871ea5e6a7b3bda928f)

struct log\_multidomain\_set\_runtime\_level set\_rt\_level

**Definition** log\_multidomain\_helper.h:128

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_multidomain\_helper.h](log__multidomain__helper_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
