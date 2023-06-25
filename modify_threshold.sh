#!/bin/bash

# Check if the script is being run with root privileges
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# Check if the input argument is within an acceptable range
if [ "$1" -lt 20 ] || [ "$1" -gt 100 ]
  then echo "Invalid input: threshold must be between 20 and 100"
  exit
fi

# Get the name of the battery by running the ls command
battery_name=$(ls /sys/class/power_supply | grep '^BAT')

# Check if the charge_control_end_threshold file exists
if [ ! -f "/sys/class/power_supply/$battery_name/charge_control_end_threshold" ]; then
    echo "Error: charge_control_end_threshold file not found"
    exit 1
fi

# Check if the battery-charge-threshold.service file exists
if [ ! -f "/etc/systemd/system/battery-charge-threshold.service" ]; then
    # Create the battery-charge-threshold.service file
    cat > /etc/systemd/system/battery-charge-threshold.service << EOF
[Unit]
Description=Set the battery charge threshold
After=multi-user.target

StartLimitBurst=0

[Service]
Type=oneshot
Restart=on-failure

ExecStart=/bin/bash -c 'echo 80 > /sys/class/power_supply/$battery_name/charge_control_end_threshold'

[Install]
WantedBy=multi-user.target
EOF

    # Enable and start the battery-charge-threshold service
    systemctl enable battery-charge-threshold.service
    systemctl start battery-charge-threshold.service
fi

# Get the current threshold value
current_threshold=$(cat /sys/class/power_supply/$battery_name/charge_control_end_threshold)
new_threshold=$1

# Update the battery-charge-threshold.service file with the new threshold value
sed -i "s/$current_threshold/$new_threshold/g" /etc/systemd/system/battery-charge-threshold.service

# Reload the systemd daemon and restart the battery-charge-threshold service
systemctl daemon-reload
systemctl restart battery-charge-threshold.service
