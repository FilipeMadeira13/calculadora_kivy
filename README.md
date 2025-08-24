# 🧮 Calculadora Kivy

Uma calculadora moderna e funcional desenvolvida em Python usando o framework Kivy, com interface gráfica intuitiva e suporte a operações matemáticas avançadas.

## ✨ Características

- **Interface moderna**: Design com botões arredondados e cores personalizadas
- **Operações básicas**: Adição, subtração, multiplicação e divisão
- **Suporte a decimais**: Operações com números decimais
- **Parênteses**: Suporte completo a expressões com parênteses
- **Porcentagem**: Cálculos com percentual integrados
- **Tratamento de erros**: Exibição de "ERROR" para operações inválidas
- **Testes automatizados**: Suite completa de testes com pytest

## 🚀 Instalação

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

### Passos de instalação

1. **Clone o repositório**
```bash
git clone https://github.com/FilipeMadeira13/calculadora_kivy.git
cd calculadora-kivy
```

2. **Crie um ambiente virtual (recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

### Dependências

As principais dependências incluem:
- `kivy`: Framework para interface gráfica
- `pytest`: Framework de testes

## 🎯 Como usar

### Executando a calculadora

```bash
python src/main.py
```

### Operações disponíveis

| Botão | Função |
|-------|--------|
| `0-9` | Números |
| `+` | Adição |
| `-` | Subtração |
| `*` | Multiplicação |
| `/` | Divisão |
| `.` | Ponto decimal |
| `%` | Porcentagem |
| `(` `)` | Parênteses |
| `=` | Calcular resultado |
| `C` | Limpar tudo |

### Exemplos de uso

- **Operação simples**: `2 + 3 =` → `5`
- **Com decimais**: `3.5 + 2.5 =` → `6`
- **Com parênteses**: `(2 + 3) * 4 =` → `20`
- **Porcentagem**: `50% =` → `0.5`
- **Porcentagem em operação**: `200 + 10% =` → `200.1`

## 🏗️ Estrutura do projeto

```
calculadora-kivy/
├── src/
│   ├── main.py          # Arquivo principal da aplicação
│   └── calc.kv          # Layout da interface (Kivy)
├── tests/
│   └── test_calculator.py  # Testes automatizados
├── requirements.txt     # Dependências do projeto
└── README.md           # Este arquivo
```

## 🧪 Executando os testes

Para executar os testes automatizados:

```bash
pytest tests/
```

Para executar com mais detalhes:

```bash
pytest tests/ -v
```

Para executar com cobertura:

```bash
pytest tests/ --cov=src
```

### Testes incluídos

- ✅ Operações matemáticas básicas
- ✅ Operações com números decimais
- ✅ Expressões com parênteses
- ✅ Cálculos com porcentagem
- ✅ Função de limpeza (Clear)
- ✅ Tratamento de erros

## 🎨 Personalização

### Modificando cores e aparência

As cores e estilos podem ser modificados no arquivo `src/calc.kv`:

- **Cor dos botões**: Modifique `background_color` em `<Button>`
- **Cor do texto**: Altere `color` em `<Button>`
- **Cor de fundo**: Ajuste `rgba` em `canvas.before`
- **Raio dos botões**: Modifique `radius` em `RoundedRectangle`

### Adicionando novas funcionalidades

Para adicionar novos botões ou operações:

1. Adicione o botão no arquivo `calc.kv`
2. Implemente a lógica no arquivo `main.py`
3. Crie testes correspondentes em `test_calculator.py`

## 🐛 Tratamento de erros

A calculadora trata os seguintes casos de erro:

- Divisão por zero
- Expressões matemáticas inválidas
- Parênteses não balanceados
- Operadores consecutivos inválidos

Quando um erro ocorre, a calculadora exibe "ERROR" e permite continuar a operação após limpar.

## 🚀 Funcionalidades avançadas

### Modo de entrada inteligente

- Automaticamente substitui a tela quando uma nova operação é iniciada
- Previne entrada de múltiplos pontos decimais
- Gerencia automaticamente parênteses balanceados

### Processamento de expressões

- Suporte a operador `%` convertido para `/100`
- Avaliação segura de expressões matemáticas
- Formatação automática de resultados (remove `.0` de números inteiros)

## 📝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Crie um Pull Request

### Diretrizes de contribuição

- Mantenha o código limpo e bem documentado
- Adicione testes para novas funcionalidades
- Siga as convenções de nomenclatura Python (PEP 8)
- Atualize a documentação conforme necessário

## 📋 TODO

- [ ] Histórico de operações
- [ ] Modo científico
- [ ] Temas personalizáveis
- [ ] Atalhos de teclado
- [ ] Função de memória (M+, M-, MR, MC)
- [ ] Exportar resultados

## 🔧 Solução de problemas

### A calculadora não inicia

- Verifique se o Kivy está instalado corretamente
- Confirme se você está usando Python 3.7+
- Verifique se o arquivo `calc.kv` está no mesmo diretório

### Testes falham

- Confirme se o pytest está instalado
- Verifique se você está executando os testes do diretório raiz
- Confirme se o módulo `src` está no PYTHONPATH

### Interface não carrega corretamente

- Verifique se o arquivo `calc.kv` não foi modificado incorretamente
- Confirme se todas as dependências do Kivy estão instaladas
- Teste em um ambiente virtual limpo

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Autor

Desenvolvido com ❤️ para aprendizado e demonstração das capacidades do framework Kivy.

---

**Nota**: Este projeto foi desenvolvido para fins educacionais e demonstra boas práticas de desenvolvimento Python com interfaces gráficas.