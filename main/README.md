# ⚙️ RatioGens – Versão Linha de Comandos (CLI)

Ferramenta desenvolvida em Python para **dimensionamento de geradores eléctricos**, através da introdução manual dos dados em linha de comandos.

## ✅ Funcionalidades

- Inserção de múltiplos equipamentos com tipo, potência e tempo de uso
- Cálculo de potência total e factor de arranque para motores
- Aplicação de factor de potência e de segurança
- Estimativa de consumo diário (kWh)
- Exportação de relatório em `.txt`

## 📌 Exemplo de utilização

```bash
python dimensionador.py

O utilizador será guiado por prompts no terminal.
```
## 🧮 Fórmulas utilizadas

Para calcular a potência necessária e o consumo diário, são utilizadas as seguintes fórmulas:
* Potência Total (W) = potência × quantidade
* Potência em kVA = (Potência Total / 1000) ÷ Factor de Potência × Factor de Segurança
* Consumo Diário = ∑ (potência × quantidade × horas/dia)

## 📄 Relatório

Gera automaticamente um ficheiro relatorio_gerador.txt com os resultados detalhados.

## 📦 Requisitos
- **Python**: 3.8 ou superior
- **Bibliotecas**: Nenhuma externa necessária