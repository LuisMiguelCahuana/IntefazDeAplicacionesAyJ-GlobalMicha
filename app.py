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
# TARJETA 1: EXAVAL LMC
# SOLO MANTENER EL BOTÓN VER VIDEO
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
    APP CONFORMACION DE CUADRILLAS
    </h4>

    <hr>

    <div style="text-align:center; margin-top:35px;">
        <a href="https://conformaciondecuadrillas.streamlit.app/"
           target="_blank"
           style="
           display:inline-block;
           background:linear-gradient(90deg,#00C8FF,#2563EB);
           color:white;
           padding:12px 28px;
           border-radius:10px;
           text-decoration:none;
           font-weight:bold;
           font-size:clamp(14px,1vw,18px);
           box-shadow:0px 0px 10px rgba(0,200,255,.4);
           ">
           Click Aqui
        </a>
    </div>

    </div>
    """, unsafe_allow_html=True)

# ==========================
# TARJETA 2: PLATAFORMA LMC
# CONSERVAR TODO EL CONTENIDO
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
    MONITOREO DE KILOMETRAJE DISTRIBUCION
    </h4>

    <hr>

    <div style="text-align:center; margin-top:35px;">
        <a href="https://monitoreoayj.streamlit.app/"
           target="_blank"
           style="
           display:inline-block;
           background:linear-gradient(90deg,#00C8FF,#2563EB);
           color:white;
           padding:12px 28px;
           border-radius:10px;
           text-decoration:none;
           font-weight:bold;
           font-size:clamp(14px,1vw,18px);
           box-shadow:0px 0px 10px rgba(0,200,255,.4);
           ">
           Click Aqui
        </a>
    </div>

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
    MONITOREO DE KILOMETRAJE GLOBAL MICHA
    </h4>

    <hr>

    <div style="text-align:center; margin-top:35px;">
        <a href="https://monitoreoglobamicha.streamlit.app/"
           target="_blank"
           style="
           display:inline-block;
           background:linear-gradient(90deg,#00C8FF,#2563EB);
           color:white;
           padding:12px 28px;
           border-radius:10px;
           text-decoration:none;
           font-weight:bold;
           font-size:clamp(14px,1vw,18px);
           box-shadow:0px 0px 10px rgba(0,200,255,.4);
           ">
           Click Aqui
        </a>
    </div>

    </div>
    """, unsafe_allow_html=True)
# ==========================
# FOOTER
# ==========================
st.markdown("""
<div class='footer'>
Versión 2.0 | Aplicacion Desarrollado por Luis Miguel Cahuana Figueroa.
</div>
""", unsafe_allow_html=True)
