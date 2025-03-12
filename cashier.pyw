# -*- coding: utf-8 -*-

from   logs import logWrite
from   tkinter import *
from   tkinter import ttk
from   tkinter.messagebox import showwarning, showinfo, askyesno
from   drivers.kkt.atol.driver import AtolDriver
import os
import re
import subprocess
import _thread


class AppCashier(AtolDriver):
	def __init__(self, master):
		super().__init__()
		
		self.master = master
		
		# Для компонентов notebook используюем стили
		lib_background  	= 'LightGray'
		lib_font_base   	= 'helvetica 12'
		lib_font_enlarged   = 'helvetica 14'
		lib_foreground  	= 'black'
		lib_timber_wolf 	= '#DCDAD5'

		s = ttk.Style()

		# Стиль 1
		# s.theme_create("yummy", parent="alt", settings={
				# 'TCombobox': {'map': {'fieldbackground': [('readonly', 'white')], 'selectbackground': [('readonly', 'white')], 'selectforeground': [('readonly', 'black')]} },
				# "TNotebook": {"configure": {"background": lib_background, 'relief': 'groove', 'padding': 5} }, 
				# "TNotebook.Tab": {
					# "configure": {"padding": 5, "width": 10, "background": lib_background, "font": lib_font_base, 'focuscolor': lib_timber_wolf},
					# "map":       {"background": [("selected", lib_timber_wolf)]}
								 # }
							  # } 
						# )

		# s.theme_use("yummy")


		# Стиль 2
		s.theme_use("clam")

		s.configure("TNotebook", background=lib_background, relief="groove", padding=5)
		s.map("TNotebook", background=[("disabled", lib_background), ("focus", lib_background)], relief=[("disabled", "groove"), ("focus", "groove")])

		s.configure('TNotebook.Tab', background=lib_background, font=lib_font_base, foreground=lib_foreground, focuscolor=lib_timber_wolf, width=10)
		s.map("TNotebook.Tab", background=[("disabled", lib_foreground), ("focus", lib_timber_wolf), ("selected", lib_timber_wolf)]) 
		# s.map("TNotebook.Tab", font = [("disabled", lib_font_base), ("focus", lib_font_base)])
		# s.map("TNotebook.Tab", foreground = [("disabled", lib_foreground), ("focus", lib_foreground)])

		s.configure('TCombobox', background=lib_background)
		s.map('TCombobox', fieldbackground=[('readonly','white')], selectbackground=[('readonly', 'white')], selectforeground=[('readonly', 'black')])



		# Создаем набор вкладок
		notebook = ttk.Notebook()
		notebook.pack(expand=True, fill=BOTH)
		 
		# Создаем пару фреймвов
		BasicFrame = ttk.Frame(notebook)
		CashiersFrame = ttk.Frame(notebook)
		 
		BasicFrame.pack(fill=BOTH, expand=True)
		CashiersFrame.pack(fill=BOTH, expand=True)
		 
		# Добавляем фреймы в качестве вкладок
		notebook.add(BasicFrame, text="Основные")
		notebook.add(CashiersFrame, text="Кассиры")


		# Определить Название торговой точки
		Label(BasicFrame, text="Название торговой точки", bg=lib_timber_wolf, font=lib_font_base).grid(row=0, column=0, padx=10, pady=[15, 3], sticky=W)
		self.sale_name = Entry(BasicFrame, font=lib_font_enlarged, width=53)
		self.sale_name.grid(row=1, column=0, padx=10, sticky=EW)

		# Определить Адрес торговой точки
		Label(BasicFrame, text="Адрес торговой точки", bg=lib_timber_wolf, font=lib_font_base).grid(row=2, column=0, padx=10, pady=[15, 3], sticky=W)
		self.sale_address = Entry(BasicFrame, font=lib_font_enlarged)
		self.sale_address.grid(row=3, column=0, padx=10, sticky=EW)


		# Определить номер кассы
		Label(BasicFrame, text="№ кассы", bg=lib_timber_wolf, font=lib_font_base).grid(row=2, column=1, padx=10, pady=[15, 3], sticky=W)
		self.cash_number = Entry(BasicFrame, font=lib_font_enlarged, width=23)
		self.cash_number.grid(row=3, column=1, padx=10, sticky=EW)


		# Определить список моделей касс
		Label(BasicFrame, text="Модель кассы", bg=lib_timber_wolf, font=lib_font_base).grid(row=4, column=0, padx=10, pady=[15, 3], sticky=W)

		self.model_value = ['Демо-режим', 'Штрих-М', 'Viki-M', 'Атол', 'Windows-принтер', 'Несколько касс']

		self.cash_model = ttk.Combobox(BasicFrame, font=lib_font_enlarged, width=24, height=15, values=self.model_value, state="readonly")		
		self.cash_model.grid(row=5, column=0, padx=10, sticky=W)
		self.cash_model.bind("<<ComboboxSelected>>")

		self.btnProperty = Button(BasicFrame, bg='LightGrey', text="Свойства", command=self.loadSettings, state=NORMAL)
		self.btnProperty.place(x=565, y=520, width=100, height=30)
		
		self.btnConfirm = Button(BasicFrame, bg='LightGrey', text="ОК", command=self.confirm, state=NORMAL)
		self.btnConfirm.place(x=670, y=520, width=100, height=30)

		Button(BasicFrame, bg='LightGrey', text="Закрыть", command=self.dismissApp).place(x=775, y=520, width=100, height=30)


	def confirm(self):
		if self.lock:
			return
		
		if self.sale_name.get() == '':
			# showinfo(title="Информация", message="Не заполнено - Название торговой точки")
			name = ' '
		else:
			name = self.sale_name.get()
			
		if self.sale_address.get() == '':
			# showinfo(title="Информация", message="Не заполнен - Адрес торговой точки")
			address = ' '
		else:
			address = self.sale_address.get()

		number = re.sub(r"^\s+|\n|\r|\s+$", '', self.cash_number.get())

		if number == '':
			showinfo(title="Информация", message="Поле № кассы не может быть не заполнено")
		else:
			model = self.idxCombobox()
			if model == None:
				showinfo(title="Информация", message="Не выбрана модель кассы")
			else:
				if number != '':
					setting = {
								'name': 	name,
								'address': 	address,
								'number': 	number,
								'model': 	model
							  }
					
					path = self.pathToFile(number)
					
					if os.path.exists(path):
						load = askyesno(title="Подтвержение операции", message=f"Найдены настройки кассы № {number}, загрузить сохраненные настройки?")

						if load:
							settings = self.kktSettings(path)

							# self.setFields(settings)
							self.openThread(settings)
							
							# showwarning(title="Внимание", message="Изменение свойств драйвера изменят настройки кассы.")
							
							self.loadSettingsDrv(path)
						else:
							update = askyesno(title="Подтвержение операции", message=f"Обновить настройки кассы № {number} с текущими параметрами рабочего места?")
							
							if update:
								settings = self.kktSettings(path)
								
								settings['name'] 	= name
								settings['address'] = address
								settings['model']	= model
								
								settings['path'] 	= path
								
								self.saveSettings(settings)
								self.loadSettingsDrv(path)
					else:
						create = askyesno(title="Подтвержение операции", message=f"Создать новую настройку кассы № {number}?")
						
						log = f"Создать новую настройку кассы № {number}? = " + str(create)
						self.logWrite(log)

						if create:
							try:
								setting['path'] = path
								
								self.saveSettings(setting)
								self.loadSettingsDrv(path)
							except Exception as e:
								log = f'Ошибка записи настроек кассы № {number}: ' + str(e)
								self.logWrite(log)


	def loadSettings(self):
		if self.lock:
			return
		
		number 	= re.sub(r"^\s+|\n|\r|\s+$", '', self.cash_number.get())
		path 	= self.pathToFile(number)
		
		if not os.path.exists(path):
			path = ''
		self.loadSettingsDrv(path)
	
	
	def openThread(self, settings):
		_thread.start_new_thread(self.setFields, (settings,))
	
	
	def setFields(self, settings):
		self.sale_name.delete(0, END)
		self.sale_name.insert(0, settings['name'])
		self.sale_address.delete(0, END)
		self.sale_address.insert(0, settings['address'])
		self.cash_model.current(settings['model'])


	def idxCombobox(self):
		selection = self.cash_model.get()
		for i, value in enumerate(self.model_value):
			if selection == value:
				return int(i)
	
	
	def dismissApp(self):
		if os.path.exists('atol-key-backup.reg'):
			res = subprocess.run(['REGEDIT', '/S', os.path.join(self.cwd, 'atol-key-backup.reg')], shell=True)	# Выполнится если пользователь имеет членство в группе Администраторы
			self.logWrite(res)
			
			try:
				os.remove(os.path.join(self.cwd, 'atol-key-backup.reg'))
			except FileNotFoundError as e:
				log = str(e)
				self.logWrite(log)
				# res = subprocess.run(['REG', 'DELETE', 'HKLM\\Software\\ATOL\\Drivers', '/Y'], shell=True)	# Выполнится только в случае если программа запущена от имени Администратора \\10.0\\KKT
				# self.logWrite(res)
				
		self.master.quit()



def main():
	master = Tk()
	obj_cashier = AppCashier(master)
	master.title("Настройка рабочего места кассира 10.3")
	master.iconbitmap(os.path.join(obj_cashier.cwd, 'src\\ico\\fptr_t.ico'))
	master.geometry("900x600")
	master.resizable(False, False)

	# Установка отображения формы в центре экрана
	x = (master.winfo_screenwidth() - master.winfo_reqwidth()) / 3.5
	y = (master.winfo_screenheight() - master.winfo_reqheight()) / 4

	master.wm_geometry("+%d+%d" % (x, y))
	master.protocol('WM_DELETE_WINDOW', obj_cashier.dismissApp)
	master.mainloop()


if __name__=='__main__':
	logWrite("{} [{}]".format(os.getpid(), type(os.getpid())))
	main()



	# import sys
	# print(sys.version_info)
	# print(sys.executable, __file__)










