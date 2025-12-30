import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================
# CONFIGURAÇÕES E CONSTANTES (Requisito 7 & 14)
# ==========================================
CONFIG = {
    "NOME_CURSO": "Master em Harmonização Facial: A Arte do Rejuvenescimento",
    "NOME_PROFISSIONAL": "Dra. Beatriz Cavalcanti",
    "BIO_CURTA": "Especialista em Harmonização Orofacial com mais de 10 anos de experiência clínica e acadêmica. Dedicada a ensinar técnicas seguras e resultados naturais para profissionais que buscam excelência.",
    "PRECO_ORIGINAL": "R$ 2.497,00",
    "PRECO_OFERTA": "R$ 1.297,00",
    "PARCELAS": "12x de R$ 129,70",
    "CHECKOUT_URL": "https://pay.hotmart.com/exemplo",
    "GARANTIA": "7 dias de garantia incondicional",
    "DURACAO": "40 horas / 50 aulas práticas e teóricas",
    "CONTATO": "@dra.beatriz_harmonizacao",
    "CORES": {
        "PRIMARIA": "#D4AF37",  # Dourado
        "SECUNDARIA": "#FDF5E6", # Creme/Off-white
        "TEXTO": "#2C2C2C",
        "ACENTO": "#E19191"     # Rosé
    }
}

COPY = {
    "HERO": {
        "HEADLINE": "Domine a Harmonização Facial com Segurança e Naturalidade",
        "SUBTITLE": "Transforme sua carreira e a autoestima de suas pacientes através de um método estruturado, do básico ao avançado, focado em resultados elegantes e ética profissional.",
        "CTA": "Quero me inscrever agora",
        "MICROCOPY": "Acesso imediato após a confirmação do pagamento."
    },
    "BENEFICIOS": [
        {"titulo": "Técnicas Modernas", "desc": "Aprenda os protocolos mais atuais do mercado internacional."},
        {"titulo": "Segurança Clínica", "desc": "Foco total em biossegurança e manejo de intercorrências."},
        {"titulo": "Resultados Naturais", "desc": "Fuja do artificial e aprenda a realçar a beleza individual."},
        {"titulo": "Suporte Especializado", "desc": "Tire suas dúvidas diretamente com a Dra. Beatriz."},
        {"titulo": "Certificado Incluso", "desc": "Certificação reconhecida para sua valorização profissional."},
        {"titulo": "Materiais de Apoio", "desc": "PDFs, guias de consulta rápida e fichas de anamnese."}
    ],
    "MODULOS": [
        {"nome": "Módulo 1: Fundamentos e Anatomia", "desc": "Anatomia facial aplicada, planos musculares e análise estética."},
        {"nome": "Módulo 2: Biossegurança e Materiais", "desc": "Escolha de produtos, assepsia e montagem de consultório."},
        {"nome": "Módulo 3: Toxina Botulínica", "desc": "Pontos de aplicação, diluição e técnicas avançadas."},
        {"nome": "Módulo 4: Preenchimento com Ácido Hialurônico", "desc": "Lábios, malar, mandíbula e sulcos."},
        {"nome": "Módulo 5: Bioestimuladores de Colágeno", "desc": "Protocolos de rejuvenescimento e firmeza da pele."},
        {"nome": "Módulo 6: Gestão e Atendimento", "desc": "Como precificar, vender e fidelizar suas pacientes."}
    ],
    "BONUS": [
        {"nome": "Masterclass: Fotografia Clínica", "valor": "R$ 297,00"},
        {"nome": "Guia de Precificação Lucrativa", "valor": "R$ 197,00"},
        {"nome": "Comunidade Exclusiva de Alunas", "valor": "Inestimável"}
    ],
    "DEPOIMENTOS": [
        {
            "nome": "Dra. Juliana Mendes",
            "cargo": "Dermatologista",
            "texto": "Sempre tive receio de entregar resultados artificiais, mas o método da Dra. Beatriz foca na naturalidade que minhas pacientes buscam. O módulo de anatomia aplicada é o mais completo que já vi. Recuperei o investimento do curso no meu primeiro procedimento pós-treinamento!",
            "foto": "https://via.placeholder.com/100?text=JM"
        },
        {
            "nome": "Dra. Carla Souza",
            "cargo": "Cirurgiã-Dentista",
            "texto": "O que mais me impressionou foi a segurança transmitida. O suporte para intercorrências me deu a confiança que faltava para realizar procedimentos mais complexos. Hoje minha agenda de harmonização está lotada com 3 semanas de antecedência.",
            "foto": "https://via.placeholder.com/100?text=CS"
        },
        {
            "nome": "Dra. Fernanda Lima",
            "cargo": "Biomédica Esteta",
            "texto": "As aulas práticas são extremamente detalhadas. Parece que estamos ao lado da professora na clínica. Os bônus de precificação e fotografia clínica foram o diferencial para eu profissionalizar meu atendimento e aumentar meu ticket médio.",
            "foto": "https://via.placeholder.com/100?text=FL"
        }
    ],
    "FAQ": [
        {"q": "Para quem é este curso?", "a": "Para profissionais da saúde que desejam ingressar ou se aperfeiçoar na harmonização facial."},
        {"q": "Tenho acesso por quanto tempo?", "a": "O acesso é vitalício, incluindo todas as atualizações futuras."},
        {"q": "Preciso de experiência prévia?", "a": "O curso vai do zero ao avançado, mas é necessário ter formação na área da saúde."},
        {"q": "Como recebo o acesso?", "a": "Imediatamente por e-mail após a aprovação do pagamento."},
        {"q": "As aulas são práticas?", "a": "Sim, temos demonstrações detalhadas em pacientes reais gravadas em alta definição."},
        {"q": "Tem suporte para dúvidas?", "a": "Sim, temos uma área de membros e grupo de WhatsApp para suporte."},
        {"q": "O certificado é válido?", "a": "Sim, emitimos certificado de conclusão com carga horária de 40h."},
        {"q": "Quais as formas de pagamento?", "a": "Cartão de crédito (até 12x), PIX ou boleto bancário."}
    ]
}

