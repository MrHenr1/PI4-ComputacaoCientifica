# Guia para Cauã e Henrique: entender e explicar (partindo do zero)

Cada parte tem duas caixas:
- **ENTENDA PRIMEIRO:** a explicação do zero, sem presumir nada. Leiam até fazer sentido.
- **DIGA ISSO:** a lista de ideias, em ordem, para falar no vídeo com as próprias palavras.

🖥️ = o que mostrar na tela · 🔢 = número para citar. Tempo total ~10 min.
Divisão sugerida: **Henrique** puxa as partes 1, 2, 4, 6 e 8; **Cauã** puxa as 3, 5 e 7 e mexe no simulador o tempo todo.

**Antes de gravar (Cauã):** rodar `.venv/bin/python src/simulador.py`; em "Métodos: erro × tempo" clicar em **Medir tempos**; voltar para "Derivadas e série"; deixar `src/taylor.py` aberto no editor.

---

## 1. Abertura · Henrique (~40 s) · 🖥️ simulador aberto

### ENTENDA PRIMEIRO
O processador do computador só faz **quatro contas**: somar, subtrair, multiplicar e dividir. Não existe um circuito que calcule "e elevado a x", logaritmo, seno etc. Mesmo assim, quando você digita `exp(2)` numa calculadora, sai a resposta. Como?

O computador **monta o resultado usando só as quatro contas**. Um jeito é usar um **polinômio**: uma soma do tipo `x + x² + x³/2 + ...`. Um polinômio só tem multiplicação e soma, então o computador sabe calcular. O truque é achar um polinômio que fique **quase igual** à função. A ferramenta que acha esse polinômio é a **série de Taylor**.

O nosso trabalho é: pegar a função **y = x·eˣ**, montar esse polinômio, decidir **quantos termos** usar, programar de forma rápida e medir o erro.

### DIGA ISSO
- Apresentar o grupo e a função **y = x·eˣ**.
- O computador só soma, subtrai, multiplica e divide. Não tem conta pronta para essa função.
- Então ele a aproxima por um polinômio. Isso é a **série de Taylor**.
- Vamos mostrar: derivadas, escolha do número de termos, código otimizado, tabela de valores e erro × tempo.

---

## 2. Derivadas, Maclaurin e a série · Henrique · 🖥️ visão "Derivadas e série" (~2 min 30 s)

### ENTENDA PRIMEIRO

**O que é uma derivada.** É a **velocidade com que a função está mudando** num ponto. Pense num carro: a posição é a função; a derivada é a velocidade. No gráfico, é a **inclinação** da curva: derivada positiva = a curva sobe; negativa = desce; zero = está no topo ou no fundo.
Exemplo: a derivada de x² é 2x. Em x = 3 a inclinação é 6 (sobe rápido); em x = 0 é 0 (fundo da curva).

**Derivar várias vezes.** Dá para derivar a derivada. A 2ª derivada diz como a **velocidade** muda (a *aceleração*, a curvatura). A 3ª diz como a aceleração muda, e assim por diante. Cada derivada traz um detalhe mais fino sobre como a função se comporta.

**Como derivamos x·eˣ à mão.** A função é um **produto** de duas coisas: `x` e `eˣ`. Existe a **regra do produto**: se f = u·v, então **f′ = u′·v + u·v′**. Aqui u = x (derivada 1) e v = eˣ (a derivada do eˣ é ele mesmo, uma propriedade especial dele):
- f = x·eˣ
- f′ = 1·eˣ + x·eˣ = **(x + 1)·eˣ**
- f″ = derivando (x+1)·eˣ: 1·eˣ + (x+1)·eˣ = **(x + 2)·eˣ**
- f‴ = **(x + 3)·eˣ**

Aparece um **padrão**: a derivada de ordem n é **(x + n)·eˣ**. (Prova rápida: se vale para n, derivando de novo dá eˣ + (x+n)·eˣ = (x+n+1)·eˣ, que é o padrão para n+1. Isso é prova por indução.)

**Valor das derivadas em x = 0.** Como e⁰ = 1, fica (0 + n)·1 = **n**. Então as derivadas em zero são **0, 1, 2, 3, 4, ...**

**O que é uma série e por que Taylor.** Uma **série** é uma soma com muitos termos (pode ser infinita). A ideia de Taylor é esta: *se eu sei tudo sobre a função num ponto, eu consigo imitá-la perto desse ponto.* Usando o carro:
- Só sei **onde o carro está** (valor f(0)): prevejo que ele fica parado. Aproximação ruim.
- Sei também a **velocidade** (f′(0)): prevejo uma **reta**. Melhor.
- Sei também a **aceleração** (f″(0)): prevejo uma **parábola**. Melhor ainda.
- Cada derivada a mais é uma correção a mais, e a previsão vai ficando mais fiel.

