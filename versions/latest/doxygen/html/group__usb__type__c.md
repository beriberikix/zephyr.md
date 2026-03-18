---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__usb__type__c.html
original_path: doxygen/html/group__usb__type__c.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

USB Type-C

[Device Driver APIs](group__io__interfaces.md)

USB Type-C.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [TC\_V\_SINK\_DISCONNECT\_MIN\_MV](#ga025aeca5768435b245ecb9fe8bfa29c8)   800 |
|  | VBUS minimum for a sink disconnect detection. |
| #define | [TC\_V\_SINK\_DISCONNECT\_MAX\_MV](#ga151c5852b9d2ad3f6f7f0869505e854b)   3670 |
|  | VBUS maximum for a sink disconnect detection. |
| #define | [TC\_T\_VBUS\_ON\_MAX\_MS](#gace546c362f92ed1ba0455a5d8006357c)   275 |
|  | From entry to Attached.SRC until VBUS reaches the minimum vSafe5V threshold as measured at the source’s receptacle See Table 4-29 VBUS and VCONN Timing Parameters. |
| #define | [TC\_T\_VBUS\_OFF\_MAX\_MS](#ga2d6440c7b480ee75ccadf8242e29e7e9)   650 |
|  | From the time the Sink is detached until the Source removes VBUS and reaches vSafe0V (See USB PD). |
| #define | [TC\_T\_VCONN\_ON\_MAX\_MS](#gaf2cbadac415eedae8c4db3dc91f3623b)   2 |
|  | From the time the Source supplied VBUS in the Attached.SRC state. |
| #define | [TC\_T\_VCONN\_ON\_PA\_MAX\_MS](#ga24837587c589d85bc48bed2a6815798d)   100 |
|  | From the time a Sink with accessory support enters the PoweredAccessory state until the Sink sources minimum VCONN voltage (see Table 4-5) See Table 4-29 VBUS and VCONN Timing Parameters. |
| #define | [TC\_T\_VCONN\_OFF\_MAX\_MS](#ga2f347359b4ffc4478338cbbc8a62d4d9)   35 |
|  | From the time that a Sink is detached or as directed until the VCONN supply is disconnected. |
| #define | [TC\_T\_SINK\_ADJ\_MAX\_MS](#gaa1291eb2b50b59a9746ffe0658d60258)   60 |
|  | Response time for a Sink to adjust its current consumption to be in the specified range due to a change in USB Type-C Current advertisement See Table 4-29 VBUS and VCONN Timing Parameters. |
| #define | [TC\_T\_DRP\_MIN\_MS](#gab042a018fbc99a402ab23371c3d6fe47)   50 |
|  | The minimum period a DRP shall complete a Source to Sink and back advertisement See Table 4-30 DRP Timing Parameters. |
| #define | [TC\_T\_DRP\_MAX\_MS](#gaba34e5687c2e12984629a9297f0e7813)   100 |
|  | The maximum period a DRP shall complete a Source to Sink and back advertisement See Table 4-30 DRP Timing Parameters. |
| #define | [TC\_T\_DRP\_TRANSITION\_MIN\_MS](#ga6ab07167512c79d9587d547902443049)   0 |
|  | The minimum time a DRP shall complete transitions between Source and Sink roles during role resolution See Table 4-30 DRP Timing Parameters. |
| #define | [TC\_T\_DRP\_TRANSITION\_MAX\_MS](#gae1e9780a30b644a1f15463cba216e385)   1 |
|  | The maximum time a DRP shall complete transitions between Source and Sink roles during role resolution See Table 4-30 DRP Timing Parameters. |
| #define | [TC\_T\_DRP\_TRY\_MIN\_MS](#ga1ee8d43885ebc26a2f4da640d5758188)   75 |
|  | Minimum wait time associated with the Try.SRC state. |
| #define | [TC\_T\_DRP\_TRY\_MAX\_MS](#ga95cd5ac306f2d27440b980593c759f07)   150 |
|  | Maximum wait time associated with the Try.SRC state. |
| #define | [TC\_T\_DRP\_TRY\_WAIT\_MIN\_MS](#gae19a1dc5b950495866359deef2cd6c7c)   400 |
|  | Minimum wait time associated with the Try.SNK state. |
| #define | [TC\_T\_DRP\_TRY\_WAIT\_MAX\_MS](#ga0eb5b996e1678f3830c38584f84a6268)   800 |
|  | Maximum wait time associated with the Try.SNK state. |
| #define | [TC\_T\_TRY\_TIMEOUT\_MIN\_MS](#ga45be1dbb0a9ad2e9a9b0549f953cb8c2)   550 |
|  | Minimum timeout for transition from Try.SRC to TryWait.SNK. |
| #define | [TC\_T\_TRY\_TIMEOUT\_MAX\_MS](#gae3e98e8acbfb5fa7f398dea64265cb0a)   1100 |
|  | Maximum timeout for transition from Try.SRC to TryWait.SNK. |
| #define | [TC\_T\_VPD\_DETACH\_MIN\_MS](#ga50a154595c40bba3e46751f6f46df848)   10 |
|  | Minimum Time for a DRP to detect that the connected Charge-Through VCONNPowered USB Device has been detached, after VBUS has been removed. |
| #define | [TC\_T\_VPD\_DETACH\_MAX\_MS](#ga33b792a38351081f316e6f854710a96e)   20 |
|  | Maximum Time for a DRP to detect that the connected Charge-Through VCONNPowered USB Device has been detached, after VBUS has been removed. |
| #define | [TC\_T\_CC\_DEBOUNCE\_MIN\_MS](#gae059acba0f01f24cb682ee2c3ded59d9)   100 |
|  | Minimum time a port shall wait before it can determine it is attached See Table 4-31 CC Timing. |
| #define | [TC\_T\_CC\_DEBOUNCE\_MAX\_MS](#gac4eb3955701e40ddabf8b2afae68ea8d)   200 |
|  | Maximum time a port shall wait before it can determine it is attached See Table 4-31 CC Timing. |
| #define | [TC\_T\_PD\_DEBOUNCE\_MIN\_MS](#ga46e03b71bd69657786755bd716383fe7)   10 |
|  | Minimum time a Sink port shall wait before it can determine it is detached due to the potential for USB PD signaling on CC as described in the state definitions. |
| #define | [TC\_T\_PD\_DEBOUNCE\_MAX\_MS](#ga4327b09ebf8f27675ac8fc6125ab6bbc)   20 |
|  | Maximum time a Sink port shall wait before it can determine it is detached due to the potential for USB PD signaling on CC as described in the state definitions. |
| #define | [TC\_T\_TRY\_CC\_DEBOUNCE\_MIN\_MS](#ga21ce86c10d5b0b9e3e7fa08e902d6f77)   10 |
|  | Minimum Time a port shall wait before it can determine it is re-attached during the try-wait process. |
| #define | [TC\_T\_TRY\_CC\_DEBOUNCE\_MAX\_MS](#ga1b736eb0d37209d95f4e305baaefc1f0)   10 |
|  | Maximum Time a port shall wait before it can determine it is re-attached during the try-wait process. |
| #define | [TC\_T\_ERROR\_RECOVERY\_SELF\_POWERED\_MIN\_MS](#ga70a063a53fba92977ed35169743368f0)   25 |
|  | Minimum time a self-powered port shall remain in the ErrorRecovery state. |
| #define | [TC\_T\_ERROR\_RECOVERY\_SOURCE\_MIN\_MS](#gaaee37a1ff25fc71a5c66f04b327f9b04)   240 |
|  | Minimum time a source shall remain in the ErrorRecovery state if it was sourcing VCONN in the previous state. |
| #define | [TC\_T\_RP\_VALUE\_CHANGE\_MIN\_MS](#ga22273343713c29c84f7ff95fc34e9573)   10 |
|  | Minimum time a Sink port shall wait before it can determine there has been a change in Rp where CC is not BMC Idle or the port is unable to detect BMC Idle. |
| #define | [TC\_T\_RP\_VALUE\_CHANGE\_MAX\_MS](#gade24fb4955e80390e4f47b86fbce1874)   20 |
|  | Maximum time a Sink port shall wait before it can determine there has been a change in Rp where CC is not BMC Idle or the port is unable to detect BMC Idle. |
| #define | [TC\_T\_SRC\_DISCONNECT\_MIN\_MS](#ga767c754753786419f50faa2888859cdb)   0 |
|  | Minimum time a Source shall detect the SRC.Open state. |
| #define | [TC\_T\_SRC\_DISCONNECT\_MAX\_MS](#ga92232c9516031a90da1a6fbd1be03b73)   20 |
|  | Maximum time a Source shall detect the SRC.Open state. |
| #define | [TC\_T\_NO\_TOGGLE\_CONNECT\_MIN\_MS](#ga5ccab8bbe9c386d47f705551c3b5f918)   0 |
|  | Minimum time to detect connection when neither Port Partner is toggling. |
| #define | [TC\_T\_NO\_TOGGLE\_CONNECT\_MAX\_MS](#ga7e56e9ff953b5fc425c4304831c19738)   5 |
|  | Maximum time to detect connection when neither Port Partner is toggling. |
| #define | [TC\_T\_ONE\_PORT\_TOGGLE\_CONNECT\_MIN\_MS](#ga44d9260612a215407d79415b30e63613)   0 |
|  | Minimum time to detect connection when one Port Partner is toggling 0ms … dcSRC.DRP max \* tDRP max + 2 \* tNoToggleConnect). |
| #define | [TC\_T\_ONE\_PORT\_TOGGLE\_CONNECT\_MAX\_MS](#ga62662057432f68c48dd59be8b28297d4)   80 |
|  | Maximum time to detect connection when one Port Partner is toggling 0ms … dcSRC.DRP max \* tDRP max + 2 \* tNoToggleConnect). |
| #define | [TC\_T\_TWO\_PORT\_TOGGLE\_CONNECT\_MIN\_MS](#ga96c2bf7f24deb8e8a0d327536a0a023e)   0 |
|  | Minimum time to detect connection when both Port Partners are toggling (0ms … 5 \* tDRP max + 2 \* tNoToggleConnect). |
| #define | [TC\_T\_TWO\_PORT\_TOGGLE\_CONNECT\_MAX\_MS](#gad911bc40a17b676c8a87d87d51fc0fbf)   510 |
|  | Maximum time to detect connection when both Port Partners are toggling (0ms … 5 \* tDRP max + 2 \* tNoToggleConnect). |
| #define | [TC\_T\_VPDCTDD\_MIN\_US](#gae2ebe887ccb4f9549d130e85b999062e)   30 |
|  | Minimum time for a Charge-Through VCONN-Powered USB Device to detect that the Charge-Through source has disconnected from CC after VBUS has been removed, transition to CTUnattached.VPD, and re-apply its Rp termination advertising 3.0 A on the host port CC. |
| #define | [TC\_T\_VPDCTDD\_MAX\_MS](#ga75223d9754d7ce76e302ee2ed40d11ef)   5 |
|  | Maximum time for a Charge-Through VCONN-Powered USB Device to detect that the Charge-Through source has disconnected from CC after VBUS has been removed, transition to CTUnattached.VPD, and re-apply its Rp termination advertising 3.0 A on the host port CC. |
| #define | [TC\_T\_VPDDISABLE\_MIN\_MS](#ga56ece8323bd0a8e4ce0755e0e9e06f96)   25 |
|  | Minimum time for a Charge-Through VCONN-Powered USB Device shall remain in CTDisabled.VPD state. |

