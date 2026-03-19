---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/peripherals/sensor/index.html
original_path: hardware/peripherals/sensor/index.html
---

# Sensors

The sensor driver API provides functionality to uniformly read, configure,
and setup event handling for devices that take real world measurements in
meaningful units.

Sensors range from very simple temperature-reading devices that must be polled
with a fixed scale to complex devices taking in readings from multitudes of
sensors and themselves producing new inferred sensor data such as step counts,
presence detection, orientation, and more.

Supporting this wide breadth of devices is a demanding task and the sensor API
attempts to provide a uniform interface to them.

## Using Sensors

Using sensors from an application there are some APIs and terms that are helpful
to understand. Sensors in Zephyr are composed of [Sensor Channels](channels.md#sensor-channel),
[Sensor Attributes](attributes.md#sensor-attribute), and [Sensor Triggers](triggers.md#sensor-trigger). Attributes and triggers may
be device or channel specific.

Note

Getting samples from sensors using the sensor API today can be done in one of
two ways. A stable and long-lived API [Fetch and Get](fetch_and_get.md#sensor-fetch-and-get), or a newer
but rapidly stabilizing API [Read and Decode](read_and_decode.md#sensor-read-and-decode). It’s expected that
in the near future [Fetch and Get](fetch_and_get.md#sensor-fetch-and-get) will be deprecated in favor of
[Read and Decode](read_and_decode.md#sensor-read-and-decode). Triggers are handled entirely differently for
[Fetch and Get](fetch_and_get.md#sensor-fetch-and-get) or [Read and Decode](read_and_decode.md#sensor-read-and-decode) and the
differences are noted in each of those sections.

## Implementing Sensor Drivers

Note

Implementing the driver side of the sensor API requires an understanding how
the sensor APIs are used. Please read through [Using Sensors](#sensor-using) first!

### Implementing Attributes

- SHOULD implement attribute setting in a blocking manner.
- SHOULD provide the ability to get and set channel scale if supported by the
  device.
- SHOULD provide the ability to get and set channel sampling rate if supported
  by the device.

### Implementing Fetch and Get

- SHOULD implement [`sensor_sample_fetch_t`](../../../doxygen/html/group__sensor__interface.md#gacae110a4edb6f29dfb457cb1ea8d68c1) as a blocking call that
  stashes the specified channels (or all sensor channels) as driver instance
  data.
- SHOULD implement [`sensor_channel_get_t`](../../../doxygen/html/group__sensor__interface.md#ga5c9b5ed9097464562004b446856043fd) without side effects
  manipulating driver state returning stashed sensor readings.
- SHOULD implement [`sensor_trigger_set_t`](../../../doxygen/html/group__sensor__interface.md#gad7f7a3d9e714cc16f23656ca06592aa4) storing the address of the
  [`sensor_trigger`](../../../doxygen/html/structsensor__trigger.md) rather than copying the contents. This is so
  [`CONTAINER_OF`](../../../doxygen/html/group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f) may be used for trigger callback context.

### Implementing Read and Decode

- MUST implement [`sensor_submit_t`](../../../doxygen/html/group__sensor__interface.md#gad77732c8f0ec5520cdd71c2829787981) as a non-blocking call.
- SHOULD implement [`sensor_submit_t`](../../../doxygen/html/group__sensor__interface.md#gad77732c8f0ec5520cdd71c2829787981) using [Real Time I/O (RTIO)](../../../services/rtio/index.md#rtio) to do non-blocking bus transfers if possible.
- MAY implement [`sensor_submit_t`](../../../doxygen/html/group__sensor__interface.md#gad77732c8f0ec5520cdd71c2829787981) using a work queue if
  [Real Time I/O (RTIO)](../../../services/rtio/index.md#rtio) is unsupported by the bus.
- SHOULD implement [`sensor_submit_t`](../../../doxygen/html/group__sensor__interface.md#gad77732c8f0ec5520cdd71c2829787981) checking the [`rtio_sqe`](../../../doxygen/html/structrtio__sqe.md)
  is of type `RTIO_SQE_RX` (read request).
- SHOULD implement [`sensor_submit_t`](../../../doxygen/html/group__sensor__interface.md#gad77732c8f0ec5520cdd71c2829787981) checking all requested channels
  supported or respond with an error if not.
- SHOULD implement [`sensor_submit_t`](../../../doxygen/html/group__sensor__interface.md#gad77732c8f0ec5520cdd71c2829787981) checking the provided buffer
  is large enough for the requested channels.
- SHOULD implement [`sensor_submit_t`](../../../doxygen/html/group__sensor__interface.md#gad77732c8f0ec5520cdd71c2829787981) in a way that directly reads into
  the provided buffer avoiding copying of any kind, with few exceptions.
- MUST implement [`sensor_decoder_api`](../../../doxygen/html/structsensor__decoder__api.md) with pure stateless functions. All state needed to convert the raw sensor readings into
  fixed point SI united values must be in the provided buffer.
- MUST implement [`sensor_get_decoder_t`](../../../doxygen/html/group__sensor__interface.md#ga21e407d552d140cfb6bfd0d9513c7d42) returning the
  [`sensor_decoder_api`](../../../doxygen/html/structsensor__decoder__api.md) for that device type.

## API Reference

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)

Related code samples

- [ADT7420 high-accuracy digital I2C temperature sensor](../../../samples/sensor/adt7420/README.md#adt7420 "Get temperature data from an ADT7420 sensor using polling and window mode.")Get temperature data from an ADT7420 sensor using polling and window mode.
- [AMG88XX infrared array sensor](../../../samples/sensor/amg88xx/README.md#amg88xx "Get temperature data from an AMG88XX 8x8 thermal camera sensor.")Get temperature data from an AMG88XX 8x8 thermal camera sensor.
- [ams iAQcore indoor air quality sensor](../../../samples/sensor/ams_iAQcore/README.md#ams_iaqcore "Get CO2 equivalent and VOC data from an ams iAQcore sensor.")Get CO2 equivalent and VOC data from an ams iAQcore sensor.
- [APDS9960 RGB, ambient light, and gesture sensor](../../../samples/sensor/apds9960/README.md#apds9960 "Get ambient light, RGB, and proximity/gesture data from an APDS9960 sensor.")Get ambient light, RGB, and proximity/gesture data from an APDS9960 sensor.
- [BME280 humidity and pressure sensor](../../../samples/sensor/bme280/README.md#bme280 "Get temperature, pressure, and humidity data from a BME280 sensor.")Get temperature, pressure, and humidity data from a BME280 sensor.
- [BMI270 6-axis IMU sensor](../../../samples/sensor/bmi270/README.md#bmi270 "Configure and read accelerometer and gyroscope data from a BMI270 sensor.")Configure and read accelerometer and gyroscope data from a BMI270 sensor.
- [BQ274XX fuel gauge sensor](../../../samples/sensor/bq274xx/README.md#bq274xx "Get various fuel gauge parameters from a BQ274XX sensor.")Get various fuel gauge parameters from a BQ274XX sensor.
- [CCS811 indoor air quality sensor](../../../samples/sensor/ccs811/README.md#ccs811 "Get CO2 equivalent and VOC data from a CCS811 sensor.")Get CO2 equivalent and VOC data from a CCS811 sensor.
- [CPU die temperature polling](../../../samples/sensor/die_temp_polling/README.md#die_temp_polling "Get CPU die temperature data from a sensor using polling.")Get CPU die temperature data from a sensor using polling.
- [DS18B20 1-Wire Temperature Sensor](../../../samples/sensor/ds18b20/README.md#ds18b20 "Get ambient temperature data from a DS18B20 sensor (polling mode).")Get ambient temperature data from a DS18B20 sensor (polling mode).
- [FDC2X1X Capacitance-to-Digital Converter](../../../samples/sensor/fdc2x1x/README.md#fdc2x1x "Get capacitance and frequency data from a FDC2X1X sensor (polling & trigger).")Get capacitance and frequency data from a FDC2X1X sensor (polling & trigger).
- [FXAS21002 Gyroscope Sensor](../../../samples/sensor/fxas21002/README.md#fxas21002 "Get gyroscope data synchronously from an FXAS21002 sensor.")Get gyroscope data synchronously from an FXAS21002 sensor.
- [FXOS8700 Accelerometer/Magnetometer Sensor](../../../samples/sensor/fxos8700/README.md#fxos8700 "Get accelerometer and magnetometer data from an FXOS8700 sensor (polling & trigger mode).")Get accelerometer and magnetometer data from an FXOS8700 sensor (polling & trigger mode).
- [Generic 3-Axis accelerometer polling](../../../samples/sensor/accel_polling/README.md#accel_polling "Get 3-Axis accelerometer data from a sensor (polling mode).")Get 3-Axis accelerometer data from a sensor (polling mode).
- [Generic CO2 polling sample](../../../samples/sensor/co2_polling/README.md#co2 "Get CO2 data from a sensor (polling mode).")Get CO2 data from a sensor (polling mode).
- [Generic digital humidity temperature sensor polling](../../../samples/sensor/dht_polling/README.md#dht_polling "Get temperature and humidity data from a DHT sensor (polling mode).")Get temperature and humidity data from a DHT sensor (polling mode).
- [Grove Light Sensor](../../../samples/sensor/grove_light/README.md#grove_light "Get illuminance data from a Grove Light Sensor.")Get illuminance data from a Grove Light Sensor.
- [Grove Temperature Sensor](../../../samples/sensor/grove_temperature/README.md#grove_temperature "Get temperature data from a Grove temperature sensor and display it on an LCD display.")Get temperature data from a Grove temperature sensor and display it on an LCD display.
- [GROW R502-A Fingerprint Sensor](../../../samples/sensor/grow_r502a/README.md#grow_r502a "Store and match fingerprints using the GROW R502-A fingerprint sensor.")Store and match fingerprints using the GROW R502-A fingerprint sensor.
- [HTS221 Temperature and Humidity Monitor](../../../samples/sensor/hts221/README.md#hts221 "Get temperature and humidity data from an HTS221 sensor (polling & trigger mode).")Get temperature and humidity data from an HTS221 sensor (polling & trigger mode).
- [I3G4250D 3-axis gyroscope sensor](../../../samples/sensor/i3g4250d/README.md#i3g4250d "Get gyroscope data from an I3G4250D sensor.")Get gyroscope data from an I3G4250D sensor.
- [INA219 Bidirectional Power/Current Monitor](../../../samples/sensor/ina219/README.md#ina219 "Get shunt voltage, bus voltage, power and current from an INA219 sensor.")Get shunt voltage, bus voltage, power and current from an INA219 sensor.
- [ISL29035 Digital Light Sensor](../../../samples/sensor/isl29035/README.md#isl29035 "Get light intensity data from an ISL29035 sensor (polling & trigger mode).")Get light intensity data from an ISL29035 sensor (polling & trigger mode).
- [JEDEC JC 42.4 compliant Temperature Sensor](../../../samples/sensor/jc42/README.md#jc42 "Get ambient temperature from a JEDEC JC 42.4 compliant temperature sensor (polling & trigger mode).")Get ambient temperature from a JEDEC JC 42.4 compliant temperature sensor (polling & trigger
  mode).
- [LIS2DH Motion Sensor](../../../samples/sensor/lis2dh/README.md#lis2dh "Get accelerometer data from an LIS2DH sensor (polling & trigger mode).")Get accelerometer data from an LIS2DH sensor (polling & trigger mode).
- [LPS22HB Temperature and Pressure Sensor](../../../samples/sensor/lps22hb/README.md#lps22hb "Get pressure and temperature data from an LPS22HB sensor (polling mode).")Get pressure and temperature data from an LPS22HB sensor (polling mode).
- [LPSS22HH Temperature and Pressure Sensor](../../../samples/sensor/lps22hh/README.md#lps22hh "Get pressure and temperature data from an LPS22HH sensor (polling & trigger mode).")Get pressure and temperature data from an LPS22HH sensor (polling & trigger mode).
- [LPSS22HH Temperature and Pressure Sensor (I3C)](../../../samples/sensor/lps22hh_i3c/README.md#lps22hh_i3c "Get pressure and temperature data from an LPS22HH sensor over I3C (polling & trigger mode).")Get pressure and temperature data from an LPS22HH sensor over I3C (polling &
  trigger mode).
- [LSM303DLHC Magnetometer and Accelerometer sensor](../../../samples/sensor/lsm303dlhc/README.md#lsmd303dlhc "Get magnetometer and accelerometer data from an LSM303DLHC sensor (polling mode).")Get magnetometer and accelerometer data from an LSM303DLHC sensor (polling
  mode).
- [LSM6DSL IMU sensor](../../../samples/sensor/lsm6dsl/README.md#lsmd6dsl "Get accelerometer and gyroscope data from an LSM6DSL sensor (polling & trigger mode).")Get accelerometer and gyroscope data from an LSM6DSL sensor (polling & trigger
  mode).
- [LSM6DSO IMU sensor](../../../samples/sensor/lsm6dso/README.md#lsmd6dso "Get accelerometer and gyroscope data from an LSM6DSO sensor (polling & trigger mode).")Get accelerometer and gyroscope data from an LSM6DSO sensor (polling & trigger
  mode).
- [LSM6DSO IMU sensor (I2C on I3C bus)](../../../samples/sensor/lsm6dso_i2c_on_i3c/README.md#lsmd6dso_i2c_on_i3c "Get accelerometer and gyroscope data from an LSM6DSO sensor using I2C on I3C bus (polling & trigger mode).")Get accelerometer and gyroscope data from an LSM6DSO sensor using I2C on I3C
  bus (polling & trigger mode).
- [LVGL line chart with accelerometer data](../../../samples/modules/lvgl/accelerometer_chart/README.md#lvgl-accelerometer-chart "Display acceleration data on a real-time chart using LVGL.")Display acceleration data on a real-time chart using LVGL.
- [Magnetometer Sensor](../../../samples/sensor/magn_polling/README.md#magn_polling "Get magnetometer data from a magnetometer sensor (polling mode).")Get magnetometer data from a magnetometer sensor (polling mode).
- [MAX17262 Fuel Gauge Sensor](../../../samples/sensor/max17262/README.md#max17262 "Get voltage, current and temperature data from a MAX17262 sensor (polling mode).")Get voltage, current and temperature data from a MAX17262 sensor (polling mode).
- [MAX30101 Heart Rate Sensor](../../../samples/sensor/max30101/README.md#max30101 "Get heart rate data from a MAX30101 sensor (polling mode).")Get heart rate data from a MAX30101 sensor (polling mode).
- [MAX6675 K-thermocouple to digital converter](../../../samples/sensor/max6675/README.md#max6675 "Get temperature from a MAX6675 K-thermocouple to digital converter (polling mode).")Get temperature from a MAX6675 K-thermocouple to digital converter (polling
  mode).
- [MPR Pressure Sensor](../../../samples/sensor/mpr/README.md#mpr "Get atmospheric pressure data from an MPR pressure sensor.")Get atmospheric pressure data from an MPR pressure sensor.
- [MPU6050 Invensense Motion Tracking Device](../../../samples/sensor/icm42605/README.md#icm42605 "Get temperature, acceleration, and angular velocity from an ICM42605 sensor (polling & trigger mode).")Get temperature, acceleration, and angular velocity from an ICM42605 sensor (polling & trigger
  mode).
- [MPU6050 motion tracking device](../../../samples/sensor/mpu6050/README.md#mpu6050 "Get temperature, acceleration, and angular velocity from an MPU6050 sensor (polling & trigger mode).")Get temperature, acceleration, and angular velocity from an MPU6050 sensor (polling & trigger
  mode).
- [MS5837 Digital Pressure Sensor](../../../samples/sensor/ms5837/README.md#ms5837 "Get pressure and temperature data from an MS5837 sensor (polling mode).")Get pressure and temperature data from an MS5837 sensor (polling mode).
- [NPCX ADC Comparator](../../../samples/sensor/adc_cmp_npcx/README.md#adc_cmp_npcx "Detect upper/lower voltage limits using NPCX ADC Comparator driver.")Detect upper/lower voltage limits using NPCX ADC Comparator driver.
- [NXP MCUX Analog Comparator (ACMP)](../../../samples/sensor/mcux_acmp/README.md#mcux_acmp "Get analog comparator data from an NXP MCUX Analog Comparator (ACMP).")Get analog comparator data from an NXP MCUX Analog Comparator (ACMP).
- [NXP MCUX Low-power Analog Comparator (LPCMP)](../../../samples/sensor/mcux_lpcmp/README.md#mcux_lpcmp "Get analog comparator data from an NXP MCUX Low-power Analog Comparator (LPCMP).")Get analog comparator data from an NXP MCUX Low-power Analog Comparator (LPCMP).
- [Proximity sensor](../../../samples/sensor/proximity_polling/README.md#proximity_polling "Get proximity data from up to 10 proximity sensors (polling mode).")Get proximity data from up to 10 proximity sensors (polling mode).
- [Quadrature Decoder Sensor](../../../samples/sensor/qdec/README.md#qdec "Get rotation data from a quadrature decoder sensor.")Get rotation data from a quadrature decoder sensor.
- [Secure MQTT Sensor/Actuator](../../../samples/net/secure_mqtt_sensor_actuator/README.md#secure-mqtt-sensor-actuator "Implement an MQTT-based IoT sensor/actuator device")Implement an MQTT-based IoT sensor/actuator device
- [Sensor shell](../../../samples/sensor/sensor_shell/README.md#sensor_shell "Interact with sensors using the shell module.")Interact with sensors using the shell module.
- [SGP40 and SHT4X digital humidity and multipixel gas sensor](../../../samples/sensor/sgp40_sht4x/README.md#sgp40_sht4x "Get temperature, humidity and gas sensor data from SGP40 and SHT4X sensors (polling mode).")Get temperature, humidity and gas sensor data from SGP40 and SHT4X sensors (polling mode).
- [SHT3XD humidity sensor](../../../samples/sensor/sht3xd/README.md#sht3xd "Get temperature and humidity from a SHT3XD sensor (polling & trigger mode).")Get temperature and humidity from a SHT3XD sensor (polling & trigger mode).
- [SM351LT Magnetoresistive Sensor](../../../samples/sensor/sm351lt/README.md#sm351lt "Detect a magnet's presence using the SM351LT magnetoresistive sensor (polling & trigger mode).")Detect a magnet's presence using the SM351LT magnetoresistive sensor (polling & trigger mode).
- [SoC Voltage Sensor](../../../samples/sensor/soc_voltage/README.md#soc_voltage "Get voltage data from an SoC's voltage sensor(s).")Get voltage data from an SoC's voltage sensor(s).
- [TH02 Temperature and Humidity Sensor](../../../samples/sensor/th02/README.md#th02 "Get temperature and humidity data from a TH02 sensor (polling mode).")Get temperature and humidity data from a TH02 sensor (polling mode).
- [Thermometer](../../../samples/sensor/thermometer/README.md#thermometer "Get ambient temperature data from a temperature sensor and get alerts when temperature drifts above a threshold. (polling & trigger mode).")Get ambient temperature data from a temperature sensor and get alerts when temperature drifts
  above a threshold. (polling & trigger mode).
- [TMP108 Temperature Sensor](../../../samples/sensor/tmp108/README.md#tmp108 "Get temperature data from a TMP108 sensor (polling & trigger mode).")Get temperature data from a TMP108 sensor (polling & trigger mode).
- [TMP112 Temperature Sensor](../../../samples/sensor/tmp112/README.md#tmp112 "Get temperature data from a TMP112 sensor (polling & trigger mode).")Get temperature data from a TMP112 sensor (polling & trigger mode).
- [VCNL4040 Proximity and Ambient Light Sensor](../../../samples/sensor/vcnl4040/README.md#vcml4040 "Get proximity and ambient light data from a VCNL4040 sensor (polling & trigger mode).")Get proximity and ambient light data from a VCNL4040 sensor (polling & trigger mode).
- [VEAA-X-3 proportional pressure control valve](../../../samples/sensor/veaa_x_3/README.md#veea_x_3 "Control a VEAA-X-3 proportional pressure control valve.")Control a VEAA-X-3 proportional pressure control valve.
- [VL53L0X Time Of Flight sensor](../../../samples/sensor/vl53l0x/README.md#vl53l0x "Get distance data from a VL53L0X sensor (polling mode).")Get distance data from a VL53L0X sensor (polling mode).
- [X-NUCLEO-53L0A1 shield](../../../samples/shields/x_nucleo_53l0a1/README.md#x-nucleo-53l0a1 "Interact with the 7-segment display and VL53L0X ranging sensor of an X-NUCLEO-53L0A1 shield.")Interact with the 7-segment display and VL53L0X ranging sensor of an X-NUCLEO-53L0A1 shield.
- [X-NUCLEO-IKS01A1 shield](../../../samples/shields/x_nucleo_iks01a1/README.md#x-nucleo-iks01a1 "Interact with all the sensors of an X-NUCLEO-IKS01A1 shield.")Interact with all the sensors of an X-NUCLEO-IKS01A1 shield.
- [X-NUCLEO-IKS01A2 shield - SensorHub (Mode 2)](../../../samples/shields/x_nucleo_iks01a2/sensorhub/README.md#x-nucleo-iks01a2-shub "Interact with all the sensors of an X-NUCLEO-IKS01A2 shield using Sensor Hub mode.")Interact with all the sensors of an X-NUCLEO-IKS01A2 shield using Sensor Hub mode.
- [X-NUCLEO-IKS01A2 shield - Standard (Mode 1)](../../../samples/shields/x_nucleo_iks01a2/standard/README.md#x-nucleo-iks01a2-std "Interact with all the sensors of an X-NUCLEO-IKS01A2 shield using Standard Mode.")Interact with all the sensors of an X-NUCLEO-IKS01A2 shield using Standard Mode.
- [X-NUCLEO-IKS01A3 shield - SensorHub (Mode 2)](../../../samples/shields/x_nucleo_iks01a3/sensorhub/README.md#x-nucleo-iks01a3-shub "Interact with all the sensors of an X-NUCLEO-IKS01A3 shield using Sensor Hub mode.")Interact with all the sensors of an X-NUCLEO-IKS01A3 shield using Sensor Hub mode.
- [X-NUCLEO-IKS01A3 shield - Standard (Mode 1)](../../../samples/shields/x_nucleo_iks01a3/standard/README.md#x-nucleo-iks01a3-std "Interact with all the sensors of an X-NUCLEO-IKS01A3 shield using Standard mode.")Interact with all the sensors of an X-NUCLEO-IKS01A3 shield using Standard mode.
- [X-NUCLEO-IKS02A1 shield - SensorHub (Mode 2)](../../../samples/shields/x_nucleo_iks02a1/sensorhub/README.md#x-nucleo-iks02a1-shub "Interact with all the sensors of an X-NUCLEO-IKS02A1 shield using Sensor Hub mode.")Interact with all the sensors of an X-NUCLEO-IKS02A1 shield using Sensor Hub mode.
- [X-NUCLEO-IKS02A1 shield - Standard (Mode 1)](../../../samples/shields/x_nucleo_iks02a1/standard/README.md#x-nucleo-iks02a1-std "Interact with all the sensors of an X-NUCLEO-IKS02A1 shield using Standard mode.")Interact with all the sensors of an X-NUCLEO-IKS02A1 shield using Standard mode.

[Sensor emulator backend API](../../../doxygen/html/group__sensor__emulator__backend.md)
