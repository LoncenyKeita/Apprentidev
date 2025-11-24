import sys
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*

class MainWindow(QMainWindow):
	#Permet d'afficher open
	
	def openFile(self):
		print()
		self.statusBar().showMessage("openFile() exécuté")


	def saveFile(self):
		print()
		self.statusBar().showMessage("openFile() exécuté")


	def __init__(self):
		super().__init__() #Appel au constructeur parent
		self.setWindowTitle("Editeur de texte")
# ----------------------Zone centrale---------
		self.textEdit = QTextEdit(self)
		sel
# Etape: rajouter des widgets à MainWindow
		bar = self.menuBar()
		fileMenu = bar.addMenu("File")
		fileMenu = bar.addMenu("Edit")

		self.actionOpen = QAction(QIcon("new.png"), "Open...", self)
		self.actionOpen.setShortcut("Ctrl+N")
		self.actionOpen.setToolTip(self.tr("Open"))
		self.actionOpen.setStatusTip(self.tr("Open"))

		self.actionSave = QAction(QIcon("save.png"), "Save...", self)
		self.actionSave.setShortcut("Ctrl+S")
		self.actionSave.setToolTip(self.tr("Save"))
		self.actionSave.setStatusTip(self.tr("Save"))

		self.actionCopy = QAction(QIcon("copy.png"), "Copy...", self)
		self.actionCopy.setShortcut("Ctrl+C")
		self.actionCopy.setToolTip(self.tr("Copy"))
		self.actionCopy.setStatusTip(self.tr("Copy"))

		self.actionQuit = QAction(QIcon("quit.png"), "Quit...", self)
		self.actionQuit.setShortcut("Ctrl+Q")
		self.actionQuit.setToolTip(self.tr("Quit"))
		self.actionQuit.setStatusTip(self.tr("Quit"))

#-------------Ajouter des actions au menu-----------------
		fileMenu.addAction(self.actionOpen)

		fileMenu.addAction(self.actionSave)
		
		fileMenu.addAction(self.actionCopy)
	

		fileMenu.addAction(self.actionQuit)
#------------- Barre d'outils---------------------

		fileToolBar = QToolBar("File")
		self.addToolBar(fileToolBar)
		fileToolBar.addAction(self.actionOpen)
		fileToolBar.addAction(self.actionSave)
		fileToolBar.addAction(self.actionCopy)
		fileToolBar.addAction(self.actionQuit)

		#newAct.setEnabled(False)

		#self.textEdit = QTextEdit(self)
		#self.setCentralWidget(self.textEdit)
#-------------Pied de page---------------------------
		self.statusBar().showMessage("")
		#self.createAction()
		#self.createMenus()
		#self.createToolBars()

# 2e Etape: Créer une classe MainWindow
def main(args):
	app = QApplication(args)
	mainWindow = MainWindow()
	mainWindow.resize(400, 400)
	mainWindow.show()

	app.exec_()

if __name__ == "__main__":
	main(sys.argv)
#--------------------------------

			
	