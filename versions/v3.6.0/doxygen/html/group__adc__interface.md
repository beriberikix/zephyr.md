---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__adc__interface.html
original_path: doxygen/html/group__adc__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ADC driver APIs

[Device Driver APIs](group__io__interfaces.md)

ADC driver APIs.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Emulated ADC](group__adc__emul.md) |
|  | Emulated ADC backend API. |

| Data Structures | |
| --- | --- |
| struct | [adc\_channel\_cfg](structadc__channel__cfg.md) |
|  | Structure for specifying the configuration of an ADC channel. [More...](structadc__channel__cfg.md#details) |
| struct | [adc\_dt\_spec](structadc__dt__spec.md) |
|  | Container for ADC channel information specified in devicetree. [More...](structadc__dt__spec.md#details) |
| struct | [adc\_sequence\_options](structadc__sequence__options.md) |
|  | Structure defining additional options for an ADC sampling sequence. [More...](structadc__sequence__options.md#details) |
| struct | [adc\_sequence](structadc__sequence.md) |
|  | Structure defining an ADC sampling sequence. [More...](structadc__sequence.md#details) |
| struct | [adc\_driver\_api](structadc__driver__api.md) |
|  | ADC driver API. [More...](structadc__driver__api.md#details) |

| Macros | |
| --- | --- |
| #define | [ADC\_CHANNEL\_CFG\_DT](#ga8d1f7d55c94fed3247c830a4569ab05e)(node\_id) |
|  | Get ADC channel configuration from a given devicetree node. |
| #define | [ADC\_DT\_SPEC\_GET\_BY\_IDX](#gae9867df7a034d45ed3d3c58c69c246ed)(node\_id, idx) |
|  | Get ADC io-channel information from devicetree. |
| #define | [ADC\_DT\_SPEC\_INST\_GET\_BY\_IDX](#ga4705a1e2cc22fe73b7e967e8ba220584)(inst, idx) |
|  | Get ADC io-channel information from a DT\_DRV\_COMPAT devicetree instance. |
| #define | [ADC\_DT\_SPEC\_GET](#gad05df3d329ba785c094ea4c32e2913b7)(node\_id) |
|  | Equivalent to [ADC\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0)](#gae9867df7a034d45ed3d3c58c69c246ed). |
| #define | [ADC\_DT\_SPEC\_INST\_GET](#ga96222a7d374e21d477b99f74d715bae1)(inst) |
|  | Equivalent to [ADC\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, 0)](#ga4705a1e2cc22fe73b7e967e8ba220584). |

| Typedefs | |
| --- | --- |
| typedef enum [adc\_action](#ga8f6df993405679f852ae4cd8c63c6917)(\* | [adc\_sequence\_callback](#ga9150eb6dc53d1c62b9fa225c0a371d6d)) (const struct [device](structdevice.md) \*dev, const struct [adc\_sequence](structadc__sequence.md) \*sequence, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sampling\_index) |
|  | Type definition of the optional callback function to be called after a requested sampling is done. |
| typedef int(\* | [adc\_api\_channel\_setup](#ga871680cf9f390bfe19a10a61eb1ca092)) (const struct [device](structdevice.md) \*dev, const struct [adc\_channel\_cfg](structadc__channel__cfg.md) \*channel\_cfg) |
|  | Type definition of ADC API function for configuring a channel. |
| typedef int(\* | [adc\_api\_read](#ga4d4484e52ff7727fd316f50b2f404adf)) (const struct [device](structdevice.md) \*dev, const struct [adc\_sequence](structadc__sequence.md) \*sequence) |
|  | Type definition of ADC API function for setting a read request. |
| typedef int(\* | [adc\_api\_read\_async](#gad0160f455d1901ebfe06568e8418a22c)) (const struct [device](structdevice.md) \*dev, const struct [adc\_sequence](structadc__sequence.md) \*sequence, struct [k\_poll\_signal](structk__poll__signal.md) \*async) |
|  | Type definition of ADC API function for setting an asynchronous read request. |

| Enumerations | |
| --- | --- |
| enum | [adc\_gain](#ga306f882323c66b263d3797124ca5f3a0) {     [ADC\_GAIN\_1\_6](#gga306f882323c66b263d3797124ca5f3a0abb26700162bfc68a2beadc1e78b758c1) , [ADC\_GAIN\_1\_5](#gga306f882323c66b263d3797124ca5f3a0a198c40369bddfc3c0eaa8ae3bb1be0c9) , [ADC\_GAIN\_1\_4](#gga306f882323c66b263d3797124ca5f3a0afa55c5a94bfebb9a70638e9ab32eabf8) , [ADC\_GAIN\_1\_3](#gga306f882323c66b263d3797124ca5f3a0af896fe01119930815ac78a4ee87635ee) ,     [ADC\_GAIN\_2\_5](#gga306f882323c66b263d3797124ca5f3a0a4a59d3dd1e2e2fbe2ec593291ca307e0) , [ADC\_GAIN\_1\_2](#gga306f882323c66b263d3797124ca5f3a0a2d36559128c21834d1188aed43d236d2) , [ADC\_GAIN\_2\_3](#gga306f882323c66b263d3797124ca5f3a0ac720b0730cfef7c55f97777fec75dc62) , [ADC\_GAIN\_4\_5](#gga306f882323c66b263d3797124ca5f3a0ad0ee4a6bfc749a3213f0c44d30e8e6df) ,     [ADC\_GAIN\_1](#gga306f882323c66b263d3797124ca5f3a0a76b3097b0b38d33266d36f5a5d534e54) , [ADC\_GAIN\_2](#gga306f882323c66b263d3797124ca5f3a0aff4b7cc577e333a3a684e4e56b124868) , [ADC\_GAIN\_3](#gga306f882323c66b263d3797124ca5f3a0a113a3324782a4517bb71fc3b03aeef5e) , [ADC\_GAIN\_4](#gga306f882323c66b263d3797124ca5f3a0a12756ff0f6a345ff3fee2077e1153300) ,     [ADC\_GAIN\_6](#gga306f882323c66b263d3797124ca5f3a0aba255a08f5ff25388778057d725a77c8) , [ADC\_GAIN\_8](#gga306f882323c66b263d3797124ca5f3a0ae9a429f8b69dd0e5cae0e1ab7dbe7dc3) , [ADC\_GAIN\_12](#gga306f882323c66b263d3797124ca5f3a0a3ff31845095f2b0fe7e62b2b826411e8) , [ADC\_GAIN\_16](#gga306f882323c66b263d3797124ca5f3a0a4b18ba08d86e630f2deeeea5b329f970) ,     [ADC\_GAIN\_24](#gga306f882323c66b263d3797124ca5f3a0a5d19226b1d1728180101e65b8386ff33) , [ADC\_GAIN\_32](#gga306f882323c66b263d3797124ca5f3a0ac693403ea0f70f5723a98fe11967c13f) , [ADC\_GAIN\_64](#gga306f882323c66b263d3797124ca5f3a0a064c567978a50dd58d48d481388dd6eb) , [ADC\_GAIN\_128](#gga306f882323c66b263d3797124ca5f3a0a1b3c6d80db15acf962192341d4754829)   } |
|  | ADC channel gain factors. [More...](#ga306f882323c66b263d3797124ca5f3a0) |
| enum | [adc\_reference](#ga91b0f997d73739cf9f7349b7581e1f56) {     [ADC\_REF\_VDD\_1](#gga91b0f997d73739cf9f7349b7581e1f56ae41651d9d2ba0d3c2a976177fc6ed1b3) , [ADC\_REF\_VDD\_1\_2](#gga91b0f997d73739cf9f7349b7581e1f56a5f47fb0b239da79577887baf2576eb0d) , [ADC\_REF\_VDD\_1\_3](#gga91b0f997d73739cf9f7349b7581e1f56a8e5dfe37c3993e118d6e316c9fa0aad1) , [ADC\_REF\_VDD\_1\_4](#gga91b0f997d73739cf9f7349b7581e1f56a93d4dc4332b3346a7332383ecf745d2c) ,     [ADC\_REF\_INTERNAL](#gga91b0f997d73739cf9f7349b7581e1f56a239921743b35d32a558a43deee2ce709) , [ADC\_REF\_EXTERNAL0](#gga91b0f997d73739cf9f7349b7581e1f56afc15362bdf426f412e150ae9f8d224e6) , [ADC\_REF\_EXTERNAL1](#gga91b0f997d73739cf9f7349b7581e1f56a2733819da753b01a8116d076498fe52a)   } |
|  | ADC references. [More...](#ga91b0f997d73739cf9f7349b7581e1f56) |
| enum | [adc\_action](#ga8f6df993405679f852ae4cd8c63c6917) { [ADC\_ACTION\_CONTINUE](#gga8f6df993405679f852ae4cd8c63c6917ac875a64d997cb883b49447006554ba92) = 0 , [ADC\_ACTION\_REPEAT](#gga8f6df993405679f852ae4cd8c63c6917a8efc10c77ea616d568f88d3ef88b1715) , [ADC\_ACTION\_FINISH](#gga8f6df993405679f852ae4cd8c63c6917a68a21759522a3d584417fa12359b4dc9) } |
|  | Action to be performed after a sampling is done. [More...](#ga8f6df993405679f852ae4cd8c63c6917) |

| Functions | |
| --- | --- |
| int | [adc\_gain\_invert](#ga5af65795f58e8e92672bf31dc2418e23) (enum [adc\_gain](#ga306f882323c66b263d3797124ca5f3a0) gain, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value) |
|  | Invert the application of gain to a measurement value. |
| int | [adc\_channel\_setup](#ga7bc0488b2d08ae2ee4996c0eed11f0bf) (const struct [device](structdevice.md) \*dev, const struct [adc\_channel\_cfg](structadc__channel__cfg.md) \*channel\_cfg) |
|  | Configure an ADC channel. |
| static int | [adc\_channel\_setup\_dt](#gaec29595ff149508847c51f14c41a5bad) (const struct [adc\_dt\_spec](structadc__dt__spec.md) \*spec) |
|  | Configure an ADC channel from a struct [adc\_dt\_spec](structadc__dt__spec.md "Container for ADC channel information specified in devicetree."). |
| int | [adc\_read](#ga7567ce3b03ebb294620b4e32b7561ab3) (const struct [device](structdevice.md) \*dev, const struct [adc\_sequence](structadc__sequence.md) \*sequence) |
|  | Set a read request. |
| static int | [adc\_read\_dt](#ga303a57dfd56f0870c62ba203483e96aa) (const struct [adc\_dt\_spec](structadc__dt__spec.md) \*spec, const struct [adc\_sequence](structadc__sequence.md) \*sequence) |
|  | Set a read request from a struct [adc\_dt\_spec](structadc__dt__spec.md "Container for ADC channel information specified in devicetree."). |
| int | [adc\_read\_async](#ga009e3733b5b20eb6b26a201c9f9734fc) (const struct [device](structdevice.md) \*dev, const struct [adc\_sequence](structadc__sequence.md) \*sequence, struct [k\_poll\_signal](structk__poll__signal.md) \*async) |
|  | Set an asynchronous read request. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [adc\_ref\_internal](#gad11845f5621d0b0d03da4b6484d79aa4) (const struct [device](structdevice.md) \*dev) |
|  | Get the internal reference voltage. |
| static int | [adc\_raw\_to\_millivolts](#gaef98dabea3e0dc1cef8add298171a950) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ref\_mv, enum [adc\_gain](#ga306f882323c66b263d3797124ca5f3a0) gain, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) resolution, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*valp) |
|  | Convert a raw ADC value to millivolts. |
| static int | [adc\_raw\_to\_millivolts\_dt](#ga11cf9c8f345a83f66704af83a2a26911) (const struct [adc\_dt\_spec](structadc__dt__spec.md) \*spec, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*valp) |
|  | Convert a raw ADC value to millivolts using information stored in a struct [adc\_dt\_spec](structadc__dt__spec.md "Container for ADC channel information specified in devicetree."). |
| static int | [adc\_sequence\_init\_dt](#ga5629d37dde5eb43faa93f4d167333f94) (const struct [adc\_dt\_spec](structadc__dt__spec.md) \*spec, struct [adc\_sequence](structadc__sequence.md) \*seq) |
|  | Initialize a struct [adc\_sequence](structadc__sequence.md "Structure defining an ADC sampling sequence.") from information stored in struct [adc\_dt\_spec](structadc__dt__spec.md "Container for ADC channel information specified in devicetree."). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [adc\_is\_ready\_dt](#ga37412f10ad2c4874e4cce0d5fa8599a0) (const struct [adc\_dt\_spec](structadc__dt__spec.md) \*spec) |
|  | Validate that the ADC device is ready. |

## Detailed Description

ADC driver APIs.

## Macro Definition Documentation

## [◆ ](#ga8d1f7d55c94fed3247c830a4569ab05e)ADC\_CHANNEL\_CFG\_DT

| #define ADC\_CHANNEL\_CFG\_DT | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[adc.h](drivers_2adc_8h.md)>`

**Value:**

{ \

.gain = [DT\_STRING\_TOKEN](group__devicetree-generic-prop.md#ga5995350cc7fd2d12ef7daa2487d1db54)(node\_id, zephyr\_gain), \

.reference = [DT\_STRING\_TOKEN](group__devicetree-generic-prop.md#ga5995350cc7fd2d12ef7daa2487d1db54)(node\_id, zephyr\_reference), \

.acquisition\_time = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, zephyr\_acquisition\_time), \

.channel\_id = [DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)(node\_id), \

IF\_ENABLED(CONFIG\_ADC\_CONFIGURABLE\_INPUTS, \

(.differential = [DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, zephyr\_input\_negative), \

.input\_positive = [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, zephyr\_input\_positive, 0), \

.input\_negative = [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, zephyr\_input\_negative, 0),)) \

IF\_ENABLED([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, zephyr\_differential), \

(.differential = true,)) \

IF\_ENABLED(CONFIG\_ADC\_CONFIGURABLE\_EXCITATION\_CURRENT\_SOURCE\_PIN, \

(.current\_source\_pin\_set = [DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, zephyr\_current\_source\_pin), \

.current\_source\_pin = [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, zephyr\_current\_source\_pin, {0}),)) \

}

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)

#define DT\_NODE\_HAS\_PROP(node\_id, prop)

Does a devicetree node have a property?

**Definition** devicetree.h:3285

[DT\_STRING\_TOKEN](group__devicetree-generic-prop.md#ga5995350cc7fd2d12ef7daa2487d1db54)

#define DT\_STRING\_TOKEN(node\_id, prop)

Get a string property's value as a token.

**Definition** devicetree.h:911

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)

#define DT\_PROP\_OR(node\_id, prop, default\_value)

Like DT\_PROP(), but with a fallback to default\_value.

**Definition** devicetree.h:777

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:615

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)

#define DT\_REG\_ADDR(node\_id)

Get a node's (only) register block address.

**Definition** devicetree.h:2214

Get ADC channel configuration from a given devicetree node.

This returns a static initializer for a struct [adc\_channel\_cfg](structadc__channel__cfg.md "Structure for specifying the configuration of an ADC channel.") filled with data from a given devicetree node.

Example devicetree fragment:

&adc {

#address-cells = <1>;

#size-cells = <0>;

channel@0 {

reg = <0>;

zephyr,gain = "ADC\_GAIN\_1\_6";

zephyr,reference = "ADC\_REF\_INTERNAL";

zephyr,acquisition-time = <ADC\_ACQ\_TIME(ADC\_ACQ\_TIME\_MICROSECONDS, 20)>;

zephyr,input-positive = <NRF\_SAADC\_AIN6>;

zephyr,input-negative = <NRF\_SAADC\_AIN7>;

};

channel@1 {

reg = <1>;

zephyr,gain = "ADC\_GAIN\_1\_6";

zephyr,reference = "ADC\_REF\_INTERNAL";

zephyr,acquisition-time = <ADC\_ACQ\_TIME\_DEFAULT>;

zephyr,input-positive = <NRF\_SAADC\_AIN0>;

};

};

Example usage:

static const struct [adc\_channel\_cfg](structadc__channel__cfg.md) ch0\_cfg\_dt =

[ADC\_CHANNEL\_CFG\_DT](#ga8d1f7d55c94fed3247c830a4569ab05e)([DT\_CHILD](group__devicetree-generic-id.md#ga88259608f4e9083ccc2e9ca5ec2c212e)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(adc), channel\_0));

static const struct [adc\_channel\_cfg](structadc__channel__cfg.md) ch1\_cfg\_dt =

[ADC\_CHANNEL\_CFG\_DT](#ga8d1f7d55c94fed3247c830a4569ab05e)([DT\_CHILD](group__devicetree-generic-id.md#ga88259608f4e9083ccc2e9ca5ec2c212e)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(adc), channel\_1));

// Initializes 'ch0\_cfg\_dt' to:

// {

// .channel\_id = 0,

// .gain = ADC\_GAIN\_1\_6,

// .reference = ADC\_REF\_INTERNAL,

// .acquisition\_time = ADC\_ACQ\_TIME(ADC\_ACQ\_TIME\_MICROSECONDS, 20),

// .differential = true,

// .input\_positive = NRF\_SAADC\_AIN6,

// .input-negative = NRF\_SAADC\_AIN7,

// }

// and 'ch1\_cfg\_dt' to:

// {

// .channel\_id = 1,

// .gain = ADC\_GAIN\_1\_6,

// .reference = ADC\_REF\_INTERNAL,

// .acquisition\_time = ADC\_ACQ\_TIME\_DEFAULT,

// .input\_positive = NRF\_SAADC\_AIN0,

// }

[ADC\_CHANNEL\_CFG\_DT](#ga8d1f7d55c94fed3247c830a4569ab05e)

#define ADC\_CHANNEL\_CFG\_DT(node\_id)

Get ADC channel configuration from a given devicetree node.

**Definition** adc.h:225

[DT\_CHILD](group__devicetree-generic-id.md#ga88259608f4e9083ccc2e9ca5ec2c212e)

#define DT\_CHILD(node\_id, child)

Get a node identifier for a child node.

**Definition** devicetree.h:421

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:198

[adc\_channel\_cfg](structadc__channel__cfg.md)

Structure for specifying the configuration of an ADC channel.

**Definition** adc.h:88

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |

Returns
:   Static initializer for an [adc\_channel\_cfg](structadc__channel__cfg.md "Structure for specifying the configuration of an ADC channel.") structure.

## [◆ ](#gad05df3d329ba785c094ea4c32e2913b7)ADC\_DT\_SPEC\_GET

| #define ADC\_DT\_SPEC\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[adc.h](drivers_2adc_8h.md)>`

**Value:**

[ADC\_DT\_SPEC\_GET\_BY\_IDX](#gae9867df7a034d45ed3d3c58c69c246ed)(node\_id, 0)

[ADC\_DT\_SPEC\_GET\_BY\_IDX](#gae9867df7a034d45ed3d3c58c69c246ed)

#define ADC\_DT\_SPEC\_GET\_BY\_IDX(node\_id, idx)

Get ADC io-channel information from devicetree.

**Definition** adc.h:388

Equivalent to [ADC\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0)](#gae9867df7a034d45ed3d3c58c69c246ed).

See also
:   [ADC\_DT\_SPEC\_GET\_BY\_IDX()](#gae9867df7a034d45ed3d3c58c69c246ed)

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |

Returns
:   Static initializer for an [adc\_dt\_spec](structadc__dt__spec.md "Container for ADC channel information specified in devicetree.") structure.

## [◆ ](#gae9867df7a034d45ed3d3c58c69c246ed)ADC\_DT\_SPEC\_GET\_BY\_IDX

| #define ADC\_DT\_SPEC\_GET\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[adc.h](drivers_2adc_8h.md)>`

**Value:**

ADC\_DT\_SPEC\_STRUCT([DT\_IO\_CHANNELS\_CTLR\_BY\_IDX](group__devicetree-io-channels.md#gaf5bbae59dca995d827ff3ec8b9ce187c)(node\_id, idx), \

[DT\_IO\_CHANNELS\_INPUT\_BY\_IDX](group__devicetree-io-channels.md#ga290c912d0a96ba65bb44341a783fac19)(node\_id, idx))

[DT\_IO\_CHANNELS\_INPUT\_BY\_IDX](group__devicetree-io-channels.md#ga290c912d0a96ba65bb44341a783fac19)

#define DT\_IO\_CHANNELS\_INPUT\_BY\_IDX(node\_id, idx)

Get an io-channels specifier input cell at an index.

**Definition** io-channels.h:161

[DT\_IO\_CHANNELS\_CTLR\_BY\_IDX](group__devicetree-io-channels.md#gaf5bbae59dca995d827ff3ec8b9ce187c)

#define DT\_IO\_CHANNELS\_CTLR\_BY\_IDX(node\_id, idx)

Get the node identifier for the node referenced by an io-channels property at an index.

**Definition** io-channels.h:50

Get ADC io-channel information from devicetree.

This returns a static initializer for an `[adc_dt_spec](structadc__dt__spec.md "Container for ADC channel information specified in devicetree.")` structure given a devicetree node and a channel index. The node must have the "io-channels" property defined.

Example devicetree fragment:

/ {

zephyr,user {

io-channels = <&adc0 1>, <&adc0 3>;

};

};

&adc0 {

#address-cells = <1>;

#size-cells = <0>;

channel@3 {

reg = <3>;

zephyr,gain = "ADC\_GAIN\_1\_5";

zephyr,reference = "ADC\_REF\_VDD\_1\_4";

zephyr,vref-mv = <750>;

zephyr,acquisition-time = <ADC\_ACQ\_TIME\_DEFAULT>;

zephyr,resolution = <12>;

zephyr,oversampling = <4>;

};

};

Example usage:

static const struct [adc\_dt\_spec](structadc__dt__spec.md) adc\_chan0 =

[ADC\_DT\_SPEC\_GET\_BY\_IDX](#gae9867df7a034d45ed3d3c58c69c246ed)([DT\_PATH](group__devicetree-generic-id.md#ga015b4819473797982e83cae497697086)(zephyr\_user), 0);

static const struct [adc\_dt\_spec](structadc__dt__spec.md) adc\_chan1 =

[ADC\_DT\_SPEC\_GET\_BY\_IDX](#gae9867df7a034d45ed3d3c58c69c246ed)([DT\_PATH](group__devicetree-generic-id.md#ga015b4819473797982e83cae497697086)(zephyr\_user), 1);

// Initializes 'adc\_chan0' to:

// {

// .dev = DEVICE\_DT\_GET(DT\_NODELABEL(adc0)),

// .channel\_id = 1,

// }

// and 'adc\_chan1' to:

// {

// .dev = DEVICE\_DT\_GET(DT\_NODELABEL(adc0)),

// .channel\_id = 3,

// .channel\_cfg\_dt\_node\_exists = true,

// .channel\_cfg = {

// .channel\_id = 3,

// .gain = ADC\_GAIN\_1\_5,

// .reference = ADC\_REF\_VDD\_1\_4,

// .acquisition\_time = ADC\_ACQ\_TIME\_DEFAULT,

// },

// .vref\_mv = 750,

// .resolution = 12,

// .oversampling = 4,

// }

[DT\_PATH](group__devicetree-generic-id.md#ga015b4819473797982e83cae497697086)

#define DT\_PATH(...)

Get a node identifier for a devicetree path.

**Definition** devicetree.h:142

[adc\_dt\_spec](structadc__dt__spec.md)

Container for ADC channel information specified in devicetree.

**Definition** adc.h:247

See also
:   [ADC\_DT\_SPEC\_GET()](#gad05df3d329ba785c094ea4c32e2913b7)

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |
    | idx | Channel index. |

Returns
:   Static initializer for an [adc\_dt\_spec](structadc__dt__spec.md "Container for ADC channel information specified in devicetree.") structure.

## [◆ ](#ga96222a7d374e21d477b99f74d715bae1)ADC\_DT\_SPEC\_INST\_GET

| #define ADC\_DT\_SPEC\_INST\_GET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[adc.h](drivers_2adc_8h.md)>`

**Value:**

[ADC\_DT\_SPEC\_GET](#gad05df3d329ba785c094ea4c32e2913b7)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[ADC\_DT\_SPEC\_GET](#gad05df3d329ba785c094ea4c32e2913b7)

#define ADC\_DT\_SPEC\_GET(node\_id)

Equivalent to ADC\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0).

**Definition** adc.h:414

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3410

Equivalent to [ADC\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, 0)](#ga4705a1e2cc22fe73b7e967e8ba220584).

See also
:   [ADC\_DT\_SPEC\_GET()](#gad05df3d329ba785c094ea4c32e2913b7)

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   Static initializer for an [adc\_dt\_spec](structadc__dt__spec.md "Container for ADC channel information specified in devicetree.") structure.

## [◆ ](#ga4705a1e2cc22fe73b7e967e8ba220584)ADC\_DT\_SPEC\_INST\_GET\_BY\_IDX

| #define ADC\_DT\_SPEC\_INST\_GET\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[adc.h](drivers_2adc_8h.md)>`

**Value:**

[ADC\_DT\_SPEC\_GET\_BY\_IDX](#gae9867df7a034d45ed3d3c58c69c246ed)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

Get ADC io-channel information from a DT\_DRV\_COMPAT devicetree instance.

See also
:   [ADC\_DT\_SPEC\_GET\_BY\_IDX()](#gae9867df7a034d45ed3d3c58c69c246ed)

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | idx | Channel index. |

Returns
:   Static initializer for an [adc\_dt\_spec](structadc__dt__spec.md "Container for ADC channel information specified in devicetree.") structure.

## Typedef Documentation

## [◆ ](#ga871680cf9f390bfe19a10a61eb1ca092)adc\_api\_channel\_setup

| typedef int(\* adc\_api\_channel\_setup) (const struct [device](structdevice.md) \*dev, const struct [adc\_channel\_cfg](structadc__channel__cfg.md) \*channel\_cfg) |
| --- |

`#include <[adc.h](drivers_2adc_8h.md)>`

Type definition of ADC API function for configuring a channel.

See [adc\_channel\_setup()](#ga7bc0488b2d08ae2ee4996c0eed11f0bf) for argument descriptions.

## [◆ ](#ga4d4484e52ff7727fd316f50b2f404adf)adc\_api\_read

| typedef int(\* adc\_api\_read) (const struct [device](structdevice.md) \*dev, const struct [adc\_sequence](structadc__sequence.md) \*sequence) |
| --- |

`#include <[adc.h](drivers_2adc_8h.md)>`

Type definition of ADC API function for setting a read request.

See [adc\_read()](#ga7567ce3b03ebb294620b4e32b7561ab3) for argument descriptions.

## [◆ ](#gad0160f455d1901ebfe06568e8418a22c)adc\_api\_read\_async

| typedef int(\* adc\_api\_read\_async) (const struct [device](structdevice.md) \*dev, const struct [adc\_sequence](structadc__sequence.md) \*sequence, struct [k\_poll\_signal](structk__poll__signal.md) \*async) |
| --- |

`#include <[adc.h](drivers_2adc_8h.md)>`

Type definition of ADC API function for setting an asynchronous read request.

See [adc\_read\_async()](#ga009e3733b5b20eb6b26a201c9f9734fc) for argument descriptions.

## [◆ ](#ga9150eb6dc53d1c62b9fa225c0a371d6d)adc\_sequence\_callback

| typedef enum [adc\_action](#ga8f6df993405679f852ae4cd8c63c6917)(\* adc\_sequence\_callback) (const struct [device](structdevice.md) \*dev, const struct [adc\_sequence](structadc__sequence.md) \*sequence, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sampling\_index) |
| --- |

`#include <[adc.h](drivers_2adc_8h.md)>`

Type definition of the optional callback function to be called after a requested sampling is done.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | sequence | Pointer to the sequence structure that triggered the sampling. This parameter points to a copy of the structure that was supplied to the call that started the sampling sequence, thus it cannot be used with the [CONTAINER\_OF()](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f "Get a pointer to a structure containing the element.") macro to retrieve some other data associated with the sequence. Instead, the [adc\_sequence\_options::user\_data](structadc__sequence__options.md#a262fd6daefb22df02c726aafcddc6d47 "Pointer to user data.") field should be used for such purpose. |
    | sampling\_index | Index (0-65535) of the sampling done. |

Returns
:   Action to be performed by the driver. See [adc\_action](#ga8f6df993405679f852ae4cd8c63c6917).

## Enumeration Type Documentation

## [◆ ](#ga8f6df993405679f852ae4cd8c63c6917)adc\_action

| enum [adc\_action](#ga8f6df993405679f852ae4cd8c63c6917) |
| --- |

`#include <[adc.h](drivers_2adc_8h.md)>`

Action to be performed after a sampling is done.

| Enumerator | |
| --- | --- |
| ADC\_ACTION\_CONTINUE | The sequence should be continued normally. |
| ADC\_ACTION\_REPEAT | The sampling should be repeated.  New samples or sample should be read from the ADC and written in the same place as the recent ones. |
| ADC\_ACTION\_FINISH | The sequence should be finished immediately. |

## [◆ ](#ga306f882323c66b263d3797124ca5f3a0)adc\_gain

| enum [adc\_gain](#ga306f882323c66b263d3797124ca5f3a0) |
| --- |

`#include <[adc.h](drivers_2adc_8h.md)>`

ADC channel gain factors.

| Enumerator | |
| --- | --- |
| ADC\_GAIN\_1\_6 | x 1/6. |
| ADC\_GAIN\_1\_5 | x 1/5. |
| ADC\_GAIN\_1\_4 | x 1/4. |
| ADC\_GAIN\_1\_3 | x 1/3. |
| ADC\_GAIN\_2\_5 | x 2/5. |
| ADC\_GAIN\_1\_2 | x 1/2. |
| ADC\_GAIN\_2\_3 | x 2/3. |
| ADC\_GAIN\_4\_5 | x 4/5. |
| ADC\_GAIN\_1 | x 1. |
| ADC\_GAIN\_2 | x 2. |
| ADC\_GAIN\_3 | x 3. |
| ADC\_GAIN\_4 | x 4. |
| ADC\_GAIN\_6 | x 6. |
| ADC\_GAIN\_8 | x 8. |
| ADC\_GAIN\_12 | x 12. |
| ADC\_GAIN\_16 | x 16. |
| ADC\_GAIN\_24 | x 24. |
| ADC\_GAIN\_32 | x 32. |
| ADC\_GAIN\_64 | x 64. |
| ADC\_GAIN\_128 | x 128. |

## [◆ ](#ga91b0f997d73739cf9f7349b7581e1f56)adc\_reference

| enum [adc\_reference](#ga91b0f997d73739cf9f7349b7581e1f56) |
| --- |

`#include <[adc.h](drivers_2adc_8h.md)>`

ADC references.

| Enumerator | |
| --- | --- |
| ADC\_REF\_VDD\_1 | VDD. |
| ADC\_REF\_VDD\_1\_2 | VDD/2. |
| ADC\_REF\_VDD\_1\_3 | VDD/3. |
| ADC\_REF\_VDD\_1\_4 | VDD/4. |
| ADC\_REF\_INTERNAL | Internal. |
| ADC\_REF\_EXTERNAL0 | External, input 0. |
| ADC\_REF\_EXTERNAL1 | External, input 1. |

## Function Documentation

## [◆ ](#ga7bc0488b2d08ae2ee4996c0eed11f0bf)adc\_channel\_setup()

| int adc\_channel\_setup | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [adc\_channel\_cfg](structadc__channel__cfg.md) \* | *channel\_cfg* ) |

`#include <[adc.h](drivers_2adc_8h.md)>`

Configure an ADC channel.

It is required to call this function and configure each channel before it is selected for a read request.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel\_cfg | Channel configuration. |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -EINVAL | If a parameter with an invalid value has been provided. |

## [◆ ](#gaec29595ff149508847c51f14c41a5bad)adc\_channel\_setup\_dt()

| | int adc\_channel\_setup\_dt | ( | const struct [adc\_dt\_spec](structadc__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[adc.h](drivers_2adc_8h.md)>`

Configure an ADC channel from a struct [adc\_dt\_spec](structadc__dt__spec.md "Container for ADC channel information specified in devicetree.").

Parameters
:   | spec | ADC specification from Devicetree. |
    | --- | --- |

Returns
:   A value from [adc\_channel\_setup()](#ga7bc0488b2d08ae2ee4996c0eed11f0bf) or -ENOTSUP if information from Devicetree is not valid.

See also
:   [adc\_channel\_setup()](#ga7bc0488b2d08ae2ee4996c0eed11f0bf)

## [◆ ](#ga5af65795f58e8e92672bf31dc2418e23)adc\_gain\_invert()

| int adc\_gain\_invert | ( | enum [adc\_gain](#ga306f882323c66b263d3797124ca5f3a0) | *gain*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *value* ) |

`#include <[adc.h](drivers_2adc_8h.md)>`

Invert the application of gain to a measurement value.

For example, if the gain passed in is ADC\_GAIN\_1\_6 and the referenced value is 10, the value after the function returns is 60.

Parameters
:   | gain | the gain used to amplify the input signal. |
    | --- | --- |
    | value | a pointer to a value that initially has the effect of the applied gain but has that effect removed when this function successfully returns. If the gain cannot be reversed the value remains unchanged. |

Return values
:   | 0 | if the gain was successfully reversed |
    | --- | --- |
    | -EINVAL | if the gain could not be interpreted |

## [◆ ](#ga37412f10ad2c4874e4cce0d5fa8599a0)adc\_is\_ready\_dt()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) adc\_is\_ready\_dt | ( | const struct [adc\_dt\_spec](structadc__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[adc.h](drivers_2adc_8h.md)>`

Validate that the ADC device is ready.

Parameters
:   | spec | ADC specification from devicetree |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if the ADC device is ready for use and false otherwise. |
    | --- | --- |

## [◆ ](#gaef98dabea3e0dc1cef8add298171a950)adc\_raw\_to\_millivolts()

| | int adc\_raw\_to\_millivolts | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *ref\_mv*, | | --- | --- | --- | --- | |  |  | enum [adc\_gain](#ga306f882323c66b263d3797124ca5f3a0) | *gain*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *resolution*, | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *valp* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[adc.h](drivers_2adc_8h.md)>`

Convert a raw ADC value to millivolts.

This function performs the necessary conversion to transform a raw ADC measurement to a voltage in millivolts.

Parameters
:   | ref\_mv | the reference voltage used for the measurement, in millivolts. This may be from [adc\_ref\_internal()](#gad11845f5621d0b0d03da4b6484d79aa4) or a known external reference. |
    | --- | --- |
    | gain | the ADC gain configuration used to sample the input |
    | resolution | the number of bits in the absolute value of the sample. For differential sampling this needs to be one less than the resolution in struct [adc\_sequence](structadc__sequence.md "Structure defining an ADC sampling sequence."). |
    | valp | pointer to the raw measurement value on input, and the corresponding millivolt value on successful conversion. If conversion fails the stored value is left unchanged. |

Return values
:   | 0 | on successful conversion |
    | --- | --- |
    | -EINVAL | if the gain is not reversible |

## [◆ ](#ga11cf9c8f345a83f66704af83a2a26911)adc\_raw\_to\_millivolts\_dt()

| | int adc\_raw\_to\_millivolts\_dt | ( | const struct [adc\_dt\_spec](structadc__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *valp* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[adc.h](drivers_2adc_8h.md)>`

Convert a raw ADC value to millivolts using information stored in a struct [adc\_dt\_spec](structadc__dt__spec.md "Container for ADC channel information specified in devicetree.").

Parameters
:   | [in] | spec | ADC specification from Devicetree. |
    | --- | --- | --- |
    | [in,out] | valp | Pointer to the raw measurement value on input, and the corresponding millivolt value on successful conversion. If conversion fails the stored value is left unchanged. |

Returns
:   A value from [adc\_raw\_to\_millivolts()](#gaef98dabea3e0dc1cef8add298171a950) or -ENOTSUP if information from Devicetree is not valid.

See also
:   [adc\_raw\_to\_millivolts()](#gaef98dabea3e0dc1cef8add298171a950)

## [◆ ](#ga7567ce3b03ebb294620b4e32b7561ab3)adc\_read()

| int adc\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [adc\_sequence](structadc__sequence.md) \* | *sequence* ) |

`#include <[adc.h](drivers_2adc_8h.md)>`

Set a read request.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | sequence | Structure specifying requested sequence of samplings. |

If invoked from user mode, any sequence struct options for callback must be NULL.

Return values
:   | 0 | On success. |
    | --- | --- |
    | -EINVAL | If a parameter with an invalid value has been provided. |
    | -ENOMEM | If the provided buffer is to small to hold the results of all requested samplings. |
    | -ENOTSUP | If the requested mode of operation is not supported. |
    | -EBUSY | If another sampling was triggered while the previous one was still in progress. This may occur only when samplings are done with intervals, and it indicates that the selected interval was too small. All requested samples are written in the buffer, but at least some of them were taken with an extra delay compared to what was scheduled. |

## [◆ ](#ga009e3733b5b20eb6b26a201c9f9734fc)adc\_read\_async()

| int adc\_read\_async | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [adc\_sequence](structadc__sequence.md) \* | *sequence*, |
|  |  | struct [k\_poll\_signal](structk__poll__signal.md) \* | *async* ) |

`#include <[adc.h](drivers_2adc_8h.md)>`

Set an asynchronous read request.

Note
:   This function is available only if `CONFIG_ADC_ASYNC` is selected.

If invoked from user mode, any sequence struct options for callback must be NULL.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | sequence | Structure specifying requested sequence of samplings. |
    | async | Pointer to a valid and ready to be signaled struct [k\_poll\_signal](structk__poll__signal.md). (Note: if NULL this function will not notify the end of the transaction, and whether it went successfully or not). |

Returns
:   0 on success, negative error code otherwise. See [adc\_read()](#ga7567ce3b03ebb294620b4e32b7561ab3) for a list of possible error codes.

## [◆ ](#ga303a57dfd56f0870c62ba203483e96aa)adc\_read\_dt()

| | int adc\_read\_dt | ( | const struct [adc\_dt\_spec](structadc__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | const struct [adc\_sequence](structadc__sequence.md) \* | *sequence* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[adc.h](drivers_2adc_8h.md)>`

Set a read request from a struct [adc\_dt\_spec](structadc__dt__spec.md "Container for ADC channel information specified in devicetree.").

Parameters
:   | spec | ADC specification from Devicetree. |
    | --- | --- |
    | sequence | Structure specifying requested sequence of samplings. |

Returns
:   A value from [adc\_read()](#ga7567ce3b03ebb294620b4e32b7561ab3).

See also
:   [adc\_read()](#ga7567ce3b03ebb294620b4e32b7561ab3)

## [◆ ](#gad11845f5621d0b0d03da4b6484d79aa4)adc\_ref\_internal()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) adc\_ref\_internal | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[adc.h](drivers_2adc_8h.md)>`

Get the internal reference voltage.

Returns the voltage corresponding to [ADC\_REF\_INTERNAL](#gga91b0f997d73739cf9f7349b7581e1f56a239921743b35d32a558a43deee2ce709), measured in millivolts.

Returns
:   a positive value is the reference voltage value. Returns zero if reference voltage information is not available.

## [◆ ](#ga5629d37dde5eb43faa93f4d167333f94)adc\_sequence\_init\_dt()

| | int adc\_sequence\_init\_dt | ( | const struct [adc\_dt\_spec](structadc__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | struct [adc\_sequence](structadc__sequence.md) \* | *seq* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[adc.h](drivers_2adc_8h.md)>`

Initialize a struct [adc\_sequence](structadc__sequence.md "Structure defining an ADC sampling sequence.") from information stored in struct [adc\_dt\_spec](structadc__dt__spec.md "Container for ADC channel information specified in devicetree.").

Note that this function only initializes the following fields:

- [adc\_sequence::channels](structadc__sequence.md#a5c497c4a5de20e8591063ca8661f79c1 "adc_sequence::channels")
- [adc\_sequence::resolution](structadc__sequence.md#ad5480691be25ed9ee81130b775743125 "adc_sequence::resolution")
- [adc\_sequence::oversampling](structadc__sequence.md#a233e8b20b57bb2fdbebf2c85f076c802 "adc_sequence::oversampling")

Other fields should be initialized by the caller.

Parameters
:   | [in] | spec | ADC specification from Devicetree. |
    | --- | --- | --- |
    | [out] | seq | Sequence to initialize. |

Return values
:   | 0 | On success |
    | --- | --- |
    | -ENOTSUP | If `spec` does not have valid channel configuration |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