# ==========================================
# ESTILIZAÇÃO CSS (Requisito 2 & 6)
# ==========================================
def apply_custom_css():
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@300;400;700&display=swap');
        
        html, body, [class*="css"] {{
            font-family: 'Lato', sans-serif;
            color: {CONFIG['CORES']['TEXTO']};
        }}
        
        h1, h2, h3 {{
            font-family: 'Playfair Display', serif;
            color: {CONFIG['CORES']['PRIMARIA']};
        }}
        
        .stButton>button {{
            background-color: {CONFIG['CORES']['PRIMARIA']};
            color: white;
            border-radius: 30px;
            padding: 15px 35px;
            font-weight: bold;
            border: none;
            transition: 0.3s;
            width: 100%;
            font-size: 1.2rem;
        }}
        
        .stButton>button:hover {{
            background-color: {CONFIG['CORES']['ACENTO']};
            transform: scale(1.02);
        }}
        
        .hero-section {{
            background-color: {CONFIG['CORES']['SECUNDARIA']};
            padding: 80px 20px;
            text-align: center;
            border-radius: 15px;
            margin-bottom: 40px;
        }}
        
        .card {{
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            margin-bottom: 20px;
            border-left: 5px solid {CONFIG['CORES']['PRIMARIA']};
        }}
        
        .bonus-card {{
            background: #FFF9F9;
            border: 2px dashed {CONFIG['CORES']['ACENTO']};
            padding: 20px;
            border-radius: 15px;
            text-align: center;
        }}
        
        .price-tag {{
            font-size: 2.5rem;
            color: {CONFIG['CORES']['PRIMARIA']};
            font-weight: bold;
        }}
        
        .footer {{
            text-align: center;
            padding: 40px;
            font-size: 0.8rem;
            color: #666;
        }}
        
        /* CTA Fixo (Simulado via Sidebar ou Topo) */
        .fixed-cta {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 1000;
        }}
        </style>
    """, unsafe_allow_html=True)

# ==========================================
# COMPONENTES DE SEÇÃO (Requisito 15)
# ==========================================

def section_hero():
    st.markdown(f"""
        <div class="hero-section">
            <h1>{COPY['HERO']['HEADLINE']}</h1>
            <p style="font-size: 1.3rem; max-width: 800px; margin: 20px auto;">{COPY['HERO']['SUBTITLE']}</p>
        </div>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button(COPY['HERO']['CTA'], key="hero_cta"):
            st.session_state.page = "checkout"
            st.rerun()
        st.markdown(f"<p style='text-align:center; font-size:0.8rem;'>{COPY['HERO']['MICROCOPY']}</p>", unsafe_allow_html=True)

