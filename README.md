# V.A.Q.A: Visualization, Assembly, Quality, Automated

**V.A.Q.A** é um pipeline totalmente automatizado desenvolvido para simplificar o processo de montagem genômica e avaliação da qualidade a partir de arquivos FASTQ pareados — com apenas **uma linha de comando**.

💡 O V.A.Q.A realiza:
- A montagem de múltiplos genomas com o **Unicycler**
- A avaliação da qualidade com **QUAST**
- A geração de gráficos com as principais **métricas de qualidade da montagem**

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

📌 Os arquivos devem seguir a seguinte convenção de nomes, com o mesmo identificador base e sufixos `_R1` e `_R2` indicando os pares:

IDENTIFICADOR_R1.fastq IDENTIFICADOR_R2.fastq

### ✅ Exemplo:

VSF3096_R1.fastq VSF3096_R2.fastq

VSF3099_R1.fastq VSF3099_R2.fastq

## 📤 Saídas geradas

Para **cada amostra**, o V.A.Q.A produz automaticamente:

- ✅ Genoma montado (`.fasta`)  
- 📄 Relatórios do **QUAST** (`.tsv`,`.html`, `.txt`)  
- 📊 Tabela resumo com as principais métricas de todas as amostras  
- 📉 Gráficos agregados:
  - Distribuição do **N50** e **L50**
  - Tamanho total dos genomas
  - Conteúdo GC por amostra
  - Número de contigs por genoma
    
---

## 🛠️ Argumentos

- `-i` ou `--input`: caminho para o diretório com os arquivos FASTQ  
- `-o` ou `--output`: diretório onde os resultados serão salvos

---

## 🧪 Requisitos

- Python ≥ 3.7  
- [Unicycler](https://github.com/rrwick/Unicycler)  
- [QUAST](https://github.com/ablab/quast)  

### Bibliotecas Python:
- pandas  
- matplotlib  
- seaborn  

---

## 📦 Instalação

Clone o repositório e instale os requisitos:

```bash
git clone https://github.com/HenriqueDaSilvaVieira/VAQA.git
cd VAQA
pip install -r requirements.txt

## ⚙️ Exemplo de uso

Execute o pipeline com:

```bash
python3 vaqa.py -i ./caminho_para_arquivos_fastq -o ./resultados


