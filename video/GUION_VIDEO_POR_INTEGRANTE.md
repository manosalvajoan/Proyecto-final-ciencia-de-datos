# Guion individual · Sebastián Manosalva Fonseca

**Presentador informado:** Sebastián Manosalva Fonseca. El video incluido con voz sintética es una demostración, no la grabación requerida. Expón personalmente entre 2 y 5 minutos, mostrando las tres etapas, código y resultados. **El profesor debe autorizar expresamente una entrega individual**, ya que la consigna requiere 2 o 3 integrantes.

### Diapositiva 1 · Sebastián

Hola, soy Sebastián Manosalva Fonseca. En este proyecto estudio la distribución de salarios de una organización simulada y construimos una regresión lineal para estimarlos. Nuestro recorrido integra limpieza, estadística y aprendizaje automático, siempre destacando los límites de los resultados.

### Diapositiva 2 · Sebastián

El punto de partida es una pregunta práctica: ¿qué variables se relacionan con los salarios? Un área de Talento Humano puede necesitar respuestas para planificar su presupuesto. Sin embargo, no pretendemos determinar el sueldo justo de una persona ni automatizar decisiones individuales.

### Diapositiva 3 · Sebastián

En la primera etapa diseñamos un conjunto ficticio y reproducible de mil quinientas catorce filas con doce columnas. Incluye salario, experiencia, antigüedad, nivel de cargo y otras características. Elegimos este escenario porque conecta la ingeniería de sistemas con análisis de datos de nómina, sin divulgar información confidencial.

### Diapositiva 4 · Sebastián

La exploración detectó catorce registros duplicados y dieciséis filas con errores de edad o de salario. Después de eliminarlos conservamos mil cuatrocientos ochenta y cuatro registros. También normalizamos nombres de departamentos, tratamos datos faltantes y verificamos la consistencia. Dejamos documentadas todas estas reglas de limpieza.

### Diapositiva 5 · Sebastián

En la segunda etapa usamos estadística descriptiva. El salario mensual promedio simulado fue aproximadamente seis millones cuatrocientos mil pesos, mientras la mediana fue cercana a seis millones doscientos mil. El histograma muestra la forma de la distribución y nos recuerda que el promedio no representa exactamente a cada empleado.

### Diapositiva 6 · Sebastián

Luego comparamos departamentos y niveles de cargo. El gráfico de barras permite observar diferencias de promedios y el diagrama de caja muestra rangos y posibles casos atípicos. No eliminamos automáticamente salarios altos porque podrían ser válidos. Tampoco interpretamos que un departamento cause diferencias salariales.

### Diapositiva 7 · Sebastián

La matriz de correlaciones es una herramienta exploratoria. En nuestros datos, el nivel de cargo tiene una correlación aproximada de cero coma sesenta y nueve con el salario. La experiencia muestra cerca de cero coma cincuenta y ocho. Estas relaciones orientan nuestras hipótesis, pero no demuestran causalidad.

### Diapositiva 8 · Sebastián

Para la tercera etapa dividimos los datos en ochenta por ciento de entrenamiento y veinte por ciento de prueba. Transformamos las categorías y entrenamos una regresión lineal. Como comparación, construimos una línea base que siempre predice la mediana del conjunto de entrenamiento. Medimos errores usando datos reservados.

### Diapositiva 9 · Sebastián

El modelo obtuvo un erre cuadrado de cero coma ochenta y seis en el conjunto de prueba. Su error absoluto medio fue de unos setecientos sesenta y cinco mil pesos, frente a más de dos millones en la línea base. También usamos validación cruzada para comprobar estabilidad. Estos resultados describen únicamente nuestra simulación.

### Diapositiva 10 · Sebastián

La historia que cuentan los datos va de un problema a evidencias verificables. Primero inspeccionamos y limpiamos; después resumimos y comparamos; finalmente medimos una predicción. Profesionalmente propondríamos un tablero de análisis agregado para nómina, con datos autorizados de SAP, revisiones de calidad y supervisión humana.

### Diapositiva 11 · Sebastián

Como conclusión, aprendimos que la ciencia de datos es mucho más que hacer gráficos o ejecutar un modelo. Debemos conocer el origen de la información, medir errores y comunicar límites. Los registros usados son ficticios: antes de una aplicación real se necesitan permisos, evaluaciones de sesgo y validación con especialistas. Gracias.
