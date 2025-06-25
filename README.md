# V. A. Q. A:  Visualization, Assembly, Quality, Automated

**V.A.Q.A** é um pipeline totalmente automatizado desenvolvido para simplificar o processo de montagem genômica e avaliação da qualidade a partir de arquivos FASTQ pareados, com apenas **uma linha de comando**.

💡 O V.A.Q.A realiza:
- A montagem de múltiplos genomas com o **Unicycler**
- A avaliação da qualidade com **QUAST**
- A geração de gráficos com as principais **métricas da montagem**

---

## 🧬 Aplicação

Inicialmente pensado para apoiar investigações genômicas de **patógenos em surtos clínicos** no contexto de **hospitais veterinários**, o V.A.Q.A também é aplicável a **qualquer projeto genômico** que envolva múltiplas amostras e exija um fluxo de trabalho reprodutível e escalável.

---

## 🚀 Funcionalidades

- 🔁 Processamento automatizado de múltiplas amostras com arquivos FASTQ pareados
- 🧪 Montagem de genomas com **Unicycler (SPAdes)**
- 📊 Avaliação da qualidade com **QUAST**
- 📈 Visualização gráfica das principais métricas:
  - Número de contigs
  - Tamanho total do genoma
  - N50 e L50
  - Conteúdo GC
- 📁 Organização automática dos resultados em pastas por amostra

---

## 📂 Entrada esperada

Um diretório contendo os arquivos de leitura pareados nos formatos `.fastq`, `.fq` ou `.gz`.

📌 Os arquivos devem seguir a seguinte convenção de nomes:
