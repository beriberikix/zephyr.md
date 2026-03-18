---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/i3c.html
original_path: hardware/peripherals/i3c.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Improved Inter-Integrated Circuit (I3C) Bus

I3C (Improved Inter-Integrated Circuit) is a two-signal shared
peripheral interface bus. Devices on the bus can operate in
two roles: as a “controller” that initiates transactions and
controls the clock, or as a “target” that responds to transaction
commands.

Currently, the API is based on [I3C Specification](https://www.mipi.org/specifications/i3c-sensor-specification) version 1.1.1.

## [I3C Controller API](#id2)

Zephyr’s I3C controller API is used when an I3C controller controls
the bus, in particularly the start and stop conditions and the clock.
This is the most common mode, used to interact with I3C target
devices such as sensors.

Due to the nature of the I3C, there are devices on the bus where
they may not have addresses when powered on. Therefore, an additional
dynamic address assignment needs to be carried out by the I3C
controller. Because of this, the controller needs to maintain
separate structures to keep track of device status. This can be done
at build time, for example, by creating arrays of device descriptors
for both I3C and I2C devices:

```c
static struct i3c_device_desc i3c_device_array[] = I3C_DEVICE_ARRAY_DT_INST(inst);
static struct i3c_i2c_device_desc i2c_device_array[] = I3C_I2C_DEVICE_ARRAY_DT_INST(inst);
```

The macros `I3C_DEVICE_ARRAY_DT_INST` and
`I3C_I2C_DEVICE_ARRAY_DT_INST` are helper macros to aid in
create arrays of device descriptors corresponding to the devicetree
nodes under the I3C controller.

Here is a list of generic steps for initializing the I3C
controller and the I3C bus inside the device driver
initialization function:

1. Initialize the data structure of the I3C controller device
   driver instance. The usual device defining macros such as
   [`DEVICE_DT_INST_DEFINE`](../../kernel/drivers/index.md#c.DEVICE_DT_INST_DEFINE "DEVICE_DT_INST_DEFINE") can be used, and the initialization
   function provided as a parameter to the macro.

   - The [`i3c_addr_slots`](#c.i3c_addr_slots) and [`i3c_dev_list`](#c.i3c_dev_list) are
     structures to aid in address assignments and device list management.
     If this is being used, this struct needs to be initialized by calling
     [`i3c_addr_slots_init()`](#c.i3c_addr_slots_init). These two structures can also be used
     with various helper functions.
   - Initialize the device descriptors if needed by the controller
     driver.
2. Initialize the hardware, including but not limited to:

   - Setup pin mux and directions.
   - Setup the clock for the controller.
   - Power on the hardware.
   - Configure the hardware (e.g. SCL clock frequency).
3. Perform bus initialization. There is a generic helper function,
   [`i3c_bus_init()`](#c.i3c_bus_init), which performs the following steps.
   This function can be used if the controller does not require
   any special handling during bus initialization.

   1. Do `RSTDAA` to reset dynamic addresses of connected devices.
      If any connected devices have already been assigned an address,
      the bookkeeping data structures do not have records of these,
      for example, at power-on. So it is a good idea to reset and
      assign them new addresses.
   2. Do `DISEC` to disable any events from devices.
   3. Do `SETDASA` to use static addresses as dynamic address
      if so desired.

      - `SETAASA` may not be supported for all connected devices
        to assign static addresses as dynamic addresses.
      - BCR and DCR need to be obtained separately to populate
        the relevant fields in the I3C target device descriptor
        struct.
   4. Do `ENTDAA` to start dynamic address assignment, if there are
      still devices without addresses.

      - If there is a device waiting for address, it will send
        its Provisioned ID, BCR, and DCR back. Match the received
        Provisioned ID to the list of registered I3C devices.

        - If there is a match, assign an address (either from
          the stated static address if `SETDASA` has not been
          done, or use a free address).

          - Also, set the BCR and DCR fields in the device descriptor
            struct.
        - If there is no match, depending on policy, it can be
          assigned a free address, or the device driver can stop
          the assignment process and errors out.

          - Note that the I3C API requires device descriptor to
            function. A device without a device descriptor cannot be
            accessed through the API.
      - This step can be skipped if there is no connected devices
        requiring DAA.
   5. These are optional but highly recommended:

      - Do `GETMRL` and `GETMWL` to get maximum read/write
        length.
      - Do `GETMXDS` to get maximum read/write speed and maximum
        read turnaround time.
      - The helper function, [`i3c_bus_init()`](#c.i3c_bus_init), would retrieve
        basic device information such as BCR, DCR, MRL and MWL.
   6. Do `ENEC` to re-enable events from devices.

      - The helper function, [`i3c_bus_init()`](#c.i3c_bus_init), only re-enables
        hot-join events. IBI event should only be enabled when
        enabling IBI of a device.

### [In-Band Interrupt (IBI)](#id3)

If a target device can generate In-Band Interrupt (IBI),
the controller needs to be made aware of it.

- `i3c_ibi_enable()` to enable IBI of a target device.

  - Some controller hardware have IBI slots which need to be
    programmed so that the controller can recognize incoming IBIs
    from a particular target device.

    - If the hardware has IBI slots, `i3c_ibi_enable()`
      needs to program those IBI slots.
    - Note that there are usually limited IBI slots on
      the controller so this operation may fail.
  - The implementation in driver should also send the `ENEC` command
    to enable interrupt of this target device.
- `i3c_ibi_disable()` to disable IBI of a target device.

  - If controller hardware makes use of IBI slots, this will remove
    description of the target device from the slots.
  - The implementation in driver should also send the `DISEC` command
    to disable interrupt of this target device.

### [Device Tree](#id4)

Here is an example for defining a I3C controller in device tree:

```devicetree
i3c0: i3c@10000 {
        compatible = "vendor,i3c";

        #address-cells = < 0x3 >;
        #size-cells = < 0x0 >;

        reg = < 0x10000 0x1000 >;
        interrupts = < 0x1F 0x0 >;

        pinctrl-0 = < &pinmux-i3c >;
        pinctrl-names = "default";

        i2c-scl-hz = < 400000 >;

        i3c-scl-hz = < 12000000 >;

        status = "okay";

        i3c-dev0: i3c-dev0@420000ABCD12345678 {
                compatible = "vendor,i3c-dev";

                reg = < 0x42 0xABCD 0x12345678 >;

                status = "okay";
        };

        i2c-dev0: i2c-dev0@380000000000000050 {
                compatible = "vendor-i2c-dev";

                reg = < 0x38 0x0 0x50 >;

                status = "okay";
        };
};
```

#### I3C Devices

For I3C devices, the `reg` property has 3 elements:

- The first one is the static address of the device.

  - Can be zero if static address is not used. Address will be
    assigned during DAA (Dynamic Address Assignment).
  - If non-zero and property `assigned-address` is not set,
    this will be the address of the device after SETDASA
    (Set Dynamic Address from Static Address) is issued.
- Second element is the upper 16-bit of the Provisioned ID (PID)
  which contains the manufacturer ID left-shifted by 1. This is
  the bits 33-47 (zero-based) of the 48-bit Provisioned ID.
- Third element contains the lower 32-bit of the Provisioned ID
  which is a combination of the part ID (left-shifted by 16,
  bits 16-31 of the PID) and the instance ID (left-shifted by 12,
  bits 12-15 of the PID).

Note that the unit-address (the part after `@`) must match
the `reg` property fully where each element is treated as
32-bit integer, combining to form a 96-bit integer. This is
required for properly generating device tree macros.

#### I2C Devices

For I2C devices where the device driver has support for
working under I3C bus, the device node can be described as
a child of the I3C controller. If the device driver is written to
only work with I2C controllers, define the node under
the I2C virtual controller as described below.
Otherwise, the `reg` property, similar to I3C devices,
has 3 elements:

- The first one is the static address of the device. This must be
  a valid address as I2C devices do not support
  dynamic address assignment.
- Second element is always zero.

  - This is used by various helper macros to determine whether
    the device tree entry corresponds to a I2C device.
- Third element is the LVR (Legacy Virtual Register):

  - bit[31:8] are unused.
  - bit[7:5] are the I2C device index:

    - Index `0`

      - I3C device has a 50 ns spike filter where it is not
        affected by high frequency on SCL.
    - Index `1`

      - I2C device does not have a 50 ns spike filter but
        can work with high frequency on SCL.
    - Index `2`

      - I3C device does not have a 50 ns spike filter and
        cannot work with high frequency on SCL.
  - bit[4] is the I2C mode indicator:

    - `0` is FM+ mode.
    - `1` is FM mode.

Similar to I3C devices, the unit-address must match the `reg`
property fully where each element is treated as 32-bit integer,
combining to form a 96-bit integer.

### [Device Drivers for I3C Devices](#id5)

All of the transfer functions of I3C controller API require
the use of device descriptors, [`i3c_device_desc`](#c.i3c_device_desc).
This struct contains runtime information about a I3C device,
such as, its dynamic address, BCR, DCR, MRL and MWL. Therefore,
the device driver of a I3C device should grab a pointer to
this device descriptor from the controller using
[`i3c_device_find()`](#c.i3c_device_find). This function takes an ID parameter
of type [`i3c_device_id`](#c.i3c_device_id) for matching. The returned
pointer can then be used in subsequent API calls to
the controller.

### [I2C Devices under I3C Bus](#id6)

Since I3C is backward compatible with I2C, the I3C controller
API can accommodate I2C API calls without modifications if the controller
device driver implements the I2C API. This has the advantage of using
existing I2C devices without any modifications to their device drivers.
However, since the I3C controller API works on device descriptors,
any calls to I2C API will need to look up the corresponding device
descriptor from the I2C device address. This adds a bit of processing
cost to any I2C API calls.

On the other hand, a device driver can be extended to utilize native
I2C device support via the I3C controller API. During device
initialization, `i3c_i2c_device_find()` needs to be called to
retrieve the pointer to the device descriptor. This pointer can be used
in subsequent API calls.

Note that, with either methods mentioned above, the devicetree node of
the I2C device must be declared according to I3C standard:

The I2C virtual controller device driver provides a way to
interface I2C devices on the I3C bus where the associated
device drivers can be used as-is without modifications. This requires
adding an intermediate node in the device tree:

```devicetree
i3c0: i3c@10000 {
        <... I3C controller related properties ...>
        <... Nodes of I3C devices, if any ...>

        i2c-dev0: i2c-dev0@420000000000000050 {
                compatible = "vendor-i2c-dev";

                reg = < 0x42 0x0 0x50 >;

                status = "okay";
        };
};
```

## [Configuration Options](#id7)

Related configuration options:

- [`CONFIG_I3C`](../../kconfig.md#CONFIG_I3C "CONFIG_I3C")
- [`CONFIG_I3C_USE_GROUP_ADDR`](../../kconfig.md#CONFIG_I3C_USE_GROUP_ADDR "CONFIG_I3C_USE_GROUP_ADDR")
- [`CONFIG_I3C_USE_IBI`](../../kconfig.md#CONFIG_I3C_USE_IBI "CONFIG_I3C_USE_IBI")
- [`CONFIG_I3C_IBI_MAX_PAYLOAD_SIZE`](../../kconfig.md#CONFIG_I3C_IBI_MAX_PAYLOAD_SIZE "CONFIG_I3C_IBI_MAX_PAYLOAD_SIZE")
- [`CONFIG_I3C_CONTROLLER_INIT_PRIORITY`](../../kconfig.md#CONFIG_I3C_CONTROLLER_INIT_PRIORITY "CONFIG_I3C_CONTROLLER_INIT_PRIORITY")

## [API Reference](#id8)

*group* I3C Interface
:   I3C Interface.

    **Since**
    :   3.2

    **Version**
    :   0.1.0

    Bus Characteristic Register (BCR)

    - BCR[7:6]: Device Role

      - 0: I3C Target
      - 1: I3C Controller capable
      - 2: Reserved
      - 3: Reserved
    - BCR[5]: Advanced Capabilities

      - 0: Does not support optional advanced capabilities.
      - 1: Supports optional advanced capabilities which can be viewed via GETCAPS CCC.
    - BCR[4]: Virtual Target Support

      - 0: Is not a virtual target.
      - 1: Is a virtual target.
    - BCR[3]: Offline Capable

      - 0: Will always response to I3C commands.
      - 1: Will not always response to I3C commands.
    - BCR[2]: IBI Payload

      - 0: No data bytes following the accepted IBI.
      - 1: One data byte (MDB, Mandatory Data Byte) follows the accepted IBI. Additional data bytes may also follows.
    - BCR[1]: IBI Request Capable

      - 0: Not capable
      - 1: Capable
    - BCR[0]: Max Data Speed Limitation

      - 0: No Limitation
      - 1: Limitation obtained via GETMXDS CCC.

    I3C\_BCR\_MAX\_DATA\_SPEED\_LIMIT
    :   Max Data Speed Limitation bit.

        0 - No Limitation. 1 - Limitation obtained via GETMXDS CCC.

    I3C\_BCR\_IBI\_REQUEST\_CAPABLE
    :   IBI Request Capable bit.

    I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE
    :   IBI Payload bit.

        0 - No data bytes following the accepted IBI. 1 - One data byte (MDB, Mandatory Data Byte) follows the accepted IBI. Additional data bytes may also follows.

    I3C\_BCR\_OFFLINE\_CAPABLE
    :   Offline Capable bit.

        0 - Will always respond to I3C commands. 1 - Will not always respond to I3C commands.

    I3C\_BCR\_VIRTUAL\_TARGET
    :   Virtual Target Support bit.

        0 - Is not a virtual target. 1 - Is a virtual target.

    I3C\_BCR\_ADV\_CAPABILITIES
    :   Advanced Capabilities bit.

        0 - Does not support optional advanced capabilities. 1 - Supports optional advanced capabilities which can be viewed via GETCAPS CCC.

    I3C\_BCR\_DEVICE\_ROLE\_I3C\_TARGET
    :   Device Role - I3C Target.

    I3C\_BCR\_DEVICE\_ROLE\_I3C\_CONTROLLER\_CAPABLE
    :   Device Role - I3C Controller Capable.

    I3C\_BCR\_DEVICE\_ROLE\_SHIFT
    :   Device Role bit shift value.

    I3C\_BCR\_DEVICE\_ROLE\_MASK
    :   Device Role bit shift mask.

    I3C\_BCR\_DEVICE\_ROLE(bcr)
    :   Device Role.

        Obtain Device Role value from the BCR value obtained via GETBCR.

        Parameters:
        :   - **bcr** – BCR value

    Legacy Virtual Register (LVR)

    Legacy Virtual Register (LVR)

    - LVR[7:5]: I2C device index:

      - 0: I2C device has a 50 ns spike filter where it is not affected by high frequency on SCL.
      - 1: I2C device does not have a 50 ns spike filter but can work with high frequency on SCL.
      - 2: I2C device does not have a 50 ns spike filter and cannot work with high frequency on SCL.
    - LVR[4]: I2C mode indicator:

      - 0: FM+ mode
      - 1: FM mode
    - LVR[3:0]: Reserved.

    I3C\_LVR\_I2C\_FM\_PLUS\_MODE
    :   I2C FM+ Mode.

    I3C\_LVR\_I2C\_FM\_MODE
    :   I2C FM Mode.

    I3C\_LVR\_I2C\_MODE\_SHIFT
    :   I2C Mode Indicator bit shift value.

    I3C\_LVR\_I2C\_MODE\_MASK
    :   I2C Mode Indicator bitmask.

    I3C\_LVR\_I2C\_MODE(lvr)
    :   I2C Mode.

        Obtain I2C Mode value from the LVR value.

        Parameters:
        :   - **lvr** – LVR value

    I3C\_LVR\_I2C\_DEV\_IDX\_0
    :   I2C Device Index 0.

        I2C device has a 50 ns spike filter where it is not affected by high frequency on SCL.

    I3C\_LVR\_I2C\_DEV\_IDX\_1
    :   I2C Device Index 1.

        I2C device does not have a 50 ns spike filter but can work with high frequency on SCL.

    I3C\_LVR\_I2C\_DEV\_IDX\_2
    :   I2C Device Index 2.

        I2C device does not have a 50 ns spike filter and cannot work with high frequency on SCL.

    I3C\_LVR\_I2C\_DEV\_IDX\_SHIFT
    :   I2C Device Index bit shift value.

    I3C\_LVR\_I2C\_DEV\_IDX\_MASK
    :   I2C Device Index bitmask.

    I3C\_LVR\_I2C\_DEV\_IDX(lvr)
    :   I2C Device Index.

        Obtain I2C Device Index value from the LVR value.

        Parameters:
        :   - **lvr** – LVR value

    Defines

    I3C\_DEVICE\_ID(pid)
    :   Structure initializer for [i3c\_device\_id](#structi3c__device__id) from PID.

        This helper macro expands to a static initializer for a `struct [i3c_device_id](#structi3c__device__id)` by populating the PID (Provisioned ID) field.

        Parameters:
        :   - **pid** – Provisioned ID.

    Enums

    enum i3c\_bus\_mode
    :   I3C bus mode.

        *Values:*

        enumerator I3C\_BUS\_MODE\_PURE
        :   Only I3C devices are on the bus.

        enumerator I3C\_BUS\_MODE\_MIXED\_FAST
        :   Both I3C and legacy I2C devices are on the bus.

            The I2C devices have 50ns spike filter on SCL.

        enumerator I3C\_BUS\_MODE\_MIXED\_LIMITED
        :   Both I3C and legacy I2C devices are on the bus.

            The I2C devices do not have 50ns spike filter on SCL and can tolerate maximum SDR SCL clock frequency.

        enumerator I3C\_BUS\_MODE\_MIXED\_SLOW
        :   Both I3C and legacy I2C devices are on the bus.

            The I2C devices do not have 50ns spike filter on SCL but cannot tolerate maximum SDR SCL clock frequency.

        enumerator I3C\_BUS\_MODE\_MAX = [I3C\_BUS\_MODE\_MIXED\_SLOW](#c.i3c_bus_mode.I3C_BUS_MODE_MIXED_SLOW)

        enumerator I3C\_BUS\_MODE\_INVALID

    enum i3c\_i2c\_speed\_type
    :   I2C bus speed under I3C bus.

        Only FM and FM+ modes are supported for I2C devices under I3C bus.

        *Values:*

        enumerator I3C\_I2C\_SPEED\_FM
        :   I2C FM mode.

        enumerator I3C\_I2C\_SPEED\_FMPLUS
        :   I2C FM+ mode.

        enumerator I3C\_I2C\_SPEED\_MAX = [I3C\_I2C\_SPEED\_FMPLUS](#c.i3c_i2c_speed_type.I3C_I2C_SPEED_FMPLUS)

        enumerator I3C\_I2C\_SPEED\_INVALID

    enum i3c\_data\_rate
    :   I3C data rate.

        I3C data transfer rate defined by the I3C specification.

        *Values:*

        enumerator I3C\_DATA\_RATE\_SDR
        :   Single Data Rate messaging.

        enumerator I3C\_DATA\_RATE\_HDR\_DDR
        :   High Data Rate - Double Data Rate messaging.

        enumerator I3C\_DATA\_RATE\_HDR\_TSL
        :   High Data Rate - Ternary Symbol Legacy-inclusive-Bus.

        enumerator I3C\_DATA\_RATE\_HDR\_TSP
        :   High Data Rate - Ternary Symbol for Pure Bus.

        enumerator I3C\_DATA\_RATE\_HDR\_BT
        :   High Data Rate - Bulk Transport.

        enumerator I3C\_DATA\_RATE\_MAX = [I3C\_DATA\_RATE\_HDR\_BT](#c.i3c_data_rate.I3C_DATA_RATE_HDR_BT)

        enumerator I3C\_DATA\_RATE\_INVALID

    enum i3c\_sdr\_controller\_error\_codes
    :   I3C SDR Controller Error Codes.

        These are error codes defined by the I3C specification.

        `I3C_ERROR_CE_UNKNOWN` and `I3C_ERROR_CE_NONE` are not official error codes according to the specification. These are there simply to aid in error handling during interactions with the I3C drivers and subsystem.

        *Values:*

        enumerator I3C\_ERROR\_CE0
        :   Transaction after sending CCC.

        enumerator I3C\_ERROR\_CE1
        :   Monitoring Error.

        enumerator I3C\_ERROR\_CE2
        :   No response to broadcast address (0x7E).

        enumerator I3C\_ERROR\_CE3
        :   Failed Controller Handoff.

        enumerator I3C\_ERROR\_CE\_UNKNOWN
        :   Unknown error (not official error code).

        enumerator I3C\_ERROR\_CE\_NONE
        :   No error (not official error code).

        enumerator I3C\_ERROR\_CE\_MAX = [I3C\_ERROR\_CE\_UNKNOWN](#c.i3c_sdr_controller_error_codes.I3C_ERROR_CE_UNKNOWN)

        enumerator I3C\_ERROR\_CE\_INVALID

    enum i3c\_sdr\_target\_error\_codes
    :   I3C SDR Target Error Codes.

        These are error codes defined by the I3C specification.

        `I3C_ERROR_TE_UNKNOWN` and `I3C_ERROR_TE_NONE` are not official error codes according to the specification. These are there simply to aid in error handling during interactions with the I3C drivers and subsystem.

        *Values:*

        enumerator I3C\_ERROR\_TE0
        :   Invalid Broadcast Address or Dynamic Address after DA assignment.

        enumerator I3C\_ERROR\_TE1
        :   CCC Code.

        enumerator I3C\_ERROR\_TE2
        :   Write Data.

        enumerator I3C\_ERROR\_TE3
        :   Assigned Address during Dynamic Address Arbitration.

        enumerator I3C\_ERROR\_TE4
        :   0x7E/R missing after RESTART during Dynamic Address Arbitration

        enumerator I3C\_ERROR\_TE5
        :   Transaction after detecting CCC.

        enumerator I3C\_ERROR\_TE6
        :   Monitoring Error.

        enumerator I3C\_ERROR\_DBR
        :   Dead Bus Recovery.

        enumerator I3C\_ERROR\_TE\_UNKNOWN
        :   Unknown error (not official error code).

        enumerator I3C\_ERROR\_TE\_NONE
        :   No error (not official error code).

        enumerator I3C\_ERROR\_TE\_MAX = [I3C\_ERROR\_TE\_UNKNOWN](#c.i3c_sdr_target_error_codes.I3C_ERROR_TE_UNKNOWN)

        enumerator I3C\_ERROR\_TE\_INVALID

    enum i3c\_config\_type
    :   Type of configuration being passed to configure function.

        *Values:*

        enumerator I3C\_CONFIG\_CONTROLLER

        enumerator I3C\_CONFIG\_TARGET

        enumerator I3C\_CONFIG\_CUSTOM

    Functions

    struct [i3c\_device\_desc](#c.i3c_device_desc) \*i3c\_dev\_list\_find(const struct [i3c\_dev\_list](#c.i3c_dev_list) \*dev\_list, const struct [i3c\_device\_id](#c.i3c_device_id) \*id)
    :   Find a I3C target device descriptor by ID.

        This finds the I3C target device descriptor in the device list matching the provided ID struct (`id`).

        Parameters:
        :   - **dev\_list** – Pointer to the device list struct.
            - **id** – Pointer to I3C device ID struct.

        Returns:
        :   Pointer to the I3C target device descriptor, or NULL if none is found.

    struct [i3c\_device\_desc](#c.i3c_device_desc) \*i3c\_dev\_list\_i3c\_addr\_find(struct [i3c\_dev\_attached\_list](#c.i3c_dev_attached_list) \*dev\_list, uint8\_t addr)
    :   Find a I3C target device descriptor by dynamic address.

        This finds the I3C target device descriptor in the attached device list matching the dynamic address (`addr`)

        Parameters:
        :   - **dev\_list** – Pointer to the device list struct.
            - **addr** – Dynamic address to be matched.

        Returns:
        :   Pointer to the I3C target device descriptor, or NULL if none is found.

    struct [i3c\_i2c\_device\_desc](#c.i3c_i2c_device_desc) \*i3c\_dev\_list\_i2c\_addr\_find(struct [i3c\_dev\_attached\_list](#c.i3c_dev_attached_list) \*dev\_list, uint16\_t addr)
    :   Find a I2C target device descriptor by address.

        This finds the I2C target device descriptor in the attached device list matching the address (`addr`)

        Parameters:
        :   - **dev\_list** – Pointer to the device list struct.
            - **addr** – Address to be matched.

        Returns:
        :   Pointer to the I2C target device descriptor, or NULL if none is found.

    int i3c\_determine\_default\_addr(struct [i3c\_device\_desc](#c.i3c_device_desc) \*target, uint8\_t \*addr)
    :   Helper function to find the default address an i3c device is attached with.

        This is a helper function to find the default address the device will be loaded with. This could be either it’s static address, a requested dynamic address, or just a dynamic address that is available

        Parameters:
        :   - **target** – **[in]** The pointer of the device descriptor
            - **addr** – **[out]** Address to be assigned to target device.

        Return values:
        :   - **0** – if successful.
            - **-EINVAL** – if the expected default address is already in use

    int i3c\_dev\_list\_daa\_addr\_helper(struct [i3c\_addr\_slots](#c.i3c_addr_slots) \*addr\_slots, const struct [i3c\_dev\_list](#c.i3c_dev_list) \*dev\_list, uint64\_t pid, bool must\_match, bool assigned\_okay, struct [i3c\_device\_desc](#c.i3c_device_desc) \*\*target, uint8\_t \*addr)
    :   Helper function to find a usable address during ENTDAA.

        This is a helper function to find a usable address during Dynamic Address Assignment. Given the PID (`pid`

        ), it will search through the device list for the matching device descriptor. If the device descriptor indicates that there is a preferred address (i.e. assigned-address in device tree,

        If

        `must_match` is true, the PID (`pid`) must match one of the device in the device list.

        See also

        [i3c\_device\_desc::init\_dynamic\_addr](#structi3c__device__desc_1a0477ac021d81431a34f55fa1c9f04bb5)), this preferred address will be returned if this address is still available. If it is not available, another free address will be returned.

        If `must_match` is false, this will return an arbitrary address. This is useful when not all devices are described in device tree. Or else, the DAA process cannot proceed since there is no address to be assigned.

        If `assigned_okay`

        is true, it will return the same address already assigned to the device (

        If

        `assigned_okay` is false, the device cannot have an address assigned already (that

        See also

        [i3c\_device\_desc::dynamic\_addr](#structi3c__device__desc_1a4e4c9614871e5ea4aa08b1560ecc40d0)). If no address has been assigned, it behaves as if `assigned_okay` is false. This is useful for assigning the same address to the same [device](../../kernel/drivers/index.md#structdevice) (for example, hot-join after [device](../../kernel/drivers/index.md#structdevice) coming back from suspend).

        See also

        [i3c\_device\_desc::dynamic\_addr](#structi3c__device__desc_1a4e4c9614871e5ea4aa08b1560ecc40d0) is not zero). This is mainly used during the initial DAA.

        Parameters:
        :   - **addr\_slots** – **[in]** Pointer to address slots struct.
            - **dev\_list** – **[in]** Pointer to the device list struct.
            - **pid** – **[in]** Provisioned ID of device to be assigned address.
            - **must\_match** – **[in]** True if PID must match devices in the device list. False otherwise.
            - **assigned\_okay** – **[in]** True if it is okay to return the address already assigned to the target matching the PID (`pid`).
            - **target** – **[out]** Store the pointer of the device descriptor if it matches the incoming PID (`pid`).
            - **addr** – **[out]** Address to be assigned to target device.

        Return values:
        :   - **0** – if successful.
            - **-ENODEV** – if no device matches the PID (`pid`) in the device list and `must_match` is true.
            - **-EINVAL** – if the device matching PID (`pid`) already has an address assigned or invalid function arguments.

    static inline int i3c\_configure(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [i3c\_config\_type](#c.i3c_config_type) type, void \*config)
    :   Configure the I3C hardware.

        Parameters:
        :   - **dev** – Pointer to controller device driver instance.
            - **type** – Type of configuration parameters being passed in `config`.
            - **config** – Pointer to the configuration parameters.

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – If invalid configure parameters.
            - **-EIO** – General Input/Output errors.
            - **-ENOSYS** – If not implemented.

    static inline int i3c\_config\_get(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [i3c\_config\_type](#c.i3c_config_type) type, void \*config)
    :   Get configuration of the I3C hardware.

        This provides a way to get the current configuration of the I3C hardware.

        This can return cached config or probed hardware parameters, but it has to be up to date with current configuration.

        Note that if `type` is `I3C_CONFIG_CUSTOM`, `config` must contain the ID of the parameter to be retrieved.

        Parameters:
        :   - **dev** – **[in]** Pointer to controller device driver instance.
            - **type** – **[in]** Type of configuration parameters being passed in `config`.
            - **config** – **[inout]** Pointer to the configuration parameters.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General Input/Output errors.
            - **-ENOSYS** – If not implemented.

    static inline int i3c\_recover\_bus(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Attempt bus recovery on the I3C bus.

        This routine asks the controller to attempt bus recovery.

        Return values:
        :   - **0** – If successful.
            - **-EBUSY** – If bus recovery fails.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – Bus recovery is not supported by the controller driver.

    int i3c\_attach\_i3c\_device(struct [i3c\_device\_desc](#c.i3c_device_desc) \*target)
    :   Attach an I3C device.

        Called to attach a I3C device to the addresses. This is typically called before a SETDASA or ENTDAA to reserve the addresses. This will also call the optional api to update any registers within the driver if implemented.

        Warning

        Use cases involving multiple writers to the i3c/i2c devices must prevent concurrent write operations, either by preventing all writers from being preempted or by using a mutex to govern writes to the i3c/i2c devices.

        Parameters:
        :   - **target** – Pointer to the target device descriptor

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – If address is not available or if the device has already been attached before

    int i3c\_reattach\_i3c\_device(struct [i3c\_device\_desc](#c.i3c_device_desc) \*target, uint8\_t old\_dyn\_addr)
    :   Reattach I3C device.

        called after every time an I3C device has its address changed. It can be because the device has been powered down and has lost its address, or it can happen when a device had a static address and has been assigned a dynamic address with SETDASA or a dynamic address has been updated with SETNEWDA. This will also call the optional api to update any registers within the driver if implemented.

        Warning

        Use cases involving multiple writers to the i3c/i2c devices must prevent concurrent write operations, either by preventing all writers from being preempted or by using a mutex to govern writes to the i3c/i2c devices.

        Parameters:
        :   - **target** – Pointer to the target device descriptor
            - **old\_dyn\_addr** – The old dynamic address of target device, 0 if there was no old dynamic address

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – If address is not available

    int i3c\_detach\_i3c\_device(struct [i3c\_device\_desc](#c.i3c_device_desc) \*target)
    :   Detach I3C Device.

        called to remove an I3C device and to free up the address that it used. If it’s dynamic address was not set, then it assumed that SETDASA failed and will free it’s static addr. This will also call the optional api to update any registers within the driver if implemented.

        Warning

        Use cases involving multiple writers to the i3c/i2c devices must prevent concurrent write operations, either by preventing all writers from being preempted or by using a mutex to govern writes to the i3c/i2c devices.

        Parameters:
        :   - **target** – Pointer to the target device descriptor

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – If device is already detached

    int i3c\_attach\_i2c\_device(struct [i3c\_i2c\_device\_desc](#c.i3c_i2c_device_desc) \*target)
    :   Attach an I2C device.

        Called to attach a I2C device to the addresses. This will also call the optional api to update any registers within the driver if implemented.

        Warning

        Use cases involving multiple writers to the i3c/i2c devices must prevent concurrent write operations, either by preventing all writers from being preempted or by using a mutex to govern writes to the i3c/i2c devices.

        Parameters:
        :   - **target** – Pointer to the target device descriptor

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – If address is not available or if the device has already been attached before

    int i3c\_detach\_i2c\_device(struct [i3c\_i2c\_device\_desc](#c.i3c_i2c_device_desc) \*target)
    :   Detach I2C Device.

        called to remove an I2C device and to free up the address that it used. This will also call the optional api to update any registers within the driver if implemented.

        Warning

        Use cases involving multiple writers to the i3c/i2c devices must prevent concurrent write operations, either by preventing all writers from being preempted or by using a mutex to govern writes to the i3c/i2c devices.

        Parameters:
        :   - **target** – Pointer to the target device descriptor

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – If device is already detached

    static inline int i3c\_do\_daa(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Perform Dynamic Address Assignment on the I3C bus.

        This routine asks the controller to perform dynamic address assignment where the controller belongs. Only the active controller of the bus should do this.

        Note

        For controller driver implementation, the controller should perform SETDASA to allow static addresses to be the dynamic addresses before actually doing ENTDAA.

        Parameters:
        :   - **dev** – Pointer to the device structure for the controller driver instance.

        Return values:
        :   - **0** – If successful.
            - **-EBUSY** – Bus is busy.
            - **-EIO** – General input / output error.
            - **-ENODEV** – If a provisioned ID does not match to any target devices in the registered device list.
            - **-ENOSPC** – No more free addresses can be assigned to target.
            - **-ENOSYS** – Dynamic address assignment is not supported by the controller driver.

    int i3c\_do\_ccc(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [i3c\_ccc\_payload](#c.i3c_ccc_payload) \*payload)
    :   Send CCC to the bus.

        Parameters:
        :   - **dev** – Pointer to the device structure for the controller driver instance.
            - **payload** – Pointer to the structure describing the CCC payload.

        Return values:
        :   - **0** – If successful.
            - **-EBUSY** – Bus is busy.
            - **-EIO** – General Input / output error.
            - **-EINVAL** – Invalid valid set in the payload structure.
            - **-ENOSYS** – Not implemented.

    static inline struct [i3c\_device\_desc](#c.i3c_device_desc) \*i3c\_device\_find(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [i3c\_device\_id](#c.i3c_device_id) \*id)
    :   Find a registered I3C target device.

        Controller only API.

        This returns the I3C device descriptor of the I3C device matching the incoming `id`.

        Parameters:
        :   - **dev** – Pointer to controller device driver instance.
            - **id** – Pointer to I3C device ID.

        Returns:
        :   Pointer to I3C device descriptor, or NULL if no I3C device found matching incoming `id`.

    int i3c\_bus\_init(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [i3c\_dev\_list](#c.i3c_bus_init) \*i3c\_dev\_list)
    :   Generic helper function to perform bus initialization.

        Parameters:
        :   - **dev** – Pointer to controller device driver instance.
            - **i3c\_dev\_list** – Pointer to I3C device list.

        Return values:
        :   - **0** – If successful.
            - **-EBUSY** – Bus is busy.
            - **-EIO** – General input / output error.
            - **-ENODEV** – If a provisioned ID does not match to any target devices in the registered device list.
            - **-ENOSPC** – No more free addresses can be assigned to target.
            - **-ENOSYS** – Dynamic address assignment is not supported by the controller driver.

    int i3c\_device\_basic\_info\_get(struct [i3c\_device\_desc](#c.i3c_device_desc) \*target)
    :   Get basic information from device and update device descriptor.

        This retrieves some basic information:

        - Bus Characteristics Register (GETBCR)
        - Device Characteristics Register (GETDCR)
        - Max Read Length (GETMRL)
        - Max Write Length (GETMWL) from the device and update the corresponding fields of the device descriptor.

        This only updates the field(s) in device descriptor only if CCC operations succeed.

        Parameters:
        :   - **target** – **[inout]** I3C target device descriptor.

        Return values:
        :   - **0** – if successful.
            - **-EIO** – General Input/Output error.

    struct i3c\_config\_controller
    :   *#include <i3c.h>*

        Configuration parameters for I3C hardware to act as controller.

        Public Members

        bool is\_secondary
        :   True if the controller is to be the secondary controller of the bus.

            False to be the primary controller.

        uint32\_t i3c
        :   SCL frequency (in Hz) for I3C transfers.

        uint32\_t i2c
        :   SCL frequency (in Hz) for I2C transfers.

        uint8\_t supported\_hdr
        :   Bit mask of supported HDR modes (0 - 7).

            This can be used to enable or disable HDR mode supported by the hardware at runtime.

    struct i3c\_config\_custom
    :   *#include <i3c.h>*

        Custom I3C configuration parameters.

        This can be used to configure the I3C hardware on parameters not covered by

        See also

        [i3c\_config\_controller](#structi3c__config__controller) or

        See also

        [i3c\_config\_target](#structi3c__config__target). Mostly used to configure vendor specific parameters of the I3C hardware.

        Public Members

        uint32\_t id
        :   ID of the configuration parameter.

        uintptr\_t val
        :   Value of configuration parameter.

        void \*ptr
        :   Pointer to configuration parameter.

            Mainly used to pointer to a struct that the device driver understands.

    struct i3c\_device\_id
    :   *#include <i3c.h>*

        Structure used for matching I3C devices.

        Public Members

        const uint64\_t pid
        :   Device Provisioned ID.

    struct i3c\_device\_desc
    :   *#include <i3c.h>*

        Structure describing a I3C target device.

        Instances of this are passed to the I3C controller device APIs, for example:

        - i3c\_device\_register() to tell the controller of a target device.
        - i3c\_transfers() to initiate data transfers between controller and target device.

        Fields `bus`, `pid` and `static_addr` must be initialized by the module that implements the target device behavior prior to passing the object reference to I3C controller device APIs. `static_addr` can be zero if target device does not have static address.

        Field `node` should not be initialized or modified manually.

        Public Members

        const struct [device](../../kernel/drivers/index.md#c.device "device") \*const bus
        :   Used to attach this node onto a linked list.

            I3C bus to which this target device is attached

        const struct [device](../../kernel/drivers/index.md#c.device "device") \*const dev
        :   Device driver instance of the I3C device.

        const uint64\_t pid
        :   Device Provisioned ID.

        const uint8\_t static\_addr
        :   Static address for this target device.

            0 if static address is not being used, and only dynamic address is used. This means that the target device must go through ENTDAA (Dynamic Address Assignment) to get a dynamic address before it can communicate with the controller. This means SETAASA and SETDASA CCC cannot be used to set dynamic address on the target device (as both are to tell target device to use static address as dynamic address).

        const uint8\_t init\_dynamic\_addr
        :   Initial dynamic address.

            This is specified in the device tree property “assigned-address” to indicate the desired dynamic address during address assignment (SETDASA and ENTDAA).

            0 if there is no preference.

        uint8\_t dynamic\_addr
        :   Dynamic Address for this target device used for communication.

            This is to be set by the controller driver in one of the following situations:

            - During Dynamic Address Assignment (during ENTDAA)
            - Reset Dynamic Address Assignment (RSTDAA)
            - Set All Addresses to Static Addresses (SETAASA)
            - Set New Dynamic Address (SETNEWDA)
            - Set Dynamic Address from Static Address (SETDASA)

            0 if address has not been assigned.

        uint8\_t group\_addr
        :   Group address for this target device.

            Set during:

            - Reset Group Address(es) (RSTGRPA)
            - Set Group Address (SETGRPA)

            0 if group address has not been assigned.

        uint8\_t bcr
        :   Bus Characteristic Register (BCR).

            - BCR[7:6]: Device Role

              - 0: I3C Target
              - 1: I3C Controller capable
              - 2: Reserved
              - 3: Reserved
            - BCR[5]: Advanced Capabilities

              - 0: Does not support optional advanced capabilities.
              - 1: Supports optional advanced capabilities which can be viewed via GETCAPS CCC.
            - BCR[4}: Virtual Target Support

              - 0: Is not a virtual target.
              - 1: Is a virtual target.
            - BCR[3]: Offline Capable

              - 0: Will always response to I3C commands.
              - 1: Will not always response to I3C commands.
            - BCR[2]: IBI Payload

              - 0: No data bytes following the accepted IBI.
              - 1: One data byte (MDB, Mandatory Data Byte) follows the accepted IBI. Additional data bytes may also follows.
            - BCR[1]: IBI Request Capable

              - 0: Not capable
              - 1: Capable
            - BCR[0]: Max Data Speed Limitation

              - 0: No Limitation
              - 1: Limitation obtained via GETMXDS CCC.

        uint8\_t dcr
        :   Device Characteristic Register (DCR).

            Describes the type of device. Refer to official documentation on what this number means.

        uint8\_t maxrd
        :   Maximum Read Speed.

        uint8\_t maxwr
        :   Maximum Write Speed.

        uint32\_t max\_read\_turnaround
        :   Maximum Read turnaround time in microseconds.

        uint16\_t mrl
        :   Maximum Read Length.

        uint16\_t mwl
        :   Maximum Write Length.

        uint8\_t max\_ibi
        :   Maximum IBI Payload Size.

            Valid only if BCR[2] is 1.

        uint8\_t gethdrcap
        :   I3C v1.0 HDR Capabilities (`I3C_CCC_GETCAPS1_*`).

            - Bit[0]: HDR-DDR
            - Bit[1]: HDR-TSP
            - Bit[2]: HDR-TSL
            - Bit[7:3]: Reserved

        uint8\_t getcap1
        :   I3C v1.1+ GETCAPS1 (`I3C_CCC_GETCAPS1_*`).

            - Bit[0]: HDR-DDR
            - Bit[1]: HDR-TSP
            - Bit[2]: HDR-TSL
            - Bit[3]: HDR-BT
            - Bit[7:4]: Reserved

        uint8\_t getcap2
        :   GETCAPS2 (`I3C_CCC_GETCAPS2_*`).

            - Bit[3:0]: I3C 1.x Specification Version
            - Bit[5:4]: Group Address Capabilities
            - Bit[6]: HDR-DDR Write Abort
            - Bit[7]: HDR-DDR Abort CRC

        uint8\_t getcap3
        :   GETCAPS3 (`I3C_CCC_GETCAPS3_*`).

            - Bit[0]: Multi-Lane (ML) Data Transfer Support
            - Bit[1]: Device to Device Transfer (D2DXFER) Support
            - Bit[2]: Device to Device Transfer (D2DXFER) IBI Capable
            - Bit[3]: Defining Byte Support in GETCAPS
            - Bit[4]: Defining Byte Support in GETSTATUS
            - Bit[5]: HDR-BT CRC-32 Support
            - Bit[6]: IBI MDB Support for Pending Read Notification
            - Bit[7]: Reserved

        uint8\_t getcap4
        :   GETCAPS4.

            - Bit[7:0]: Reserved

        struct [i3c\_device\_desc](#c.i3c_device_desc).[anonymous] getcaps
        :   Describes advanced (Target) capabilities and features.

        i3c\_target\_ibi\_cb\_t ibi\_cb
        :   Private data by the controller to aid in transactions.

            Do not modify. In-Band Interrupt (IBI) callback.

    struct i3c\_i2c\_device\_desc
    :   *#include <i3c.h>*

        Structure describing a I2C device on I3C bus.

        Instances of this are passed to the I3C controller device APIs, for example: () i3c\_i2c\_device\_register() to tell the controller of an I2C device. () i3c\_i2c\_transfers() to initiate data transfers between controller and I2C device.

        Fields other than `node` must be initialized by the module that implements the device behavior prior to passing the object reference to I3C controller device APIs.

        Public Members

        const struct [device](../../kernel/drivers/index.md#c.device "device") \*bus
        :   Used to attach this node onto a linked list.

            I3C bus to which this I2C device is attached

        const uint16\_t addr
        :   Static address for this I2C device.

        const uint8\_t lvr
        :   Legacy Virtual Register (LVR).

            - LVR[7:5]: I2C device index:

              - 0: I2C device has a 50 ns spike filter where it is not affected by high frequency on SCL.
              - 1: I2C device does not have a 50 ns spike filter but can work with high frequency on SCL.
              - 2: I2C device does not have a 50 ns spike filter and cannot work with high frequency on SCL.
            - LVR[4]: I2C mode indicator:

              - 0: FM+ mode
              - 1: FM mode
            - LVR[3:0]: Reserved.

    struct i3c\_dev\_attached\_list
    :   *#include <i3c.h>*

        Structure for describing attached devices for a controller.

        This contains slists of attached I3C and I2C devices.

        This is a helper struct that can be used by controller device driver to aid in device management.

        Public Members

        struct [i3c\_addr\_slots](#c.i3c_addr_slots) addr\_slots
        :   Address slots:

            - Aid in dynamic address assignment.
            - Quick way to find out if a target address is a I3C or I2C device.

        [sys\_slist\_t](../../kernel/data_structures/slist.md#c.sys_slist_t "sys_slist_t") i3c
        :   Linked list of attached I3C devices.

        [sys\_slist\_t](../../kernel/data_structures/slist.md#c.sys_slist_t "sys_slist_t") i2c
        :   Linked list of attached I2C devices.

    struct i3c\_dev\_list
    :   *#include <i3c.h>*

        Structure for describing known devices for a controller.

        This contains arrays of known I3C and I2C devices.

        This is a helper struct that can be used by controller device driver to aid in device management.

        Public Members

        struct [i3c\_device\_desc](#c.i3c_device_desc) \*const i3c
        :   Pointer to array of known I3C devices.

        struct [i3c\_i2c\_device\_desc](#c.i3c_i2c_device_desc) \*const i2c
        :   Pointer to array of known I2C devices.

        const uint8\_t num\_i3c
        :   Number of I3C devices in array.

        const uint8\_t num\_i2c
        :   Number of I2C devices in array.

    struct i3c\_driver\_config
    :   *#include <i3c.h>*

        This structure is common to all I3C drivers and is expected to be the first element in the object pointed to by the config field in the device structure.

        Public Members

        struct [i3c\_dev\_list](#c.i3c_dev_list) dev\_list
        :   I3C/I2C device list struct.

    struct i3c\_driver\_data
    :   *#include <i3c.h>*

        This structure is common to all I3C drivers and is expected to be the first element in the driver’s struct driver\_data declaration.

        Public Members

        struct [i3c\_config\_controller](#c.i3c_config_controller) ctrl\_config
        :   Controller Configuration.

        struct [i3c\_dev\_attached\_list](#c.i3c_dev_attached_list) attached\_dev
        :   Attached I3C/I2C devices and addresses.

*group* I3C Common Command Codes
:   I3C Common Command Codes.

    Defines

    I3C\_CCC\_BROADCAST\_MAX\_ID
    :   Maximum CCC ID for broadcast.

    I3C\_CCC\_ENEC(broadcast)
    :   Enable Events Command.

        Parameters:
        :   - **broadcast** – True if broadcast, false if direct.

    I3C\_CCC\_DISEC(broadcast)
    :   Disable Events Command.

        Parameters:
        :   - **broadcast** – True if broadcast, false if direct.

    I3C\_CCC\_ENTAS(as, broadcast)
    :   Enter Activity State.

        Parameters:
        :   - **as** – Desired activity state
            - **broadcast** – True if broadcast, false if direct.

    I3C\_CCC\_ENTAS0(broadcast)
    :   Enter Activity State 0.

        Parameters:
        :   - **broadcast** – True if broadcast, false if direct.

    I3C\_CCC\_ENTAS1(broadcast)
    :   Enter Activity State 1.

        Parameters:
        :   - **broadcast** – True if broadcast, false if direct.

    I3C\_CCC\_ENTAS2(broadcast)
    :   Enter Activity State 2.

        Parameters:
        :   - **broadcast** – True if broadcast, false if direct.

    I3C\_CCC\_ENTAS3(broadcast)
    :   Enter Activity State 3.

        Parameters:
        :   - **broadcast** – True if broadcast, false if direct.

    I3C\_CCC\_RSTDAA
    :   Reset Dynamic Address Assignment (Broadcast).

    I3C\_CCC\_ENTDAA
    :   Enter Dynamic Address Assignment (Broadcast).

    I3C\_CCC\_DEFTGTS
    :   Define List of Targets (Broadcast).

    I3C\_CCC\_SETMWL(broadcast)
    :   Set Max Write Length (Broadcast or Direct).

        Parameters:
        :   - **broadcast** – True if broadcast, false if direct.

    I3C\_CCC\_SETMRL(broadcast)
    :   Set Max Read Length (Broadcast or Direct).

        Parameters:
        :   - **broadcast** – True if broadcast, false if direct.

    I3C\_CCC\_ENTTM
    :   Enter Test Mode (Broadcast).

    I3C\_CCC\_SETBUSCON
    :   Set Bus Context (Broadcast).

    I3C\_CCC\_ENDXFER(broadcast)
    :   Data Transfer Ending Procedure Control.

        Parameters:
        :   - **broadcast** – True if broadcast, false if direct.

    I3C\_CCC\_ENTHDR(x)
    :   Enter HDR Mode (HDR-DDR) (Broadcast).

    I3C\_CCC\_ENTHDR0
    :   Enter HDR Mode 0 (HDR-DDR) (Broadcast).

    I3C\_CCC\_ENTHDR1
    :   Enter HDR Mode 1 (HDR-TSP) (Broadcast).

    I3C\_CCC\_ENTHDR2
    :   Enter HDR Mode 2 (HDR-TSL) (Broadcast).

    I3C\_CCC\_ENTHDR3
    :   Enter HDR Mode 3 (HDR-BT) (Broadcast).

    I3C\_CCC\_ENTHDR4
    :   Enter HDR Mode 4 (Broadcast).

    I3C\_CCC\_ENTHDR5
    :   Enter HDR Mode 5 (Broadcast).

    I3C\_CCC\_ENTHDR6
    :   Enter HDR Mode 6 (Broadcast).

    I3C\_CCC\_ENTHDR7
    :   Enter HDR Mode 7 (Broadcast).

    I3C\_CCC\_SETXTIME(broadcast)
    :   Exchange Timing Information (Broadcast or Direct).

        Parameters:
        :   - **broadcast** – True if broadcast, false if direct.

    I3C\_CCC\_SETAASA
    :   Set All Addresses to Static Addresses (Broadcast).

    I3C\_CCC\_RSTACT(broadcast)
    :   Target Reset Action.

        Parameters:
        :   - **broadcast** – True if broadcast, false if direct.

    I3C\_CCC\_DEFGRPA
    :   Define List of Group Address (Broadcast).

    I3C\_CCC\_RSTGRPA(broadcast)
    :   Reset Group Address.

        Parameters:
        :   - **broadcast** – True if broadcast, false if direct.

    I3C\_CCC\_MLANE(broadcast)
    :   Multi-Lane Data Transfer Control (Broadcast).

    I3C\_CCC\_VENDOR(broadcast, id)
    :   Vendor/Standard Extension.

        Parameters:
        :   - **broadcast** – True if broadcast, false if direct.
            - **id** – Extension ID.

    I3C\_CCC\_SETDASA
    :   Set Dynamic Address from Static Address (Direct).

    I3C\_CCC\_SETNEWDA
    :   Set New Dynamic Address (Direct).

    I3C\_CCC\_GETMWL
    :   Get Max Write Length (Direct).

    I3C\_CCC\_GETMRL
    :   Get Max Read Length (Direct).

    I3C\_CCC\_GETPID
    :   Get Provisioned ID (Direct).

    I3C\_CCC\_GETBCR
    :   Get Bus Characteristics Register (Direct).

    I3C\_CCC\_GETDCR
    :   Get Device Characteristics Register (Direct).

    I3C\_CCC\_GETSTATUS
    :   Get Device Status (Direct).

    I3C\_CCC\_GETACCCR
    :   Get Accept Controller Role (Direct).

    I3C\_CCC\_SETBRGTGT
    :   Set Bridge Targets (Direct).

    I3C\_CCC\_GETMXDS
    :   Get Max Data Speed (Direct).

    I3C\_CCC\_GETCAPS
    :   Get Optional Feature Capabilities (Direct).

    I3C\_CCC\_SETROUTE
    :   Set Route (Direct).

    I3C\_CCC\_D2DXFER
    :   Device to Device(s) Tunneling Control (Direct).

    I3C\_CCC\_GETXTIME
    :   Get Exchange Timing Information (Direct).

    I3C\_CCC\_SETGRPA
    :   Set Group Address (Direct).

    I3C\_CCC\_ENEC\_EVT\_ENINTR
    :   Enable Events (ENEC) - Target Interrupt Requests.

    I3C\_CCC\_ENEC\_EVT\_ENCR
    :   Enable Events (ENEC) - Controller Role Requests.

    I3C\_CCC\_ENEC\_EVT\_ENHJ
    :   Enable Events (ENEC) - Hot-Join Event.

    I3C\_CCC\_ENEC\_EVT\_ALL

    I3C\_CCC\_DISEC\_EVT\_DISINTR
    :   Disable Events (DISEC) - Target Interrupt Requests.

    I3C\_CCC\_DISEC\_EVT\_DISCR
    :   Disable Events (DISEC) - Controller Role Requests.

    I3C\_CCC\_DISEC\_EVT\_DISHJ
    :   Disable Events (DISEC) - Hot-Join Event.

    I3C\_CCC\_DISEC\_EVT\_ALL

    I3C\_CCC\_EVT\_INTR
    :   Events - Target Interrupt Requests.

    I3C\_CCC\_EVT\_CR
    :   Events - Controller Role Requests.

    I3C\_CCC\_EVT\_HJ
    :   Events - Hot-Join Event.

    I3C\_CCC\_EVT\_ALL
    :   Bitmask for all events.

    I3C\_CCC\_GETSTATUS\_PROTOCOL\_ERR
    :   GETSTATUS Format 1 - Protocol Error bit.

    I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_SHIFT
    :   GETSTATUS Format 1 - Activity Mode bit shift value.

    I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_MASK
    :   GETSTATUS Format 1 - Activity Mode bitmask.

    I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE(status)
    :   GETSTATUS Format 1 - Activity Mode.

        Obtain Activity Mode from GETSTATUS Format 1 value obtained via GETSTATUS.

        Parameters:
        :   - **status** – GETSTATUS Format 1 value

    I3C\_CCC\_GETSTATUS\_NUM\_INT\_SHIFT
    :   GETSTATUS Format 1 - Number of Pending Interrupts bit shift value.

    I3C\_CCC\_GETSTATUS\_NUM\_INT\_MASK
    :   GETSTATUS Format 1 - Number of Pending Interrupts bitmask.

    I3C\_CCC\_GETSTATUS\_NUM\_INT(status)
    :   GETSTATUS Format 1 - Number of Pending Interrupts.

        Obtain Number of Pending Interrupts from GETSTATUS Format 1 value obtained via GETSTATUS.

        Parameters:
        :   - **status** – GETSTATUS Format 1 value

    I3C\_CCC\_GETSTATUS\_PRECR\_DEEP\_SLEEP\_DETECTED
    :   GETSTATUS Format 2 - PERCR - Deep Sleep Detected bit.

    I3C\_CCC\_GETSTATUS\_PRECR\_HANDOFF\_DELAY\_NACK
    :   GETSTATUS Format 2 - PERCR - Handoff Delay NACK.

    I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_MAX
    :   Get Max Data Speed (GETMXDS) - Default Max Sustained Data Rate.

    I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_8MHZ
    :   Get Max Data Speed (GETMXDS) - 8MHz Max Sustained Data Rate.

    I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_6MHZ
    :   Get Max Data Speed (GETMXDS) - 6MHz Max Sustained Data Rate.

    I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_4MHZ
    :   Get Max Data Speed (GETMXDS) - 4MHz Max Sustained Data Rate.

    I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_2MHZ
    :   Get Max Data Speed (GETMXDS) - 2MHz Max Sustained Data Rate.

    I3C\_CCC\_GETMXDS\_TSCO\_8NS
    :   Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 8ns.

    I3C\_CCC\_GETMXDS\_TSCO\_9NS
    :   Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 9ns.

    I3C\_CCC\_GETMXDS\_TSCO\_10NS
    :   Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 10ns.

    I3C\_CCC\_GETMXDS\_TSCO\_11NS
    :   Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 11ns.

    I3C\_CCC\_GETMXDS\_TSCO\_12NS
    :   Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 12ns.

    I3C\_CCC\_GETMXDS\_TSCO\_GT\_12NS
    :   Get Max Data Speed (GETMXDS) - Clock to Data Turnaround > 12ns.

    I3C\_CCC\_GETMXDS\_MAXWR\_DEFINING\_BYTE\_SUPPORT
    :   Get Max Data Speed (GETMXDS) - maxWr - Optional Defining Byte Support.

    I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_SHIFT
    :   Get Max Data Speed (GETMXDS) - Max Sustained Data Rate bit shift value.

    I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_MASK
    :   Get Max Data Speed (GETMXDS) - Max Sustained Data Rate bitmask.

    I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL(maxwr)
    :   Get Max Data Speed (GETMXDS) - maxWr - Max Sustained Data Rate.

        Obtain Max Sustained Data Rate value from GETMXDS maxWr value obtained via GETMXDS.

        Parameters:
        :   - **maxwr** – GETMXDS maxWr value.

    I3C\_CCC\_GETMXDS\_MAXRD\_W2R\_PERMITS\_STOP\_BETWEEN
    :   Get Max Data Speed (GETMXDS) - maxRd - Write-to-Read Permits Stop Between.

    I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_SHIFT
    :   Get Max Data Speed (GETMXDS) - maxRd - Clock to Data Turnaround bit shift value.

    I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_MASK
    :   Get Max Data Speed (GETMXDS) - maxRd - Clock to Data Turnaround bitmask.

    I3C\_CCC\_GETMXDS\_MAXRD\_TSCO(maxrd)
    :   Get Max Data Speed (GETMXDS) - maxRd - Clock to Data Turnaround.

        Obtain Clock to Data Turnaround value from GETMXDS maxRd value obtained via GETMXDS.

        Parameters:
        :   - **maxrd** – GETMXDS maxRd value.

    I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_SHIFT
    :   Get Max Data Speed (GETMXDS) - maxRd - Max Sustained Data Rate bit shift value.

    I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_MASK
    :   Get Max Data Speed (GETMXDS) - maxRd - Max Sustained Data Rate bitmask.

    I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL(maxrd)
    :   Get Max Data Speed (GETMXDS) - maxRd - Max Sustained Data Rate.

        Obtain Max Sustained Data Rate value from GETMXDS maxRd value obtained via GETMXDS.

        Parameters:
        :   - **maxrd** – GETMXDS maxRd value.

    I3C\_CCC\_GETMXDS\_CRDHLY1\_SET\_BUS\_ACT\_STATE
    :   Get Max Data Speed (GETMXDS) - CRDHLY1 - Set Bus Activity State bit shift value.

    I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE\_SHIFT
    :   Get Max Data Speed (GETMXDS) - CRDHLY1 - Controller Handoff Activity State bit shift value.

    I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE\_MASK
    :   Get Max Data Speed (GETMXDS) - CRDHLY1 - Controller Handoff Activity State bitmask.

    I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE(crhdly1)
    :   Get Max Data Speed (GETMXDS) - CRDHLY1 - Controller Handoff Activity State.

        Obtain Controller Handoff Activity State value from GETMXDS value obtained via GETMXDS.

        Parameters:
        :   - **crhdly1** – GETMXDS value.

    I3C\_CCC\_GETCAPS1\_HDR\_DDR
    :   Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR-DDR mode bit.

    I3C\_CCC\_GETCAPS1\_HDR\_TSP
    :   Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR-TSP mode bit.

    I3C\_CCC\_GETCAPS1\_HDR\_TSL
    :   Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR-TSL mode bit.

    I3C\_CCC\_GETCAPS1\_HDR\_BT
    :   Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR-BT mode bit.

    I3C\_CCC\_GETCAPS1\_HDR\_MODE(x)
    :   Get Optional Feature Capabilities Byte 1 (GETCAPS) - HDR Mode.

        Get the bit corresponding to HDR mode.

        Parameters:
        :   - **x** – HDR mode

    I3C\_CCC\_GETCAPS1\_HDR\_MODE0
    :   Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR Mode 0.

    I3C\_CCC\_GETCAPS1\_HDR\_MODE1
    :   Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR Mode 1.

    I3C\_CCC\_GETCAPS1\_HDR\_MODE2
    :   Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR Mode 2.

    I3C\_CCC\_GETCAPS1\_HDR\_MODE3
    :   Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR Mode 3.

    I3C\_CCC\_GETCAPS1\_HDR\_MODE4
    :   Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR Mode 4.

    I3C\_CCC\_GETCAPS1\_HDR\_MODE5
    :   Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR Mode 5.

    I3C\_CCC\_GETCAPS1\_HDR\_MODE6
    :   Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR Mode 6.

    I3C\_CCC\_GETCAPS1\_HDR\_MODE7
    :   Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR Mode 7.

    I3C\_CCC\_GETCAPS2\_HDRDDR\_WRITE\_ABORT
    :   Get Optional Feature Capabilities Byte 2 (GETCAPS) Format 1 - HDR-DDR Write Abort bit.

    I3C\_CCC\_GETCAPS2\_HDRDDR\_ABORT\_CRC
    :   Get Optional Feature Capabilities Byte 2 (GETCAPS) Format 1 - HDR-DDR Abort CRC bit.

    I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_SHIFT
    :   Get Optional Feature Capabilities Byte 2 (GETCAPS) Format 1 - Group Address Capabilities bit shift value.

    I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_MASK
    :   Get Optional Feature Capabilities Byte 2 (GETCAPS) Format 1 - Group Address Capabilities bitmask.

    I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP(getcaps2)
    :   Get Optional Feature Capabilities Byte 2 (GETCAPS) Format 1 - Group Address Capabilities.

        Obtain Group Address Capabilities value from GETCAPS Format 1 value obtained via GETCAPS.

        Parameters:
        :   - **getcaps2** – GETCAPS2 value.

    I3C\_CCC\_GETCAPS2\_SPEC\_VER\_SHIFT
    :   Get Optional Feature Capabilities Byte 2 (GETCAPS) Format 1 - I3C 1.x Specification Version bit shift value.

    I3C\_CCC\_GETCAPS2\_SPEC\_VER\_MASK
    :   Get Optional Feature Capabilities Byte 2 (GETCAPS) Format 1 - I3C 1.x Specification Version bitmask.

    I3C\_CCC\_GETCAPS2\_SPEC\_VER(getcaps2)
    :   Get Optional Feature Capabilities Byte 2 (GETCAPS) Format 1 - I3C 1.x Specification Version.

        Obtain I3C 1.x Specification Version value from GETCAPS Format 1 value obtained via GETCAPS.

        Parameters:
        :   - **getcaps2** – GETCAPS2 value.

    I3C\_CCC\_GETCAPS3\_MLANE\_SUPPORT
    :   Get Optional Feature Capabilities Byte 3 (GETCAPS) Format 1 - Multi-Lane Data Transfer Support bit.

    I3C\_CCC\_GETCAPS3\_D2DXFER\_SUPPORT
    :   Get Optional Feature Capabilities Byte 3 (GETCAPS) Format 1 - Device to Device Transfer (D2DXFER) Support bit.

    I3C\_CCC\_GETCAPS3\_D2DXFER\_IBI\_CAPABLE
    :   Get Optional Feature Capabilities Byte 3 (GETCAPS) Format 1 - Device to Device Transfer (D2DXFER) IBI Capable bit.

    I3C\_CCC\_GETCAPS3\_GETCAPS\_DEFINING\_BYTE\_SUPPORT
    :   Get Optional Feature Capabilities Byte 3 (GETCAPS) Format 1 - Defining Byte Support in GETCAPS bit.

    I3C\_CCC\_GETCAPS3\_GETSTATUS\_DEFINING\_BYTE\_SUPPORT
    :   Get Optional Feature Capabilities Byte 3 (GETCAPS) Format 1 - Defining Byte Support in GETSTATUS bit.

    I3C\_CCC\_GETCAPS3\_HDRBT\_CRC32\_SUPPORT
    :   Get Optional Feature Capabilities Byte 3 (GETCAPS) Format 1 - HDR-BT CRC-32 Support bit.

    I3C\_CCC\_GETCAPS3\_IBI\_MDR\_PENDING\_READ\_NOTIFICATION
    :   Get Optional Feature Capabilities Byte 3 (GETCAPS) Format 1 - IBI MDB Support for Pending Read Notification bit.

    I3C\_CCC\_GETCAPS\_TESTPAT1
    :   Get Fixed Test Pattern (GETCAPS) Format 2 - Fixed Test Pattern Byte 1.

    I3C\_CCC\_GETCAPS\_TESTPAT2
    :   Get Fixed Test Pattern (GETCAPS) Format 2 - Fixed Test Pattern Byte 2.

    I3C\_CCC\_GETCAPS\_TESTPAT3
    :   Get Fixed Test Pattern (GETCAPS) Format 2 - Fixed Test Pattern Byte 3.

    I3C\_CCC\_GETCAPS\_TESTPAT4
    :   Get Fixed Test Pattern (GETCAPS) Format 2 - Fixed Test Pattern Byte 4.

    I3C\_CCC\_GETCAPS\_TESTPAT
    :   Get Fixed Test Pattern (GETCAPS) Format 2 - Fixed Test Pattern Word in Big Endian.

    I3C\_CCC\_GETCAPS\_CRCAPS1\_HJ\_SUPPORT
    :   Get Controller Handoff Capabilities Byte 1 (GETCAPS) Format 2 - Hot-Join Support.

    I3C\_CCC\_GETCAPS\_CRCAPS1\_GRP\_MANAGEMENT\_SUPPORT
    :   Get Controller Handoff Capabilities Byte 1 (GETCAPS) Format 2 - Group Management Support.

    I3C\_CCC\_GETCAPS\_CRCAPS1\_ML\_SUPPORT
    :   Get Controller Handoff Capabilities Byte 1 (GETCAPS) Format 2 - Multi-Lane Support.

    I3C\_CCC\_GETCAPS\_CRCAPS2\_IBI\_TIR\_SUPPORT
    :   Get Controller Handoff Capabilities Byte 2 (GETCAPS) Format 2 - In-Band Interrupt Support.

    I3C\_CCC\_GETCAPS\_CRCAPS2\_CONTROLLER\_PASSBACK
    :   Get Controller Handoff Capabilities Byte 2 (GETCAPS) Format 2 - Controller Pass-Back.

    I3C\_CCC\_GETCAPS\_CRCAPS2\_DEEP\_SLEEP\_CAPABLE
    :   Get Controller Handoff Capabilities Byte 2 (GETCAPS) Format 2 - Deep Sleep Capable.

    I3C\_CCC\_GETCAPS\_CRCAPS2\_DELAYED\_CONTROLLER\_HANDOFF
    :   Get Controller Handoff Capabilities Byte 2 (GETCAPS) Format 2 - Deep Sleep Capable.

    I3C\_CCC\_GETCAPS\_VTCAP1\_VITRUAL\_TARGET\_TYPE\_SHIFT
    :   Get Capabilities (GETCAPS) - VTCAP1 - Virtual Target Type bit shift value.

    I3C\_CCC\_GETCAPS\_VTCAP1\_VITRUAL\_TARGET\_TYPE\_MASK
    :   Get Capabilities (GETCAPS) - VTCAP1 - Virtual Target Type bitmask.

    I3C\_CCC\_GETCAPS\_VTCAP1\_VITRUAL\_TARGET\_TYPE(vtcap1)
    :   Get Capabilities (GETCAPS) - VTCAP1 - Virtual Target Type.

        Obtain Virtual Target Type value from VTCAP1 value obtained via GETCAPS format 2 VTCAP def byte.

        Parameters:
        :   - **vtcap1** – VTCAP1 value.

    I3C\_CCC\_GETCAPS\_VTCAP1\_SIDE\_EFFECTS
    :   Get Virtual Target Capabilities Byte 1 (GETCAPS) Format 2 - Side Effects.

    I3C\_CCC\_GETCAPS\_VTCAP1\_SHARED\_PERIPH\_DETECT
    :   Get Virtual Target Capabilities Byte 1 (GETCAPS) Format 2 - Shared Peripheral Detect.

    I3C\_CCC\_GETCAPS\_VTCAP2\_INTERRUPT\_REQUESTS\_SHIFT
    :   Get Capabilities (GETCAPS) - VTCAP2 - Interrupt Requests bit shift value.

    I3C\_CCC\_GETCAPS\_VTCAP2\_INTERRUPT\_REQUESTS\_MASK
    :   Get Capabilities (GETCAPS) - VTCAP2 - Interrupt Requests bitmask.

    I3C\_CCC\_GETCAPS\_VTCAP2\_INTERRUPT\_REQUESTS(vtcap2)
    :   Get Capabilities (GETCAPS) - VTCAP2 - Interrupt Requests.

        Obtain Interrupt Requests value from VTCAP2 value obtained via GETCAPS format 2 VTCAP def byte.

        Parameters:
        :   - **vtcap2** – VTCAP2 value.

    I3C\_CCC\_GETCAPS\_VTCAP2\_ADDRESS\_REMAPPING
    :   Get Virtual Target Capabilities Byte 2 (GETCAPS) Format 2 - Address Remapping.

    I3C\_CCC\_GETCAPS\_VTCAP2\_BUS\_CONTEXT\_AND\_COND\_SHIFT
    :   Get Capabilities (GETCAPS) - VTCAP2 - Bus Context and Condition bit shift value.

    I3C\_CCC\_GETCAPS\_VTCAP2\_BUS\_CONTEXT\_AND\_COND\_MASK
    :   Get Capabilities (GETCAPS) - VTCAP2 - Bus Context and Condition bitmask.

    I3C\_CCC\_GETCAPS\_VTCAP2\_BUS\_CONTEXT\_AND\_COND(vtcap2)
    :   Get Capabilities (GETCAPS) - VTCAP2 - Bus Context and Condition.

        Obtain Bus Context and Condition value from VTCAP2 value obtained via GETCAPS format 2 VTCAP def byte.

        Parameters:
        :   - **vtcap2** – VTCAP2 value.

    Enums

    enum i3c\_ccc\_getstatus\_fmt
    :   Indicate which format of GETSTATUS to use.

        *Values:*

        enumerator GETSTATUS\_FORMAT\_1
        :   GETSTATUS Format 1.

        enumerator GETSTATUS\_FORMAT\_2
        :   GETSTATUS Format 2.

    enum i3c\_ccc\_getstatus\_defbyte
    :   Defining byte values for GETSTATUS Format 2.

        *Values:*

        enumerator GETSTATUS\_FORMAT\_2\_TGTSTAT = 0x00U
        :   Target status.

        enumerator GETSTATUS\_FORMAT\_2\_PRECR = 0x91U
        :   PRECR - Alternate status format describing Controller-capable device.

        enumerator GETSTATUS\_FORMAT\_2\_INVALID = 0x100U
        :   Invalid defining byte.

    enum i3c\_ccc\_getcaps\_fmt
    :   Indicate which format of GETCAPS to use.

        *Values:*

        enumerator GETCAPS\_FORMAT\_1
        :   GETCAPS Format 1.

        enumerator GETCAPS\_FORMAT\_2
        :   GETCAPS Format 2.

    enum i3c\_ccc\_getcaps\_defbyte
    :   Enum for I3C Get Capabilities (GETCAPS) Format 2 Defining Byte Values.

        *Values:*

        enumerator GETCAPS\_FORMAT\_2\_TGTCAPS = 0x00U
        :   Standard Target capabilities and features.

        enumerator GETCAPS\_FORMAT\_2\_TESTPAT = 0x5AU
        :   Fixed 32b test pattern.

        enumerator GETCAPS\_FORMAT\_2\_CRCAPS = 0x91U
        :   Controller handoff capabilities and features.

        enumerator GETCAPS\_FORMAT\_2\_VTCAPS = 0x93U
        :   Virtual Target capabilities and features.

        enumerator GETCAPS\_FORMAT\_2\_DBGCAPS = 0xD7U
        :   Debug-capable Device capabilities and features.

        enumerator GETCAPS\_FORMAT\_2\_INVALID = 0x100
        :   Invalid defining byte.

    enum i3c\_ccc\_rstact\_defining\_byte
    :   Enum for I3C Reset Action (RSTACT) Defining Byte Values.

        *Values:*

        enumerator I3C\_CCC\_RSTACT\_NO\_RESET = 0x00U
        :   No Reset on Target Reset Pattern.

        enumerator I3C\_CCC\_RSTACT\_PERIPHERAL\_ONLY = 0x01U
        :   Reset the I3C Peripheral Only.

        enumerator I3C\_CCC\_RSTACT\_RESET\_WHOLE\_TARGET = 0x02U
        :   Reset the Whole Target.

        enumerator I3C\_CCC\_RSTACT\_DEBUG\_NETWORK\_ADAPTER = 0x03U
        :   Debug Network Adapter Reset.

        enumerator I3C\_CCC\_RSTACT\_VIRTUAL\_TARGET\_DETECT = 0x04U
        :   Virtual Target Detect.

    Functions

    static inline bool i3c\_ccc\_is\_payload\_broadcast(const struct [i3c\_ccc\_payload](#c.i3c_ccc_payload) \*payload)
    :   Test if I3C CCC payload is for broadcast.

        This tests if the CCC payload is for broadcast.

        Parameters:
        :   - **payload** – **[in]** Pointer to the CCC payload.

        Return values:
        :   - **true** – if payload target is broadcast
            - **false** – if payload target is direct

    int i3c\_ccc\_do\_getbcr(struct [i3c\_device\_desc](#c.i3c_device_desc) \*target, struct [i3c\_ccc\_getbcr](#c.i3c_ccc_getbcr) \*bcr)
    :   Get BCR from a target.

        Helper function to get BCR (Bus Characteristic Register) from target device.

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **target** – **[in]** Pointer to the target device descriptor.
            - **bcr** – **[out]** Pointer to the BCR payload structure.

        Returns:

    int i3c\_ccc\_do\_getdcr(struct [i3c\_device\_desc](#c.i3c_device_desc) \*target, struct [i3c\_ccc\_getdcr](#c.i3c_ccc_getdcr) \*dcr)
    :   Get DCR from a target.

        Helper function to get DCR (Device Characteristic Register) from target device.

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **target** – **[in]** Pointer to the target device descriptor.
            - **dcr** – **[out]** Pointer to the DCR payload structure.

        Returns:

    int i3c\_ccc\_do\_getpid(struct [i3c\_device\_desc](#c.i3c_device_desc) \*target, struct [i3c\_ccc\_getpid](#c.i3c_ccc_getpid) \*pid)
    :   Get PID from a target.

        Helper function to get PID (Provisioned ID) from target device.

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **target** – **[in]** Pointer to the target device descriptor.
            - **pid** – **[out]** Pointer to the PID payload structure.

        Returns:

    int i3c\_ccc\_do\_rstact\_all(const struct [device](../../kernel/drivers/index.md#c.device "device") \*controller, enum [i3c\_ccc\_rstact\_defining\_byte](#c.i3c_ccc_rstact_defining_byte) action)
    :   Broadcast RSTACT to reset I3C Peripheral.

        Helper function to broadcast Target Reset Action (RSTACT) to all connected targets to Reset the I3C Peripheral Only (0x01).

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **controller** – **[in]** Pointer to the controller device driver instance.
            - **action** – **[in]** What reset action to perform.

        Returns:

    int i3c\_ccc\_do\_rstdaa\_all(const struct [device](../../kernel/drivers/index.md#c.device "device") \*controller)
    :   Broadcast RSTDAA to reset dynamic addresses for all targets.

        Helper function to reset dynamic addresses of all connected targets.

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **controller** – **[in]** Pointer to the controller device driver instance.

        Returns:

    int i3c\_ccc\_do\_setdasa(const struct [i3c\_device\_desc](#c.i3c_device_desc) \*target)
    :   Set Dynamic Address from Static Address for a target.

        Helper function to do SETDASA (Set Dynamic Address from Static Address) for a particular target.

        Note this does not update `target` with the new dynamic address.

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **target** – **[in]** Pointer to the target device descriptor where the device is configured with a static address.

        Returns:

    int i3c\_ccc\_do\_setnewda(const struct [i3c\_device\_desc](#c.i3c_device_desc) \*target, struct [i3c\_ccc\_address](#c.i3c_ccc_address) new\_da)
    :   Set New Dynamic Address for a target.

        Helper function to do SETNEWDA(Set New Dynamic Address) for a particular target.

        Note this does not update `target` with the new dynamic address.

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **target** – **[in]** Pointer to the target device descriptor where the device is configured with a static address.
            - **new\_da** – **[in]** Pointer to the new\_da struct.

        Returns:

    int i3c\_ccc\_do\_events\_all\_set(const struct [device](../../kernel/drivers/index.md#c.device "device") \*controller, bool enable, struct [i3c\_ccc\_events](#c.i3c_ccc_events) \*events)
    :   Broadcast ENEC/DISEC to enable/disable target events.

        Helper function to broadcast Target Events Command to enable or disable target events (ENEC/DISEC).

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **controller** – **[in]** Pointer to the controller device driver instance.
            - **enable** – **[in]** ENEC if true, DISEC if false.
            - **events** – **[in]** Pointer to the event struct.

        Returns:

    int i3c\_ccc\_do\_events\_set(struct [i3c\_device\_desc](#c.i3c_device_desc) \*target, bool enable, struct [i3c\_ccc\_events](#c.i3c_ccc_events) \*events)
    :   Direct CCC ENEC/DISEC to enable/disable target events.

        Helper function to send Target Events Command to enable or disable target events (ENEC/DISEC) on a single target.

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **target** – **[in]** Pointer to the target device descriptor.
            - **enable** – **[in]** ENEC if true, DISEC if false.
            - **events** – **[in]** Pointer to the event struct.

        Returns:

    int i3c\_ccc\_do\_setmwl\_all(const struct [device](../../kernel/drivers/index.md#c.device "device") \*controller, const struct [i3c\_ccc\_mwl](#c.i3c_ccc_mwl) \*mwl)
    :   Broadcast SETMWL to Set Maximum Write Length.

        Helper function to do SETMWL (Set Maximum Write Length) to all connected targets.

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **controller** – **[in]** Pointer to the controller device driver instance.
            - **mwl** – **[in]** Pointer to SETMWL payload.

        Returns:

    int i3c\_ccc\_do\_setmwl(const struct [i3c\_device\_desc](#c.i3c_device_desc) \*target, const struct [i3c\_ccc\_mwl](#c.i3c_ccc_mwl) \*mwl)
    :   Single target SETMWL to Set Maximum Write Length.

        Helper function to do SETMWL (Set Maximum Write Length) to one target.

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **target** – **[in]** Pointer to the target device descriptor.
            - **mwl** – **[in]** Pointer to SETMWL payload.

        Returns:

    int i3c\_ccc\_do\_getmwl(const struct [i3c\_device\_desc](#c.i3c_device_desc) \*target, struct [i3c\_ccc\_mwl](#c.i3c_ccc_mwl) \*mwl)
    :   Single target GETMWL to Get Maximum Write Length.

        Helper function to do GETMWL (Get Maximum Write Length) of one target.

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **target** – **[in]** Pointer to the target device descriptor.
            - **mwl** – **[out]** Pointer to GETMWL payload.

        Returns:

    int i3c\_ccc\_do\_setmrl\_all(const struct [device](../../kernel/drivers/index.md#c.device "device") \*controller, const struct [i3c\_ccc\_mrl](#c.i3c_ccc_mrl) \*mrl, bool has\_ibi\_size)
    :   Broadcast SETMRL to Set Maximum Read Length.

        Helper function to do SETMRL (Set Maximum Read Length) to all connected targets.

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **controller** – **[in]** Pointer to the controller device driver instance.
            - **mrl** – **[in]** Pointer to SETMRL payload.
            - **has\_ibi\_size** – **[in]** True if also sending the optional IBI payload size. False if not sending.

        Returns:

    int i3c\_ccc\_do\_setmrl(const struct [i3c\_device\_desc](#c.i3c_device_desc) \*target, const struct [i3c\_ccc\_mrl](#c.i3c_ccc_mrl) \*mrl)
    :   Single target SETMRL to Set Maximum Read Length.

        Helper function to do SETMRL (Set Maximum Read Length) to one target.

        Note this uses the BCR of the target to determine whether to send the optional IBI payload size.

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **target** – **[in]** Pointer to the target device descriptor.
            - **mrl** – **[in]** Pointer to SETMRL payload.

        Returns:

    int i3c\_ccc\_do\_getmrl(const struct [i3c\_device\_desc](#c.i3c_device_desc) \*target, struct [i3c\_ccc\_mrl](#c.i3c_ccc_mrl) \*mrl)
    :   Single target GETMRL to Get Maximum Read Length.

        Helper function to do GETMRL (Get Maximum Read Length) of one target.

        Note this uses the BCR of the target to determine whether to send the optional IBI payload size.

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **target** – **[in]** Pointer to the target device descriptor.
            - **mrl** – **[out]** Pointer to GETMRL payload.

        Returns:

    int i3c\_ccc\_do\_getstatus(const struct [i3c\_device\_desc](#c.i3c_device_desc) \*target, union [i3c\_ccc\_getstatus](#c.i3c_ccc_getstatus) \*status, enum [i3c\_ccc\_getstatus\_fmt](#c.i3c_ccc_getstatus_fmt) fmt, enum [i3c\_ccc\_getstatus\_defbyte](#c.i3c_ccc_getstatus_defbyte) defbyte)
    :   Single target GETSTATUS to Get Target Status.

        Helper function to do GETSTATUS (Get Target Status) of one target.

        Note this uses the BCR of the target to determine whether to send the optional IBI payload size.

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **target** – **[in]** Pointer to the target device descriptor.
            - **status** – **[out]** Pointer to GETSTATUS payload.
            - **fmt** – **[in]** Which GETSTATUS to use.
            - **defbyte** – **[in]** Defining Byte if using format 2.

        Returns:

    static inline int i3c\_ccc\_do\_getstatus\_fmt1(const struct [i3c\_device\_desc](#c.i3c_device_desc) \*target, union [i3c\_ccc\_getstatus](#c.i3c_ccc_getstatus) \*status)
    :   Single target GETSTATUS to Get Target Status (Format 1).

        Helper function to do GETSTATUS (Get Target Status, format 1) of one target.

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **target** – **[in]** Pointer to the target device descriptor.
            - **status** – **[out]** Pointer to GETSTATUS payload.

        Returns:

    static inline int i3c\_ccc\_do\_getstatus\_fmt2(const struct [i3c\_device\_desc](#c.i3c_device_desc) \*target, union [i3c\_ccc\_getstatus](#c.i3c_ccc_getstatus) \*status, enum [i3c\_ccc\_getstatus\_defbyte](#c.i3c_ccc_getstatus_defbyte) defbyte)
    :   Single target GETSTATUS to Get Target Status (Format 2).

        Helper function to do GETSTATUS (Get Target Status, format 2) of one target.

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **target** – **[in]** Pointer to the target device descriptor.
            - **status** – **[out]** Pointer to GETSTATUS payload.
            - **defbyte** – **[in]** Defining Byte for GETSTATUS format 2.

        Returns:

    int i3c\_ccc\_do\_getcaps(const struct [i3c\_device\_desc](#c.i3c_device_desc) \*target, union [i3c\_ccc\_getcaps](#c.i3c_ccc_getcaps) \*caps, enum [i3c\_ccc\_getcaps\_fmt](#c.i3c_ccc_getcaps_fmt) fmt, enum [i3c\_ccc\_getcaps\_defbyte](#c.i3c_ccc_getcaps_defbyte) defbyte)
    :   Single target GETCAPS to Get Target Status.

        Helper function to do GETCAPS (Get Capabilities) of one target.

        This should only be supported if Advanced Capabilities Bit of the BCR is set

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **target** – **[in]** Pointer to the target device descriptor.
            - **caps** – **[out]** Pointer to GETCAPS payload.
            - **fmt** – **[in]** Which GETCAPS to use.
            - **defbyte** – **[in]** Defining Byte if using format 2.

        Returns:

    static inline int i3c\_ccc\_do\_getcaps\_fmt1(const struct [i3c\_device\_desc](#c.i3c_device_desc) \*target, union [i3c\_ccc\_getcaps](#c.i3c_ccc_getcaps) \*caps)
    :   Single target GETCAPS to Get Capabilities (Format 1).

        Helper function to do GETCAPS (Get Capabilities, format 1) of one target.

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **target** – **[in]** Pointer to the target device descriptor.
            - **caps** – **[out]** Pointer to GETCAPS payload.

        Returns:

    static inline int i3c\_ccc\_do\_getcaps\_fmt2(const struct [i3c\_device\_desc](#c.i3c_device_desc) \*target, union [i3c\_ccc\_getcaps](#c.i3c_ccc_getcaps) \*caps, enum [i3c\_ccc\_getcaps\_defbyte](#c.i3c_ccc_getcaps_defbyte) defbyte)
    :   Single target GETCAPS to Get Capabilities (Format 2).

        Helper function to do GETCAPS (Get Capabilities, format 2) of one target.

        See also

        [i3c\_do\_ccc](#group__i3c__interface_1gaa6d5445489bfc8611c98b93f49305862)

        Parameters:
        :   - **target** – **[in]** Pointer to the target device descriptor.
            - **caps** – **[out]** Pointer to GETCAPS payload.
            - **defbyte** – **[in]** Defining Byte for GETCAPS format 2.

        Returns:

    struct i3c\_ccc\_target\_payload
    :   *#include <ccc.h>*

        Payload structure for Direct CCC to one target.

        Public Members

        uint8\_t addr
        :   Target address.

        uint8\_t rnw
        :   `0` for Write, `1` for Read

        uint8\_t \*data
        :   - For Write CCC, pointer to the byte array of data to be sent, which may contain the Sub-Command Byte and additional data.
            - For Read CCC, pointer to the byte buffer for data to be read into.

        size\_t data\_len
        :   Length in bytes for `data`.

        size\_t num\_xfer
        :   Total number of bytes transferred.

            A Target can issue an EoD or the Controller can abort a transfer before the length of the buffer. It is expected for the driver to write to this after the transfer.

    struct i3c\_ccc\_payload
    :   *#include <ccc.h>*

        Payload structure for one CCC transaction.

        Public Members

        uint8\_t id
        :   The CCC ID (`I3C_CCC_*`).

        uint8\_t \*data
        :   Pointer to byte array of data for this CCC.

            This is the bytes following the CCC command in CCC frame. Set to `NULL` if no associated data.

        size\_t data\_len
        :   Length in bytes for optional data array.

        size\_t num\_xfer
        :   Total number of bytes transferred.

            A Controller can abort a transfer before the length of the buffer. It is expected for the driver to write to this after the transfer.

        struct [i3c\_ccc\_target\_payload](#c.i3c_ccc_target_payload) \*payloads
        :   Array of struct [i3c\_ccc\_target\_payload](#structi3c__ccc__target__payload).

            Each element describes the target and associated payloads for this CCC.

            Use with Direct CCC.

        size\_t num\_targets
        :   Number of targets.

    struct i3c\_ccc\_events
    :   *#include <ccc.h>*

        Payload for ENEC/DISEC CCC (Target Events Command).

        Public Members

        uint8\_t events
        :   Event byte:

            - Bit[0]: ENINT/DISINT:

              - Target Interrupt Requests
            - Bit[1]: ENCR/DISCR:

              - Controller Role Requests
            - Bit[3]: ENHJ/DISHJ:

              - Hot-Join Event

    struct i3c\_ccc\_mwl
    :   *#include <ccc.h>*

        Payload for SETMWL/GETMWL CCC (Set/Get Maximum Write Length).

        Note

        For drivers and help functions, the raw data coming back from target device is in big endian. This needs to be translated back to CPU endianness before passing back to function caller.

        Public Members

        uint16\_t len
        :   Maximum Write Length.

    struct i3c\_ccc\_mrl
    :   *#include <ccc.h>*

        Payload for SETMRL/GETMRL CCC (Set/Get Maximum Read Length).

        Note

        For drivers and help functions, the raw data coming back from target device is in big endian. This needs to be translated back to CPU endianness before passing back to function caller.

        Public Members

        uint16\_t len
        :   Maximum Read Length.

        uint8\_t ibi\_len
        :   Optional IBI Payload Size.

    struct i3c\_ccc\_deftgts\_active\_controller
    :   *#include <ccc.h>*

        The active controller part of payload for DEFTGTS CCC.

        This is used by DEFTGTS (Define List of Targets) CCC to describe the active controller on the I3C bus.

        Public Members

        uint8\_t addr
        :   Dynamic Address of Active Controller.

        uint8\_t dcr
        :   Device Characteristic Register of Active Controller.

        uint8\_t bcr
        :   Bus Characteristic Register of Active Controller.

        uint8\_t static\_addr
        :   Static Address of Active Controller.

    struct i3c\_ccc\_deftgts\_target
    :   *#include <ccc.h>*

        The target device part of payload for DEFTGTS CCC.

        This is used by DEFTGTS (Define List of Targets) CCC to describe the existing target devices on the I3C bus.

        Public Members

        uint8\_t addr
        :   Dynamic Address of a target device, or a group address.

        uint8\_t dcr
        :   Device Characteristic Register of a I3C target device or a group.

        uint8\_t lvr
        :   Legacy Virtual Register for legacy I2C device.

        uint8\_t bcr
        :   Bus Characteristic Register of a target device or a group.

        uint8\_t static\_addr
        :   Static Address of a target device or a group.

    struct i3c\_ccc\_deftgts
    :   *#include <ccc.h>*

        Payload for DEFTGTS CCC (Define List of Targets).

        Note

        `[i3c_ccc_deftgts_target](#structi3c__ccc__deftgts__target)` is an array of targets, where the number of elements is dependent on the number of I3C targets on the bus. Please have enough space for both read and write of this CCC.

        Public Members

        struct [i3c\_ccc\_deftgts\_active\_controller](#c.i3c_ccc_deftgts_active_controller) active\_controller
        :   Data describing the active controller.

        struct [i3c\_ccc\_deftgts\_target](#c.i3c_ccc_deftgts_target) targets[]
        :   Data describing the target(s) on the bus.

    struct i3c\_ccc\_address
    :   *#include <ccc.h>*

        Payload for a single device address.

        This is used for:

        - SETDASA (Set Dynamic Address from Static Address)
        - SETNEWDA (Set New Dynamic Address)
        - SETGRPA (Set Group Address)
        - GETACCCR (Get Accept Controller Role)

        Note that the target address is encoded within struct [i3c\_ccc\_target\_payload](#structi3c__ccc__target__payload) instead of being encoded in this payload.

        Public Members

        uint8\_t addr
        :   - For SETDASA, Static Address to be assigned as Dynamic Address.
            - For SETNEWDA, new Dynamic Address to be assigned.
            - For SETGRPA, new Group Address to be set.
            - For GETACCCR, the correct address of Secondary Controller.

            Note

            For SETDATA, SETNEWDA and SETGRAP, the address is left-shift by 1, and bit[0] is always 0.

            Note

            Fpr SET GETACCCR, the address is left-shift by 1, and bit[0] is the calculated odd parity bit.

    struct i3c\_ccc\_getpid
    :   *#include <ccc.h>*

        Payload for GETPID CCC (Get Provisioned ID).

        Public Members

        uint8\_t pid[6]
        :   48-bit Provisioned ID.

            Note

            Data is big-endian where first byte is MSB.

    struct i3c\_ccc\_getbcr
    :   *#include <ccc.h>*

        Payload for GETBCR CCC (Get Bus Characteristics Register).

        Public Members

        uint8\_t bcr
        :   Bus Characteristics Register.

    struct i3c\_ccc\_getdcr
    :   *#include <ccc.h>*

        Payload for GETDCR CCC (Get Device Characteristics Register).

        Public Members

        uint8\_t dcr
        :   Device Characteristics Register.

    union i3c\_ccc\_getstatus
    :   *#include <ccc.h>*

        Payload for GETSTATUS CCC (Get Device Status).

        Public Members

        uint16\_t status
        :   Device Status.

            - Bit[15:8]: Reserved.
            - Bit[7:6]: Activity Mode.
            - Bit[5]: Protocol Error.
            - Bit[4]: Reserved.
            - Bit[3:0]: Number of Pending Interrupts.

            Note

            For drivers and help functions, the raw data coming back from target device is in big endian. This needs to be translated back to CPU endianness before passing back to function caller.

        struct [i3c\_ccc\_getstatus](#c.i3c_ccc_getstatus).[anonymous] fmt1

        uint16\_t tgtstat
        :   Defining Byte 0x00: TGTSTAT.

            See also

            i3c\_ccc\_getstatus::fmt1::status

        uint16\_t precr
        :   Defining Byte 0x91: PRECR.

            - Bit[15:8]: Vendor Reserved
            - Bit[7:2]: Reserved
            - Bit[1]: Handoff Delay NACK
            - Bit[0]: Deep Sleep Detected

            Note

            For drivers and help functions, the raw data coming back from target device is in big endian. This needs to be translated back to CPU endianness before passing back to function caller.

        uint16\_t raw\_u16

        union [i3c\_ccc\_getstatus](#c.i3c_ccc_getstatus).[anonymous] fmt2

    struct i3c\_ccc\_setbrgtgt\_tgt
    :   *#include <ccc.h>*

        One Bridged Target for SETBRGTGT payload.

        Public Members

        uint8\_t addr
        :   Dynamic address of the bridged target.

            Note

            The address is left-shift by 1, and bit[0] is always 0.

        uint16\_t id
        :   16-bit ID for the bridged target.

            Note

            For drivers and help functions, the raw data coming back from target device is in big endian. This needs to be translated back to CPU endianness before passing back to function caller.

    struct i3c\_ccc\_setbrgtgt
    :   *#include <ccc.h>*

        Payload for SETBRGTGT CCC (Set Bridge Targets).

        Note that the bridge target address is encoded within struct [i3c\_ccc\_target\_payload](#structi3c__ccc__target__payload) instead of being encoded in this payload.

        Public Members

        uint8\_t count
        :   Number of bridged targets.

        struct [i3c\_ccc\_setbrgtgt\_tgt](#c.i3c_ccc_setbrgtgt_tgt) targets[]
        :   Array of bridged targets.

    union i3c\_ccc\_getmxds
    :   *#include <ccc.h>*

        Payload for GETMXDS CCC (Get Max Data Speed).

        Note

        This is only for GETMXDS Format 1 and Format 2.

        Public Members

        uint8\_t maxwr
        :   maxWr

        uint8\_t maxrd
        :   maxRd

        struct [i3c\_ccc\_getmxds](#c.i3c_ccc_getmxds).[anonymous] fmt1

        uint8\_t maxrdturn[3]
        :   Maximum Read Turnaround Time in microsecond.

            This is in little-endian where first byte is LSB.

        struct [i3c\_ccc\_getmxds](#c.i3c_ccc_getmxds).[anonymous] fmt2

        uint8\_t wrrdturn
        :   Defining Byte 0x00: WRRDTURN.

            See also

            [i3c\_ccc\_getmxds::fmt2](#unioni3c__ccc__getmxds_1adfb70b06d5e769fccc7630a356067fcd)

        uint8\_t crhdly1
        :   Defining Byte 0x91: CRHDLY.

            - Bit[2]: Set Bus Activity State
            - Bit[1:0]: Controller Handoff Activity State

        struct [i3c\_ccc\_getmxds](#c.i3c_ccc_getmxds).[anonymous] fmt3

    union i3c\_ccc\_getcaps
    :   *#include <ccc.h>*

        Payload for GETCAPS CCC (Get Optional Feature Capabilities).

        Note

        Only supports GETCAPS Format 1 and Format 2. In I3C v1.0 this was GETHDRCAP which only returned a single byte which is the same as the GETCAPS1 byte.

        Public Members

        uint8\_t gethdrcap
        :   I3C v1.0 HDR Capabilities.

            - Bit[0]: HDR-DDR
            - Bit[1]: HDR-TSP
            - Bit[2]: HDR-TSL
            - Bit[7:3]: Reserved

        uint8\_t getcaps[4]
        :   I3C v1.1+ Device Capabilities Byte 1 GETCAPS1.

            - Bit[0]: HDR-DDR
            - Bit[1]: HDR-TSP
            - Bit[2]: HDR-TSL
            - Bit[3]: HDR-BT
            - Bit[7:4]: Reserved Byte 2 GETCAPS2
            - Bit[3:0]: I3C 1.x Specification Version
            - Bit[5:4]: Group Address Capabilities
            - Bit[6]: HDR-DDR Write Abort
            - Bit[7]: HDR-DDR Abort CRC Byte 3 GETCAPS3
            - Bit[0]: Multi-Lane (ML) Data Transfer Support
            - Bit[1]: Device to Device Transfer (D2DXFER) Support
            - Bit[2]: Device to Device Transfer (D2DXFER) IBI Capable
            - Bit[3]: Defining Byte Support in GETCAPS
            - Bit[4]: Defining Byte Support in GETSTATUS
            - Bit[5]: HDR-BT CRC-32 Support
            - Bit[6]: IBI MDB Support for Pending Read Notification
            - Bit[7]: Reserved Byte 4 GETCAPS4
            - Bit[7:0]: Reserved

        union [i3c\_ccc\_getcaps](#c.i3c_ccc_getcaps).[anonymous] fmt1

        uint8\_t tgtcaps[4]
        :   Defining Byte 0x00: TGTCAPS.

            See also

            i3c\_ccc\_getcaps::fmt1::getcaps

        uint32\_t testpat
        :   Defining Byte 0x5A: TESTPAT.

            Note

            should always be 0xA55AA55A in big endian

        uint8\_t crcaps[2]
        :   Defining Byte 0x91: CRCAPS Byte 1 CRCAPS1.

            - Bit[0]: Hot-Join Support
            - Bit[1]: Group Management Support
            - Bit[2]: Multi-Lane Support Byte 2 CRCAPS2
            - Bit[0]: In-Band Interrupt Support
            - Bit[1]: Controller Pass-Back
            - Bit[2]: Deep Sleep Capable
            - Bit[3]: Delayed Controller Handoff

        uint8\_t vtcaps[2]
        :   Defining Byte 0x93: VTCAPS Byte 1 VTCAPS1.

            - Bit[2:0]: Virtual Target Type
            - Bit[4]: Side Effects
            - Bit[5]: Shared Peripheral Detect Byte 2 VTCAPS2
            - Bit[1:0]: Interrupt Requests
            - Bit[2]: Address Remapping
            - Bit[4:3]: Bus Context and Conditions

        union [i3c\_ccc\_getcaps](#c.i3c_ccc_getcaps).[anonymous] fmt2

*group* I3C Address-related Helper Code
:   I3C Address-related Helper Code.

    Defines

    I3C\_BROADCAST\_ADDR
    :   Broadcast Address on I3C bus.

    I3C\_MAX\_ADDR
    :   Maximum value of device addresses.

    Enums

    enum i3c\_addr\_slot\_status
    :   Enum to indicate whether an address is reserved, has I2C/I3C device attached, or no device attached.

        *Values:*

        enumerator I3C\_ADDR\_SLOT\_STATUS\_FREE = 0U
        :   Address has not device attached.

        enumerator I3C\_ADDR\_SLOT\_STATUS\_RSVD
        :   Address is reserved.

        enumerator I3C\_ADDR\_SLOT\_STATUS\_I3C\_DEV
        :   Address is associated with an I3C device.

        enumerator I3C\_ADDR\_SLOT\_STATUS\_I2C\_DEV
        :   Address is associated with an I2C device.

        enumerator I3C\_ADDR\_SLOT\_STATUS\_MASK = 0x03U
        :   Bit masks used to filter status bits.

    Functions

    int i3c\_addr\_slots\_init(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Initialize the I3C address slots struct.

        This clears out the assigned address bits, and set the reserved address bits according to the I3C specification.

        Parameters:
        :   - **dev** – Pointer to controller device driver instance.

        Return values:
        :   - **0** – if successful.
            - **-EINVAL** – if duplicate addresses.

    void i3c\_addr\_slots\_set(struct [i3c\_addr\_slots](#c.i3c_addr_slots) \*slots, uint8\_t dev\_addr, enum [i3c\_addr\_slot\_status](#c.i3c_addr_slot_status) status)
    :   Set the address status of a device.

        Parameters:
        :   - **slots** – Pointer to the address slots structure.
            - **dev\_addr** – Device address.
            - **status** – New status for the address `dev_addr`.

    enum [i3c\_addr\_slot\_status](#c.i3c_addr_slot_status) i3c\_addr\_slots\_status(struct [i3c\_addr\_slots](#c.i3c_addr_slots) \*slots, uint8\_t dev\_addr)
    :   Get the address status of a device.

        Parameters:
        :   - **slots** – Pointer to the address slots structure.
            - **dev\_addr** – Device address.

        Returns:
        :   Address status for the address `dev_addr`.

    bool i3c\_addr\_slots\_is\_free(struct [i3c\_addr\_slots](#c.i3c_addr_slots) \*slots, uint8\_t dev\_addr)
    :   Check if the address is free.

        Parameters:
        :   - **slots** – Pointer to the address slots structure.
            - **dev\_addr** – Device address.

        Return values:
        :   - **true** – if address is free.
            - **false** – if address is not free.

    uint8\_t i3c\_addr\_slots\_next\_free\_find(struct [i3c\_addr\_slots](#c.i3c_addr_slots) \*slots, uint8\_t start\_addr)
    :   Find the next free address.

        This can be used to find the next free address that can be assigned to a new device.

        Parameters:
        :   - **slots** – Pointer to the address slots structure.
            - **start\_addr** – Where to start searching

        Returns:
        :   The next free address, or 0 if none found.

    static inline void i3c\_addr\_slots\_mark\_free(struct [i3c\_addr\_slots](#c.i3c_addr_slots) \*addr\_slots, uint8\_t addr)
    :   Mark the address as free (not used) in device list.

        Parameters:
        :   - **addr\_slots** – Pointer to the address slots struct.
            - **addr** – Device address.

    static inline void i3c\_addr\_slots\_mark\_rsvd(struct [i3c\_addr\_slots](#c.i3c_addr_slots) \*addr\_slots, uint8\_t addr)
    :   Mark the address as reserved in device list.

        Parameters:
        :   - **addr\_slots** – Pointer to the address slots struct.
            - **addr** – Device address.

    static inline void i3c\_addr\_slots\_mark\_i3c(struct [i3c\_addr\_slots](#c.i3c_addr_slots) \*addr\_slots, uint8\_t addr)
    :   Mark the address as I3C device in device list.

        Parameters:
        :   - **addr\_slots** – Pointer to the address slots struct.
            - **addr** – Device address.

    static inline void i3c\_addr\_slots\_mark\_i2c(struct [i3c\_addr\_slots](#c.i3c_addr_slots) \*addr\_slots, uint8\_t addr)
    :   Mark the address as I2C device in device list.

        Parameters:
        :   - **addr\_slots** – Pointer to the address slots struct.
            - **addr** – Device address.

    struct i3c\_addr\_slots
    :   *#include <addresses.h>*

        Structure to keep track of addresses on I3C bus.

*group* I3C Target Device API
:   I3C Target Device API.

    Functions

    static inline int i3c\_target\_tx\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*buf, uint16\_t len)
    :   Writes to the target’s TX FIFO.

        Write to the TX FIFO `dev` I3C bus driver using the provided buffer and length. Some I3C targets will NACK read requests until data is written to the TX FIFO. This function will write as much as it can to the FIFO return the total number of bytes written. It is then up to the application to utalize the target callbacks to write the remaining data. Negative returns indicate error.

        Most of the existing hardware allows simultaneous support for master and target mode. This is however not guaranteed.

        Parameters:
        :   - **dev** – Pointer to the device structure for an I3C controller driver configured in target mode.
            - **buf** – Pointer to the buffer
            - **len** – Length of the buffer

        Return values:
        :   - **Total** – number of bytes written
            - **-ENOTSUP** – Not in Target Mode
            - **-ENOSPC** – No space in Tx FIFO
            - **-ENOSYS** – If target mode is not implemented

    static inline int i3c\_target\_register(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [i3c\_target\_config](#c.i3c_target_config) \*cfg)
    :   Registers the provided config as target device of a controller.

        Enable I3C target mode for the `dev` I3C bus driver using the provided config struct (`cfg`) containing the functions and parameters to send bus events. The I3C target will be registered at the address provided as [i3c\_target\_config::address](#structi3c__target__config_1a89b7f8bd52beec7dd733ab6dd1111758) struct member. Any I3C bus events related to the target mode will be passed onto I3C target device driver via a set of callback functions provided in the ‘callbacks’ struct member.

        Most of the existing hardware allows simultaneous support for master and target mode. This is however not guaranteed.

        Parameters:
        :   - **dev** – Pointer to the device structure for an I3C controller driver configured in target mode.
            - **cfg** – Config struct with functions and parameters used by the I3C target driver to send bus events

        Return values:
        :   - **0** – Is successful
            - **-EINVAL** – If parameters are invalid
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If target mode is not implemented

    static inline int i3c\_target\_unregister(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [i3c\_target\_config](#c.i3c_target_config) \*cfg)
    :   Unregisters the provided config as target device.

        This routine disables I3C target mode for the `dev` I3C bus driver using the provided config struct (`cfg`) containing the functions and parameters to send bus events.

        Parameters:
        :   - **dev** – Pointer to the device structure for an I3C controller driver configured in target mode.
            - **cfg** – Config struct with functions and parameters used by the I3C target driver to send bus events

        Return values:
        :   - **0** – Is successful
            - **-EINVAL** – If parameters are invalid
            - **-ENOSYS** – If target mode is not implemented

    struct i3c\_config\_target
    :   *#include <target\_device.h>*

        Configuration parameters for I3C hardware to act as target device.

        This can also be used to configure the controller if it is to act as a secondary controller on the bus.

        Public Members

        bool enable
        :   If the hardware is to act as a target device on the bus.

        uint8\_t static\_addr
        :   I3C target address.

            Used used when operates as secondary controller or as a target device.

        uint64\_t pid
        :   Provisioned ID.

        bool pid\_random
        :   True if lower 32-bit of Provisioned ID is random.

            This sets the bit 32 of Provisioned ID which means the lower 32-bit is random value.

        uint8\_t bcr
        :   Bus Characteristics Register (BCR).

        uint8\_t dcr
        :   Device Characteristics Register (DCR).

        uint16\_t max\_read\_len
        :   Maximum Read Length (MRL).

        uint16\_t max\_write\_len
        :   Maximum Write Length (MWL).

        uint8\_t supported\_hdr
        :   Bit mask of supported HDR modes (0 - 7).

            This can be used to enable or disable HDR mode supported by the hardware at runtime.

    struct i3c\_target\_config
    :   *#include <target\_device.h>*

        Structure describing a device that supports the I3C target API.

        Instances of this are passed to the [i3c\_target\_register()](#group__i3c__target__device_1gaf13d2b84a91e17d5ec49a41e9c553d42) and [i3c\_target\_unregister()](#group__i3c__target__device_1ga3dc0e6451fb13fa063c5ec3e18fe22e4) functions to indicate addition and removal of a target device, respective.

        Fields other than `node` must be initialized by the module that implements the device behavior prior to passing the object reference to [i3c\_target\_register()](#group__i3c__target__device_1gaf13d2b84a91e17d5ec49a41e9c553d42).

        Public Members

        [sys\_snode\_t](../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Private, do not modify.

        uint8\_t flags
        :   Flags for the target device defined by I3C\_TARGET\_FLAGS\_\* constants.

        uint8\_t address
        :   Address for this target device.

        const struct [i3c\_target\_callbacks](#c.i3c_target_callbacks) \*callbacks
        :   Callback functions.

    struct i3c\_target\_callbacks
    :   *#include <target\_device.h>*

        Public Members

        int (\*write\_requested\_cb)(struct [i3c\_target\_config](#c.i3c_target_config) \*config)
        :   Function called when a write to the device is initiated.

            This function is invoked by the controller when the bus completes a start condition for a write operation to the address associated with a particular device.

            A success return shall cause the controller to ACK the next byte received. An error return shall cause the controller to NACK the next byte received.

            Param config:
            :   Configuration structure associated with the device to which the operation is addressed.

            Return:
            :   0 if the write is accepted, or a negative error code.

        int (\*write\_received\_cb)(struct [i3c\_target\_config](#c.i3c_target_config) \*config, uint8\_t val)
        :   Function called when a write to the device is continued.

            This function is invoked by the controller when it completes reception of a byte of data in an ongoing write operation to the device.

            A success return shall cause the controller to ACK the next byte received. An error return shall cause the controller to NACK the next byte received.

            Param config:
            :   Configuration structure associated with the device to which the operation is addressed.

            Param val:
            :   the byte received by the controller.

            Return:
            :   0 if more data can be accepted, or a negative error code.

        int (\*read\_requested\_cb)(struct [i3c\_target\_config](#c.i3c_target_config) \*config, uint8\_t \*val)
        :   Function called when a read from the device is initiated.

            This function is invoked by the controller when the bus completes a start condition for a read operation from the address associated with a particular device.

            The value returned in `val` will be transmitted. A success return shall cause the controller to react to additional read operations. An error return shall cause the controller to ignore bus operations until a new start condition is received.

            Param config:
            :   Configuration structure associated with the device to which the operation is addressed.

            Param val:
            :   Pointer to storage for the first byte of data to return for the read request.

            Return:
            :   0 if more data can be requested, or a negative error code.

        int (\*read\_processed\_cb)(struct [i3c\_target\_config](#c.i3c_target_config) \*config, uint8\_t \*val)
        :   Function called when a read from the device is continued.

            This function is invoked by the controller when the bus is ready to provide additional data for a read operation from the address associated with the device device.

            The value returned in `val` will be transmitted. A success return shall cause the controller to react to additional read operations. An error return shall cause the controller to ignore bus operations until a new start condition is received.

            Param config:
            :   Configuration structure associated with the device to which the operation is addressed.

            Param val:
            :   Pointer to storage for the next byte of data to return for the read request.

            Return:
            :   0 if data has been provided, or a negative error code.

        int (\*stop\_cb)(struct [i3c\_target\_config](#c.i3c_target_config) \*config)
        :   Function called when a stop condition is observed after a start condition addressed to a particular device.

            This function is invoked by the controller when the bus is ready to provide additional data for a read operation from the address associated with the device device. After the function returns the controller shall enter a state where it is ready to react to new start conditions.

            Param config:
            :   Configuration structure associated with the device to which the operation is addressed.

            Return:
            :   Ignored.

    struct i3c\_target\_driver\_api
    :   *#include <target\_device.h>*