def section_benefits():
    st.markdown("## Por que escolher este método?")
    cols = st.columns(3)
    for i, ben in enumerate(COPY['BENEFICIOS']):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="card">
                    <h4>{ben['titulo']}</h4>
                    <p>{ben['desc']}</p>
                </div>
            """, unsafe_allow_html=True)

def section_social_proof():
    st.markdown("## O que nossas alunas dizem")
    
    # Depoimentos Detalhados (Novos)
    cols = st.columns(3)
    for i, dep in enumerate(COPY['DEPOIMENTOS']):
        with cols[i]:
            st.markdown(f"""
                <div class="card" style="height: 100%;">
                    <div style="display: flex; align-items: center; margin-bottom: 15px;">
                        <img src="{dep['foto']}" style="border-radius: 50%; width: 60px; margin-right: 15px;">
                        <div>
                            <strong style="color: {CONFIG['CORES']['PRIMARIA']};">{dep['nome']}</strong><br>
                            <small>{dep['cargo']}</small>
                        </div>
                    </div>
                    <p style="font-style: italic; font-size: 0.95rem;">"{dep['texto']}"</p>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Depoimentos Rápidos (Placeholders anteriores)
    proofs = [
        {"nome": "M.S.", "cidade": "São Paulo/SP", "texto": "Resultados muito mais naturais!"},
        {"nome": "A.C.", "cidade": "Curitiba/PR", "texto": "Me sinto pronta para atender."},
        {"nome": "R.F.", "cidade": "Belo Horizonte/MG", "texto": "O módulo de intercorrências vale ouro."}
    ]
    cols_small = st.columns(3)
    for i, p in enumerate(proofs):
        with cols_small[i]:
            st.markdown(f"""
                <div style="font-style: italic; padding: 10px; border-left: 3px solid {CONFIG['CORES']['ACENTO']}; background: #f9f9f9; font-size: 0.85rem;">
                    "{p['texto']}" - <strong>{p['nome']}</strong>
                </div>
            """, unsafe_allow_html=True)

def section_modules():
    st.markdown("## Conteúdo Programático")
    for mod in COPY['MODULOS']:
        with st.expander(mod['nome']):
            st.write(mod['desc'])

def section_about():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://via.placeholder.com/300x400?text=Dra.+Beatriz", caption=CONFIG['NOME_PROFISSIONAL'])
    with col2:
        st.markdown(f"## Sobre a Mentora")
        st.write(CONFIG['BIO_CURTA'])
        st.markdown(f"**Siga no Instagram:** [{CONFIG['CONTATO']}](https://instagram.com)")

def section_bonus():
    st.markdown("## Bônus Exclusivos")
    cols = st.columns(len(COPY['BONUS']))
    for i, b in enumerate(COPY['BONUS']):
        with cols[i]:
            st.markdown(f"""
                <div class="bonus-card">
                    <h4>{b['nome']}</h4>
                    <p style="text-decoration: line-through; color: #999;">De {b['valor']}</p>
                    <p style="color: {CONFIG['CORES']['ACENTO']}; font-weight: bold;">GRÁTIS</p>
                </div>
            """, unsafe_allow_html=True)

def section_target():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Este curso é para você se:")
        st.markdown("- Busca segurança em seus procedimentos\n- Quer entregar resultados naturais\n- Deseja valorizar seu ticket médio\n- É profissional da saúde formada")
    with col2:
        st.markdown("### Este curso NÃO é para você se:")
        st.markdown("- Busca fórmulas mágicas\n- Não tem formação na área da saúde\n- Não preza pela ética profissional\n- Quer apenas o certificado sem estudar")

def section_offer():
    st.markdown("<div style='text-align:center; padding: 50px 0;'>", unsafe_allow_html=True)
    st.markdown(f"## Garanta sua vaga no {CONFIG['NOME_CURSO']}")
    st.markdown(f"<p style='text-decoration: line-through;'>De {CONFIG['PRECO_ORIGINAL']}</p>", unsafe_allow_html=True)
    st.markdown(f"<p class='price-tag'>Por apenas {CONFIG['PRECO_OFERTA']}</p>", unsafe_allow_html=True)
    st.markdown(f"### ou {CONFIG['PARCELAS']}")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("QUERO ME INSCREVER AGORA", key="offer_cta"):
            st.session_state.page = "checkout"
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

