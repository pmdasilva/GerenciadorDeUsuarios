from flask import Flask,url_for, render_template

# Inicialização do flask __name__ somente para ele organizar as informações do projeto.
app = Flask(__name__, template_folder='template')



# Criando uma rota
@app.route("/")
def main_page():
    titulo = 'Gestão de usuarios'
    usuarios = [
        {'nome':'Paulo Silva','membro_ativo':True},
        {'nome':'Marcelo','membro_ativo':False},
        {'nome':'Luis','membro_ativo':True},
        {'nome':'Marcelo','membro_ativo':True},
        {'nome':'Paulo','membro_ativo':False},
        {'nome':'Luiza','membro_ativo':True},
        {'nome':'Jose','membro_ativo':False},

    ]
    return render_template('index.html',titulo=titulo, usuarios=usuarios)

@app.route("/sobre")
def about_page():
    titulo1 = 'Lista de usuarios'
    return render_template('sobre.html',titulo1=titulo1)

# Função responsavél por execultar o nosso servidor.
# debbug =True estamos dizendo ao flask que estamos no modo desenvolvedor ou, seja ela vai atualizar todos as modificações automaticamente no projeto assim que salvamos o arquivo.
app.run(debug=True)