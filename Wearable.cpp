Codigo en arduino:
#include <Wire.h>
#include <DFRobot_MAX30102.h> #include <Temperature_LM75_Derived.h> #include <ESP8266WiFi.h>
#include <PubSubClient.h>
DFRobot_MAX30102 particleSensor;
WiFiClient espClient; PubSubClient client(espClient);

// Definición de constantes
const char* SSID = "RC8766";
const char* PASSWORD = "123456789";
const char* MQTT_SERVER = "192.168.137.1"; const char* CLIENT_ID = "ESP8266-2";
const int MQTT_BROKER_PORT = 1883;
const char* topic_heartrate = "Pulso";
const char* topic_spo2 = "Oxigenacion";
const char* topic_temperature = "Temperatura"; const char* topic_mq7 = "MQ7";
int _ADDR = 0x70; // Dirección I2C del multiplexor PCA9548A
int MAX30102_CHANNEL = 0; // Canal del MAX30102 en el multiplexor int LM75B_CHANNEL = 1; // Canal del LM75B en el multiplexor
Generic_LM75 temperature(0x48); // Sensor de temperatura LM75B en la dirección 0x48

// Definición de una estructura para almacenar datos del MAX30102 typedef struct
{
const char* topic; int32_t value; int8_t isValid;
} MAX30102Data;
MAX30102Data heartrate = {"heartrate", 0, 0}; MAX30102Data spo2 = {"spo2", 0, 0};
void setup() { Serial.begin(115200); Wire.begin();
// Configuración del PCA9548A para seleccionar el canal del MAX30102 tcaselect(MAX30102_CHANNEL);
while (!particleSensor.begin()) { Serial.println("MAX30102 was not found"); delay(1000);
}
// Configuración del sensor MAX30102
particleSensor.sensorConfiguration(96, SAMPLERATE_100, PULSEWIDTH_411, ADCRANGE_16384);
MODE_MULTILED,
// Configuración del PCA9548A para seleccionar el canal del LM75B tcaselect(LM75B_CHANNEL);
setup_wifi(); // Configuración de la conexión WiFi client.setServer(MQTT_SERVER, 1883); // Configuración del cliente MQTT
}
void loop() {
// Selecciona el canal del multiplexor para el MAX30102 tcaselect(MAX30102_CHANNEL);
// Realiza la lectura del MAX30102
particleSensor.heartrateAndOxygenSaturation(&spo2.value, &spo2.isValid, &heartrate.value, &heartrate.isValid);
// Publica los resultados en los temas MQTT correspondientes publishToMQTT(topic_heartrate, heartrate.value); publishToMQTT(topic_spo2, spo2.value);
// Selecciona el canal del multiplexor para el LM75B tcaselect(LM75B_CHANNEL);
// Lee datos de temperatura
float tempC = temperature.readTemperatureC(); publishToMQTT(topic_temperature, static_cast<int32_t>(tempC));
// Lee datos del sensor MQ7 en el pin A0 int mq7Value = analogRead(A0); publishToMQTT(topic_mq7, mq7Value);
delay(1000); // Agrega un retardo para controlar la frecuencia de las lecturas. }
// Función para seleccionar el canal del multiplexor PCA9548A void tcaselect(uint8_t i2c_bus) {
if (i2c_bus > 7) return; Wire.beginTransmission(_ADDR);
Wire.write(1 << i2c_bus); Wire.endTransmission();
delay(100); // Añadir un pequeño tiempo de espera
}
// Función para publicar datos en un tema MQTT
void publishToMQTT(const char* topic, int32_t value) { if (!client.connected()) {
reconnect(); }
if (!client.loop()) { client.connect(CLIENT_ID);
}
char payload[10];
snprintf(payload, sizeof(payload), "%ld", value); client.publish(topic, payload); Serial.print("Payload: ");
Serial.print(payload);
Serial.print(", published to: "); Serial.print(topic);
Serial.println(" MQTT topic.");
}
// Función para configurar la conexión WiFi void setup_wifi() {
delay(10);
Serial.println();
Serial.print("Connecting to "); Serial.println(SSID);
WiFi.begin(SSID, PASSWORD);
while (WiFi.status() != WL_CONNECTED) {
delay(500);
Serial.print("."); }
Serial.println("");
Serial.print("WiFi connected - ESP IP address: "); Serial.println(WiFi.localIP());

// Función para reconectar al servidor MQTT
void reconnect() {
while (!client.connected()) {
Serial.print("Attempting MQTT connection..."); if (client.connect(CLIENT_ID)) {
Serial.println("connected"); } else {
Serial.print("MQTT connection failed, rc="); Serial.print(client.state());
Serial.println(" try again in 5 seconds"); delay(5000);
} }
}