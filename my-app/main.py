import flet as ft
from DataBase.db import MeuBanco
from urllib.parse import quote_plus
from time import sleep
# Criação da conexão com o MongoDB
username = "newtonaraujo6"
password = "Lorenzo@7045"  
encoded_password = quote_plus(password)

data_connection = f"mongodb+srv://{username}:{encoded_password}@systemmydoctor.8cxo4.mongodb.net/?retryWrites=true&w=majority&appName=SystemMyDoctor"
connection_db = MeuBanco(data_connection, 'SystemMyDoctor') 

def main(page: ft.Page):
    page.bgcolor = "#71D4D6"
    page.window_max_width = 812
    page.window_max_height = 375
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.update()

    #Variaveis com os dados do usuario
    nm_user = ft.TextField(
                            label="NOME",
                            width=250,
                            height=35,
                            prefix_icon=ft.icons.ACCOUNT_BOX,
                            color=ft.colors.BLACK,
                            label_style=ft.TextStyle(
                                size=13
                            )
                        )
    email_user = ft.TextField(
                            label="EMAIL",
                            width=250,
                            height=35,
                            prefix_icon=ft.icons.EMAIL,
                            color=ft.colors.BLACK,
                            label_style=ft.TextStyle(
                                size=13
                            )
                        )
    cpf = ft.TextField(
            label="CPF",
            width=250,
            height=35,
            prefix_icon=ft.icons.PERM_IDENTITY,
            color=ft.colors.BLACK,
            label_style=ft.TextStyle(
            size=13
            ),
        )
    password = ft.TextField(
            label="SENHA",
            width=250,
            height=35,
            prefix_icon=ft.icons.PASSWORD,
            color=ft.colors.BLACK,
            password=True,
            can_reveal_password=True,
            label_style=ft.TextStyle(
            size=13
            )                
        )
    confirme_password = ft.TextField(
            label="CONFIRMA SENHA",
            width=250,
            height=35,
            prefix_icon=ft.icons.PASSWORD,
            color=ft.colors.BLACK,
            password=True,
            can_reveal_password=True,
            label_style=ft.TextStyle(
            size=13
                )
            )
    
    #Variaveis do RESET SENHA
    new_password = ft.TextField(
            label="NOVA SENHA",
            width=250,
            height=35,
            prefix_icon=ft.icons.PASSWORD,
            color=ft.colors.BLACK,
            password=True,
            can_reveal_password=True,
            label_style=ft.TextStyle(
            size=13,
            ),
            disabled=True                
        )
    confirm_new_password =ft.TextField(
            label="REPETIR SENHA",
            width=250,
            height=35,
            prefix_icon=ft.icons.PASSWORD,
            color=ft.colors.BLACK,
            password=True,
            can_reveal_password=True,
            label_style=ft.TextStyle(
            size=13
            ),
            disabled=True                
        )


    #---CADASTRAR USUARIO
    def cadastrar_usuario():
        page.clean()
        
        #Salvar Usuario
        def salvar_usuario(e, nome,email,cpf_user,user_password,user_conf_password):
            
            try:
                #Condição para verificar se os campos estao preenchidos
                if not (nome and email and cpf_user and user_password and user_conf_password):
                    page.snack_bar = ft.SnackBar(
                        content=ft.Text(value="Prencha todos os campos!",color=ft.colors.WHITE),
                        bgcolor=ft.colors.RED,
                    )
                    page.snack_bar.open =True
                    page.update()
                    return
                    
                #Condição para verificar se as senhas conferem 
                if user_password != user_conf_password:
                    page.snack_bar = ft.SnackBar(
                        content=ft.Text(
                            value="Senhas não Conferem",
                            color=ft.colors.WHITE
                            ),
                        bgcolor=ft.colors.RED
                    )
                    page.snack_bar.open = True
                    page.update()
                    return
                
                #Dicionario com os dados do usuario
                dados ={
                    "nome":nome,
                    "email":email,
                    "cpf":cpf_user,
                    "password":user_password,
                    "conf_password":user_conf_password
                }
                
                print(dados)
                
                #Conexao com a collection
                colecao = connection_db.db['usuarios']
                
                #Retorno dos dados do banco -- TRUE (Caso os dados sejam salvo) False(Caso os dados já existem)
                result = connection_db.adicionar_dados(colecao,dados)
                
                #Caso o cadastro seja efetuado aparecera uma mensagem para o usuario
                if result:
                    page.snack_bar = ft.SnackBar(
                        content=ft.Text(value="Cadastrado com sucesso",color=ft.colors.WHITE),
                        bgcolor=ft.colors.GREEN_300
                    )
                    page.snack_bar.open = True
                    page.update()
                    
                    #RESENTANDO OS VALORES
                    nm_user.value = ""
                    email_user.value = ""
                    cpf.value = ""
                    password.value = ""
                    confirme_password.value = ""
                    
                    pagina_inicial()
                    
                #Caso o CPF já conste na base de dados o usuario sera informado
                else:
                    page.snack_bar = ft.SnackBar(
                        content=ft.Text(value="CPF já Cadastrado",color=ft.colors.WHITE),
                        bgcolor=ft.colors.RED
                    )
                    page.snack_bar.open = True
                    page.update()
                    return
                #Em caso de erro aparecera uma mensagem para o usuario pedindo para entrar em contato com o SUPORTE
            except NameError as e:
                    page.snack_bar = ft.SnackBar(
                        content=ft.Text(value="POR FAVOR ENTRE EM CONTATO COM O SUPORTE",color=ft.colors.BLACK),
                        bgcolor=ft.colors.YELLOW
                    )
                    page.snack_bar.open = True
                    page.update()
                    
        #-- TITULO DO CADASTRO
        titulo_cadastrar = ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(ft.icons.ACCOUNT_CIRCLE,size=100)  # Correção do uso do ícone
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Text(
                            value="NOVO CADASTRO",
                            color=ft.colors.BLACK,
                            weight=ft.FontWeight.BOLD,
                            size=25
                            )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )
        
        #-- DADOS DO USUARIOS
        dados_usuario = ft.Row(
            [
                ft.Column(
                    [ #INPUT COM O DADOS DO USUARIO
                        nm_user,
                        email_user,
                        cpf,
                        password,
                        confirme_password,
                    ]       
                )
                
            ],alignment=ft.MainAxisAlignment.CENTER
            
        )
        
        botoes_cadastrar_voltar = ft.Row(
            [
                ft.Column(
                    [
                        ft.Container(
                            width=250,
                            height=40,
                            content=ft.Row(
                                [
                                    ft.ElevatedButton(
                                        text="CADASTRAR",
                                        bgcolor=ft.colors.GREEN_400,
                                        color=ft.colors.WHITE,
                                        on_click= lambda e: salvar_usuario(e,nm_user.value,email_user.value,cpf.value,password.value,confirme_password.value)
                                        ),
                                     ft.ElevatedButton(
                                        text="SAIR",
                                        icon=ft.icons.ARROW_BACK,
                                        bgcolor=ft.colors.BLUE_300,
                                        color=ft.colors.WHITE,
                                        on_click= lambda _: pagina_inicial()
                                        ),

                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            )
                        )
                    ]
                    
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        
        #Dimensões do container -- TELA DE CADASTRO
        pg_cadastrar = ft.Container(
        bgcolor=ft.colors.WHITE,
        width=500,
        height=500,
        border_radius=ft.border_radius.all(10),
        margin=ft.margin.only(right=2, left=2),
        shadow=ft.BoxShadow(
            blur_radius=60,
            spread_radius=2,
            color=ft.colors.BLACK45,
            offset=ft.Offset(1, 1)
        ),
        content=ft.Column(
            [
                ft.Container(#Container do TITULO
                    width=500,
                    margin=ft.margin.only(top=30),
                    content=titulo_cadastrar
                ),
                  ft.Container(#Container do TITULO
                    width=500,
                    margin=ft.margin.only(top=10),
                    content=dados_usuario
                ),
                    ft.Container(#Container do TITULO
                    width=500,
                    margin=ft.margin.only(top=10),
                    content=botoes_cadastrar_voltar
                ),
            ]
        )
    )
        page.add(pg_cadastrar)
    
    #TELA -  RESET SENHA 
    def reset_senha():
        page.clean()
        #--Titulo de RESET SENHA
        titulo_reset = ft.Column(
            [
                ft.Row([
                    ft.Icon(
                        ft.icons.MANAGE_ACCOUNTS,
                        size=100,
                        color=ft.colors.BLACK
                        )
                ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Text(
                            value="Redefinir Senha",
                            color=ft.colors.BLACK45,
                            size=30
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
                
            ],
            spacing=0
        )
        
        #--Informaçoes para o usuarios
        infor_msg_reset = ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            width=250,
                            height=25,
                            border_radius=ft.border_radius.all(10),
                            content=ft.Row(
                                [
                                    ft.Text(
                                        value="Informe seu CPF ou EMAIL cadastrados",
                                        size=12,
                                        color=ft.colors.BLUE,
                                        weight=ft.FontWeight.BOLD
                                        )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            )
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ]
        )
        
        #--Dados para RESETAR SENHA
        dados_user_reset = ft.Row(
            [
                ft.Column(
                    [
                        email_user,
                        cpf,
                        new_password,
                        confirm_new_password
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ) 
        
        #--Botoes ---> BUSCAR E SALVAR
        botoes_reset = ft.Row(
            [
                ft.Container(
                    width=250,
                    content=ft.Row(
                        [
                            ft.ElevatedButton(
                                text="BUSCAR",
                                bgcolor=ft.colors.BLUE_400,
                                color=ft.colors.WHITE,
                                icon=ft.icons.SEARCH
                                #-- IMPLANTAR FUNCAO PARA BUSCAR CPF OU EMAIL
                                ),
                            ft.ElevatedButton(
                                text="SALVAR",
                                bgcolor=ft.colors.GREEN_300,
                                color=ft.colors.WHITE,
                                icon=ft.icons.SAVE,
                                on_click= lambda _: pagina_inicial() #-- IMPLANTAR FUNÇAO PARA SALVAR NOVA SENHA
                                
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),  
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        #--Configuração do Container - RESET SENHA
        pg_esqueci_senha = ft.Container(
        bgcolor=ft.colors.WHITE,
        width=500,
        height=500,
        border_radius=ft.border_radius.all(10),
        margin=ft.margin.only(right=2, left=2),
        shadow=ft.BoxShadow(
            blur_radius=60,
            spread_radius=2,
            color=ft.colors.BLACK45,
            offset=ft.Offset(1, 1)
        ),
        content=ft.Column(
            [
                ft.Container(#Container do TITULO
                    width=500,
                    margin=ft.margin.only(top=50),
                    content=titulo_reset
                ),
                ft.Container(#Container do TITULO
                    width=500,
                    margin=ft.margin.only(top=-10),
                    content=infor_msg_reset
                ),
                ft.Container(#Container do TITULO
                    width=500,
                    margin=ft.margin.only(top=-10),
                    content=dados_user_reset
                ),  
                ft.Container(#Container do TITULO
                    width=500,
                    margin=ft.margin.only(top=10),
                    content=botoes_reset
                ),
                
            ]
        )
    )
        page.add(pg_esqueci_senha)
    
    #--PAGINA INICIAL
    def pagina_inicial():
        page.clean()
        # Título - LOGIN
        titulo = ft.Column(
            [
                ft.Row(
                    [
                        ft.Image(src="images/cruzazul.png", width=100)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.Text(
                            value="MyDoctor",
                            size=40,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.BLACK
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            spacing=0
        )
        #Login - EMAIL E SENHA
        login = ft.Column(
            [
                ft.Row(
                    [
                        ft.TextField(
                            label="EMAIL",
                            width=250,
                            height=40,
                            prefix_icon=ft.icons.EMAIL,
                            color=ft.colors.BLACK,
                            
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.TextField(
                            label="PASSWORD",
                            width=250,
                            height=40,
                            prefix_icon=ft.icons.PASSWORD,
                            color=ft.colors.BLACK,
                            password=True,
                            can_reveal_password=True
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            spacing=10
        )
        #Botoes - ENTRAR,CADASTRAR e ESQUECI MINHA SENHA
        botoes_tela_login = ft.Column(
            [
                ft.Row(
                    [
                    ft.ElevatedButton(
                        text="ENTRAR", #----- ENTRAR
                        bgcolor=ft.colors.GREEN_300,
                        color=ft.colors.WHITE,
                        on_click=lambda _:print("Criar função para Entrar no sistema")
                        
                        ),
                    ft.ElevatedButton(
                        text="CADASTRAR", #------ CADASTRAR
                        bgcolor=ft.colors.BLUE_400,
                        color=ft.colors.WHITE,
                        on_click=lambda e: cadastrar_usuario()
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                    ft.TextButton(
                        text="ESQUECI MINHA SENHA", #------- ESQUECI SENHA
                        style=ft.ButtonStyle(
                            bgcolor=ft.colors.WHITE,
                            color=ft.colors.RED,
                            ),
                        on_click=lambda _:reset_senha()
                        
                    )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            spacing=5
        )
        
            # Container - PÁGINA INICIAL
        pg_inicial = ft.Container(
            bgcolor=ft.colors.WHITE,
            width=500,
            height=500,
            border_radius=ft.border_radius.all(10),
            margin=ft.margin.only(right=2, left=2),
            shadow=ft.BoxShadow(
                blur_radius=60,
                spread_radius=2,
                color=ft.colors.BLACK45,
                offset=ft.Offset(1, 1)
            ),
            content=ft.Column(
                [
                    ft.Container(#Container do TITULO
                        width=500,
                        margin=ft.margin.only(top=60),
                        content=titulo
                    ),
                    ft.Container(#Container do LOGIN - EMAIL E SENHA
                        width=500,
                        height=100,
                        margin=ft.margin.only(top=20),
                        content=login
                    ),
                    ft.Container(#Container do TITULO
                        width=500,
                        height=100,
                        # margin=ft.margin.only(top=10),
                        content=botoes_tela_login
                    ),
                    
                    
                ]
            )
        )

        page.add(pg_inicial)

        
        

    
    pagina_inicial()
ft.app(main,assets_dir="assets")
