# CollegeListBR
## Descrição
Cria uma duas planilhas baseada nos indices do ENADE e do IDD, uma métrica para cursos de Instituições de Ensino Superior Brasileiras.

## Como usar
A implementação do docker compose ainda não foi terminada, por enquanto rode esses comandos:
pip3 install -r requirements.txt
python main.py
Modifique o array chamado courses com o(s) curso(s) que você que aparecem na planilha criada, formatados com strings, e escolha o ano em que o esses cursos participaram

## Anos
Devido ao método que o MEC utiliza para verificar os cursos, divindo ás áreas em 3 anos com planilhas diferentes, atualmente cada ano é uma opção quando o script é rodado, a junção de todos os cursos verificados nesses três anos em só uma pasta é uma feauture planejada

