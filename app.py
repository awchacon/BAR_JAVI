import streamlit as st
import base64
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="EL RIBEIRIÑO", page_icon="static/images/logo.png", layout="centered")

# Cargar el archivo CSS
def load_css():
    with open("static/styles/styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

# Título principal
st.markdown("<h1 class='center-text'>EL RIBEIRIÑO</h1>", unsafe_allow_html=True)
st.write("")

# Menú de opciones
selected = st.selectbox(
    "Menú",
    ["Inicio", "Para Compartir", "Platos Especiales", "Combinados", "Cocteles", "Contacto"]
)

# Función HomePage
def HomePage():
    col1, col2, col3 = st.columns(3)
    
    with col1:
        file_es = open("static/images/Flag_España.png", "rb")
        contents_es = file_es.read()
        data_url_es = base64.b64encode(contents_es).decode("utf-8")
        file_es.close()
        st.markdown(f'<div class="center-content"><img src="data:image/png;base64,{data_url_es}" alt="Flag España"></div>', unsafe_allow_html=True)
        
    with col2:
        file_pt = open("static/images/Flag_Dominican_Republic.png", "rb")
        contents_pt = file_pt.read()
        data_url_pt = base64.b64encode(contents_pt).decode("utf-8")
        file_pt.close()
        st.markdown(f'<div class="center-content"><img src="data:image/png;base64,{data_url_pt}" alt="Flag RD"></div>', unsafe_allow_html=True)
        
    with col3:
        file_br = open("static/images/Flag_of_Italy.png", "rb")
        contents_br = file_br.read()
        data_url_br = base64.b64encode(contents_br).decode("utf-8")
        file_br.close()
        st.markdown(f'<div class="center-content"><img src="data:image/png;base64,{data_url_br}" alt="Flag Italy"></div>', unsafe_allow_html=True)
    
    st.markdown("<h2 class='center-text'>¡Bienvenidos al Bar Ribeiriño!</h2>", unsafe_allow_html=True)
    st.markdown("<p class='center-text'>Disfruta de nuestros deliciosos platos y bebidas en un ambiente acogedor.</p>", unsafe_allow_html=True)

# Función para mostrar la carta
def para_compartir():
    image = Image.open("static/images/para_compartir.jpg")
    st.image(image, caption='Menú para compartir ', use_column_width=True)

# Función para mostrar los platos especiales
def PlatosEspeciales():
    image = Image.open("static/images/todo.jpg")
    st.image(image, caption='Menú platos Especiales', use_column_width=True)

def Combinados():
    image = Image.open("static/images/combinados.jpg")
    st.image(image, caption='Menú platos combinados', use_column_width=True)

def Cocteles():
    image = Image.open("static/images/cocteles.jpg")
    st.image(image, caption='Cócteles', use_column_width=True)    

# Función para mostrar la información de contacto
def Contacto():
    st.header("Contacto")
    st.write("📞 Teléfono: 606720892")
    st.write("📍 Dirección: C. de la Isla de Rodas, 4, Fuencarral-El Pardo, 28034 Madrid")
    st.markdown("<a href='https://g.co/kgs/ffq7gLk' target='_blank'>Ubicación en Google Maps</a>", unsafe_allow_html=True)
    st.write("📧 Email: fabioladerek_0709@icloud.com")
    st.markdown("""
        <div class="footer">
            <div class="social-icons">
                <p>
                    <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/Tiktok-logo.png" alt="TikTok" title="TikTok" width="20" height="20">
                    Síguenos en <a href="https://www.tiktok.com/@el_rinconcito_de_colasa?_t=8o9TbJPQtPN&_r=1" target="_blank">TikTok</a>
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Navegación entre las opciones del menú
if selected == "Inicio":
    HomePage()

if selected == "Para Compartir":
    para_compartir()

if selected == "Platos Especiales":
    PlatosEspeciales()

if selected == "Combinados":
    Combinados()

if selected == "Cocteles":
    Cocteles()

if selected == "Contacto":
    Contacto()
