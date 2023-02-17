from flask import request, Flask, send_file, render_template, url_for
from college_workbook import create
from openpyxl import load_workbook
app = Flask(__name__)
app.templates_auto_reload = True


courses_21 = ['ARTES VISUAIS ', 'CIÊNCIA DA COMPUTAÇÃO ', 'CIÊNCIAS BIOLÓGICAS ', 'CIÊNCIAS SOCIAIS ', 'DESIGN', 'EDUCAÇÃO FÍSICA ', 'FILOSOFIA ', 'FÍSICA ', 'GEOGRAFIA ', 'HISTÓRIA ', 'LETRAS - INGLÊS ', 'LETRAS-PORTUGUÊS ', 'LETRAS-PORTUGUÊS E ESPANHOL ', 'LETRAS-PORTUGUÊS E INGLÊS ', 'MATEMÁTICA ', 'MÚSICA ', 'PEDAGOGIA ', 'QUÍMICA ', 'SISTEMAS DE INFORMAÇÃO', 'TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS', 'TECNOLOGIA EM GESTÃO DA TECNOLOGIA DA INFORMAÇÃO', 'TECNOLOGIA EM REDES DE COMPUTADORES']

courses_19 = ['MEDICINA VETERINÁRIA', 'ODONTOLOGIA', 'MEDICINA', 'AGRONOMIA', 'FARMÁCIA', 'ARQUITETURA E URBANISMO', 'ENFERMAGEM', 'FONOAUDIOLOGIA', 'NUTRIÇÃO', 'FISIOTERAPIA', 'ZOOTECNIA', 'BIOMEDICINA', 'TECNOLOGIA EM RADIOLOGIA', 'TECNOLOGIA EM AGRONEGÓCIOS', 'TECNOLOGIA EM GESTÃO HOSPITALAR', 'TECNOLOGIA EM GESTÃO AMBIENTAL', 'TECNOLOGIA EM ESTÉTICA E COSMÉTICA', 'EDUCAÇÃO FÍSICA (BACHARELADO)', 'ENGENHARIA DA COMPUTAÇÃO', 'ENGENHARIA CIVIL', 'ENGENHARIA ELÉTRICA', 'ENGENHARIA DE CONTROLE E AUTOMAÇÃO', 'ENGENHARIA MECÂNICA', 'ENGENHARIA DE ALIMENTOS', 'ENGENHARIA QUÍMICA', 'ENGENHARIA DE PRODUÇÃO', 'ENGENHARIA AMBIENTAL', 'ENGENHARIA FLORESTAL', 'TECNOLOGIA EM SEGURANÇA NO TRABALHO']

courses_18 = ['DIREITO', 'CIÊNCIAS ECONÔMICAS', 'SERVIÇO SOCIAL', 'CIÊNCIAS CONTÁBEIS', 'ADMINISTRAÇÃO', 'RELAÇÕES INTERNACIONAIS', 'COMUNICAÇÃO SOCIAL - JORNALISMO', 'PSICOLOGIA', 'SECRETARIADO EXECUTIVO', 'TURISMO', 'TEOLOGIA', 'DESIGN', 'COMUNICAÇÃO SOCIAL - PUBLICIDADE E PROPAGANDA', 'ADMINISTRAÇÃO PÚBLICA', 'TECNOLOGIA EM GASTRONOMIA', 'TECNOLOGIA EM DESIGN DE MODA', 'TECNOLOGIA EM GESTÃO DE RECURSOS HUMANOS', 'TECNOLOGIA EM MARKETING', 'TECNOLOGIA EM GESTÃO FINANCEIRA', 'TECNOLOGIA EM DESIGN DE INTERIORES', 'TECNOLOGIA EM PROCESSOS GERENCIAIS', 'TECNOLOGIA EM GESTÃO DA QUALIDADE', 'TECNOLOGIA EM DESIGN GRÁFICO', 'TECNOLOGIA EM LOGÍSTICA', 'TECNOLOGIA EM GESTÃO COMERCIAL', 'TECNOLOGIA EM COMÉRCIO EXTERIOR', 'TECNOLOGIA EM GESTÃO PÚBLICA'] + courses_19 + courses_21

states = ['MT', 'DF', 'SE', 'AM', 'PI', 'MG', 'PR', 'PE', 'RS', 'RJ', 'SP', 'BA', 'CE', 'SC', 'GO', 'RN', 'ES', 'PB', 'PA', 'MS', 'RO', 'TO', 'AL', 'MA', 'AC', 'RR', 'AP']

adm_category = ['Pública Federal', 'Pública Estadual', 'Privada sem fins lucrativos', 'Pública Municipal', 'Privada com fins lucrativos', 'Especial']

@app.route('/<path:year>/<path:ws_type>/<path:raw_courses>/<path:UFs>/<path:adm_category>', methods=['POST', 'GET'])
def save_file(year, ws_type, raw_courses, UFs, adm_category):
    raw_courses = raw_courses.replace('_', ' ')
    courses = raw_courses.split(';')
    file = create(ws_type=ws_type, year=year, courses=courses, UFs=UFs, adm_category=adm_category)
    return send_file(file)
@app.route('/')
def index():
    return render_template('index.html', cursos2018 = courses_18, states = states, adm_category = adm_category)