Isso vira a fórmula. A **série de Maclaurin** é a série de Taylor feita **em torno de x = 0** (que é o nosso caso):

> f(x) ≈ f(0) + f′(0)·x + f″(0)·x²/2! + f‴(0)·x³/3! + ...

O **n!** (fatorial) é só um ajuste: 3! = 3·2·1 = 6, 4! = 24 etc. Ele garante que cada termo entre com o peso certo.

**Aplicando ao nosso caso.** Com f⁽ⁿ⁾(0) = n, o termo de ordem n é `n·xⁿ/n!`, e como n/n! = 1/(n−1)!, vira **xⁿ/(n−1)!**:

> **x + x² + x³/2 + x⁴/6 + x⁵/24 + ...**

Reparem que isso é **x vezes a série do eˣ** (1 + x + x²/2 + x³/6 + ...), o que faz sentido, já que a função é x·eˣ.

**Exemplo com número.** Em x = 1, o valor exato é 1·e = 2,718...
- 1 termo (T₁): 1
- 2 termos (T₂): 1 + 1 = 2
- 3 termos (T₃): 1 + 1 + 0,5 = 2,5
- 5 termos (T₅): 1 + 1 + 0,5 + 0,167 + 0,042 = **2,708**
Cada termo chega mais perto de 2,718.

### DIGA ISSO
- A derivada é a inclinação da curva, a velocidade com que ela muda.
- Derivamos à mão com a **regra do produto**, porque x·eˣ é um produto.
- Resultado: f′ = (x+1)eˣ, f″ = (x+2)eˣ, f‴ = (x+3)eˣ → padrão **f⁽ⁿ⁾(x) = (x+n)eˣ**.
- Em x = 0 (e⁰ = 1) as derivadas valem **0, 1, 2, 3...**
- A série de **Maclaurin** é a de Taylor centrada em 0: usa o valor e as derivadas em 0 para montar um polinômio que imita a função. Cada derivada a mais é uma correção a mais.
- Aplicando: o termo é xⁿ/(n−1)!, a série é **x + x² + x³/2 + x⁴/6 + ...** = **x vezes a série de eˣ**.
- 🖥️ Gráfico de cima: a função e as derivadas, com a fórmula na legenda.
- 🖥️ Gráfico de baixo: arrastar **N** de 1 a 20; as somas parciais chegam no valor exato (linha vermelha).
- 🔢 Em x = 1: com 3 termos dá 2,5; com 5 dá 2,708; o exato é 2,718.

---

## 3. Aproximações e propriedades · Cauã · 🖥️ visão "Aproximação f(x) × T_N(x)" (~2 min)

### ENTENDA PRIMEIRO

**O que é o N e o T_N.** **N** é quantos termos da série somamos. **T_N(x)** é o polinômio que sai dessa soma. Então T₁ = x, T₂ = x + x², T₃ = x + x² + x³/2, e assim por diante. É "a aproximação com N termos".

**O que o gráfico mostra.** A linha preta é a função de verdade. A azul é o polinômio. Com N = 1 o polinômio é a reta y = x (só usa o valor e a inclinação em 0), que só cola na curva bem perto de 0. Cada termo novo estende o trecho em que a azul cola na preta. Quanto mais longe de 0, mais termos são necessários, porque a série "parte" do zero.

**Propriedades da função (o enunciado pede):**
- Vale 0 em x = 0 e perto dali ≈ **x** (por isso T₁ = x).
- **Mínimo em x = −1:** a derivada (x+1)eˣ é zero ali, e a função vale −1/e ≈ **−0,37**. É o ponto mais baixo da curva.
- À esquerda a curva **tende a 0** (o eˣ diminui mais rápido do que o x cresce). O eixo x é uma assíntota.
- À direita ela **cresce muito rápido** (o eˣ explode).

**O que é o gráfico de baixo.** É o erro, |f − T_N|, em **escala logarítmica**: cada linha horizontal é 10× menor que a de cima. Usamos escala log porque o erro vai de números grandes até minúsculos; numa escala normal só se veria o zero. O erro é mínimo perto de 0 e cresce com a distância.

### DIGA ISSO
- N = número de termos; T_N = polinômio com N termos.
- 🖥️ N = 1: é a reta **y = x**, boa só perto de 0. Subir para 2, 3, 5, 10: a azul vai colando na preta.
- Quanto mais longe de 0, mais termos precisa.
- 🖥️ Soltar o slider: o valor anterior fica tracejado, para comparar.
- Propriedades: perto de 0 ≈ x; **mínimo em x = −1** valendo −1/e (🔢 ≈ −0,37); tende a 0 à esquerda; cresce muito rápido à direita.
- 🖥️ Painel Resultados: valor do polinômio, valor exato, erro e a garantia de Lagrange (explicada na parte 4).

