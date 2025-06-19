from PyQt5.QtWidgets import QDialog, QLineEdit, QDialogButtonBox, QTextEdit, QFormLayout, QApplication, QVBoxLayout


class InfoInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit the information")
        self.resize(350, 200)
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Name of the node")
        self.description = QLineEdit(self)
        self.description.setPlaceholderText("Description of the node")
        self.code_py = QLineEdit(self) #TODO should be a box with multiple lines and later returns a list
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.layout = QFormLayout()
        self.layout.addRow('Name', self.name)
        self.layout.addRow('Description', self.description)
        self.layout.addRow('Code python', self.code_py)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def get_input_name(self):
        print(self.name.text())
        return self.name.text()
    def get_input_description(self):
        print(self.description.text())
        return self.description.text()
    def get_input_code_py(self)-> list:
        code_py = self.code_py.text().split('\n')
        for line in code_py:
            print(line)
        return code_py





