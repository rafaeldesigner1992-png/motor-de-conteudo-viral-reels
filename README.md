# 🎬 Motor de Conteúdo — Sistema Completo

Sistema de inteligência de conteúdo orgânico para redes sociais.
Baseado na metodologia **Jornada Z** (Giullya Becker / Comunicadores Magnéticos) e **Reels Pro** (Rafael Bem).

> **Compatível com:** Claude, ChatGPT, Gemini, Cursor, e qualquer LLM que aceite arquivos de contexto.

---

## 📁 Estrutura

```
motor-conteudo-repo/
├── skills/
│   └── motor-de-conteudo.md     ← Skill principal (importar no Claude/ChatGPT)
├── tools/
│   └── trends_miner.py          ← Script Python para Google Trends Brasil
├── prompts/
│   └── card-generator.md        ← Prompt para gerar cards de pauta
└── examples/
    └── cards-nutricao.md        ← Exemplo de 10 cards gerados para nutrição
```

---

## 🚀 Como usar

### 1. Importar a skill em qualquer IA

Copie o conteúdo de `skills/motor-de-conteudo.md` e cole como:
- **Claude**: Project Instructions ou System Prompt
- **ChatGPT**: Custom Instructions ou GPT System Prompt  
- **Cursor**: `.cursorrules` ou context file
- **Gemini**: System Instructions

### 2. Rodar análise de tendências

```bash
# Instalar dependência
pip3 install pytrends

# Rodar para qualquer nicho
python3 tools/trends_miner.py "seu nicho"

# Exemplos
python3 tools/trends_miner.py "nutricionista"
python3 tools/trends_miner.py "AVCB"
python3 tools/trends_miner.py "emagrecimento"
```

O script salva um `.json` com top buscas, buscas em alta e tópicos relacionados — prontos para alimentar a IA na geração de pautas.

---

## 🧠 Metodologia base

- **OCA** (O quê / Como / Ação) — estrutura da ideia
- **IDF** (Início / Desenvolvimento / Fechamento) — roteiro em 3 atos
- **5 Formatos**: Vlog, Institucional, Storytelling, Anúncio, Magnético
- **Rubricas**: direcionamento de câmera e intenção emocional
- **Jornada Z**: pesquisa → tríade da criatividade → roteiro → distribuição

---

## 📄 Licença

Uso pessoal e comercial livre. Metodologia baseada em cursos de terceiros — créditos a Giullya Becker e Rafael Bem.