---

## 4. Escolha de N · Henrique · 🖥️ visão "Erro × N" (~2 min)

### ENTENDA PRIMEIRO

**O problema.** A série tem infinitos termos, mas o computador só pode somar um número finito. Onde parar? É isso que o professor pergunta: *qual N e por quê?*

**Erro.** É a diferença entre o valor certo e o nosso. **Erro absoluto** = |certo − nosso|. **Erro relativo** = esse erro dividido pelo valor certo (ex.: 0,05 = 5%).

**Resto de Lagrange (a "garantia").** Quando paramos no termo N, os termos que ficaram de fora formam o **resto**. A fórmula de Lagrange não diz o erro exato, mas dá um **teto**: o erro **nunca passa** de um certo valor. Para x entre −a e a, esse teto é:

> (N + 1 + a) · eᵃ · aᴺ⁺¹ / (N+1)!

Repare que o (N+1)! no denominador cresce muito rápido, então o teto despenca conforme N aumenta.

**Como escolhemos.** Fixamos uma **tolerância** (o erro máximo que aceitamos): **10⁻¹²** (0,000000000001). Procuramos o **menor N** em que o teto fica abaixo dela:
- se vou usar a fórmula só para |x| ≤ 1 → **N = 16**;
- até |x| ≤ 5 → N = 35.
Por isso **não existe um N único**: ele depende de até onde quero usar a fórmula e de quanto erro aceito.

**O piso de 10⁻¹⁶.** O computador (float64) guarda só ~16 dígitos. Por isso o erro nunca fica menor que cerca de 10⁻¹⁶, não importa quantos termos se somem. É o "chão" do gráfico.

**No gráfico.** Em cima: o erro real cai e para no chão de 10⁻¹⁶. A linha vermelha é a tolerância; a vertical cinza é o N que a garantia pede. Embaixo: a curva laranja (garantia) fica sempre **acima** da azul (erro real), porque a garantia é um teto, e na prática erramos menos do que ela promete.

### DIGA ISSO
- Pergunta: onde parar a série? Qual N e por quê?
- Erro absoluto e relativo, em uma frase.
- **Resto de Lagrange** = um teto: garante o erro máximo, sem precisar do valor exato.
- Tolerância de **10⁻¹²**; escolhemos o menor N que fica abaixo disso. 🔢 |x| ≤ 1 → **N = 16**; |x| ≤ 5 → N = 35. **O N depende do intervalo.**
- 🖥️ Gráfico de cima: o erro cai e para em **~10⁻¹⁶**, o limite do computador (float64 guarda ~16 dígitos).
- 🖥️ Mexer na **tolerância** (sobe o N sugerido) e em **x** (x maior pede mais termos).
- 🖥️ Gráfico de baixo: a garantia (laranja) fica sempre acima do erro real (azul).

---

## 5. Código otimizado · Cauã (Henrique complementa) · 🖥️ editor com `src/taylor.py` (~2 min)

### ENTENDA PRIMEIRO

São **4 jeitos de programar a mesma série**. O resultado matemático é igual; muda o custo.

1. **Ingênua:** em cada termo calcula xⁿ e n! do zero. Muito trabalho repetido (n! e xⁿ crescem muito).
2. **Recorrência:** cada termo vem do anterior: `termo_novo = termo_anterior · x / k`. Não precisa de fatorial nem de potência. Ex.: do termo x³/3! para o x⁴/4! basta multiplicar por x/4.
3. **Horner:** reescreve `1 + x + x²/2 + ...` como `1 + x(1 + x/2(1 + x/3(...)))`. Faz o mínimo de multiplicações.
4. **Otimizada (redução de argumento):** o truque mais forte. A série funciona bem quando x é **pequeno**, mas fica pesada quando x é grande (em x = 10, precisa de dezenas de termos). A saída: escrever
   > **eˣ = 2ᵐ · eʳ**, com m inteiro e r pequeno (|r| ≤ 0,35)
   Dividimos x por ln 2 para achar m. Aí a série só precisa calcular eʳ, com r pequeno, e bastam **13 termos para qualquer x**. O fator 2ᵐ é "de graça": o computador guarda números como mantissa × 2^expoente, então multiplicar por 2ᵐ só mexe no expoente. A função `ldexp` faz isso.

É a mesma ideia que as bibliotecas matemáticas de verdade usam.

