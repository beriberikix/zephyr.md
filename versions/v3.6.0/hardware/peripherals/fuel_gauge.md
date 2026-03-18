---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/fuel_gauge.html
original_path: hardware/peripherals/fuel_gauge.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Fuel Gauge

The fuel gauge subsystem exposes an API to uniformly access battery fuel gauge devices. Currently,
only reading data is supported.

Note: This API is currently experimental and this doc will be significantly changed as new features
are added to the API.

## Basic Operation

### Properties

Fundamentally, a property is a quantity that a fuel gauge device can measure.

Fuel gauges typically support multiple properties, such as temperature readings of the battery-pack
or present-time current/voltage.

Properties are fetched by the client one at a time using [`fuel_gauge_get_prop()`](#c.fuel_gauge_get_prop), or fetched
in a batch using [`fuel_gauge_get_props()`](#c.fuel_gauge_get_props).

Properties are set by the client one at a time using [`fuel_gauge_set_prop()`](#c.fuel_gauge_set_prop), or set in a
batch using [`fuel_gauge_set_props()`](#c.fuel_gauge_set_props).

### Battery Cutoff

Many fuel gauges embedded within battery packs expose a register address that when written to with a
specific payload will do a battery cutoff. This battery cutoff is often referred to as ship, shelf,
or sleep mode due to its utility in reducing battery drain while devices are stored or shipped.

The fuel gauge API exposes battery cutoff with the [`fuel_gauge_battery_cutoff()`](#c.fuel_gauge_battery_cutoff) function.

### Caching

The Fuel Gauge API explicitly provides no caching for its clients.

## API Reference

*group* fuel\_gauge\_interface
:   Fuel Gauge Interface.

    Defines

    SBS\_GAUGE\_MANUFACTURER\_NAME\_MAX\_SIZE
    :   Data structures for reading SBS buffer properties.

    SBS\_GAUGE\_DEVICE\_NAME\_MAX\_SIZE

    SBS\_GAUGE\_DEVICE\_CHEMISTRY\_MAX\_SIZE

    Typedefs

    typedef uint16\_t fuel\_gauge\_prop\_t

    typedef int (\*fuel\_gauge\_get\_property\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [fuel\_gauge\_prop\_t](#c.fuel_gauge_prop_t) prop, union [fuel\_gauge\_prop\_val](#c.fuel_gauge_prop_val) \*val)
    :   Callback API for getting a fuel\_gauge property.

        See fuel\_gauge\_get\_property() for argument description

    typedef int (\*fuel\_gauge\_set\_property\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [fuel\_gauge\_prop\_t](#c.fuel_gauge_prop_t) prop, union [fuel\_gauge\_prop\_val](#c.fuel_gauge_prop_val) val)
    :   Callback API for setting a fuel\_gauge property.

        See fuel\_gauge\_set\_property() for argument description

    typedef int (\*fuel\_gauge\_get\_buffer\_property\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [fuel\_gauge\_prop\_t](#c.fuel_gauge_prop_t) prop\_type, void \*dst, size\_t dst\_len)
    :   Callback API for getting a fuel\_gauge buffer property.

        See fuel\_gauge\_get\_buffer\_property() for argument description

    typedef int (\*fuel\_gauge\_battery\_cutoff\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Callback API for doing a battery cutoff.

        See [fuel\_gauge\_battery\_cutoff()](#group__fuel__gauge__interface_1ga763a40688dc8fc6a0ba85fdc79178ebc) for argument description

    Enums

    enum fuel\_gauge\_prop\_type
    :   *Values:*

        enumerator FUEL\_GAUGE\_AVG\_CURRENT = 0
        :   Runtime Dynamic Battery Parameters.

            Provide a 1 minute average of the current on the battery. Does not check for flags or whether those values are bad readings. See driver instance header for details on implementation and how the average is calculated. Units in uA negative=discharging

        enumerator FUEL\_GAUGE\_BATTERY\_CUTOFF
        :   Used to cutoff the battery from the system - useful for storage/shipping of devices.

        enumerator FUEL\_GAUGE\_CURRENT
        :   Battery current (uA); negative=discharging.

        enumerator FUEL\_GAUGE\_CHARGE\_CUTOFF
        :   Whether the battery underlying the fuel-gauge is cut off from charge.

        enumerator FUEL\_GAUGE\_CYCLE\_COUNT
        :   Cycle count in 1/100ths (number of charge/discharge cycles).

        enumerator FUEL\_GAUGE\_CONNECT\_STATE
        :   Connect state of battery.

        enumerator FUEL\_GAUGE\_FLAGS
        :   General Error/Runtime Flags.

        enumerator FUEL\_GAUGE\_FULL\_CHARGE\_CAPACITY
        :   Full Charge Capacity in uAh (might change in some implementations to determine wear).

        enumerator FUEL\_GAUGE\_PRESENT\_STATE
        :   Is the battery physically present.

        enumerator FUEL\_GAUGE\_REMAINING\_CAPACITY
        :   Remaining capacity in uAh.

        enumerator FUEL\_GAUGE\_RUNTIME\_TO\_EMPTY
        :   Remaining battery life time in minutes.

        enumerator FUEL\_GAUGE\_RUNTIME\_TO\_FULL
        :   Remaining time in minutes until battery reaches full charge.

        enumerator FUEL\_GAUGE\_SBS\_MFR\_ACCESS
        :   Retrieve word from SBS1.1 ManufactuerAccess.

        enumerator FUEL\_GAUGE\_ABSOLUTE\_STATE\_OF\_CHARGE
        :   Absolute state of charge (percent, 0-100) - expressed as % of design capacity.

        enumerator FUEL\_GAUGE\_RELATIVE\_STATE\_OF\_CHARGE
        :   Relative state of charge (percent, 0-100) - expressed as % of full charge capacity.

        enumerator FUEL\_GAUGE\_TEMPERATURE
        :   Temperature in 0.1 K.

        enumerator FUEL\_GAUGE\_VOLTAGE
        :   Battery voltage (uV).

        enumerator FUEL\_GAUGE\_SBS\_MODE
        :   Battery Mode (flags).

        enumerator FUEL\_GAUGE\_CHARGE\_CURRENT
        :   Battery desired Max Charging Current (uA).

        enumerator FUEL\_GAUGE\_CHARGE\_VOLTAGE
        :   Battery desired Max Charging Voltage (uV).

        enumerator FUEL\_GAUGE\_STATUS
        :   Alarm, Status and Error codes (flags).

        enumerator FUEL\_GAUGE\_DESIGN\_CAPACITY
        :   Design Capacity (mAh or 10mWh).

        enumerator FUEL\_GAUGE\_DESIGN\_VOLTAGE
        :   Design Voltage (mV).

        enumerator FUEL\_GAUGE\_SBS\_ATRATE
        :   AtRate (mA or 10 mW).

        enumerator FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_FULL
        :   AtRateTimeToFull (minutes).

        enumerator FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_EMPTY
        :   AtRateTimeToEmpty (minutes).

        enumerator FUEL\_GAUGE\_SBS\_ATRATE\_OK
        :   AtRateOK (boolean).

        enumerator FUEL\_GAUGE\_SBS\_REMAINING\_CAPACITY\_ALARM
        :   Remaining Capacity Alarm (mAh or 10mWh).

        enumerator FUEL\_GAUGE\_SBS\_REMAINING\_TIME\_ALARM
        :   Remaining Time Alarm (minutes).

        enumerator FUEL\_GAUGE\_MANUFACTURER\_NAME
        :   Manufacturer of pack (1 byte length + 20 bytes data).

        enumerator FUEL\_GAUGE\_DEVICE\_NAME
        :   Name of pack (1 byte length + 20 bytes data).

        enumerator FUEL\_GAUGE\_DEVICE\_CHEMISTRY
        :   Chemistry (1 byte length + 4 bytes data).

        enumerator FUEL\_GAUGE\_COMMON\_COUNT
        :   Reserved to demark end of common fuel gauge properties.

        enumerator FUEL\_GAUGE\_CUSTOM\_BEGIN
        :   Reserved to demark downstream custom properties - use this value as the actual value may change over future versions of this API.

        enumerator FUEL\_GAUGE\_PROP\_MAX = UINT16\_MAX
        :   Reserved to demark end of valid enum properties.

    Functions

    int fuel\_gauge\_get\_prop(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [fuel\_gauge\_prop\_t](#c.fuel_gauge_prop_t) prop, union [fuel\_gauge\_prop\_val](#c.fuel_gauge_prop_val) \*val)
    :   Fetch a battery fuel-gauge property.

        Parameters:
        :   - **dev** – Pointer to the battery fuel-gauge device
            - **prop** – Type of property to be fetched from device
            - **val** – pointer to a union [fuel\_gauge\_prop\_val](#unionfuel__gauge__prop__val) where the property is read into from the fuel gauge device.

        Returns:
        :   0 if successful, negative errno code if failure.

    int fuel\_gauge\_get\_props(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [fuel\_gauge\_prop\_t](#c.fuel_gauge_prop_t) \*props, union [fuel\_gauge\_prop\_val](#c.fuel_gauge_prop_val) \*vals, size\_t len)
    :   Fetch multiple battery fuel-gauge properies.

        The default implementation is the same as calling [fuel\_gauge\_get\_prop()](#group__fuel__gauge__interface_1gab84999beab9a43241992945a3b2d37e1) multiple times. A driver may implement the `get_properties` field of the fuel gauge driver APIs struct to override this implementation.

        Parameters:
        :   - **dev** – Pointer to the battery fuel-gauge device
            - **props** – Array of the type of property to be fetched from device, each index corresponds to the same index of the vals input array.
            - **vals** – Pointer to array of union [fuel\_gauge\_prop\_val](#unionfuel__gauge__prop__val) where the property is read into from the fuel gauge device. The vals array is not permuted.
            - **len** – number of properties in props & vals array

        Returns:
        :   0 if successful, negative errno code of first failing property

    int fuel\_gauge\_set\_prop(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [fuel\_gauge\_prop\_t](#c.fuel_gauge_prop_t) prop, union [fuel\_gauge\_prop\_val](#c.fuel_gauge_prop_val) val)
    :   Set a battery fuel-gauge property.

        Parameters:
        :   - **dev** – Pointer to the battery fuel-gauge device
            - **prop** – Type of property that’s being set
            - **val** – Value to set associated prop property.

        Returns:
        :   0 if successful, negative errno code of first failing property

    int fuel\_gauge\_set\_props(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [fuel\_gauge\_prop\_t](#c.fuel_gauge_prop_t) \*props, union [fuel\_gauge\_prop\_val](#c.fuel_gauge_prop_val) \*vals, size\_t len)
    :   Set a battery fuel-gauge property.

        Parameters:
        :   - **dev** – Pointer to the battery fuel-gauge device
            - **props** – Array of the type of property to be set, each index corresponds to the same index of the vals input array.
            - **vals** – Pointer to array of union [fuel\_gauge\_prop\_val](#unionfuel__gauge__prop__val) where the property is written the fuel gauge device. The vals array is not permuted.
            - **len** – number of properties in props array

        Returns:
        :   return=0 if successful. Otherwise, return array index of failing property.

    int fuel\_gauge\_get\_buffer\_prop(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [fuel\_gauge\_prop\_t](#c.fuel_gauge_prop_t) prop\_type, void \*dst, size\_t dst\_len)
    :   Fetch a battery fuel-gauge buffer property.

        Parameters:
        :   - **dev** – Pointer to the battery fuel-gauge device
            - **prop\_type** – Type of property to be fetched from device
            - **dst** – byte array or struct that will hold the buffer data that is read from the fuel gauge
            - **dst\_len** – the length of the destination array in bytes

        Returns:
        :   return=0 if successful, return < 0 if getting property failed, return 0 on success

    int fuel\_gauge\_battery\_cutoff(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Have fuel gauge cutoff its associated battery.

        Parameters:
        :   - **dev** – Pointer to the battery fuel-gauge device

        Returns:
        :   return=0 if successful and battery cutoff is now in process, return < 0 if failed to do battery cutoff.

    union fuel\_gauge\_prop\_val
    :   *#include <fuel\_gauge.h>*

        Property field to value/type union.

        Public Members

        int avg\_current
        :   FUEL\_GAUGE\_AVG\_CURRENT.

        bool cutoff
        :   FUEL\_GAUGE\_CHARGE\_CUTOFF.

        int current
        :   FUEL\_GAUGE\_CURRENT.

        uint32\_t cycle\_count
        :   FUEL\_GAUGE\_CYCLE\_COUNT.

        uint32\_t flags
        :   FUEL\_GAUGE\_FLAGS.

        uint32\_t full\_charge\_capacity
        :   FUEL\_GAUGE\_FULL\_CHARGE\_CAPACITY.

        uint32\_t remaining\_capacity
        :   FUEL\_GAUGE\_REMAINING\_CAPACITY.

        uint32\_t runtime\_to\_empty
        :   FUEL\_GAUGE\_RUNTIME\_TO\_EMPTY.

        uint32\_t runtime\_to\_full
        :   FUEL\_GAUGE\_RUNTIME\_TO\_FULL.

        uint16\_t sbs\_mfr\_access\_word
        :   FUEL\_GAUGE\_SBS\_MFR\_ACCESS.

        uint8\_t absolute\_state\_of\_charge
        :   FUEL\_GAUGE\_ABSOLUTE\_STATE\_OF\_CHARGE.

        uint8\_t relative\_state\_of\_charge
        :   FUEL\_GAUGE\_RELATIVE\_STATE\_OF\_CHARGE.

        uint16\_t temperature
        :   FUEL\_GAUGE\_TEMPERATURE.

        int voltage
        :   FUEL\_GAUGE\_VOLTAGE.

        uint16\_t sbs\_mode
        :   FUEL\_GAUGE\_SBS\_MODE.

        uint32\_t chg\_current
        :   FUEL\_GAUGE\_CHARGE\_CURRENT.

        uint32\_t chg\_voltage
        :   FUEL\_GAUGE\_CHARGE\_VOLTAGE.

        uint16\_t fg\_status
        :   FUEL\_GAUGE\_STATUS.

        uint16\_t design\_cap
        :   FUEL\_GAUGE\_DESIGN\_CAPACITY.

        uint16\_t design\_volt
        :   FUEL\_GAUGE\_DESIGN\_VOLTAGE.

        int16\_t sbs\_at\_rate
        :   FUEL\_GAUGE\_SBS\_ATRATE.

        uint16\_t sbs\_at\_rate\_time\_to\_full
        :   FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_FULL.

        uint16\_t sbs\_at\_rate\_time\_to\_empty
        :   FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_EMPTY.

        bool sbs\_at\_rate\_ok
        :   FUEL\_GAUGE\_SBS\_ATRATE\_OK.

        uint16\_t sbs\_remaining\_capacity\_alarm
        :   FUEL\_GAUGE\_SBS\_REMAINING\_CAPACITY\_ALARM.

        uint16\_t sbs\_remaining\_time\_alarm
        :   FUEL\_GAUGE\_SBS\_REMAINING\_TIME\_ALARM.

    struct sbs\_gauge\_manufacturer\_name
    :   *#include <fuel\_gauge.h>*

    struct sbs\_gauge\_device\_name
    :   *#include <fuel\_gauge.h>*

    struct sbs\_gauge\_device\_chemistry
    :   *#include <fuel\_gauge.h>*

    struct fuel\_gauge\_driver\_api
    :   *#include <fuel\_gauge.h>*

        Public Members

        [fuel\_gauge\_get\_property\_t](#c.fuel_gauge_get_property_t) get\_property
        :   Note: Historically this API allowed drivers to implement a custom multi-get/set property function, this was added so drivers could potentially optimize batch read with their specific chip.

            However, it was removed because of no existing concrete case upstream. If this need is demonstrated, we can add this back in as an API field.

*group* fuel\_gauge\_emulator\_backend
:   Fuel gauge backend emulator APIs.

    Functions

    int emul\_fuel\_gauge\_set\_battery\_charging(const struct [emul](../emulator/bus_emulators.md#c.emul "emul") \*target, uint32\_t uV, int uA)
    :   Set charging for fuel gauge associated battery.

        Set how much the battery associated with a fuel gauge IC is charging or discharging. Where voltage is always positive and a positive or negative current denotes charging or discharging, respectively.

        Parameters:
        :   - **target** – Pointer to the emulator structure for the fuel gauge emulator instance.
            - **uV** – Microvolts describing the battery voltage.
            - **uA** – Microamps describing the battery current where negative is discharging.

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – if mV or mA are 0.

    int emul\_fuel\_gauge\_is\_battery\_cutoff(const struct [emul](../emulator/bus_emulators.md#c.emul "emul") \*target, bool \*cutoff)
    :   Check if the battery has been cut off.

        Parameters:
        :   - **target** – Pointer to the emulator structure for the fuel gauge emulator instance.
            - **cutoff** – Pointer to bool storing variable.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – if not supported by emulator.
