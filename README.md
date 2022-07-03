# OpenAMS Firmware

## Copying the repository
To copy the repository to the Raspberry Pi, open the terminal in desired location and run:
```
git clone https://github.com/OpenAMS-SUT/Firmware.git
```
## Running on startup
To run the OpenAMS web server on startup follow these steps.
1. Change `ExecStart` line in the `openams.service` file to reflect your `server.py` location:
    ```
    [Service]
    ExecStart=/usr/bin/python3 /home/pi/Desktop/Firmware/server.py
    ```
1. Move the `openams.service` file to `/lib/systemd/system/` directory:
    ```
    sudo mv openams.service /lib/systemd/system
    ```
1. Run these commands:
    ```
    sudo systemctl daemon-reload
    sudo systemctl enable openams.service
    ```
The OpenAMS web server will now run at startup.
To check status of the service, run:
```
systemctl status openams.service
```
