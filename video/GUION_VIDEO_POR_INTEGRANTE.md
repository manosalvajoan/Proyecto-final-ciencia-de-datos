# Guion de grabación para el equipo

**Importante:** el MP4 incluido tiene voz sintetizada como demostración. La consigna exige presentación original **realizada por 2 o 3 integrantes**; graben sus propias voces y sustituyan el video demostrativo antes de entregar.

Reparto sugerido: integrante 1, diapositivas 1 a 5; integrante 2, diapositivas 6 a 11. Si son tres, integrante 1: 1–4; integrante 2: 5–8; integrante 3: 9–11.

### Diapositiva 1 · Presentador 1

Hola. Somos el equipo de Ciencia de Datos. En este proyecto estudiamos la distribución de salarios de una organización simulada y construimos una regresión lineal para estimarlos. Nuestro recorrido integra limpieza, estadística y aprendizaje automático, siempre destacando los límites de los resultados.

### Diapositiva 2 · Presentador 1

El punto de partida es una pregunta práctica: ¿qué variables se relacionan con los salarios? Un área de Talento Humano puede necesitar respuestas para planificar su presupuesto. Sin embargo, no pretendemos determinar el sueldo justo de una persona ni automatizar decisiones individuales.

### Diapositiva 3 · Presentador 1

En la primera etapa diseñamos un conjunto ficticio y reproducible de mil quinientas catorce filas con doce columnas. Incluye salario, experiencia, antigüedad, nivel de cargo y otras características. Elegimos este escenario porque conecta la ingeniería de sistemas con análisis de datos de nómina, sin divulgar información confidencial.

### Diapositiva 4 · Presentador 1

La exploración detectó catorce registros duplicados y dieciséis filas con errores de edad o de salario. Después de eliminarlos conservamos mil cuatrocientos ochenta y cuatro registros. También normalizamos nombres de departamentos, tratamos datos faltantes y verificamos la consistencia. Dejamos documentadas todas estas reglas de limpieza.

### Diapositiva 5 · Presentador 1

En la segunda etapa usamos estadística descriptiva. El salario mensual promedio simulado fue aproximadamente seis millones cuatrocientos mil pesos, mientras la mediana fue cercana a seis millones doscientos mil. El histograma muestra la forma de la distribución y nos recuerda que el promedio no representa exactamente a cada empleado.

### Diapositiva 6 · Presentador 2

Luego comparamos departamentos y niveles de cargo. El gráfico de barras permite observar diferencias de promedios y el diagrama de caja muestra rangos y posibles casos atípicos. No eliminamos automáticamente salarios altos porque podrían ser válidos. Tampoco interpretamos que un departamento cause diferencias salariales.

### Diapositiva 7 · Presentador 2

La matriz de correlaciones es una herramienta exploratoria. En nuestros datos, el nivel de cargo tiene una correlación aproximada de cero coma sesenta y nueve con el salario. La experiencia muestra cerca de cero coma cincuenta y ocho. Estas relaciones orientan nuestras hipótesis, pero no demuestran causalidad.

### Diapositiva 8 · Presentador 2

Para la tercera etapa dividimos los datos en ochenta por ciento de entrenamiento y veinte por ciento de prueba. Transformamos las categorías y entrenamos una regresión lineal. Como comparación, construimos una línea base que siempre predice la mediana del conjunto de entrenamiento. Medimos errores usando datos reservados.

### Diapositiva 9 · Presentador 2

El modelo obtuvo un erre cuadrado de cero coma ochenta y seis en el conjunto de prueba. Su error absoluto medio fue de unos setecientos sesenta y cinco mil pesos, frente a más de dos millones en la línea base. También usamos validación cruzada para comprobar estabilidad. Estos resultados describen únicamente nuestra simulación.

### Diapositiva 10 · Presentador 2

La historia que cuentan los datos va de un problema a evidencias verificables. Primero inspeccionamos y limpiamos; después resumimos y comparamos; finalmente medimos una predicción. Profesionalmente propondríamos un tablero de análisis agregado para nómina, con datos autorizados de SAP, revisiones de calidad y supervisión humana.

### Diapositiva 11 · Presentador 2

Como conclusión, aprendimos que la ciencia de datos es mucho más que hacer gráficos o ejecutar un modelo. Debemos conocer el origen de la información, medir errores y comunicar límites. Los registros usados son ficticios: antes de una aplicación real se necesitan permisos, evaluaciones de sesgo y validación con especialistas. Gracias.
