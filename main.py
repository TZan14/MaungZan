from counter_form import Ui_Counter
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from sys import argv
from datetime import datetime
from time import sleep


class MainApp(QtWidgets.QWidget, Ui_Counter):
    def __init__(self):
        super().__init__()
        self.WindowSetup() #Function for window setup
        self.Widgets()
        self.show()

    def WindowSetup(self): #Function for window setup
        self.setupUi(self) #Load UI pass through MainApp
        self.setFixedSize(400, 320) #Set Fixed Size to 400 Px Width and 320 Px Height
        self.num = 0 #Initial num value as 0

    def Widgets(self): #Function for widgets
        self.increase.clicked.connect(self.increase_count) #Increase Button
        self.decrease.clicked.connect(self.decrease_count) #Decrease Button
        self.exit.clicked.connect(self.close) #Exit Button

        timer = QtCore.QTimer(self) #Timer for counting and updating 
        timer.timeout.connect(self.update_time) #Timer connected with label
        timer.start(1000) # Timer start for refresh and update data in every 1 sec

    def increase_count(self): #Function for increase button 
        self.num = self.num+1 # If increase button pressed, num is added by 1
        self.lcd.display(self.num) #Show the num value in lcd display

    def decrease_count(self): #Function for decrease button
        self.num = self.num-1 #If decrease button pressed, num is substracted by 1
        self.lcd.display(self.num) #Show the num value in lcd display

        if self.num <= -1: #If num is <= 1, 
            self.lcd.display(0) #Lcd display is set to 0
            self.num = 0 # Num is set to 0 (Which means tally is not counted negative values)

    def update_time(self): #For updating the label
        DateTime = datetime.now() #Get the date time value
        self.label_2.setText('{} ({})'.format(DateTime.strftime('%x'), DateTime.strftime('%X'))) #Show the date time value on lable

#Run and execute the app 
if __name__ == '__main__':
    app = QtWidgets.QApplication(argv) #App pass through system argv
    window = MainApp() #Recall for MainApp
    app.exec_() #Execute the app
        