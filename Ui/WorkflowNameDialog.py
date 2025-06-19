from PyQt5.QtWidgets import QDialog, QLineEdit, QDialogButtonBox, QFormLayout


class WorkflowNameDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Choose a name for your workflow")
        self.resize(350, 200)
        self._name = QLineEdit(self)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        layout = QFormLayout()
        layout.addRow('Name', self._name)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

    def get_input_name(self):
        print(self._name.text())
        return self._name.text()