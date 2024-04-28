#Прочитати збережений csv-файл із попереднього завдання та зберегти дані в excel-файл.
#Крім віку - стовпець з цими даними не потрібний.

#*Додаткове завдання не обов'язкове до виконання:
#розгорнути таблицю на дев'яносто градусів (стовпці стають рядками, а рядки стовпцями).
#До завдання прикріплений приклад як має виглядати змісту підсумкового файлу.

import csv, openpyxl

# with open('my_first.csv') as file:
#     reader_csv = file.read()
#     print(reader_csv)

wb = openpyxl.Workbook()
wb.create_sheet('first_list', index=0)
wb.remove(wb['Sheet'])
print(wb.sheetnames)