---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/usbc__tc_8h.html
original_path: doxygen/html/usbc__tc_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbc\_tc.h File Reference

USB Type-C Cable and Connector API used for USB-C drivers.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](usbc__tc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [TC\_V\_SINK\_DISCONNECT\_MIN\_MV](group__usb__type__c.md#ga025aeca5768435b245ecb9fe8bfa29c8)   800 |
|  | VBUS minimum for a sink disconnect detection. |
| #define | [TC\_V\_SINK\_DISCONNECT\_MAX\_MV](group__usb__type__c.md#ga151c5852b9d2ad3f6f7f0869505e854b)   3670 |
|  | VBUS maximum for a sink disconnect detection. |
| #define | [TC\_T\_VBUS\_ON\_MAX\_MS](group__usb__type__c.md#gace546c362f92ed1ba0455a5d8006357c)   275 |
|  | From entry to Attached.SRC until VBUS reaches the minimum vSafe5V threshold as measured at the source’s receptacle See Table 4-29 VBUS and VCONN Timing Parameters. |
| #define | [TC\_T\_VBUS\_OFF\_MAX\_MS](group__usb__type__c.md#ga2d6440c7b480ee75ccadf8242e29e7e9)   650 |
|  | From the time the Sink is detached until the Source removes VBUS and reaches vSafe0V (See USB PD). |
| #define | [TC\_T\_VCONN\_ON\_MAX\_MS](group__usb__type__c.md#gaf2cbadac415eedae8c4db3dc91f3623b)   2 |
|  | From the time the Source supplied VBUS in the Attached.SRC state. |
| #define | [TC\_T\_VCONN\_ON\_PA\_MAX\_MS](group__usb__type__c.md#ga24837587c589d85bc48bed2a6815798d)   100 |
|  | From the time a Sink with accessory support enters the PoweredAccessory state until the Sink sources minimum VCONN voltage (see Table 4-5) See Table 4-29 VBUS and VCONN Timing Parameters. |
| #define | [TC\_T\_VCONN\_OFF\_MAX\_MS](group__usb__type__c.md#ga2f347359b4ffc4478338cbbc8a62d4d9)   35 |
|  | From the time that a Sink is detached or as directed until the VCONN supply is disconnected. |
| #define | [TC\_T\_SINK\_ADJ\_MAX\_MS](group__usb__type__c.md#gaa1291eb2b50b59a9746ffe0658d60258)   60 |
|  | Response time for a Sink to adjust its current consumption to be in the specified range due to a change in USB Type-C Current advertisement See Table 4-29 VBUS and VCONN Timing Parameters. |
| #define | [TC\_T\_DRP\_MIN\_MS](group__usb__type__c.md#gab042a018fbc99a402ab23371c3d6fe47)   50 |
|  | The minimum period a DRP shall complete a Source to Sink and back advertisement See Table 4-30 DRP Timing Parameters. |
| #define | [TC\_T\_DRP\_MAX\_MS](group__usb__type__c.md#gaba34e5687c2e12984629a9297f0e7813)   100 |
|  | The maximum period a DRP shall complete a Source to Sink and back advertisement See Table 4-30 DRP Timing Parameters. |
| #define | [TC\_T\_DRP\_TRANSITION\_MIN\_MS](group__usb__type__c.md#ga6ab07167512c79d9587d547902443049)   0 |
|  | The minimum time a DRP shall complete transitions between Source and Sink roles during role resolution See Table 4-30 DRP Timing Parameters. |
| #define | [TC\_T\_DRP\_TRANSITION\_MAX\_MS](group__usb__type__c.md#gae1e9780a30b644a1f15463cba216e385)   1 |
|  | The maximum time a DRP shall complete transitions between Source and Sink roles during role resolution See Table 4-30 DRP Timing Parameters. |
| #define | [TC\_T\_DRP\_TRY\_MIN\_MS](group__usb__type__c.md#ga1ee8d43885ebc26a2f4da640d5758188)   75 |
|  | Minimum wait time associated with the Try.SRC state. |
| #define | [TC\_T\_DRP\_TRY\_MAX\_MS](group__usb__type__c.md#ga95cd5ac306f2d27440b980593c759f07)   150 |
|  | Maximum wait time associated with the Try.SRC state. |
| #define | [TC\_T\_DRP\_TRY\_WAIT\_MIN\_MS](group__usb__type__c.md#gae19a1dc5b950495866359deef2cd6c7c)   400 |
|  | Minimum wait time associated with the Try.SNK state. |
| #define | [TC\_T\_DRP\_TRY\_WAIT\_MAX\_MS](group__usb__type__c.md#ga0eb5b996e1678f3830c38584f84a6268)   800 |
|  | Maximum wait time associated with the Try.SNK state. |
| #define | [TC\_T\_TRY\_TIMEOUT\_MIN\_MS](group__usb__type__c.md#ga45be1dbb0a9ad2e9a9b0549f953cb8c2)   550 |
|  | Minimum timeout for transition from Try.SRC to TryWait.SNK. |
| #define | [TC\_T\_TRY\_TIMEOUT\_MAX\_MS](group__usb__type__c.md#gae3e98e8acbfb5fa7f398dea64265cb0a)   1100 |
|  | Maximum timeout for transition from Try.SRC to TryWait.SNK. |
| #define | [TC\_T\_VPD\_DETACH\_MIN\_MS](group__usb__type__c.md#ga50a154595c40bba3e46751f6f46df848)   10 |
|  | Minimum Time for a DRP to detect that the connected Charge-Through VCONNPowered USB Device has been detached, after VBUS has been removed. |
| #define | [TC\_T\_VPD\_DETACH\_MAX\_MS](group__usb__type__c.md#ga33b792a38351081f316e6f854710a96e)   20 |
|  | Maximum Time for a DRP to detect that the connected Charge-Through VCONNPowered USB Device has been detached, after VBUS has been removed. |
| #define | [TC\_T\_CC\_DEBOUNCE\_MIN\_MS](group__usb__type__c.md#gae059acba0f01f24cb682ee2c3ded59d9)   100 |
|  | Minimum time a port shall wait before it can determine it is attached See Table 4-31 CC Timing. |
| #define | [TC\_T\_CC\_DEBOUNCE\_MAX\_MS](group__usb__type__c.md#gac4eb3955701e40ddabf8b2afae68ea8d)   200 |
|  | Maximum time a port shall wait before it can determine it is attached See Table 4-31 CC Timing. |
| #define | [TC\_T\_PD\_DEBOUNCE\_MIN\_MS](group__usb__type__c.md#ga46e03b71bd69657786755bd716383fe7)   10 |
|  | Minimum time a Sink port shall wait before it can determine it is detached due to the potential for USB PD signaling on CC as described in the state definitions. |
| #define | [TC\_T\_PD\_DEBOUNCE\_MAX\_MS](group__usb__type__c.md#ga4327b09ebf8f27675ac8fc6125ab6bbc)   20 |
|  | Maximum time a Sink port shall wait before it can determine it is detached due to the potential for USB PD signaling on CC as described in the state definitions. |
| #define | [TC\_T\_TRY\_CC\_DEBOUNCE\_MIN\_MS](group__usb__type__c.md#ga21ce86c10d5b0b9e3e7fa08e902d6f77)   10 |
|  | Minimum Time a port shall wait before it can determine it is re-attached during the try-wait process. |
| #define | [TC\_T\_TRY\_CC\_DEBOUNCE\_MAX\_MS](group__usb__type__c.md#ga1b736eb0d37209d95f4e305baaefc1f0)   10 |
|  | Maximum Time a port shall wait before it can determine it is re-attached during the try-wait process. |
| #define | [TC\_T\_ERROR\_RECOVERY\_SELF\_POWERED\_MIN\_MS](group__usb__type__c.md#ga70a063a53fba92977ed35169743368f0)   25 |
|  | Minimum time a self-powered port shall remain in the ErrorRecovery state. |
| #define | [TC\_T\_ERROR\_RECOVERY\_SOURCE\_MIN\_MS](group__usb__type__c.md#gaaee37a1ff25fc71a5c66f04b327f9b04)   240 |
|  | Minimum time a source shall remain in the ErrorRecovery state if it was sourcing VCONN in the previous state. |
| #define | [TC\_T\_RP\_VALUE\_CHANGE\_MIN\_MS](group__usb__type__c.md#ga22273343713c29c84f7ff95fc34e9573)   10 |
|  | Minimum time a Sink port shall wait before it can determine there has been a change in Rp where CC is not BMC Idle or the port is unable to detect BMC Idle. |
| #define | [TC\_T\_RP\_VALUE\_CHANGE\_MAX\_MS](group__usb__type__c.md#gade24fb4955e80390e4f47b86fbce1874)   20 |
|  | Maximum time a Sink port shall wait before it can determine there has been a change in Rp where CC is not BMC Idle or the port is unable to detect BMC Idle. |
| #define | [TC\_T\_SRC\_DISCONNECT\_MIN\_MS](group__usb__type__c.md#ga767c754753786419f50faa2888859cdb)   0 |
|  | Minimum time a Source shall detect the SRC.Open state. |
| #define | [TC\_T\_SRC\_DISCONNECT\_MAX\_MS](group__usb__type__c.md#ga92232c9516031a90da1a6fbd1be03b73)   20 |
|  | Maximum time a Source shall detect the SRC.Open state. |
| #define | [TC\_T\_NO\_TOGGLE\_CONNECT\_MIN\_MS](group__usb__type__c.md#ga5ccab8bbe9c386d47f705551c3b5f918)   0 |
|  | Minimum time to detect connection when neither Port Partner is toggling. |
| #define | [TC\_T\_NO\_TOGGLE\_CONNECT\_MAX\_MS](group__usb__type__c.md#ga7e56e9ff953b5fc425c4304831c19738)   5 |
|  | Maximum time to detect connection when neither Port Partner is toggling. |
| #define | [TC\_T\_ONE\_PORT\_TOGGLE\_CONNECT\_MIN\_MS](group__usb__type__c.md#ga44d9260612a215407d79415b30e63613)   0 |
|  | Minimum time to detect connection when one Port Partner is toggling 0ms … dcSRC.DRP max \* tDRP max + 2 \* tNoToggleConnect). |
| #define | [TC\_T\_ONE\_PORT\_TOGGLE\_CONNECT\_MAX\_MS](group__usb__type__c.md#ga62662057432f68c48dd59be8b28297d4)   80 |
|  | Maximum time to detect connection when one Port Partner is toggling 0ms … dcSRC.DRP max \* tDRP max + 2 \* tNoToggleConnect). |
| #define | [TC\_T\_TWO\_PORT\_TOGGLE\_CONNECT\_MIN\_MS](group__usb__type__c.md#ga96c2bf7f24deb8e8a0d327536a0a023e)   0 |
|  | Minimum time to detect connection when both Port Partners are toggling (0ms … 5 \* tDRP max + 2 \* tNoToggleConnect). |
| #define | [TC\_T\_TWO\_PORT\_TOGGLE\_CONNECT\_MAX\_MS](group__usb__type__c.md#gad911bc40a17b676c8a87d87d51fc0fbf)   510 |
|  | Maximum time to detect connection when both Port Partners are toggling (0ms … 5 \* tDRP max + 2 \* tNoToggleConnect). |
| #define | [TC\_T\_VPDCTDD\_MIN\_US](group__usb__type__c.md#gae2ebe887ccb4f9549d130e85b999062e)   30 |
|  | Minimum time for a Charge-Through VCONN-Powered USB Device to detect that the Charge-Through source has disconnected from CC after VBUS has been removed, transition to CTUnattached.VPD, and re-apply its Rp termination advertising 3.0 A on the host port CC. |
| #define | [TC\_T\_VPDCTDD\_MAX\_MS](group__usb__type__c.md#ga75223d9754d7ce76e302ee2ed40d11ef)   5 |
|  | Maximum time for a Charge-Through VCONN-Powered USB Device to detect that the Charge-Through source has disconnected from CC after VBUS has been removed, transition to CTUnattached.VPD, and re-apply its Rp termination advertising 3.0 A on the host port CC. |
| #define | [TC\_T\_VPDDISABLE\_MIN\_MS](group__usb__type__c.md#ga56ece8323bd0a8e4ce0755e0e9e06f96)   25 |
|  | Minimum time for a Charge-Through VCONN-Powered USB Device shall remain in CTDisabled.VPD state. |

