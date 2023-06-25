#!/bin/bash

current_threshold=$(cat /sys/class/power_supply/BAT0/charge_control_end_threshold)
new_threshold=$1
sed -i "s/$current_threshold/$new_threshold/g" /etc/systemd/system/battery-charge-threshold.service
# systemctl stop battery-charge-threshold.service
# systemctl disable battery-charge-threshold.service
# systemctl daemon-reload
# systemctl enable battery-charge-threshold.service
# systemctl start battery-charge-threshold.service
systemctl daemon-reload
systemctl restart battery-charge-threshold.service