---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/w1_8h_source.html
original_path: doxygen/html/w1_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

w1.h

[Go to the documentation of this file.](w1_8h.md)

1/\*

2 \* Copyright (c) 2018 Roman Tataurov <diytronic@yandex.ru>

3 \* Copyright (c) 2022 Thomas Stranger

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_W1\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_W1\_H\_

15

16#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

17#include <[zephyr/device.h](device_8h.md)>

18#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

19#include <[zephyr/sys/crc.h](crc_8h.md)>

20#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

32

34

35/\*

36 \* Count the number of slaves expected on the bus.

37 \* This can be used to decide if the bus has a multidrop topology or

38 \* only a single slave is present.

39 \* There is a comma after each ordinal (including the last)

40 \* Hence FOR\_EACH adds "+1" once too often which has to be subtracted in the end.

41 \*/

42#define F1(x) 1

43#define W1\_SLAVE\_COUNT(node\_id) \

44 (FOR\_EACH(F1, (+), DT\_SUPPORTS\_DEP\_ORDS(node\_id)) - 1)

45#define W1\_INST\_SLAVE\_COUNT(inst) \

46 (W1\_SLAVE\_COUNT(DT\_DRV\_INST(inst)))

47

49

[ 53](group__w1__interface.md#ga382989ef707709b5d26c40a394833612)enum [w1\_settings\_type](group__w1__interface.md#ga382989ef707709b5d26c40a394833612) {

[ 57](group__w1__interface.md#gga382989ef707709b5d26c40a394833612a788fee2803793832c58951d623d823d5) [W1\_SETTING\_SPEED](group__w1__interface.md#gga382989ef707709b5d26c40a394833612a788fee2803793832c58951d623d823d5),

[ 62](group__w1__interface.md#gga382989ef707709b5d26c40a394833612ae3293dfeaa3f1976e8cf57e694d5f811) [W1\_SETTING\_STRONG\_PULLUP](group__w1__interface.md#gga382989ef707709b5d26c40a394833612ae3293dfeaa3f1976e8cf57e694d5f811),

63

[ 67](group__w1__interface.md#gga382989ef707709b5d26c40a394833612a814e27d05a04e027c52cb206aaf69b22) [W1\_SETINGS\_TYPE\_COUNT](group__w1__interface.md#gga382989ef707709b5d26c40a394833612a814e27d05a04e027c52cb206aaf69b22),

68};

69

71

73struct w1\_master\_config {

74 /\* Number of connected slaves \*/

75 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) slave\_count;

76};

77

79struct w1\_master\_data {

80 /\* The mutex used by w1\_lock\_bus and w1\_unlock\_bus methods \*/

81 struct k\_mutex bus\_lock;

82};

83

84typedef int (\*w1\_reset\_bus\_t)(const struct [device](structdevice.md) \*dev);

85typedef int (\*w1\_read\_bit\_t)(const struct [device](structdevice.md) \*dev);

86typedef int (\*w1\_write\_bit\_t)(const struct [device](structdevice.md) \*dev, bool bit);

87typedef int (\*w1\_read\_byte\_t)(const struct [device](structdevice.md) \*dev);

88typedef int (\*w1\_write\_byte\_t)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte);

89typedef int (\*w1\_read\_block\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer,

90 size\_t len);

91typedef int (\*w1\_write\_block\_t)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer,

92 size\_t len);

93typedef [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) (\*w1\_get\_slave\_count\_t)(const struct [device](structdevice.md) \*dev);

