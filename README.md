# Raspberry Pi Shutdown Button

**Push to shut Raspberry Pi down ...**

![Push Button](https://static.thenounproject.com/png/509859-200.png)

---

SICHTEN: 

http://razzpisampler.oreilly.com/ch07.html

https://www.raspberrypi.org/forums/viewtopic.php?t=133665

https://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up

Service à la https://github.com/workinghard/jslisten

https://maker-tutorials.com/raspberry-pi-mit-einer-bueroklammer-ausschalten-bzw-herunterfahren/

---
Place script in `/home/pi/projects/rpi_shutdown_button/rpi_shutdown_button.py`

Start at Raspbian Startup by putting shutdown-button.service in /etc/systemd/system,
then enable with `systemctl enable shutdown-button.service`

---

Pins 18 and GND - short them to force shutdown ...

---
Raspberry Pi 1
![Pinout](http://razzpisampler.oreilly.com/images/rpck_1101.png)

---

Raspberry Pi 2/3
![Pinout 2](https://www.jameco.com/Jameco/workshop/circuitnotes/raspberry_pi_circuit_note_fig2.jpg)
