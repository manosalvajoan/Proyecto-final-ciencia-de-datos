# Resumen ejecutivo y storytelling

**Pregunta:** ¿Cuáles variables se relacionan con salarios ficticios y cuál es la capacidad de una regresión lineal simple para estimarlos?

**Fase 1: confianza antes del cálculo.** Iniciamos con 1.514 filas de nómina ficticia: 14 duplicados exactos y 16 registros adicionales con edad o salario invalidado por el generador. Se analizaron finalmente 1.484 empleados sintéticos, con datos completos después del tratamiento y corrección de etiquetas.

**Fase 2: variación antes de predicción.** El salario medio fue 6.403.693 COP y el mediano 6.198.000 COP. La desviación estándar fue 2.471.449 COP. La correlación del nivel de cargo con el salario alcanzó 0,695 y la de experiencia 0,584. Se marcaron y conservaron 12 salarios atípicos de IQR. El departamento con mayor salario promedio fue Tecnología, aunque esa diferencia no es evidencia causal.

**Fase 3: predicción comprobada.** Sobre el conjunto de prueba de 297 filas, un modelo base que devuelve la mediana obtuvo MAE de 2.059.364 COP, frente a 764.628 COP de la regresión lineal. Su RMSE fue de 963.004 COP, y R²=0,8605 (aprox. 0,861). La validación cruzada obtuvo R² promedio de 0,841. **El modelo aprende un simulador artificial:** ese desempeño no prueba capacidad predictiva en salarios de empleados reales.

**Aplicación profesional:** propuesta de arquitectura de un tablero de calidad y planeación agregada de nómina, con información debidamente autorizada desde SAP HCM, controles de privacidad, transformación reproducible, evaluación del error y supervisión profesional. Este ejercicio no valida por sí mismo un uso real.

**Mensaje para recordar:** el flujo de ciencia de datos solo es confiable si comunica origen de la información, decisiones de limpieza, medición del error y límites éticos.
