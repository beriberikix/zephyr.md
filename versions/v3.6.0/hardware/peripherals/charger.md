---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/charger.html
original_path: hardware/peripherals/charger.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Chargers

The charger subsystem exposes an API to uniformly access battery charger devices.

## Basic Operation

### Initiating a Charge Cycle

A charge cycle is initiated or terminated using [`charger_charge_enable()`](#c.charger_charge_enable).

### Properties

Fundamentally, a property is a configurable setting, state, or quantity that a charger device can
measure.

Chargers typically support multiple properties, such as temperature readings of the battery-pack
or present-time current/voltage.

Properties are fetched by the client one at a time using [`charger_get_prop()`](#c.charger_get_prop).
Properties are set by the client one at a time using [`charger_set_prop()`](#c.charger_set_prop).

## API Reference

*group* charger\_interface
:   Charger Interface.

    Typedefs

    typedef uint16\_t charger\_prop\_t
    :   A charger property’s identifier.

        See [charger\_property](#group__charger__interface_1ga6eb3b4cc76e4f1e34732b7853eb860b7) for a list of identifiers

    typedef int (\*charger\_get\_property\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const [charger\_prop\_t](#c.charger_prop_t) prop, union [charger\_propval](#c.charger_propval) \*val)
    :   Callback API for getting a charger property.

        See charger\_get\_property() for argument description

    typedef int (\*charger\_set\_property\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const [charger\_prop\_t](#c.charger_prop_t) prop, const union [charger\_propval](#c.charger_propval) \*val)
    :   Callback API for setting a charger property.

        See charger\_set\_property() for argument description

    typedef int (\*charger\_charge\_enable\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const bool enable)
    :   Callback API enabling or disabling a charge cycle.

        See [charger\_charge\_enable()](#group__charger__interface_1gace1ea9841574d75d314db078df5a0b3a) for argument description

    Enums

    enum charger\_property
    :   Runtime Dynamic Battery Parameters.

        *Values:*

        enumerator CHARGER\_PROP\_ONLINE = 0
        :   Indicates if external supply is present for the charger.

            Value should be of type enum [charger\_online](#group__charger__interface_1gad95d2b1aaf18ac3a1c536f2d40317c19)

        enumerator CHARGER\_PROP\_PRESENT
        :   Reports whether or not a battery is present.

            Value should be of type bool

        enumerator CHARGER\_PROP\_STATUS
        :   Represents the charging status of the charger.

            Value should be of type enum [charger\_status](#group__charger__interface_1ga4a3c46bc0916082d15e665f7665c89d7)

        enumerator CHARGER\_PROP\_CHARGE\_TYPE
        :   Represents the charging algo type of the charger.

            Value should be of type enum [charger\_charge\_type](#group__charger__interface_1gaee833a379a8674621d2fdf9b57d1f803)

        enumerator CHARGER\_PROP\_HEALTH
        :   Represents the health of the charger.

            Value should be of type enum [charger\_health](#group__charger__interface_1gaab33241d3b85ab0770be9b1bd17e4412)

        enumerator CHARGER\_PROP\_CONSTANT\_CHARGE\_CURRENT\_UA
        :   Configuration of current sink used for charging in µA.

        enumerator CHARGER\_PROP\_PRECHARGE\_CURRENT\_UA
        :   Configuration of current sink used for conditioning in µA.

        enumerator CHARGER\_PROP\_CHARGE\_TERM\_CURRENT\_UA
        :   Configuration of charge termination target in µA.

        enumerator CHARGER\_PROP\_CONSTANT\_CHARGE\_VOLTAGE\_UV
        :   Configuration of charge voltage regulation target in µV.

        enumerator CHARGER\_PROP\_INPUT\_REGULATION\_CURRENT\_UA
        :   Configuration of the input current regulation target in µA.

            This value is a rising current threshold that is regulated by reducing the charge current output

        enumerator CHARGER\_PROP\_INPUT\_REGULATION\_VOLTAGE\_UV
        :   Configuration of the input voltage regulation target in µV.

            This value is a falling voltage threshold that is regulated by reducing the charge current output

        enumerator CHARGER\_PROP\_INPUT\_CURRENT\_NOTIFICATION
        :   Configuration to issue a notification to the system based on the input current level and timing.

            Value should be of type struct charger\_input\_current\_notifier

        enumerator CHARGER\_PROP\_COMMON\_COUNT
        :   Reserved to demark end of common charger properties.

        enumerator CHARGER\_PROP\_CUSTOM\_BEGIN = [CHARGER\_PROP\_COMMON\_COUNT](#c.charger_property.CHARGER_PROP_COMMON_COUNT) + 1
        :   Reserved to demark downstream custom properties - use this value as the actual value may change over future versions of this API.

        enumerator CHARGER\_PROP\_MAX = UINT16\_MAX
        :   Reserved to demark end of valid enum properties.

    enum charger\_online
    :   External supply states.

        *Values:*

        enumerator CHARGER\_ONLINE\_OFFLINE = 0
        :   External supply not present.

        enumerator CHARGER\_ONLINE\_FIXED
        :   External supply is present and of fixed output.

        enumerator CHARGER\_ONLINE\_PROGRAMMABLE
        :   External supply is present and of programmable output.

    enum charger\_status
    :   Charging states.

        *Values:*

        enumerator CHARGER\_STATUS\_UNKNOWN = 0
        :   Charging device state is unknown.

        enumerator CHARGER\_STATUS\_CHARGING
        :   Charging device is charging a battery.

        enumerator CHARGER\_STATUS\_DISCHARGING
        :   Charging device is not able to charge a battery.

        enumerator CHARGER\_STATUS\_NOT\_CHARGING
        :   Charging device is not charging a battery.

        enumerator CHARGER\_STATUS\_FULL
        :   The battery is full and the charging device will not attempt charging.

    enum charger\_charge\_type
    :   Charge algorithm types.

        *Values:*

        enumerator CHARGER\_CHARGE\_TYPE\_UNKNOWN = 0
        :   Charge type is unknown.

        enumerator CHARGER\_CHARGE\_TYPE\_NONE
        :   Charging is not occurring.

        enumerator CHARGER\_CHARGE\_TYPE\_TRICKLE
        :   Charging is occurring at the slowest desired charge rate, typically for battery detection or preconditioning.

        enumerator CHARGER\_CHARGE\_TYPE\_FAST
        :   Charging is occurring at the fastest desired charge rate.

        enumerator CHARGER\_CHARGE\_TYPE\_STANDARD
        :   Charging is occurring at a moderate charge rate.

        enumerator CHARGER\_CHARGE\_TYPE\_ADAPTIVE

        enumerator CHARGER\_CHARGE\_TYPE\_LONGLIFE

        enumerator CHARGER\_CHARGE\_TYPE\_BYPASS

    enum charger\_health
    :   Charger health conditions.

        These conditions determine the ability to, or the rate of, charge

        *Values:*

        enumerator CHARGER\_HEALTH\_UNKNOWN = 0
        :   Charger health condition is unknown.

        enumerator CHARGER\_HEALTH\_GOOD
        :   Charger health condition is good.

        enumerator CHARGER\_HEALTH\_OVERHEAT
        :   The charger device is overheated.

        enumerator CHARGER\_HEALTH\_OVERVOLTAGE
        :   The battery voltage has exceeded its overvoltage threshold.

        enumerator CHARGER\_HEALTH\_UNSPEC\_FAILURE
        :   The battery or charger device is experiencing an unspecified failure.

        enumerator CHARGER\_HEALTH\_COLD
        :   The battery temperature is below the “cold” threshold.

        enumerator CHARGER\_HEALTH\_WATCHDOG\_TIMER\_EXPIRE
        :   The charger device’s watchdog timer has expired.

        enumerator CHARGER\_HEALTH\_SAFETY\_TIMER\_EXPIRE
        :   The charger device’s safety timer has expired.

        enumerator CHARGER\_HEALTH\_CALIBRATION\_REQUIRED
        :   The charger device requires calibration.

        enumerator CHARGER\_HEALTH\_WARM
        :   The battery temperature is in the “warm” range.

        enumerator CHARGER\_HEALTH\_COOL
        :   The battery temperature is in the “cool” range.

        enumerator CHARGER\_HEALTH\_HOT
        :   The battery temperature is below the “hot” threshold.

        enumerator CHARGER\_HEALTH\_NO\_BATTERY
        :   The charger device does not detect a battery.

    enum charger\_notification\_severity
    :   Charger severity levels for system notifications.

        *Values:*

        enumerator CHARGER\_SEVERITY\_PEAK = 0
        :   Most severe level, typically triggered instantaneously.

        enumerator CHARGER\_SEVERITY\_CRITICAL
        :   More severe than the warning level, less severe than peak.

        enumerator CHARGER\_SEVERITY\_WARNING
        :   Base severity level.

    Functions

    int charger\_get\_prop(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const [charger\_prop\_t](#c.charger_prop_t) prop, union [charger\_propval](#c.charger_propval) \*val)
    :   Fetch a battery charger property.

        Parameters:
        :   - **dev** – Pointer to the battery charger device
            - **prop** – Charger property to get
            - **val** – Pointer to [charger\_propval](#unioncharger__propval) union

        Return values:
        :   - **0** – if successful
            - **<** – 0 if getting property failed

    int charger\_set\_prop(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const [charger\_prop\_t](#c.charger_prop_t) prop, const union [charger\_propval](#c.charger_propval) \*val)
    :   Set a battery charger property.

        Parameters:
        :   - **dev** – Pointer to the battery charger device
            - **prop** – Charger property to set
            - **val** – Pointer to [charger\_propval](#unioncharger__propval) union

        Return values:
        :   - **0** – if successful
            - **<** – 0 if setting property failed

    int charger\_charge\_enable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const bool enable)
    :   Enable or disable a charge cycle.

        Parameters:
        :   - **dev** – Pointer to the battery charger device
            - **enable** – true enables a charge cycle, false disables a charge cycle

        Return values:
        :   - **0** – if successful
            - **-EIO** – if communication with the charger failed
            - **-EINVAL** – if the conditions for initiating charging are invalid

    struct charger\_current\_notifier
    :   *#include <charger.h>*

        The input current thresholds for the charger to notify the system.

        Public Members

        uint8\_t severity
        :   The severity of the notification where CHARGER\_SEVERITY\_PEAK is the most severe.

        uint32\_t current\_ua
        :   The current threshold to be exceeded.

        uint32\_t duration\_us
        :   The duration of excess current before notifying the system.

    union charger\_propval
    :   *#include <charger.h>*

        container for a [charger\_property](#group__charger__interface_1ga6eb3b4cc76e4f1e34732b7853eb860b7) value

        Public Members

        enum [charger\_online](#c.charger_online) online
        :   CHARGER\_PROP\_ONLINE.

        bool present
        :   CHARGER\_PROP\_PRESENT.

        enum [charger\_status](#c.charger_status) status
        :   CHARGER\_PROP\_STATUS.

        enum [charger\_charge\_type](#c.charger_charge_type) charge\_type
        :   CHARGER\_PROP\_CHARGE\_TYPE.

        enum [charger\_health](#c.charger_health) health
        :   CHARGER\_PROP\_HEALTH.

        uint32\_t const\_charge\_current\_ua
        :   CHARGER\_PROP\_CONSTANT\_CHARGE\_CURRENT\_UA.

        uint32\_t precharge\_current\_ua
        :   CHARGER\_PROP\_PRECHARGE\_CURRENT\_UA.

        uint32\_t charge\_term\_current\_ua
        :   CHARGER\_PROP\_CHARGE\_TERM\_CURRENT\_UA.

        uint32\_t const\_charge\_voltage\_uv
        :   CHARGER\_PROP\_CONSTANT\_CHARGE\_VOLTAGE\_UV.

        uint32\_t input\_current\_regulation\_current\_ua
        :   CHARGER\_PROP\_INPUT\_REGULATION\_CURRENT\_UA.

        uint32\_t input\_voltage\_regulation\_voltage\_uv
        :   CHARGER\_PROP\_INPUT\_REGULATION\_VOLTAGE\_UV.

        struct [charger\_current\_notifier](#c.charger_current_notifier) input\_current\_notification
        :   CHARGER\_PROP\_INPUT\_CURRENT\_NOTIFICATION.

    struct charger\_driver\_api
    :   *#include <charger.h>*

        Charging device API.

        Caching is entirely on the onus of the client
