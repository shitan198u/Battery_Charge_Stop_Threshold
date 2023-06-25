import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSpinBox, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt


class BatteryChargeThresholdApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Battery Charge Threshold")
        self.setWindowFlag(Qt.WindowStaysOnTopHint)  # Set the window to stay on top
        self.setFixedSize(300, 150)
        # self.setGeometry(300, 300, 150, 150)
        
        self.label = QLabel("Set Battery Charge Threshold (%):")
        self.spinBox = QSpinBox()
        self.spinBox.setRange(20, 100)
        self.spinBox.setValue(80)  # Default value of 80%
        self.button = QPushButton("Set Threshold")
        self.button.clicked.connect(self.set_threshold)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.spinBox)
        layout.addWidget(self.button)
        self.setLayout(layout)
        
    def set_threshold(self):
        new_threshold = self.spinBox.value()
        
        try:
            subprocess.run(["pkexec", "bash", "-c", "/home/shsrra/CODE/GUI/Battery_Charge/modify_threshold.sh {}".format(new_threshold)], check=True)
        except subprocess.CalledProcessError:
            QMessageBox.critical(self, "Error", "Failed to set battery charge threshold.")
        else:
            QMessageBox.information(self, "Success", f"Battery charge threshold set to {new_threshold}%.")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = BatteryChargeThresholdApp()
    window.show()

    sys.exit(app.exec_())
