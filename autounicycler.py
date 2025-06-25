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
    
