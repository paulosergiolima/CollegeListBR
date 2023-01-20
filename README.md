# CollegeListBR
## Descrição
Cria uma duas planilhas baseada nos indices do ENADE e do IDD, uma métrica para cursos de Instituições de Ensino Superior Brasileiras.

## Como usar
Existem dois metódos de utilisar, pelo college_workbook.py diretamente, ou rodando o main.py e escolhendo os cursos na interface web.
### Interface web
Escolha o ano na caixa "Year" e os cursos na caixa "Courses". Quando estiver escolhendo os cursos, escreva eles usando o nome que é utilizado no arquivo original do MEC, e tudo em Maisculo. Os cursos são divididos usando ;.
### CLI
Edite o array chamado courses no arquivo college_workbook.py e rode ele.

## Anos
Devido ao método que o MEC utiliza para verificar os cursos, divindo ás áreas em 3 anos com planilhas diferentes, atualmente cada ano é uma opção quando o script é rodado, a junção de todos os cursos verificados nesses três anos em só uma pasta é uma feauture planejada

