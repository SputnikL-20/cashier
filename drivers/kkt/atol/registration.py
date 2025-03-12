# -*- coding: utf-8 -*-
#
#########################
# Регистрация ККТ для Версии 10.10.6.0
#
# Для регистрации ККТ необходимо вызвать метод fnOperation() с типом операции LIBFPTR_PARAM_FN_OPERATION_TYPE равным LIBFPTR_FNOP_REGISTRATION. 
# Также необходимо указать параметры регистрации:
#
# Параметр 								Описание 										Тип 	Версии ФФД
# -------------------------------------+-----------------------------------------------+-------+----------
# 1060 									Адрес сайта ФНС 								string 	Все
# 1009 									Адрес расчетов 									string 	Все
# 1018 									ИНН пользователя 								string 	Все
# 1048 									Наименование пользователя 						string 	Все
# 1062 									Системы налогообложения 						int 	Все
# 1117 									Адрес электронной почты отправителя чека 		string 	Все
# 1057 									Признак агента 									int 	≤ 1.1
# 1187 									Место расчетов 									string 	Все
# 1037 									Регистрационный номер ККТ 						string 	Все
# 1209 									Номер версии ФФД 								int 	≤ 1.1
# 1001 									Признак автоматического режима 					bool 	Все
# 1036 									Номер автомата 									string 	Все
# 1002 									Признак автономного режима 						bool 	Все
# 1056 									Признак шифрования 								bool 	Все
# 1108 									Признак ККТ для расчетов в сети Интернет 		bool 	Все
# 1109 									Признак расчетов за услуги 						bool 	Все
# 1110 									Признак АС БСО 									bool 	Все
# 1126 									Признак проведения лотерей 						bool 	Все
# 1193 									Признак проведения азартных игр 				bool 	Все
# 1207 									Признак подакцизного товара 					bool 	Все
# 1221 									Признак установки в автомате 					bool 	Все
# LIBFPTR_PARAM_PAWN_SHOP_ACTIVITY 		Признак осуществления ломбардной деятельности 	bool 	≥ 1.2
# LIBFPTR_PARAM_INSURANCE_ACTIVITY 		Признак осуществления страховой деятельности 	bool 	≥ 1.2
# LIBFPTR_PARAM_TRADE_MARKED_PRODUCTS 	Признак торговли маркированными товарами 		bool 	≥ 1.2
# LIBFPTR_PARAM_VENDING 				Признак применения в торговом автомате 			bool 	≥ 1.2
# LIBFPTR_PARAM_CATERING 				Признак осуществления услуг общ. питания 		bool 	≥ 1.2
# LIBFPTR_PARAM_WHOLESALE 				Признак оптовой торговли 						bool 	≥ 1.2
# 1017 									ИНН ОФД 										string 	Все
# 1046 									Название ОФД 									string 	Все
# -------------------------------------+-----------------------------------------------+-------+----------


def registration(fptr, IFptr, settings):	# Функция регистрация ККТ Атол
	
	# logRegistration(settings)
	
	if settings['model'] == 3:	# Условие для модели кассы Атол (3)
		
		try:
			fptr.setParam(IFptr.LIBFPTR_PARAM_FN_OPERATION_TYPE, IFptr.LIBFPTR_FNOP_REGISTRATION)
			
			# Также необходимо указать параметры регистрации:
			fptr.setParam(1060, "www.nalog.gov.ru")						# Адрес сайта ФНС
			fptr.setParam(1009, settings['address'])					# Адрес расчетов +
			fptr.setParam(1018, " ")									# ИНН пользователя
			fptr.setParam(1048, settings['name'])						# Наименование пользователя
			
			# Значение реквизита 1062 (системы налогообложения) - битовое поле, значениями которого являются одно или несколько из следующих значений:
			# LIBFPTR_TT_OSN 				- общая;
			# LIBFPTR_TT_USN_INCOME 		- упрощенная доход;
			# LIBFPTR_TT_USN_INCOME_OUTCOME - упрощенная доход минус расход;
			# LIBFPTR_TT_ESN 				- единый сельскохозяйственный доход;
			# LIBFPTR_TT_PATENT 			- патентная система налогообложения.	
			fptr.setParam(1062, IFptr.LIBFPTR_TT_OSN | IFptr.LIBFPTR_TT_PATENT)		# Системы налогообложения
			fptr.setParam(1117, " ")												# Адрес электронной почты отправителя чека
			
			# Значение реквизита 1057 (признак агента) - битовое поле, значениями которого являются одно или несколько из следующих значений:
			# LIBFPTR_AT_NONE 					- признак агента отсутствует;
			# LIBFPTR_AT_BANK_PAYING_AGENT 		- банковский платежный агент;
			# LIBFPTR_AT_BANK_PAYING_SUBAGENT 	- банковский платежный субагент;
			# LIBFPTR_AT_PAYING_AGENT 			- платежный агент;
			# LIBFPTR_AT_PAYING_SUBAGENT 		- платежный субагент;
			# LIBFPTR_AT_ATTORNEY 				- поверенный;
			# LIBFPTR_AT_COMMISSION_AGENT 		- комиссионер;
			# LIBFPTR_AT_ANOTHER 				- другой тип агента, "иной" агент.
			fptr.setParam(1057, IFptr.LIBFPTR_AT_BANK_PAYING_AGENT | IFptr.LIBFPTR_AT_PAYING_AGENT | IFptr.LIBFPTR_AT_ATTORNEY)

			fptr.setParam(1187, settings['address'])				# Место расчетов +
			fptr.setParam(1037, settings['number'])					# Регистрационный номер ККТ +
			
			# Реквизит 1209 (номер версии ФФД) может принимать следующие значения:
			# LIBFPTR_FFD_UNKNOWN 	- неизвестная;
			# LIBFPTR_FFD_1_0_5 	- ФФД 1.05;
			# LIBFPTR_FFD_1_1 		- ФФД 1.1;
			# LIBFPTR_FFD_1_2 		- ФФД 1.2.
			fptr.setParam(1209, IFptr.LIBFPTR_FFD_1_0_5)			# ФФД 1.05
			fptr.setParam(1001, False)								# Признак автоматического режима
			fptr.setParam(1036, " ")								# Номер автомата
			fptr.setParam(1002, False)								# Признак автономного режима
			fptr.setParam(1056, False)								# Признак шифрования
			fptr.setParam(1108, False)								# Признак ККТ для расчетов в сети Интернет
			fptr.setParam(1109, False)								# Признак расчетов за услуги
			fptr.setParam(1110, False)								# Признак АС БСО
			fptr.setParam(1126, False)								# Признак проведения лотерей
			fptr.setParam(1193, False)								# Признак проведения азартных игр
			fptr.setParam(1207, False)								# Признак подакцизного товара
			fptr.setParam(1221, False)								# Признак установки в автомате

			fptr.setParam(1017, "9715260691")						# ИНН ОФД
			fptr.setParam(1046, "ООО \"Эвотор ОФД\"")				# Название ОФД

			fptr.fnOperation()
			
		except Exception as e:
			e = 'Ошибка: ' + str(e)
			logRegistration(log)




def logRegistration(log):

	from datetime import datetime

	with open('file-log.log', 'a', encoding='UTF-8') as f:
		print(datetime.now(), f'{str(log)}', file=f)



