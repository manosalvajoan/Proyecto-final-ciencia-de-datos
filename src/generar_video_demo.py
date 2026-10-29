"""Crea video demostrativo narrado por síntesis de voz, NO sustituye exposición del equipo.
Requiere libreoffice, pdftoppm, ffmpeg y espeak instalados.
"""
from pathlib import Path
import subprocess, json
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'presentacion'/'Proyecto_Final_Analisis_Salarios.pdf'
OUT=ROOT/'video'
WORK=ROOT/'.cache_video'
WORK.mkdir(exist_ok=True)
NARRACIONES=[
"Hola. Somos el equipo de Ciencia de Datos. En este proyecto estudiamos la distribución de salarios de una organización simulada y construimos una regresión lineal para estimarlos. Nuestro recorrido integra limpieza, estadística y aprendizaje automático, siempre destacando los límites de los resultados.",
"El punto de partida es una pregunta práctica: ¿qué variables se relacionan con los salarios? Un área de Talento Humano puede necesitar respuestas para planificar su presupuesto. Sin embargo, no pretendemos determinar el sueldo justo de una persona ni automatizar decisiones individuales.",
"En la primera etapa diseñamos un conjunto ficticio y reproducible de mil quinientas catorce filas con doce columnas. Incluye salario, experiencia, antigüedad, nivel de cargo y otras características. Elegimos este escenario porque conecta la ingeniería de sistemas con análisis de datos de nómina, sin divulgar información confidencial.",
"La exploración detectó catorce registros duplicados y dieciséis filas con errores de edad o de salario. Después de eliminarlos conservamos mil cuatrocientos ochenta y cuatro registros. También normalizamos nombres de departamentos, tratamos datos faltantes y verificamos la consistencia. Dejamos documentadas todas estas reglas de limpieza.",
"En la segunda etapa usamos estadística descriptiva. El salario mensual promedio simulado fue aproximadamente seis millones cuatrocientos mil pesos, mientras la mediana fue cercana a seis millones doscientos mil. El histograma muestra la forma de la distribución y nos recuerda que el promedio no representa exactamente a cada empleado.",
"Luego comparamos departamentos y niveles de cargo. El gráfico de barras permite observar diferencias de promedios y el diagrama de caja muestra rangos y posibles casos atípicos. No eliminamos automáticamente salarios altos porque podrían ser válidos. Tampoco interpretamos que un departamento cause diferencias salariales.",
"La matriz de correlaciones es una herramienta exploratoria. En nuestros datos, el nivel de cargo tiene una correlación aproximada de cero coma sesenta y nueve con el salario. La experiencia muestra cerca de cero coma cincuenta y ocho. Estas relaciones orientan nuestras hipótesis, pero no demuestran causalidad.",
"Para la tercera etapa dividimos los datos en ochenta por ciento de entrenamiento y veinte por ciento de prueba. Transformamos las categorías y entrenamos una regresión lineal. Como comparación, construimos una línea base que siempre predice la mediana del conjunto de entrenamiento. Medimos errores usando datos reservados.",
"El modelo obtuvo un erre cuadrado de cero coma ochenta y seis en el conjunto de prueba. Su error absoluto medio fue de unos setecientos sesenta y cinco mil pesos, frente a más de dos millones en la línea base. También usamos validación cruzada para comprobar estabilidad. Estos resultados describen únicamente nuestra simulación.",
"La historia que cuentan los datos va de un problema a evidencias verificables. Primero inspeccionamos y limpiamos; después resumimos y comparamos; finalmente medimos una predicción. Profesionalmente propondríamos un tablero de análisis agregado para nómina, con datos autorizados de SAP, revisiones de calidad y supervisión humana.",
"Como conclusión, aprendimos que la ciencia de datos es mucho más que hacer gráficos o ejecutar un modelo. Debemos conocer el origen de la información, medir errores y comunicar límites. Los registros usados son ficticios: antes de una aplicación real se necesitan permisos, evaluaciones de sesgo y validación con especialistas. Gracias."
]

def run(cmd):subprocess.run(cmd,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)

def duration(fn):
 p=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(fn)],capture_output=True,text=True,check=True)
 return float(p.stdout.strip())

if __name__=='__main__':
 if not PDF.exists(): raise FileNotFoundError(PDF)
 run(['pdftoppm','-jpeg','-r','96',str(PDF),str(WORK/'slide')])
 lines=[];seg=[];dur_total=0
 for i,txt in enumerate(NARRACIONES,1):
  wav=WORK/f'audio_{i:02d}.wav';mp4=WORK/f'clip_{i:02d}.mp4'
  run(['espeak','-v','es','-s','141','-p','48','-a','165','-w',str(wav),txt])
  dur=duration(wav)+1.0
  img=WORK/f'slide-{i:02d}.jpg'
  assert img.exists(), img
  vf="scale=1280:720,drawbox=x=0:y=680:w=1280:h=40:color=black@0.8:t=fill,drawtext=text='VIDEO DEMOSTRATIVO - VOZ SINTETICA | GRABAR NARRACION DEL EQUIPO':fontcolor=white:fontsize=17:x=(w-text_w)/2:y=692,format=yuv420p"
  run(['ffmpeg','-y','-loglevel','error','-loop','1','-framerate','12','-i',str(img),'-i',str(wav),'-vf',vf,'-c:v','libx264','-preset','veryfast','-crf','30','-pix_fmt','yuv420p','-r','12','-c:a','aac','-b:a','96k','-t',f'{dur:.2f}','-shortest',str(mp4)])
  seg.append(mp4);dur_total+=duration(mp4)
  lines.append(f"### Diapositiva {i} · Presentador {'1' if i<=5 else '2'}\n\n{txt}\n")
 (OUT/'GUION_VIDEO_POR_INTEGRANTE.md').write_text('# Guion de grabación para el equipo\n\n**Importante:** el MP4 incluido tiene voz sintetizada como demostración. La consigna exige presentación original **realizada por 2 o 3 integrantes**; graben sus propias voces y sustituyan el video demostrativo antes de entregar.\n\nReparto sugerido: integrante 1, diapositivas 1 a 5; integrante 2, diapositivas 6 a 11. Si son tres, integrante 1: 1–4; integrante 2: 5–8; integrante 3: 9–11.\n\n'+ '\n'.join(lines),encoding='utf-8')
 concat=WORK/'clips.txt';concat.write_text(''.join("file '"+str(p)+"'\n" for p in seg))
 dst=OUT/'VIDEO_DEMOSTRATIVO_VOZ_SINTETICA.mp4'
 run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',str(concat),'-c','copy','-movflags','+faststart',str(dst)])
 print('Video terminado',dst,'duración',round(duration(dst),1),'segundos,',round(duration(dst)/60,2),'minutos')
