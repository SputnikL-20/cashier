# -*- coding: utf-8 -*-

from   logs import logWrite
import json
import os
import subprocess
import _thread


class AtolDriver:
    def __init__(self):
        self.cwd      = os.getcwd()                 # Получаем абсолютный путь корня запущенного приложения cashier.pyw
        self.logWrite = logWrite
        self.lock     = False


    def loadSettingsDrv(self, path):                # Функция открытия свойств настроек драйвера Атол
        try:
            self.openSubprocess(path, os.getpid())
        except Exception as e:
            log = 'Ошибка открытия процесса: ' + str(e)
            self.logWrite(log)


    def openSubprocess(self, path, pid):
        _thread.start_new_thread(self.startSubprocess, (path, pid))


    def startSubprocess(self, path, pid):
        self.lock = True
        res = subprocess.run([os.path.join(self.cwd, 'show.py'), str(path), str(pid)], shell=True)
        
        if res.returncode == 0:
            self.lock = False


    def saveSettings(self, settings):               # Функция записи настроек в файл *.json
        path = settings.pop('path')                 # Извлекаем ключ с данными расположения файла настроек, сам ключ удаляется
        if not os.path.isdir(os.path.dirname(path)):
            os.mkdir(os.path.dirname(path), mode=0o777, dir_fd=None)
        with open(path, "w") as outfile:            # Конвертация и запись JSON объекта  в файл *.json
            json.dump(settings, outfile, indent=4)


    def kktSettings(self, path):                    # Функция возвращает настройки свойств драйвера кассы и основные настройки рабочего места в коллекции dict
        with open(path, "r") as inpfile:
            settings = json.load(inpfile)
        return settings


    def pathToFile(self, number):                                           # Получаем абсолютный путь к файлу настроек по имени номера кассы
        path = os.path.join(self.cwd, f'src\\json\\{number}.json')          # Получаем полный путь к файла с расширением *.json 
        return path













# def functionAnonim(**kwargs):
    # for name, value in kwargs.items():
        # print(f'{name} = {value}')






