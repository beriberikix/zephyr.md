---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/tisci_8h.html
original_path: doxygen/html/tisci_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tisci.h File Reference

Public APIs for the TISCI driver.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](tisci_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [tisci\_version\_info](structtisci__version__info.md) |
|  | version information structure [More...](structtisci__version__info.md#details) |
| struct | [tisci\_msg\_fwl\_region](structtisci__msg__fwl__region.md) |
| struct | [tisci\_msg\_fwl\_owner](structtisci__msg__fwl__owner.md) |
|  | Request and Response for firewall owner change. [More...](structtisci__msg__fwl__owner.md#details) |
| struct | [tisci\_msg\_rm\_udmap\_tx\_ch\_cfg](structtisci__msg__rm__udmap__tx__ch__cfg.md) |
|  | Configures a Navigator Subsystem UDMAP transmit channel. [More...](structtisci__msg__rm__udmap__tx__ch__cfg.md#details) |
| struct | [tisci\_msg\_rm\_udmap\_rx\_ch\_cfg](structtisci__msg__rm__udmap__rx__ch__cfg.md) |
|  | Configures a Navigator Subsystem UDMAP receive channel. [More...](structtisci__msg__rm__udmap__rx__ch__cfg.md#details) |
| struct | [tisci\_irq\_set\_req](structtisci__irq__set__req.md) |
|  | Request to set up an interrupt route. [More...](structtisci__irq__set__req.md#details) |
| struct | [tisci\_irq\_release\_req](structtisci__irq__release__req.md) |
|  | Request to release interrupt peripheral resources. [More...](structtisci__irq__release__req.md#details) |

| Macros | |
| --- | --- |
| #define | [MAILBOX\_MBOX\_SIZE](#a396f8869a1aee7aa1b88a039a17746bf)   60 |
| #define | [TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_FILT\_EINFO\_VALID](#a736e0c626ee9d1df858ce5936bf4029e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| #define | [TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_FILT\_PSWORDS\_VALID](#a6db1d6169cc2def41e73ce4c22fa118e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| #define | [TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_SUPR\_TDPKT\_VALID](#a64195889325d54d493923b95620b1550)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| #define | [TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_CREDIT\_COUNT\_VALID](#a1110504d079ae51a526ed80144560b27)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| #define | [TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_FDEPTH\_VALID](#af8dbd5c7af94ec3690012458d35f2456)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| #define | [TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_TDTYPE\_VALID](#a4de2b535f4d2548218dde6c2dddc9448)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| #define | [TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_EXTENDED\_CH\_TYPE\_VALID](#abb692a88d05498a4c0dd5e69857cda92)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) |
| #define | [TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_RX\_FLOWID\_START\_VALID](#ae0c03a2c76f884f37f472b081d0dd028)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| #define | [TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_RX\_FLOWID\_CNT\_VALID](#a04febde272953c690f94d44db18663f7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| #define | [TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_RX\_IGNORE\_SHORT\_VALID](#a512091ff6dff198c2801a8f51fe18755)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| #define | [TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_RX\_IGNORE\_LONG\_VALID](#a818ed2617f42b219d3e3aed2a46ed7d8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| #define | [TISCI\_MSG\_VALUE\_RM\_DST\_ID\_VALID](#ae309074218959da90a5978304c34e916)   (1u << 0u) |
| #define | [TISCI\_MSG\_VALUE\_RM\_DST\_HOST\_IRQ\_VALID](#a69aa4a4b3a5e99a86adbc6a0ccf74560)   (1u << 1u) |
| #define | [TISCI\_MSG\_VALUE\_RM\_IA\_ID\_VALID](#abf34b43187cdc7ea4b68ee151816d97a)   (1u << 2u) |
| #define | [TISCI\_MSG\_VALUE\_RM\_VINT\_VALID](#a334a7f7a6fd37286c5635f1cfe2d061f)   (1u << 3u) |
| #define | [TISCI\_MSG\_VALUE\_RM\_GLOBAL\_EVENT\_VALID](#aad5b430c5924f794b35cfb7c9830b48b)   (1u << 4u) |
| #define | [TISCI\_MSG\_VALUE\_RM\_VINT\_STATUS\_BIT\_INDEX\_VALID](#ae2c0b651fc864d6904bfef4fdacb2aea)   (1u << 5u) |

| Functions | |
| --- | --- |
| int | [tisci\_cmd\_get\_revision](#aea0b9addbd3cfcb2be691f0801128fe1) (const struct [device](structdevice.md) \*dev, struct [tisci\_version\_info](structtisci__version__info.md) \*ver) |
|  | Get the revision information of the TI SCI firmware. |
| int | [tisci\_cmd\_get\_clock\_state](#a3f8128fa6c8c6f10bb7e302e6e9cfeaf) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*programmed\_state, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*current\_state) |
|  | Get the state of a clock. |
| int | [tisci\_set\_clock\_state](#a086d96bed3d789bf303f56405a791aa6) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Set the state of a clock. |
| int | [tisci\_cmd\_clk\_is\_on](#a7f0bafa6005d46d2786db590a27add25) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*req\_state, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*curr\_state) |
|  | Check if the clock is ON. |
| int | [tisci\_cmd\_clk\_is\_off](#a20276a83e2037db6895085770353a194) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*req\_state, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*curr\_state) |
|  | Check if the clock is OFF. |
| int | [tisci\_cmd\_clk\_is\_auto](#aaebb0012c291ded1b9303d634b1bb245) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*req\_state) |
|  | Check if the clock is being auto-managed. |
| int | [tisci\_cmd\_clk\_get\_freq](#a5c69f5f12b79a0b37a1f704624106960) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*freq) |
|  | Get the current frequency of a clock. |
| int | [tisci\_cmd\_clk\_set\_freq](#ad3563b7ec2fa13eb4b1faa564062ae12) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) min\_freq, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) target\_freq, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) max\_freq) |
|  | Set a frequency for a clock. |
| int | [tisci\_cmd\_clk\_get\_match\_freq](#a9801b388e5dc60f10aa624040cb8bfe2) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) min\_freq, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) target\_freq, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) max\_freq, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*match\_freq) |
|  | Get a matching frequency for a clock. |
| int | [tisci\_cmd\_clk\_set\_parent](#a6ad9804cf3e23246955bcab1e98aecdb) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) parent\_id) |
|  | Set the parent clock for a clock. |
| int | [tisci\_cmd\_clk\_get\_parent](#a86e0ed2c8711363dc5ea710b12a303af) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*parent\_id) |
|  | Get the parent clock for a clock. |
| int | [tisci\_cmd\_clk\_get\_num\_parents](#ae93fb7c70a4f2299415a51b993d36741) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*num\_parents) |
|  | Get the number of parent clocks for a clock. |
| int | [tisci\_cmd\_get\_clock](#ab63106de04e579ba18f34763b3efa8b3) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) needs\_ssc, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) can\_change\_freq, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable\_input\_term) |
|  | Get control of a clock from TI SCI. |
| int | [tisci\_cmd\_idle\_clock](#a3d39780a18358066ec8f187474c18f71) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id) |
|  | Idle a clock that is under control of TI SCI. |
| int | [tisci\_cmd\_put\_clock](#ae48c6c78db3f4bee6520c0af66e37e7d) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) clk\_id) |
|  | Release a clock from control back to TI SCI. |
| int | [tisci\_set\_device\_state](#a8b6d6f99df32eeba9131ce130ee4f12d) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Set the state of a device. |
| int | [tisci\_set\_device\_state\_no\_wait](#a05f871388f68d9c71620ea43bde1e3ab) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Set the state of a device without waiting for a response. |
| int | [tisci\_get\_device\_state](#ada78c57b3cb24e57a3f6cc155e3a3d09) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*clcnt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*resets, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*p\_state, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*c\_state) |
|  | Get the state of a device. |
| int | [tisci\_cmd\_get\_device](#a4011bbe29370fb581ab2dd0fcaa151db) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id) |
|  | Request exclusive access to a device managed by TISCI. |
| int | [tisci\_cmd\_get\_device\_exclusive](#adc16227f1ec150d0c6cf32442fa3e915) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id) |
| int | [tisci\_cmd\_idle\_device](#ab8203c5d0b699ec726a889e7027ae034) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id) |
|  | Command to idle a device managed by TISCI. |
| int | [tisci\_cmd\_idle\_device\_exclusive](#aab1720913f75a771e041e2195b9deede) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id) |
| int | [tisci\_cmd\_put\_device](#a5a7c9ff34ad1ffa87c62fef6b2ac8719) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id) |
|  | Command to release a device managed by TISCI. |
| int | [tisci\_cmd\_dev\_is\_valid](#a4f4072f951c0ebbeb75e8cd2f06b6e8f) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id) |
|  | Check if a device ID is valid. |
| int | [tisci\_cmd\_dev\_get\_clcnt](#a01393f21cb5a88388ce51e36ba1843fc) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*count) |
|  | Get the context loss counter for a device. |
| int | [tisci\_cmd\_dev\_is\_idle](#af9ff6eee5bca675c50c28fbc4af3048c) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*r\_state) |
|  | Check if the device is requested to be idle. |
| int | [tisci\_cmd\_dev\_is\_stop](#a1a441bdad9bfef9a0136f0b737c9c7aa) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*r\_state, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*curr\_state) |
|  | Check if the device is requested to be stopped. |
| int | [tisci\_cmd\_dev\_is\_on](#aa7bb463be840666d87a68c1e65496b19) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*r\_state, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*curr\_state) |
|  | Check if the device is requested to be ON. |
| int | [tisci\_cmd\_dev\_is\_trans](#a4a3b7acb3098f71b2a9f85fbb318d595) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*curr\_state) |
|  | Check if the device is currently transitioning. |
| int | [tisci\_cmd\_set\_device\_resets](#a94f43ead8c81320f651fa9c0450a2493) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reset\_state) |
|  | Set resets for a device managed by TISCI. |
| int | [tisci\_cmd\_get\_device\_resets](#a90613df222309651abc1adb2f4d82272) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*reset\_state) |
|  | Get reset state for a device managed by TISCI. |
| int | [tisci\_get\_resource\_range](#a8ced32499c14aae81994368d4450422d) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subtype, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) s\_host, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*range\_start, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*range\_num) |
|  | Get a range of resources assigned to a host. |
| int | [tisci\_cmd\_get\_resource\_range](#ae249d114c60b6b1a76f7de8dab5c3ce1) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subtype, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*range\_start, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*range\_num) |
|  | Get a range of resources assigned to the host. |
| int | [tisci\_cmd\_get\_resource\_range\_from\_shost](#aa261b08c9141360c5f4f9e50ab151ed5) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subtype, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) s\_host, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*range\_start, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*range\_num) |
|  | Get a range of resources assigned to a specified host. |
| int | [tisci\_cmd\_proc\_request](#a3181b68860761b0060048a01d71888a8) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proc\_id) |
|  | Command to request a physical processor control. |
| int | [tisci\_cmd\_proc\_release](#a2e0e3e88c635a4e6399941696056b8a9) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proc\_id) |
|  | Command to release a physical processor control. |
| int | [tisci\_cmd\_proc\_handover](#a1acfab0f8fd3b1db050f97aa21d26ce3) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proc\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) host\_id) |
|  | Command to handover a physical processor control to a host in the processor's access control list. |
| int | [tisci\_cmd\_set\_proc\_boot\_cfg](#a3551276e98c3f03ea4beb9086c3b89c3) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proc\_id, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) bootvector, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) config\_flags\_set, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) config\_flags\_clear) |
|  | Command to set the processor boot configuration flags. |
| int | [tisci\_cmd\_set\_proc\_boot\_ctrl](#aee60c2eb75e6786b91d9dc73c7a7e2c6) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proc\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) control\_flags\_set, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) control\_flags\_clear) |
|  | Command to set the processor boot control flags. |
| int | [tisci\_cmd\_proc\_auth\_boot\_image](#aaa3b1c5f5072b40e2eb1c626cb6f6f29) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*image\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*image\_size) |
|  | Command to authenticate and load the image, then set the processor configuration flags. |
| int | [tisci\_cmd\_get\_proc\_boot\_status](#a9e057dd13353ccdd7df3b2263ef22940) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proc\_id, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*bv, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*cfg\_flags, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ctrl\_flags, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*sts\_flags) |
|  | Command to get the processor boot status. |
| int | [tisci\_proc\_wait\_boot\_status\_no\_wait](#a8a29455ba732efa082c1a72922f46f9e) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proc\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_wait\_iterations, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_match\_iterations, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) delay\_per\_iteration\_us, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) delay\_before\_iterations\_us, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) status\_flags\_1\_set\_all\_wait, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) status\_flags\_1\_set\_any\_wait, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) status\_flags\_1\_clr\_all\_wait, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) status\_flags\_1\_clr\_any\_wait) |
|  | Helper function to wait for a processor boot status without requesting or waiting for a response. |
| int | [tisci\_cmd\_proc\_shutdown\_no\_wait](#a9a80ade10fb08159e3fdfbd85ac8dfbf) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) proc\_id) |
|  | Command to shutdown a core without requesting or waiting for a response. |
| int | [cmd\_set\_board\_config\_using\_msg](#ac83cc7874ddc4c42c35e6a9f41e64ee7) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) msg\_type, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Set board configuration using a specified message type. |
| int | [tisci\_cmd\_ring\_config](#a9110e6b0fd37057ea72c64c8c2067a21) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) valid\_params, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) nav\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) index, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr\_lo, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr\_hi, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order\_id) |
|  | Configure a RA ring. |
| int | [tisci\_cmd\_sys\_reset](#aa7b6bef27ce24be4762d28499197a8bd) (const struct [device](structdevice.md) \*dev) |
|  | Request a system reset. |
| int | [tisci\_cmd\_query\_msmc](#a01625817d1a222c2979443413c7d712c) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*msmc\_start, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*msmc\_end) |
|  | Query the available MSMC memory range. |
| int | [tisci\_cmd\_set\_fwl\_region](#a2a1873dd1b47f7437cfd8adbea2decab) (const struct [device](structdevice.md) \*dev, const struct [tisci\_msg\_fwl\_region](structtisci__msg__fwl__region.md) \*region) |
|  | Configure a firewall region. |
| int | [tisci\_cmd\_get\_fwl\_region](#aafb0c859914130228e6c229725f87eca) (const struct [device](structdevice.md) \*dev, struct [tisci\_msg\_fwl\_region](structtisci__msg__fwl__region.md) \*region) |
|  | Get firewall region configuration. |
| int | [tisci\_cmd\_change\_fwl\_owner](#afe30856eaa98b6f30b11ab99daf1dc91) (const struct [device](structdevice.md) \*dev, struct [tisci\_msg\_fwl\_owner](structtisci__msg__fwl__owner.md) \*owner) |
|  | Change firewall region owner. |
| int | [tisci\_cmd\_rm\_udmap\_tx\_ch\_cfg](#a98a90edf1033e5146c51da785ee29581) (const struct [device](structdevice.md) \*dev, const struct [tisci\_msg\_rm\_udmap\_tx\_ch\_cfg](structtisci__msg__rm__udmap__tx__ch__cfg.md) \*params) |
|  | Configure a UDMAP transmit channel. |
| int | [tisci\_cmd\_rm\_udmap\_rx\_ch\_cfg](#a5217423ca42a90a472777a907864128e) (const struct [device](structdevice.md) \*dev, const struct [tisci\_msg\_rm\_udmap\_rx\_ch\_cfg](structtisci__msg__rm__udmap__rx__ch__cfg.md) \*params) |
|  | Configure a UDMAP receive channel. |
| int | [tisci\_cmd\_rm\_psil\_pair](#a64b6aa840b820beed84fc9a21ffde350) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) nav\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) src\_thread, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dst\_thread) |
|  | Pair PSI-L source thread to destination thread. |
| int | [tisci\_cmd\_rm\_psil\_unpair](#a61d3ce5732bbd5a25d5d63af5a059666) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) nav\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) src\_thread, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dst\_thread) |
|  | Unpair PSI-L source thread from destination thread. |
| int | [tisci\_cmd\_rm\_irq\_set](#a0d5c1b5afc2842e38de56c64c62f17fd) (const struct [device](structdevice.md) \*dev, struct [tisci\_irq\_set\_req](structtisci__irq__set__req.md) \*req) |
|  | Set a Navigator Subsystem IRQ. |
| int | [tisci\_cmd\_rm\_irq\_release](#ac30ac2d3539999418f8b200e7b78d259) (const struct [device](structdevice.md) \*dev, struct [tisci\_irq\_release\_req](structtisci__irq__release__req.md) \*req) |
|  | Release a Navigator Subsystem IRQ. |

## Detailed Description

Public APIs for the TISCI driver.

## Macro Definition Documentation

## [◆ ](#a396f8869a1aee7aa1b88a039a17746bf)MAILBOX\_MBOX\_SIZE

| #define MAILBOX\_MBOX\_SIZE   60 |
| --- |

## [◆ ](#a69aa4a4b3a5e99a86adbc6a0ccf74560)TISCI\_MSG\_VALUE\_RM\_DST\_HOST\_IRQ\_VALID

| #define TISCI\_MSG\_VALUE\_RM\_DST\_HOST\_IRQ\_VALID   (1u << 1u) |
| --- |

## [◆ ](#ae309074218959da90a5978304c34e916)TISCI\_MSG\_VALUE\_RM\_DST\_ID\_VALID

| #define TISCI\_MSG\_VALUE\_RM\_DST\_ID\_VALID   (1u << 0u) |
| --- |

## [◆ ](#aad5b430c5924f794b35cfb7c9830b48b)TISCI\_MSG\_VALUE\_RM\_GLOBAL\_EVENT\_VALID

| #define TISCI\_MSG\_VALUE\_RM\_GLOBAL\_EVENT\_VALID   (1u << 4u) |
| --- |

## [◆ ](#abf34b43187cdc7ea4b68ee151816d97a)TISCI\_MSG\_VALUE\_RM\_IA\_ID\_VALID

| #define TISCI\_MSG\_VALUE\_RM\_IA\_ID\_VALID   (1u << 2u) |
| --- |

## [◆ ](#abb692a88d05498a4c0dd5e69857cda92)TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_EXTENDED\_CH\_TYPE\_VALID

| #define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_EXTENDED\_CH\_TYPE\_VALID   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) |
| --- |

## [◆ ](#a04febde272953c690f94d44db18663f7)TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_RX\_FLOWID\_CNT\_VALID

| #define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_RX\_FLOWID\_CNT\_VALID   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

## [◆ ](#ae0c03a2c76f884f37f472b081d0dd028)TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_RX\_FLOWID\_START\_VALID

| #define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_RX\_FLOWID\_START\_VALID   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

## [◆ ](#a818ed2617f42b219d3e3aed2a46ed7d8)TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_RX\_IGNORE\_LONG\_VALID

| #define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_RX\_IGNORE\_LONG\_VALID   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

## [◆ ](#a512091ff6dff198c2801a8f51fe18755)TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_RX\_IGNORE\_SHORT\_VALID

| #define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_RX\_IGNORE\_SHORT\_VALID   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

## [◆ ](#a1110504d079ae51a526ed80144560b27)TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_CREDIT\_COUNT\_VALID

| #define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_CREDIT\_COUNT\_VALID   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

## [◆ ](#af8dbd5c7af94ec3690012458d35f2456)TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_FDEPTH\_VALID

| #define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_FDEPTH\_VALID   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

## [◆ ](#a736e0c626ee9d1df858ce5936bf4029e)TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_FILT\_EINFO\_VALID

| #define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_FILT\_EINFO\_VALID   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

## [◆ ](#a6db1d6169cc2def41e73ce4c22fa118e)TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_FILT\_PSWORDS\_VALID

| #define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_FILT\_PSWORDS\_VALID   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

## [◆ ](#a64195889325d54d493923b95620b1550)TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_SUPR\_TDPKT\_VALID

| #define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_SUPR\_TDPKT\_VALID   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

## [◆ ](#a4de2b535f4d2548218dde6c2dddc9448)TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_TDTYPE\_VALID

| #define TISCI\_MSG\_VALUE\_RM\_UDMAP\_CH\_TX\_TDTYPE\_VALID   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| --- |

## [◆ ](#ae2c0b651fc864d6904bfef4fdacb2aea)TISCI\_MSG\_VALUE\_RM\_VINT\_STATUS\_BIT\_INDEX\_VALID

| #define TISCI\_MSG\_VALUE\_RM\_VINT\_STATUS\_BIT\_INDEX\_VALID   (1u << 5u) |
| --- |

## [◆ ](#a334a7f7a6fd37286c5635f1cfe2d061f)TISCI\_MSG\_VALUE\_RM\_VINT\_VALID

| #define TISCI\_MSG\_VALUE\_RM\_VINT\_VALID   (1u << 3u) |
| --- |

## Function Documentation

## [◆ ](#ac83cc7874ddc4c42c35e6a9f41e64ee7)cmd\_set\_board\_config\_using\_msg()

| int cmd\_set\_board\_config\_using\_msg | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *msg\_type*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *addr*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *size* ) |

Set board configuration using a specified message type.

Sends a board configuration message to the TI SCI firmware with configuration data from a specified memory location.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | msg\_type | TISCI message type for board configuration |
    | addr | Physical address of board configuration data |
    | size | Size of board configuration data in bytes |

Returns
:   0 if successful, or an error code

## [◆ ](#afe30856eaa98b6f30b11ab99daf1dc91)tisci\_cmd\_change\_fwl\_owner()

| int tisci\_cmd\_change\_fwl\_owner | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [tisci\_msg\_fwl\_owner](structtisci__msg__fwl__owner.md) \* | *owner* ) |

Change firewall region owner.

Changes the ownership of a firewall region and retrieves updated ownership information.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | owner | Pointer to firewall owner configuration. On input: contains fwl\_id, region, and owner\_index On output: contains updated ownership information |

Returns
:   0 if successful, or an error code

## [◆ ](#a5c69f5f12b79a0b37a1f704624106960)tisci\_cmd\_clk\_get\_freq()

| int tisci\_cmd\_clk\_get\_freq | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *clk\_id*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *freq* ) |

Get the current frequency of a clock.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | clk\_id | Clock identifier for the device for this request |
    | freq | Pointer to store the current frequency in Hz |

Returns
:   0 if successful, or an error code

## [◆ ](#a9801b388e5dc60f10aa624040cb8bfe2)tisci\_cmd\_clk\_get\_match\_freq()

| int tisci\_cmd\_clk\_get\_match\_freq | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *clk\_id*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *min\_freq*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *target\_freq*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *max\_freq*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *match\_freq* ) |

Get a matching frequency for a clock.

Finds a frequency that matches the requested range for a clock.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | clk\_id | Clock identifier for the device for this request |
    | min\_freq | Minimum allowable frequency in Hz |
    | target\_freq | Target clock frequency in Hz |
    | max\_freq | Maximum allowable frequency in Hz |
    | match\_freq | Pointer to store the matched frequency in Hz |

Returns
:   0 if successful, or an error code

## [◆ ](#ae93fb7c70a4f2299415a51b993d36741)tisci\_cmd\_clk\_get\_num\_parents()

| int tisci\_cmd\_clk\_get\_num\_parents | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *clk\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *num\_parents* ) |

Get the number of parent clocks for a clock.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | clk\_id | Clock identifier for the device for this request |
    | num\_parents | Pointer to store the number of parent clocks |

Returns
:   0 if successful, or an error code

## [◆ ](#a86e0ed2c8711363dc5ea710b12a303af)tisci\_cmd\_clk\_get\_parent()

| int tisci\_cmd\_clk\_get\_parent | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *clk\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *parent\_id* ) |

Get the parent clock for a clock.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | clk\_id | Clock identifier for the device for this request |
    | parent\_id | Pointer to store the identifier of the parent clock |

Returns
:   0 if successful, or an error code

## [◆ ](#aaebb0012c291ded1b9303d634b1bb245)tisci\_cmd\_clk\_is\_auto()

| int tisci\_cmd\_clk\_is\_auto | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *clk\_id*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *req\_state* ) |

Check if the clock is being auto-managed.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | clk\_id | Clock identifier for the device for this request |
    | req\_state | Pointer to store whether the clock is auto-managed |

Returns
:   0 if successful, or an error code

## [◆ ](#a20276a83e2037db6895085770353a194)tisci\_cmd\_clk\_is\_off()

| int tisci\_cmd\_clk\_is\_off | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *clk\_id*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *req\_state*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *curr\_state* ) |

Check if the clock is OFF.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | clk\_id | Clock identifier for the device for this request |
    | req\_state | Pointer to store whether the clock is managed and disabled |
    | curr\_state | Pointer to store whether the clock is NOT ready for operation |

Returns
:   0 if successful, or an error code

## [◆ ](#a7f0bafa6005d46d2786db590a27add25)tisci\_cmd\_clk\_is\_on()

| int tisci\_cmd\_clk\_is\_on | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *clk\_id*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *req\_state*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *curr\_state* ) |

Check if the clock is ON.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | clk\_id | Clock identifier for the device for this request |
    | req\_state | Pointer to store whether the clock is managed and enabled |
    | curr\_state | Pointer to store whether the clock is ready for operation |

Returns
:   0 if successful, or an error code

## [◆ ](#ad3563b7ec2fa13eb4b1faa564062ae12)tisci\_cmd\_clk\_set\_freq()

| int tisci\_cmd\_clk\_set\_freq | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *clk\_id*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *min\_freq*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *target\_freq*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *max\_freq* ) |

Set a frequency for a clock.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | clk\_id | Clock identifier for the device for this request |
    | min\_freq | Minimum allowable frequency in Hz |
    | target\_freq | Target clock frequency in Hz |
    | max\_freq | Maximum allowable frequency in Hz |

Returns
:   0 if successful, or an error code

## [◆ ](#a6ad9804cf3e23246955bcab1e98aecdb)tisci\_cmd\_clk\_set\_parent()

| int tisci\_cmd\_clk\_set\_parent | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *clk\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *parent\_id* ) |

Set the parent clock for a clock.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | clk\_id | Clock identifier for the device for this request |
    | parent\_id | Identifier of the parent clock to set |

Returns
:   0 if successful, or an error code

## [◆ ](#a01393f21cb5a88388ce51e36ba1843fc)tisci\_cmd\_dev\_get\_clcnt()

| int tisci\_cmd\_dev\_get\_clcnt | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *count* ) |

Get the context loss counter for a device.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | count | Pointer to store the context loss counter |

Returns
:   0 if successful, or an error code

## [◆ ](#af9ff6eee5bca675c50c28fbc4af3048c)tisci\_cmd\_dev\_is\_idle()

| int tisci\_cmd\_dev\_is\_idle | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *r\_state* ) |

Check if the device is requested to be idle.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | r\_state | Pointer to store the result (true if requested to be idle) |

Returns
:   0 if successful, or an error code

## [◆ ](#aa7bb463be840666d87a68c1e65496b19)tisci\_cmd\_dev\_is\_on()

| int tisci\_cmd\_dev\_is\_on | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *r\_state*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *curr\_state* ) |

Check if the device is requested to be ON.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | r\_state | Pointer to store the result (true if requested to be ON) |
    | curr\_state | Pointer to store the result (true if currently ON and active) |

Returns
:   0 if successful, or an error code

## [◆ ](#a1a441bdad9bfef9a0136f0b737c9c7aa)tisci\_cmd\_dev\_is\_stop()

| int tisci\_cmd\_dev\_is\_stop | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *r\_state*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *curr\_state* ) |

Check if the device is requested to be stopped.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | r\_state | Pointer to store the result (true if requested to be stopped) |
    | curr\_state | Pointer to store the result (true if currently stopped) |

Returns
:   0 if successful, or an error code

## [◆ ](#a4a3b7acb3098f71b2a9f85fbb318d595)tisci\_cmd\_dev\_is\_trans()

| int tisci\_cmd\_dev\_is\_trans | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *curr\_state* ) |

Check if the device is currently transitioning.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | curr\_state | Pointer to store the result (true if currently transitioning) |

Returns
:   0 if successful, or an error code

## [◆ ](#a4f4072f951c0ebbeb75e8cd2f06b6e8f)tisci\_cmd\_dev\_is\_valid()

| int tisci\_cmd\_dev\_is\_valid | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id* ) |

Check if a device ID is valid.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |

Returns
:   0 if the device ID is valid, or an error code

## [◆ ](#ab63106de04e579ba18f34763b3efa8b3)tisci\_cmd\_get\_clock()

| int tisci\_cmd\_get\_clock | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *clk\_id*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *needs\_ssc*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *can\_change\_freq*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable\_input\_term* ) |

Get control of a clock from TI SCI.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | clk\_id | Clock identifier for the device for this request |
    | needs\_ssc | 'true' if Spread Spectrum clock is desired, else 'false' |
    | can\_change\_freq | 'true' if frequency change is desired, else 'false' |
    | enable\_input\_term | 'true' if input termination is desired, else 'false' |

Returns
:   0 if successful, or an error code

## [◆ ](#a3f8128fa6c8c6f10bb7e302e6e9cfeaf)tisci\_cmd\_get\_clock\_state()

| int tisci\_cmd\_get\_clock\_state | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *clk\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *programmed\_state*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *current\_state* ) |

Get the state of a clock.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | clk\_id | Clock identifier for the device for this request |
    | programmed\_state | Pointer to store the requested state of the clock |
    | current\_state | Pointer to store the current state of the clock |

Returns
:   0 if successful, or an error code

## [◆ ](#a4011bbe29370fb581ab2dd0fcaa151db)tisci\_cmd\_get\_device()

| int tisci\_cmd\_get\_device | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id* ) |

Request exclusive access to a device managed by TISCI.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |

Returns
:   0 if successful, or an error code

## [◆ ](#adc16227f1ec150d0c6cf32442fa3e915)tisci\_cmd\_get\_device\_exclusive()

| int tisci\_cmd\_get\_device\_exclusive | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id* ) |

## [◆ ](#a90613df222309651abc1adb2f4d82272)tisci\_cmd\_get\_device\_resets()

| int tisci\_cmd\_get\_device\_resets | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *reset\_state* ) |

Get reset state for a device managed by TISCI.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | reset\_state | Pointer to store the reset state |

Returns
:   0 if successful, or an error code

## [◆ ](#aafb0c859914130228e6c229725f87eca)tisci\_cmd\_get\_fwl\_region()

| int tisci\_cmd\_get\_fwl\_region | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [tisci\_msg\_fwl\_region](structtisci__msg__fwl__region.md) \* | *region* ) |

Get firewall region configuration.

Retrieves the configuration of a firewall region including permissions, addresses, and control settings.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | region | Pointer to store the firewall region configuration. The fwl\_id, region, and n\_permission\_regs fields must be set before calling this function. |

Returns
:   0 if successful, or an error code

## [◆ ](#a9e057dd13353ccdd7df3b2263ef22940)tisci\_cmd\_get\_proc\_boot\_status()

| int tisci\_cmd\_get\_proc\_boot\_status | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *proc\_id*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *bv*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *cfg\_flags*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *ctrl\_flags*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *sts\_flags* ) |

Command to get the processor boot status.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | proc\_id | Processor ID this request is for |
    | bv | Pointer to store the boot vector |
    | cfg\_flags | Pointer to store the configuration flags |
    | ctrl\_flags | Pointer to store the control flags |
    | sts\_flags | Pointer to store the status flags |

Returns
:   0 if successful, or an error code

## [◆ ](#ae249d114c60b6b1a76f7de8dab5c3ce1)tisci\_cmd\_get\_resource\_range()

| int tisci\_cmd\_get\_resource\_range | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *subtype*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *range\_start*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *range\_num* ) |

Get a range of resources assigned to the host.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | TISCI device ID |
    | subtype | Resource assignment subtype being requested |
    | range\_start | Pointer to store the start index of the resource range |
    | range\_num | Pointer to store the number of resources in the range |

Returns
:   0 if successful, or an error code

## [◆ ](#aa261b08c9141360c5f4f9e50ab151ed5)tisci\_cmd\_get\_resource\_range\_from\_shost()

| int tisci\_cmd\_get\_resource\_range\_from\_shost | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *subtype*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *s\_host*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *range\_start*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *range\_num* ) |

Get a range of resources assigned to a specified host.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | TISCI device ID |
    | subtype | Resource assignment subtype being requested |
    | s\_host | Host processor ID to which the resources are allocated |
    | range\_start | Pointer to store the start index of the resource range |
    | range\_num | Pointer to store the number of resources in the range |

Returns
:   0 if successful, or an error code

## [◆ ](#aea0b9addbd3cfcb2be691f0801128fe1)tisci\_cmd\_get\_revision()

| int tisci\_cmd\_get\_revision | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [tisci\_version\_info](structtisci__version__info.md) \* | *ver* ) |

Get the revision information of the TI SCI firmware.

Queries the TI SCI firmware for its version and revision information. The retrieved information is stored in the provided `ver` structure.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | ver | Pointer to a structure where the firmware version information will be stored |

Returns
:   0 if successful, or a negative error code on failure

## [◆ ](#a3d39780a18358066ec8f187474c18f71)tisci\_cmd\_idle\_clock()

| int tisci\_cmd\_idle\_clock | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *clk\_id* ) |

Idle a clock that is under control of TI SCI.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | clk\_id | Clock identifier for the device for this request |

Returns
:   0 if successful, or an error code

## [◆ ](#ab8203c5d0b699ec726a889e7027ae034)tisci\_cmd\_idle\_device()

| int tisci\_cmd\_idle\_device | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id* ) |

Command to idle a device managed by TISCI.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |

Returns
:   0 if successful, or an error code

## [◆ ](#aab1720913f75a771e041e2195b9deede)tisci\_cmd\_idle\_device\_exclusive()

| int tisci\_cmd\_idle\_device\_exclusive | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id* ) |

## [◆ ](#aaa3b1c5f5072b40e2eb1c626cb6f6f29)tisci\_cmd\_proc\_auth\_boot\_image()

| int tisci\_cmd\_proc\_auth\_boot\_image | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *image\_addr*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *image\_size* ) |

Command to authenticate and load the image, then set the processor configuration flags.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | image\_addr | Pointer to the memory address of the payload image and certificate |
    | image\_size | Pointer to the size of the image after authentication |

Returns
:   0 if successful, or an error code

## [◆ ](#a1acfab0f8fd3b1db050f97aa21d26ce3)tisci\_cmd\_proc\_handover()

| int tisci\_cmd\_proc\_handover | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *proc\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *host\_id* ) |

Command to handover a physical processor control to a host in the processor's access control list.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | proc\_id | Processor ID this request is for |
    | host\_id | Host ID to get the control of the processor |

Returns
:   0 if successful, or an error code

## [◆ ](#a2e0e3e88c635a4e6399941696056b8a9)tisci\_cmd\_proc\_release()

| int tisci\_cmd\_proc\_release | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *proc\_id* ) |

Command to release a physical processor control.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | proc\_id | Processor ID this request is for |

Returns
:   0 if successful, or an error code

## [◆ ](#a3181b68860761b0060048a01d71888a8)tisci\_cmd\_proc\_request()

| int tisci\_cmd\_proc\_request | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *proc\_id* ) |

Command to request a physical processor control.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | proc\_id | Processor ID this request is for |

Returns
:   0 if successful, or an error code

## [◆ ](#a9a80ade10fb08159e3fdfbd85ac8dfbf)tisci\_cmd\_proc\_shutdown\_no\_wait()

| int tisci\_cmd\_proc\_shutdown\_no\_wait | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *proc\_id* ) |

Command to shutdown a core without requesting or waiting for a response.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | proc\_id | Processor ID this request is for |

Returns
:   0 if successful, or an error code

## [◆ ](#ae48c6c78db3f4bee6520c0af66e37e7d)tisci\_cmd\_put\_clock()

| int tisci\_cmd\_put\_clock | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *clk\_id* ) |

Release a clock from control back to TI SCI.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | clk\_id | Clock identifier for the device for this request |

Returns
:   0 if successful, or an error code

## [◆ ](#a5a7c9ff34ad1ffa87c62fef6b2ac8719)tisci\_cmd\_put\_device()

| int tisci\_cmd\_put\_device | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id* ) |

Command to release a device managed by TISCI.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |

Returns
:   0 if successful, or an error code

## [◆ ](#a01625817d1a222c2979443413c7d712c)tisci\_cmd\_query\_msmc()

| int tisci\_cmd\_query\_msmc | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *msmc\_start*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *msmc\_end* ) |

Query the available MSMC memory range.

Queries the TI SCI firmware for the currently available MSMC (Multi-Standard Shared Memory Controller) memory range.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | msmc\_start | Pointer to store the MSMC start address |
    | msmc\_end | Pointer to store the MSMC end address |

Returns
:   0 if successful, or an error code

## [◆ ](#a9110e6b0fd37057ea72c64c8c2067a21)tisci\_cmd\_ring\_config()

| int tisci\_cmd\_ring\_config | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *valid\_params*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *nav\_id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *index*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *addr\_lo*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *addr\_hi*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *count*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mode*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *size*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *order\_id* ) |

Configure a RA ring.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | valid\_params | Bitfield defining validity of ring configuration parameters |
    | nav\_id | Device ID of Navigator Subsystem from which the ring is allocated |
    | index | Ring index |
    | addr\_lo | The ring base address low 32 bits |
    | addr\_hi | The ring base address high 32 bits |
    | count | Number of ring elements |
    | mode | The mode of the ring |
    | size | The ring element size |
    | order\_id | Specifies the ring's bus order ID |

Returns
:   0 if successful, or an error code

## [◆ ](#ac30ac2d3539999418f8b200e7b78d259)tisci\_cmd\_rm\_irq\_release()

| int tisci\_cmd\_rm\_irq\_release | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [tisci\_irq\_release\_req](structtisci__irq__release__req.md) \* | *req* ) |

Release a Navigator Subsystem IRQ.

Releases an interrupt route in the Navigator Subsystem using the provided request structure.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | req | Pointer to the IRQ release request structure |

Returns
:   0 if successful, or an error code

## [◆ ](#a0d5c1b5afc2842e38de56c64c62f17fd)tisci\_cmd\_rm\_irq\_set()

| int tisci\_cmd\_rm\_irq\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [tisci\_irq\_set\_req](structtisci__irq__set__req.md) \* | *req* ) |

Set a Navigator Subsystem IRQ.

Sets up an interrupt route in the Navigator Subsystem using the provided request structure.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | req | Pointer to the IRQ set request structure |

Returns
:   0 if successful, or an error code

## [◆ ](#a64b6aa840b820beed84fc9a21ffde350)tisci\_cmd\_rm\_psil\_pair()

| int tisci\_cmd\_rm\_psil\_pair | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *nav\_id*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *src\_thread*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dst\_thread* ) |

Pair PSI-L source thread to destination thread.

Pairs a PSI-L source thread to a destination thread in the Navigator Subsystem.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | nav\_id | Navigator Subsystem device ID |
    | src\_thread | Source thread ID |
    | dst\_thread | Destination thread ID |

Returns
:   0 if successful, or an error code

## [◆ ](#a61d3ce5732bbd5a25d5d63af5a059666)tisci\_cmd\_rm\_psil\_unpair()

| int tisci\_cmd\_rm\_psil\_unpair | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *nav\_id*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *src\_thread*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dst\_thread* ) |

Unpair PSI-L source thread from destination thread.

Unpairs a PSI-L source thread from a destination thread in the Navigator Subsystem.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | nav\_id | Navigator Subsystem device ID |
    | src\_thread | Source thread ID |
    | dst\_thread | Destination thread ID |

Returns
:   0 if successful, or an error code

## [◆ ](#a5217423ca42a90a472777a907864128e)tisci\_cmd\_rm\_udmap\_rx\_ch\_cfg()

| int tisci\_cmd\_rm\_udmap\_rx\_ch\_cfg | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [tisci\_msg\_rm\_udmap\_rx\_ch\_cfg](structtisci__msg__rm__udmap__rx__ch__cfg.md) \* | *params* ) |

Configure a UDMAP receive channel.

Configures the non-real-time registers of a Navigator Subsystem UDMAP receive channel.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | params | Pointer to the receive channel configuration parameters |

Returns
:   0 if successful, or an error code

## [◆ ](#a98a90edf1033e5146c51da785ee29581)tisci\_cmd\_rm\_udmap\_tx\_ch\_cfg()

| int tisci\_cmd\_rm\_udmap\_tx\_ch\_cfg | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [tisci\_msg\_rm\_udmap\_tx\_ch\_cfg](structtisci__msg__rm__udmap__tx__ch__cfg.md) \* | *params* ) |

Configure a UDMAP transmit channel.

Configures the non-real-time registers of a Navigator Subsystem UDMAP transmit channel.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | params | Pointer to the transmit channel configuration parameters |

Returns
:   0 if successful, or an error code

## [◆ ](#a94f43ead8c81320f651fa9c0450a2493)tisci\_cmd\_set\_device\_resets()

| int tisci\_cmd\_set\_device\_resets | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *reset\_state* ) |

Set resets for a device managed by TISCI.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | reset\_state | Device-specific reset bit field |

Returns
:   0 if successful, or an error code

## [◆ ](#a2a1873dd1b47f7437cfd8adbea2decab)tisci\_cmd\_set\_fwl\_region()

| int tisci\_cmd\_set\_fwl\_region | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [tisci\_msg\_fwl\_region](structtisci__msg__fwl__region.md) \* | *region* ) |

Configure a firewall region.

Sets up a firewall region with the specified configuration parameters including permissions, addresses, and control settings.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | region | Pointer to the firewall region configuration parameters |

Returns
:   0 if successful, or an error code

## [◆ ](#a3551276e98c3f03ea4beb9086c3b89c3)tisci\_cmd\_set\_proc\_boot\_cfg()

| int tisci\_cmd\_set\_proc\_boot\_cfg | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *proc\_id*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *bootvector*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *config\_flags\_set*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *config\_flags\_clear* ) |

Command to set the processor boot configuration flags.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | proc\_id | Processor ID this request is for |
    | bootvector | Boot vector address |
    | config\_flags\_set | Configuration flags to be set |
    | config\_flags\_clear | Configuration flags to be cleared |

Returns
:   0 if successful, or an error code

## [◆ ](#aee60c2eb75e6786b91d9dc73c7a7e2c6)tisci\_cmd\_set\_proc\_boot\_ctrl()

| int tisci\_cmd\_set\_proc\_boot\_ctrl | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *proc\_id*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *control\_flags\_set*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *control\_flags\_clear* ) |

Command to set the processor boot control flags.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | proc\_id | Processor ID this request is for |
    | control\_flags\_set | Control flags to be set |
    | control\_flags\_clear | Control flags to be cleared |

Returns
:   0 if successful, or an error code

## [◆ ](#aa7b6bef27ce24be4762d28499197a8bd)tisci\_cmd\_sys\_reset()

| int tisci\_cmd\_sys\_reset | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Request a system reset.

Commands the TI SCI firmware to perform a system reset.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |

Returns
:   0 if successful, or an error code

## [◆ ](#ada78c57b3cb24e57a3f6cc155e3a3d09)tisci\_get\_device\_state()

| int tisci\_get\_device\_state | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *clcnt*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *resets*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *p\_state*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *c\_state* ) |

Get the state of a device.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | clcnt | Pointer to store the Context Loss Count |
    | resets | Pointer to store the reset count |
    | p\_state | Pointer to store the programmed state |
    | c\_state | Pointer to store the current state |

Returns
:   0 if successful, or an error code

## [◆ ](#a8ced32499c14aae81994368d4450422d)tisci\_get\_resource\_range()

| int tisci\_get\_resource\_range | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *subtype*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *s\_host*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *range\_start*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *range\_num* ) |

Get a range of resources assigned to a host.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | TISCI device ID |
    | subtype | Resource assignment subtype being requested |
    | s\_host | Host processor ID to which the resources are allocated |
    | range\_start | Pointer to store the start index of the resource range |
    | range\_num | Pointer to store the number of resources in the range |

Returns
:   0 if successful, or an error code

## [◆ ](#a8a29455ba732efa082c1a72922f46f9e)tisci\_proc\_wait\_boot\_status\_no\_wait()

| int tisci\_proc\_wait\_boot\_status\_no\_wait | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *proc\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_wait\_iterations*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_match\_iterations*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *delay\_per\_iteration\_us*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *delay\_before\_iterations\_us*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *status\_flags\_1\_set\_all\_wait*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *status\_flags\_1\_set\_any\_wait*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *status\_flags\_1\_clr\_all\_wait*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *status\_flags\_1\_clr\_any\_wait* ) |

Helper function to wait for a processor boot status without requesting or waiting for a response.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | proc\_id | Processor ID this request is for |
    | num\_wait\_iterations | Total number of iterations to check before timeout |
    | num\_match\_iterations | Number of consecutive matches required to confirm status |
    | delay\_per\_iteration\_us | Delay in microseconds between each status check |
    | delay\_before\_iterations\_us | Delay in microseconds before the first status check |
    | status\_flags\_1\_set\_all\_wait | Flags that must all be set to 1 |
    | status\_flags\_1\_set\_any\_wait | Flags where at least one must be set to 1 |
    | status\_flags\_1\_clr\_all\_wait | Flags that must all be cleared to 0 |
    | status\_flags\_1\_clr\_any\_wait | Flags where at least one must be cleared to 0 |

Returns
:   0 if successful, or an error code

## [◆ ](#a086d96bed3d789bf303f56405a791aa6)tisci\_set\_clock\_state()

| int tisci\_set\_clock\_state | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *clk\_id*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *state* ) |

Set the state of a clock.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | clk\_id | Clock identifier for the device for this request |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Header flags as needed |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | State to request for the clock |

Returns
:   0 if successful, or an error code

## [◆ ](#a8b6d6f99df32eeba9131ce130ee4f12d)tisci\_set\_device\_state()

| int tisci\_set\_device\_state | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *state* ) |

Set the state of a device.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags to set for the device |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | State to move the device to:  - 0: Device is off - 1: Device is on - 2: Device is in retention - 3: Device is in reset |

Returns
:   0 if successful, or an error code

## [◆ ](#a05f871388f68d9c71620ea43bde1e3ab)tisci\_set\_device\_state\_no\_wait()

| int tisci\_set\_device\_state\_no\_wait | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_id*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *state* ) |

Set the state of a device without waiting for a response.

Parameters
:   | dev | Pointer to the TI SCI device |
    | --- | --- |
    | dev\_id | Device identifier for this request |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags to set for the device |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | State to move the device to:  - 0: Device is off - 1: Device is on - 2: Device is in retention - 3: Device is in reset |

Returns
:   0 if successful, or an error code

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [firmware](dir_e97f19a49725d52aae6eece65b856a75.md)
- [tisci](dir_32233e7c9e492e9cba0b091ed92f7703.md)
- [tisci.h](tisci_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
