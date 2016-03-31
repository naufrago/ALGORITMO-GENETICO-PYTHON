# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'algoritmo.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
#coding: iso-8859-1
#*********algoritmos geneticos *********
#@uthor: NAUFRAGO(Yeison Aguirre Osorio )
#22 marzo 2016
#***************************************




import sys, re, random, ctypes
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5 import uic
from matplotlib import pyplot
import numpy as np


modelos=[]#Objetivo a alcanzar
# ND: Para una funcíon, calcular según formula
lInd =0  #La longitud del material genetico de cada individuo

tamano =0#La cantidad de individuos que habra en la poblacion

## ND: La diferenciua entre la población y los que cruzan
## ND: Determina los individuos que se mantiene por el elitismo
padres=0  #ND: Cuantos individuos se seleccionan para reproduccion. Necesariamente mayor que 2

# ND: Para este codigo no hay probabilidad de Cruce - Todos cruzan, menos definidos por elitismo
# ND: Definir como parametro, probCruce

probMutac=0  #La probabilidad de que un individuo mute  
## ND: esta muy alta
# Esta probabilidad se aplica por cromosoma.. error

detalles=[]#almacenara en cada iteracion todo lo sucedido en  la iteracion
x=[]
yy=[] # almacenara la sumatoria de todos los individuos en  la iteracion

