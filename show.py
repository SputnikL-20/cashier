# -*- coding: utf-8 -*-

from   libfptr10 import IFptr										# Обертка Python-API
from   logs import logWrite
from   tkinter.messagebox import showerror, showinfo
from   winreg import QueryValueEx, OpenKey, HKEY_LOCAL_MACHINE
import codecs
import json
import os
import platform
import subprocess
import sys

class Show:
	def __init__(self, path = '', pid = 0):
		self.logWrite	= logWrite
		self.cwd  	 	= os.getcwd()								# Получаем абсолютный путь корня запущенного приложения cashier.pyw
		self.path		= path										# Параметр 'path' (тип строка) представляет путь к файлу json с настройками кассы
		self.pid		= os.getpid()


	def showSettings(self):
		
		self.existsKey()
		
		settings = {}
		self.IFptr = IFptr
		self.fptr = self.IFptr('')
		
		if self.path != '':
			settings = self.getSettings(self.path)
			if 'settings' in settings:								# Если ключ 'settings' присутствуют
				self.fptr.setSettings(settings['settings'])			# Устанавливаем параметры свойств драйвера

		result = self.fptr.showProperties(self.IFptr.LIBFPTR_GUI_PARENT_NATIVE, 0)	# Диалог настройки связи с ККТ

		if result != -1 and result != 1:
			news_settings = self.fptr.getSettings()
			
			if 'settings' in settings:
				saves_settings = settings.pop('settings')
				state = self.equalsKwargs(saves_settings, news_settings)
				
				if state == 0:
					settings['settings'] = news_settings
					settings['path'] 	 = self.path
					self.setSettings(settings)
			
			elif not 'settings' in settings and self.path != '':
				
				# if self.path == '':
					# showerror(title="Ошибка. Не выбрана касса.", message="Невозможно сохранить настройки свойств.")
				# else:
				settings['settings'] = news_settings
				settings['path'] 	 = self.path
				self.setSettings(settings)
				
		elif result == -1:
			self.logWrite("{} [{}]".format(self.fptr.errorCode(), self.fptr.errorDescription()))
		
		del self.fptr


	def getSettings(self, path):									# Функция возвращает настройки свойств драйвера кассы и основные настройки рабочего места в коллекции dict
		with open(path, "r") as inpfile:
			settings = json.load(inpfile)
		return settings


	def setSettings(self, settings):								# Функция записи настроек в файл *.json
		path = settings.pop('path')									# Извлекаем ключ с данными расположения файла настроек, сам ключ удаляется
		with open(path, "w") as outfile:							# Конвертация и запись JSON объекта  в файл *.json
			json.dump(settings, outfile, indent=4)


	def equalsKwargs(self, settings, news_settings):				# Сравнение настроек имеющихся и измененных свойст драйвера
		for key, value in settings.items():
			if key in news_settings:
				if value != news_settings[key]:
					return 0


	def existsKey(self):
		try:
			lib_path = os.path.join(QueryValueEx(OpenKey(HKEY_LOCAL_MACHINE, "Software\\ATOL\\Drivers\\10.0\\KKT"), "INSTALL_DIR")[0], 'bin\\fptr10.dll')
			
			key = QueryValueEx(OpenKey(HKEY_LOCAL_MACHINE, "Software\\ATOL\\Drivers\\10.0\\KKT"), "INSTALL_DIR")[0]
			log = "Путь к библиотеке в реестре: " + str(key)
			self.logWrite(log)
			
			if platform.architecture()[0] == '64bit':
				lib_app  = os.path.join(self.cwd, 'ATOL\\x64\\KKT')
			elif platform.architecture()[0] == '32bit':
				lib_app  = os.path.join(self.cwd, 'ATOL\\x86\\KKT')
			
			self.logWrite(lib_app)
			
			if str(key) != lib_app:
				log = "Значение параметра INSTALL_DIR ключа КТТ в реестре не равно расположению библиотеки fptr10.dll. Будет создан новый ключ."
				self.logWrite(log)
				
				processjl = subprocess.Popen(['REG', 'EXPORT', 'HKLM\Software\ATOL', os.path.join(self.cwd, 'atol-key-backup.reg'), '/Y'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				stdout, stderr = processjl.communicate()

				if len(stdout) != 0:
					log = stdout.decode('866').strip() + ' Путь: ' + os.path.join(self.cwd, 'atol-key-backup.reg')
				elif len(stderr) != 0:
					log = stderr.decode('866')
				
				self.logWrite(log)
				
				self.createKey()
			else:
				return
			
		except FileNotFoundError as e:
			log = "Отсутствует запись в реестре: " + str(e.args)
			self.logWrite(log)
			
			keys = u"Windows Registry Editor Version 5.00\n\n\
[HKEY_LOCAL_MACHINE\Software\ATOL]\n\n\
[-HKEY_LOCAL_MACHINE\Software\ATOL\Drivers]\n\n\
[-HKEY_LOCAL_MACHINE\Software\ATOL\Drivers\\10.0]\n\n\
[-HKEY_LOCAL_MACHINE\Software\ATOL\Drivers\\10.0\KKT]\n"
			
			# Pick the non-native version of UTF-16 encoding
			bom = codecs.BOM_UTF16_LE
			encoding = 'utf_16_le'
			
			encoded_text = keys.encode(encoding) # Encode the text.
			
			with open('atol-key-backup.reg', mode='wb') as f:
				# Write the selected byte-order marker. It is not included in the encoded text because we were explicit about the byte order when selecting the encoding.
				f.write(bom)
				# Write the byte string for the encoded text.
				f.write(encoded_text)
			
			self.createKey()
	
	def createKey(self):
		keys = u"Windows Registry Editor Version 5.00\n\n\
[HKEY_LOCAL_MACHINE\Software\ATOL]\n\n\
[HKEY_LOCAL_MACHINE\Software\ATOL\Drivers]\n\n\
[HKEY_LOCAL_MACHINE\Software\ATOL\Drivers\\10.0]\n\n\
[HKEY_LOCAL_MACHINE\Software\ATOL\Drivers\\10.0\KKT]\n"
		
		value = self.cwd.replace("\\", "\\\\")
		
		if platform.architecture()[0] == '64bit':
			keys = keys + f'"INSTALL_DIR"="{value}\\\\ATOL\\\\x64\\\\KKT"'
		elif platform.architecture()[0] == '32bit':
			keys = keys + f'"INSTALL_DIR"="{value}\\\\ATOL\\\\x86\\\\KKT"'
		
		# Pick the non-native version of UTF-16 encoding
		bom = codecs.BOM_UTF16_LE
		encoding = 'utf_16_le'
		
		encoded_text = keys.encode(encoding) # Encode the text.
		
		with open('key-cashier.reg', mode='wb') as f:
			# Write the selected byte-order marker.  It is not included in the encoded text because we were explicit about the byte order when selecting the encoding.
			f.write(bom)
			# Write the byte string for the encoded text.
			f.write(encoded_text)
		
		log = "Создан новый ключ реестра. Абсолютный путь ключа: " + os.path.join(self.cwd, "key-cashier.reg")
		self.logWrite(log)
		
		res = subprocess.run(['REGEDIT', '/S', os.path.join(self.cwd, 'key-cashier.reg')], shell=True) # Выполнится только в случае если программа запущена от имени Администратора
		self.logWrite(res)
		
		try:
			os.remove(os.path.join(self.cwd, 'key-cashier.reg'))
		except FileNotFoundError as e:
			log = str(e)
			self.logWrite(log)



if __name__=='__main__':
	if len(sys.argv) > 1:
		obj_show = Show(sys.argv[1], sys.argv[2])
	else:
		obj_show = Show()
	
	obj_show.showSettings()




