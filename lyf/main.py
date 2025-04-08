#
# from PyQt5 import QtCore, QtGui, QtWidgets
# import lyf
# import sys
# from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox
# import pandas as pd
#
#
# class T(lyf.Ui_MainWindow, QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#
#         self.csv.clicked.connect(self.opencsv)
#         self.xlsx.clicked.connect(self.openxlsx)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "林怡凡"))
#         self.gini.setText(_translate("MainWindow", "gini"))
#         self.entopy.setText(_translate("MainWindow", "entopy"))
#         self.csv.setText(_translate("MainWindow", "输入数据 CSV文件"))
#         self.xlsx.setText(_translate("MainWindow", "输入数据 xlsx文件"))
#
#     def opencsv(self):
#         openfile_name, _ = QFileDialog.getOpenFileName(
#             self, '选择文件', '', 'CSV files (*.csv)')
#         if openfile_name:
#             self.display_data(openfile_name, is_csv=True)
#
#     def openxlsx(self):
#         openfile_name, _ = QFileDialog.getOpenFileName(
#             self, '选择文件', '', 'Excel files (*.xlsx *.xls)')
#         if openfile_name:
#             self.display_data(openfile_name, is_csv=False)
#
#     def display_data(self, file_path, is_csv=True):
#         """显示数据到tableWidget"""
#         try:
#             # 读取数据
#             if is_csv:
#                 df = pd.read_csv(file_path)
#             else:
#                 df = pd.read_excel(file_path)
#
#             # 设置表格行数和列数
#             self.tableWidget.setRowCount(df.shape[0])
#             self.tableWidget.setColumnCount(df.shape[1])
#
#             # 设置表头
#             self.tableWidget.setHorizontalHeaderLabels(df.columns)
#
#             # 填充数据
#             for row in range(df.shape[0]):
#                 for col in range(df.shape[1]):
#                     self.tableWidget.setItem(
#                         row, col, QTableWidgetItem(str(df.iloc[row, col]))
#                     )
#
#             # 自动调整列宽
#             self.tableWidget.resizeColumnsToContents()
#
#         except Exception as e:
#             QMessageBox.critical(self, "错误", f"加载文件失败:\n{e}")
#
#
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     win = T()
#     win.show()
#     sys.exit(app.exec_())
#



from PyQt5 import QtCore, QtGui, QtWidgets
import lyf
import sys
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox
import pandas as pd


class T(lyf.Ui_MainWindow ,QtWidgets.QMainWindow) :

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.csv.clicked.connect(self.opencsv)
        self.xlsx.clicked.connect(self.openxlsx)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "林怡凡"))
        self.gini.setText(_translate("MainWindow", "gini"))
        self.entopy.setText(_translate("MainWindow", "entopy"))
        self.csv.setText(_translate("MainWindow", "输入数据 CSV文件"))
        self.xlsx.setText(_translate("MainWindow", "输入数据 xlsx文件"))

    def opencsv(self):
        print(000)
        openfile_name, _ = QFileDialog.getOpenFileName(self, '选择文件', '', 'CSV files (*.csv)')
        print('success')
        if openfile_name :
            print('success')
            self.display_data(openfile_name,is_csv=True)
            print('success')



    def openxlsx(self) :
        openfile_name,_ = QtWidgets.QFileDialog.getOpenFileName(None, '选择文件', '', 'Excel files(*.xlsx , *.xls)')
        if openfile_name :
            self.display_data(openfile_name,is_csv=False)
            # self.load_xlsx_to_table(self,openfile_name)

    def display_data(self, file_path, is_csv=True):
        """显示数据到tableWidget"""
        print(file_path)
        try:
            print(file_path)
            # 读取数据
            if is_csv:
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path)
            print('display')
            # 设置表格行数和列数
            self.tableWidget.setRowCount(df.shape[0])
            self.tableWidget.setColumnCount(df.shape[1])

            # 设置表头
            self.tableWidget.setHorizontalHeaderLabels(df.columns)

            # 填充数据
            for row in range(df.shape[0]):
                for col in range(df.shape[1]):
                    self.tableWidget.setItem(
                        row, col, QTableWidgetItem(str(df.iloc[row, col]))
                    )

            # 自动调整列宽
            self.tableWidget.resizeColumnsToContents()

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "错误", f"加载文件失败:\n{e}")


if __name__ == '__main__' :

    app = QtWidgets.QApplication(sys.argv)
    win = T()
    win.show()
    sys.exit(app.exec())