def section_faq():
    st.markdown("## Perguntas Frequentes")
    for item in COPY['FAQ']:
        with st.expander(item['q']):
            st.write(item['a'])

# ==========================================
# PÁGINAS (Requisito 9 & 12)
# ==========================================

def page_landing():
    section_hero()
    st.divider()
    section_benefits()
    st.divider()
    section_social_proof()
    st.divider()
    section_modules()
    st.divider()
    section_about()
    st.divider()
    section_bonus()
    st.divider()
    section_target()
    st.divider()
    section_offer()
    st.divider()
    st.markdown(f"### 🛡️ {CONFIG['GARANTIA']}")
    st.write("Se em até 7 dias você não estiver satisfeita, devolvemos 100% do seu investimento.")
    st.divider()
    section_faq()
    
    st.markdown(f"""
        <div class="footer">
            <p>© {datetime.now().year} {CONFIG['NOME_CURSO']} - Todos os direitos reservados.</p>
            <p>Aviso Legal: Este curso é destinado a profissionais da saúde. A prática de procedimentos depende da regulamentação do seu conselho de classe.</p>
        </div>
    """, unsafe_allow_html=True)

def page_checkout():
    st.markdown("## Finalizar Inscrição")
    st.write("Você está a um passo de transformar sua carreira.")
    
    tab1, tab2 = st.tabs(["Opção A: Pagamento Rápido", "Opção B: Cadastro de Interesse"])
    
    with tab1:
        st.info("Você será redirecionado para o ambiente seguro de pagamento.")
        st.markdown(f"[![Botão Checkout](https://via.placeholder.com/300x60?text=IR+PARA+PAGAMENTO+SEGURO)]({CONFIG['CHECKOUT_URL']})")
        if st.button("Voltar para a página inicial", key="back_a"):
            st.session_state.page = "landing"
            st.rerun()
            
    with tab2:
        with st.form("capture_form"):
            nome = st.text_input("Nome Completo")
            email = st.text_input("E-mail")
            whatsapp = st.text_input("WhatsApp")
            submit = st.form_submit_button("Ir para pagamento")
            if submit:
                st.success(f"Obrigado, {nome}! Redirecionando...")
                st.markdown(f"Acesse aqui: [Link de Pagamento]({CONFIG['CHECKOUT_URL']})")
        if st.button("Voltar", key="back_b"):
            st.session_state.page = "landing"
            st.rerun()

def page_members():
    st.markdown("## 🎓 Área de Alunas (Demonstração)")
    
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        
    if not st.session_state.authenticated:
        password = st.text_input("Digite a senha de acesso (Dica: 'aluna2024')", type="password")
        if st.button("Entrar"):
            if password == "aluna2024":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Senha incorreta.")
    else:
        st.sidebar.success("Bem-vinda, Aluna!")
        if st.sidebar.button("Sair"):
            st.session_state.authenticated = False
            st.rerun()
            
        st.write("### Suas Aulas Disponíveis")
        cols = st.columns(2)
        with cols[0]:
            st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Placeholder
            st.caption("Aula 1: Introdução à Harmonização")
        with cols[1]:
            st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Placeholder
            st.caption("Aula 2: Anatomia Aplicada")
            
        st.info("Esta é uma área de demonstração. No curso real, aqui estariam todos os módulos e materiais.")

# ==========================================
# MAIN APP LOGIC
# ==========================================

def main():
    st.set_page_config(page_title=CONFIG['NOME_CURSO'], page_icon="✨", layout="wide")
    apply_custom_css()
    
    if "page" not in st.session_state:
        st.session_state.page = "landing"
        
    # Navegação Simples
    st.sidebar.title("Navegação")
    if st.sidebar.button("Landing Page"):
        st.session_state.page = "landing"
    if st.sidebar.button("Checkout"):
        st.session_state.page = "checkout"
    if st.sidebar.button("Área de Alunas"):
        st.session_state.page = "members"
        
    if st.session_state.page == "landing":
        page_landing()
    elif st.session_state.page == "checkout":
        page_checkout()
    elif st.session_state.page == "members":
        page_members()

if __name__ == "__main__":
    main()
