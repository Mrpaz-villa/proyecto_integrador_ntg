import streamlit as st
import paho.mqtt.client as mqtt

# Configuración de MQTT
broker = ""
port = ""
subscribe = ""
publish = ""
input_message = ""

try:
    # Crear una instancia del cliente MQTT
    client = mqtt.Client()

    # Callback para cuando el cliente se conecta al servidor MQTT
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe(subscribe)

    # Callback para cuando se recibe un mensaje MQTT
    def on_message(client, userdata, msg):
        global input_message
        value = "".join(chr(i) for i in msg.payload)
        input_message += value
        msj.text_area("Mensajes", input_message, 200)
        input_message += '\n'

    # Configurar los callbacks
    client.on_connect = on_connect
    client.on_message = on_message

    # Conectar al servidor MQTT
    client.connect(broker, 1883, 60)
except:
    pass

# Crear la base de datos si no existe
db.create_database()

# Obtener la configuración
setting = db.get_setting()

with st.expander("Configuración"):
    st.subheader("MQTT")
    broker = st.text_input('Broker', setting[0][1])
    port = st.text_input('Puerto', setting[0][2])
    subscribe = st.text_input('Tópico suscripción', setting[0][3])
    publish = st.text_input('Tópico publicación', setting[0][4])

if broker:
    db.update_broker(1, broker)
if port:
    db.update_port(1, port)
if subscribe:
    db.update_topic_subscriber(1, subscribe)
if publish:
    db.update_topic_publisher(1, publish)

msj = st.text("")
msj.text_area("Mensajes", "", 200)

text1 = st.empty()
value = text1.text_input("Enviar mensaje", value="", key="1")
if st.button("Enviar"):
    if value:
        client.publish(publish, subscribe + ":" + value)
        text1.text_input("Enviar mensaje", value="", key="2")

client.loop_forever()
