#!/usr/bin/env python3

import os
import argparse
import subprocess
import sys

def validate_input_directory(diretorio):
    if not os.path.isdir(diretorio):
        print(f"ERRO: Diretório de entrada inválido: {diretorio}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Running AutoUnicycler')
    parser.add_argument('-i', '--input', metavar='', type=str, required=True,
                        help='Path to the input files, e.g.: /home/user/myfiles')
    parser.add_argument('-t', '--thread', metavar='', type=int, required=False, default=1,
                        help='[OPTIONAL] Number of threads, e.g.: 8 (default=1)')
    args = parser.parse_args()

    diretorio = os.path.expanduser(args.input)
    validate_input_directory(diretorio)

    extensoes = ['.fastq', '.fq', '.gz']  
    output_dir = os.path.join(diretorio, 'results_autounicycler')
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    pares = {}

    
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith(tuple(extensoes)):
            if '_R1' in arquivo:
                nome_amostra = arquivo.split('_R1')[0]
                pares.setdefault(nome_amostra, {})['R1'] = arquivo
            elif '_R2' in arquivo:
                nome_amostra = arquivo.split('_R2')[0]
                pares.setdefault(nome_amostra, {})['R2'] = arquivo

    if not pares:
        print(f"Nenhum par de arquivos R1/R2 foi encontrado em {diretorio}", file=sys.stderr)
        sys.exit(1)

    for amostra, arquivos in pares.items():
        if 'R1' in arquivos and 'R2' in arquivos:
            print(f"Montando amostra: {amostra}")

            caminho_r1 = os.path.join(diretorio, arquivos['R1'])
            caminho_r2 = os.path.join(diretorio, arquivos['R2'])

            out_amostra = os.path.join(output_dir, amostra)
            if not os.path.exists(out_amostra):
                os.mkdir(out_amostra)

            
            cmd = [
                'unicycler',
                '-1', caminho_r1,
                '-2', caminho_r2,
                '-o', out_amostra,
                '-t', str(args.thread)
            ]

            print(f"Executando: {' '.join(cmd)}")
            try:
                subprocess.run(cmd, check=True)
                print(f"Montagem da amostra {amostra} concluída com sucesso.")
            except subprocess.CalledProcessError as e:
                print(f"Erro na montagem da amostra {amostra}: {e}", file=sys.stderr)
        else:
            print(f"ATENÇÃO: Amostra {amostra} não possui par R1 e R2 completos.", file=sys.stderr)

if __name__ == "__main__":
    main()

#Auto Quast
#!/usr/bin/env python3

import glob
import subprocess
import os

def rodar_quast_em_fasta(pasta_dos_fasta='.', pasta_saida_quast='quast_output'):
    print("Procurando arquivos .fasta para rodar o QUAST...")

    fasta_files = glob.glob(os.path.join(pasta_dos_fasta, '*.fasta'))

    if not fasta_files:
        print("Nenhum arquivo .fasta encontrado para rodar o QUAST.")
        return

    os.makedirs(pasta_saida_quast, exist_ok=True)

    cmd = ["quast.py", "-o", pasta_saida_quast] + fasta_files

    print(f"Executando QUAST com {len(fasta_files)} arquivos...")
    print(" ".join(cmd))

    try:
        subprocess.run(cmd, check=True)
        print("QUAST finalizado com sucesso. Resultados em:", pasta_saida_quast)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao rodar QUAST: {e}")
        return


    print("Gerando gráficos com base nos relatórios do QUAST...")
    try:
        subprocess.run(["python3", "plotmetrics.py", "-i", pasta_saida_quast], check=True)
        print("Gráficos gerados com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao gerar gráficos: {e}")

if __name__ == "__main__":
    rodar_quast_em_fasta()

#plotmetrics
#!/usr/bin/env python3

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

sns.set(style="whitegrid")
plt.rcParams.update({'figure.dpi': 150})

report_path = 'quast_output/report.tsv'
output_dir = 'graficos'

os.makedirs(output_dir, exist_ok=True)

try:
    df_raw = pd.read_csv(report_path, sep='\t', index_col=0)
    df = df_raw.transpose()
    df.index.name = "Assembly"
    df.reset_index(inplace=True)
except FileNotFoundError:
    print(f"Arquivo {report_path} não encontrado.")
    exit(1)

graficos = {
    "GC (%)": {"tipo": "bar", "nome": "gc_barplot.png", "titulo": "GC (%)"},
    "# contigs": {"tipo": "bar", "nome": "contigs_barplot.png", "titulo": "Número de contigs"},
    "Total length": {"tipo": "bar", "nome": "total_length_barplot.png", "titulo": "Tamanho total do genoma (pb)"},
    "N50": {"tipo": "bar", "nome": "n50_barplot.png", "titulo": "N50 (pb)"},
    "L50": {"tipo": "bar", "nome": "l50_barplot.png", "titulo": "L50"}
}

colunas_existentes = [col for col in graficos if col in df.columns]
if not colunas_existentes:
    print("Nenhuma das colunas esperadas foi encontrada.")
    exit(1)

df = df.dropna(subset=colunas_existentes)
df = df.sort_values("Assembly")

def ajustar_eixo_y(ax, coluna):
    min_val = df[coluna].min()
    max_val = df[coluna].max()
    delta = max_val - min_val

    if delta == 0:
        bottom = min_val - 1
        top = max_val + 1
    else:
        margin = delta * 0.2
        bottom = max(0, min_val - margin)
        top = max_val + margin

    ax.set_ylim(bottom, top)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x):,}'.replace(',', '.')))

def salvar_fig(nome_arquivo, titulo):
    plt.title(titulo, fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, nome_arquivo))
    plt.close()

for coluna, info in graficos.items():
    if coluna not in df.columns:
        print(f"Coluna '{coluna}' não encontrada.")
        continue

    plt.figure(figsize=(10, 5))
    ax = sns.barplot(
        x="Assembly",
        y=coluna,
        data=df,
        color="steelblue",
        width=0.4
    )
    ajustar_eixo_y(ax, coluna)
    salvar_fig(info["nome"], info["titulo"])

print(f"Gráficos salvos em: {output_dir}/")
