---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/wifi__credentials_8h_source.html
original_path: doxygen/html/wifi__credentials_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_credentials.h

[Go to the documentation of this file.](wifi__credentials_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef WIFI\_CREDENTIALS\_H\_\_

8#define WIFI\_CREDENTIALS\_H\_\_

9

10#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

11#include <[zephyr/net/wifi.h](wifi_8h.md)>

12#include <[zephyr/kernel.h](kernel_8h.md)>

13

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

27/\* this entry contains a BSSID \*/

[ 28](group__wifi__credentials.md#ga656bc737cf1bceffc1cf85d06419cec9)#define WIFI\_CREDENTIALS\_FLAG\_BSSID BIT(0)

29/\* this entry is to be preferred over others \*/

[ 30](group__wifi__credentials.md#ga34c10ac642daf7ee05c1b940c01f8932)#define WIFI\_CREDENTIALS\_FLAG\_FAVORITE BIT(1)

31/\* this entry can use the 2.4 GHz band \*/

[ 32](group__wifi__credentials.md#ga179a3abf6a1a44b0bee0d2a9736ece0c)#define WIFI\_CREDENTIALS\_FLAG\_2\_4GHz BIT(2)

33/\* this entry can use the 5 GHz band \*/

[ 34](group__wifi__credentials.md#ga22d0707e4e4d2fd082563f7c1ebf5308)#define WIFI\_CREDENTIALS\_FLAG\_5GHz BIT(3)

35/\* this entry requires management frame protection \*/

[ 36](group__wifi__credentials.md#gab9a8dd24857d6ddb22ae96096a3ee75c)#define WIFI\_CREDENTIALS\_FLAG\_MFP\_REQUIRED BIT(4)

37/\* this entry disables management frame protection \*/

[ 38](group__wifi__credentials.md#ga973e4e6faafa8f8b946d3164b1daf95d)#define WIFI\_CREDENTIALS\_FLAG\_MFP\_DISABLED BIT(5)

39

[ 40](group__wifi__credentials.md#gaf9d3ffe6c9120a7fbc248c3ee66f42fa)#define WIFI\_CREDENTIALS\_MAX\_PASSWORD\_LEN \

41 MAX(WIFI\_PSK\_MAX\_LEN, CONFIG\_WIFI\_CREDENTIALS\_SAE\_PASSWORD\_LENGTH)

42

[ 51](structwifi__credentials__header.md)struct [wifi\_credentials\_header](structwifi__credentials__header.md) {

[ 52](structwifi__credentials__header.md#a5b873555b2154e22367644c2805c0494) enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [type](structwifi__credentials__header.md#a5b873555b2154e22367644c2805c0494);

[ 53](structwifi__credentials__header.md#a172c0a2052146ce1748e7ab4e0aa076f) char [ssid](structwifi__credentials__header.md#a172c0a2052146ce1748e7ab4e0aa076f)[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)];

[ 54](structwifi__credentials__header.md#ab5bfa4ac972a8ad1ba4b395fad48a923) size\_t [ssid\_len](structwifi__credentials__header.md#ab5bfa4ac972a8ad1ba4b395fad48a923);

[ 55](structwifi__credentials__header.md#a59b8b99ad309c0cc2cb6c5438554fefe) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structwifi__credentials__header.md#a59b8b99ad309c0cc2cb6c5438554fefe);

[ 56](structwifi__credentials__header.md#ab6b02e3c88ff13a323cbafdf9af9ba1f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timeout](structwifi__credentials__header.md#ab6b02e3c88ff13a323cbafdf9af9ba1f);

[ 57](structwifi__credentials__header.md#a18d7796039bcdec0ce611a7f2dfe5c63) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bssid](structwifi__credentials__header.md#a18d7796039bcdec0ce611a7f2dfe5c63)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

[ 58](structwifi__credentials__header.md#a9ab939e7cb212a85d2612d5582e2336d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structwifi__credentials__header.md#a9ab939e7cb212a85d2612d5582e2336d);

59};

60

[ 69](structwifi__credentials__personal.md)struct [wifi\_credentials\_personal](structwifi__credentials__personal.md) {

[ 70](structwifi__credentials__personal.md#a40f13f70ee0dd797d31b643cc754440c) struct [wifi\_credentials\_header](structwifi__credentials__header.md) [header](structwifi__credentials__personal.md#a40f13f70ee0dd797d31b643cc754440c);

[ 71](structwifi__credentials__personal.md#ae9ed5b123e0467054e6e18831c2b29c5) char [password](structwifi__credentials__personal.md#ae9ed5b123e0467054e6e18831c2b29c5)[[WIFI\_CREDENTIALS\_MAX\_PASSWORD\_LEN](group__wifi__credentials.md#gaf9d3ffe6c9120a7fbc248c3ee66f42fa)];

[ 72](structwifi__credentials__personal.md#a627104585a2f6d58e2f899563c2993ad) size\_t [password\_len](structwifi__credentials__personal.md#a627104585a2f6d58e2f899563c2993ad);

73};

74

[ 79](structwifi__credentials__enterprise.md)struct [wifi\_credentials\_enterprise](structwifi__credentials__enterprise.md) {

[ 80](structwifi__credentials__enterprise.md#a58ba430cb51a80009639263ebe412895) struct [wifi\_credentials\_header](structwifi__credentials__header.md) [header](structwifi__credentials__enterprise.md#a58ba430cb51a80009639263ebe412895);

[ 81](structwifi__credentials__enterprise.md#aadd1fe1f5d3f3983a5cd82d5d33a4ff4) size\_t [identity\_len](structwifi__credentials__enterprise.md#aadd1fe1f5d3f3983a5cd82d5d33a4ff4);

[ 82](structwifi__credentials__enterprise.md#a8871721054c824b056fcbb9492bf96aa) size\_t [anonymous\_identity\_len](structwifi__credentials__enterprise.md#a8871721054c824b056fcbb9492bf96aa);

[ 83](structwifi__credentials__enterprise.md#aeb480da7b9b4c7e0f4ab3b86977032f9) size\_t [password\_len](structwifi__credentials__enterprise.md#aeb480da7b9b4c7e0f4ab3b86977032f9);

[ 84](structwifi__credentials__enterprise.md#a74d046dbfdc2f1208848c564c8d98843) size\_t [ca\_cert\_len](structwifi__credentials__enterprise.md#a74d046dbfdc2f1208848c564c8d98843);

[ 85](structwifi__credentials__enterprise.md#a33525f5af6db7813b8f19554fd5c04f0) size\_t [client\_cert\_len](structwifi__credentials__enterprise.md#a33525f5af6db7813b8f19554fd5c04f0);

[ 86](structwifi__credentials__enterprise.md#a757f7cfbaf1874be1300f68bf42ebc9d) size\_t [private\_key\_len](structwifi__credentials__enterprise.md#a757f7cfbaf1874be1300f68bf42ebc9d);

[ 87](structwifi__credentials__enterprise.md#ab532c721b2e10c44bf660d67ca63f994) size\_t [private\_key\_pw\_len](structwifi__credentials__enterprise.md#ab532c721b2e10c44bf660d67ca63f994);

88};

89

[ 110](group__wifi__credentials.md#ga548522fbc6b5fdcff4585c34f3565c82)int [wifi\_credentials\_get\_by\_ssid\_personal](group__wifi__credentials.md#ga548522fbc6b5fdcff4585c34f3565c82)(const char \*[ssid](structwifi__credentials__header.md#a172c0a2052146ce1748e7ab4e0aa076f), size\_t [ssid\_len](structwifi__credentials__header.md#ab5bfa4ac972a8ad1ba4b395fad48a923),

111 enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) \*[type](structwifi__credentials__header.md#a5b873555b2154e22367644c2805c0494), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*bssid\_buf,

112 size\_t bssid\_buf\_len, char \*password\_buf,

113 size\_t password\_buf\_len, size\_t \*password\_len,

114 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[channel](structwifi__credentials__header.md#a9ab939e7cb212a85d2612d5582e2336d), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[timeout](structwifi__credentials__header.md#ab6b02e3c88ff13a323cbafdf9af9ba1f));

115

[ 135](group__wifi__credentials.md#ga28b13d11cca692921252e98788552957)int [wifi\_credentials\_set\_personal](group__wifi__credentials.md#ga28b13d11cca692921252e98788552957)(const char \*[ssid](structwifi__credentials__header.md#a172c0a2052146ce1748e7ab4e0aa076f), size\_t [ssid\_len](structwifi__credentials__header.md#ab5bfa4ac972a8ad1ba4b395fad48a923), enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [type](structwifi__credentials__header.md#a5b873555b2154e22367644c2805c0494),

136 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[bssid](structwifi__credentials__header.md#a18d7796039bcdec0ce611a7f2dfe5c63), size\_t bssid\_len, const char \*password,

137 size\_t password\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structwifi__credentials__header.md#a9ab939e7cb212a85d2612d5582e2336d),

138 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timeout](structwifi__credentials__header.md#ab6b02e3c88ff13a323cbafdf9af9ba1f));

139

[ 152](group__wifi__credentials.md#ga3d83001e713206ec07f94996137537d5)int [wifi\_credentials\_get\_by\_ssid\_personal\_struct](group__wifi__credentials.md#ga3d83001e713206ec07f94996137537d5)(const char \*[ssid](structwifi__credentials__header.md#a172c0a2052146ce1748e7ab4e0aa076f), size\_t [ssid\_len](structwifi__credentials__header.md#ab5bfa4ac972a8ad1ba4b395fad48a923),

153 struct [wifi\_credentials\_personal](structwifi__credentials__personal.md) \*buf);

154

[ 165](group__wifi__credentials.md#ga1b5525c7a6a7ca312236a2c674d94055)int [wifi\_credentials\_set\_personal\_struct](group__wifi__credentials.md#ga1b5525c7a6a7ca312236a2c674d94055)(const struct [wifi\_credentials\_personal](structwifi__credentials__personal.md) \*creds);

166

[ 176](group__wifi__credentials.md#ga644d29db8091512a977f8e27b245975e)int [wifi\_credentials\_delete\_by\_ssid](group__wifi__credentials.md#ga644d29db8091512a977f8e27b245975e)(const char \*[ssid](structwifi__credentials__header.md#a172c0a2052146ce1748e7ab4e0aa076f), size\_t [ssid\_len](structwifi__credentials__header.md#ab5bfa4ac972a8ad1ba4b395fad48a923));

177

[ 183](group__wifi__credentials.md#ga467ef5e15a637c33cb1926a3548ffb9e)bool [wifi\_credentials\_is\_empty](group__wifi__credentials.md#ga467ef5e15a637c33cb1926a3548ffb9e)(void);

184

[ 193](group__wifi__credentials.md#gade76c60899e42fc2af5f7e93143c21ad)int [wifi\_credentials\_delete\_all](group__wifi__credentials.md#gade76c60899e42fc2af5f7e93143c21ad)(void);

194

[ 202](group__wifi__credentials.md#ga30c9333f10e8e8d03f268fb5c9a69562)typedef void (\*[wifi\_credentials\_ssid\_cb](group__wifi__credentials.md#ga30c9333f10e8e8d03f268fb5c9a69562))(void \*cb\_arg, const char \*[ssid](structwifi__credentials__header.md#a172c0a2052146ce1748e7ab4e0aa076f), size\_t [ssid\_len](structwifi__credentials__header.md#ab5bfa4ac972a8ad1ba4b395fad48a923));

203

[ 210](group__wifi__credentials.md#ga3a5b20d07afc52cc452a9c55998ebcf7)void [wifi\_credentials\_for\_each\_ssid](group__wifi__credentials.md#ga3a5b20d07afc52cc452a9c55998ebcf7)([wifi\_credentials\_ssid\_cb](group__wifi__credentials.md#ga30c9333f10e8e8d03f268fb5c9a69562) cb, void \*cb\_arg);

211

212#ifdef \_\_cplusplus

213}

214#endif

215

217

218#endif /\* WIFI\_CREDENTIALS\_H\_\_ \*/

[wifi\_credentials\_set\_personal\_struct](group__wifi__credentials.md#ga1b5525c7a6a7ca312236a2c674d94055)

int wifi\_credentials\_set\_personal\_struct(const struct wifi\_credentials\_personal \*creds)

Set credentials for given SSID by struct.

[wifi\_credentials\_set\_personal](group__wifi__credentials.md#ga28b13d11cca692921252e98788552957)

int wifi\_credentials\_set\_personal(const char \*ssid, size\_t ssid\_len, enum wifi\_security\_type type, const uint8\_t \*bssid, size\_t bssid\_len, const char \*password, size\_t password\_len, uint32\_t flags, uint8\_t channel, uint32\_t timeout)

Set credentials for given SSID.

[wifi\_credentials\_ssid\_cb](group__wifi__credentials.md#ga30c9333f10e8e8d03f268fb5c9a69562)

void(\* wifi\_credentials\_ssid\_cb)(void \*cb\_arg, const char \*ssid, size\_t ssid\_len)

Callback type for wifi\_credentials\_for\_each\_ssid.

**Definition** wifi\_credentials.h:202

[wifi\_credentials\_for\_each\_ssid](group__wifi__credentials.md#ga3a5b20d07afc52cc452a9c55998ebcf7)

void wifi\_credentials\_for\_each\_ssid(wifi\_credentials\_ssid\_cb cb, void \*cb\_arg)

Call callback for each registered SSID.

[wifi\_credentials\_get\_by\_ssid\_personal\_struct](group__wifi__credentials.md#ga3d83001e713206ec07f94996137537d5)

int wifi\_credentials\_get\_by\_ssid\_personal\_struct(const char \*ssid, size\_t ssid\_len, struct wifi\_credentials\_personal \*buf)

Get credentials for given SSID by struct.

[wifi\_credentials\_is\_empty](group__wifi__credentials.md#ga467ef5e15a637c33cb1926a3548ffb9e)

bool wifi\_credentials\_is\_empty(void)

Check if credentials storage is empty.

[wifi\_credentials\_get\_by\_ssid\_personal](group__wifi__credentials.md#ga548522fbc6b5fdcff4585c34f3565c82)

int wifi\_credentials\_get\_by\_ssid\_personal(const char \*ssid, size\_t ssid\_len, enum wifi\_security\_type \*type, uint8\_t \*bssid\_buf, size\_t bssid\_buf\_len, char \*password\_buf, size\_t password\_buf\_len, size\_t \*password\_len, uint32\_t \*flags, uint8\_t \*channel, uint32\_t \*timeout)

Get credentials for given SSID.

[wifi\_credentials\_delete\_by\_ssid](group__wifi__credentials.md#ga644d29db8091512a977f8e27b245975e)

int wifi\_credentials\_delete\_by\_ssid(const char \*ssid, size\_t ssid\_len)

Delete credentials for given SSID.

[wifi\_credentials\_delete\_all](group__wifi__credentials.md#gade76c60899e42fc2af5f7e93143c21ad)

int wifi\_credentials\_delete\_all(void)

Deletes all stored Wi-Fi credentials.

[WIFI\_CREDENTIALS\_MAX\_PASSWORD\_LEN](group__wifi__credentials.md#gaf9d3ffe6c9120a7fbc248c3ee66f42fa)

#define WIFI\_CREDENTIALS\_MAX\_PASSWORD\_LEN

**Definition** wifi\_credentials.h:40

[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)

#define WIFI\_MAC\_ADDR\_LEN

MAC address length.

**Definition** wifi.h:282

[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)

#define WIFI\_SSID\_MAX\_LEN

Max SSID length.

**Definition** wifi.h:274

[wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c)

wifi\_security\_type

IEEE 802.11 security types.

**Definition** wifi.h:42

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[wifi\_credentials\_enterprise](structwifi__credentials__enterprise.md)

Wi-Fi Enterprise credentials entry.

**Definition** wifi\_credentials.h:79

[wifi\_credentials\_enterprise::client\_cert\_len](structwifi__credentials__enterprise.md#a33525f5af6db7813b8f19554fd5c04f0)

size\_t client\_cert\_len

Length of the client certificate.

**Definition** wifi\_credentials.h:85

[wifi\_credentials\_enterprise::header](structwifi__credentials__enterprise.md#a58ba430cb51a80009639263ebe412895)

struct wifi\_credentials\_header header

Header.

**Definition** wifi\_credentials.h:80

[wifi\_credentials\_enterprise::ca\_cert\_len](structwifi__credentials__enterprise.md#a74d046dbfdc2f1208848c564c8d98843)

size\_t ca\_cert\_len

Length of the CA certificate.

**Definition** wifi\_credentials.h:84

[wifi\_credentials\_enterprise::private\_key\_len](structwifi__credentials__enterprise.md#a757f7cfbaf1874be1300f68bf42ebc9d)

size\_t private\_key\_len

Length of the private key.

**Definition** wifi\_credentials.h:86

[wifi\_credentials\_enterprise::anonymous\_identity\_len](structwifi__credentials__enterprise.md#a8871721054c824b056fcbb9492bf96aa)

size\_t anonymous\_identity\_len

Length of the anonymous identity.

**Definition** wifi\_credentials.h:82

[wifi\_credentials\_enterprise::identity\_len](structwifi__credentials__enterprise.md#aadd1fe1f5d3f3983a5cd82d5d33a4ff4)

size\_t identity\_len

Length of the identity.

**Definition** wifi\_credentials.h:81

[wifi\_credentials\_enterprise::private\_key\_pw\_len](structwifi__credentials__enterprise.md#ab532c721b2e10c44bf660d67ca63f994)

size\_t private\_key\_pw\_len

Length of the private key password.

**Definition** wifi\_credentials.h:87

[wifi\_credentials\_enterprise::password\_len](structwifi__credentials__enterprise.md#aeb480da7b9b4c7e0f4ab3b86977032f9)

size\_t password\_len

Length of the password.

**Definition** wifi\_credentials.h:83

[wifi\_credentials\_header](structwifi__credentials__header.md)

Wi-Fi credentials entry header.

**Definition** wifi\_credentials.h:51

[wifi\_credentials\_header::ssid](structwifi__credentials__header.md#a172c0a2052146ce1748e7ab4e0aa076f)

char ssid[32]

SSID (Service Set Identifier).

**Definition** wifi\_credentials.h:53

[wifi\_credentials\_header::bssid](structwifi__credentials__header.md#a18d7796039bcdec0ce611a7f2dfe5c63)

uint8\_t bssid[6]

BSSID (Basic Service Set Identifier).

**Definition** wifi\_credentials.h:57

[wifi\_credentials\_header::flags](structwifi__credentials__header.md#a59b8b99ad309c0cc2cb6c5438554fefe)

uint32\_t flags

Flags for controlling detail settings.

**Definition** wifi\_credentials.h:55

[wifi\_credentials\_header::type](structwifi__credentials__header.md#a5b873555b2154e22367644c2805c0494)

enum wifi\_security\_type type

Wi-Fi security type.

**Definition** wifi\_credentials.h:52

[wifi\_credentials\_header::channel](structwifi__credentials__header.md#a9ab939e7cb212a85d2612d5582e2336d)

uint8\_t channel

Channel on which the network operates.

**Definition** wifi\_credentials.h:58

[wifi\_credentials\_header::ssid\_len](structwifi__credentials__header.md#ab5bfa4ac972a8ad1ba4b395fad48a923)

size\_t ssid\_len

Length of the SSID.

**Definition** wifi\_credentials.h:54

[wifi\_credentials\_header::timeout](structwifi__credentials__header.md#ab6b02e3c88ff13a323cbafdf9af9ba1f)

uint32\_t timeout

Timeout for connecting to the network.

**Definition** wifi\_credentials.h:56

[wifi\_credentials\_personal](structwifi__credentials__personal.md)

Wi-Fi Personal credentials entry.

**Definition** wifi\_credentials.h:69

[wifi\_credentials\_personal::header](structwifi__credentials__personal.md#a40f13f70ee0dd797d31b643cc754440c)

struct wifi\_credentials\_header header

Header.

**Definition** wifi\_credentials.h:70

[wifi\_credentials\_personal::password\_len](structwifi__credentials__personal.md#a627104585a2f6d58e2f899563c2993ad)

size\_t password\_len

Length of the password.

**Definition** wifi\_credentials.h:72

[wifi\_credentials\_personal::password](structwifi__credentials__personal.md#ae9ed5b123e0467054e6e18831c2b29c5)

char password[MAX(64, CONFIG\_WIFI\_CREDENTIALS\_SAE\_PASSWORD\_LENGTH)]

Password/PSK.

**Definition** wifi\_credentials.h:71

[wifi.h](wifi_8h.md)

IEEE 802.11 protocol and general Wi-Fi definitions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [wifi\_credentials.h](wifi__credentials_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
