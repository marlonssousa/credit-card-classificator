import gradio as gr
from gradio_calendar import Calendar


def greet(name):
    return "Hello " + name + "!"


with gr.Blocks(title="Cartão de Crédito - Classificação") as demo:
    with gr.Row():
        with gr.Column():
            with gr.Row():
                genero = gr.Dropdown(["Masculino", "Feminino"], label="Gênero")
                carro = gr.Dropdown(["Sim", "Não"], label="Possui Carro Próprio?")
            with gr.Row():
                casa  = gr.Dropdown(["Sim", "Não"], label="Possui Casa Próprio?")
                crianca  = gr.Dropdown(["Sem Filho", "1 Filho", "2 ou mais Filhos"], label="Tem Filhos?")
            with gr.Row():
                renda  = gr.Number(label="Renda Total")
                education  = gr.Dropdown(["Fundamental", "Ensino Médio", "Ensino Médio Incompleto", "Ensino Superior"], label="Formação?")
            civil  = gr.Dropdown(["Casado", "Solteiro", "Casado Civil", "Divorciado", "Viuvo(a)"], label="Estado Civil")
            casa_tipo  = gr.Dropdown(["Casa / Apartamento", "Mora com os pais ou parentes", "Apartamento Municipal", "Apartamento alugado", "Apartamento escritório", "Apartamento cooperativo"], label="Tipo de Moradia")
            nascimento = Calendar(type="datetime", label="Data de Nascimento", info="Selectione sua data de nascimento.")
    
        with gr.Column():
            empregado = Calendar(type="datetime", label="Data que iniciou em seu emprego", info="Selecione o inicio de sua contratação.")
            celular = gr.Dropdown(["Sim", "Não"], label="Possui Telefone Celular?")
            telefone_comercia = gr.Dropdown(["Sim", "Não"], label="Possui Telefone Comercial?")
            telefone = gr.Dropdown(["Sim", "Não"], label="Possui Telefone?")
            email = gr.Dropdown(["Sim", "Não"], label="Possui Email?")
            emprego = gr.Dropdown(["Trabalhador", "Equipe Central", "Equipe de Vendas", "Gerentes", "Motorista", "Equipe Técnica", "Contador", "Medicina", "Cozinha", "Segurança", "Limpeza", "Serviço Privado", "Trabalhadores de baixa qualificação", "Secretário", "Garçons/Barmen", "Equipe de RH", "Equipe de TI", "Agentes imobiliários"], label="Tipo do seu Emprego?")
            greet_btn = gr.Button("Analisar")

        with gr.Column():
            gr.Text()
if __name__ == "__main__":
    demo.launch()
