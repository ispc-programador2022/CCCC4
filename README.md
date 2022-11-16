![image](https://user-images.githubusercontent.com/101228469/172445821-245dee9a-7c37-4f00-97b4-7c03965467f3.png)
# BIENVENIDOS AL GRUPO CCCC4 - AULA 4 - COHORTE 2022
## TECNICATURA EN CIENCIAS DE DATOS E INTELIGENCIA ARTIFICIAL
## PROYECTO TECNOLÓGICO INTEGRADOR 2022 - PROYECTO GAMA

### Colaboradores 
- [Chacon Claudio Gabriel](https://github.com/cchaconispc)
- [Contreras Carla Daniela](https://github.com/krla2022)
- [Cordoba Marcelo Gustavo](https://github.com/MarceloGustavoCordoba)
- [Cuestas Natalia Noemi](https://github.com/nataliacuestas20)               

# Tema a desarrolar:
## ⚽⚽⚽Mundial Qatar 20222⚽⚽⚽
![image](https://www.jumpdesign.co.uk/wp-content/uploads/2021/02/BANNER-LOGO.jpg)
<br></br>
## Librerias Utilizadas

### -[bs4 BeatifulSoup](https://pypi.org/project/beautifulsoup4/)
### -[Requests](https://pypi.org/project/requests/)
### -[Pandas](https://pypi.org/project/pandas/)
### -[Pathlib](https://docs.python.org/3/library/pathlib.html)
### -[Mysql-connector](https://pypi.org/project/mysql-connector-python)
### -[PySide6](https://pypi.org/project/PySide6/)
### - HTML
### - CSS

<br></br>

## Desarrollo del Proyecto:
Mediante la técnica de Web Scraping se extrajeron datos de diferentes páginas web relacionadas al Mundial Qatar 2022
<br></br>
Paginas utilizadas:
<br></br>
-https://www.goal.com/es-ar/noticias/boletos-mundial-qatar-2022-cuanto-cuestan-donde-comprar/xh01er94xekk1i4erzse4gndf
<br></br>
-https://www.transfermarkt.com.ar/argentina/kader/verein/3437/saison_id/2022/plus/1
<br></br>
-https://www.transfermarkt.com.ar/statistik/weltrangliste
<br></br>
-https://www.goal.com/es-ar/noticias/el-fixture-del-mundial-qatar-2022/bltdf3aa8843cf52580
<br></br>
-https://datosmacro.expansion.com/demografia/poblacion
<br></br>
-https://www.transfermarkt.com.ar
<br></br>
-https://www.fansapp.net/world-cup-tickets.html

## El objetivo era recopilar datos como:
•	Valor de entradas generales y de reventa con apertura por partidos
•	Fixture 
•	Información detallada de cada uno de los jugadores de cada selección
•	Valor de Mercado de los jugadores
•	Datos de demografía y población de los países participantes
<br></br>
Una vez realizada la extracción de datos se exportan a csv, para luego crear la base de datos en SQL donde se realiza la unificación de la información.
Para el  informe se utilizó PowerBI para la confección de los Dashboards interactivos comparando los diferentes datos recolectados.
<br></br>
Como valor agregado creamos:
<br></br>
•	Una aplicación ejecutable con Python la cual nos muestra un conteo regresivo para el inicio del Mundial.
<br></br>
•	Una Pagina Web con HTML y CSS donde se pueden visualizar nuestro trabajo realizado
<br></br>
Nuestro Proyecto fue llevado a cabo de manera colaborativa en la plataforma Trello para la gestión del mismo y flujo de trabajo cada uno con el rol que se le fue asignado:
<br></br>
## Chacon Claudio Gabriel: Administrador de Base de Datos (DBA)
## Contreras Carla Daniela: Web Scraper
## Cordoba Marcelo Gustavo: Analista Power BI
## Cuestas Natalia Noemi: Scrum Master (SM)
<br></br>
Link de descarga de ejecutable Aplicación Contador:
<br></br>
Link Página Web: 


<br></br>
# Consignas

<br></br>
### OBJETIVO
#### El objetivo principal del Proyecto Tecnológico Integrador es que puedan vivenciar una experiencia real de trabajo colaborativo en Ciencia de Datos, en un entorno Ágil.
#### Por eso además del trabajo en equipo y lo aprendido durante la cursada del presente año en los diferentes espacios curriculares, es fundamental la investigación, la creatividad y el aprovechamiento de los diferentes perfiles que hay en cada grupo para alcanzar el éxito de esta experiencia.

<br></br>
### ANTES DE COMENZAR
#### Les sugerimos que lean muy bien las consignas, investiguen sobre el material adicional y sobre todo, busquen información que les sea de utilidad para llevarlo adelante, de igual manera aprovechen de compartir, no solo las dudas, si no los avances dentro y fuera de los grupos que están realizando el Proyecto Integrador.
#### Como podrán ver en la estructura del proyecto, hay una serie de documentos/hitos a cumplimentar/cumplir, en un plazo acotado, les sugerimos que dividan las actividades y no permitan que el atraso en alguna consigna, frene las presentaciones de las restantes.
<br></br>
### FUNDAMENTACIÓN
#### Una tarea habitual en Ciencia de Datos es obtener datos de múltiples fuentes. 
#### Una de estas técnicas suele ser el “Scraping”, el cual permite obtener datos de páginas web para manipularlas desde la aplicación desarrollada.
#### El web scraping es una técnica que permite extraer datos e información de una web. 
#### Recomendamos que realicen el web scraping con Python, utilizando para ello la librería Beautiful Soup.
<br></br>
### PROYECTO
#### La consigna consiste en desarrollar una aplicación en Python, que tome los datos de alguna ó algunas páginas web, haciendo Web Scraping, guardando los datos recolectados en una base de datos.
#### Luego hacer una aplicación que muestre los datos almacenados, pero que también permita manipular los mismos.
#### Por último, con dicha información, realizar un informe. Este informe puede ser simple a través de la comparación entre elementos recolectados de las diferentes fuentes, estadísticos sobre las series de los datos o cualquier tipo de análisis del tipo Big Data o Machine Learning, como regresiones, proyecciones, etc.
<br></br>
### EJEMPLO
#### Solo a los fines de proponer un ejemplo que amplíe la consigna, imaginemos que tomamos páginas como [investpy 1.0.8](https://pypi.org/project/investpy/) ó [Yahoo! Finance "Telefónica, S.A. (TEF)"](https://es.finance.yahoo.com/quote/TEF?p=TEF&.tsrc=fin-srch) ó [Bolsa de Madrid](https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000) ó de Gobiernos Abiertos.
#### Como bien sabemos las páginas web son documentos estructurados formados por una jerarquía de elementos. Así que luego de elegir la página, el siguiente paso consiste en identificar correctamente el elemento o elementos que contienen la información deseada.
#### Luego hay que descargar el contenido de la página utilizando la librería requests.
#### El contenido de la página obtenido en el paso anterior será el que utilicemos para crear la «sopa», esto es, el árbol de objetos Python que representan al documento HTML.
#### Ahora estamos en condiciones de buscar en el árbol y obtener los objetos que contienen la información y datos que necesitamos.
#### Una vez obtenidos los datos los guardarán en una base de datos. La cual permitirá manipular los mismos haciendo modificaciones o eliminando registros.
#### Por último, realizar algún informe.
<br></br>
### GESTIÓN DEL PROYECTO
#### La gestión del proyecto se llevará adelante, con las herramientas utilizadas, por lo tanto, tendrán que crear un repositorio público en GitHub con el nombre del grupo, dentro del https://github.com/ispc-programador2022/. En el mismo subirán los documentos de trabajo, enlaces con documentación utilizada para encaminar el proyecto, más los códigos y las bases utilizadas.
#### De igual manera crearán un tablero en Trello, con acceso para ispc.programador2022@gmail.com en donde compartirán como van trabajando e interactuando entre Uds.
<br></br>
### ENTREGABLES Y PLAZOS
#### Los entregables y plazos del proyecto son los siguientes
- #### i) Documento de KickOff del proyecto. El mismo se ira completando sobre el siguiente [documento colaborativo](https://docs.google.com/spreadsheets/d/13yc5EIMPd_KinnN1uaM0laSg48Qzvu3a1bEMR1rchpM/edit?usp=sharing) y las tres columnas principales (Nombre del Grupo, Tema a desarrollar y Pagina Web Origen de Datos) tienen que estar completas por el equipo antes del 26/10/22.
- #### ii) Ejecución del Proyecto. Esto hace referencia a la codificación del WebScrapping, las bases de datos, los informes y el documento que contenga el resumen del proyecto. Y tiene que estar finalizado antes del 16/11/22.
- #### iii) Presentación del proyecto. Consiste en la realización de un video o grabación de un meet interno del equipo de proyecto, con una duración no mayor a 15 minutos, en donde el equipo presente los resultados obtenidos y comenten sobre el proceso de ejecución del proyecto. Esto tiene que ser presentado antes del 23/11/22.
- #### iv) Cabe aclarar que cada una de estas etapas y generación de estos documentos, tiene que ser cargado en el documento de KickOff. El que también es un desafío, puesto al ser colaborativo sirve no solo para que todos los equipos estén al corriente del avance de los otros equipos, si no que quien lo edita para agregar información debe ser muy cuidadoso y respetuoso para que no se vaya a perder información de ningún otro equipo compañero.
<br></br>
### RUBRICA
#### A continuación, les compartimos un cuadro, que será tenido en cuenta para la valoración final de cada uno de los proyectos. Como podrán ver en el mismo, hay competencias que se complementan y otras que no se acumulan, por tal motivo es muy importante que, si alguna actividad no la llegan a cumplimentar en tiempo y/o forma, no dejen de presentar el resto.

![imagen](https://user-images.githubusercontent.com/105946879/197096166-04e7cdb6-8480-4bbd-bd58-e7ca2cc6ceea.png)

<br></br>
### MATERIAL DE SOPORTE
#### Como el proceso es autogestionado y el equipo docente no estará disponible para guiarlos en temas puntuales, es fundamental que vean todo el material de referencia que les dejamos a continuación, lo mismo que los invitamos a que busquen Uds. todo lo que necesiten en bibliotecas educativas y la web en su conjunto, para llevar el proyecto adelante.
#### - [Github](https://youtu.be/eQMcIGVc8N0)
#### - [Web Scrapping](https://j2logo.com/python/web-scraping-con-python-guia-inicio-beautifulsoup/)
#### - [Web Scraping con Python, utilizando para ello la librería Beautiful Soup 1](https://youtu.be/kPNHKrOqedI)
#### - [Web Scraping con Python, utilizando para ello la librería Beautiful Soup 2](https://youtu.be/SuwCyiCLe8Y) (ejercicio scraping, comienza minuto 35 - muy importante minuto 55 a 1:05)
#### - [Html - etiquetas básicas](https://youtu.be/RafelMz450g)
#### - [Kagle](https://youtu.be/NhHTWGIglRI)
#### - [Conexión a BBDD desde Python - MySql y MongoDB 1](https://github.com/narcisoperez/21SemanaProgramacion_210521)
#### - [Conexión a BBDD desde Python - MySql y MongoDB 2](https://github.com/narcisoperez/7SemanaBasedeDatos_300621)
#### - [Conexión a BBDD desde Python - MySql y MongoDB 3](https://github.com/narcisoperez/8vaSemanaBase_de_Datos_070721)
#### - [BD MySQL Phyton](https://youtu.be/Ch7xsRmaJCs)
<br></br>
### BIBLIOTECA DEL PROYECTO
#### Como todo proyecto colaborativo, buscamos fortalecernos e incrementar nuestras competencias entre todos y por ese motivo, los invito a que en conjunto vayamos creando la [biblioteca del proyecto](https://docs.google.com/spreadsheets/d/1ofo1QjRsTy0m038SJyxAdGpgdsNBCDDNBkpg5slrEug/edit?usp=sharing), es decir cada que un equipo encuentra un documento, código o video que consideren les ha resultado de interés para llevar adelante el proyecto, lo compartiremos en el siguiente documento colaborativo
<br></br>
