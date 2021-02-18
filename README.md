# Meowality - CrossLink NX mixed reality

(early WIP - outline ideas)

Per eye:
 - H381DLN01.0 or equivalent 1080x1200x90fps AMOLED
 - iMX477 camera using the 4-lane 22-pin Pi connector (should be 1080p120+ capable)
 - LIFCL-40-9BG400C FPGA
 - ICM-20948 IMU
 - QSPI boot flash
 - 2 user buttons
 - 6 RGB LEDs and connector for RGB cat ear extension
 - PMOD for debug/extension

M.2 slot for WiFi module using CrossLink NX for hypothetical wireless VR with minimal stack (raw packets and minimal DPCM type compression only).

Debug/IO board at side:
 - Allwinner F1C200S (ARM9, embedded 64MB DDR, basic video encode/decode)
 - USB type-C with USB2 and CVBS video in over SBU. USB PD support for max power.
 - microSD card for bitstreams/firmware
 - SDIO WiFi module for untethered bitstream loading
 - LVDS video interface into left FPGA board (720p max, intended for overlay)
 - RTOS/minimal Linux??