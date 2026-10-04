# Guia – 5 a 6 minutos

Antes de gravar: abrir o simulador e, na aba **Métodos: erro × tempo**, clicar em **Medir tempos**.
**Entender** = para vocês saberem. **Falar** = as ideias, na ordem. **Mexer** = o que fazer na tela.

---

## 1. Abertura · Henrique · ~40 s
**Entender:** o computador só faz as quatro contas. Para calcular uma função como x·eˣ ele usa um **polinômio** (soma de x, x², x³…), que só precisa de soma e multiplicação. A **série de Taylor** é a receita para montar esse polinômio.

**Falar:**
- Nossa função é **y = x·eˣ**.
- O computador não tem conta pronta para ela, então aproxima por um polinômio.
- Vamos mostrar: derivadas, quantos termos usar, código otimizado, tabela e erro × tempo.

---

## 2. Aba "Derivadas e série" · Henrique · ~1 min 15 s
**Entender:**
- **Derivada** = a inclinação da curva (quão rápido ela sobe ou desce).
- Como x·eˣ é um produto, usamos a **regra do produto**: (u·v)′ = u′v + uv′.
- **Maclaurin** é a série de Taylor em torno de x = 0: usa o valor e as derivadas em 0 para montar o polinômio. Cada derivada a mais é uma correção a mais (ponto → reta → parábola…).

**Falar:**
- Derivamos à mão: f′ = (x+1)eˣ, f″ = (x+2)eˣ, f‴ = (x+3)eˣ.
- Padrão: **a derivada de ordem n é (x+n)eˣ**. Em x = 0 ela vale **n**.
- A série de Maclaurin fica **x + x² + x³/2 + x⁴/6 + …** (é x vezes a série de eˣ).

**Mexer:** slider **N** de 1 a 20 → as somas parciais chegam no valor exato (linha vermelha).

---

## 3. Aba "Aproximação f(x) × T_N(x)" · Cauã · ~1 min
**Entender:** **N** = quantos termos somamos. **T_N** = o polinômio com N termos. Preta = função de verdade, azul = polinômio.

**Falar:**
- Com N = 1 é só a reta **y = x**, que só vale perto de 0.
- Cada termo a mais faz a azul colar na preta por um trecho maior.
- Quanto mais longe de 0, mais termos precisa.
- Propriedades da função: perto de 0 ≈ x; **mínimo em x = −1** (vale −1/e ≈ −0,37); à esquerda tende a 0; à direita cresce muito rápido.

**Mexer:** slider **N** → 1, 2, 3, 5, 10. Soltar o slider para mostrar o valor anterior tracejado.

---

## 4. Aba "Erro × N" · Henrique · ~1 min 15 s
**Entender:**
- A série é infinita, mas só podemos somar uns poucos termos. Onde parar?
- O **resto de Lagrange** dá um **teto** do erro: o erro nunca passa dele.
- Escolhemos uma **tolerância** (erro máximo aceito: 10⁻¹²) e pegamos o menor N que fica abaixo dela.
- O erro para de cair em ~10⁻¹⁶ porque o computador só guarda ~16 dígitos.

**Falar:**
- Como escolhemos N? Pelo resto de Lagrange, com tolerância de 10⁻¹².
- Para |x| ≤ 1 dá **N = 16**; para |x| ≤ 5 dá N = 35. **O N depende do intervalo.**
- O erro real cai e para em 10⁻¹⁶ (limite do computador).
- A garantia (laranja) fica sempre acima do erro real (azul).

**Mexer:** slider **Tolerância** → o N sugerido sobe. Slider **x** → x maior pede mais termos.

---

## 5. Código `taylor.py` · Cauã · ~45 s
**Entender:** são 4 jeitos de programar a **mesma** série. A diferença é o custo.

**Falar:**
- **Ingênua:** recalcula potência e fatorial em todo termo (lenta).
- **Recorrência:** cada termo sai do anterior (× x/k), sem fatorial.
- **Horner:** agrupa a soma e faz menos multiplicações.
- **Otimizada:** escreve **eˣ = 2ᵐ · eʳ** com r pequeno; assim bastam **13 termos para qualquer x**. O 2ᵐ é aplicado de graça com `ldexp`.

**Mexer:** rolar o arquivo mostrando as 4 funções (sem ler linha por linha).

---

## 6. Aba "Métodos: erro × tempo" · Cauã · ~45 s
**Entender:** cada ponto é um N; mostra quanto tempo gasta e que erro atinge. **Melhor = canto inferior esquerdo** (rápido e preciso).

**Falar:**
- Para erro menor que 10⁻¹⁰: a ingênua usa **32 termos (~3,5 µs)**; a otimizada usa **10 termos (~0,3 µs)**.
- A otimizada é **~11× mais rápida**.
- As curvas achatam no fim: limite de precisão do computador.

**Mexer:** trocar o modo para destacar um método de cada vez; depois "Todos os métodos".

---

## 7. Aba "Tabela de valores" · Henrique · ~45 s
**Entender:** é a tabela de valores mais usados (x de −5 a 10) com o erro de cada um. Em x negativo grande a série simples erra por **cancelamento** (termos grandes com sinais alternados se anulam e perdem dígitos).

**Falar:**
- Série simples com N = 16: ótima perto de 0, mas em **x = 10 erra ~5%** e em x = −5 erra muito mais.
- Com a otimizada, todos os erros ficam em ~10⁻¹⁶.

**Mexer:** modo **Série simples** → depois **Otimizada**; olhar as barras de erro caírem.

---

## 8. Encerramento · Cauã · ~20 s
**Falar:**
- Derivamos à mão, escolhemos N com Lagrange, otimizamos o código e comparamos erro e tempo.
- Código e README no GitHub (link na descrição).
- Citar as fontes.

---
**Frase de socorro:** *mais termos, mais perto da função.*
Mais detalhes para estudar: `guia-apresentacao.md`.
