---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/deprecated.html
original_path: doxygen/html/deprecated.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Deprecated List

Module [bt\_hci\_driver](group__bt__hci__driver.md)
:   This is the old HCI driver API. Drivers should use [Bluetooth HCI APIs](group__bt__hci__api.md "Bluetooth HCI APIs") instead.

Global [bt\_hci\_driver\_register](group__bt__hci__driver.md#ga642d226772448dccbd14f2c287d687f0) (const struct [bt\_hci\_driver](structbt__hci__driver.md "Abstraction which represents the HCI transport to the controller.") \*drv)
:   Use the new HCI driver interface instead: [Bluetooth HCI APIs](group__bt__hci__api.md "Bluetooth HCI APIs")

Global [BT\_LE\_ADV\_CONN\_NAME](group__bt__gap.md#ga7b29dba3d892186897c5b4ca5adfd2e3)
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_ADV\_CONN\_NAME\_AD](group__bt__gap.md#ga213307090f1debdc783c54faf4a36740)
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_ADV\_NCONN\_NAME](group__bt__gap.md#gac1c3c47e3136ce813bb50b00a9387cb4)
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea0a9642077d93cf9c0eb42f64a9e34e73)
:   This option will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_ADV\_OPT\_USE\_NAME](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398)
:   This option will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_EXT\_ADV\_CODED\_NCONN\_NAME](group__bt__gap.md#ga8c6027f7c0888c577f9b61a65104be05)
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_EXT\_ADV\_CONN\_NAME](group__bt__gap.md#gac4880197cbe21aad78c4edf10cde95da)
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_EXT\_ADV\_NCONN\_NAME](group__bt__gap.md#ga5c79af6787ccda890f485a45c931cdc8)
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_EXT\_ADV\_SCAN\_NAME](group__bt__gap.md#ga3e4abd3691e2c6d95acd21b9ca566edd)
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [bt\_recv](group__bt__hci__driver.md#gaca80bc9dacc4fa44416bd545bd185ef7) (struct [net\_buf](structnet__buf.md "Network buffer representation.") \*buf)
:   Use the new HCI driver interface instead: [Bluetooth HCI APIs](group__bt__hci__api.md "Bluetooth HCI APIs")

Global [can\_calc\_prescaler](group__can__interface.md#ga7ee7a3296995c09c7f35f54029ed26cd) (const struct device \*dev, struct [can\_timing](structcan__timing.md "CAN bus timing structure.") \*timing, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate)
:   This function allows for bitrate errors, but bitrate errors between nodes on the same network leads to them drifting apart after the start-of-frame (SOF) synchronization has taken place.

Global [can\_get\_max\_bitrate](group__can__interface.md#gad3f929b2170f27b1cbe37a1caccb2e37) (const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*max\_bitrate)
:   Use *[can\_get\_bitrate\_max()](group__can__interface.md#ga1e6dc8026e4d922bce4d398d9f32a457 "Get maximum supported bitrate.")* instead.

Global [can\_get\_min\_bitrate](group__can__interface.md#gaef00151aad8c47fef798d53140ea7296) (const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*min\_bitrate)
:   Use *[can\_get\_bitrate\_min()](group__can__interface.md#ga343456749eec6144a91bacae0d94b114 "Get minimum supported bitrate.")* instead.

Global [CAN\_MAX\_EXT\_ID](group__can__interface.md#ga0f3572940065f8f6d54099e7a4175f8f)
:   Use [CAN\_EXT\_ID\_MASK](group__can__interface.md#ga15ee71e8abcf51008925585049125986 "Bit mask for an extended (29-bit) CAN identifier.") instead.

Global [CAN\_MAX\_STD\_ID](group__can__interface.md#ga7987c1d4089742f87a7ac611add1a286)
:   Use [CAN\_STD\_ID\_MASK](group__can__interface.md#ga4cd8ce34887b90baeeaa6a4aa048b398 "Bit mask for a standard (11-bit) CAN identifier.") instead.

Global [CBPRINTF\_PACKAGE\_COPY\_KEEP\_RO\_STR](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga66d65a0f8f9c32440cb7b92a37d0e248)
:   Use [CBPRINTF\_PACKAGE\_CONVERT\_KEEP\_RO\_STR](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga582ebea3e0d18285840bf277c5382da6 "CBPRINTF_PACKAGE_CONVERT_KEEP_RO_STR") instead.

Global [CBPRINTF\_PACKAGE\_COPY\_RO\_STR](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga3da36360cc579adbd5e991addf4c3fc6)
:   Use [CBPRINTF\_PACKAGE\_CONVERT\_RO\_STR](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga9802b700abd5d3cd7cef0e0cbcceb3e7 "CBPRINTF_PACKAGE_CONVERT_RO_STR") instead.

Global [CBPRINTF\_PACKAGE\_COPY\_RW\_STR](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga1b3b798a2a208276ddc3931b06064323)
:   Use [CBPRINTF\_PACKAGE\_CONVERT\_RW\_STR](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga983c65ed8afb356a29fa2736f9de7b39 "CBPRINTF_PACKAGE_CONVERT_RW_STR") instead.

Global [ceiling\_fraction](group__sys-util.md#gaad408461e7ab356650bcd5c83bc0ed39) (numerator, divider)
:   Use [DIV\_ROUND\_UP()](group__sys-util.md#gae664e7492e37d324831caf2321ddda37 "Divide and round up.") instead.

Global [IEEE802154\_HW\_SLEEP\_TO\_TX](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a36f46639c08e70bc30fc98ca1043b071)
:   Drivers and L2 SHALL not introduce additional references to this capability and remove existing ones as outlined in #63670.

Global [K\_THREAD\_STACK\_MEMBER](group__thread__stack__api.md#ga753188e7f124f0ee03ed0fa1dad8ecfb) (sym, size)
:   This is now deprecated, as stacks defined in this way are not usable from user mode. Use K\_KERNEL\_STACK\_MEMBER.

Global [lwm2m\_get\_u64](group__lwm2m__api.md#ga831d229d9a4b983223dff626bbde7a66) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md "LwM2M object path structure.") \*path, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value)
:   Unsigned 64bit value type does not exits. This is internally handled as a [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b). Use [lwm2m\_get\_s64()](group__lwm2m__api.md#gaaffe06ca9ee5302fb6e26164f250653e "Get resource (instance) value (s64).") instead.

Global [lwm2m\_set\_u64](group__lwm2m__api.md#ga8a751dc8384cc47f9c14d916e20ae19d) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md "LwM2M object path structure.") \*path, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value)
:   Unsigned 64bit value type does not exits. This is internally handled as a [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b). Use [lwm2m\_set\_s64()](group__lwm2m__api.md#ga18fcee379640c0dda32d6e3d14827260 "Set resource (instance) value (s64).") instead.

Global [net\_if\_ipv4\_get\_netmask](group__net__if.md#ga41aeb0e7c5f9bc837f7b2ec13401afd1) (struct [net\_if](structnet__if.md "Network Interface structure.") \*iface)
:   Use [net\_if\_ipv4\_get\_netmask\_by\_addr()](group__net__if.md#gadfad7d9232bf58c5626266387a2eb761 "Get IPv4 netmask related to an address of an interface.") instead.

Global [net\_if\_ipv4\_set\_netmask](group__net__if.md#gad599bd11663fefa7d785b9fc5d52caf0) (struct [net\_if](structnet__if.md "Network Interface structure.") \*iface, const struct [in\_addr](structin__addr.md "IPv4 address struct.") \*netmask)
:   Use [net\_if\_ipv4\_set\_netmask\_by\_addr()](group__net__if.md#ga7beda6ccba46fce3cf2da1ce6c0725ec "Set IPv4 netmask for an interface index for a given address.") instead.

Global [net\_if\_ipv4\_set\_netmask\_by\_index](group__net__if.md#ga94f2d2e69548609dd329c7e6b21e8958) (int index, const struct [in\_addr](structin__addr.md "IPv4 address struct.") \*netmask)
:   Use [net\_if\_ipv4\_set\_netmask\_by\_addr()](group__net__if.md#ga7beda6ccba46fce3cf2da1ce6c0725ec "Set IPv4 netmask for an interface index for a given address.") instead.

Global [PWM\_STM32\_COMPLEMENTARY](stm32__pwm_8h.md#ac73e020f7f8787beaa8ddf7871578c6f)
:   Use the PWM complementary [STM32\_PWM\_COMPLEMENTARY](stm32__pwm_8h.md#a8e4959803792254f90bb31e0454a4249 "PWM complementary output pin is enabled.") flag instead.

Global [smp\_add\_cmd\_ret](mgmt_2mcumgr_2smp_2smp_8h.md#abad955ba2e5e19b6f6443c8eed4f1760) (zcbor\_state\_t \*zse, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) group, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ret)
:   Deprecated after Zephyr 3.4, use [smp\_add\_cmd\_err()](mgmt_2mcumgr_2smp_2smp_8h.md#a191eb8c8a5a531b158374a1071925ca7 "Appends an "err" response.") instead

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
