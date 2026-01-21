# Simulação e Análise de Partículas Ativas Brownianas (ABP)

![Status do Projeto](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow) ![Linguagem](https://img.shields.io/badge/Linguagem-Python-blue)

Este repositório contém o código fonte para a simulação de Partículas Ativas Brownianas (Active Brownian Particles - ABP) em 2D. O objetivo principal é gerar trajetórias estocásticas baseadas em dinâmica de Langevin e realizar análises estatísticas sobre o comportamento do sistema.

> **Nota:** O módulo de simulação está completo. As ferramentas de análise de dados estão atualmente em desenvolvimento.

## 📋 Sobre o Projeto

Partículas Ativas Brownianas são modelos fundamentais na física da matéria ativa, descrevendo agentes que convertem energia do ambiente em movimento direcionado, sujeitos a flutuações térmicas.

Este projeto visa:
1.  **Simular** o movimento de $N$ partículas em um ambiente confinado ou periódico.
2.  **Armazenar** os dados posicionais e orientacionais.
3.  **Analisar** propriedades de transporte (futuro).

## 🧪 Modelo Físico

A dinâmica das partículas é regida pelas equações de Langevin. Para uma partícula na posição $\mathbf{r} = (x, y)$ com orientação $\phi$:

$$\frac{d\mathbf{r}}{dt} = v_0 \hat{\mathbf{n}}(\phi) + \sqrt{2D_t} \boldsymbol{\xi}_t(t)$$

$$\frac{d\phi}{dt} = \sqrt{2D_r} \xi_r(t)$$

Onde:
* $v_0$: Velocidade de autopropulsão constante.
* $\hat{\mathbf{n}}(\phi) = (\cos\phi, \sin\phi)$: Vetor diretor.
* $D_t$ e $D_r$: Coeficientes de difusão translacional e rotacional.
* $\boldsymbol{\xi}$: Ruído Gaussiano branco com média zero e variância unitária.

## 🚀 Funcionalidades

### Atuais (Prontas)
* [x] Integração numérica das equações de movimento (Método de Euler-Maruyama).
* [x] Exportação de dados brutos de trajetória.
### Em Desenvolvimento (Roadmap)
* [ ] Condições de contorno (ex: Periódicas ou Paredes Rígidas).
* [ ] Cálculo do Deslocamento Quadrático Médio (MSD).
* [ ] Visualização/Animação das trajetórias em tempo real.
* [ ] Cálculo de parâmetros de ordem.

