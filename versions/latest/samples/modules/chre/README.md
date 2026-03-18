---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/modules/chre/README.html
original_path: samples/modules/chre/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Android’s Context Hub Runtime Environment (CHRE)

Android’s context hub enables the use of nanoapps. A single nanoapp has 3 entry points seen in
[chre\_api/chre/nanoapp.h](https://cs.android.com/android/platform/superproject/+/master:system/chre/chre_api/include/chre_api/chre/nanoapp.h;drc=7c60a553288d63e6e3370d679803da46dac723a4):

- A `nanoappStart` function used to notify the nanoapp that it is now active.
- A `nanoappHandleEvent` function used to notify the nanoapp tha an event of interest took place.
- A `nanoappEnd` function used to notify the nanoapp that it is now deactivated.

The CHRE connects to several frameworks called Platform Abstraction Layers (PAL)s. Note that
currently, none of these are implemented for Zephyr, but they are scheduled to be added. These
frameworks include:

1. *Audio* - a framework allowing nanoapps to get audio events. See [pal/audio.h](https://cs.android.com/android/platform/superproject/+/master:system/chre/pal/include/chre/pal/audio.h;l=69;drc=6ca547ad175f80ce9f09f5b7b14fcc6f14565f5c) for API details.
2. *GNSS* - a framework allowing nanoapps to manage location and measurement sessions. See
   [pal/gnss.h](https://cs.android.com/android/platform/superproject/+/master:system/chre/pal/include/chre/pal/gnss.h;l=152;drc=830255234157cc7afe5201dca19a7fb71ea850fe) for API details.
3. *Sensor* - a framework allowing nanoapps to request changes to sensors configuration get
   data/bias events. See [pal/sensor.h](https://cs.android.com/android/platform/superproject/+/master:system/chre/pal/include/chre/pal/sensor.h;l=51;drc=23207906add05054a94dfab41b95bcfc39bedfe4) for API details.
4. *System* - a framework allowing nanoapps to make common system requests such as logging, clock,
   and some basic memory allocation/deallocation. See [pal/system.h](https://cs.android.com/android/platform/superproject/+/master:system/chre/pal/include/chre/pal/system.h;l=49;drc=6ca547ad175f80ce9f09f5b7b14fcc6f14565f5c) for API details.
5. *WiFi* - a framework allowing nanoapps to interact with the on board WiFi. See [pal/wifi.h](https://cs.android.com/android/platform/superproject/+/master:system/chre/pal/include/chre/pal/wifi.h;l=153;drc=b673b80ed98e1b6e6360bee4ba98e2cd8f4e0935) for
   API details.
6. *WWAN* - a framework allowing nanoapps to interact with the WWAN module such as getting the
   current capabilities and info. See [pal/wwan.h](https://cs.android.com/android/platform/superproject/+/master:system/chre/pal/include/chre/pal/wwan.h;l=69;drc=629361a803cb305c8575b41614e6e071e7141a03) for API details.

## Building and expectations

To build the sample use the following west command:

```shell
# From the root of the zephyr repository
west build -b native_sim samples/modules/chre
```

Once built and run, the sample application should:

1. Print a hello message
2. Notify that the event loop started via an `inf` level log
3. Notify that a nanoapp was started and assigned an instance/app ID of 1 via a `dbg` level log
4. Print a message saying that the nanoapp’s start callback was called
5. Send an event of type `1` and no data to the nanoapp
6. Notify that the event was processed
7. Call the `nanoappEnd` function of the nanoapp
8. Print a message notifying that it’s not possible to remove a system level nanoapp
9. Exit the event loop

## Roadmap

1. Add an implementation of the [pal/sensor.h](https://cs.android.com/android/platform/superproject/+/master:system/chre/pal/include/chre/pal/sensor.h;l=51;drc=23207906add05054a94dfab41b95bcfc39bedfe4) and [pal/system.h](https://cs.android.com/android/platform/superproject/+/master:system/chre/pal/include/chre/pal/system.h;l=49;drc=6ca547ad175f80ce9f09f5b7b14fcc6f14565f5c) to Zephyr. These will be
   standalone modules that can be used independently of CHRE, but when `CONFIG_CHRE` is enabled
   will also provide an implementation of `chrePalSensorGetApi()` and `struct chrePalSystemApi`.
2. Add a directory `chre/nanoapps` which will host various nanoapps to be used by the Zephyr
   community. These should each have their own Kconfig to enable them and set the appropriate
   dependencies. The first nanoapp will be a lid angle calculator which will use 2 accelerometers.
3. Update the `overlay.dts` of this sample application to include 2 emulated accelerometers and
   configure them to return scripted data.
4. Run this sample application and watch the nanoapp provide lid angle calculations based on 2
   accelerometers provided by the sensors PAL framework.
