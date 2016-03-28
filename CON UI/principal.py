#coding: iso-8859-1
#*********algoritmos geneticos *********
#@utor: NAUFRAGO(Yeison Aguirre Osorio )
#22 marzo 2016
#***************************************
import sys, re, random

from PyQt5.QtWidgets import QApplication,QDialog, QMessageBox
from PyQt5 import uic

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

class Dialogo(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi('algoritmo.ui', self)
		self.lind.textChanged.connect(self.validar_lind)
		self.modelo.textChanged.connect(self.validar_modelo)
		self.tpoblacion.textChanged.connect(self.validar_tpoblacion)
		self.npadres.textChanged.connect(self.validar_npadres)
		self.pmutacion.textChanged.connect(self.validar_pmutacion)
		self.asignar.clicked.connect(self.mostar_modelo)
		self.evaluar.clicked.connect(self.imprimir)
		self.reiniciarr.clicked.connect(self.reiniciar)
		self.iter.clicked.connect(self.val_detalles)



	
				
	
		

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
			QMessageBox.information(self,"ALERTA", "< HAY CAMPOS VACIOS > \n\n\n" + mensaje,QMessageBox.Discard)


		if evaluar :

			self.tpoblacion.setEnabled(False)
			self.npadres.setEnabled(False)
			self.pmutacion.setEnabled(False)
			print("\n\nModelo: %s\n"%(modelos))
			
			lInd= int(self.lind.text())
			tamano=int(self.tpoblacion.text())
			padres=int(self.npadres.text())
			probMutac=float(self.pmutacion.text())
			iteraciones=int(self.iteraciones.text())
			print("\n\nlind: %s"%(lInd))
			print("\n\ntamaño: %s"%(tamano))
			print("\n\npadres: %s"%(padres))
			print("\n\nprobmutacion: %s"%(probMutac))
			print("\n\niterarar: %s"%(iteraciones))
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
			print("Poblacion Inicial:\n%s"%(poblacion)) #Se muestra la poblacion inicial
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
				print("iteracion %s"%(x+1))
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
				print("Poblacion seleccionada:\n%s"%(puntuados))
				detalles2=detalles2+"* POBLACION SELECCIONADA EN PARES ORDENADOS  (FITNESS, INDIVIDUO):\n"+str(puntuados)+"\n\n"
				puntuados = [i[1] for i in sorted(puntuados)]
				print("Poblacion ordenada:\n%s"%(puntuados))
				detalles2=detalles2+"* POBLACION ORDENADA SEGUN SU FITNESS: \n"+str(puntuados)+"\n\n"
				poblacion=puntuados


				#toma los ultimos  datos por  la seleccion de individuos
				seleccion =  puntuados[(len(puntuados)-padres):]
				print("P seleccion:\n%s"%(seleccion))
				detalles2=detalles2+"*MEJORES PROSPECTOS DE PADRES SELECCIONADOS :\n"+str(seleccion)+"\n\n"


				#Se mezcla el material genetico para crear nuevos individuos
			    # ND: Este es el cruce:
				for i in range(len(poblacion)-padres):
					punto=random.randint(1,lInd-1) #Se elige un punto para hacer el intercambio
					print("punto de corte:\n%s"%(punto))
					padre = random.sample(seleccion, 2) #Se eligen dos padres
					print("padres \n%s"%(padre)) 
					poblacion[i][:punto] = padre[0][:punto] #Se mezcla el material genetico de los padres en cada nuevo individuo
					poblacion[i][punto:] = padre[1][punto:]
					#los ultimas posiciones quedan iguales pues son los padres
				print("P seleccion cruzada:\n%s\n\n"%(poblacion))
				detalles2=detalles2+"*SELECCION CRUZADA - NUEVA POBLACION SIN MUTAR\n"+str(poblacion)+"\n\n"

				for i in range(len(poblacion)-padres):
					aleatorio=random.random()
					if aleatorio<= probMutac:
						punto = random.randint(1,lInd-1)
						nuevo_valor = random.randint(1,9)
						while nuevo_valor == poblacion[i][punto]:
							nuevo_valor = random.randint(1,9)
						poblacion[i][punto] = nuevo_valor
				print("Poblacion mutada:\n%s"%(poblacion))
				detalles2=detalles2+"*LA NUEVA POBLACION DESPUES DE MUTAR ES :\n"+str(poblacion)+"\n\n\n"
				total=detalle1+ detalles2
				detalles.append(total)
				detalles2=""




				
			self.solucion.setText(str(poblacion))
			print("\nPoblacion Final:\n%s"%(poblacion)) #Se muestra la poblacion evolucionada
			print( "detallado \n%s"%(detalles))
			print("\n\n")

				

	
	        

	        
	 
	            
	 

	def val_detalles(self):

		iteracion=int(self.dtallesiter.text())
		resultado=str(detalles[(iteracion-1)])
		QMessageBox.information(self,"DETALLES", "< DETALLES DE LA ITERACION >\n"+resultado,QMessageBox.Discard)
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
				QMessageBox.information(self,"ALERTA", "LA PROBABILIDAD DEBE ESTAR ENTRE 0 Y 1",QMessageBox.Discard)
				return False
			else:
				self.pmutacion.setStyleSheet("border: 2px solid green;")
				return True



	def reiniciar(self):
		QMessageBox.information(self,"ALERTA", "< SE REINICIARA TODA LA APLICACION >",QMessageBox.Discard)
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
		self.lind.setEnabled(True)
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
		if (self.lind.text()!="0" and self.lind.text()!="" and self.lind.text()!="1" and self.lind.text()!="2") and self.modelo.text()!="" :
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
				if bits>=1 and cmodelo <lind:
					QMessageBox.information(self,"ALERTA", "INGRESE EL SIGUIENTE BIT",QMessageBox.Discard)
				if lind==int(self.cmodelo.text()):
					self.modelo.setText(listo)
					

			else:
				self.modelo.setText(str(listo))
				self.modelo.setEnabled(False)
				self.asignar.setEnabled(False)
				QMessageBox.information(self,"ALERTA", "YA INGRESO TODOS LOS BITS REQUERIDOS",QMessageBox.Discard)

		else:
			men=""
			if self.lind.text()=="0" or self.lind.text()=="" or self.lind.text()=="01" or self.lind.text()=="02" or self.lind.text()=="1" or self.lind.text()=="2":
				self.lind.setStyleSheet("border: 2px solid red;")
				men=men+"*EL CAMPO LIND ESTA  VACIO O TIENE UN NUMERO < 3\n"
			if self.modelo.text()=="":
				self.modelo.setStyleSheet("border: 2px solid red;")
				men=men+"*EL CAMPO MODELO ESTA  VACIO  "

			QMessageBox.information(self,"ALERTA", "< ALGO ESTA MAL >\n\n"+men,QMessageBox.Discard)

	
    
   


app=QApplication(sys.argv)
dialogo=Dialogo()
dialogo.show()
app.exec_()