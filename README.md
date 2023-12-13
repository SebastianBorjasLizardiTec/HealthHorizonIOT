# HealthHorizonIOT
IOT Wearable project
DESCRIPCIÓN:
La materia de salud en plantas industriales ha sido un tópico de explotación mayor en las
organizaciones mundiales de salud. En un estudio realizado por “Journal of environmental and public health” en 2013 titulado “A review of the epidemiological methods used to investigate the health impacts of air pollution around major industrial areas” Muestra una ejemplificación clara de una instancia negativa en la salud de los habitantes alrededor de plantas industriales.
“For instance, in the South of France, the industrial area of l’etang de Berre hosts 430 industries classified for the protection of the environment and more than 60% of the Seveso II (referring to the European directive 96/82/CE) plants of the region. About 16 towns representing more than 300,000 inhabitants are exposed to the plumes produced by these plants .” ( Pascal, M., Pascal, L., Bidondo, M. L., Cochet, A., Sarter, H., Stempfelet, M., Wagner, V. (2013). )
En el desarrollo de este proyecto buscamos integrar la tecnología del internet de las cosas para implementar un dispositivo que permita una metodología de estudio participativa con los trabajadores en plantas industriales con la convicción de recabar información numérica en una base de datos que pudiera ser interpretada en función de la salud de los empleados. Con este proyecto se busca estudiar la integración de distintas tecnologías con el fin de poder diseñar un proyecto que reúna los componentes utilizados en el desarrollo de las mismas para llegar a la solución real de un problema de la vida real. Siendo una pregunta detonante ¿Cómo podemos estudiar el impacto de salud en un trabajador industrial a medida de indicadores médicos con un dispositivo de tecnología computacional?. Creemos que el desarrollo de un wearable es una práctica convincente como solución a la problemática presentada puesto que la cercanía del
dispositivo con el usuario permite encontrar indicadores mayores sobre la salud del mismo. Y encontrando una base de datos diseñada con el fin de poder recabar estadística generalizada de la locación de los trabajadores o particular del usuario mismo, podemos facilitar la interpretación de los datos recabados.
![Screenshot 2023-12-13 at 1 42 15 p m](https://github.com/S0Borjas/HealthHorizonIOT/assets/153686142/d50fab32-7498-491c-a6b4-3b70339f1d47)
![Screenshot 2023-12-13 at 1 42 35 p m](https://github.com/S0Borjas/HealthHorizonIOT/assets/153686142/07098d6c-6c7b-460f-9ed6-c40c1dd9678c)
![Screenshot 2023-12-13 at 1 42 35 p m](https://github.com/S0Borjas/HealthHorizonIOT/assets/153686142/0e1fcc15-5e6b-401f-a27b-0c336385d6f0)
![Screenshot 2023-12-13 at 1 43 06 p m](https://github.com/S0Borjas/HealthHorizonIOT/assets/153686142/110306c9-3550-4083-9f60-30b9d8eec983)
Para la organización de nuestro proyecto utilizamos las herramientas Gantt y Trello:
![Screenshot 2023-12-13 at 1 43 35 p m](https://github.com/S0Borjas/HealthHorizonIOT/assets/153686142/077ea3d9-bba1-4d7e-af15-261dba3a89e4)
![Screenshot 2023-12-13 at 1 43 44 p m](https://github.com/S0Borjas/HealthHorizonIOT/assets/153686142/67432460-df4e-44ed-811d-0e85e7abc408)
Como se muestra en la imagen, en Trello añadimos dos tarjetas por cada una de las secciones del proyecto, una lista de cosas por hacer, y una de actividades completadas; cada vez que completamos una actividad, cambiamos el registro a la tarjeta donde. En la tarjeta DB implementamos las actividades de la base de datos. En la de Sensor todo lo relacionado con sensores, su conectividad y calibración. En la tarjeta Hardware está todo lo relacionado con la unión de los componentes del proyecto. Y en la tarjeta interfaz todo lo relacionado con la UI diseñada.
Existen actividades que no están puestas en Trello. Esto porque comenzamos a utilizar Trello después de haber comenzado el proyecto. Al tener una herramienta de organización como Gantt, no vimos la utilidad de Trello hasta que encontramos la necesidad de trabajar remotamente y llevar un registro de las actividades que iba haciendo el otro.

DIAGRAMA DE BLOQUES:
![Screenshot 2023-12-13 at 1 44 24 p m](https://github.com/S0Borjas/HealthHorizonIOT/assets/153686142/f186d792-2431-469f-be80-6c7a949fbcc5)

COMPONENTES:
Sensores:
MAX30102 - Oxigenación/Pulso LM75B - Temperatura
MQ7 - CO2
Multiplexor I2C: PCA9548A Microcontrolador: ESP8266

TECNOLOGÍAS USADAS:
HTML: Para el desarrollo general de la interfaz de usuario.
CSS: Dentro del código HTML utilizamos CSS para definir especificaciones de diseño. JavaScript: Dentro del mismo HTML definimos funciones goback( ) y navigate DataPage( ) para definir los botones de data y go back en la interacción de la página.
Jinja: Para generar URLs dinámicas dentro de la definición de imágenes y manejar la dirección de los datos de las imágenes con flash.
Flask: Marco de desarrollo para definir las rutas hacia las funciones de python y poder llamarlas desde el html y para renderizar las plantillas html. Para hacer una solicitud POST a un código en python que se encarga de generar las gráficas. Define el servidor y el puerto de desarrollo y maneja los parámetros de las funciones del código conecta.py que genera gráficas en png. MySQL: La base de datos fue creada utilizando mySQL con el usuario Root.
Draw.io: El diagrama entidad relación fue diseñado en esta plataforma.
phpMyAdmin: Utilizamos está interfaz para manejar y crear la base de datos física.
Arduino IDE: El editor de código que usamos para declarar y obtener las mediciones de los sensores fue Arduino IDE y las librerías que este tiene
Mosquitto: Utilizamos este servidor de mensajes MQTT para facilitar la comunicación entre diferentes dispositivos
Comunicación a través de la red: Para establecer comunicación a través de la red en nuestro proyecto, hemos integrado varias librerías. Una de ellas es ESP8266WiFi.h, que proporciona funciones y clases para la configuración y gestión de conexiones Wi-Fi en nuestro dispositivo ESP8266. Gracias a esta librería, logramos que nuestro dispositivo se conecte a redes Wi-Fi, adaptándose a diversos entornos y escenarios de uso.
Otra librería que utilizamos fue PubSubClient.h, diseñada para facilitar la comunicación mediante el protocolo MQTT. Este protocolo ofrece una solución eficiente para la transmisión de datos en entornos IoT, permitiendo la conexión a un servidor MQTT, la publicación de mensajes en topics específicos y la suscripción para recibir mensajes relevantes para nuestro sistema.
Es importante destacar que nuestro código Arduino se ejecuta en una computadora distinta a la que contiene la base de datos. Esta decisión se tomó debido a ciertos inconvenientes técnicos. En una de las computadoras, tuvimos problemas con el correcto funcionamiento de phpMyAdmin,. Mientras tanto, en la otra computadora, que es un dispositivo Apple, se presentaron limitaciones para compartir la conexión a Internet con el ESP8266.
La conexión de los dos dispositivos se logró mediante el uso de mosquitto, dejando de lado el programa de rednode proporcionado por nuestro profesor, eso debido a las limitaciones que mencionamos anteriormente

Resultados:
En Arduino obtuvimos las mediciones de los sensores

![Screenshot 2023-12-13 at 1 45 07 p m](https://github.com/S0Borjas/HealthHorizonIOT/assets/153686142/8c8de233-e447-495b-83ee-33891f1e3dd2)

Mientras que los resultados de las mediciones en el programa de mosquitto en las dos
computadoras que utilizamos dueron estos:

![Screenshot 2023-12-13 at 1 45 32 p m](https://github.com/S0Borjas/HealthHorizonIOT/assets/153686142/91891d16-8d01-4a8b-be53-9396452b499e)

LO QUE LOGRAMOS:

Con este proyecto logramos integrar diferentes tecnologías de la computación, desde sensores, hasta herramientas de diseño de interfaz para crear un producto competitivo en busca del desarrollo de un producto para la salud del trabajador industrial. Conseguimos crear un prototipo
  
de utilidad que fuera cómodo para el sujeto recabado de datos, conectar los componentes del mismo a una red externa, diseñar una base de datos para expresar las mediciones sensoriales del producto y desarrollar una herramienta de análisis de datos en una interfaz de usuario que fuera cómoda para el mismo, funcionando a su vez con el lenguaje de programación MySQL.
LO QUE NO LOGRAMOS:
No logramos la efectiva computación de un sensor de movimiento en el producto final. Este sensor tiene el objetivo de medir la actividad física del trabajador. No logramos una integración con la tecnología de red por problemas con la conectividad. No logramos integrar otro método de graficación interactiva con el usuario.
TRABAJO A FUTURO:
Creemos que con más tiempo de desarrollo este proyecto pudiera convertirse en una herramienta para el análisis correcto de la salud del trabajador en el área industrial. Pensamos que medir los indicadores de salud del cuerpo con tanta cercanía podría ayudar a la recabación de los datos de una manera más real que cualquier otro indicador. Concluimos entonces que el producto desarrollado, siendo el servicio de análisis de datos para la conciencia empresarial del consumidor fue efectiva, puesto que existe cada vez más un interés por apelar a la salud del trabajador por parte de las fábricas. Es verdad que las plantas industriales pierden más ingreso en la correcta estimulación de su sistema interno de salud que tiende a estar saturado por consecuencia de la incorrecta planificación de los componentes que afectan al trabajador, y por lo mismo que el proyecto podría funcionar como un valor agregado de alguna empresa que se dedique a la salud industrial. Sin embargo pensamos que como empresa individual, el costo del servicio tendría que ser lo suficientemente elevado para sustentar la mejora continua de la tecnología utilizada. Entonces concluimos que si una asociación individual intentará

implementar la empresa sería muy complicado mantener el desarrollo de la tecnología y las ventas de la misma mientras no están simbióticamente relacionadas con alguna otra corporación de salud que pudiera dar plataforma y validez al proyecto.
CONCLUSIONES DE EQUIPO:

El resultado de la investigación y desarrollo del proyecto fue efectivo para el aprendizaje de lo que es la integración del internet de las cosas con diferentes tecnologías. Creemos que teniendo la habilidad de crear productos inteligentes que puedan comunicarse con un desarrollo computacional extenso podemos encontrar inteligencia en la recabación de información y datos para crear servicios que le sean de utilidad a un usuario. Con el fin de demostrar la interconexión entre la parte razonable de un proyecto computacional y la parte física del mismo, hemos conseguido utilizar habilidades adquiridas durante las clases de este curso. Aprendimos que el diseño y desarrollo de planificación en abstracción como lo es la planificación de una base de datos y la utilización de un software de organización como Gantt es importante para plantar los cimientos de un proyecto bien estructurado. Aprendimos cómo funciona la relación entre los datos con modelos de entidades y relacionales. Aprendimos que dentro de la documentación de un producto de hardware podemos encontrar la información necesaria para la implementación del mismo.

CONCLUSIONES PERSONALES:

Sebastian Borjas: Este módulo me sirvió para entender las habilidades computacionales en las que no he logrado tener un desarrollo efectivo, como lo ha sido el hardware y la programación del mismo. Creo que en este ámbito puede complementar mis conocimientos con los de mi compañero. Me considero una persona competente en la planificación de arquitecturas de datos computacionales, de las cuales he aprendido más allá de lo indispensable. En la programación de
la interfaz de usuario tuve un error al comenzar con la interfaz antes de conseguir una planificación del flujo de datos correcto y un marco computacional adecuado para comunicarse con la base de datos. De esa forma aprendí que no solamente la planificación conceptual puede aportar al desarrollo de inteligencia, sino que también una visualización de la tecnología a utilizar es importante en la planeación del proyecto. Me he dado cuenta que el fuerte de mis capacidades habita dentro de mi capacidad para buscar una utilidad para el usuario y plantear las preguntas adecuadas para generar un proyecto atractivo.
Vicente Ramos:
A lo largo de estos dos períodos, he adquirido grandes conocimientos en el ámbito de la informática y las tecnologías, aprendiendo herramientas cruciales para abordar desafíos de la vida cotidiana. Esta experiencia me ha permitido no solo familiarizarme con diversas tecnologías de software y hardware, sino también comprender la aplicabilidad de estas en situaciones del mundo real. Además, durante este proceso de aprendizaje, he llegado a la conclusión de que existen múltiples enfoques para abordar proyectos complejos. Cada problema presenta oportunidades para la creatividad.
También aprendí a complementarme con mi equipo, puesto que los conocimientos que cada quien tenía fueron fundamentales en la creación del proyecto, siendo mi fuerte la resolución de problemas del hardware y la comunicación entre las dos computadoras sin dejar de lado la importancia del software.

