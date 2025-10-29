# 🧮 Calculator em Python

Uma **calculadora simples e orientada a objetos**, desenvolvida em Python, com suporte às operações matemáticas básicas (adição, subtração, multiplicação, divisão e potência).
O projeto inclui **validação de tipos**, **tratamento de erros** e **testes automatizados** utilizando o módulo `unittest`.

---

## 🚀 Funcionalidades

✅ Soma (`add`)
✅ Subtração (`subtract`)
✅ Multiplicação (`multiply`)
✅ Divisão com tratamento de erro para divisão por zero (`divide`)
✅ Potência (`power`)
✅ Validação automática para garantir que apenas números sejam aceitos (`_validate_numbers`)
✅ Testes automatizados (`unittest`)

---

## 🧠 Conceitos aplicados

Este projeto foi criado com o objetivo de **praticar e demonstrar domínio dos fundamentos de Python**:

* **Programação Orientada a Objetos (POO)**
  Criação de classes e métodos para encapsular lógica e comportamento.
* **Encapsulamento e validação de dados**
  Uso de método interno (`_validate_numbers`) para garantir integridade dos parâmetros.
* **Tratamento de exceções**
  Utilização de `raise` para capturar erros esperados (como divisão por zero).
* **Type hints (anotações de tipo)**
  Uso de `Union[int, float]` para maior clareza e segurança.
* **Testes automatizados**
  Implementação com `unittest` para validar o comportamento de cada método.

---

## 🧩 Estrutura do projeto

```
📦 calculator
├── calculator.py       # Classe principal e testes automáticos
├── README.md           # Documentação do projeto
└── __pycache__/        # Cache gerado automaticamente (ignorar)
```

---

## 🧰 Pré-requisitos

Antes de executar o projeto, é necessário ter instalado:

* **Python 3.8+**
* Nenhuma biblioteca externa é obrigatória — apenas o `unittest`, que já vem com o Python.

---

## ⚙️ Como executar o projeto

1. **Clone o repositório**

```bash
git clone https://github.com/SEU-USUARIO/calculator.git
cd calculator
```

2. **Execute o arquivo principal**

```bash
python calculator.py
```

Isso exibirá:

* Um pequeno **exemplo de uso** no terminal
* E em seguida, os **testes automatizados**

Exemplo de saída esperada:

```
Demonstração manual:
3 + 4 = 7
10 - 2 = 8
5 × 6 = 30
9 ÷ 3 = 3.0
2 ^ 4 = 16

Executando testes automáticos...

......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

---

## 🧪 Rodando apenas os testes

Se quiser rodar apenas os testes (sem a parte de demonstração), use:

```bash
python -m unittest calculator.py
```

---

## 🛠️ Exemplo de uso em outro arquivo Python

Você também pode importar e usar a classe `Calculator` em outros projetos:

```python
from calculator import Calculator

calc = Calculator()

print(calc.add(10, 5))       # 15
print(calc.divide(8, 2))     # 4.0
print(calc.power(2, 5))      # 32
```

---

## 🧱 Expansões futuras

* Implementar **operações com múltiplos números** (`add_many`, `multiply_many`)
* Adicionar **tratamento de precisão decimal** com o módulo `decimal`
* Criar **interface gráfica (GUI)** com Tkinter ou PyQt
* Publicar como **pacote Python (PyPI)**

---

## 🧑‍💻 Autor

**Hélio do Nascimento Silva**
📧 [hedonasi.1979@gmail.com](mailto:hedonasi.1979@gmail.com)
📱 (21) 99673-8288
🌐 [LinkedIn](https://www.linkedin.com) • [GitHub](https://github.com/SEU-USUARIO)

---

## 📝 Licença

Este projeto está sob a licença **MIT** — sinta-se livre para usar, modificar e compartilhar.
Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

> 💬 *"Aprender a programar é mais do que escrever código — é aprender a pensar de forma estruturada e criativa."*
# Classes-e-testes-logicos
Estudo e Exercícios de apredizado de testes em Pyhton
