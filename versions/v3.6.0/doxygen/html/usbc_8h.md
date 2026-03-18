---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/usbc_8h.html
original_path: doxygen/html/usbc_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbc.h File Reference

USB-C Device APIs.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/usb_c/usbc_tcpc.h](usbc__tcpc_8h_source.md)>`  
`#include <[zephyr/drivers/usb_c/usbc_vbus.h](usbc__vbus_8h_source.md)>`

[Go to the source code of this file.](usbc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [FIXED\_5V\_100MA\_RDO](group____usbc__device__api.md#gaaa5c1f6278a7ca6d589c9c80695ca746)   0x1100280a |
|  | This Request Data Object (RDO) value can be returned from the policy\_cb\_get\_rdo if 5V@100mA with the following options are sufficient for the Sink to operate. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [policy\_cb\_get\_snk\_cap\_t](group__sink__callbacks.md#gaaed0161142c3481ce9180015b6968357)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*\*pdos, int \*num\_pdos) |
|  | Callback type used to get the Sink Capabilities. |
| typedef void(\* | [policy\_cb\_set\_src\_cap\_t](group__sink__callbacks.md#ga6096d6909698f1b86a1a9cbd1f8d4097)) (const struct [device](structdevice.md) \*dev, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*pdos, const int num\_pdos) |
|  | Callback type used to report the received Port Partner's Source Capabilities. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [policy\_cb\_check\_t](group__sink__callbacks.md#ga2aacd704d08a8cecbf818150e8ec51b6)) (const struct [device](structdevice.md) \*dev, const enum [usbc\_policy\_check\_t](group____usbc__device__api.md#gafea882f4f3cc96c502d53a24a3e5aec5) policy\_check) |
|  | Callback type used to check a policy. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [policy\_cb\_wait\_notify\_t](group__sink__callbacks.md#gaea62016b263dfaf5f869dd6ea036fdad)) (const struct [device](structdevice.md) \*dev, const enum [usbc\_policy\_wait\_t](group____usbc__device__api.md#gadf5d2934b5dc8e2b01d20bb904988784) wait\_notify) |
|  | Callback type used to notify Device Policy Manager of WAIT message reception. |
| typedef void(\* | [policy\_cb\_notify\_t](group__sink__callbacks.md#ga44af668d9c22e757983c803d7b8ff82e)) (const struct [device](structdevice.md) \*dev, const enum [usbc\_policy\_notify\_t](group____usbc__device__api.md#ga66f934a5c5cd88b574c71d1f18fbda23) policy\_notify) |
|  | Callback type used to notify Device Policy Manager of a policy change. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [policy\_cb\_get\_rdo\_t](group__sink__callbacks.md#gae0448c6b271273c5db59775c3a6260dc)) (const struct [device](structdevice.md) \*dev) |
|  | Callback type used to get the Request Data Object (RDO). |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [policy\_cb\_is\_snk\_at\_default\_t](group__sink__callbacks.md#ga1a3da6faad509213f607893fef16b673)) (const struct [device](structdevice.md) \*dev) |
|  | Callback type used to check if the sink power supply is at the default level. |
| typedef int(\* | [policy\_cb\_get\_src\_caps\_t](group__source__callbacks.md#ga4bbf78bd752d38d915412dd942d3aab8)) (const struct [device](structdevice.md) \*dev, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*\*pdos, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*num\_pdos) |
|  | Callback type used to get the Source Capabilities from the Device Policy Manager. |
| typedef enum [usbc\_snk\_req\_reply\_t](group____usbc__device__api.md#ga4c4f0592a034b4e49eee85e95af33f94)(\* | [policy\_cb\_check\_sink\_request\_t](group__source__callbacks.md#gaeeda677224456f685137e4b345c0e173)) (const struct [device](structdevice.md) \*dev, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) request\_msg) |
|  | Callback type used to check if Sink request is valid. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [policy\_cb\_is\_ps\_ready\_t](group__source__callbacks.md#gae7391e858485e44a74e5fcdbb7931ca7)) (const struct [device](structdevice.md) \*dev) |
|  | Callback type used to check if Source Power Supply is ready. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [policy\_cb\_present\_contract\_is\_valid\_t](group__source__callbacks.md#ga2925e462140a700920251d92ae5a3aa4)) (const struct [device](structdevice.md) \*dev, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) present\_contract) |
|  | Callback type used to check if present Contract is still valid. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [policy\_cb\_change\_src\_caps\_t](group__source__callbacks.md#ga699811c862990b31ec0126dd3a4c3e4d)) (const struct [device](structdevice.md) \*dev) |
|  | Callback type used to request that a different set of Source Caps be sent to the Sink. |
| typedef void(\* | [policy\_cb\_set\_port\_partner\_snk\_cap\_t](group__source__callbacks.md#gae903c8108e8d1563cb0b1ccdd901c925)) (const struct [device](structdevice.md) \*dev, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*pdos, const int num\_pdos) |
|  | Callback type used to report the Capabilities received from a Sink Port Partner. |
| typedef int(\* | [policy\_cb\_get\_src\_rp\_t](group__source__callbacks.md#ga7c75f8192001179f20bf1fe48316f3c6)) (const struct [device](structdevice.md) \*dev, enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) \*rp) |
|  | Callback type used to get the Rp value that should be placed on the CC lines. |
| typedef int(\* | [policy\_cb\_src\_en\_t](group__source__callbacks.md#gaaecac7683d7092c0a477e8d9ca0e5a33)) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) en) |
|  | Callback type used to enable VBUS. |

| Enumerations | |
| --- | --- |
| enum | [usbc\_policy\_request\_t](group____usbc__device__api.md#ga38a301a97a5e1a85e9836bbf083859f3) {     [REQUEST\_NOP](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a2274197ac367b3da6358cac8dd781134) , [REQUEST\_TC\_DISABLED](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a899633a1b63b1c3a826b5556f0f23d8b) , [REQUEST\_TC\_ERROR\_RECOVERY](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a8a7b77d81428f0c4784af3204f33b290) , [REQUEST\_TC\_END](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a0c5ff3bc4c0d6f636663fd3911ed85d5) ,     [REQUEST\_PE\_DR\_SWAP](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a1fe9f57fac7f5149fe5f0f7c42523536) , [REQUEST\_PE\_HARD\_RESET\_SEND](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a7c3c9c959439ee73539cff13e561c403) , [REQUEST\_PE\_SOFT\_RESET\_SEND](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3ad45120b1ceabeb054c2c2273b8431894) , [REQUEST\_PE\_GET\_SRC\_CAPS](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3a8c6083028ee8655cd0bebb6d9aab2e1e) ,     [REQUEST\_GET\_SNK\_CAPS](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3ade1edc3aef0e4d563934edbc9ce784bc) , [REQUEST\_PE\_GOTO\_MIN](group____usbc__device__api.md#gga38a301a97a5e1a85e9836bbf083859f3ae5b4eb0db00e81a98cfe2436b64a7018)   } |
|  | Device Policy Manager requests. [More...](group____usbc__device__api.md#ga38a301a97a5e1a85e9836bbf083859f3) |
| enum | [usbc\_policy\_notify\_t](group____usbc__device__api.md#ga66f934a5c5cd88b574c71d1f18fbda23) {     [MSG\_ACCEPT\_RECEIVED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a43bc56906b5dc4767d3297400053d286) , [MSG\_REJECTED\_RECEIVED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a4ad0620e76c694004d3a1b43458a14b2) , [MSG\_DISCARDED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23aa316636e8353dad1a9d5dec8b85a67e4) , [MSG\_NOT\_SUPPORTED\_RECEIVED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23ab2f97ffaa13c84e656f7ac0004ec86ae) ,     [DATA\_ROLE\_IS\_UFP](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a4020203569dcb95ab1b3d2946efced19) , [DATA\_ROLE\_IS\_DFP](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a791604f4f0b2a2c3ccea4e98d1659a61) , [PD\_CONNECTED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23adbefad204068244fdf75ba1ff211fbfc) , [NOT\_PD\_CONNECTED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23adebcbf5155b43ce562127d4077d46d7d) ,     [TRANSITION\_PS](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a3a27b8e70ffe5788aa3ffea1bf61cae9) , [PORT\_PARTNER\_NOT\_RESPONSIVE](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23ad52e1c4f949bb64fef1d996ac2f4e0de) , [PROTOCOL\_ERROR](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a8cb937247ec21f791706f4f426496a8c) , [SNK\_TRANSITION\_TO\_DEFAULT](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23aa02158d0afdd60c755453977200dfb28) ,     [HARD\_RESET\_RECEIVED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23ab74f5bcaa94a5fb1e46cdd7c6a5d822f) , [POWER\_CHANGE\_0A0](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a0fb0676a11ad8bad2d5249031ba5fd19) , [POWER\_CHANGE\_DEF](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a3a50be6f70c1a7abd724ab447491c46a) , [POWER\_CHANGE\_1A5](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a336bfb983c4d07684d67d4d9ef6c1489) ,     [POWER\_CHANGE\_3A0](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a3477c1c6ad8885c3ab7a9c58b7399dcf) , [SENDER\_RESPONSE\_TIMEOUT](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23ac22b0026881f65c574d0bf7454321745) , [SOURCE\_CAPABILITIES\_RECEIVED](group____usbc__device__api.md#gga66f934a5c5cd88b574c71d1f18fbda23a0266a21d8c836cf281c30542eb6badd4)   } |
|  | Device Policy Manager notifications. [More...](group____usbc__device__api.md#ga66f934a5c5cd88b574c71d1f18fbda23) |
| enum | [usbc\_policy\_check\_t](group____usbc__device__api.md#gafea882f4f3cc96c502d53a24a3e5aec5) {     [CHECK\_POWER\_ROLE\_SWAP](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a1181a470497b797136cf0eb204394106) , [CHECK\_DATA\_ROLE\_SWAP\_TO\_DFP](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5afa602e00bf418656e365baa4d9ff6cef) , [CHECK\_DATA\_ROLE\_SWAP\_TO\_UFP](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a7c97208a8a12f70e7ffa43bb406b9ebd) , [CHECK\_SNK\_AT\_DEFAULT\_LEVEL](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a17f7f4fc9aa4178f0358769dedd29ade) ,     [CHECK\_VCONN\_CONTROL](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a655e913c86db5caa961083dad9f6b7a1) , [CHECK\_SRC\_PS\_AT\_DEFAULT\_LEVEL](group____usbc__device__api.md#ggafea882f4f3cc96c502d53a24a3e5aec5a42b660bb630edcca5ae8b031033d0718)   } |
|  | Device Policy Manager checks. [More...](group____usbc__device__api.md#gafea882f4f3cc96c502d53a24a3e5aec5) |
| enum | [usbc\_policy\_wait\_t](group____usbc__device__api.md#gadf5d2934b5dc8e2b01d20bb904988784) { [WAIT\_SINK\_REQUEST](group____usbc__device__api.md#ggadf5d2934b5dc8e2b01d20bb904988784a009ce2ceacd92db88d9a6beb01f84a28) , [WAIT\_POWER\_ROLE\_SWAP](group____usbc__device__api.md#ggadf5d2934b5dc8e2b01d20bb904988784a91f1f41bf9318e06c02c1957a39a762a) , [WAIT\_DATA\_ROLE\_SWAP](group____usbc__device__api.md#ggadf5d2934b5dc8e2b01d20bb904988784ae5ef03f78d78a7014404c581bad77c18) , [WAIT\_VCONN\_SWAP](group____usbc__device__api.md#ggadf5d2934b5dc8e2b01d20bb904988784aa982aed81f39e35cde74399c6d74e601) } |
|  | Device Policy Manager Wait message notifications. [More...](group____usbc__device__api.md#gadf5d2934b5dc8e2b01d20bb904988784) |
| enum | [usbc\_snk\_req\_reply\_t](group____usbc__device__api.md#ga4c4f0592a034b4e49eee85e95af33f94) { [SNK\_REQUEST\_VALID](group____usbc__device__api.md#gga4c4f0592a034b4e49eee85e95af33f94a7922edb67afe83596819994a71de76dd) , [SNK\_REQUEST\_REJECT](group____usbc__device__api.md#gga4c4f0592a034b4e49eee85e95af33f94a714f82e830f9528a8200c2c14795b282) , [SNK\_REQUEST\_WAIT](group____usbc__device__api.md#gga4c4f0592a034b4e49eee85e95af33f94a7ae46f6deb593eedd0564d30cb4c75fb) } |
|  | Device Policy Manager's response to a Sink Request. [More...](group____usbc__device__api.md#ga4c4f0592a034b4e49eee85e95af33f94) |

| Functions | |
| --- | --- |
| int | [usbc\_start](group____usbc__device__api.md#ga1535f7f53b3cc859ff536883fd631830) (const struct [device](structdevice.md) \*dev) |
|  | Start the USB-C Subsystem. |
| int | [usbc\_suspend](group____usbc__device__api.md#ga68b73c03a5098a21260b5c3638edc973) (const struct [device](structdevice.md) \*dev) |
|  | Suspend the USB-C Subsystem. |
| int | [usbc\_request](group____usbc__device__api.md#ga42691b0bb2b4be50147ac655e2cd9761) (const struct [device](structdevice.md) \*dev, const enum [usbc\_policy\_request\_t](group____usbc__device__api.md#ga38a301a97a5e1a85e9836bbf083859f3) req) |
|  | Make a request of the USB-C Subsystem. |
| void | [usbc\_bypass\_next\_sleep](group____usbc__device__api.md#ga0ffb467dc02585187e9543b17abd6c6a) (const struct [device](structdevice.md) \*dev) |
| void | [usbc\_set\_dpm\_data](group____usbc__device__api.md#ga997007cab2e54ad53b774b4215d0f593) (const struct [device](structdevice.md) \*dev, void \*dpm\_data) |
|  | Set pointer to Device Policy Manager (DPM) data. |
| void \* | [usbc\_get\_dpm\_data](group____usbc__device__api.md#gabd99b6926baf67212d65c4a4d147ce5b) (const struct [device](structdevice.md) \*dev) |
|  | Get pointer to Device Policy Manager (DPM) data. |
| void | [usbc\_set\_vconn\_control\_cb](group____usbc__device__api.md#ga9846b36061453023e16c160f5f120159) (const struct [device](structdevice.md) \*dev, const [tcpc\_vconn\_control\_cb\_t](group__usb__type__c__port__controller__api.md#ga7a989ffd6bdc83696188de59acbd49c7) cb) |
|  | Set the callback used to set VCONN control. |
| void | [usbc\_set\_vconn\_discharge\_cb](group____usbc__device__api.md#ga8741df33b5432d9c7d5902af9bd67084) (const struct [device](structdevice.md) \*dev, const [tcpc\_vconn\_discharge\_cb\_t](group__usb__type__c__port__controller__api.md#ga4437e66605f988be1e16c52b9912e9c2) cb) |
|  | Set the callback used to discharge VCONN. |
| void | [usbc\_set\_policy\_cb\_check](group____usbc__device__api.md#ga67a046b411134d7c631942ae6ba73fc5) (const struct [device](structdevice.md) \*dev, const [policy\_cb\_check\_t](group__sink__callbacks.md#ga2aacd704d08a8cecbf818150e8ec51b6) cb) |
|  | Set the callback used to check a policy. |
| void | [usbc\_set\_policy\_cb\_notify](group____usbc__device__api.md#gaedec1b4ad7b028ad18e1bcbe5396f1ee) (const struct [device](structdevice.md) \*dev, const [policy\_cb\_notify\_t](group__sink__callbacks.md#ga44af668d9c22e757983c803d7b8ff82e) cb) |
|  | Set the callback used to notify Device Policy Manager of a policy change. |
| void | [usbc\_set\_policy\_cb\_wait\_notify](group____usbc__device__api.md#gaa295593c7d5ede31328efaaab38b5880) (const struct [device](structdevice.md) \*dev, const [policy\_cb\_wait\_notify\_t](group__sink__callbacks.md#gaea62016b263dfaf5f869dd6ea036fdad) cb) |
|  | Set the callback used to notify Device Policy Manager of WAIT message reception. |
| void | [usbc\_set\_policy\_cb\_get\_snk\_cap](group____usbc__device__api.md#gafbd2885d758aa869635041fa89750596) (const struct [device](structdevice.md) \*dev, const [policy\_cb\_get\_snk\_cap\_t](group__sink__callbacks.md#gaaed0161142c3481ce9180015b6968357) cb) |
|  | Set the callback used to get the Sink Capabilities. |
| void | [usbc\_set\_policy\_cb\_set\_src\_cap](group____usbc__device__api.md#ga4536f47082f58f49d492de6f2b00dd17) (const struct [device](structdevice.md) \*dev, const [policy\_cb\_set\_src\_cap\_t](group__sink__callbacks.md#ga6096d6909698f1b86a1a9cbd1f8d4097) cb) |
|  | Set the callback used to store the received Port Partner's Source Capabilities. |
| void | [usbc\_set\_policy\_cb\_get\_rdo](group____usbc__device__api.md#ga7c1ffea81f71416ab2942fc5a5b67d41) (const struct [device](structdevice.md) \*dev, const [policy\_cb\_get\_rdo\_t](group__sink__callbacks.md#gae0448c6b271273c5db59775c3a6260dc) cb) |
|  | Set the callback used to get the Request Data Object (RDO). |
| void | [usbc\_set\_policy\_cb\_is\_snk\_at\_default](group____usbc__device__api.md#gaffa045ee6e2fbc07fde7e84e44d3853f) (const struct [device](structdevice.md) \*dev, const [policy\_cb\_is\_snk\_at\_default\_t](group__sink__callbacks.md#ga1a3da6faad509213f607893fef16b673) cb) |
|  | Set the callback used to check if the sink power supply is at the default level. |
| void | [usbc\_set\_policy\_cb\_get\_src\_rp](group____usbc__device__api.md#ga8974f9661dfebf8f686d677f999d5957) (const struct [device](structdevice.md) \*dev, const [policy\_cb\_get\_src\_rp\_t](group__source__callbacks.md#ga7c75f8192001179f20bf1fe48316f3c6) cb) |
|  | Set the callback used to get the Rp value that should be placed on the CC lines. |
| void | [usbc\_set\_policy\_cb\_src\_en](group____usbc__device__api.md#gaf5332ba0c87ff737e1c476d7be071fec) (const struct [device](structdevice.md) \*dev, const [policy\_cb\_src\_en\_t](group__source__callbacks.md#gaaecac7683d7092c0a477e8d9ca0e5a33) cb) |
|  | Set the callback used to enable VBUS. |
| void | [usbc\_set\_policy\_cb\_get\_src\_caps](group____usbc__device__api.md#ga7800c065ae5cfb7a95b58865d47c7f04) (const struct [device](structdevice.md) \*dev, const [policy\_cb\_get\_src\_caps\_t](group__source__callbacks.md#ga4bbf78bd752d38d915412dd942d3aab8) cb) |
|  | Set the callback used to get the Source Capabilities from the Device Policy Manager. |
| void | [usbc\_set\_policy\_cb\_check\_sink\_request](group____usbc__device__api.md#ga7f85188cc4f1a95350195abd0d736ada) (const struct [device](structdevice.md) \*dev, const [policy\_cb\_check\_sink\_request\_t](group__source__callbacks.md#gaeeda677224456f685137e4b345c0e173) cb) |
|  | Set the callback used to check if Sink request is valid. |
| void | [usbc\_set\_policy\_cb\_is\_ps\_ready](group____usbc__device__api.md#gaf25c9cc2b6c514b9dcddc8129a76ccee) (const struct [device](structdevice.md) \*dev, const [policy\_cb\_is\_ps\_ready\_t](group__source__callbacks.md#gae7391e858485e44a74e5fcdbb7931ca7) cb) |
|  | Set the callback used to check if Source Power Supply is ready. |
| void | [usbc\_set\_policy\_cb\_present\_contract\_is\_valid](group____usbc__device__api.md#ga5b4adb4330dfadf127d0a01253d722bb) (const struct [device](structdevice.md) \*dev, const [policy\_cb\_present\_contract\_is\_valid\_t](group__source__callbacks.md#ga2925e462140a700920251d92ae5a3aa4) cb) |
|  | Set the callback to check if present Contract is still valid. |
| void | [usbc\_set\_policy\_cb\_change\_src\_caps](group____usbc__device__api.md#gaa8f89bfb1e9a1840b2d61ebaa13aeb2f) (const struct [device](structdevice.md) \*dev, const [policy\_cb\_change\_src\_caps\_t](group__source__callbacks.md#ga699811c862990b31ec0126dd3a4c3e4d) cb) |
|  | Set the callback used to request that a different set of Source Caps be sent to the Sink. |
| void | [usbc\_set\_policy\_cb\_set\_port\_partner\_snk\_cap](group____usbc__device__api.md#gafd0a407558bb92dc8b7007d9d717b940) (const struct [device](structdevice.md) \*dev, const [policy\_cb\_set\_port\_partner\_snk\_cap\_t](group__source__callbacks.md#gae903c8108e8d1563cb0b1ccdd901c925) cb) |
|  | Set the callback used to store the Capabilities received from a Sink Port Partner. |

## Detailed Description

USB-C Device APIs.

This file contains the USB-C Device APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb\_c](dir_29299904d896cedab2c4945a0291e19f.md)
- [usbc.h](usbc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
