NALAsy - Análise de Precificação Estratégica e Otimização de Receita
Visão Geral do Projeto

Este projeto teve como objetivo principal avaliar a estratégia de precificação da NALAsy, respondendo à questão da diretoria: "Estamos a cobrar demasiado caro?". 

Através de uma análise multifacetada, exploramos o posicionamento de preços da NALAsy em comparação com a concorrência, identificamos oportunidades de otimização e validamos hipóteses de negócio usando um modelo preditivo e a simulação de um experimento de teste A/B.

Metodologia de Análise
O projeto foi dividido em três fases principais para garantir uma abordagem sistemática e rigorosa:

Fase 1: Análise Exploratória e Diagnóstico
Objetivo: Comparar as taxas de serviço da NALAsy com as taxas dos concorrentes nos principais corredores e entender o comportamento de clientes novos vs. recorrentes.

Análise:
Comparação de Preços: Verificação das taxas médias de serviço por corredor.

Análise por Cliente: Avaliação da variabilidade de taxas e comportamento de transações por cliente.

Uniformidade de Preços: Comparação das taxas médias para clientes novos e recorrentes.

Fase 2: Modelagem Preditiva de Sensibilidade a Preços

Objetivo: Construir um modelo preditivo para entender como mudanças na nossa taxa de serviço podem afetar o volume de transações, permitindo simular cenários estratégicos.

Modelo: RandomForestRegressor do scikit-learn, treinado com dados agregados por corredor e data.

Variáveis-Chave:

Features (X): media_taxa, media_diferenca_taxa, media_taxa_concorrente.

Target (y):volume_transacoes.

Fase 3: Design de Experimentos de Precificação (Teste A/B Simulado)

Objetivo: Validar uma hipótese de negócio com um experimento rigoroso, simulando uma alteração de preço e avaliando o impacto no volume e receita.

Design: Criação de Grupo de Controle e Grupo de Teste com uma alteração de preço, seguida de uma análise estatística (t-test) para determinar a significância dos resultados.

Principais Conclusões e Descobertas
Vantagem Competitiva de Preço: A NALAsy opera com taxas médias de serviço consistentemente mais baixas que a concorrência em todos os corredores, refutando a suspeita inicial da diretoria.

EUA -> Brasil: NALAsy (2.50%) vs. Concorrentes (2.64%)

Portugal -> Moçambique: NALAsy (3.49%) vs. Concorrentes (3.63%)

Reino Unido -> Quénia: NALAsy (1.51%) vs. Concorrentes (1.69%)

Estratégia de Preços Uniforme: A NALAsy não diferencia a precificação entre clientes novos e recorrentes, o que representa uma oportunidade de melhoria.

Oportunidade no Corredor Crítico: O corredor Reino Unido para Quénia gera a menor receita total ($26.516), apesar de ter um volume de transações elevado, devido às suas taxas de serviço consistentemente baixas.

Modelo Preditivo: O RandomForestRegressor alcançou um R² de 0.34, indicando que as variáveis de preço explicam 34% da variação no volume de transações.

Validação de Hipótese (Teste A/B): A simulação da redução de 1% na taxa do corredor Portugal -> Moçambique mostrou que:

Houve um ligeiro aumento no volume de transações, mas essa diferença não foi estatisticamente significativa (p-value = 0.1289).

A mudança resultou numa perda substancial de receita (queda de $30.191 para $22.556).

Recomendações Estratégicas
Com base nas conclusões deste projeto, as seguintes recomendações são propostas para a diretoria da NALAsy:

Otimização de Preços no Reino Unido -> Quénia: Implementar um teste gradual de aumento de preços neste corredor. O modelo preditivo sugere que um aumento moderado pode levar a um aumento da receita sem um impacto significativo na perda de clientes.

Desenvolvimento de um Programa de Fidelização: Explorar a implementação de preços diferenciados ou recompensas para clientes recorrentes nos corredores de maior receita (Portugal -> Moçambique e EUA -> Brasil), utilizando o preço como ferramenta para reter clientes.

Investigação Adicional: Aprofundar a análise para identificar outros fatores (exemplo: Sazonalidade, eventos de marketing) que possam influenciar o volume de transações, para melhorar a capacidade preditiva do modelo.

Tecnologias Utilizadas
Linguagem: Python

Bibliotecas: 
pandas
numpy
scikit-learn
matplotlib
seaborn
scipy