---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/deprecated.html
original_path: doxygen/html/deprecated.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Deprecated List

Module [bt\_hci\_driver](group__bt__hci__driver.md)
:   This is the old HCI driver API. Drivers should use [Bluetooth HCI APIs](group__bt__hci__api.md "Bluetooth HCI APIs") instead.

Global [bt\_hci\_driver\_register](group__bt__hci__driver.md#ga642d226772448dccbd14f2c287d687f0) (const struct [bt\_hci\_driver](structbt__hci__driver.md "Abstraction which represents the HCI transport to the controller.") \*drv)
:   Use the new HCI driver interface instead: [Bluetooth HCI APIs](group__bt__hci__api.md "Bluetooth HCI APIs")

Global [BT\_LE\_ADV\_CONN](group__bt__gap.md#gad490487b9e196526a13fe249a4c25448)
:   This is a convenience macro for [BT\_LE\_ADV\_OPT\_CONNECTABLE](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3 "BT_LE_ADV_OPT_CONNECTABLE"), which is deprecated. Please use [BT\_LE\_ADV\_CONN\_FAST\_1](group__bt__gap.md#gaa700527b1caf3bef27d96a3f91a29f69 "BT_LE_ADV_CONN_FAST_1") or [BT\_LE\_ADV\_CONN\_FAST\_2](group__bt__gap.md#ga684a1110a8973bc17211f6f0824beccd "BT_LE_ADV_CONN_FAST_2") instead.

Global [BT\_LE\_ADV\_CONN\_NAME](group__bt__gap.md#ga7b29dba3d892186897c5b4ca5adfd2e3)
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_ADV\_CONN\_NAME\_AD](group__bt__gap.md#ga213307090f1debdc783c54faf4a36740)
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_ADV\_NCONN\_NAME](group__bt__gap.md#gac1c3c47e3136ce813bb50b00a9387cb4)
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_ADV\_OPT\_CONNECTABLE](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3)
:   Use [BT\_LE\_ADV\_OPT\_CONN](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169 "BT_LE_ADV_OPT_CONN") instead.

Global [BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea0a9642077d93cf9c0eb42f64a9e34e73)
:   This option will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_ADV\_OPT\_ONE\_TIME](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea7d12782a02afefcf4b5c04442a99f8a2)
:   Use [BT\_LE\_ADV\_OPT\_CONN](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169 "BT_LE_ADV_OPT_CONN") instead.

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

Global [IEEE802154\_HW\_SLEEP\_TO\_TX](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a36f46639c08e70bc30fc98ca1043b071)
:   Drivers and L2 SHALL not introduce additional references to this capability and remove existing ones as outlined in #63670.

Global [kscan\_callback\_t](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480) )(const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) row, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) column, bool pressed)

Global [kscan\_config](group__kscan__interface.md#ga9caf0c1e798d610befcb9bdd4a50ddc5) (const struct device \*dev, [kscan\_callback\_t](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480 "Keyboard scan callback called when user press/release a key on a matrix keyboard.") callback)

Global [kscan\_disable\_callback](group__kscan__interface.md#ga183471b229ec08d827952c7515625e28) (const struct device \*dev)

Global [kscan\_enable\_callback](group__kscan__interface.md#gaa1d46198ea2b36526671b0c32b3b6eab) (const struct device \*dev)

Module [kscan\_interface](group__kscan__interface.md)

Global [net\_buf\_get](group__net__buf.md#ga014a0e87afc143d06a7eaf6c2f04c742) (struct [k\_fifo](structk__fifo.md) \*fifo, [k\_timeout\_t](structk__timeout__t.md "Kernel timeout type.") timeout)
:   Use *[k\_fifo\_get()](group__fifo__apis.md#ga1e2c480e2124116af97e94e7b4435de6 "Get an element from a FIFO queue.")* instead.

Global [net\_buf\_put](group__net__buf.md#ga7e1bcc520b7bffcbd9c1d3d308100047) (struct [k\_fifo](structk__fifo.md) \*fifo, struct [net\_buf](structnet__buf.md "Network buffer representation.") \*buf)
:   Use *[k\_fifo\_put()](group__fifo__apis.md#ga3addb10f86f19e245c23362433d5c913 "Add an element to a FIFO queue.")* instead.

Global [net\_if\_ipv4\_get\_netmask](group__net__if.md#ga41aeb0e7c5f9bc837f7b2ec13401afd1) (struct [net\_if](structnet__if.md "Network Interface structure.") \*iface)
:   Use [net\_if\_ipv4\_get\_netmask\_by\_addr()](group__net__if.md#gadfad7d9232bf58c5626266387a2eb761 "Get IPv4 netmask related to an address of an interface.") instead.

Global [net\_if\_ipv4\_set\_netmask](group__net__if.md#gad599bd11663fefa7d785b9fc5d52caf0) (struct [net\_if](structnet__if.md "Network Interface structure.") \*iface, const struct [in\_addr](structin__addr.md "IPv4 address struct.") \*netmask)
:   Use [net\_if\_ipv4\_set\_netmask\_by\_addr()](group__net__if.md#ga7beda6ccba46fce3cf2da1ce6c0725ec "Set IPv4 netmask for an interface index for a given address.") instead.

Global [net\_if\_ipv4\_set\_netmask\_by\_index](group__net__if.md#ga94f2d2e69548609dd329c7e6b21e8958) (int index, const struct [in\_addr](structin__addr.md "IPv4 address struct.") \*netmask)
:   Use [net\_if\_ipv4\_set\_netmask\_by\_addr()](group__net__if.md#ga7beda6ccba46fce3cf2da1ce6c0725ec "Set IPv4 netmask for an interface index for a given address.") instead.

Global [PWM\_STM32\_COMPLEMENTARY](stm32__pwm_8h.md#ac73e020f7f8787beaa8ddf7871578c6f)
:   Use the PWM complementary [STM32\_PWM\_COMPLEMENTARY](stm32__pwm_8h.md#a8e4959803792254f90bb31e0454a4249 "PWM complementary output pin is enabled.") flag instead.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
