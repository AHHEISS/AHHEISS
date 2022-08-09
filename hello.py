import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #Add a title
        self.setWindowTitle("Hello World!!")

        # Set Vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # Create a label
        my_label = qtw.QLabel("Hello World! What's your name?")
        # Change the font size of label
        my_label.setFont(qtg.QFont('Helvetica', 18))

        self.layout().addWidget(my_label)

        # Create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("placeholder")
        self.layout().addWidget(my_entry)
        
        self.show()


app = qtw.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()
