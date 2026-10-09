import streamlit as st

st.set_page_config(
    page_title="LMC",
    layout="wide"
)

# ==========================
# FONDO DE LA APLICACIÓN
# ==========================
st.markdown("""
<style>

.stApp{
    background-image:
        linear-gradient(
            rgba(0,0,0,0.85),
            rgba(0,0,0,0.85)
        ),
        url("https://i.ibb.co/HLB5SMWc/Fondo-para-aplicacion-integrada.png");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

.block-container{
    max-width:100% !important;
    min-height:95vh;
    display:flex;
    flex-direction:column;
    justify-content:space-between;
    padding-top:1rem;
    padding-left:3rem;
    padding-right:3rem;
    padding-bottom:1rem;
}

.titulo{
    text-align:center;
    color:white;
    font-size:40px;
    font-weight:700;
    margin-bottom:40px;
}

.card{
    background: rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.15);
    border-radius:25px;
    padding:25px;
    min-height:420px;
    backdrop-filter: blur(10px);
    box-shadow:0 8px 25px rgba(0,0,0,.35);
}

.card:hover{
    transform:translateY(-5px);
    transition:0.3s;
}

.footer{
    text-align:center;
    color:white;
    font-size:16px;
    font-weight:600;
    text-shadow:0px 0px 10px black;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

.stLinkButton a{
    background: linear-gradient(90deg,#00C8FF,#2563EB);
    color:white !important;
    border-radius:12px;
    font-size:20px !important;
    font-weight:bold;
    padding:14px 0px !important;
    min-height:60px !important;
}

.stLinkButton a:hover{
    transform:translateY(-3px);
    box-shadow:0px 5px 20px rgba(0,200,255,.4);
}

</style>
""", unsafe_allow_html=True)

# ==========================
# TITULO
# ==========================
st.markdown("""
<h1 style="
text-align:center;
color:white;
font-size:clamp(32px,3vw,55px);
font-weight:900;
text-shadow:0px 0px 25px #00C8FF;
margin-top:0px;
margin-bottom:30px;
">
🤖 APLICACIONES INTEGRADAS LMC
</h1>
""", unsafe_allow_html=True)

# ==========================
# COLUMNAS
# ==========================

col1, col2, col3 = st.columns(3, gap="large")

# ==========================
# TARJETA 1
# ==========================

with col1:
    st.markdown("""
    <div style="
        background: rgba(255,255,255,0.05);
        border:1px solid rgba(255,255,255,0.15);
        border-radius:20px;
        padding:25px;
        color:white;
        min-height:420px;
        box-shadow:0 8px 20px rgba(0,0,0,0.3);
    ">

    <h4 style="
    text-align:center;
    color:#00E5FF;
    font-size:clamp(22px,2vw,34px);
    font-weight:900;
    text-shadow:0px 0px 15px #00E5FF;
    ">
    EXAVAL LMC
    </h4>

    <hr>
    <p style="
    margin:0;
    font-size:18px;
    font-weight:bold;
    color:#FFFFFF;
    ">
    Credencial Principal <span style="color:#00E5FF;"></span>
    </p>
    
    <p style="
    margin:0;
    font-size:clamp(14px,1vw,18px);
    font-weight:bold;
    color:#FFFFFF;
    ">
    👤 Usuario: <span style="color:#00E5FF;">lcahuana</span>
    </p>
    
    <p style="
    margin:0;
    font-size:clamp(14px,1vw,18px);
    font-weight:bold;
    color:#FFFFFF;
    ">
    🔑 Contraseña: <span style="color:#00E5FF;">Lmc$%</span>
    </p>

    <h4 style="color:#00E5FF;">Módulos</h4>

    <ol style="
    font-size:clamp(15px,1vw,19px);
    font-weight:600;
    line-height:1.4;
    color:white;
    text-shadow:0px 0px 8px rgba(0,0,0,0.8);
    margin-bottom:10px;
    ">
        <li>📤 Expor Lect Rep v3.1</li>
        <li>📋 Asig Lect Rep v3.2</li>
        <li>📋 Asig Lect Rep v3.3</li>
        <li>🚀 Validar Reparto</li>
        <li>🚀 Validar Rep Prog</li>
    </ol>
    
    <div style="text-align:center;">
        <a href="https://www.youtube.com/playlist?list=PL4cQJ4fKEyHxRE5KBv8J9a_O5w9MNs0v8"
           target="_blank"
           style="
           display:inline-block;
           background:linear-gradient(90deg,#00C8FF,#2563EB);
           color:white;
           padding:8px 20px;
           border-radius:10px;
           text-decoration:none;
           font-weight:bold;
           font-size:clamp(14px,1vw,18px);
           box-shadow:0px 0px 10px rgba(0,200,255,.4);
           ">
           🎥 Ver Video
        </a>
    </div>

    </div>
    """, unsafe_allow_html=True)

# ==========================
# TARJETA 2
# ==========================

