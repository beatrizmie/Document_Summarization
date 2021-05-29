# Document_Summarization

O LSA (Latent Semantic Allocation) de Dirichlet foi o modelo estatístico generativo escolhido para a extração de sentenças importantes a partir de um documento de texto. A partir da matriz termo-documento de frequências de palavras em documentos gerada, foi aplicada a técnica de seleção de sentenças de Steinberger e Jezek, a qual utiliza o cálculo do tamanho da sentença para extrair as mais importantes e assim formar o sumário com tais sentenças. 

Para obter um sumário a partir do arquivo de teste, basta rodar:

```
python summarize.py
```

Depois, escolha o número de sentenças desejado (por exemplo 5), e o programa vai gerar um sumário do texto!

Texto retirado do artigo: https://www.nasa.gov/feature/nasa-rover-to-search-for-water-other-resources-on-moon