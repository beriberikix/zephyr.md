---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/gnss.html
original_path: hardware/peripherals/gnss.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# GNSS (Global Navigation Satellite System)

## Overview

GNSS is a general term which covers satellite systems used for
navigation, like GPS (Global Positioning System). GNSS services
are usually accessed through GNSS modems which receive and
process GNSS signals to determine their position, or more
specifically, their antennas position. They usually
additionally provide a precise time synchronization mechanism,
commonly named PPS (Pulse-Per-Second).

## Subsystem support

The GNSS subsystem is based on the [Modem modules](../../services/modem/index.md#modem). The GNSS
subsystem covers everything from sending and receiving commands
to and from the modem, to parsing, creating and processing
NMEA0183 messages.

Adding support for additional NMEA0183 based GNSS modems
requires little more than implementing power management
and configuration for the specific GNSS modem.

Adding support for GNSS modems which use other protocols and/or
buses than the usual NMEA0183 over UART is possible, but will
require a bit more work from the driver developer.

## Configuration Options

Related configuration options:

- [`CONFIG_GNSS`](../../kconfig.md#CONFIG_GNSS "CONFIG_GNSS")
- [`CONFIG_GNSS_SATELLITES`](../../kconfig.md#CONFIG_GNSS_SATELLITES "CONFIG_GNSS_SATELLITES")
- [`CONFIG_GNSS_DUMP_TO_LOG`](../../kconfig.md#CONFIG_GNSS_DUMP_TO_LOG "CONFIG_GNSS_DUMP_TO_LOG")

## Navigation Reference

Related code samples

[GNSS](../../samples/drivers/gnss/README.md#gnss "Connect to a GNSS device to obtain time, navigation data, and satellite information.")
:   Connect to a GNSS device to obtain time, navigation data, and satellite information.

*group* Navigation
:   Navigation utilities.

    Functions

    int navigation\_distance(uint64\_t \*distance, const struct [navigation\_data](#c.navigation_data) \*p1, const struct [navigation\_data](#c.navigation_data) \*p2)
    :   Calculate the distance between two navigation points along the surface of the sphere they are relative to.

        Parameters:
        :   - **distance** – Destination for calculated distance in millimeters
            - **p1** – First navigation point
            - **p2** – Second navigation point

        Returns:
        :   0 if successful

        Returns:
        :   -EINVAL if either navigation point is invalid

    int navigation\_bearing(uint32\_t \*bearing, const struct [navigation\_data](#c.navigation_data) \*from, const struct [navigation\_data](#c.navigation_data) \*to)
    :   Calculate the bearing from one navigation point to another.

        Parameters:
        :   - **bearing** – Destination for calculated bearing angle in millidegrees
            - **from** – First navigation point
            - **to** – Second navigation point

        Returns:
        :   0 if successful

        Returns:
        :   -EINVAL if either navigation point is invalid

    struct navigation\_data
    :   *#include <navigation.h>*

        Navigation data structure.

        The structure describes the momentary navigation details of a point relative to a sphere (commonly Earth)

        Public Members

        int64\_t latitude
        :   Latitudal position in nanodegrees (0 to +-180E9).

        int64\_t longitude
        :   Longitudal position in nanodegrees (0 to +-180E9).

        uint32\_t bearing
        :   Bearing angle in millidegrees (0 to 360E3).

        uint32\_t speed
        :   Speed in millimeters per second.

        int32\_t altitude
        :   Altitude in millimeters.

## GNSS API Reference

Related code samples

[GNSS](../../samples/drivers/gnss/README.md#gnss "Connect to a GNSS device to obtain time, navigation data, and satellite information.")
:   Connect to a GNSS device to obtain time, navigation data, and satellite information.

*group* GNSS Interface
:   GNSS Interface.

    **Since**
    :   3.6

    **Version**
    :   0.1.0

    Defines

    GNSS\_DATA\_CALLBACK\_DEFINE(\_dev, \_callback)
    :   Register a callback structure for GNSS data published.

        Parameters:
        :   - **\_dev** – Device pointer
            - **\_callback** – The callback function

    GNSS\_SATELLITES\_CALLBACK\_DEFINE(\_dev, \_callback)
    :   Register a callback structure for GNSS satellites published.

        Parameters:
        :   - **\_dev** – Device pointer
            - **\_callback** – The callback function

    Typedefs

    typedef int (\*gnss\_set\_fix\_rate\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t fix\_interval\_ms)
    :   API for setting fix rate.

    typedef int (\*gnss\_get\_fix\_rate\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t \*fix\_interval\_ms)
    :   API for getting fix rate.

    typedef int (\*gnss\_set\_periodic\_config\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [gnss\_periodic\_config](#c.gnss_periodic_config) \*periodic\_config)
    :   API for setting periodic tracking configuration.

    typedef int (\*gnss\_get\_periodic\_config\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [gnss\_periodic\_config](#c.gnss_periodic_config) \*periodic\_config)
    :   API for setting periodic tracking configuration.

    typedef int (\*gnss\_set\_navigation\_mode\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [gnss\_navigation\_mode](#c.gnss_navigation_mode) mode)
    :   API for setting navigation mode.

    typedef int (\*gnss\_get\_navigation\_mode\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [gnss\_navigation\_mode](#c.gnss_navigation_mode) \*mode)
    :   API for getting navigation mode.

    typedef uint32\_t gnss\_systems\_t
    :   Type storing bitmask of GNSS systems.

    typedef int (\*gnss\_set\_enabled\_systems\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [gnss\_systems\_t](#c.gnss_systems_t) systems)
    :   API for enabling systems.

    typedef int (\*gnss\_get\_enabled\_systems\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [gnss\_systems\_t](#c.gnss_systems_t) \*systems)
    :   API for getting enabled systems.

    typedef int (\*gnss\_get\_supported\_systems\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [gnss\_systems\_t](#c.gnss_systems_t) \*systems)
    :   API for getting enabled systems.

    typedef void (\*gnss\_data\_callback\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [gnss\_data](#c.gnss_data) \*data)
    :   Template for GNSS data callback.

    typedef void (\*gnss\_satellites\_callback\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [gnss\_satellite](#c.gnss_satellite) \*satellites, uint16\_t size)
    :   Template for GNSS satellites callback.

    Enums

    enum gnss\_pps\_mode
    :   GNSS PPS modes.

        *Values:*

        enumerator GNSS\_PPS\_MODE\_DISABLED = 0
        :   PPS output disabled.

        enumerator GNSS\_PPS\_MODE\_ENABLED = 1
        :   PPS output always enabled.

        enumerator GNSS\_PPS\_MODE\_ENABLED\_AFTER\_LOCK = 2
        :   PPS output enabled from first lock.

        enumerator GNSS\_PPS\_MODE\_ENABLED\_WHILE\_LOCKED = 3
        :   PPS output enabled while locked.

    enum gnss\_navigation\_mode
    :   GNSS navigation modes.

        *Values:*

        enumerator GNSS\_NAVIGATION\_MODE\_ZERO\_DYNAMICS = 0
        :   Dynamics have no impact on tracking.

        enumerator GNSS\_NAVIGATION\_MODE\_LOW\_DYNAMICS = 1
        :   Low dynamics have higher impact on tracking.

        enumerator GNSS\_NAVIGATION\_MODE\_BALANCED\_DYNAMICS = 2
        :   Low and high dynamics have equal impact on tracking.

        enumerator GNSS\_NAVIGATION\_MODE\_HIGH\_DYNAMICS = 3
        :   High dynamics have higher impact on tracking.

    enum gnss\_system
    :   Systems contained in [gnss\_systems\_t](#group__gnss__interface_1ga731907f9ae501909bf26ecae5441a5ce).

        *Values:*

        enumerator GNSS\_SYSTEM\_GPS = [BIT](../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Global Positioning System (GPS).

        enumerator GNSS\_SYSTEM\_GLONASS = [BIT](../../kernel/util/index.md#c.BIT "BIT")(1)
        :   GLObal NAvigation Satellite System (GLONASS).

        enumerator GNSS\_SYSTEM\_GALILEO = [BIT](../../kernel/util/index.md#c.BIT "BIT")(2)
        :   Galileo.

        enumerator GNSS\_SYSTEM\_BEIDOU = [BIT](../../kernel/util/index.md#c.BIT "BIT")(3)
        :   BeiDou Navigation Satellite System.

        enumerator GNSS\_SYSTEM\_QZSS = [BIT](../../kernel/util/index.md#c.BIT "BIT")(4)
        :   Quasi-Zenith Satellite System (QZSS).

        enumerator GNSS\_SYSTEM\_IRNSS = [BIT](../../kernel/util/index.md#c.BIT "BIT")(5)
        :   Indian Regional Navigation Satellite System (IRNSS).

        enumerator GNSS\_SYSTEM\_SBAS = [BIT](../../kernel/util/index.md#c.BIT "BIT")(6)
        :   Satellite-Based Augmentation System (SBAS).

        enumerator GNSS\_SYSTEM\_IMES = [BIT](../../kernel/util/index.md#c.BIT "BIT")(7)
        :   Indoor Messaging System (IMES).

    enum gnss\_fix\_status
    :   GNSS fix status.

        *Values:*

        enumerator GNSS\_FIX\_STATUS\_NO\_FIX = 0
        :   No GNSS fix acquired.

        enumerator GNSS\_FIX\_STATUS\_GNSS\_FIX = 1
        :   GNSS fix acquired.

        enumerator GNSS\_FIX\_STATUS\_DGNSS\_FIX = 2
        :   Differential GNSS fix acquired.

        enumerator GNSS\_FIX\_STATUS\_ESTIMATED\_FIX = 3
        :   Estimated fix acquired.

    enum gnss\_fix\_quality
    :   GNSS fix quality.

        *Values:*

        enumerator GNSS\_FIX\_QUALITY\_INVALID = 0
        :   Invalid fix.

        enumerator GNSS\_FIX\_QUALITY\_GNSS\_SPS = 1
        :   Standard positioning service.

        enumerator GNSS\_FIX\_QUALITY\_DGNSS = 2
        :   Differential GNSS.

        enumerator GNSS\_FIX\_QUALITY\_GNSS\_PPS = 3
        :   Precise positioning service.

        enumerator GNSS\_FIX\_QUALITY\_RTK = 4
        :   Real-time kinematic.

        enumerator GNSS\_FIX\_QUALITY\_FLOAT\_RTK = 5
        :   Floating real-time kinematic.

        enumerator GNSS\_FIX\_QUALITY\_ESTIMATED = 6
        :   Estimated fix.

    Functions

    int gnss\_set\_fix\_rate(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t fix\_interval\_ms)
    :   Set the GNSS fix rate.

        Parameters:
        :   - **dev** – Device instance
            - **fix\_interval\_ms** – Fix interval to set in milliseconds

        Returns:
        :   0 if successful

        Returns:
        :   -errno negative errno code on failure

    int gnss\_get\_fix\_rate(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t \*fix\_interval\_ms)
    :   Get the GNSS fix rate.

        Parameters:
        :   - **dev** – Device instance
            - **fix\_interval\_ms** – Destination for fix interval in milliseconds

        Returns:
        :   0 if successful

        Returns:
        :   -errno negative errno code on failure

    int gnss\_set\_periodic\_config(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [gnss\_periodic\_config](#c.gnss_periodic_config) \*config)
    :   Set the GNSS periodic tracking configuration.

        Parameters:
        :   - **dev** – Device instance
            - **config** – Periodic tracking configuration to set

        Returns:
        :   0 if successful

        Returns:
        :   -errno negative errno code on failure

    int gnss\_get\_periodic\_config(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [gnss\_periodic\_config](#c.gnss_periodic_config) \*config)
    :   Get the GNSS periodic tracking configuration.

        Parameters:
        :   - **dev** – Device instance
            - **config** – Destination for periodic tracking configuration

        Returns:
        :   0 if successful

        Returns:
        :   -errno negative errno code on failure

    int gnss\_set\_navigation\_mode(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [gnss\_navigation\_mode](#c.gnss_navigation_mode) mode)
    :   Set the GNSS navigation mode.

        Parameters:
        :   - **dev** – Device instance
            - **mode** – Navigation mode to set

        Returns:
        :   0 if successful

        Returns:
        :   -errno negative errno code on failure

    int gnss\_get\_navigation\_mode(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [gnss\_navigation\_mode](#c.gnss_navigation_mode) \*mode)
    :   Get the GNSS navigation mode.

        Parameters:
        :   - **dev** – Device instance
            - **mode** – Destination for navigation mode

        Returns:
        :   0 if successful

        Returns:
        :   -errno negative errno code on failure

    int gnss\_set\_enabled\_systems(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [gnss\_systems\_t](#c.gnss_systems_t) systems)
    :   Set enabled GNSS systems.

        Parameters:
        :   - **dev** – Device instance
            - **systems** – Systems to enable

        Returns:
        :   0 if successful

        Returns:
        :   -errno negative errno code on failure

    int gnss\_get\_enabled\_systems(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [gnss\_systems\_t](#c.gnss_systems_t) \*systems)
    :   Get enabled GNSS systems.

        Parameters:
        :   - **dev** – Device instance
            - **systems** – Destination for enabled systems

        Returns:
        :   0 if successful

        Returns:
        :   -errno negative errno code on failure

    int gnss\_get\_supported\_systems(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [gnss\_systems\_t](#c.gnss_systems_t) \*systems)
    :   Get supported GNSS systems.

        Parameters:
        :   - **dev** – Device instance
            - **systems** – Destination for supported systems

        Returns:
        :   0 if successful

        Returns:
        :   -errno negative errno code on failure

    struct gnss\_periodic\_config
    :   *#include <gnss.h>*

        GNSS periodic tracking configuration.

        Note

        Setting either active\_time or inactive\_time to 0 will disable periodic function.

        Public Members

        uint32\_t active\_time\_ms
        :   The time the GNSS will spend in the active state in ms.

        uint32\_t inactive\_time\_ms
        :   The time the GNSS will spend in the inactive state in ms.

    struct gnss\_info
    :   *#include <gnss.h>*

        GNSS info data structure.

        Public Members

        uint16\_t satellites\_cnt
        :   Number of satellites being tracked.

        uint32\_t hdop
        :   Horizontal dilution of precision in 1/1000.

        enum [gnss\_fix\_status](#c.gnss_fix_status) fix\_status
        :   The fix status.

        enum [gnss\_fix\_quality](#c.gnss_fix_quality) fix\_quality
        :   The fix quality.

    struct gnss\_time
    :   *#include <gnss.h>*

        GNSS time data structure.

        Public Members

        uint8\_t hour
        :   Hour [0, 23].

        uint8\_t minute
        :   Minute [0, 59].

        uint16\_t millisecond
        :   Millisecond [0, 59999].

        uint8\_t month\_day
        :   Day of month [1, 31].

        uint8\_t month
        :   Month [1, 12].

        uint8\_t century\_year
        :   Year [0, 99].

    struct gnss\_driver\_api
    :   *#include <gnss.h>*

        GNSS API structure.

    struct gnss\_data
    :   *#include <gnss.h>*

        GNSS data structure.

        Public Members

        struct [navigation\_data](#c.navigation_data) nav\_data
        :   Navigation data acquired.

        struct [gnss\_info](#c.gnss_info) info
        :   GNSS info when navigation data was acquired.

        struct [gnss\_time](#c.gnss_time) utc
        :   UTC time when data was acquired.

    struct gnss\_data\_callback
    :   *#include <gnss.h>*

        GNSS callback structure.

        Public Members

        const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev
        :   Filter callback to GNSS data from this device if not NULL.

        [gnss\_data\_callback\_t](#c.gnss_data_callback_t) callback
        :   Callback called when GNSS data is published.

    struct gnss\_satellite
    :   *#include <gnss.h>*

        GNSS satellite structure.

        Public Members

        uint8\_t prn
        :   Pseudo-random noise sequence.

        uint8\_t snr
        :   Signal-to-noise ratio in dB.

        uint8\_t elevation
        :   Elevation in degrees [0, 90].

        uint16\_t azimuth
        :   Azimuth relative to True North in degrees [0, 359].

        enum [gnss\_system](#c.gnss_system) system
        :   System of satellite.

        uint8\_t is\_tracked
        :   True if satellite is being tracked.

    struct gnss\_satellites\_callback
    :   *#include <gnss.h>*

        GNSS callback structure.

        Public Members

        const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev
        :   Filter callback to GNSS data from this device if not NULL.

        [gnss\_satellites\_callback\_t](#c.gnss_satellites_callback_t) callback
        :   Callback called when GNSS satellites is published.
