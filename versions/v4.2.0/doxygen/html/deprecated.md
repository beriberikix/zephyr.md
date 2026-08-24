---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/deprecated.html
original_path: doxygen/html/deprecated.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Deprecated List

Global [bt\_hci\_cmd\_create](hci_8h.md#a88da5ec3183ac23bc19ef0ebf66b004b) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) opcode, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) param\_len)
:   Use [bt\_hci\_cmd\_alloc()](hci_8h.md#a974e6e9262601e73537cbdcba7a7c93c "Allocate an HCI command buffer.") instead.

Global [BT\_LE\_ADV\_CONN](group__bt__gap.md#gad490487b9e196526a13fe249a4c25448)
:   This is a convenience macro for [BT\_LE\_ADV\_OPT\_CONNECTABLE](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a2a90f8d144a194f74c5432079c5d42a3 "BT_LE_ADV_OPT_CONNECTABLE"), which is deprecated. Please use [BT\_LE\_ADV\_CONN\_FAST\_1](group__bt__gap.md#gaa700527b1caf3bef27d96a3f91a29f69 "BT_LE_ADV_CONN_FAST_1") or [BT\_LE\_ADV\_CONN\_FAST\_2](group__bt__gap.md#ga684a1110a8973bc17211f6f0824beccd "BT_LE_ADV_CONN_FAST_2") instead.

Global [BT\_LE\_ADV\_CONN\_NAME](group__bt__gap.md#ga7b29dba3d892186897c5b4ca5adfd2e3)
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_ADV\_CONN\_NAME\_AD](group__bt__gap.md#ga213307090f1debdc783c54faf4a36740)
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_ADV\_NCONN\_NAME](group__bt__gap.md#gac1c3c47e3136ce813bb50b00a9387cb4)
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_ADV\_OPT\_CONNECTABLE](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a2a90f8d144a194f74c5432079c5d42a3)
:   Use [BT\_LE\_ADV\_OPT\_CONN](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28aa1407c130bb1cdf1e1dcaaac457d3169 "BT_LE_ADV_OPT_CONN") instead.

Global [BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a0a9642077d93cf9c0eb42f64a9e34e73)
:   This option will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_ADV\_OPT\_ONE\_TIME](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a7d12782a02afefcf4b5c04442a99f8a2)
:   Use [BT\_LE\_ADV\_OPT\_CONN](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28aa1407c130bb1cdf1e1dcaaac457d3169 "BT_LE_ADV_OPT_CONN") instead.

Global [BT\_LE\_ADV\_OPT\_USE\_NAME](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a2dbc9ec77d6de134d96a7bd3d9256398)
:   This option will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_EXT\_ADV\_CODED\_NCONN\_NAME](group__bt__gap.md#ga8c6027f7c0888c577f9b61a65104be05)
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_EXT\_ADV\_CONN\_NAME](group__bt__gap.md#gac4880197cbe21aad78c4edf10cde95da)
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_EXT\_ADV\_NCONN\_NAME](group__bt__gap.md#ga5c79af6787ccda890f485a45c931cdc8)
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [BT\_LE\_EXT\_ADV\_SCAN\_NAME](group__bt__gap.md#ga3e4abd3691e2c6d95acd21b9ca566edd)
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Global [IEEE802154\_HW\_SLEEP\_TO\_TX](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4a36f46639c08e70bc30fc98ca1043b071)
:   Drivers and L2 SHALL not introduce additional references to this capability and remove existing ones as outlined in #63670.

Global [net\_if\_ipv4\_get\_netmask](group__net__if.md#ga41aeb0e7c5f9bc837f7b2ec13401afd1) (struct [net\_if](structnet__if.md "Network Interface structure.") \*iface)
:   Use [net\_if\_ipv4\_get\_netmask\_by\_addr()](group__net__if.md#gadfad7d9232bf58c5626266387a2eb761 "Get IPv4 netmask related to an address of an interface.") instead.

Global [net\_if\_ipv4\_set\_netmask](group__net__if.md#gad599bd11663fefa7d785b9fc5d52caf0) (struct [net\_if](structnet__if.md "Network Interface structure.") \*iface, const struct [in\_addr](structin__addr.md "IPv4 address struct.") \*netmask)
:   Use [net\_if\_ipv4\_set\_netmask\_by\_addr()](group__net__if.md#ga7beda6ccba46fce3cf2da1ce6c0725ec "Set IPv4 netmask for an interface index for a given address.") instead.

Global [net\_if\_ipv4\_set\_netmask\_by\_index](group__net__if.md#ga94f2d2e69548609dd329c7e6b21e8958) (int index, const struct [in\_addr](structin__addr.md "IPv4 address struct.") \*netmask)
:   Use [net\_if\_ipv4\_set\_netmask\_by\_addr()](group__net__if.md#ga7beda6ccba46fce3cf2da1ce6c0725ec "Set IPv4 netmask for an interface index for a given address.") instead.

Global [openthread\_api\_mutex\_lock](group__openthread.md#ga1f702bb5768795bce5561efe457b1028) (struct openthread\_context \*ot\_context)
:   use [openthread\_mutex\_lock](modules_2openthread_2include_2openthread_8h.md#ae3945bc3549118dc5420f9859588282d "openthread_mutex_lock").

Global [openthread\_api\_mutex\_try\_lock](group__openthread.md#ga05c5792a8d2ceaf93336f62760c74862) (struct openthread\_context \*ot\_context)
:   use [openthread\_mutex\_try\_lock](modules_2openthread_2include_2openthread_8h.md#ab5669622dfd83d3a5175fa47325dade3 "openthread_mutex_try_lock") instead.

Global [openthread\_api\_mutex\_unlock](group__openthread.md#ga0c3cb86690f2b1b714ad655b7df23bf3) (struct openthread\_context \*ot\_context)
:   use [openthread\_mutex\_unlock](modules_2openthread_2include_2openthread_8h.md#a420c3321272141f63ea86166b84ec845 "openthread_mutex_unlock") instead.

Global [openthread\_start](group__openthread.md#ga4674b60779f2fd0adaa9c96afb840265) (struct openthread\_context \*ot\_context)
:   use [openthread\_run](modules_2openthread_2include_2openthread_8h.md#a558165d2e49e9335649c94ac0be53392 "openthread_run") instead.

Struct [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md)
:   use [openthread\_state\_changed\_callback](structopenthread__state__changed__callback.md "openthread_state_changed_callback") instead.

Global [openthread\_state\_changed\_cb\_register](group__openthread.md#ga46471bc0ccdf1f953b81dd9720883327) (struct openthread\_context \*ot\_context, struct [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md "OpenThread state change callback.") \*cb)
:   use [openthread\_state\_changed\_callback\_register](modules_2openthread_2include_2openthread_8h.md#a4178b72288585869e2c941acdc21db57 "openthread_state_changed_callback_register") instead.

Global [openthread\_state\_changed\_cb\_unregister](group__openthread.md#ga89eaabc16f6feb84b61f97c5e5cac764) (struct openthread\_context \*ot\_context, struct [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md "OpenThread state change callback.") \*cb)
:   use [openthread\_state\_changed\_callback\_unregister](modules_2openthread_2include_2openthread_8h.md#ae4ad25613f8eada1a0a29426a2f4a518 "openthread_state_changed_callback_unregister") instead.

Global [PWM\_STM32\_COMPLEMENTARY](stm32__pwm_8h.md#ac73e020f7f8787beaa8ddf7871578c6f)
:   Use the PWM complementary [STM32\_PWM\_COMPLEMENTARY](stm32__pwm_8h.md#a8e4959803792254f90bb31e0454a4249 "PWM complementary output pin is enabled.") flag instead.

Global [stream\_flash\_erase\_page](group__stream__flash.md#ga75711b22789724c2d8629e1202dcb48d) (struct [stream\_flash\_ctx](structstream__flash__ctx.md "Structure for stream flash context.") \*ctx, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) off)
:   Use *[flash\_area\_erase()](group__flash__area__api.md#gacc5cbff19d23773115f3334f862814d2 "Erase flash area.")* or [flash\_erase()](group__flash__interface.md#ga05f9c8b0c1ff7273f71797e7ff799c95 "Erase part or all of a flash memory."). Note that there is no Stream Flash API equivalent for that.

Global [TLS\_CREDENTIAL\_SERVER\_CERTIFICATE](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5a541cc34b6fd5af911e633154e54f52f4)
:   Use TLS\_CREDENTIAL\_PUBLIC\_CERTIFICATE instead.

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
