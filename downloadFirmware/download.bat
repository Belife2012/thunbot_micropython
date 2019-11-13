python esptool.py --chip esp32 --port COM13 --baud 921600 erase_flash
python esptool.py --chip esp32 --port COM13  --baud 921600 write_flash -z 0x1000 ./firmware.bin