94typedef int (\*w1\_configure\_t)(const struct [device](structdevice.md) \*dev,

95 enum [w1\_settings\_type](group__w1__interface.md#ga382989ef707709b5d26c40a394833612) type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

96typedef int (\*w1\_change\_bus\_lock\_t)(const struct [device](structdevice.md) \*dev, bool lock);

97

98\_\_subsystem struct w1\_driver\_api {

99 w1\_reset\_bus\_t reset\_bus;

100 w1\_read\_bit\_t read\_bit;

101 w1\_write\_bit\_t write\_bit;

102 w1\_read\_byte\_t read\_byte;

103 w1\_write\_byte\_t write\_byte;

104 w1\_read\_block\_t read\_block;

105 w1\_write\_block\_t write\_block;

106 w1\_configure\_t configure;

107 w1\_change\_bus\_lock\_t change\_bus\_lock;

108};

110

112\_\_syscall int w1\_change\_bus\_lock(const struct [device](structdevice.md) \*dev, bool lock);

113

114static inline int z\_impl\_w1\_change\_bus\_lock(const struct [device](structdevice.md) \*dev, bool lock)

115{

116 struct w1\_master\_data \*ctrl\_data = (struct w1\_master\_data \*)dev->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

117 const struct w1\_driver\_api \*api = (const struct w1\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

118

119 if (api->change\_bus\_lock) {

120 return api->change\_bus\_lock(dev, lock);

121 }

122

123 if (lock) {

124 return [k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)(&ctrl\_data->bus\_lock, [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca));

125 } else {

126 return [k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)(&ctrl\_data->bus\_lock);

127 }

128}

130

[ 143](group__w1__interface.md#gab18b0f60a126d38c982730d3ad9756c1)static inline int [w1\_lock\_bus](group__w1__interface.md#gab18b0f60a126d38c982730d3ad9756c1)(const struct [device](structdevice.md) \*dev)

144{

145 return w1\_change\_bus\_lock(dev, true);

146}

147

[ 158](group__w1__interface.md#ga7230fad2428ab62fa963b50e67388c19)static inline int [w1\_unlock\_bus](group__w1__interface.md#ga7230fad2428ab62fa963b50e67388c19)(const struct [device](structdevice.md) \*dev)

159{

160 return w1\_change\_bus\_lock(dev, false);

161}

162

169

[ 189](group__w1__data__link.md#gab4eccd585c6f14330807055ccc151fd6)\_\_syscall int [w1\_reset\_bus](group__w1__data__link.md#gab4eccd585c6f14330807055ccc151fd6)(const struct [device](structdevice.md) \*dev);

190

191static inline int z\_impl\_w1\_reset\_bus(const struct [device](structdevice.md) \*dev)

192{

193 const struct w1\_driver\_api \*api = (const struct w1\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

194

195 return api->reset\_bus(dev);

196}

197

[ 206](group__w1__data__link.md#ga0f2b37163f3d7c9816371942765509b4)\_\_syscall int [w1\_read\_bit](group__w1__data__link.md#ga0f2b37163f3d7c9816371942765509b4)(const struct [device](structdevice.md) \*dev);

207

208static inline int z\_impl\_w1\_read\_bit(const struct [device](structdevice.md) \*dev)

209{

210 const struct w1\_driver\_api \*api = (const struct w1\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

211

212 return api->read\_bit(dev);

213}

214

[ 224](group__w1__data__link.md#ga3671d8bbf9d044c60d7e96e4190ba2fa)\_\_syscall int [w1\_write\_bit](group__w1__data__link.md#ga3671d8bbf9d044c60d7e96e4190ba2fa)(const struct [device](structdevice.md) \*dev, const bool bit);

225

226static inline int z\_impl\_w1\_write\_bit(const struct [device](structdevice.md) \*dev, bool bit)

227{

228 const struct w1\_driver\_api \*api = (const struct w1\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

229

230 return api->write\_bit(dev, bit);

231}

232

[ 241](group__w1__data__link.md#ga868980684bb98149af5b59e3fa8a83b6)\_\_syscall int [w1\_read\_byte](group__w1__data__link.md#ga868980684bb98149af5b59e3fa8a83b6)(const struct [device](structdevice.md) \*dev);

242

243static inline int z\_impl\_w1\_read\_byte(const struct [device](structdevice.md) \*dev)

244{

245 const struct w1\_driver\_api \*api = (const struct w1\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

246

247 return api->read\_byte(dev);

248}

249

[ 259](group__w1__data__link.md#ga978a8f14fb8cb3a569f8b731b20cc840)\_\_syscall int [w1\_write\_byte](group__w1__data__link.md#ga978a8f14fb8cb3a569f8b731b20cc840)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte);

260

261static inline int z\_impl\_w1\_write\_byte(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte)

262{

263 const struct w1\_driver\_api \*api = (const struct w1\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

264

265 return api->write\_byte(dev, byte);

266}

267

[ 278](group__w1__data__link.md#ga2967c99ec93b7c31beb9cf2a327a23f4)\_\_syscall int [w1\_read\_block](group__w1__data__link.md#ga2967c99ec93b7c31beb9cf2a327a23f4)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, size\_t len);

279

[ 290](group__w1__data__link.md#gab30a58c42c06088da9e0845de7d089ce)\_\_syscall int [w1\_write\_block](group__w1__data__link.md#gab30a58c42c06088da9e0845de7d089ce)(const struct [device](structdevice.md) \*dev,

291 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, size\_t len);

292

[ 301](group__w1__data__link.md#ga65892855c763dccc27b508d870c1d144)\_\_syscall size\_t [w1\_get\_slave\_count](group__w1__data__link.md#ga65892855c763dccc27b508d870c1d144)(const struct [device](structdevice.md) \*dev);

302

303static inline size\_t z\_impl\_w1\_get\_slave\_count(const struct [device](structdevice.md) \*dev)

304{

305 const struct w1\_master\_config \*ctrl\_cfg =

306 (const struct w1\_master\_config \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

307

308 return ctrl\_cfg->slave\_count;

309}

310

[ 325](group__w1__data__link.md#gae989e0deebe5666edc9ff8a3839cf216)\_\_syscall int [w1\_configure](group__w1__data__link.md#gae989e0deebe5666edc9ff8a3839cf216)(const struct [device](structdevice.md) \*dev,

326 enum [w1\_settings\_type](group__w1__interface.md#ga382989ef707709b5d26c40a394833612) type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

327

328static inline int z\_impl\_w1\_configure(const struct [device](structdevice.md) \*dev,

329 enum [w1\_settings\_type](group__w1__interface.md#ga382989ef707709b5d26c40a394833612) type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value)

330{

331 const struct w1\_driver\_api \*api = (const struct w1\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

332

333 return api->configure(dev, type, value);

334}

335

339

346

351

[ 356](group__w1__network.md#ga9792cb2093e911a4722b7fa9457093dc)#define W1\_CMD\_SKIP\_ROM 0xCC

357

[ 362](group__w1__network.md#gae97f7ecda699ccf9b63030f2af632bc8)#define W1\_CMD\_MATCH\_ROM 0x55

363

[ 368](group__w1__network.md#ga31230559122289c179f01e09e3847830)#define W1\_CMD\_RESUME 0xA5

369

[ 376](group__w1__network.md#ga9e1a9a38889bf165370670c28778028b)#define W1\_CMD\_READ\_ROM 0x33

377

[ 382](group__w1__network.md#ga57f17871edab0b771f2f664bf9bafb79)#define W1\_CMD\_SEARCH\_ROM 0xF0

383

[ 388](group__w1__network.md#gafc7a257428c69bb4549c6cd05a928957)#define W1\_CMD\_SEARCH\_ALARM 0xEC

389

[ 394](group__w1__network.md#ga8b61b2308f2681801894f24ea2c95b12)#define W1\_CMD\_OVERDRIVE\_SKIP\_ROM 0x3C

395

[ 400](group__w1__network.md#ga3e3f9fa70074188a2e489f34555b519b)#define W1\_CMD\_OVERDRIVE\_MATCH\_ROM 0x69

401

403

408

[ 410](group__w1__network.md#gaa4ad8d9a3791fbca6c99d49b9793a002)#define W1\_CRC8\_SEED 0x00

[ 412](group__w1__network.md#gabe56ffbe20c2ba7e0a5c87c8e36c45e5)#define W1\_CRC8\_POLYNOMIAL 0x8C

[ 414](group__w1__network.md#ga324f30f17c6cd1b33650b58055a3a57f)#define W1\_CRC16\_SEED 0x0000

[ 416](group__w1__network.md#gab94362fbf4eec5f115f93fc8976cff0d)#define W1\_CRC16\_POLYNOMIAL 0xa001

417

419

[ 421](group__w1__network.md#ga909502b9b18c15a9ab0da8d3605e8c37)#define W1\_SEARCH\_ALL\_FAMILIES 0x00

422

[ 424](group__w1__network.md#ga17770ecebad7170e9004afd9a7735c73)#define W1\_ROM\_INIT\_ZERO \

425 { \

426 .family = 0, .serial = { 0 }, .crc = 0, \

427 }

428

[ 432](structw1__rom.md)struct [w1\_rom](structw1__rom.md) {

[ 439](structw1__rom.md#adc7f4f9fca172392b11864a17424a14c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [family](structw1__rom.md#adc7f4f9fca172392b11864a17424a14c);

[ 441](structw1__rom.md#a134ee6d6e5e5eb711caf59449d11732e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [serial](structw1__rom.md#a134ee6d6e5e5eb711caf59449d11732e)[6];

[ 443](structw1__rom.md#a73d85d7ce0ef671027c910b9b7a54165) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crc](structw1__rom.md#a73d85d7ce0ef671027c910b9b7a54165);

444};

445

[ 452](structw1__slave__config.md)struct [w1\_slave\_config](structw1__slave__config.md) {

[ 454](structw1__slave__config.md#a9f42fd1257483f308115ae02e6ef8596) struct [w1\_rom](structw1__rom.md) [rom](structw1__slave__config.md#a9f42fd1257483f308115ae02e6ef8596);

[ 456](structw1__slave__config.md#ab8a2d4522505416863fed561df22d058) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [overdrive](structw1__slave__config.md#ab8a2d4522505416863fed561df22d058) : 1;

458 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) res : 31;

460};

461

[ 469](group__w1__network.md#ga2f5540f2a86fd55edcd7a8ffecbfd786)typedef void (\*[w1\_search\_callback\_t](group__w1__network.md#ga2f5540f2a86fd55edcd7a8ffecbfd786))(struct [w1\_rom](structw1__rom.md) rom, void \*user\_data);

470

[ 488](group__w1__network.md#ga93abefbd0e7067db474e6480301a0c4c)int [w1\_read\_rom](group__w1__network.md#ga93abefbd0e7067db474e6480301a0c4c)(const struct [device](structdevice.md) \*dev, struct [w1\_rom](structw1__rom.md) \*rom);

489

[ 510](group__w1__network.md#ga53f34d64504498dbb194bc2119727908)int [w1\_match\_rom](group__w1__network.md#ga53f34d64504498dbb194bc2119727908)(const struct [device](structdevice.md) \*dev, const struct [w1\_slave\_config](structw1__slave__config.md) \*config);

511

[ 524](group__w1__network.md#ga67c815bb99b75c862a483d4f8556b24a)int [w1\_resume\_command](group__w1__network.md#ga67c815bb99b75c862a483d4f8556b24a)(const struct [device](structdevice.md) \*dev);

525

[ 541](group__w1__network.md#gaba2be4e87ff472e90b705dbd73b913de)int [w1\_skip\_rom](group__w1__network.md#gaba2be4e87ff472e90b705dbd73b913de)(const struct [device](structdevice.md) \*dev, const struct [w1\_slave\_config](structw1__slave__config.md) \*config);

542

[ 554](group__w1__network.md#gaa0acc88fe02535a3d512b866b6d34b8a)int [w1\_reset\_select](group__w1__network.md#gaa0acc88fe02535a3d512b866b6d34b8a)(const struct [device](structdevice.md) \*dev, const struct [w1\_slave\_config](structw1__slave__config.md) \*config);

555

[ 573](group__w1__network.md#ga1cf8c016ac66c3970f72fa1f409fa680)int [w1\_write\_read](group__w1__network.md#ga1cf8c016ac66c3970f72fa1f409fa680)(const struct [device](structdevice.md) \*dev, const struct [w1\_slave\_config](structw1__slave__config.md) \*config,

574 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*write\_buf, size\_t write\_len,

575 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*read\_buf, size\_t read\_len);

576

[ 601](group__w1__network.md#ga19533f445029a69aac7d4ca5a7aeedcd)\_\_syscall int [w1\_search\_bus](group__w1__network.md#ga19533f445029a69aac7d4ca5a7aeedcd)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) command,

602 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [family](structw1__rom.md#adc7f4f9fca172392b11864a17424a14c), [w1\_search\_callback\_t](group__w1__network.md#ga2f5540f2a86fd55edcd7a8ffecbfd786) callback,

603 void \*user\_data);

604

[ 620](group__w1__network.md#ga024af0ee5018d7078808cc0a544cfd26)static inline int [w1\_search\_rom](group__w1__network.md#ga024af0ee5018d7078808cc0a544cfd26)(const struct [device](structdevice.md) \*dev,

621 [w1\_search\_callback\_t](group__w1__network.md#ga2f5540f2a86fd55edcd7a8ffecbfd786) callback, void \*user\_data)

622{

623 return [w1\_search\_bus](group__w1__network.md#ga19533f445029a69aac7d4ca5a7aeedcd)(dev, [W1\_CMD\_SEARCH\_ROM](group__w1__network.md#ga57f17871edab0b771f2f664bf9bafb79), [W1\_SEARCH\_ALL\_FAMILIES](group__w1__network.md#ga909502b9b18c15a9ab0da8d3605e8c37),

624 callback, user\_data);

625}

626

[ 642](group__w1__network.md#ga0f510bd3720e54b4eeb4e368934db7f0)static inline int [w1\_search\_alarm](group__w1__network.md#ga0f510bd3720e54b4eeb4e368934db7f0)(const struct [device](structdevice.md) \*dev,

643 [w1\_search\_callback\_t](group__w1__network.md#ga2f5540f2a86fd55edcd7a8ffecbfd786) callback, void \*user\_data)

644{

645 return [w1\_search\_bus](group__w1__network.md#ga19533f445029a69aac7d4ca5a7aeedcd)(dev, [W1\_CMD\_SEARCH\_ALARM](group__w1__network.md#gafc7a257428c69bb4549c6cd05a928957), [W1\_SEARCH\_ALL\_FAMILIES](group__w1__network.md#ga909502b9b18c15a9ab0da8d3605e8c37),

646 callback, user\_data);

647}

648

[ 656](group__w1__network.md#ga178a88d0c585d5df0405aadde3ea9178)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [w1\_rom\_to\_uint64](group__w1__network.md#ga178a88d0c585d5df0405aadde3ea9178)(const struct [w1\_rom](structw1__rom.md) \*rom)

657{

658 return [sys\_get\_be64](sys_2byteorder_8h.md#ad8e00ff5c0b9e394291936d1a570c215)(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)rom);

659}

660

[ 667](group__w1__network.md#ga6e4dba051a6b29c974e499db17315034)static inline void [w1\_uint64\_to\_rom](group__w1__network.md#ga6e4dba051a6b29c974e499db17315034)(const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) rom64, struct [w1\_rom](structw1__rom.md) \*rom)

668{

669 [sys\_put\_be64](sys_2byteorder_8h.md#a3e0d2e4e85249497011f5f9ea0d2987c)(rom64, ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)rom);

670}

671

[ 684](group__w1__network.md#ga350a384a6040d1fbb86bfb804013ade3)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [w1\_crc8](group__w1__network.md#ga350a384a6040d1fbb86bfb804013ade3)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len)

685{

686 return [crc8](group__crc.md#gaa614e73ee7484ca0424fa7d14a54bbb6)(src, len, [W1\_CRC8\_POLYNOMIAL](group__w1__network.md#gabe56ffbe20c2ba7e0a5c87c8e36c45e5), [W1\_CRC8\_SEED](group__w1__network.md#gaa4ad8d9a3791fbca6c99d49b9793a002), true);

687}

688

[ 704](group__w1__network.md#ga5635f79a54a2e5b96c8b7ca9a8ab8366)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [w1\_crc16](group__w1__network.md#ga5635f79a54a2e5b96c8b7ca9a8ab8366)(const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src,

705 const size\_t len)

706{

707 return [crc16\_reflect](group__crc.md#gaccbcb5b80cf8deaac252474ecc6d9914)([W1\_CRC16\_POLYNOMIAL](group__w1__network.md#gab94362fbf4eec5f115f93fc8976cff0d), seed, src, len);

708}

709

713

714#ifdef \_\_cplusplus

715}

716#endif

717

721#include <syscalls/w1.h>

722

723#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_W1\_H\_ \*/

[crc.h](crc_8h.md)

CRC computation function.

[device.h](device_8h.md)

[K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)

#define K\_FOREVER

Generate infinite timeout delay.

**Definition** kernel.h:1361

[crc8](group__crc.md#gaa614e73ee7484ca0424fa7d14a54bbb6)

uint8\_t crc8(const uint8\_t \*src, size\_t len, uint8\_t polynomial, uint8\_t initial\_value, bool reversed)

Generic function for computing CRC 8.

[crc16\_reflect](group__crc.md#gaccbcb5b80cf8deaac252474ecc6d9914)

uint16\_t crc16\_reflect(uint16\_t poly, uint16\_t seed, const uint8\_t \*src, size\_t len)

Generic function for computing a CRC-16 with input and output reflection.

[k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)

int k\_mutex\_unlock(struct k\_mutex \*mutex)

Unlock a mutex.

[k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)

int k\_mutex\_lock(struct k\_mutex \*mutex, k\_timeout\_t timeout)

Lock a mutex.

[w1\_read\_bit](group__w1__data__link.md#ga0f2b37163f3d7c9816371942765509b4)

int w1\_read\_bit(const struct device \*dev)

Read a single bit from the 1-Wire bus.

[w1\_read\_block](group__w1__data__link.md#ga2967c99ec93b7c31beb9cf2a327a23f4)

int w1\_read\_block(const struct device \*dev, uint8\_t \*buffer, size\_t len)

Read a block of data from the 1-Wire bus.

[w1\_write\_bit](group__w1__data__link.md#ga3671d8bbf9d044c60d7e96e4190ba2fa)

int w1\_write\_bit(const struct device \*dev, const bool bit)

Write a single bit to the 1-Wire bus.

[w1\_get\_slave\_count](group__w1__data__link.md#ga65892855c763dccc27b508d870c1d144)

size\_t w1\_get\_slave\_count(const struct device \*dev)

Get the number of slaves on the bus.

[w1\_read\_byte](group__w1__data__link.md#ga868980684bb98149af5b59e3fa8a83b6)

int w1\_read\_byte(const struct device \*dev)

Read a single byte from the 1-Wire bus.

[w1\_write\_byte](group__w1__data__link.md#ga978a8f14fb8cb3a569f8b731b20cc840)

int w1\_write\_byte(const struct device \*dev, uint8\_t byte)

Write a single byte to the 1-Wire bus.

[w1\_write\_block](group__w1__data__link.md#gab30a58c42c06088da9e0845de7d089ce)

int w1\_write\_block(const struct device \*dev, const uint8\_t \*buffer, size\_t len)

Write a block of data from the 1-Wire bus.

[w1\_reset\_bus](group__w1__data__link.md#gab4eccd585c6f14330807055ccc151fd6)

int w1\_reset\_bus(const struct device \*dev)

Reset the 1-Wire bus to prepare slaves for communication.

[w1\_configure](group__w1__data__link.md#gae989e0deebe5666edc9ff8a3839cf216)

int w1\_configure(const struct device \*dev, enum w1\_settings\_type type, uint32\_t value)

Configure parameters of the 1-Wire master.

[w1\_settings\_type](group__w1__interface.md#ga382989ef707709b5d26c40a394833612)

w1\_settings\_type

Defines the 1-Wire master settings types, which are runtime configurable.

**Definition** w1.h:53

[w1\_unlock\_bus](group__w1__interface.md#ga7230fad2428ab62fa963b50e67388c19)

static int w1\_unlock\_bus(const struct device \*dev)

Unlock the 1-wire bus.

**Definition** w1.h:158

[w1\_lock\_bus](group__w1__interface.md#gab18b0f60a126d38c982730d3ad9756c1)

static int w1\_lock\_bus(const struct device \*dev)

Lock the 1-wire bus to prevent simultaneous access.

**Definition** w1.h:143

[W1\_SETTING\_SPEED](group__w1__interface.md#gga382989ef707709b5d26c40a394833612a788fee2803793832c58951d623d823d5)

@ W1\_SETTING\_SPEED

Overdrive speed is enabled in case a value of 1 is passed and disabled passing 0.

**Definition** w1.h:57

[W1\_SETINGS\_TYPE\_COUNT](group__w1__interface.md#gga382989ef707709b5d26c40a394833612a814e27d05a04e027c52cb206aaf69b22)

@ W1\_SETINGS\_TYPE\_COUNT

Number of different settings types.

**Definition** w1.h:67

[W1\_SETTING\_STRONG\_PULLUP](group__w1__interface.md#gga382989ef707709b5d26c40a394833612ae3293dfeaa3f1976e8cf57e694d5f811)

@ W1\_SETTING\_STRONG\_PULLUP

The strong pullup resistor is activated immediately after the next written data block by passing a va...

**Definition** w1.h:62

[w1\_search\_rom](group__w1__network.md#ga024af0ee5018d7078808cc0a544cfd26)

static int w1\_search\_rom(const struct device \*dev, w1\_search\_callback\_t callback, void \*user\_data)

Search for 1-Wire slave on bus.

**Definition** w1.h:620

[w1\_search\_alarm](group__w1__network.md#ga0f510bd3720e54b4eeb4e368934db7f0)

static int w1\_search\_alarm(const struct device \*dev, w1\_search\_callback\_t callback, void \*user\_data)

Search for 1-Wire slaves with an active alarm.

**Definition** w1.h:642

[w1\_rom\_to\_uint64](group__w1__network.md#ga178a88d0c585d5df0405aadde3ea9178)

static uint64\_t w1\_rom\_to\_uint64(const struct w1\_rom \*rom)

Function to convert a w1\_rom struct to an uint64\_t.

**Definition** w1.h:656

[w1\_search\_bus](group__w1__network.md#ga19533f445029a69aac7d4ca5a7aeedcd)

int w1\_search\_bus(const struct device \*dev, uint8\_t command, uint8\_t family, w1\_search\_callback\_t callback, void \*user\_data)

Search 1-wire slaves on the bus.

[w1\_write\_read](group__w1__network.md#ga1cf8c016ac66c3970f72fa1f409fa680)

int w1\_write\_read(const struct device \*dev, const struct w1\_slave\_config \*config, const uint8\_t \*write\_buf, size\_t write\_len, uint8\_t \*read\_buf, size\_t read\_len)

Write then read data from the 1-Wire slave with matching ROM.

[w1\_search\_callback\_t](group__w1__network.md#ga2f5540f2a86fd55edcd7a8ffecbfd786)

void(\* w1\_search\_callback\_t)(struct w1\_rom rom, void \*user\_data)

Define the application callback handler function signature for searches.

**Definition** w1.h:469

[w1\_crc8](group__w1__network.md#ga350a384a6040d1fbb86bfb804013ade3)

static uint8\_t w1\_crc8(const uint8\_t \*src, size\_t len)

Compute CRC-8 chacksum as defined in the 1-Wire specification.

**Definition** w1.h:684

[w1\_match\_rom](group__w1__network.md#ga53f34d64504498dbb194bc2119727908)

int w1\_match\_rom(const struct device \*dev, const struct w1\_slave\_config \*config)

Select a specific slave by broadcasting a selected ROM.

[w1\_crc16](group__w1__network.md#ga5635f79a54a2e5b96c8b7ca9a8ab8366)

static uint16\_t w1\_crc16(const uint16\_t seed, const uint8\_t \*src, const size\_t len)

Compute 1-Wire variant of CRC 16.

**Definition** w1.h:704

[W1\_CMD\_SEARCH\_ROM](group__w1__network.md#ga57f17871edab0b771f2f664bf9bafb79)

#define W1\_CMD\_SEARCH\_ROM

This command allows the bus master to discover the addresses (i.e., ROM codes) of all slave devices o...

**Definition** w1.h:382

[w1\_resume\_command](group__w1__network.md#ga67c815bb99b75c862a483d4f8556b24a)

int w1\_resume\_command(const struct device \*dev)

Select the slave last addressed with a Match ROM or Search ROM commnad.

[w1\_uint64\_to\_rom](group__w1__network.md#ga6e4dba051a6b29c974e499db17315034)

static void w1\_uint64\_to\_rom(const uint64\_t rom64, struct w1\_rom \*rom)

Function to write an uint64\_t to struct w1\_rom pointer.

**Definition** w1.h:667

[W1\_SEARCH\_ALL\_FAMILIES](group__w1__network.md#ga909502b9b18c15a9ab0da8d3605e8c37)

#define W1\_SEARCH\_ALL\_FAMILIES

This flag can be passed to searches in order to not filter on family ID.

**Definition** w1.h:421

[w1\_read\_rom](group__w1__network.md#ga93abefbd0e7067db474e6480301a0c4c)

int w1\_read\_rom(const struct device \*dev, struct w1\_rom \*rom)

Read Peripheral 64-bit ROM.

[w1\_reset\_select](group__w1__network.md#gaa0acc88fe02535a3d512b866b6d34b8a)

int w1\_reset\_select(const struct device \*dev, const struct w1\_slave\_config \*config)

In single drop configurations use Skip Select command, otherweise use Match ROM command.

[W1\_CRC8\_SEED](group__w1__network.md#gaa4ad8d9a3791fbca6c99d49b9793a002)

#define W1\_CRC8\_SEED

Seed value used to calculate the 1-Wire 8-bit crc.

**Definition** w1.h:410

[W1\_CRC16\_POLYNOMIAL](group__w1__network.md#gab94362fbf4eec5f115f93fc8976cff0d)

#define W1\_CRC16\_POLYNOMIAL

Polynomial used to calculate the 1-Wire 16-bit crc.

**Definition** w1.h:416

[w1\_skip\_rom](group__w1__network.md#gaba2be4e87ff472e90b705dbd73b913de)

int w1\_skip\_rom(const struct device \*dev, const struct w1\_slave\_config \*config)

Select all slaves regardless of ROM.

[W1\_CRC8\_POLYNOMIAL](group__w1__network.md#gabe56ffbe20c2ba7e0a5c87c8e36c45e5)

#define W1\_CRC8\_POLYNOMIAL

Polynomial used to calculate the 1-Wire 8-bit crc.

**Definition** w1.h:412

[W1\_CMD\_SEARCH\_ALARM](group__w1__network.md#gafc7a257428c69bb4549c6cd05a928957)

#define W1\_CMD\_SEARCH\_ALARM

This command allows the bus master to identify which devices have experienced an alarm condition.

**Definition** w1.h:388

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

[size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)

Size of off\_t must be equal or less than size of size\_t

**Definition** retained\_mem.h:28

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:397

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[device::config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc)

const void \* config

Address of device instance config information.

**Definition** device.h:391

[w1\_rom](structw1__rom.md)

w1\_rom struct.

**Definition** w1.h:432

[w1\_rom::serial](structw1__rom.md#a134ee6d6e5e5eb711caf59449d11732e)

uint8\_t serial[6]

The serial together with the family code composes the unique 56-bit id.

**Definition** w1.h:441

[w1\_rom::crc](structw1__rom.md#a73d85d7ce0ef671027c910b9b7a54165)

uint8\_t crc

8-bit checksum of the 56-bit unique id.

**Definition** w1.h:443

[w1\_rom::family](structw1__rom.md#adc7f4f9fca172392b11864a17424a14c)

uint8\_t family

The 1-Wire family code identifying the slave device type.

**Definition** w1.h:439

[w1\_slave\_config](structw1__slave__config.md)

Node specific 1-wire configuration struct.

**Definition** w1.h:452

[w1\_slave\_config::rom](structw1__slave__config.md#a9f42fd1257483f308115ae02e6ef8596)

struct w1\_rom rom

Unique 1-Wire ROM.

**Definition** w1.h:454

[w1\_slave\_config::overdrive](structw1__slave__config.md#ab8a2d4522505416863fed561df22d058)

uint32\_t overdrive

overdrive speed is used if set to 1.

**Definition** w1.h:456

[byteorder.h](sys_2byteorder_8h.md)

Byte order helpers.

[sys\_put\_be64](sys_2byteorder_8h.md#a3e0d2e4e85249497011f5f9ea0d2987c)

static void sys\_put\_be64(uint64\_t val, uint8\_t dst[8])

Put a 64-bit integer as big-endian to arbitrary location.

**Definition** byteorder.h:368

[sys\_get\_be64](sys_2byteorder_8h.md#ad8e00ff5c0b9e394291936d1a570c215)

static uint64\_t sys\_get\_be64(const uint8\_t src[8])

Get a 64-bit integer stored in big-endian format.

**Definition** byteorder.h:519

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [w1.h](w1_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
