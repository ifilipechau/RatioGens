# Projecto: DIMENSIONADOR DE GERADOR


# Importa bibliotecas necessárias
import streamlit as st
import datetime

#Define o título da aba e o layout da página
st.set_page_config(page_title="Dimensionador de Gerador", layout="centered")

# Cabeçalho principal
st.title(" Dimensionador de Gerador")
st.write("Insira os dados dos equipamentos abaixo:")

# Lista para guardar os equipamentos inseridos
equipamentos = []

# Campo para o utilizador definir quantos equipamentos vai inserir
quantidade_equipamentos = st.number_input(
    "Quantos equipamentos deseja inserir?", min_value=1, step=1
)

# Loop para inserir os dados de cada equipamento
for i in range(quantidade_equipamentos):
    # Um "expander" para cada equipamento (caixa colapsável)
    with st.expander(f"Equipamento {i+1}"):
        nome = st.text_input(f"Nome do equipamento {i+1}", key=f"nome_{i}")

        #Caixa de seleção para tipo de equipamento
        tipo = st.selectbox(
            f"Tipo de equipamento {i+1}",
            ["iluminação", "moto", "equipamento comum", "sensível"],
            key=f"tipo_{i}"
        )

        # Entrada de potência, quantidade e tempo de uso diário
        potencia = st.number_input(
            f"Potência (W) do equipamento {i+1}", min_value=0.0, key=f"potencia_{i}"
        )
        quantidade = st.number_input(
            f"Quantidade do equipamento {i+1}", min_value=1, step=1, key=f"quantidade_{i}"
        )
        tempo_uso = st.number_input(
            f"Horas de uso por dia (opcional)", min_value=0.0, key=f"tempo_uso_{i}"
        )

        # Aplica o factor de arranque se for motor
        if tipo == "motor":
            potencia *=2.5

        # Guarda os dados do equipamento
        equipamentos.append({
            "nome": nome,
            "tipo": tipo,
            "potencia": potencia,
            "quantidade": quantidade,
            "tempo_uso": tempo_uso
        })

# Separador visual
st.divider()

# Campos para factor de potencia e factor de segurança
factor_potencia = st.number_input("Factor de potência", value=0.8, step=0.1)
factor_seguranca = st.number_input("Factor de segurança", value=1.2, step=0.01)

# Botão principal que realiza os cálculos
if st.button("🔍 Calcular Gerador"):
    # Calcula a potência total em W
    potencia_total = sum(e["potencia"] * e["quantidade"] for e in equipamentos)

    # Converte para kVA com os factores fornecidos
    potencia_kva = (potencia_total / 1000) / factor_potencia * factor_seguranca

    # Estima o consumo diario em kWh
    energia_total_diaria = sum(
        e['potencia'] * e['quantidade'] * e['tempo_uso'] for e in equipamentos
    )

    # Mostra os resultados
    st.success("✅ Cálculo concluído com sucesso!")
    st.metric("Potência Total (W)", f"{potencia_total:.2f} W")
    st.metric("Potência Ideal do Gerador", f"{potencia_kva:.2f} kVA")

    if energia_total_diaria > 0:
        st.metric("Consumo diário estimado", f"{energia_total_diaria/1000:.2f} KWh/dia")

    # Botão para gerar e descarregar o relatório .txt
    if st.download_button(
        "⬇️ Exportar Relatório .txt",
        file_name="relatorio_gerador.txt",
        mime="text/plain",
        data=f"""
RELATÓRIO DE DIMENSIONAMENTO DE GERADOR
Data: {datetime.datetime.now()}

Equipamentos:
{chr(10).join([f"- {e['quantidade']}x {e['nome']} ({e['potencia']}W) - Tipo: {e['tipo']}" for e in equipamentos])}

Potência total: {potencia_total:.2f} W
Factor de potência: {factor_potencia}
Potência ideal do gerador: {potencia_kva:.2f} kVA
Consumo diário estimado: {energia_total_diaria/1000:.2f} kWh
    """):
     st.success("📄 Relatório pronto para download!")