from PyQt5.QtWidgets import QDialog, QInputDialog, QComboBox

from Ui.InfoInputDialog import InfoInputDialog


class InfoInputDialogQuestion(InfoInputDialog):
    def __init__(self, parent=None):
        super(InfoInputDialogQuestion, self).__init__(parent)
        # Create the combo box for first arrow label
        self.first_arrow_label_combo = QComboBox()
        self.second_arrow_label_combo = QComboBox()
        self.layout.removeWidget(self.buttonBox)
        self.first_arrow_label_combo.addItems(["True", "False"])
        self.second_arrow_label_combo.addItems(["True", "False"])
        self.layout.addRow("Label for first arrow", self.first_arrow_label_combo)
        self.layout.addRow("Label for second arrow", self.second_arrow_label_combo)
        self.layout.addWidget(self.buttonBox)

    def get_first_arrow_label(self):
        return self.first_arrow_label_combo.currentText()

    def get_second_arrow_label(self):
        return self.second_arrow_label_combo.currentText()
