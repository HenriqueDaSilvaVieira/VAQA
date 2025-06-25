<p align="right">
  <img src="https://github.com/user-attachments/assets/a3b067ad-732b-42cb-9331-c6f74ec7c061">
</p>



# V.A.Q.A: Visualization, Assembly, Quality, Automated

**V.A.Q.A** is a fully automated pipeline designed to simplify the process of genomic assembly and quality assessment from paired FASTQ files - with just **one command line**.

💡 O V.A.Q.A realizes:
- The assembly of multiple genomes with **Unicycler**;
- Quality assessment with **QUAST;
- The generation of graphs with the main **assembly quality metrics**.

---

## 🧬 Application

Initially designed to support genomic investigations of **pathogens in clinical outbreaks** in the context of **veterinary hospitals**, V.A.Q.A is also applicable to **any genomic project** involving multiple samples and requiring a reproducible and scalable workflow.

---

## 🚀 Features

- 🔁 Automated processing of multiple samples with paired FASTQ files  
- Genome assembly with **Unicycler (SPAdes)**  
- Quality assessment with **QUAST**  
- Graphical visualization of the main metrics:
  - Number of contigs;
  - Total genome size;
  - N50 and L50;
  - GC Content.
- Automatic organization of results in folders by sample  

---

## 📂 Expected entry

A directory containing the paired read files in `.fastq`, `.fq` or `.gz` format.

📌 Files must follow the following naming convention, with the same base identifier and suffixes `_R1` and `_R2` indicating the pairs:

IDENTIFIER_R1.fastq IDENTIFIER_R2.fastq

### Example:

VSF3096_R1.fastq VSF3096_R2.fastq

VSF3099_R1.fastq VSF3099_R2.fastq

## 📤 Outputs generated

For **each sample**, V.A.Q.A produces it automatically:

- Assembled genome (`.fasta`)  
- Reports from **QUAST** (`.tsv`,`.html`, `.txt`)  
- Summary table with the main metrics of all the samples  
- Aggregate charts:
  - Distribution of **N50** and **L50**
  - Total genome size
  - GC content per sample
  - Number of contigs per genome
    
---

## 🛠️ Arguments

- `-i` or `--input`: path to the directory with the FASTQ files
- `-o` or `--output`: directory where the results will be saved

---

## 🧪 Requirements

- Python ≥ 3.7  
- [Unicycler](https://github.com/rrwick/Unicycler)  
- [QUAST](https://github.com/ablab/quast)  

### Python libraries:
- pandas  
- matplotlib  
- seaborn  

---

## 📦 Installation and use

Clone the repository and install the requirements:

```bash
git clone https://github.com/HenriqueDaSilvaVieira/VAQA.git
cd VAQA
pip install -r requirements.txt

python3 vaqa.py -i ./caminho_para_arquivos_fastq -o ./resultados


