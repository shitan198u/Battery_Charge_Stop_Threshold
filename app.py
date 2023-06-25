import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSpinBox, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt


class BatteryChargeThresholdApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Battery Charge Threshold")
        self.setWindowFlag(Qt.WindowStaysOnTopHint)  # Set the window to stay on top
        self.setFixedSize(300, 150)

        # Create the label
        self.label = QLabel("Set Battery Charge Threshold (%):")

        # Create the spin box to set the threshold value
        self.spinBox = QSpinBox()
        self.spinBox.setRange(20, 100)  # Set the range from 20 to 100

        # Get the current threshold value and set it as the default value of the spin box
        current_threshold = self.get_current_threshold()
        if current_threshold:
            self.spinBox.setValue(current_threshold)
        else:
            self.spinBox.setValue(80)  # Default value of 80%

        # Create the button to set the threshold
        self.button = QPushButton("Set Threshold")
        self.button.clicked.connect(self.set_threshold)

        # Create the layout and add the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.spinBox)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def get_current_threshold(self):
        try:
            # Get the name of the battery by running the ls command
            battery_name = subprocess.check_output(["ls", "/sys/class/power_supply"]).decode().strip().split("\n")[-1]

            # Construct the path to the charge_control_end_threshold file using the battery name
            threshold_path = f"/sys/class/power_supply/{battery_name}/charge_control_end_threshold"

            # Read the current threshold value from the charge_control_end_threshold file
            with open(threshold_path, "r") as f:
                current_threshold = int(f.read().strip())
                return current_threshold

        except Exception as e:
            print(f"Error: {e}")
            return None

    def set_threshold(self):
        # Get the new threshold value from the spin box
        new_threshold = self.spinBox.value()

        try:
            # Get the present working directory
            current_directory = os.getcwd()
            
            # Construct the path to the shell script using the present working directory
            script_path = os.path.join(current_directory, "modify_threshold.sh")

            # Check if the shell script exists and is executable
            if not os.path.isfile(script_path) or not os.access(script_path, os.X_OK):
                raise Exception("Shell script not found or not executable")

            # Execute the shell script with pkexec and pass the new threshold value as an argument
            subprocess.run(["pkexec", "bash", "-c", "{} {}".format(script_path, new_threshold)], check=True)

        except Exception as e:
            # Display an error message if something goes wrong
            QMessageBox.critical(self, "Error", str(e))
        
        else:
            # Display a success message with the new threshold value
            QMessageBox.information(self, "Success", f"Battery charge threshold set to {new_threshold}%.")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = BatteryChargeThresholdApp()
    window.show()

    sys.exit(app.exec_())