class Ui_Dialog(object):
	

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(393, 583)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 10, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lind = QtWidgets.QLineEdit(Dialog)
        self.lind.setGeometry(QtCore.QRect(140, 100, 71, 20))
        self.lind.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.lind.setObjectName("lind")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 381, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.modelo = QtWidgets.QLineEdit(Dialog)
        self.modelo.setGeometry(QtCore.QRect(70, 150, 81, 20))
        self.modelo.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.modelo.setObjectName("modelo")
        self.asignar = QtWidgets.QPushButton(Dialog)
        self.asignar.setGeometry(QtCore.QRect(70, 170, 81, 23))
        self.asignar.setObjectName("asignar")
        self.tpoblacion = QtWidgets.QLineEdit(Dialog)
        self.tpoblacion.setEnabled(True)
        self.tpoblacion.setGeometry(QtCore.QRect(250, 210, 51, 20))
        self.tpoblacion.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.tpoblacion.setText("")
        self.tpoblacion.setObjectName("tpoblacion")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 210, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.npadres = QtWidgets.QLineEdit(Dialog)
        self.npadres.setGeometry(QtCore.QRect(250, 250, 51, 20))
        self.npadres.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.npadres.setText("")
        self.npadres.setObjectName("npadres")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 250, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pmutacion = QtWidgets.QLineEdit(Dialog)
        self.pmutacion.setGeometry(QtCore.QRect(250, 280, 51, 20))
        self.pmutacion.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.pmutacion.setText("")
        self.pmutacion.setObjectName("pmutacion")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 280, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.iteraciones = QtWidgets.QSpinBox(Dialog)
        self.iteraciones.setGeometry(QtCore.QRect(230, 390, 61, 22))
        self.iteraciones.setMaximum(20000)
        self.iteraciones.setObjectName("iteraciones")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(90, 390, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 320, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 340, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(90, 360, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.evaluar = QtWidgets.QPushButton(Dialog)
        self.evaluar.setGeometry(QtCore.QRect(90, 420, 211, 23))
        self.evaluar.setObjectName("evaluar")
        self.cmodelo = QtWidgets.QLabel(Dialog)
        self.cmodelo.setGeometry(QtCore.QRect(170, 150, 21, 16))
        self.cmodelo.setObjectName("cmodelo")
        self.m1 = QtWidgets.QLabel(Dialog)
        self.m1.setGeometry(QtCore.QRect(160, 170, 16, 16))
        self.m1.setObjectName("m1")
        self.mmodelo = QtWidgets.QLabel(Dialog)
        self.mmodelo.setGeometry(QtCore.QRect(170, 170, 191, 20))
        self.mmodelo.setText("")
        self.mmodelo.setObjectName("mmodelo")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(370, 170, 16, 16))
        self.label_12.setObjectName("label_12")
        self.solucion = QtWidgets.QTextEdit(Dialog)
        self.solucion.setEnabled(True)
        self.solucion.setGeometry(QtCore.QRect(10, 480, 371, 61))
        self.solucion.setObjectName("solucion")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 460, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.iter = QtWidgets.QPushButton(Dialog)
        self.iter.setEnabled(False)
        self.iter.setGeometry(QtCore.QRect(80, 550, 111, 23))
        self.iter.setObjectName("iter")
        self.dtallesiter = QtWidgets.QSpinBox(Dialog)
        self.dtallesiter.setEnabled(False)
        self.dtallesiter.setGeometry(QtCore.QRect(10, 550, 61, 22))
        self.dtallesiter.setMinimum(1)
        self.dtallesiter.setMaximum(10000)
        self.dtallesiter.setObjectName("dtallesiter")
        self.reiniciarr = QtWidgets.QPushButton(Dialog)
        self.reiniciarr.setGeometry(QtCore.QRect(254, 550, 101, 23))
        self.reiniciarr.setObjectName("reiniciarr")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(80, 70, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(240, 150, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.grafica = QtWidgets.QPushButton(Dialog)
        self.grafica.setGeometry(QtCore.QRect(200, 550, 51, 23))
        self.grafica.setObjectName("grafica")

        self.lind.textChanged.connect(self.validar_lind)
        self.modelo.textChanged.connect(self.validar_modelo)
        self.tpoblacion.textChanged.connect(self.validar_tpoblacion)
        self.npadres.textChanged.connect(self.validar_npadres)
        self.pmutacion.textChanged.connect(self.validar_pmutacion)
        self.asignar.clicked.connect(self.mostar_modelo)
        self.evaluar.clicked.connect(self.imprimir)
        self.reiniciarr.clicked.connect(self.reiniciar)
        self.iter.clicked.connect(self.val_detalles)
        self.grafica.clicked.connect(self.val_grafica)
		
		
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "EVALUACION ALGORITMO GENETICO"))
        self.label.setText(_translate("Dialog", "ALGORITMOS GENETICOS"))
        self.lind.setText(_translate("Dialog", "0"))
        self.label_2.setText(_translate("Dialog", "LIND: \"limite de bits que tendra cada individuo\""))
        self.label_3.setText(_translate("Dialog", "ELEMENTO DEL MODELO ALCANZAR NUMEROS ADMITIDOS DEL 0 AL 9"))
        self.asignar.setText(_translate("Dialog", "ASIGNAR"))
        self.label_4.setText(_translate("Dialog", "TAMAÑO DE POBLACIÓN : (>=5)"))
        self.label_5.setText(_translate("Dialog", "# DE PADRES A SELECCIONAR :  (>=3)"))
        self.label_6.setText(_translate("Dialog", "PROBABILIDAD DE MUTACIÓN: (%)"))
        self.label_7.setText(_translate("Dialog", "ITERACIONES DESEADAS"))
        self.label_8.setText(_translate("Dialog", "SELECCIONAR EL NUMERO DE ITERACIONES DESEADAS"))
        self.label_9.setText(_translate("Dialog", "PARA LA BUSQUEDA DEL MODELO, O DEJAR  EN CERO "))
        self.label_11.setText(_translate("Dialog", "PARA  ITERAR 10000 VECES."))
        self.evaluar.setText(_translate("Dialog", "EVALUAR "))
        self.cmodelo.setText(_translate("Dialog", "0"))
        self.m1.setText(_translate("Dialog", "[                         "))
        self.label_12.setText(_translate("Dialog", "]"))
        self.label_10.setText(_translate("Dialog", "SOLUCIÓN   HALLADA  SEGUN LAS ITERACIONES DADAS"))
        self.iter.setText(_translate("Dialog", "detalles de iteración"))
        self.reiniciarr.setText(_translate("Dialog", "reiniciar aplicación"))
        self.label_13.setText(_translate("Dialog", "recomendable minimo 3 bits."))
        self.label_14.setText(_translate("Dialog", "modelo"))
        self.grafica.setText(_translate("Dialog", "grafica"))


    def imprimir(self):
    	evaluar=True
    	mensaje=""
    	detalle1="****DATOS INICIALES DE EVALUACION****\n\n"
    	if self.lind.text()=="" or self.lind.text()== "0" :
    		self.lind.setStyleSheet("border: 2px solid red;")
    		evaluar =False
    		mensaje=mensaje+"*CAMPO LIND,\n"
    	if self.modelo.text()=="" or int(self.cmodelo.text())< int(self.lind.text()):
    		self.modelo.setStyleSheet("border: 2px solid red;")
    		evaluar =False
    		mensaje=mensaje+"*CAMPO MODELO vacio o falta un bit, \n"
    	if self.tpoblacion.text()=="" or int(self.tpoblacion.text())<5:
    		self.tpoblacion.setStyleSheet("border: 2px solid red;")
    		evaluar =False
    		mensaje=mensaje+"*CAMPO POBLACION vacio o es un numero < 5, \n"
    	if self.npadres.text()=="" or int(self.npadres.text())<=2 or int(self.npadres.text())>=int(self.tpoblacion.text()) :
    		self.npadres.setStyleSheet("border: 2px solid red;")
    		evaluar =False
    		mensaje=mensaje+"*CAMPO #DE PADRES vacio o es un numero < 3 o el numero de padres es >= a la poblacion,  \n"
    	if self.pmutacion.text()=="":
    		self.pmutacion.setStyleSheet("border: 2px solid red;")
    		evaluar =False
    		mensaje=mensaje+"*CAMPO PROB-MUTACION "

    	if not evaluar:
    		#QMessageBox.information(self,"ALERTA", "< HAY CAMPOS VACIOS > \n\n\n" + mensaje,QMessageBox.Discard)
    		ctypes.windll.user32.MessageBoxW(0,"< HAY CAMPOS VACIOS > \n\n\n" + mensaje , "ALERTA", 0)
    		

    	if evaluar :
    		d=len(detalles)
    		for x in range(d):
    			detalles.pop()
    		for r in range(len(yy)):
    			x.pop()
    			yy.pop()
                
                


            
                

    		self.tpoblacion.setEnabled(False)
    		self.npadres.setEnabled(False)
    		self.pmutacion.setEnabled(False)
    		self.dtallesiter.setEnabled(True)
    		self.iter.setEnabled(True)
    		#print("\n\nModelo: %s\n"%(modelos))

    		lInd= int(self.lind.text())
    		tamano=int(self.tpoblacion.text())
    		padres=int(self.npadres.text())
    		probMutac=float(self.pmutacion.text())
    		iteraciones=int(self.iteraciones.text())
    		#print("\n\nlind: %s"%(lInd))
    		#print("\n\ntamaño: %s"%(tamano))
    		#print("\n\npadres: %s"%(padres))
    		#print("\n\nprobmutacion: %s"%(probMutac))
    		#print("\n\niterarar: %s"%(iteraciones))
    		detalle1=detalle1+"*MODELO INGRESADO POR EL USUARIO: "+str(modelos) +"\n"
    		detalle1=detalle1+"*LIMITE DEL INDIVIDUO : "+str(lInd) +"\n"
    		detalle1=detalle1+"*POBLACION DE TAMAÑO : "+str(tamano) +"\n"
    		detalle1=detalle1+"*CANTIDAD DE MEJORES PADRES : "+str(padres) +"\n"
    		detalle1=detalle1+"*SE REALIZARON : "+str(iteraciones) +" ITERACIONES\n\n"
    		#crea la poblacion inicial
    		listai=[]#lista de tamaño de  individuos
    		listap=[]#lista de poblacion

    		for x in range(tamano):
    			for y in range(lInd):
    				listai.append(random.randint(0, 9))
    			listap.append(listai)
    			listai=[]
    		poblacion = listap #asigna poblacion inicial
    		#print("Poblacion Inicial:\n%s"%(poblacion)) #Se muestra la poblacion inicial
    		detalle1=detalle1+"****POBLACION ALEATORIA INICIAL****\n"+str(poblacion) +"\n\n\n"
    		detalle1=detalle1+"*******************************************************\n"
    		#Se evoluciona la poblacion 
    		# ND: Defini un nuemro de iteraciones... que debe ser un parametro
    		numItera=0
    		if iteraciones>0:
    			numItera=iteraciones
    		else:
    			numItera=10000

    		poblacion=[]
    		detalles2=""
    		self.dtallesiter.setMaximum(numItera)
    		for x in range(numItera):#numero de iteraciones para evaluar
    			puntuados=[]
    			detalles2=detalles2+"****ITERACION "+str(x+1)+"****\n\n"
    			#print("iteracion %s"%(x+1))
    			for y in range(len(listap)): #recorre la lista de poblacion
    				listax=listap[y] #toma la lista un individuo con sus bits
    				fitness = 0
    				for a in range(len(listax)):# recorre la  lista de  bits del individuo seleccionado
    					#castea los valores para comprovar el fitness
    					lis=int(listax[a])
    					mod=int(modelos[a])
    					if lis== mod:
    						fitness+=1
    				puntuados.append((fitness,listax))# guarda los pares ordenados (#de fitnes hallados, lista de  bits del individuo)
    			#print("Poblacion seleccionada:\n%s"%(puntuados))
    			detalles2=detalles2+"* POBLACION SELECCIONADA EN PARES ORDENADOS  (FITNESS, INDIVIDUO):\n"+str(puntuados)+"\n\n"
    			puntuados = [i[1] for i in sorted(puntuados)]
    			#print("Poblacion ordenada:\n%s"%(puntuados))
    			detalles2=detalles2+"* POBLACION ORDENADA SEGUN SU FITNESS: \n"+str(puntuados)+"\n\n"
    			poblacion=puntuados

    			#toma los ultimos  datos por  la seleccion de individuos
    			seleccion =  puntuados[(len(puntuados)-padres):]
    			#print("P seleccion:\n%s"%(seleccion))
    			detalles2=detalles2+"*MEJORES PROSPECTOS DE PADRES SELECCIONADOS :\n"+str(seleccion)+"\n\n"
    			#Se mezcla el material genetico para crear nuevos individuos
    			# ND: Este es el cruce:

    			for i in range(len(poblacion)-padres):
    				punto=random.randint(1,lInd-1) #Se elige un punto para hacer el intercambio
    				#print("punto de corte:\n%s"%(punto))
    				padre = random.sample(seleccion, 2) #Se eligen dos padres
    				#print("padres \n%s"%(padre)) 
    				poblacion[i][:punto] = padre[0][:punto] #Se mezcla el material genetico de los padres en cada nuevo individuo
    				poblacion[i][punto:] = padre[1][punto:]
    				#los ultimas posiciones quedan iguales pues son los padres
    			#print("P seleccion cruzada:\n%s\n\n"%(poblacion))
    			detalles2=detalles2+"*SELECCION CRUZADA - NUEVA POBLACION SIN MUTAR\n"+str(poblacion)+"\n\n"
    			for i in range(len(poblacion)-padres):
    				aleatorio=random.random()
    				if aleatorio<= probMutac:
    					punto = random.randint(1,lInd-1)
    					nuevo_valor = random.randint(1,9)
    					while nuevo_valor == poblacion[i][punto]:
    						nuevo_valor = random.randint(1,9)
    					poblacion[i][punto] = nuevo_valor
    			#print("Poblacion mutada:\n%s"%(poblacion))
    			detalles2=detalles2+"*LA NUEVA POBLACION DESPUES DE MUTAR ES :\n"+str(poblacion)+"\n\n\n"
    			total=detalle1+ detalles2
    			detalles.append(total)
    			detalles2=""
    			sumatoria = 0
    			for x in range(len(poblacion)): # cantidad de individuos
    				for q in range(len(poblacion[x])): #cantidad de bits de cada individuo
    					sumatoria+=int(poblacion[x][q]) #realiza la suma de cada uno de los bits de todos los individuos de esa iteracion
    			x.append(x)
    			yy.append(suma)#almacena en el vector plot el resultado de la suma

                
                
                    
                    
                        
                

                        
                   

    		self.solucion.setText(str(poblacion))
    		#print("\nPoblacion Final:\n%s"%(poblacion)) #Se muestra la poblacion evolucionada
    		#print( "detallado \n%s"%(detalles))
    		#print("\n\n")



    def val_grafica(self):
    	w=np.array([1, 4, 9, 16])
    	ww=np.array([1, 4, 9, 16])
    	pyplot.plot(w, ww)
    	pyplot.show()
    	

    	

    def val_detalles(self):
    	iteracion=int(self.dtallesiter.text())
    	resultado=str(detalles[(iteracion-1)])
    	#QMessageBox.information(self,"DETALLES", "< DETALLES DE LA ITERACION >\n"+resultado,QMessageBox.Discard)
    	ctypes.windll.user32.MessageBoxW(0,"< DETALLES DE LA ITERACION >\n"+resultado , "DETALLES", 0)
    	resultado=""

    def validar_lind(self):
    	lind = self.lind.text()
    	validar = re.match('^[0-9]+$', lind, re.I)
    	if lind =="":
    		self.lind.setStyleSheet("border: 2px solid red;")
    		return False
    	elif not validar :
    		self.lind.setStyleSheet("border: 2px solid red;")
    		self.lind.clear()
    		return False
    	else:
    		self.lind.setStyleSheet("border: 2px solid green;")
    		return True


    def validar_modelo(self):
    	modelo = self.modelo.text()
    	lind = int(self.lind.text())
    	validar = re.match('^[0-9]+$', modelo, re.I)
    	if modelo =="":
    		self.modelo.setStyleSheet("border: 2px solid red;")
    		return False
    	elif (not validar and  lind>int(self.cmodelo.text())) or int(modelo)>=10 :
    		self.modelo.setStyleSheet("border: 2px solid red;")
    		self.modelo.clear()
    		return False
    	else:
    		self.modelo.setStyleSheet("border: 2px solid green;")
    		return True


    def validar_tpoblacion(self):
    	tpoblacion = self.tpoblacion.text()
    	validar = re.match('^[0-9]+$', tpoblacion, re.I)
    	if tpoblacion =="":
    		self.tpoblacion.setStyleSheet("border: 2px solid red;")
    		return False
    	elif not validar  :
    		self.tpoblacion.setStyleSheet("border: 2px solid red;")
    		self.tpoblacion.clear()
    		return False
    	else:
    		self.tpoblacion.setStyleSheet("border: 2px solid green;")
    		return True


    def validar_npadres(self):
    	npadres = self.npadres.text()
    	validar = re.match('^[0-9]+$', npadres, re.I)
    	if npadres =="":
    		self.npadres.setStyleSheet("border: 2px solid red;")
    		return False
    	elif not validar:
    		self.npadres.setStyleSheet("border: 2px solid red;")
    		self.npadres.clear()
    		return False
    	else:
    		self.npadres.setStyleSheet("border: 2px solid green;")
    		return True


    def validar_pmutacion(self):
    	pmutacion = self.pmutacion.text()
    	validar = re.match('^[0-9\.]+$', pmutacion, re.I)
    	if pmutacion =="":
    		self.pmutacion.setStyleSheet("border: 2px solid red;")
    		return False
    	elif not validar:
    		self.pmutacion.setStyleSheet("border: 2px solid red;")
    		self.pmutacion.clear()
    		return False
    	else:
    		p=float(self.pmutacion.text())
    		if validar and p>1.0:
    			self.pmutacion.setStyleSheet("border: 2px solid red;")
    			self.pmutacion.clear()
    			#QMessageBox.information(self,"ALERTA", "LA PROBABILIDAD DEBE ESTAR ENTRE 0 Y 1",QMessageBox.Discard)
    			ctypes.windll.user32.MessageBoxW(0, "LA PROBABILIDAD DEBE ESTAR ENTRE 0 Y 1" , "ALERTA", 0)
    			return False
    		else:
    			self.pmutacion.setStyleSheet("border: 2px solid green;")
    			return True


    def reiniciar(self):
    	#QMessageBox.information(self,"ALERTA", "< SE REINICIARA TODA LA APLICACION >",QMessageBox.Discard)
    	ctypes.windll.user32.MessageBoxW(0, "< SE REINICIARA TODA LA APLICACION >" , "ALERTA", 0)
    	m=len(modelos)
    	d=len(detalles)
    	for x in range(m):
    		modelos.pop()
    	for x in range(d):
    		detalles.pop()

    	lInd =0
    	tamano =0
    	padres=0
    	probMutac=0 
    	self.dtallesiter.setEnabled(False)
    	self.iter.setEnabled(False)
    	self.modelo.setEnabled(True)
    	self.asignar.setEnabled(True)
    	self.tpoblacion.setEnabled(True)
    	self.npadres.setEnabled(True)
    	self.pmutacion.setEnabled(True)
    	self.solucion.setText("")
    	self.lind.setText("0")
    	self.cmodelo.setText("0")
    	self.modelo.setText("")
    	self.mmodelo.setText("")
    	self.tpoblacion.setText("")
    	self.npadres.setText("")
    	self.pmutacion.setText("")


    def mostar_modelo(self):
    	if (self.lind.text()!="0" and self.lind.text()!="" and self.lind.text()!="1" and self.lind.text()!="2" and self.lind.text()!="01" and self.lind.text()!="02") and self.modelo.text()!="" :
    		self.lind.setEnabled(False)
    		lind = int(self.lind.text())
    		cmodelo = int(self.cmodelo.text())
    		mmodelo= self.mmodelo.text()
    		modelo=self.modelo.text()
    		bits=lind-cmodelo
    		listo="000000"
    		if bits>0 :
    			cmodelo = cmodelo + 1
    			self.cmodelo.setText(str(cmodelo))
    			if cmodelo==1:
    				modelos.append(modelo)
    				mmodelo= modelo 
    				self.mmodelo.setText(str(mmodelo))
    				self.modelo.clear()
    			if bits>0 and cmodelo !=1:
    				modelos.append(modelo)
    				mmodelo=mmodelo + ", "+ modelo
    				self.mmodelo.setText(str(mmodelo))
    				self.modelo.clear()
    			#if bits>=1 and cmodelo <lind:QMessageBox.information(QWidget,"ALERTA", "INGRESE EL SIGUIENTE BIT",QMessageBox.Discard)
    			ctypes.windll.user32.MessageBoxW(0,"INGRESE EL SIGUIENTE BIT" , "ALERTA", 0)
    			if lind==int(self.cmodelo.text()):
    				self.modelo.setText(listo)
    		else:
    			self.modelo.setText(str(listo))
    			self.modelo.setEnabled(False)
    			self.asignar.setEnabled(False)
    			#QMessageBox.information(QWidget,"ALERTA", "YA INGRESO TODOS LOS BITS REQUERIDOS",QMessageBox.Discard)
    			ctypes.windll.user32.MessageBoxW(0,"YA INGRESO TODOS LOS BITS REQUERIDOS" , "ALERTA", 0)
    	else:
    		men=""
    		if self.lind.text()=="0" or self.lind.text()=="" or self.lind.text()=="01" or self.lind.text()=="02" or self.lind.text()=="1" or self.lind.text()=="2":
    			self.lind.setStyleSheet("border: 2px solid red;")
    			men=men+"*EL CAMPO LIND ESTA  VACIO O TIENE UN NUMERO < 3\n"
    		if self.modelo.text()=="":
    			self.modelo.setStyleSheet("border: 2px solid red;")
    			men=men+"*EL CAMPO MODELO ESTA  VACIO  "
    		#QMessageBox.information(QWidget,"ALERTA", "< ALGO ESTA MAL >\n\n"+men,QMessageBox.Discard)
    		ctypes.windll.user32.MessageBoxW(0,"< ALGO ESTA MAL >\n\n"+men , "ALERTA", 0)
		
			
				


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