with col2:
    st.markdown("""
    <div style="
        background: rgba(255,255,255,0.05);
        border:1px solid rgba(255,255,255,0.15);
        border-radius:20px;
        padding:25px;
        color:white;
        min-height:420px;
        box-shadow:0 8px 20px rgba(0,0,0,0.3);
    ">

    <h4 style="
    text-align:center;
    color:#00E5FF;
    font-size:clamp(22px,2vw,34px);
    font-weight:900;
    text-shadow:0px 0px 15px #00E5FF;
    ">
    PLATAFORMA LMC
    </h4>

    <hr>
    <p style="
    margin:0;
    font-size:18px;
    font-weight:bold;
    color:#FFFFFF;
    ">
    Credencial Principal <span style="color:#00E5FF;"></span>
    </p>
    
    <p style="
    margin:0;
    font-size:clamp(14px,1vw,18px);
    font-weight:bold;
    color:#FFFFFF;
    ">
    👤 Usuario: <span style="color:#00E5FF;">lmc</span>
    </p>
    
    <p style="
    margin:0;
    font-size:clamp(14px,1vw,18px);
    font-weight:bold;
    color:#FFFFFF;
    ">
    🔑 Contraseña: <span style="color:#00E5FF;">Lmc$</span>
    </p>

    <h4 style="color:#00E5FF;">Módulos</h4>

    <ol style="
    font-size:clamp(15px,1vw,19px);
    font-weight:600;
    line-height:1.4;
    color:white;
    text-shadow:0px 0px 8px rgba(0,0,0,0.8);
    ">
        <li>📑Selfies Lect Rep Sheets</li>
        <li>📷Galería de Reparto</li>
        <li>📊Refacturados v3 99999</li>
        <li>⚡Riesgo Elect Hga Cang</li>
        <li>📥Desc Masiva Lect Rep</li>
        <li>🧾% Avance Lect y Relect</li>
        <li>🧾% Avance Reparto</li>
        <li>📋Ver Asig Lect Rep</li>
        <li>📈Sum Mis o Dif Obs</li>
    </ol>

    </div>
    """, unsafe_allow_html=True)
    
with col3:
    st.markdown("""
    <div style="
        background: rgba(255,255,255,0.05);
        border:1px solid rgba(255,255,255,0.15);
        border-radius:20px;
        padding:25px;
        color:white;
        min-height:420px;
        box-shadow:0 8px 20px rgba(0,0,0,0.3);
    ">

    <h4 style="
    text-align:center;
    color:#00E5FF;
    font-size:clamp(22px,2vw,34px);
    font-weight:900;
    text-shadow:0px 0px 15px #00E5FF;
    ">
    EXA FIELSERVICE LMC
    </h4>

    <hr>
    <p style="
    margin:0;
    font-size:18px;
    font-weight:bold;
    color:#FFFFFF;
    ">
    Credencial Principal <span style="color:#00E5FF;"></span>
    </p>
    
    <p style="
    margin:0;
    font-size:clamp(14px,1vw,18px);
    font-weight:bold;
    color:#FFFFFF;
    ">
    👤 Usuario: <span style="color:#00E5FF;">lmcf</span>
    </p>
    
    <p style="
    margin:0;
    font-size:clamp(14px,1vw,18px);
    font-weight:bold;
    color:#FFFFFF;
    ">
    🔑 Contraseña: <span style="color:#00E5FF;">Lcahuana</span>
    </p>

    <h4 style="color:#00E5FF;">Módulos</h4>

    <ol style="
    font-size:clamp(15px,1vw,19px);
    font-weight:600;
    line-height:1.4;
    color:white;
    text-shadow:0px 0px 8px rgba(0,0,0,0.8);
    margin-bottom:10px;
    ">
        <li>📤 Exportar OT Lectura</li>
        <li>📋 Asig Lect 2 Criterio</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

# ==========================
# FILA DE BOTONES
# ==========================

st.markdown(
    "<div style='height:2px'></div>",
    unsafe_allow_html=True
)

btn1, btn2, btn3 = st.columns(3, gap="large")

with btn1:
    st.link_button(
        "👤 HUMANO INGRESAR",
        "https://sistemadeexportacionasignacionlecturarepartoyvalidacionreparto.streamlit.app/",
        use_container_width=True
    )

with btn2:
    st.link_button(
        "👤 HUMANO INGRESAR",
        "https://sistema-de-aplicaciones-lmc.streamlit.app/",
        use_container_width=True
    )

with btn3:
    st.link_button(
        "👤 HUMANO INGRESAR",
        "https://sistema-de-exportacion-asignacion-lectura-field-service-ngc.streamlit.app/",
        use_container_width=True
    )
# ==========================
# FOOTER
# ==========================

st.markdown("""
<div class='footer'>
Versión 2.0 | Aplicacion Desarrollado por Luis Miguel Cahuana Figueroa.
</div>
""", unsafe_allow_html=True)