| Enumerations | |
| --- | --- |
| enum | [tc\_cc\_voltage\_state](#ga64e32ec2da97f70fd5b96975317cb92c) {     [TC\_CC\_VOLT\_OPEN](#gga64e32ec2da97f70fd5b96975317cb92ca1f4b82ea64d23167df5083fd7550cf05) = 0 , [TC\_CC\_VOLT\_RA](#gga64e32ec2da97f70fd5b96975317cb92ca17a8d72f4dc6b29e1d4ad35a4f1531ea) = 1 , [TC\_CC\_VOLT\_RD](#gga64e32ec2da97f70fd5b96975317cb92ca2267bbcda871c265e77228a5fe6342a9) = 2 , [TC\_CC\_VOLT\_RP\_DEF](#gga64e32ec2da97f70fd5b96975317cb92ca06bd58eb73aa7f097046e7b88fde0293) = 5 ,     [TC\_CC\_VOLT\_RP\_1A5](#gga64e32ec2da97f70fd5b96975317cb92ca3cc0d3c1ac9775b1b8ba77b87868bc72) = 6 , [TC\_CC\_VOLT\_RP\_3A0](#gga64e32ec2da97f70fd5b96975317cb92ca3965e449dbcc8ca6e87d72cd5a73f0ca) = 7   } |
|  | CC Voltage status. [More...](#ga64e32ec2da97f70fd5b96975317cb92c) |
| enum | [tc\_vbus\_level](#ga015455a6c5620dfc96cfb713bbb72161) { [TC\_VBUS\_SAFE0V](#gga015455a6c5620dfc96cfb713bbb72161a86bf4c0568d7a7ec89180e8e36c91827) = 0 , [TC\_VBUS\_PRESENT](#gga015455a6c5620dfc96cfb713bbb72161a33f8f0dac47bfaffe331553cd42495f5) = 1 , [TC\_VBUS\_REMOVED](#gga015455a6c5620dfc96cfb713bbb72161a84aaa14f5d6dd4b1bf52564af73f24bc) = 2 } |
|  | VBUS level voltages. [More...](#ga015455a6c5620dfc96cfb713bbb72161) |
| enum | [tc\_rp\_value](#ga4e0eec97f7c5c97b87eff9561deea2d5) { [TC\_RP\_USB](#gga4e0eec97f7c5c97b87eff9561deea2d5a22d5e50479ca672f0469af9006b4f4bb) = 0 , [TC\_RP\_1A5](#gga4e0eec97f7c5c97b87eff9561deea2d5a1c74df7e2b6bbe75d8c61ca4a7202a28) = 1 , [TC\_RP\_3A0](#gga4e0eec97f7c5c97b87eff9561deea2d5afa7eda9742f3670a90736a52620cfe3c) = 2 , [TC\_RP\_RESERVED](#gga4e0eec97f7c5c97b87eff9561deea2d5a215508ac427e2cc53478e5f096a400d1) = 3 } |
|  | Pull-Up resistor values. [More...](#ga4e0eec97f7c5c97b87eff9561deea2d5) |
| enum | [tc\_cc\_pull](#ga0200c820510eb786f3ca30a9b5f7aada) {     [TC\_CC\_RA](#gga0200c820510eb786f3ca30a9b5f7aadaaf52a9f9d10c81fca5b048ad2230cf1e8) = 0 , [TC\_CC\_RP](#gga0200c820510eb786f3ca30a9b5f7aadaa7a0a6a716cb42af3a572f43bedc2a322) = 1 , [TC\_CC\_RD](#gga0200c820510eb786f3ca30a9b5f7aadaa60a4e008afce1c9395a0fb6d34767c6e) = 2 , [TC\_CC\_OPEN](#gga0200c820510eb786f3ca30a9b5f7aadaa4859548c59439c79e3ad080e1fa07fa8) = 3 ,     [TC\_RA\_RD](#gga0200c820510eb786f3ca30a9b5f7aadaa95c81809d680f28281e9dcaef4fff35e) = 4   } |
|  | CC pull resistors. [More...](#ga0200c820510eb786f3ca30a9b5f7aada) |
| enum | [tc\_cable\_plug](#ga8707ac194510396d55a40887673b53ca) { [PD\_PLUG\_FROM\_DFP\_UFP](#gga8707ac194510396d55a40887673b53caad1092c45d3fad497dbafe15fd9f1c3b3) = 0 , [PD\_PLUG\_FROM\_CABLE\_VPD](#gga8707ac194510396d55a40887673b53caa49960a4dee1da0c7330cce2b13c4c0ed) = 1 } |
|  | Cable plug. [More...](#ga8707ac194510396d55a40887673b53ca) |
| enum | [tc\_power\_role](#gaa6dda0612045b5f55b9d8ba63d2b9f9d) { [TC\_ROLE\_SINK](#ggaa6dda0612045b5f55b9d8ba63d2b9f9da0023468cf2e977c8372899e6f1a0aafb) = 0 , [TC\_ROLE\_SOURCE](#ggaa6dda0612045b5f55b9d8ba63d2b9f9da1b8caf27ae76de5ea874b0e52adc4cf1) = 1 } |
|  | Power Delivery Power Role. [More...](#gaa6dda0612045b5f55b9d8ba63d2b9f9d) |
| enum | [tc\_data\_role](#ga6b98bbe238e62cfd5531688494a63de2) { [TC\_ROLE\_UFP](#gga6b98bbe238e62cfd5531688494a63de2a9472c4319bf0be6937436e1602c7b414) = 0 , [TC\_ROLE\_DFP](#gga6b98bbe238e62cfd5531688494a63de2a812112dccb0c3d8dd555d351a7f5b9e1) = 1 , [TC\_ROLE\_DISCONNECTED](#gga6b98bbe238e62cfd5531688494a63de2a155c3d22f151d83899f46e516e88a058) = 2 } |
|  | Power Delivery Data Role. [More...](#ga6b98bbe238e62cfd5531688494a63de2) |
| enum | [tc\_cc\_polarity](#gac5b4b58840c9b076a869a5816ba100db) { [TC\_POLARITY\_CC1](#ggac5b4b58840c9b076a869a5816ba100dba1ace08cbeb63866305ccfb0c3bf338c2) = 0 , [TC\_POLARITY\_CC2](#ggac5b4b58840c9b076a869a5816ba100dbae3ad03c80e84e32f8974a14e815ed910) = 1 } |
|  | Polarity of the CC lines. [More...](#gac5b4b58840c9b076a869a5816ba100db) |
| enum | [tc\_cc\_states](#ga5bb2cfcf3ab60423048db38103657197) {     [TC\_CC\_NONE](#gga5bb2cfcf3ab60423048db38103657197a21cf3890c4a2fa6ee9f137f2b22e51f0) = 0 , [TC\_CC\_UFP\_NONE](#gga5bb2cfcf3ab60423048db38103657197a90544a6af90af7722cec8ffe83f752f0) = 1 , [TC\_CC\_UFP\_AUDIO\_ACC](#gga5bb2cfcf3ab60423048db38103657197a4b841a1438a120652ab78fb3ae2c7dea) = 2 , [TC\_CC\_UFP\_DEBUG\_ACC](#gga5bb2cfcf3ab60423048db38103657197aaba130e5d3d999794eb87e2b8a09cf78) = 3 ,     [TC\_CC\_UFP\_ATTACHED](#gga5bb2cfcf3ab60423048db38103657197a0cfcabb4325e4b59213002aaeda75524) = 4 , [TC\_CC\_DFP\_ATTACHED](#gga5bb2cfcf3ab60423048db38103657197a950c6ff65a4af5db2f1fdab3383489ba) = 5 , [TC\_CC\_DFP\_DEBUG\_ACC](#gga5bb2cfcf3ab60423048db38103657197a8821754209b4cd977b2c97d43957166c) = 6   } |
|  | Possible port partner connections based on CC line states. [More...](#ga5bb2cfcf3ab60423048db38103657197) |

## Detailed Description

USB Type-C.

## Macro Definition Documentation

## [◆ ](#gac4eb3955701e40ddabf8b2afae68ea8d)TC\_T\_CC\_DEBOUNCE\_MAX\_MS

| #define TC\_T\_CC\_DEBOUNCE\_MAX\_MS   200 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Maximum time a port shall wait before it can determine it is attached See Table 4-31 CC Timing.

## [◆ ](#gae059acba0f01f24cb682ee2c3ded59d9)TC\_T\_CC\_DEBOUNCE\_MIN\_MS

| #define TC\_T\_CC\_DEBOUNCE\_MIN\_MS   100 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Minimum time a port shall wait before it can determine it is attached See Table 4-31 CC Timing.

## [◆ ](#gaba34e5687c2e12984629a9297f0e7813)TC\_T\_DRP\_MAX\_MS

| #define TC\_T\_DRP\_MAX\_MS   100 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

The maximum period a DRP shall complete a Source to Sink and back advertisement See Table 4-30 DRP Timing Parameters.

## [◆ ](#gab042a018fbc99a402ab23371c3d6fe47)TC\_T\_DRP\_MIN\_MS

| #define TC\_T\_DRP\_MIN\_MS   50 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

The minimum period a DRP shall complete a Source to Sink and back advertisement See Table 4-30 DRP Timing Parameters.

## [◆ ](#gae1e9780a30b644a1f15463cba216e385)TC\_T\_DRP\_TRANSITION\_MAX\_MS

| #define TC\_T\_DRP\_TRANSITION\_MAX\_MS   1 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

The maximum time a DRP shall complete transitions between Source and Sink roles during role resolution See Table 4-30 DRP Timing Parameters.

## [◆ ](#ga6ab07167512c79d9587d547902443049)TC\_T\_DRP\_TRANSITION\_MIN\_MS

| #define TC\_T\_DRP\_TRANSITION\_MIN\_MS   0 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

The minimum time a DRP shall complete transitions between Source and Sink roles during role resolution See Table 4-30 DRP Timing Parameters.

## [◆ ](#ga95cd5ac306f2d27440b980593c759f07)TC\_T\_DRP\_TRY\_MAX\_MS

| #define TC\_T\_DRP\_TRY\_MAX\_MS   150 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Maximum wait time associated with the Try.SRC state.

See Table 4-30 DRP Timing Parameters

## [◆ ](#ga1ee8d43885ebc26a2f4da640d5758188)TC\_T\_DRP\_TRY\_MIN\_MS

| #define TC\_T\_DRP\_TRY\_MIN\_MS   75 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Minimum wait time associated with the Try.SRC state.

See Table 4-30 DRP Timing Parameters

## [◆ ](#ga0eb5b996e1678f3830c38584f84a6268)TC\_T\_DRP\_TRY\_WAIT\_MAX\_MS

| #define TC\_T\_DRP\_TRY\_WAIT\_MAX\_MS   800 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Maximum wait time associated with the Try.SNK state.

See Table 4-30 DRP Timing Parameters

## [◆ ](#gae19a1dc5b950495866359deef2cd6c7c)TC\_T\_DRP\_TRY\_WAIT\_MIN\_MS

| #define TC\_T\_DRP\_TRY\_WAIT\_MIN\_MS   400 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Minimum wait time associated with the Try.SNK state.

See Table 4-30 DRP Timing Parameters

## [◆ ](#ga70a063a53fba92977ed35169743368f0)TC\_T\_ERROR\_RECOVERY\_SELF\_POWERED\_MIN\_MS

| #define TC\_T\_ERROR\_RECOVERY\_SELF\_POWERED\_MIN\_MS   25 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Minimum time a self-powered port shall remain in the ErrorRecovery state.

See Table 4-31 CC Timing

## [◆ ](#gaaee37a1ff25fc71a5c66f04b327f9b04)TC\_T\_ERROR\_RECOVERY\_SOURCE\_MIN\_MS

| #define TC\_T\_ERROR\_RECOVERY\_SOURCE\_MIN\_MS   240 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Minimum time a source shall remain in the ErrorRecovery state if it was sourcing VCONN in the previous state.

See Table 4-31 CC Timing

## [◆ ](#ga7e56e9ff953b5fc425c4304831c19738)TC\_T\_NO\_TOGGLE\_CONNECT\_MAX\_MS

| #define TC\_T\_NO\_TOGGLE\_CONNECT\_MAX\_MS   5 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Maximum time to detect connection when neither Port Partner is toggling.

See Table 4-31 CC Timing

## [◆ ](#ga5ccab8bbe9c386d47f705551c3b5f918)TC\_T\_NO\_TOGGLE\_CONNECT\_MIN\_MS

| #define TC\_T\_NO\_TOGGLE\_CONNECT\_MIN\_MS   0 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Minimum time to detect connection when neither Port Partner is toggling.

See Table 4-31 CC Timing

## [◆ ](#ga62662057432f68c48dd59be8b28297d4)TC\_T\_ONE\_PORT\_TOGGLE\_CONNECT\_MAX\_MS

| #define TC\_T\_ONE\_PORT\_TOGGLE\_CONNECT\_MAX\_MS   80 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Maximum time to detect connection when one Port Partner is toggling 0ms … dcSRC.DRP max \* tDRP max + 2 \* tNoToggleConnect).

See Table 4-31 CC Timing

## [◆ ](#ga44d9260612a215407d79415b30e63613)TC\_T\_ONE\_PORT\_TOGGLE\_CONNECT\_MIN\_MS

| #define TC\_T\_ONE\_PORT\_TOGGLE\_CONNECT\_MIN\_MS   0 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Minimum time to detect connection when one Port Partner is toggling 0ms … dcSRC.DRP max \* tDRP max + 2 \* tNoToggleConnect).

See Table 4-31 CC Timing

## [◆ ](#ga4327b09ebf8f27675ac8fc6125ab6bbc)TC\_T\_PD\_DEBOUNCE\_MAX\_MS

| #define TC\_T\_PD\_DEBOUNCE\_MAX\_MS   20 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Maximum time a Sink port shall wait before it can determine it is detached due to the potential for USB PD signaling on CC as described in the state definitions.

See Table 4-31 CC Timing

## [◆ ](#ga46e03b71bd69657786755bd716383fe7)TC\_T\_PD\_DEBOUNCE\_MIN\_MS

| #define TC\_T\_PD\_DEBOUNCE\_MIN\_MS   10 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Minimum time a Sink port shall wait before it can determine it is detached due to the potential for USB PD signaling on CC as described in the state definitions.

See Table 4-31 CC Timing

## [◆ ](#gade24fb4955e80390e4f47b86fbce1874)TC\_T\_RP\_VALUE\_CHANGE\_MAX\_MS

| #define TC\_T\_RP\_VALUE\_CHANGE\_MAX\_MS   20 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Maximum time a Sink port shall wait before it can determine there has been a change in Rp where CC is not BMC Idle or the port is unable to detect BMC Idle.

See Table 4-31 CC Timing

## [◆ ](#ga22273343713c29c84f7ff95fc34e9573)TC\_T\_RP\_VALUE\_CHANGE\_MIN\_MS

| #define TC\_T\_RP\_VALUE\_CHANGE\_MIN\_MS   10 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Minimum time a Sink port shall wait before it can determine there has been a change in Rp where CC is not BMC Idle or the port is unable to detect BMC Idle.

See Table 4-31 CC Timing

## [◆ ](#gaa1291eb2b50b59a9746ffe0658d60258)TC\_T\_SINK\_ADJ\_MAX\_MS

| #define TC\_T\_SINK\_ADJ\_MAX\_MS   60 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Response time for a Sink to adjust its current consumption to be in the specified range due to a change in USB Type-C Current advertisement See Table 4-29 VBUS and VCONN Timing Parameters.

## [◆ ](#ga92232c9516031a90da1a6fbd1be03b73)TC\_T\_SRC\_DISCONNECT\_MAX\_MS

| #define TC\_T\_SRC\_DISCONNECT\_MAX\_MS   20 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Maximum time a Source shall detect the SRC.Open state.

The Source should detect the SRC.Open state as quickly as practical. See Table 4-31 CC Timing

## [◆ ](#ga767c754753786419f50faa2888859cdb)TC\_T\_SRC\_DISCONNECT\_MIN\_MS

| #define TC\_T\_SRC\_DISCONNECT\_MIN\_MS   0 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Minimum time a Source shall detect the SRC.Open state.

The Source should detect the SRC.Open state as quickly as practical. See Table 4-31 CC Timing

## [◆ ](#ga1b736eb0d37209d95f4e305baaefc1f0)TC\_T\_TRY\_CC\_DEBOUNCE\_MAX\_MS

| #define TC\_T\_TRY\_CC\_DEBOUNCE\_MAX\_MS   10 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Maximum Time a port shall wait before it can determine it is re-attached during the try-wait process.

See Table 4-31 CC Timing

## [◆ ](#ga21ce86c10d5b0b9e3e7fa08e902d6f77)TC\_T\_TRY\_CC\_DEBOUNCE\_MIN\_MS

| #define TC\_T\_TRY\_CC\_DEBOUNCE\_MIN\_MS   10 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Minimum Time a port shall wait before it can determine it is re-attached during the try-wait process.

See Table 4-31 CC Timing

## [◆ ](#gae3e98e8acbfb5fa7f398dea64265cb0a)TC\_T\_TRY\_TIMEOUT\_MAX\_MS

| #define TC\_T\_TRY\_TIMEOUT\_MAX\_MS   1100 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Maximum timeout for transition from Try.SRC to TryWait.SNK.

See Table 4-30 DRP Timing Parameters

## [◆ ](#ga45be1dbb0a9ad2e9a9b0549f953cb8c2)TC\_T\_TRY\_TIMEOUT\_MIN\_MS

| #define TC\_T\_TRY\_TIMEOUT\_MIN\_MS   550 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Minimum timeout for transition from Try.SRC to TryWait.SNK.

See Table 4-30 DRP Timing Parameters

## [◆ ](#gad911bc40a17b676c8a87d87d51fc0fbf)TC\_T\_TWO\_PORT\_TOGGLE\_CONNECT\_MAX\_MS

| #define TC\_T\_TWO\_PORT\_TOGGLE\_CONNECT\_MAX\_MS   510 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Maximum time to detect connection when both Port Partners are toggling (0ms … 5 \* tDRP max + 2 \* tNoToggleConnect).

See Table 4-31 CC Timing

## [◆ ](#ga96c2bf7f24deb8e8a0d327536a0a023e)TC\_T\_TWO\_PORT\_TOGGLE\_CONNECT\_MIN\_MS

| #define TC\_T\_TWO\_PORT\_TOGGLE\_CONNECT\_MIN\_MS   0 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Minimum time to detect connection when both Port Partners are toggling (0ms … 5 \* tDRP max + 2 \* tNoToggleConnect).

See Table 4-31 CC Timing

## [◆ ](#ga2d6440c7b480ee75ccadf8242e29e7e9)TC\_T\_VBUS\_OFF\_MAX\_MS

| #define TC\_T\_VBUS\_OFF\_MAX\_MS   650 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

From the time the Sink is detached until the Source removes VBUS and reaches vSafe0V (See USB PD).

See Table 4-29 VBUS and VCONN Timing Parameters

## [◆ ](#gace546c362f92ed1ba0455a5d8006357c)TC\_T\_VBUS\_ON\_MAX\_MS

| #define TC\_T\_VBUS\_ON\_MAX\_MS   275 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

From entry to Attached.SRC until VBUS reaches the minimum vSafe5V threshold as measured at the source’s receptacle See Table 4-29 VBUS and VCONN Timing Parameters.

## [◆ ](#ga2f347359b4ffc4478338cbbc8a62d4d9)TC\_T\_VCONN\_OFF\_MAX\_MS

| #define TC\_T\_VCONN\_OFF\_MAX\_MS   35 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

From the time that a Sink is detached or as directed until the VCONN supply is disconnected.

See Table 4-29 VBUS and VCONN Timing Parameters

## [◆ ](#gaf2cbadac415eedae8c4db3dc91f3623b)TC\_T\_VCONN\_ON\_MAX\_MS

| #define TC\_T\_VCONN\_ON\_MAX\_MS   2 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

From the time the Source supplied VBUS in the Attached.SRC state.

See Table 4-29 VBUS and VCONN Timing Parameters

## [◆ ](#ga24837587c589d85bc48bed2a6815798d)TC\_T\_VCONN\_ON\_PA\_MAX\_MS

| #define TC\_T\_VCONN\_ON\_PA\_MAX\_MS   100 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

From the time a Sink with accessory support enters the PoweredAccessory state until the Sink sources minimum VCONN voltage (see Table 4-5) See Table 4-29 VBUS and VCONN Timing Parameters.

## [◆ ](#ga33b792a38351081f316e6f854710a96e)TC\_T\_VPD\_DETACH\_MAX\_MS

| #define TC\_T\_VPD\_DETACH\_MAX\_MS   20 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Maximum Time for a DRP to detect that the connected Charge-Through VCONNPowered USB Device has been detached, after VBUS has been removed.

See Table 4-30 DRP Timing Parameters

## [◆ ](#ga50a154595c40bba3e46751f6f46df848)TC\_T\_VPD\_DETACH\_MIN\_MS

| #define TC\_T\_VPD\_DETACH\_MIN\_MS   10 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Minimum Time for a DRP to detect that the connected Charge-Through VCONNPowered USB Device has been detached, after VBUS has been removed.

See Table 4-30 DRP Timing Parameters

## [◆ ](#ga75223d9754d7ce76e302ee2ed40d11ef)TC\_T\_VPDCTDD\_MAX\_MS

| #define TC\_T\_VPDCTDD\_MAX\_MS   5 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Maximum time for a Charge-Through VCONN-Powered USB Device to detect that the Charge-Through source has disconnected from CC after VBUS has been removed, transition to CTUnattached.VPD, and re-apply its Rp termination advertising 3.0 A on the host port CC.

See Table 4-31 CC Timing

## [◆ ](#gae2ebe887ccb4f9549d130e85b999062e)TC\_T\_VPDCTDD\_MIN\_US

| #define TC\_T\_VPDCTDD\_MIN\_US   30 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Minimum time for a Charge-Through VCONN-Powered USB Device to detect that the Charge-Through source has disconnected from CC after VBUS has been removed, transition to CTUnattached.VPD, and re-apply its Rp termination advertising 3.0 A on the host port CC.

See Table 4-31 CC Timing

## [◆ ](#ga56ece8323bd0a8e4ce0755e0e9e06f96)TC\_T\_VPDDISABLE\_MIN\_MS

| #define TC\_T\_VPDDISABLE\_MIN\_MS   25 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Minimum time for a Charge-Through VCONN-Powered USB Device shall remain in CTDisabled.VPD state.

See Table 4-31 CC Timing

## [◆ ](#ga151c5852b9d2ad3f6f7f0869505e854b)TC\_V\_SINK\_DISCONNECT\_MAX\_MV

| #define TC\_V\_SINK\_DISCONNECT\_MAX\_MV   3670 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

VBUS maximum for a sink disconnect detection.

See Table 4-3 VBUS Sink Characteristics

## [◆ ](#ga025aeca5768435b245ecb9fe8bfa29c8)TC\_V\_SINK\_DISCONNECT\_MIN\_MV

| #define TC\_V\_SINK\_DISCONNECT\_MIN\_MV   800 |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

VBUS minimum for a sink disconnect detection.

See Table 4-3 VBUS Sink Characteristics

## Enumeration Type Documentation

## [◆ ](#ga8707ac194510396d55a40887673b53ca)tc\_cable\_plug

| enum [tc\_cable\_plug](#ga8707ac194510396d55a40887673b53ca) |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Cable plug.

See 6.2.1.1.7 Cable Plug. Only applies to SOP' and SOP". Replaced by pd\_power\_role for SOP packets.

| Enumerator | |
| --- | --- |
| PD\_PLUG\_FROM\_DFP\_UFP |  |
| PD\_PLUG\_FROM\_CABLE\_VPD |  |

## [◆ ](#gac5b4b58840c9b076a869a5816ba100db)tc\_cc\_polarity

| enum [tc\_cc\_polarity](#gac5b4b58840c9b076a869a5816ba100db) |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Polarity of the CC lines.

| Enumerator | |
| --- | --- |
| TC\_POLARITY\_CC1 | Use CC1 IO for Power Delivery communication. |
| TC\_POLARITY\_CC2 | Use CC2 IO for Power Delivery communication. |

## [◆ ](#ga0200c820510eb786f3ca30a9b5f7aada)tc\_cc\_pull

| enum [tc\_cc\_pull](#ga0200c820510eb786f3ca30a9b5f7aada) |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

CC pull resistors.

| Enumerator | |
| --- | --- |
| TC\_CC\_RA | Ra Pull-Down resistor. |
| TC\_CC\_RP | Rp Pull-Up resistor. |
| TC\_CC\_RD | Rd Pull-Down resistor. |
| TC\_CC\_OPEN | No CC resistor. |
| TC\_RA\_RD | Ra and Rd Pull-Down resistor. |

## [◆ ](#ga5bb2cfcf3ab60423048db38103657197)tc\_cc\_states

| enum [tc\_cc\_states](#ga5bb2cfcf3ab60423048db38103657197) |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Possible port partner connections based on CC line states.

| Enumerator | |
| --- | --- |
| TC\_CC\_NONE | No port partner attached. |
| TC\_CC\_UFP\_NONE | From DFP perspective.  No UFP accessory connected |
| TC\_CC\_UFP\_AUDIO\_ACC | UFP Audio accessory connected. |
| TC\_CC\_UFP\_DEBUG\_ACC | UFP Debug accessory connected. |
| TC\_CC\_UFP\_ATTACHED | Plain UFP attached. |
| TC\_CC\_DFP\_ATTACHED | From UFP perspective.  Plain DFP attached |
| TC\_CC\_DFP\_DEBUG\_ACC | DFP debug accessory connected. |

## [◆ ](#ga64e32ec2da97f70fd5b96975317cb92c)tc\_cc\_voltage\_state

| enum [tc\_cc\_voltage\_state](#ga64e32ec2da97f70fd5b96975317cb92c) |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

CC Voltage status.

| Enumerator | |
| --- | --- |
| TC\_CC\_VOLT\_OPEN | No port partner connection. |
| TC\_CC\_VOLT\_RA | Port partner is applying Ra. |
| TC\_CC\_VOLT\_RD | Port partner is applying Rd. |
| TC\_CC\_VOLT\_RP\_DEF | Port partner is applying Rp (0.5A). |
| TC\_CC\_VOLT\_RP\_1A5 |  |
| TC\_CC\_VOLT\_RP\_3A0 | Port partner is applying Rp (3.0A). |

## [◆ ](#ga6b98bbe238e62cfd5531688494a63de2)tc\_data\_role

| enum [tc\_data\_role](#ga6b98bbe238e62cfd5531688494a63de2) |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Power Delivery Data Role.

| Enumerator | |
| --- | --- |
| TC\_ROLE\_UFP | Data role is an Upstream Facing Port. |
| TC\_ROLE\_DFP | Data role is a Downstream Facing Port. |
| TC\_ROLE\_DISCONNECTED | Port is disconnected. |

## [◆ ](#gaa6dda0612045b5f55b9d8ba63d2b9f9d)tc\_power\_role

| enum [tc\_power\_role](#gaa6dda0612045b5f55b9d8ba63d2b9f9d) |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Power Delivery Power Role.

| Enumerator | |
| --- | --- |
| TC\_ROLE\_SINK | Power role is a sink. |
| TC\_ROLE\_SOURCE | Power role is a source. |

## [◆ ](#ga4e0eec97f7c5c97b87eff9561deea2d5)tc\_rp\_value

| enum [tc\_rp\_value](#ga4e0eec97f7c5c97b87eff9561deea2d5) |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

Pull-Up resistor values.

| Enumerator | |
| --- | --- |
| TC\_RP\_USB | Pull-Up resistor for a current of 900mA. |
| TC\_RP\_1A5 | Pull-Up resistor for a current of 1.5A. |
| TC\_RP\_3A0 | Pull-Up resistor for a current of 3.0A. |
| TC\_RP\_RESERVED | No Pull-Up resistor is applied. |

## [◆ ](#ga015455a6c5620dfc96cfb713bbb72161)tc\_vbus\_level

| enum [tc\_vbus\_level](#ga015455a6c5620dfc96cfb713bbb72161) |
| --- |

`#include <[usbc_tc.h](usbc__tc_8h.md)>`

VBUS level voltages.

| Enumerator | |
| --- | --- |
| TC\_VBUS\_SAFE0V | VBUS is less than vSafe0V max. |
| TC\_VBUS\_PRESENT | VBUS is at least vSafe5V min. |
| TC\_VBUS\_REMOVED | VBUS is less than vSinkDisconnect max. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
