---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sd_8h_source.html
original_path: doxygen/html/sd_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sd.h

[Go to the documentation of this file.](sd_8h.md)

1/\*

2 \* Copyright 2022 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_SD\_SD\_H\_

13#define ZEPHYR\_INCLUDE\_SD\_SD\_H\_

14

15#include <[zephyr/device.h](device_8h.md)>

16#include <[zephyr/drivers/sdhc.h](sdhc_8h.md)>

17#include <[zephyr/kernel.h](kernel_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

[ 26](sd_8h.md#a52167aac735d93085a5eebc6f50e1bba)enum [card\_status](sd_8h.md#a52167aac735d93085a5eebc6f50e1bba) {

[ 27](sd_8h.md#a52167aac735d93085a5eebc6f50e1bbaaa059e919850b36b85ebe33a07050e453) [CARD\_UNINITIALIZED](sd_8h.md#a52167aac735d93085a5eebc6f50e1bbaaa059e919850b36b85ebe33a07050e453) = 0,

[ 28](sd_8h.md#a52167aac735d93085a5eebc6f50e1bbaa5458e6fab05f8c1afbe7d191eb489e5e) [CARD\_ERROR](sd_8h.md#a52167aac735d93085a5eebc6f50e1bbaa5458e6fab05f8c1afbe7d191eb489e5e) = 1,

[ 29](sd_8h.md#a52167aac735d93085a5eebc6f50e1bbaa839d17bb0bee41a125a617683bce17c9) [CARD\_INITIALIZED](sd_8h.md#a52167aac735d93085a5eebc6f50e1bbaa839d17bb0bee41a125a617683bce17c9) = 2,

30};

31

[ 35](sd_8h.md#aee707e2ff5691dbdefd9341a18de7b14)enum [card\_type](sd_8h.md#aee707e2ff5691dbdefd9341a18de7b14) {

[ 36](sd_8h.md#aee707e2ff5691dbdefd9341a18de7b14a8b26749346e26d9257cd53c48a68eda4) [CARD\_SDMMC](sd_8h.md#aee707e2ff5691dbdefd9341a18de7b14a8b26749346e26d9257cd53c48a68eda4) = 0,

[ 37](sd_8h.md#aee707e2ff5691dbdefd9341a18de7b14a5afc0338b5a0541bb34f1a5b67139b6b) [CARD\_SDIO](sd_8h.md#aee707e2ff5691dbdefd9341a18de7b14a5afc0338b5a0541bb34f1a5b67139b6b) = 1,

[ 38](sd_8h.md#aee707e2ff5691dbdefd9341a18de7b14ad527710e81e76e0938689015c2013090) [CARD\_COMBO](sd_8h.md#aee707e2ff5691dbdefd9341a18de7b14ad527710e81e76e0938689015c2013090) = 2,

[ 39](sd_8h.md#aee707e2ff5691dbdefd9341a18de7b14a868625c31f4384780de3992d78b93345) [CARD\_MMC](sd_8h.md#aee707e2ff5691dbdefd9341a18de7b14a868625c31f4384780de3992d78b93345) = 3,

40};

41

[ 48](structsdio__func.md)struct [sdio\_func](structsdio__func.md) {

[ 49](structsdio__func.md#a3bc320f1ca7268344b848a998ace615c) enum [sdio\_func\_num](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6) [num](structsdio__func.md#a3bc320f1ca7268344b848a998ace615c);

[ 50](structsdio__func.md#a7387979362ba892c013a7a69e004d96b) struct [sd\_card](structsd__card.md) \*[card](structsdio__func.md#a7387979362ba892c013a7a69e004d96b);

[ 51](structsdio__func.md#af83e71e628841b8acf70130261a97060) struct [sdio\_cis](structsdio__cis.md) [cis](structsdio__func.md#af83e71e628841b8acf70130261a97060);

[ 52](structsdio__func.md#aa4ad13eb77f656020b38f6cf165e2965) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [block\_size](structsdio__func.md#aa4ad13eb77f656020b38f6cf165e2965);

53};

54

55

[ 63](structsd__card.md)struct [sd\_card](structsd__card.md) {

[ 64](structsd__card.md#afabeaa207f2f5caaec8cfedac6b35661) const struct [device](structdevice.md) \*[sdhc](structsd__card.md#afabeaa207f2f5caaec8cfedac6b35661);

[ 65](structsd__card.md#a875b7081a3e647b782cdb835372f5029) struct [sdhc\_io](structsdhc__io.md) [bus\_io](structsd__card.md#a875b7081a3e647b782cdb835372f5029);

[ 66](structsd__card.md#ae8e85d2fc44a97b42247d87a5c2aafdf) enum [sd\_voltage](group__sdhc__interface.md#ga34041edf280f125b8500809226b3de5d) [card\_voltage](structsd__card.md#ae8e85d2fc44a97b42247d87a5c2aafdf);

[ 67](structsd__card.md#aba2501397066d0930691c40778405aa7) struct [k\_mutex](structk__mutex.md) [lock](structsd__card.md#aba2501397066d0930691c40778405aa7);

[ 68](structsd__card.md#a9f597007072d3af5b70ea5cc2a4cbd29) struct [sdhc\_host\_props](structsdhc__host__props.md) [host\_props](structsd__card.md#a9f597007072d3af5b70ea5cc2a4cbd29);

[ 69](structsd__card.md#a856e7ea75577c62be17dc5d8c99908f4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ocr](structsd__card.md#a856e7ea75577c62be17dc5d8c99908f4);

[ 70](structsd__card.md#a03eac55046f7222c97d60fa919e3cae9) struct [sd\_switch\_caps](structsd__switch__caps.md) [switch\_caps](structsd__card.md#a03eac55046f7222c97d60fa919e3cae9);

[ 71](structsd__card.md#a17a021db8aa3a8ad224e422f3854eafc) unsigned int [num\_io](structsd__card.md#a17a021db8aa3a8ad224e422f3854eafc): 3;

[ 72](structsd__card.md#a1db9545598f0eb6b6440e63d4941d2ab) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [relative\_addr](structsd__card.md#a1db9545598f0eb6b6440e63d4941d2ab);

[ 73](structsd__card.md#acdcfdaab67d284ef3a8ee3202fd7a538) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [block\_count](structsd__card.md#acdcfdaab67d284ef3a8ee3202fd7a538);

[ 74](structsd__card.md#a3d29b73f029af5182475c2a2d365173b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [block\_size](structsd__card.md#a3d29b73f029af5182475c2a2d365173b);

[ 75](structsd__card.md#a5a9a627df5daf23b468ce705bf5f5f81) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sd\_version](structsd__card.md#a5a9a627df5daf23b468ce705bf5f5f81);

[ 76](structsd__card.md#a8beccfe60fc714c159528fbd2c122b16) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [card\_speed](structsd__card.md#a8beccfe60fc714c159528fbd2c122b16);

[ 77](structsd__card.md#a03d7be3154dcd881df60921681a4f308) enum [card\_status](sd_8h.md#a52167aac735d93085a5eebc6f50e1bba) [status](structsd__card.md#a03d7be3154dcd881df60921681a4f308);

[ 78](structsd__card.md#a798acb1bb9495d1009a23f139d269108) enum [card\_type](sd_8h.md#aee707e2ff5691dbdefd9341a18de7b14) [type](structsd__card.md#a798acb1bb9495d1009a23f139d269108);

[ 79](structsd__card.md#ad5d6e798ae8b04d829fb8131f6cb1ccf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structsd__card.md#ad5d6e798ae8b04d829fb8131f6cb1ccf);

[ 80](structsd__card.md#a38383b8f5c1f9bff1537f407fbec9faf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bus\_width](structsd__card.md#a38383b8f5c1f9bff1537f407fbec9faf);

[ 81](structsd__card.md#ab122e442ab3ba5078c99a98a861ec908) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cccr\_flags](structsd__card.md#ab122e442ab3ba5078c99a98a861ec908);

[ 82](structsd__card.md#a93986ee5db729d9931b4ababe41c303a) struct [sdio\_func](structsdio__func.md) [func0](structsd__card.md#a93986ee5db729d9931b4ababe41c303a);

83

84 /\* NOTE: The buffer is accessed as a uint32\_t\* by the SD subsystem, so must be

85 \* aligned to 4 bytes for platforms that don't support unaligned access...

86 \* Systems where the buffer is accessed by DMA may require wider alignment, in

87 \* which case, use CONFIG\_SDHC\_BUFFER\_ALIGNMENT.

88 \*/

[ 89](structsd__card.md#a81c9ec36c79e77599c10163455c86e7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [card\_buffer](structsd__card.md#a81c9ec36c79e77599c10163455c86e7c)[CONFIG\_SD\_BUFFER\_SIZE]

90 \_\_aligned([MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(4, CONFIG\_SDHC\_BUFFER\_ALIGNMENT)); /\* Card internal buffer \*/

91};

92

[ 105](sd_8h.md#ac02b6fe46112b8b891e9713ef24bd131)int [sd\_init](sd_8h.md#ac02b6fe46112b8b891e9713ef24bd131)(const struct [device](structdevice.md) \*sdhc\_dev, struct [sd\_card](structsd__card.md) \*[card](structsdio__func.md#a7387979362ba892c013a7a69e004d96b));

106

[ 114](sd_8h.md#aed46c9c492c5c6434a6ae4d6151ac7d3)bool [sd\_is\_card\_present](sd_8h.md#aed46c9c492c5c6434a6ae4d6151ac7d3)(const struct [device](structdevice.md) \*sdhc\_dev);

115

116

117#ifdef \_\_cplusplus

118}

119#endif

120

121#endif /\* ZEPHYR\_INCLUDE\_SD\_SD\_H\_ \*/

[device.h](device_8h.md)

[sd\_voltage](group__sdhc__interface.md#ga34041edf280f125b8500809226b3de5d)

sd\_voltage

SD voltage.

**Definition** sdhc.h:146

[MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)

#define MAX(a, b)

Obtain the maximum of two values.

**Definition** util.h:376

[kernel.h](kernel_8h.md)

Public kernel APIs.

[card\_status](sd_8h.md#a52167aac735d93085a5eebc6f50e1bba)

card\_status

card status.

**Definition** sd.h:26

[CARD\_ERROR](sd_8h.md#a52167aac735d93085a5eebc6f50e1bbaa5458e6fab05f8c1afbe7d191eb489e5e)

@ CARD\_ERROR

card state is error

**Definition** sd.h:28

[CARD\_INITIALIZED](sd_8h.md#a52167aac735d93085a5eebc6f50e1bbaa839d17bb0bee41a125a617683bce17c9)

@ CARD\_INITIALIZED

card is in valid state

**Definition** sd.h:29

[CARD\_UNINITIALIZED](sd_8h.md#a52167aac735d93085a5eebc6f50e1bbaaa059e919850b36b85ebe33a07050e453)

@ CARD\_UNINITIALIZED

card has not been initialized

**Definition** sd.h:27

[sd\_init](sd_8h.md#ac02b6fe46112b8b891e9713ef24bd131)

int sd\_init(const struct device \*sdhc\_dev, struct sd\_card \*card)

Initialize an SD device.

[sd\_is\_card\_present](sd_8h.md#aed46c9c492c5c6434a6ae4d6151ac7d3)

bool sd\_is\_card\_present(const struct device \*sdhc\_dev)

checks to see if card is present in the SD slot

[card\_type](sd_8h.md#aee707e2ff5691dbdefd9341a18de7b14)

card\_type

card type.

**Definition** sd.h:35

[CARD\_SDIO](sd_8h.md#aee707e2ff5691dbdefd9341a18de7b14a5afc0338b5a0541bb34f1a5b67139b6b)

@ CARD\_SDIO

SD I/O card.

**Definition** sd.h:37

[CARD\_MMC](sd_8h.md#aee707e2ff5691dbdefd9341a18de7b14a868625c31f4384780de3992d78b93345)

@ CARD\_MMC

MMC memory card.

**Definition** sd.h:39

[CARD\_SDMMC](sd_8h.md#aee707e2ff5691dbdefd9341a18de7b14a8b26749346e26d9257cd53c48a68eda4)

@ CARD\_SDMMC

SD memory card.

**Definition** sd.h:36

[CARD\_COMBO](sd_8h.md#aee707e2ff5691dbdefd9341a18de7b14ad527710e81e76e0938689015c2013090)

@ CARD\_COMBO

SD memory and I/O card.

**Definition** sd.h:38

[sdio\_func\_num](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6)

sdio\_func\_num

SDIO function number.

**Definition** sd\_spec.h:784

[sdhc.h](sdhc_8h.md)

SD Host Controller public API header file.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2917

[sd\_card](structsd__card.md)

SD card structure.

**Definition** sd.h:63

[sd\_card::status](structsd__card.md#a03d7be3154dcd881df60921681a4f308)

enum card\_status status

Card status.

**Definition** sd.h:77

[sd\_card::switch\_caps](structsd__card.md#a03eac55046f7222c97d60fa919e3cae9)

struct sd\_switch\_caps switch\_caps

SD switch capabilities.

**Definition** sd.h:70

[sd\_card::num\_io](structsd__card.md#a17a021db8aa3a8ad224e422f3854eafc)

unsigned int num\_io

I/O function count.

**Definition** sd.h:71

[sd\_card::relative\_addr](structsd__card.md#a1db9545598f0eb6b6440e63d4941d2ab)

uint16\_t relative\_addr

Card relative address.

**Definition** sd.h:72

[sd\_card::bus\_width](structsd__card.md#a38383b8f5c1f9bff1537f407fbec9faf)

uint8\_t bus\_width

Desired bus width.

**Definition** sd.h:80

[sd\_card::block\_size](structsd__card.md#a3d29b73f029af5182475c2a2d365173b)

uint16\_t block\_size

SD block size.

**Definition** sd.h:74

[sd\_card::sd\_version](structsd__card.md#a5a9a627df5daf23b468ce705bf5f5f81)

uint8\_t sd\_version

SD specification version.

**Definition** sd.h:75

[sd\_card::type](structsd__card.md#a798acb1bb9495d1009a23f139d269108)

enum card\_type type

Card type.

**Definition** sd.h:78

[sd\_card::card\_buffer](structsd__card.md#a81c9ec36c79e77599c10163455c86e7c)

uint8\_t card\_buffer[CONFIG\_SD\_BUFFER\_SIZE]

**Definition** sd.h:90

[sd\_card::ocr](structsd__card.md#a856e7ea75577c62be17dc5d8c99908f4)

uint32\_t ocr

Raw card OCR content.

**Definition** sd.h:69

[sd\_card::bus\_io](structsd__card.md#a875b7081a3e647b782cdb835372f5029)

struct sdhc\_io bus\_io

Current bus I/O props for SDHC.

**Definition** sd.h:65

[sd\_card::card\_speed](structsd__card.md#a8beccfe60fc714c159528fbd2c122b16)

uint8\_t card\_speed

Card timing mode.

**Definition** sd.h:76

[sd\_card::func0](structsd__card.md#a93986ee5db729d9931b4ababe41c303a)

struct sdio\_func func0

Function 0 common card data.

**Definition** sd.h:82

[sd\_card::host\_props](structsd__card.md#a9f597007072d3af5b70ea5cc2a4cbd29)

struct sdhc\_host\_props host\_props

SDHC host properties.

**Definition** sd.h:68

[sd\_card::cccr\_flags](structsd__card.md#ab122e442ab3ba5078c99a98a861ec908)

uint32\_t cccr\_flags

SDIO CCCR data.

**Definition** sd.h:81

[sd\_card::lock](structsd__card.md#aba2501397066d0930691c40778405aa7)

struct k\_mutex lock

card mutex

**Definition** sd.h:67

[sd\_card::block\_count](structsd__card.md#acdcfdaab67d284ef3a8ee3202fd7a538)

uint32\_t block\_count

Number of blocks in SD card.

**Definition** sd.h:73

[sd\_card::flags](structsd__card.md#ad5d6e798ae8b04d829fb8131f6cb1ccf)

uint16\_t flags

Card flags.

**Definition** sd.h:79

[sd\_card::card\_voltage](structsd__card.md#ae8e85d2fc44a97b42247d87a5c2aafdf)

enum sd\_voltage card\_voltage

Card signal voltage.

**Definition** sd.h:66

[sd\_card::sdhc](structsd__card.md#afabeaa207f2f5caaec8cfedac6b35661)

const struct device \* sdhc

SD host controller for card.

**Definition** sd.h:64

[sd\_switch\_caps](structsd__switch__caps.md)

SD switch capabilities.

**Definition** sd\_spec.h:505

[sdhc\_host\_props](structsdhc__host__props.md)

SD host controller properties.

**Definition** sdhc.h:225

[sdhc\_io](structsdhc__io.md)

SD host controller I/O control structure.

**Definition** sdhc.h:210

[sdio\_cis](structsdio__cis.md)

SDIO common CIS tuple properties.

**Definition** sd\_spec.h:918

[sdio\_func](structsdio__func.md)

SDIO function definition.

**Definition** sd.h:48

[sdio\_func::num](structsdio__func.md#a3bc320f1ca7268344b848a998ace615c)

enum sdio\_func\_num num

Function number.

**Definition** sd.h:49

[sdio\_func::card](structsdio__func.md#a7387979362ba892c013a7a69e004d96b)

struct sd\_card \* card

Card this function is present on.

**Definition** sd.h:50

[sdio\_func::block\_size](structsdio__func.md#aa4ad13eb77f656020b38f6cf165e2965)

uint16\_t block\_size

Current block size for this function.

**Definition** sd.h:52

[sdio\_func::cis](structsdio__func.md#af83e71e628841b8acf70130261a97060)

struct sdio\_cis cis

CIS tuple data for this function.

**Definition** sd.h:51

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sd](dir_ff091b3f4b9505cc58dad89321d1c232.md)
- [sd.h](sd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
