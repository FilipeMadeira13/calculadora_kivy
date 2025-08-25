# Calculator Project

Uma calculadora desenvolvida com Python e Kivy, com interface responsiva e funcionalidades avançadas para Android.

## Características

- Interface gráfica responsiva adaptável a diferentes tamanhos de tela
- Operações matemáticas básicas (+, -, *, /)
- Suporte a números decimais
- Cálculos com parênteses
- Operações de porcentagem
- Função limpar (Clear)
- Compilação para Android via Buildozer

## Estrutura do Projeto

```
kivy-project/
├── main.py          # Lógica principal da calculadora
├── calc.kv              # Interface do usuário (Kivy)
├── test_calculator.py   # Testes automatizados
├── buildozer.spec       # Configuração para Android
├── requirements.txt     # Dependências do projeto
└── README.md           # Este arquivo
```

## Instalação e Configuração

### Pré-requisitos

```bash
# Ubuntu/Debian
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses-dev cmake libffi-dev libssl-dev

# Python 3.11+ recomendado
python3 --version
```

### Instalação das Dependências

```bash
# Clone o repositório
git clone https://github.com/FilipeMadeira13/calculadora_kivy.git
cd kivy-project

# Crie um ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt
```

### Dependências Principais

- **Kivy**: Framework para interface gráfica multiplataforma
- **Buildozer**: Ferramenta para compilação Android
- **Cython**: Necessário para compilação
- **pytest**: Framework de testes

## Execução

### Desktop/Desenvolvimento
```bash
cd src
python main.py
```

### Compilação para Android

```bash
# Primeira compilação (pode demorar)
buildozer android debug

# Compilações subsequentes
buildozer android debug

# Instalar no dispositivo (ADB configurado)
buildozer android debug deploy run
```

## Funcionalidades da Calculadora

### Operações Básicas
- **Números**: Digite números de 0-9
- **Operadores**: +, -, *, /
- **Decimal**: Use o ponto (.) para números decimais
- **Igual**: = para executar o cálculo
- **Limpar**: C para resetar

### Recursos Avançados
- **Parênteses**: ( e ) para agrupamento de operações
- **Porcentagem**: % converte números para porcentagem (50% = 0.5)
- **Validação**: Previne operações inválidas
- **Tratamento de Erros**: Exibe "ERROR" para expressões inválidas

### Exemplos de Uso
```
2 + 3 = 5
(2 + 3) * 4 = 20
50% = 0.5
200 + 10% = 200.1
```

## Testes

Execute os testes automatizados:

```bash
# Executar todos os testes
pytest test_calculator.py

# Executar com detalhes
pytest -v test_calculator.py

# Executar teste específico
pytest test_calculator.py::test_basics
```

### Cobertura de Testes
- Operações matemáticas básicas
- Números decimais
- Parênteses e precedência
- Operações de porcentagem  
- Função limpar
- Tratamento de erros

## Interface Responsiva

A interface foi desenvolvida com `size_hint` e `pos_hint` para adaptação automática a diferentes tamanhos de tela:

- **Display**: Ocupa 25% da altura da tela
- **Botões**: Distribuídos uniformemente em grid 5x4
- **Fontes**: Escaláveis baseadas no tamanho dos componentes
- **Espaçamento**: Proporcional ao tamanho da tela

## Configuração Android

### buildozer.spec - Principais Configurações

```ini
[app]
title = Calculator Project
package.name = calculatorproject
package.domain = br.com.calculatorproject.filipemadeira

[android]
permissions = android.permission.INTERNET
api = 31
minapi = 21
ndk_api = 21
archs = arm64-v8a, armeabi-v7a
```

### Instalação Manual no Android

Se o ADB não funcionar:
1. Compile: `buildozer android debug`
2. Copie o APK: `cp bin/*.apk /mnt/c/Users/$USER/Desktop/`
3. Transfira para o dispositivo
4. Instale permitindo "Fontes desconhecidas"

## Solução de Problemas

### Python 3.12 - Erro distutils
```bash
pip install setuptools
```

### WSL2 - ADB não encontra dispositivo
```bash
# Configure ADB bridge
export ADB_SERVER_SOCKET=tcp:localhost:5037

# No Windows
adb start-server
adb devices
```

### Buildozer - main.py não encontrado
Certifique-se de que existe um arquivo `main.py` na raiz do projeto.

## Desenvolvimento

### Adicionando Novas Funcionalidades

1. **Lógica**: Implemente em `src/main.py`
2. **Interface**: Atualize `calc.kv`
3. **Testes**: Adicione casos em `test_calculator.py`
4. **Documentação**: Atualize este README

### Estrutura do Código

- `CalculatorLayout`: Classe principal com lógica de negócio
- `CalculatorApp`: Aplicação Kivy que carrega a interface
- Widgets customizados: `NumberButton`, `OperatorButton`, etc.

## Tecnologias Utilizadas

- **Python 3.11+**: Linguagem principal
- **Kivy 2.3.0**: Framework GUI multiplataforma
- **Buildozer**: Compilação para Android
- **pytest**: Testes automatizados
- **Android NDK/SDK**: Compilação nativa Android

## Licença

Este projeto é de uso educacional e demonstrativo.

## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Autor

Desenvolvido como projeto de aprendizado em desenvolvimento mobile com Python/Kivy.