| Enumerations | |
| --- | --- |
| enum | [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) {     [TC\_CC\_VOLT\_OPEN](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca1f4b82ea64d23167df5083fd7550cf05) = 0 , [TC\_CC\_VOLT\_RA](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca17a8d72f4dc6b29e1d4ad35a4f1531ea) = 1 , [TC\_CC\_VOLT\_RD](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca2267bbcda871c265e77228a5fe6342a9) = 2 , [TC\_CC\_VOLT\_RP\_DEF](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca06bd58eb73aa7f097046e7b88fde0293) = 5 ,     [TC\_CC\_VOLT\_RP\_1A5](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca3cc0d3c1ac9775b1b8ba77b87868bc72) = 6 , [TC\_CC\_VOLT\_RP\_3A0](group__usb__type__c.md#gga64e32ec2da97f70fd5b96975317cb92ca3965e449dbcc8ca6e87d72cd5a73f0ca) = 7   } |
|  | CC Voltage status. [More...](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) |
| enum | [tc\_vbus\_level](group__usb__type__c.md#ga015455a6c5620dfc96cfb713bbb72161) { [TC\_VBUS\_SAFE0V](group__usb__type__c.md#gga015455a6c5620dfc96cfb713bbb72161a86bf4c0568d7a7ec89180e8e36c91827) = 0 , [TC\_VBUS\_PRESENT](group__usb__type__c.md#gga015455a6c5620dfc96cfb713bbb72161a33f8f0dac47bfaffe331553cd42495f5) = 1 , [TC\_VBUS\_REMOVED](group__usb__type__c.md#gga015455a6c5620dfc96cfb713bbb72161a84aaa14f5d6dd4b1bf52564af73f24bc) = 2 } |
|  | VBUS level voltages. [More...](group__usb__type__c.md#ga015455a6c5620dfc96cfb713bbb72161) |
| enum | [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) { [TC\_RP\_USB](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5a22d5e50479ca672f0469af9006b4f4bb) = 0 , [TC\_RP\_1A5](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5a1c74df7e2b6bbe75d8c61ca4a7202a28) = 1 , [TC\_RP\_3A0](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5afa7eda9742f3670a90736a52620cfe3c) = 2 , [TC\_RP\_RESERVED](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5a215508ac427e2cc53478e5f096a400d1) = 3 } |
|  | Pull-Up resistor values. [More...](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5) |
| enum | [tc\_cc\_pull](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada) {     [TC\_CC\_RA](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaaf52a9f9d10c81fca5b048ad2230cf1e8) = 0 , [TC\_CC\_RP](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaa7a0a6a716cb42af3a572f43bedc2a322) = 1 , [TC\_CC\_RD](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaa60a4e008afce1c9395a0fb6d34767c6e) = 2 , [TC\_CC\_OPEN](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaa4859548c59439c79e3ad080e1fa07fa8) = 3 ,     [TC\_RA\_RD](group__usb__type__c.md#gga0200c820510eb786f3ca30a9b5f7aadaa95c81809d680f28281e9dcaef4fff35e) = 4   } |
|  | CC pull resistors. [More...](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada) |
| enum | [tc\_cable\_plug](group__usb__type__c.md#ga8707ac194510396d55a40887673b53ca) { [PD\_PLUG\_FROM\_DFP\_UFP](group__usb__type__c.md#gga8707ac194510396d55a40887673b53caad1092c45d3fad497dbafe15fd9f1c3b3) = 0 , [PD\_PLUG\_FROM\_CABLE\_VPD](group__usb__type__c.md#gga8707ac194510396d55a40887673b53caa49960a4dee1da0c7330cce2b13c4c0ed) = 1 } |
|  | Cable plug. [More...](group__usb__type__c.md#ga8707ac194510396d55a40887673b53ca) |
| enum | [tc\_power\_role](group__usb__type__c.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d) { [TC\_ROLE\_SINK](group__usb__type__c.md#ggaa6dda0612045b5f55b9d8ba63d2b9f9da0023468cf2e977c8372899e6f1a0aafb) = 0 , [TC\_ROLE\_SOURCE](group__usb__type__c.md#ggaa6dda0612045b5f55b9d8ba63d2b9f9da1b8caf27ae76de5ea874b0e52adc4cf1) = 1 } |
|  | Power Delivery Power Role. [More...](group__usb__type__c.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d) |
| enum | [tc\_data\_role](group__usb__type__c.md#ga6b98bbe238e62cfd5531688494a63de2) { [TC\_ROLE\_UFP](group__usb__type__c.md#gga6b98bbe238e62cfd5531688494a63de2a9472c4319bf0be6937436e1602c7b414) = 0 , [TC\_ROLE\_DFP](group__usb__type__c.md#gga6b98bbe238e62cfd5531688494a63de2a812112dccb0c3d8dd555d351a7f5b9e1) = 1 , [TC\_ROLE\_DISCONNECTED](group__usb__type__c.md#gga6b98bbe238e62cfd5531688494a63de2a155c3d22f151d83899f46e516e88a058) = 2 } |
|  | Power Delivery Data Role. [More...](group__usb__type__c.md#ga6b98bbe238e62cfd5531688494a63de2) |
| enum | [tc\_cc\_polarity](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) { [TC\_POLARITY\_CC1](group__usb__type__c.md#ggac5b4b58840c9b076a869a5816ba100dba1ace08cbeb63866305ccfb0c3bf338c2) = 0 , [TC\_POLARITY\_CC2](group__usb__type__c.md#ggac5b4b58840c9b076a869a5816ba100dbae3ad03c80e84e32f8974a14e815ed910) = 1 } |
|  | Polarity of the CC lines. [More...](group__usb__type__c.md#gac5b4b58840c9b076a869a5816ba100db) |
| enum | [tc\_cc\_states](group__usb__type__c.md#ga5bb2cfcf3ab60423048db38103657197) {     [TC\_CC\_NONE](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a21cf3890c4a2fa6ee9f137f2b22e51f0) = 0 , [TC\_CC\_UFP\_NONE](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a90544a6af90af7722cec8ffe83f752f0) = 1 , [TC\_CC\_UFP\_AUDIO\_ACC](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a4b841a1438a120652ab78fb3ae2c7dea) = 2 , [TC\_CC\_UFP\_DEBUG\_ACC](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197aaba130e5d3d999794eb87e2b8a09cf78) = 3 ,     [TC\_CC\_UFP\_ATTACHED](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a0cfcabb4325e4b59213002aaeda75524) = 4 , [TC\_CC\_DFP\_ATTACHED](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a950c6ff65a4af5db2f1fdab3383489ba) = 5 , [TC\_CC\_DFP\_DEBUG\_ACC](group__usb__type__c.md#gga5bb2cfcf3ab60423048db38103657197a8821754209b4cd977b2c97d43957166c) = 6   } |
|  | Possible port partner connections based on CC line states. [More...](group__usb__type__c.md#ga5bb2cfcf3ab60423048db38103657197) |

## Detailed Description

USB Type-C Cable and Connector API used for USB-C drivers.

The information in this file was taken from the USB Type-C Cable and Connector Specification Release 2.1

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb\_c](dir_a57818ecbbcbfd5f3cb9a612ed0259e0.md)
- [usbc\_tc.h](usbc__tc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
