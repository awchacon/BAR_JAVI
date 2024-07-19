import streamlit as st
import base64
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Bar Ribeiriño", page_icon="static/images/logo.png", layout="centered")

# Cargar el archivo CSS
def load_css():
    with open("static/styles/styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

# Título principal
st.markdown("<h1 class='center-text'>Bar Ribeiriño</h1>", unsafe_allow_html=True)
st.write("")

# Menú de opciones
selected = st.selectbox(
    "Menú",
    ["Inicio", "Carta", "Platos Especiales", "Contacto"]
)

# Función HomePage
def HomePage():
    file_ = open("static/images/bar_gif.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
        f'<div class="centered-content"><img src="data:image/gif;base64,{data_url}" alt="main gif"></div>',
        unsafe_allow_html=True,
    )
    st.markdown("<h2 class='center-text'>¡Bienvenidos al Bar Ribeiriño!</h2>", unsafe_allow_html=True)
    st.write("Disfruta de nuestros deliciosos platos y bebidas en un ambiente acogedor.")

# Función para mostrar la carta
def Carta():
    st.header("Nuestra Carta")
    image = Image.open('static/images/menu.jpg')
    st.image(image, caption='Menú del Bar', use_column_width=True)

# Función para mostrar los platos especiales
def PlatosEspeciales():
    st.header("Platos Especiales")
    image = Image.open('static/images/menu.jpg')
    st.image(image, caption='Platos Especiales', use_column_width=True)

# Función para mostrar la información de contacto
def Contacto():
    st.header("Contacto")
    st.write("📍 Dirección: Calle del Bar, 123, Ciudad")
    st.write("📞 Teléfono: +34 123 456 789")
    st.write("📧 Email: contacto@barribeirinho.com")
    st.markdown("""
        <div class="footer">
            <div class="social-icons">
                <p>
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Instagram_logo_2022.svg/1200px-Instagram_logo_2022.svg.png" alt="Instagram" title="Instagram">
                    Síguenos en <a href="url_de_tu_perfil_de_instagram" target="_blank">Instagram</a>
                </p>
            </div>
            <div class="social-icons">
                <p>
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/2021_Facebook_icon.svg/220px-2021_Facebook_icon.svg.png" alt="Facebook" title="Facebook">
                    Síguenos en <a href="url_de_tu_perfil_de_facebook" target="_blank">Facebook</a>
                </p>
            </div>
            <div class="social-icons">
                <p>
                    <img src="https://store-images.s-microsoft.com/image/apps.31120.9007199266245564.44dc7699-748d-4c34-ba5e-d04eb48f7960.bc4172bd-63f0-455a-9acd-5457f44e4473" alt="LinkedIn" title="LinkedIn">
                    Síguenos en <a href="url_de_tu_perfil_de_linkedin" target="_blank">LinkedIn</a>
                </p>
            </div>
            <p>Creador 🤖 por <a href="www.linkedin.com/in/aaron-chacon" target="_blank">Bar Ribeiriño</a></p>
        </div>
    """, unsafe_allow_html=True)

# Navegación entre las opciones del menú
if selected == "Inicio":
    HomePage()

if selected == "Carta":
    Carta()

if selected == "Platos Especiales":
    PlatosEspeciales()

if selected == "Contacto":
    Contacto()
