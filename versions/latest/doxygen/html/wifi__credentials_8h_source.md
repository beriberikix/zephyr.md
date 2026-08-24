---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/wifi__credentials_8h_source.html
original_path: doxygen/html/wifi__credentials_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

26

27

28/\* this entry contains a BSSID \*/

[ 29](group__wifi__credentials.md#ga656bc737cf1bceffc1cf85d06419cec9)#define WIFI\_CREDENTIALS\_FLAG\_BSSID BIT(0)

30/\* this entry is to be preferred over others \*/

[ 31](group__wifi__credentials.md#ga34c10ac642daf7ee05c1b940c01f8932)#define WIFI\_CREDENTIALS\_FLAG\_FAVORITE BIT(1)

32/\* this entry can use the 2.4 GHz band \*/

[ 33](group__wifi__credentials.md#ga179a3abf6a1a44b0bee0d2a9736ece0c)#define WIFI\_CREDENTIALS\_FLAG\_2\_4GHz BIT(2)

34/\* this entry can use the 5 GHz band \*/

[ 35](group__wifi__credentials.md#ga22d0707e4e4d2fd082563f7c1ebf5308)#define WIFI\_CREDENTIALS\_FLAG\_5GHz BIT(3)

36/\* this entry can use the 6 GHz band \*/

[ 37](group__wifi__credentials.md#ga50b7c4fd09530f93a7632a03a9a12604)#define WIFI\_CREDENTIALS\_FLAG\_6GHz BIT(4)

38/\* this entry requires management frame protection \*/

[ 39](group__wifi__credentials.md#gab9a8dd24857d6ddb22ae96096a3ee75c)#define WIFI\_CREDENTIALS\_FLAG\_MFP\_REQUIRED BIT(5)

40/\* this entry disables management frame protection \*/

[ 41](group__wifi__credentials.md#ga973e4e6faafa8f8b946d3164b1daf95d)#define WIFI\_CREDENTIALS\_FLAG\_MFP\_DISABLED BIT(6)

42/\* this entry has anonymous identity configured \*/

[ 43](group__wifi__credentials.md#gab7024a46e99dc304dd4741c45b13c846)#define WIFI\_CREDENTIALS\_FLAG\_ANONYMOUS\_IDENTITY BIT(7)

44/\* this entry has key password configured \*/

[ 45](group__wifi__credentials.md#ga9a411a277da97426aa190a8f911a4042)#define WIFI\_CREDENTIALS\_FLAG\_KEY\_PASSWORD BIT(8)

46

47/\* Maximum length of the password \*/

[ 48](group__wifi__credentials.md#gaf9d3ffe6c9120a7fbc248c3ee66f42fa)#define WIFI\_CREDENTIALS\_MAX\_PASSWORD\_LEN \

49 MAX(WIFI\_PSK\_MAX\_LEN, CONFIG\_WIFI\_CREDENTIALS\_SAE\_PASSWORD\_LENGTH)

50

[ 59](structwifi__credentials__header.md)struct [wifi\_credentials\_header](structwifi__credentials__header.md) {

[ 61](structwifi__credentials__header.md#a5b873555b2154e22367644c2805c0494) enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [type](structwifi__credentials__header.md#a5b873555b2154e22367644c2805c0494);

62

[ 64](structwifi__credentials__header.md#a172c0a2052146ce1748e7ab4e0aa076f) char [ssid](structwifi__credentials__header.md#a172c0a2052146ce1748e7ab4e0aa076f)[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)];

65

[ 67](structwifi__credentials__header.md#ab5bfa4ac972a8ad1ba4b395fad48a923) size\_t [ssid\_len](structwifi__credentials__header.md#ab5bfa4ac972a8ad1ba4b395fad48a923);

68

[ 70](structwifi__credentials__header.md#a59b8b99ad309c0cc2cb6c5438554fefe) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structwifi__credentials__header.md#a59b8b99ad309c0cc2cb6c5438554fefe);

71

[ 73](structwifi__credentials__header.md#ab6b02e3c88ff13a323cbafdf9af9ba1f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timeout](structwifi__credentials__header.md#ab6b02e3c88ff13a323cbafdf9af9ba1f);

74

[ 76](structwifi__credentials__header.md#a18d7796039bcdec0ce611a7f2dfe5c63) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bssid](structwifi__credentials__header.md#a18d7796039bcdec0ce611a7f2dfe5c63)[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)];

77

[ 79](structwifi__credentials__header.md#a9ab939e7cb212a85d2612d5582e2336d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structwifi__credentials__header.md#a9ab939e7cb212a85d2612d5582e2336d);

80

[ 82](structwifi__credentials__header.md#acbbd421fda51f23d2243dd9573b05d71) char [anon\_id](structwifi__credentials__header.md#acbbd421fda51f23d2243dd9573b05d71)[16];

83

[ 85](structwifi__credentials__header.md#a2c39cdc6f7023560de61fb353a178369) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [aid\_length](structwifi__credentials__header.md#a2c39cdc6f7023560de61fb353a178369);

86

[ 88](structwifi__credentials__header.md#a99ccc993d609632f42650aabe9fc861b) char [key\_passwd](structwifi__credentials__header.md#a99ccc993d609632f42650aabe9fc861b)[16];

89

[ 91](structwifi__credentials__header.md#a605b62d473586f3d8312aa1c80731ee6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key\_passwd\_length](structwifi__credentials__header.md#a605b62d473586f3d8312aa1c80731ee6);

92};

93

[ 102](structwifi__credentials__personal.md)struct [wifi\_credentials\_personal](structwifi__credentials__personal.md) {

[ 104](structwifi__credentials__personal.md#a40f13f70ee0dd797d31b643cc754440c) struct [wifi\_credentials\_header](structwifi__credentials__header.md) [header](structwifi__credentials__personal.md#a40f13f70ee0dd797d31b643cc754440c);

105

[ 107](structwifi__credentials__personal.md#ae9ed5b123e0467054e6e18831c2b29c5) char [password](structwifi__credentials__personal.md#ae9ed5b123e0467054e6e18831c2b29c5)[[WIFI\_CREDENTIALS\_MAX\_PASSWORD\_LEN](group__wifi__credentials.md#gaf9d3ffe6c9120a7fbc248c3ee66f42fa)];

108

[ 110](structwifi__credentials__personal.md#a627104585a2f6d58e2f899563c2993ad) size\_t [password\_len](structwifi__credentials__personal.md#a627104585a2f6d58e2f899563c2993ad);

111};

112

[ 117](structwifi__credentials__enterprise.md)struct [wifi\_credentials\_enterprise](structwifi__credentials__enterprise.md) {

[ 119](structwifi__credentials__enterprise.md#a58ba430cb51a80009639263ebe412895) struct [wifi\_credentials\_header](structwifi__credentials__header.md) [header](structwifi__credentials__enterprise.md#a58ba430cb51a80009639263ebe412895);

120

[ 122](structwifi__credentials__enterprise.md#aadd1fe1f5d3f3983a5cd82d5d33a4ff4) size\_t [identity\_len](structwifi__credentials__enterprise.md#aadd1fe1f5d3f3983a5cd82d5d33a4ff4);

123

[ 125](structwifi__credentials__enterprise.md#a8871721054c824b056fcbb9492bf96aa) size\_t [anonymous\_identity\_len](structwifi__credentials__enterprise.md#a8871721054c824b056fcbb9492bf96aa);

126

[ 128](structwifi__credentials__enterprise.md#aeb480da7b9b4c7e0f4ab3b86977032f9) size\_t [password\_len](structwifi__credentials__enterprise.md#aeb480da7b9b4c7e0f4ab3b86977032f9);

129

[ 131](structwifi__credentials__enterprise.md#a74d046dbfdc2f1208848c564c8d98843) size\_t [ca\_cert\_len](structwifi__credentials__enterprise.md#a74d046dbfdc2f1208848c564c8d98843);

132

[ 134](structwifi__credentials__enterprise.md#a33525f5af6db7813b8f19554fd5c04f0) size\_t [client\_cert\_len](structwifi__credentials__enterprise.md#a33525f5af6db7813b8f19554fd5c04f0);

135

[ 137](structwifi__credentials__enterprise.md#a757f7cfbaf1874be1300f68bf42ebc9d) size\_t [private\_key\_len](structwifi__credentials__enterprise.md#a757f7cfbaf1874be1300f68bf42ebc9d);

138

[ 140](structwifi__credentials__enterprise.md#ab532c721b2e10c44bf660d67ca63f994) size\_t [private\_key\_pw\_len](structwifi__credentials__enterprise.md#ab532c721b2e10c44bf660d67ca63f994);

141};

142

[ 163](group__wifi__credentials.md#ga548522fbc6b5fdcff4585c34f3565c82)int [wifi\_credentials\_get\_by\_ssid\_personal](group__wifi__credentials.md#ga548522fbc6b5fdcff4585c34f3565c82)(const char \*[ssid](structwifi__credentials__header.md#a172c0a2052146ce1748e7ab4e0aa076f), size\_t [ssid\_len](structwifi__credentials__header.md#ab5bfa4ac972a8ad1ba4b395fad48a923),

164 enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) \*[type](structwifi__credentials__header.md#a5b873555b2154e22367644c2805c0494), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*bssid\_buf,

165 size\_t bssid\_buf\_len, char \*password\_buf,

166 size\_t password\_buf\_len, size\_t \*password\_len,

167 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[channel](structwifi__credentials__header.md#a9ab939e7cb212a85d2612d5582e2336d), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[timeout](structwifi__credentials__header.md#ab6b02e3c88ff13a323cbafdf9af9ba1f));

168

[ 188](group__wifi__credentials.md#ga28b13d11cca692921252e98788552957)int [wifi\_credentials\_set\_personal](group__wifi__credentials.md#ga28b13d11cca692921252e98788552957)(const char \*[ssid](structwifi__credentials__header.md#a172c0a2052146ce1748e7ab4e0aa076f), size\_t [ssid\_len](structwifi__credentials__header.md#ab5bfa4ac972a8ad1ba4b395fad48a923), enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [type](structwifi__credentials__header.md#a5b873555b2154e22367644c2805c0494),

189 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[bssid](structwifi__credentials__header.md#a18d7796039bcdec0ce611a7f2dfe5c63), size\_t bssid\_len, const char \*password,

190 size\_t password\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structwifi__credentials__header.md#a9ab939e7cb212a85d2612d5582e2336d),

191 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timeout](structwifi__credentials__header.md#ab6b02e3c88ff13a323cbafdf9af9ba1f));

192

[ 205](group__wifi__credentials.md#ga3d83001e713206ec07f94996137537d5)int [wifi\_credentials\_get\_by\_ssid\_personal\_struct](group__wifi__credentials.md#ga3d83001e713206ec07f94996137537d5)(const char \*[ssid](structwifi__credentials__header.md#a172c0a2052146ce1748e7ab4e0aa076f), size\_t [ssid\_len](structwifi__credentials__header.md#ab5bfa4ac972a8ad1ba4b395fad48a923),

206 struct [wifi\_credentials\_personal](structwifi__credentials__personal.md) \*buf);

207

[ 218](group__wifi__credentials.md#ga1b5525c7a6a7ca312236a2c674d94055)int [wifi\_credentials\_set\_personal\_struct](group__wifi__credentials.md#ga1b5525c7a6a7ca312236a2c674d94055)(const struct [wifi\_credentials\_personal](structwifi__credentials__personal.md) \*creds);

219

[ 229](group__wifi__credentials.md#ga644d29db8091512a977f8e27b245975e)int [wifi\_credentials\_delete\_by\_ssid](group__wifi__credentials.md#ga644d29db8091512a977f8e27b245975e)(const char \*[ssid](structwifi__credentials__header.md#a172c0a2052146ce1748e7ab4e0aa076f), size\_t [ssid\_len](structwifi__credentials__header.md#ab5bfa4ac972a8ad1ba4b395fad48a923));

230

[ 236](group__wifi__credentials.md#ga467ef5e15a637c33cb1926a3548ffb9e)bool [wifi\_credentials\_is\_empty](group__wifi__credentials.md#ga467ef5e15a637c33cb1926a3548ffb9e)(void);

237

[ 246](group__wifi__credentials.md#gade76c60899e42fc2af5f7e93143c21ad)int [wifi\_credentials\_delete\_all](group__wifi__credentials.md#gade76c60899e42fc2af5f7e93143c21ad)(void);

247

[ 256](group__wifi__credentials.md#ga30c9333f10e8e8d03f268fb5c9a69562)typedef void (\*[wifi\_credentials\_ssid\_cb](group__wifi__credentials.md#ga30c9333f10e8e8d03f268fb5c9a69562))(void \*cb\_arg, const char \*[ssid](structwifi__credentials__header.md#a172c0a2052146ce1748e7ab4e0aa076f), size\_t [ssid\_len](structwifi__credentials__header.md#ab5bfa4ac972a8ad1ba4b395fad48a923));

257

[ 264](group__wifi__credentials.md#ga3a5b20d07afc52cc452a9c55998ebcf7)void [wifi\_credentials\_for\_each\_ssid](group__wifi__credentials.md#ga3a5b20d07afc52cc452a9c55998ebcf7)([wifi\_credentials\_ssid\_cb](group__wifi__credentials.md#ga30c9333f10e8e8d03f268fb5c9a69562) cb, void \*cb\_arg);

265

266#ifdef \_\_cplusplus

267}

268#endif

269

271

272#endif /\* WIFI\_CREDENTIALS\_H\_\_ \*/

[wifi\_credentials\_set\_personal\_struct](group__wifi__credentials.md#ga1b5525c7a6a7ca312236a2c674d94055)

int wifi\_credentials\_set\_personal\_struct(const struct wifi\_credentials\_personal \*creds)

Set credentials for given SSID by struct.

[wifi\_credentials\_set\_personal](group__wifi__credentials.md#ga28b13d11cca692921252e98788552957)

int wifi\_credentials\_set\_personal(const char \*ssid, size\_t ssid\_len, enum wifi\_security\_type type, const uint8\_t \*bssid, size\_t bssid\_len, const char \*password, size\_t password\_len, uint32\_t flags, uint8\_t channel, uint32\_t timeout)

Set credentials for given SSID.

[wifi\_credentials\_ssid\_cb](group__wifi__credentials.md#ga30c9333f10e8e8d03f268fb5c9a69562)

void(\* wifi\_credentials\_ssid\_cb)(void \*cb\_arg, const char \*ssid, size\_t ssid\_len)

Callback type for wifi\_credentials\_for\_each\_ssid.

**Definition** wifi\_credentials.h:256

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

**Definition** wifi\_credentials.h:48

[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)

#define WIFI\_MAC\_ADDR\_LEN

MAC address length.

**Definition** wifi.h:309

[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)

#define WIFI\_SSID\_MAX\_LEN

Max SSID length.

**Definition** wifi.h:301

[wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c)

wifi\_security\_type

IEEE 802.11 security types.

**Definition** wifi.h:69

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

**Definition** wifi\_credentials.h:117

[wifi\_credentials\_enterprise::client\_cert\_len](structwifi__credentials__enterprise.md#a33525f5af6db7813b8f19554fd5c04f0)

size\_t client\_cert\_len

Length of the client certificate.

**Definition** wifi\_credentials.h:134

[wifi\_credentials\_enterprise::header](structwifi__credentials__enterprise.md#a58ba430cb51a80009639263ebe412895)

struct wifi\_credentials\_header header

Header.

**Definition** wifi\_credentials.h:119

[wifi\_credentials\_enterprise::ca\_cert\_len](structwifi__credentials__enterprise.md#a74d046dbfdc2f1208848c564c8d98843)

size\_t ca\_cert\_len

Length of the CA certificate.

**Definition** wifi\_credentials.h:131

[wifi\_credentials\_enterprise::private\_key\_len](structwifi__credentials__enterprise.md#a757f7cfbaf1874be1300f68bf42ebc9d)

size\_t private\_key\_len

Length of the private key.

**Definition** wifi\_credentials.h:137

[wifi\_credentials\_enterprise::anonymous\_identity\_len](structwifi__credentials__enterprise.md#a8871721054c824b056fcbb9492bf96aa)

size\_t anonymous\_identity\_len

Length of the anonymous identity.

**Definition** wifi\_credentials.h:125

[wifi\_credentials\_enterprise::identity\_len](structwifi__credentials__enterprise.md#aadd1fe1f5d3f3983a5cd82d5d33a4ff4)

size\_t identity\_len

Length of the identity.

**Definition** wifi\_credentials.h:122

[wifi\_credentials\_enterprise::private\_key\_pw\_len](structwifi__credentials__enterprise.md#ab532c721b2e10c44bf660d67ca63f994)

size\_t private\_key\_pw\_len

Length of the private key password.

**Definition** wifi\_credentials.h:140

[wifi\_credentials\_enterprise::password\_len](structwifi__credentials__enterprise.md#aeb480da7b9b4c7e0f4ab3b86977032f9)

size\_t password\_len

Length of the password.

**Definition** wifi\_credentials.h:128

[wifi\_credentials\_header](structwifi__credentials__header.md)

Wi-Fi credentials entry header.

**Definition** wifi\_credentials.h:59

[wifi\_credentials\_header::ssid](structwifi__credentials__header.md#a172c0a2052146ce1748e7ab4e0aa076f)

char ssid[32]

SSID (Service Set Identifier).

**Definition** wifi\_credentials.h:64

[wifi\_credentials\_header::bssid](structwifi__credentials__header.md#a18d7796039bcdec0ce611a7f2dfe5c63)

uint8\_t bssid[6]

BSSID (Basic Service Set Identifier).

**Definition** wifi\_credentials.h:76

[wifi\_credentials\_header::aid\_length](structwifi__credentials__header.md#a2c39cdc6f7023560de61fb353a178369)

uint8\_t aid\_length

Length of the Anonymous identifier.

**Definition** wifi\_credentials.h:85

[wifi\_credentials\_header::flags](structwifi__credentials__header.md#a59b8b99ad309c0cc2cb6c5438554fefe)

uint32\_t flags

Flags for controlling detail settings.

**Definition** wifi\_credentials.h:70

[wifi\_credentials\_header::type](structwifi__credentials__header.md#a5b873555b2154e22367644c2805c0494)

enum wifi\_security\_type type

Wi-Fi security type.

**Definition** wifi\_credentials.h:61

[wifi\_credentials\_header::key\_passwd\_length](structwifi__credentials__header.md#a605b62d473586f3d8312aa1c80731ee6)

uint8\_t key\_passwd\_length

Length of the Password.

**Definition** wifi\_credentials.h:91

[wifi\_credentials\_header::key\_passwd](structwifi__credentials__header.md#a99ccc993d609632f42650aabe9fc861b)

char key\_passwd[16]

Password/PSK (Limited to 16 bytes due to settings subsystem overflow).

**Definition** wifi\_credentials.h:88

[wifi\_credentials\_header::channel](structwifi__credentials__header.md#a9ab939e7cb212a85d2612d5582e2336d)

uint8\_t channel

Channel on which the network operates.

**Definition** wifi\_credentials.h:79

[wifi\_credentials\_header::ssid\_len](structwifi__credentials__header.md#ab5bfa4ac972a8ad1ba4b395fad48a923)

size\_t ssid\_len

Length of the SSID.

**Definition** wifi\_credentials.h:67

[wifi\_credentials\_header::timeout](structwifi__credentials__header.md#ab6b02e3c88ff13a323cbafdf9af9ba1f)

uint32\_t timeout

Timeout for connecting to the network.

**Definition** wifi\_credentials.h:73

[wifi\_credentials\_header::anon\_id](structwifi__credentials__header.md#acbbd421fda51f23d2243dd9573b05d71)

char anon\_id[16]

Anonymous identifier (Limited to 16 bytes due to settings subsystem overflow).

**Definition** wifi\_credentials.h:82

[wifi\_credentials\_personal](structwifi__credentials__personal.md)

Wi-Fi Personal credentials entry.

**Definition** wifi\_credentials.h:102

[wifi\_credentials\_personal::header](structwifi__credentials__personal.md#a40f13f70ee0dd797d31b643cc754440c)

struct wifi\_credentials\_header header

Header.

**Definition** wifi\_credentials.h:104

[wifi\_credentials\_personal::password\_len](structwifi__credentials__personal.md#a627104585a2f6d58e2f899563c2993ad)

size\_t password\_len

Length of the password.

**Definition** wifi\_credentials.h:110

[wifi\_credentials\_personal::password](structwifi__credentials__personal.md#ae9ed5b123e0467054e6e18831c2b29c5)

char password[MAX(64, CONFIG\_WIFI\_CREDENTIALS\_SAE\_PASSWORD\_LENGTH)]

Password/PSK.

**Definition** wifi\_credentials.h:107

[wifi.h](wifi_8h.md)

IEEE 802.11 protocol and general Wi-Fi definitions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [wifi\_credentials.h](wifi__credentials_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