### DIGA ISSO
- 4 versões da mesma série. 🖥️ Rolar o arquivo: `derivada`, `taylor_ingenua`, `taylor_recorrencia`, `taylor_horner`, `taylor_otimizada`, `escolher_N`.
- `derivada` guarda a fórmula (x+n)eˣ que achamos à mão.
- **Ingênua:** recalcula potência e fatorial em todo termo (lenta).
- **Recorrência:** reaproveita o termo anterior (×x/k), sem fatorial.
- **Horner:** agrupa a soma e faz menos multiplicações.
- **Otimizada:** **redução de argumento**, eˣ = 2ᵐ·eʳ com r pequeno → poucos termos. 🔢 **13 termos** servem para qualquer x. O 2ᵐ é aplicado de graça com `ldexp`.
- É o que as bibliotecas reais fazem.

---

## 6. Erro × tempo · Henrique · 🖥️ visão "Métodos: erro × tempo" (~1 min 30 s)

### ENTENDA PRIMEIRO

Aqui comparamos os 4 métodos: quanto **tempo** cada um gasta (em microssegundos, µs) e que **erro** atinge. Para cada N medimos os dois e marcamos um ponto.

**Como ler o gráfico de cima:** eixo x = tempo; eixo y = erro (escala log). Melhor = **canto inferior esquerdo** (rápido e preciso). Cada curva é um método e cada ponto, um N.

**O resultado.** Para chegar a erro menor que 10⁻¹⁰ em [−5, 5]:
- ingênua: **32 termos**, ~3,5 µs;
- recorrência e Horner: 32 termos, ~0,7 µs;
- **otimizada: 10 termos, ~0,3 µs.**
A otimizada é a **mais precisa e a mais rápida**, uns 11× mais rápida que a ingênua. O ganho vem de precisar de menos termos.

**O chão no fim das curvas** (~10⁻¹³ e ~10⁻¹⁶) é o limite de precisão do float64.

Os tempos exatos mudam de computador para computador, mas a **ordem** entre os métodos se mantém.

### DIGA ISSO
- Comparamos os 4 métodos: tempo × erro.
- Como ler: melhor método = canto inferior esquerdo.
- 🔢 Erro < 10⁻¹⁰: ingênua **32 termos / ~3,5 µs**; otimizada **10 termos / ~0,3 µs** → **~11× mais rápida**.
- Ganho: precisa de menos termos.
- As curvas achatam no fim: limite de precisão do computador.
- 🖥️ Alternar entre um método de cada vez e "Todos os métodos".

---

## 7. Tabela de valores · Cauã · 🖥️ visão "Tabela de valores" (~1 min)

### ENTENDA PRIMEIRO

O enunciado pede uma **tabela de valores mais usados**: para x = −5, −2, −1, −0,5, 0, 0,5, 1, 2, 5 e 10, o valor exato, o valor pela nossa série e o erro.

**O que ela mostra.** Com a série simples e N = 16 (escolhido para |x| ≤ 1):
- perto de 0 o erro é minúsculo;
- em **x = 10 erra uns 5%**: 16 termos não bastam para um x tão grande;
- em **x = −5 erra muito mais**, por **cancelamento**: os termos são grandes e com sinais alternados (+, −, +, −), então ao somar eles quase se anulam e o resultado perde dígitos.
Com a **otimizada**, todos os erros ficam em ~10⁻¹⁶, o limite do computador, para qualquer x. É a prova de que a otimização resolve o problema.

### DIGA ISSO
- A tabela pedida: valores mais usados, x de −5 a 10.
- 🖥️ Série simples, N = 16: ótima perto de 0, mas **em x = 10 erra ~5%** e em x = −5 erra muito mais (cancelamento).
- 🖥️ Trocar para **Otimizada**: todos os erros caem para ~10⁻¹⁶, em qualquer x.
- Conclusão: a redução de argumento é o que faz a fórmula valer em qualquer x.

---

## 8. Encerramento · Henrique (~20 s) · 🖥️ simulador

### DIGA ISSO
- Resumo em uma frase: derivamos à mão, escolhemos o N com Lagrange, otimizamos o código e comparamos erro e tempo.
- Código e README no GitHub, link na descrição.
- **Citar as fontes** que o grupo usou.

---

## Se um dos dois travar
A frase que resume tudo: **"Mais termos, mais perto da função. A gente escolheu quantos termos com uma garantia matemática, e otimizou o código para precisar de menos termos e gastar menos tempo."**
Se esquecer um número, falem "bem pequeno" ou "bem mais rápido": o gráfico mostra o resto. Dá para regravar só a parte errada.
