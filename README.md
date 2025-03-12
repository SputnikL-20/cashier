# cashier
Настройка рабочего места кассира 10.3

Чтобы программа выполнилась, - необходимо запускать файл `cashier.pyw`.
Программа умеет подключатся, сохранять и восстанавливать настройки свойств драйвера Атол для разных онлайн касс. 
Даже если приложение `Тест драйвера ККТ` не установлено на компьютере пользователя.
Программа реализована на библиотеке драйвера fptr10.dll Атол 10.3 для Windows (x86-x64), обертка API libfptr10.py на языке Python соответственно.

-----------------------
ВНИМАНИЕ: Программа манипулирует системный реестром Windows (HKEY_LOCAL_MACHINE). 
Если приложение не работает должным образом необходимо запустить `cashier.pyw` или файл `autorun.cmd` от имени Администратора.

-----------------------
ПРИЛОЖЕНИЕ: Ключ реестра Windows по умолчанию для всех версий драйвера АТОЛ (HKEY_LOCAL_MACHINE\SOFTWARE\ATOL\Drivers\10.0\KKT), - значение котого это путь к директории с установленной программой `Тест драйвера ККТ` (C:\Program Files\ATOL\Drivers10\KKT).
