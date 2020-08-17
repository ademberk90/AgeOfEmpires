from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from main_design_python import Ui_MainWindow
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtChart import QChartView,QBarSet,QBarCategoryAxis,QBarSeries,QChart,QValueAxis,QLineSeries
import requests

class mainApp(QMainWindow):

    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #initial value
        self.file = None
        self.players=dict()
        self.counter = 0

        """Signal connections"""
        #open file chooser
        self.ui.pushButton_choose.clicked.connect(self.openDialogBox)
        #download file from url
        self.ui.pushButton_download.clicked.connect(self.downloadFromUrl)
        #after choosing file, go results page
        self.ui.pushButton_start.clicked.connect(self.changePage)
        #replay game with timer
        self.ui.pushButton_x.clicked.connect(partial(self.updateGraph,1000))
        self.ui.pushButton_2x.clicked.connect(partial(self.updateGraph, 1000/2))
        self.ui.pushButton_4x.clicked.connect(partial(self.updateGraph, 1000/4))
        self.ui.pushButton_16x.clicked.connect(partial(self.updateGraph, 1000/16))
        #stop animation
        self.ui.pushButton_stop.clicked.connect(self.stopUpdateGraph)

    def openDialogBox(self):
        filter = "Text files (*.txt)"
        filename = QFileDialog.getOpenFileName(self, filter=filter, initialFilter=filter)
        self.file = filename[0]
        if self.file:
            self.prepareInformations()
        else:
            print("Problem file")

    def downloadFromUrl(self):
        r = requests.get('http://operations.sparsetechnology.com/public/users/yca/aotstats.txt', allow_redirects=True)
        file = open('data.txt', 'wb')
        file.write(r.content)
        file.close()
        file = open('data.txt',"r")
        lines = file.readlines()
        del lines[-1]
        open('data.txt',"w").writelines(lines)
        self.file = "data.txt"
        self.prepareInformations()
    def prepareInformations(self):
        file = open(self.file,'r')
        #split each line
        self.lines = [line.split(',') for line in file]
        degerler=[0,2,3,4,5,6,7]
        #convert strings to int in file
        for line in self.lines:
            try:
                for i in degerler:
                    line[i]= int(line[i])
            except:
                pass

        #calculate score and append the end of line
        for line in self.lines:
            if line[0] == "time":
                continue
            score = line[7]*75 + line[6] * 50 * 0.2 + (line[2]+line[3]+line[4]+line[5]) * 0.2
            score = round(score)
            line.append(score)
        #learn the number of player and time
        self.end_time=self.lines[-1][0]
        self.playerCount = int((len(self.lines)-1) / ((int(self.end_time)/100)+1))
        self.gecici = []
        for i in range(self.playerCount):
            for k in range(0,int((len(self.lines) - 1) / self.playerCount)):
                self.gecici.append(self.lines[k*self.playerCount+i+1])
            self.players[i] = self.gecici
            self.gecici=[]

        #set the results page interface
        self.setInformations()

    def setInformations(self):
        #add the values of food,wood,stone etc for every player
        for i in range(int(self.playerCount)):
            lineEdit1 = QLabel()
            lineEdit1.setText(self.players[i][-1][1])
            lineEdit1.setAlignment(Qt.AlignCenter)

            lineEdit2 = QLabel()
            lineEdit2.setText(str(self.players[i][-1][2]))
            lineEdit2.setAlignment(Qt.AlignCenter)

            lineEdit3 = QLabel()
            lineEdit3.setText(str(self.players[i][-1][3]))
            lineEdit3.setAlignment(Qt.AlignCenter)

            lineEdit4 = QLabel()
            lineEdit4.setText(str(self.players[i][-1][4]))
            lineEdit4.setAlignment(Qt.AlignCenter)

            lineEdit5 = QLabel()
            lineEdit5.setText(str(self.players[i][-1][5]))
            lineEdit5.setAlignment(Qt.AlignCenter)

            lineEdit6 = QLabel()
            lineEdit6.setText(str(self.players[i][-1][6]))
            lineEdit6.setAlignment(Qt.AlignCenter)

            lineEdit7 = QLabel()
            lineEdit7.setText(str(self.players[i][-1][7]))
            lineEdit7.setAlignment(Qt.AlignCenter)

            lineEdit8 = QLabel()
            lineEdit8.setText(str(self.players[i][-1][8]))
            lineEdit8.setAlignment(Qt.AlignCenter)

            self.hbox = QtWidgets.QHBoxLayout()
            self.hbox.setObjectName("hbox_{}".format(i))

            self.hbox.addWidget(lineEdit1)
            self.hbox.addWidget(lineEdit2)
            self.hbox.addWidget(lineEdit3)
            self.hbox.addWidget(lineEdit4)
            self.hbox.addWidget(lineEdit5)
            self.hbox.addWidget(lineEdit6)
            self.hbox.addWidget(lineEdit7)
            self.hbox.addWidget(lineEdit8)

            self.ui.verticalLayout_2.addLayout(self.hbox)
        #add the result graph
        self.series = QBarSeries()
        self.maxScore = 0
        for i in range(self.playerCount):
            set = QBarSet(self.players[i][0][1])
            set.append(self.players[i][-1][8])
            self.series.append(set)
            if set[0] > self.maxScore:
                self.maxScore = set[0]

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle("Percent Example")
        self.chart.setAnimationOptions(QChart.NoAnimation)

        categories = ["Score"]

        self.axisX = QBarCategoryAxis()
        self.axisX.append(categories)

        self.axisY = QValueAxis()
        self.axisY.setRange(0,self.maxScore)

        self.chart.addAxis(self.axisX,Qt.AlignBottom)
        self.chart.addAxis(self.axisY,Qt.AlignLeft)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chartView = QChartView(self.chart)

        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.ui.gridLayout_6.addWidget(self.chartView)

        self.ui.pushButton_start.setEnabled(True)

        #add the checkbox for every player due to replay game
        for i in range(self.playerCount):
            checkbox = QCheckBox(self.players[i][0][1])
            checkbox.setObjectName("checkBox_{}".format(i))
            self.ui.gridLayout_9.addWidget(checkbox)

    def updateGraph(self,time):

        #firstly remove the score in graph then set new graph
        self.chart.removeSeries(self.series)
        self.chart.removeAxis(self.axisX)
        self.chart.removeAxis(self.axisY)

        self.axisX = QBarCategoryAxis()
        categories = ["food", "wood", "gold", "stone", "villages", "military units"]
        self.axisX.append(categories)

        # self.axisY = QValueAxis()
        # self.axisY.setRange(0, 5)

        #self.chart.setAnimationOptions(QChart.NoAnimations)

        self.chart.addAxis(self.axisX, Qt.AlignBottom)
        # self.chart.addAxis(self.axisY, Qt.AlignLeft)

        #learn which checkbox is 2
        self.readyPlayer = []
        for i in range(self.playerCount):
            checkbox = self.findChild(QCheckBox, "checkBox_{}".format(i))
            if checkbox.checkState() == 2:
                self.readyPlayer.append(i)
        #if at least one checkbox is 2 start the timer for update graph

        if len(self.readyPlayer)>0:

            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.startReplay)
            self.timer.start(time)

    def startReplay(self):
        self.counter += 1

        self.series.clear()
        self.count = int(int(self.end_time)/100 + 1)
        for i in self.readyPlayer:
            print("----------------")
            set = QBarSet(self.players[i][0][1])
            for which in range(2,8):
                set.append(self.players[i][self.counter][which])
                print(self.players[i][self.counter][which])
            self.series.append(set)
        self.chart.addSeries(self.series)
        if self.counter == (self.count-1):
            self.timer.stop()
    def stopUpdateGraph(self):
        self.timer.stop()
    def changePage(self):
        if self.file:
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            QMessageBox.warning(self,"Warning", "Please choose or download file or something is wrong with your file")


if __name__ == '__main__':
    app = QApplication([])
    window = mainApp()
    window.show()
    app.exec_()