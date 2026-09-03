 ⚡ Consumo de Energia

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)
![Energia](https://img.shields.io/badge/Energia-El%C3%A9trica-green)

 🎯 Objetivo

O **Consumo de Energia** é um programa desenvolvido em Python que calcula o consumo mensal de energia elétrica de um aparelho.

O usuário informa o nome do aparelho, sua potência em watts e o tempo médio de uso diário. O programa calcula o consumo mensal em kWh e estima o custo da energia.

 🧮 Fórmula utilizada

O consumo mensal é calculado utilizando a seguinte fórmula:

```text
consumoMensal = (potencia * horasDia * 30) / 1000
```

O resultado é apresentado em **kWh/mês**.

Para estimar o custo da energia, é utilizado o valor de **R$ 0,75 por kWh**:

```text
custo = consumoMensal * 0,75
```

 ▶️ Como executar

1. Abra a pasta do projeto no VS Code.
2. Abra o terminal.
3. Execute o comando:

```bash
python app.py
```

4. Informe os dados solicitados pelo programa.

 💡 Exemplo

```text
Aparelho: Geladeira
Potência: 100 W
Uso diário: 5 horas
Consumo mensal: 15 kWh
Custo estimado: R$ 11,25
```

 📁 Estrutura do projeto

```text
consumo-energia/
├── app.py
└── README.md
```

 👨‍💻 Autor

Projeto desenvolvido por **Pedro Figueredo dos Santos**.
