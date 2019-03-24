[Unit]
Description=Button Shutdown Service
After=network.target auditd.service

[Service]
Type=idle
ExecStart=/home/pi/projects/rpi_shutdown_button/rpi_shutdown_button.py
ExecReload=/bin/kill -9 $MAINPID
ExecStop=/bin/kill -9 $MAINPID
KillMode=process
Restart=on-failure
User=pi

[Install]
WantedBy=multi-user.target