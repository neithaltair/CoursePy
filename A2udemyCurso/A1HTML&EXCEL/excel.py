#ficheros formato excel
import pandas as pd
#pasa el contenido del excel a un dataFrame
#video 124
ficheroExcel = pd.ExcelFile('/home/neithaltair/Documentos/CoursePy/A2udemyCurso/A1HTML&EXCEL/poblacion.xlsx')

misdatExc = ficheroExcel.parse('Hoja1')

print(misdatExc)