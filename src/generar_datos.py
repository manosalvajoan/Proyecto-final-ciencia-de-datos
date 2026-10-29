"""Generador de datos de nómina ficticios, reproducibles y sin información personal.
Uso: python src/generar_datos.py
Este dataset NO es una extracción de SAP, IBM ni una muestra representativa de Colombia.
"""
from pathlib import Path
import numpy as np
import pandas as pd

SEMILLA = 202611

def generar(n=1500, semilla=SEMILLA):
    rng = np.random.default_rng(semilla)
    nivel = rng.choice([1,2,3,4,5], n, p=[.20,.32,.27,.16,.05])
    edad = rng.integers(21, 62, n)
    exp = np.maximum(0, edad - 20 - rng.integers(0,14, n)).astype(float)
    antig = np.minimum(exp, rng.integers(0,17,n)).astype(float)
    dept = rng.choice(['Tecnología','Operaciones','Finanzas','Comercial','Talento Humano'],n,p=[.30,.27,.16,.16,.11]).astype(object)
    educ = rng.choice(['Bachillerato','Técnico','Profesional','Especialización','Maestría'], n, p=[.13,.20,.39,.20,.08]).astype(object)
    ciudad = rng.choice(['Bogotá','Medellín','Cali','Barranquilla'], n, p=[.55,.22,.15,.08]).astype(object)
    modalidad = rng.choice(['Presencial','Híbrida','Remota'], n, p=[.45,.35,.20]).astype(object)
    extras = rng.poisson(4.8,n).clip(0,22)
    satisf = rng.choice([1,2,3,4,5],n,p=[.05,.13,.26,.38,.18])
    nivel_eff = np.select([nivel==1,nivel==2,nivel==3,nivel==4,nivel==5], [350000,1250000,2500000,4400000,7100000])
    dept_eff = pd.Series(dept).map({'Tecnología':700000,'Operaciones':-100000,'Finanzas':500000,'Comercial':250000,'Talento Humano':0}).to_numpy()
    educ_eff = pd.Series(educ).map({'Bachillerato':-300000,'Técnico':-100000,'Profesional':150000,'Especialización':450000,'Maestría':750000}).to_numpy()
    city_eff = pd.Series(ciudad).map({'Bogotá':250000,'Medellín':180000,'Cali':0,'Barranquilla':-100000}).to_numpy()
    salario = 1450000 + nivel_eff + exp*120000 + antig*33000 + dept_eff + educ_eff + city_eff + extras*16000 + rng.normal(0,840000,n)
    salario = np.round(np.maximum(salario, 1300000)/1000)*1000
    df=pd.DataFrame({'EmpleadoID':np.arange(100001,100001+n), 'Edad':edad, 'Departamento':dept,
                     'NivelCargo':nivel, 'ExperienciaAnios':exp, 'AntiguedadAnios':antig,
                     'NivelEducativo':educ,'Ciudad':ciudad,'ModalidadTrabajo':modalidad,
                     'HorasExtraMes':extras,'SatisfaccionLaboral':satisf,'SalarioMensualCOP':salario})
    # Problemas creados deliberadamente para documentar limpieza en la etapa 1.
    for c,k in [('NivelEducativo',22),('Departamento',11),('ExperienciaAnios',14),('SalarioMensualCOP',8)]:
        indices=rng.choice(df.index,k,replace=False)
        df.loc[indices,c]=np.nan
    df.loc[[11,85,143],'Edad']=[15,16,90]
    df.loc[[48,219],'SalarioMensualCOP']=[-300000,0]
    df.loc[[320,601,803],'SalarioMensualCOP']=[99000000,99000000,99000000]
    df.loc[[408,509],'ExperienciaAnios']=[-5,-2]
    df.loc[20:35,'Departamento']=' tecnologia '
    df.loc[36:48,'Departamento']='TALENTO HUMANO'
    df.loc[49:61,'Departamento']='operaciones'
    df.loc[62:73,'ModalidadTrabajo']='remota '
    df.loc[76:85,'Ciudad']='bogota'
    df=pd.concat([df, df.sample(n=14, random_state=semilla)], ignore_index=True)
    return df

if __name__=='__main__':
    output=Path(__file__).resolve().parents[1]/'datos'/'empleados_original.csv'
    df=generar()
    output.parent.mkdir(parents=True,exist_ok=True)
    df.to_csv(output,index=False,encoding='utf-8-sig')
    print('Dataset original creado:', output, 'filas:',len(df),'columnas:',len(df.columns))
