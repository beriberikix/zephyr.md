---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/qspi__if_8h_source.html
original_path: doxygen/html/qspi__if_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

qspi\_if.h

[Go to the documentation of this file.](qspi__if_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef \_\_QSPI\_IF\_H\_\_

13#define \_\_QSPI\_IF\_H\_\_

14

15#include <[zephyr/kernel.h](kernel_8h.md)>

16#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

17#ifdef CONFIG\_NRF70\_ON\_QSPI

18#include <nrfx\_qspi.h>

19#endif

20

[ 21](qspi__if_8h.md#a84e11529cde7bba98bc0e612c4dec8a7)#define RPU\_WAKEUP\_NOW BIT(0) /\* WAKEUP RPU - RW \*/

[ 22](qspi__if_8h.md#a4d4c792a7693d161e62fd7ea78f3ac33)#define RPU\_AWAKE\_BIT BIT(1) /\* RPU AWAKE FROM SLEEP - RO \*/

[ 23](qspi__if_8h.md#adf0f3cc72222e245bec2922f9d48d7b9)#define RPU\_READY\_BIT BIT(2) /\* RPU IS READY - RO\*/

24

[ 25](structqspi__config.md)struct [qspi\_config](structqspi__config.md) {

26#ifdef CONFIG\_NRF70\_ON\_QSPI

27 nrf\_qspi\_addrmode\_t addrmode;

28 nrf\_qspi\_readoc\_t readoc;

29 nrf\_qspi\_writeoc\_t writeoc;

30 nrf\_qspi\_frequency\_t sckfreq;

31#endif

[ 32](structqspi__config.md#a0871c7febd31179f45eb095b70f5caee) unsigned char [RDC4IO](structqspi__config.md#a0871c7febd31179f45eb095b70f5caee);

[ 33](structqspi__config.md#a6b79c9618e16540f93714008462b51be) bool [easydma](structqspi__config.md#a6b79c9618e16540f93714008462b51be);

[ 34](structqspi__config.md#a4b69e092bf8f73ac8e9b416690a58d28) bool [single\_op](structqspi__config.md#a4b69e092bf8f73ac8e9b416690a58d28);

[ 35](structqspi__config.md#aac7103e7473ccd56c2b9b3dc747f7ce1) bool [quad\_spi](structqspi__config.md#aac7103e7473ccd56c2b9b3dc747f7ce1);

[ 36](structqspi__config.md#a88db2e115bbd7a1928c8cc54dba3857f) bool [encryption](structqspi__config.md#a88db2e115bbd7a1928c8cc54dba3857f);

[ 37](structqspi__config.md#a259a8d91bfe758d84df07acfc55499b6) bool [CMD\_CNONCE](structqspi__config.md#a259a8d91bfe758d84df07acfc55499b6);

[ 38](structqspi__config.md#aee934c27f6916f6c7297db5a1e6e8ded) bool [enc\_enabled](structqspi__config.md#aee934c27f6916f6c7297db5a1e6e8ded);

[ 39](structqspi__config.md#abaf0a8bf1706301dcd27e1f4a17676af) struct k\_sem [lock](structqspi__config.md#abaf0a8bf1706301dcd27e1f4a17676af);

[ 40](structqspi__config.md#a38bd66f9b0acdf6f0a656427b7c0c7f8) unsigned int [addrmask](structqspi__config.md#a38bd66f9b0acdf6f0a656427b7c0c7f8);

[ 41](structqspi__config.md#ab0c0611e6960a1c84e02f987f3c2a767) unsigned char [qspi\_slave\_latency](structqspi__config.md#ab0c0611e6960a1c84e02f987f3c2a767);

42#if defined(CONFIG\_NRF70\_ON\_QSPI) && (NRF\_QSPI\_HAS\_XIP\_ENC || NRF\_QSPI\_HAS\_DMA\_ENC)

43 nrf\_qspi\_encryption\_t p\_cfg;

44#endif /\*CONFIG\_NRF70\_ON\_QSPI && (NRF\_QSPI\_HAS\_XIP\_ENC || NRF\_QSPI\_HAS\_DMA\_ENC)\*/

[ 45](structqspi__config.md#a945333ae972b568219b94b2ed5f640a9) int [test\_hlread](structqspi__config.md#a945333ae972b568219b94b2ed5f640a9);

[ 46](structqspi__config.md#a2d01b48538d0103b03faf800b9d74819) char \*[test\_name](structqspi__config.md#a2d01b48538d0103b03faf800b9d74819);

[ 47](structqspi__config.md#a5df29101652b0101b9cd24ffc8c469e9) int [test\_start](structqspi__config.md#a5df29101652b0101b9cd24ffc8c469e9);

[ 48](structqspi__config.md#a386c8f8150985ea26f1f7fb92abdd344) int [test\_end](structqspi__config.md#a386c8f8150985ea26f1f7fb92abdd344);

[ 49](structqspi__config.md#a8f3a31437f28208b5ce6b00c702b7c44) int [test\_iterations](structqspi__config.md#a8f3a31437f28208b5ce6b00c702b7c44);

[ 50](structqspi__config.md#a3bb96eee89df742635aa9cbc1101c025) int [test\_timediff\_read](structqspi__config.md#a3bb96eee89df742635aa9cbc1101c025);

[ 51](structqspi__config.md#a423967ddc3952545c7f2081a8b649992) int [test\_timediff\_write](structqspi__config.md#a423967ddc3952545c7f2081a8b649992);

[ 52](structqspi__config.md#ad147f9c013f82fb08ca674f09791f731) int [test\_status](structqspi__config.md#ad147f9c013f82fb08ca674f09791f731);

[ 53](structqspi__config.md#a729d72b95d82092c2b9b7b1b17d2a121) int [test\_iteration](structqspi__config.md#a729d72b95d82092c2b9b7b1b17d2a121);

54};

[ 55](structqspi__dev.md)struct [qspi\_dev](structqspi__dev.md) {

[ 56](structqspi__dev.md#a29a97c1f869a4538bcf829e3d6b3c2ab) int (\*[deinit](structqspi__dev.md#a29a97c1f869a4538bcf829e3d6b3c2ab))(void);

[ 57](structqspi__dev.md#af25dcbe7de18525172dfb3fd8fc9e6fc) void \*[config](structqspi__dev.md#af25dcbe7de18525172dfb3fd8fc9e6fc);

[ 58](structqspi__dev.md#affbb12cc141db791e43db4e10e396a39) int (\*[init](structqspi__dev.md#affbb12cc141db791e43db4e10e396a39))(struct [qspi\_config](structqspi__config.md) \*[config](structqspi__dev.md#af25dcbe7de18525172dfb3fd8fc9e6fc));

[ 59](structqspi__dev.md#adb95f998ffb510ea555c14ca4edfdbb0) int (\*[write](structqspi__dev.md#adb95f998ffb510ea555c14ca4edfdbb0))(unsigned int addr, const void \*data, int len);

[ 60](structqspi__dev.md#a4aa5d9952cea1d00f104a2299cee2669) int (\*[read](structqspi__dev.md#a4aa5d9952cea1d00f104a2299cee2669))(unsigned int addr, void \*data, int len);

[ 61](structqspi__dev.md#a591de50877cd5c1de7e4c2a4aa4f1a53) int (\*[hl\_read](structqspi__dev.md#a591de50877cd5c1de7e4c2a4aa4f1a53))(unsigned int addr, void \*data, int len);

[ 62](structqspi__dev.md#a5ffd087ce38cd40a4db3fa6dcd5872aa) void (\*[hard\_reset](structqspi__dev.md#a5ffd087ce38cd40a4db3fa6dcd5872aa))(void);

63};

64

[ 65](qspi__if_8h.md#a5ee3cedbf2fe79babdbb5268874a6e93)int [qspi\_cmd\_wakeup\_rpu](qspi__if_8h.md#a5ee3cedbf2fe79babdbb5268874a6e93)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data);

66

[ 67](qspi__if_8h.md#a424155de82df701be9706afae24e920d)int [qspi\_init](qspi__if_8h.md#a424155de82df701be9706afae24e920d)(struct [qspi\_config](structqspi__config.md) \*config);

68

[ 69](qspi__if_8h.md#aa277c292d448168861400c43d8f75b92)int [qspi\_write](qspi__if_8h.md#aa277c292d448168861400c43d8f75b92)(unsigned int addr, const void \*data, int len);

70

[ 71](qspi__if_8h.md#a1b48dfac997cc62e27f54304cc3c0bfc)int [qspi\_read](qspi__if_8h.md#a1b48dfac997cc62e27f54304cc3c0bfc)(unsigned int addr, void \*data, int len);

72

[ 73](qspi__if_8h.md#ab44ab165657864085e9a747f198b7eec)int [qspi\_hl\_read](qspi__if_8h.md#ab44ab165657864085e9a747f198b7eec)(unsigned int addr, void \*data, int len);

74

[ 75](qspi__if_8h.md#a31827628f36adae2af395c906a118d40)int [qspi\_deinit](qspi__if_8h.md#a31827628f36adae2af395c906a118d40)(void);

76

[ 77](qspi__if_8h.md#aa73129b0b275e974361fa5a0ef252c2f)void [gpio\_free\_irq](qspi__if_8h.md#aa73129b0b275e974361fa5a0ef252c2f)(int pin, struct [gpio\_callback](structgpio__callback.md) \*button\_cb\_data);

78

[ 79](qspi__if_8h.md#a8bed70457c6dfbb6fe7dd1540390cfb7)int [gpio\_request\_irq](qspi__if_8h.md#a8bed70457c6dfbb6fe7dd1540390cfb7)(int pin, struct [gpio\_callback](structgpio__callback.md) \*button\_cb\_data, void (\*irq\_handler)());

80

[ 81](qspi__if_8h.md#a01aa4b1df13cf07ea545c14e0bd82828)struct [qspi\_config](structqspi__config.md) \*[qspi\_defconfig](qspi__if_8h.md#a01aa4b1df13cf07ea545c14e0bd82828)(void);

82

[ 83](qspi__if_8h.md#ae7e8a05b3fcc5e483398493e2a7d7e93)struct [qspi\_dev](structqspi__dev.md) \*[qspi\_dev](qspi__if_8h.md#ae7e8a05b3fcc5e483398493e2a7d7e93)(void);

[ 84](qspi__if_8h.md#a8d943d5376b6cf3c9d4f37bcf5fc306a)struct [qspi\_config](structqspi__config.md) \*[qspi\_get\_config](qspi__if_8h.md#a8d943d5376b6cf3c9d4f37bcf5fc306a)(void);

85

[ 86](qspi__if_8h.md#ade1b91ab08c431e4a884013b87fda0a4)int [qspi\_cmd\_sleep\_rpu](qspi__if_8h.md#ade1b91ab08c431e4a884013b87fda0a4)(const struct [device](structdevice.md) \*dev);

87

[ 88](qspi__if_8h.md#afb4a6c00361cf7109799350d3b27ad83)void [hard\_reset](qspi__if_8h.md#afb4a6c00361cf7109799350d3b27ad83)(void);

[ 89](qspi__if_8h.md#a14aeaefb2884e2dd7b2000c724069f31)void [get\_sleep\_stats](qspi__if_8h.md#a14aeaefb2884e2dd7b2000c724069f31)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wrd\_len);

90

91extern struct [device](structdevice.md) [qspi\_perip](qspi__if_8h.md#a1814c557c5e1a14b180cdb96ffdc6efc);

92

[ 93](qspi__if_8h.md#afba5e08a80ba35ed4860f244ca177364)int [qspi\_validate\_rpu\_wake\_writecmd](qspi__if_8h.md#afba5e08a80ba35ed4860f244ca177364)(const struct [device](structdevice.md) \*dev);

94int [qspi\_cmd\_wakeup\_rpu](qspi__if_8h.md#a5ee3cedbf2fe79babdbb5268874a6e93)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

[ 95](qspi__if_8h.md#aa48981a0dad166b00a07a7fd724ea899)int [qspi\_wait\_while\_rpu\_awake](qspi__if_8h.md#aa48981a0dad166b00a07a7fd724ea899)(const struct [device](structdevice.md) \*dev);

96

[ 97](qspi__if_8h.md#a5d234f9a705746b4406d587437de92ed)int [qspi\_RDSR1](qspi__if_8h.md#a5d234f9a705746b4406d587437de92ed)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rdsr1);

[ 98](qspi__if_8h.md#af5b8aea6ccbe60b83c5b10c05f197b41)int [qspi\_RDSR2](qspi__if_8h.md#af5b8aea6ccbe60b83c5b10c05f197b41)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rdsr2);

[ 99](qspi__if_8h.md#a88ab9dead7c0272b233dfb6d941b4a85)int [qspi\_WRSR2](qspi__if_8h.md#a88ab9dead7c0272b233dfb6d941b4a85)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wrsr2);

100

101#ifdef CONFIG\_NRF\_WIFI\_LOW\_POWER

102int func\_rpu\_sleep(void);

103int func\_rpu\_wake(void);

104int func\_rpu\_sleep\_status(void);

105#endif /\* CONFIG\_NRF\_WIFI\_LOW\_POWER \*/

106

[ 107](qspi__if_8h.md#aaab62367cf18acc6c77435eac0e84d1c)#define QSPI\_KEY\_LEN\_BYTES 16

108

[ 114](qspi__if_8h.md#ae1f2810d7be515acbb2944f600dbf765)int [qspi\_enable\_encryption](qspi__if_8h.md#ae1f2810d7be515acbb2944f600dbf765)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*key);

115

116#endif /\* \_\_QSPI\_IF\_H\_\_ \*/

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[qspi\_defconfig](qspi__if_8h.md#a01aa4b1df13cf07ea545c14e0bd82828)

struct qspi\_config \* qspi\_defconfig(void)

[get\_sleep\_stats](qspi__if_8h.md#a14aeaefb2884e2dd7b2000c724069f31)

void get\_sleep\_stats(uint32\_t addr, uint32\_t \*buff, uint32\_t wrd\_len)

[qspi\_perip](qspi__if_8h.md#a1814c557c5e1a14b180cdb96ffdc6efc)

struct device qspi\_perip

[qspi\_read](qspi__if_8h.md#a1b48dfac997cc62e27f54304cc3c0bfc)

int qspi\_read(unsigned int addr, void \*data, int len)

[qspi\_deinit](qspi__if_8h.md#a31827628f36adae2af395c906a118d40)

int qspi\_deinit(void)

[qspi\_init](qspi__if_8h.md#a424155de82df701be9706afae24e920d)

int qspi\_init(struct qspi\_config \*config)

[qspi\_RDSR1](qspi__if_8h.md#a5d234f9a705746b4406d587437de92ed)

int qspi\_RDSR1(const struct device \*dev, uint8\_t \*rdsr1)

[qspi\_cmd\_wakeup\_rpu](qspi__if_8h.md#a5ee3cedbf2fe79babdbb5268874a6e93)

int qspi\_cmd\_wakeup\_rpu(const struct device \*dev, uint8\_t data)

[qspi\_WRSR2](qspi__if_8h.md#a88ab9dead7c0272b233dfb6d941b4a85)

int qspi\_WRSR2(const struct device \*dev, const uint8\_t wrsr2)

[gpio\_request\_irq](qspi__if_8h.md#a8bed70457c6dfbb6fe7dd1540390cfb7)

int gpio\_request\_irq(int pin, struct gpio\_callback \*button\_cb\_data, void(\*irq\_handler)())

[qspi\_get\_config](qspi__if_8h.md#a8d943d5376b6cf3c9d4f37bcf5fc306a)

struct qspi\_config \* qspi\_get\_config(void)

[qspi\_write](qspi__if_8h.md#aa277c292d448168861400c43d8f75b92)

int qspi\_write(unsigned int addr, const void \*data, int len)

[qspi\_wait\_while\_rpu\_awake](qspi__if_8h.md#aa48981a0dad166b00a07a7fd724ea899)

int qspi\_wait\_while\_rpu\_awake(const struct device \*dev)

[gpio\_free\_irq](qspi__if_8h.md#aa73129b0b275e974361fa5a0ef252c2f)

void gpio\_free\_irq(int pin, struct gpio\_callback \*button\_cb\_data)

[qspi\_hl\_read](qspi__if_8h.md#ab44ab165657864085e9a747f198b7eec)

int qspi\_hl\_read(unsigned int addr, void \*data, int len)

[qspi\_cmd\_sleep\_rpu](qspi__if_8h.md#ade1b91ab08c431e4a884013b87fda0a4)

int qspi\_cmd\_sleep\_rpu(const struct device \*dev)

[qspi\_enable\_encryption](qspi__if_8h.md#ae1f2810d7be515acbb2944f600dbf765)

int qspi\_enable\_encryption(uint8\_t \*key)

Enable encryption.

[qspi\_dev](qspi__if_8h.md#ae7e8a05b3fcc5e483398493e2a7d7e93)

struct qspi\_dev \* qspi\_dev(void)

[qspi\_RDSR2](qspi__if_8h.md#af5b8aea6ccbe60b83c5b10c05f197b41)

int qspi\_RDSR2(const struct device \*dev, uint8\_t \*rdsr2)

[hard\_reset](qspi__if_8h.md#afb4a6c00361cf7109799350d3b27ad83)

void hard\_reset(void)

[qspi\_validate\_rpu\_wake\_writecmd](qspi__if_8h.md#afba5e08a80ba35ed4860f244ca177364)

int qspi\_validate\_rpu\_wake\_writecmd(const struct device \*dev)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:463

[gpio\_callback](structgpio__callback.md)

GPIO callback structure.

**Definition** gpio.h:741

[qspi\_config](structqspi__config.md)

**Definition** qspi\_if.h:25

[qspi\_config::RDC4IO](structqspi__config.md#a0871c7febd31179f45eb095b70f5caee)

unsigned char RDC4IO

**Definition** qspi\_if.h:32

[qspi\_config::CMD\_CNONCE](structqspi__config.md#a259a8d91bfe758d84df07acfc55499b6)

bool CMD\_CNONCE

**Definition** qspi\_if.h:37

[qspi\_config::test\_name](structqspi__config.md#a2d01b48538d0103b03faf800b9d74819)

char \* test\_name

**Definition** qspi\_if.h:46

[qspi\_config::test\_end](structqspi__config.md#a386c8f8150985ea26f1f7fb92abdd344)

int test\_end

**Definition** qspi\_if.h:48

[qspi\_config::addrmask](structqspi__config.md#a38bd66f9b0acdf6f0a656427b7c0c7f8)

unsigned int addrmask

**Definition** qspi\_if.h:40

[qspi\_config::test\_timediff\_read](structqspi__config.md#a3bb96eee89df742635aa9cbc1101c025)

int test\_timediff\_read

**Definition** qspi\_if.h:50

[qspi\_config::test\_timediff\_write](structqspi__config.md#a423967ddc3952545c7f2081a8b649992)

int test\_timediff\_write

**Definition** qspi\_if.h:51

[qspi\_config::single\_op](structqspi__config.md#a4b69e092bf8f73ac8e9b416690a58d28)

bool single\_op

**Definition** qspi\_if.h:34

[qspi\_config::test\_start](structqspi__config.md#a5df29101652b0101b9cd24ffc8c469e9)

int test\_start

**Definition** qspi\_if.h:47

[qspi\_config::easydma](structqspi__config.md#a6b79c9618e16540f93714008462b51be)

bool easydma

**Definition** qspi\_if.h:33

[qspi\_config::test\_iteration](structqspi__config.md#a729d72b95d82092c2b9b7b1b17d2a121)

int test\_iteration

**Definition** qspi\_if.h:53

[qspi\_config::encryption](structqspi__config.md#a88db2e115bbd7a1928c8cc54dba3857f)

bool encryption

**Definition** qspi\_if.h:36

[qspi\_config::test\_iterations](structqspi__config.md#a8f3a31437f28208b5ce6b00c702b7c44)

int test\_iterations

**Definition** qspi\_if.h:49

[qspi\_config::test\_hlread](structqspi__config.md#a945333ae972b568219b94b2ed5f640a9)

int test\_hlread

**Definition** qspi\_if.h:45

[qspi\_config::quad\_spi](structqspi__config.md#aac7103e7473ccd56c2b9b3dc747f7ce1)

bool quad\_spi

**Definition** qspi\_if.h:35

[qspi\_config::qspi\_slave\_latency](structqspi__config.md#ab0c0611e6960a1c84e02f987f3c2a767)

unsigned char qspi\_slave\_latency

**Definition** qspi\_if.h:41

[qspi\_config::lock](structqspi__config.md#abaf0a8bf1706301dcd27e1f4a17676af)

struct k\_sem lock

**Definition** qspi\_if.h:39

[qspi\_config::test\_status](structqspi__config.md#ad147f9c013f82fb08ca674f09791f731)

int test\_status

**Definition** qspi\_if.h:52

[qspi\_config::enc\_enabled](structqspi__config.md#aee934c27f6916f6c7297db5a1e6e8ded)

bool enc\_enabled

**Definition** qspi\_if.h:38

[qspi\_dev](structqspi__dev.md)

**Definition** qspi\_if.h:55

[qspi\_dev::deinit](structqspi__dev.md#a29a97c1f869a4538bcf829e3d6b3c2ab)

int(\* deinit)(void)

**Definition** qspi\_if.h:56

[qspi\_dev::read](structqspi__dev.md#a4aa5d9952cea1d00f104a2299cee2669)

int(\* read)(unsigned int addr, void \*data, int len)

**Definition** qspi\_if.h:60

[qspi\_dev::hl\_read](structqspi__dev.md#a591de50877cd5c1de7e4c2a4aa4f1a53)

int(\* hl\_read)(unsigned int addr, void \*data, int len)

**Definition** qspi\_if.h:61

[qspi\_dev::hard\_reset](structqspi__dev.md#a5ffd087ce38cd40a4db3fa6dcd5872aa)

void(\* hard\_reset)(void)

**Definition** qspi\_if.h:62

[qspi\_dev::write](structqspi__dev.md#adb95f998ffb510ea555c14ca4edfdbb0)

int(\* write)(unsigned int addr, const void \*data, int len)

**Definition** qspi\_if.h:59

[qspi\_dev::config](structqspi__dev.md#af25dcbe7de18525172dfb3fd8fc9e6fc)

void \* config

**Definition** qspi\_if.h:57

[qspi\_dev::init](structqspi__dev.md#affbb12cc141db791e43db4e10e396a39)

int(\* init)(struct qspi\_config \*config)

**Definition** qspi\_if.h:58

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [wifi](dir_478165533ab14baf575002d17a842a12.md)
- [nrf\_wifi](dir_827a5ceb820ded32f2709b259acb2436.md)
- [bus](dir_a8af871e2af95a2ae463c0a62cb13e77.md)
- [qspi\_if.h](qspi__if_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
