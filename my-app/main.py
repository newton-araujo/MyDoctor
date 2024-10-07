import flet as ft
from DataBase.mydoctordb import new_cadastrar_usuario
from time import sleep


def main(page: ft.Page):
    page.bgcolor = "#71D4D6"
    page.window_max_width = 812
    page.window_max_height = 375
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.update()
    
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
                )
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

    def acessar(e, user, senha):
        if user == "newton" and senha == "admin":
            page.clean()
            menu_central()  # Certifique-se de que essa função esteja definida
            print("Deu certo")
            page.update()
        else:
            print(f"esse é o user: {user}")
            page.snack_bar = ft.SnackBar(
                content=ft.Text(value="Erro ao acessar", color=ft.colors.WHITE),
                bgcolor=ft.colors.RED
            )
            page.snack_bar.open = True
            page.update()
    
    #Menu central
    def menu_central():
        page.clean()
        
        opcoes = ft.Row( #Container opcoes
                [   
                    #Acresentar funcionalidade em todo os botões
                    
                    #titulo e boas vindas
                    ft.Container(
                        width=340,
                        height=80,
                        bgcolor='#71D4D6',
                        content=ft.Column(
                            [
                                ft.Container( #Boa vindas buscando o nome do usuario
                                    width=350,
                                    height=30,
                                    content=ft.Row( #Boa vindas buscando o nome do usuario
                                    [
                                        ft.Row(
                                                [
                                                    ft.Text(value=f"Olá {nm_user.value}",color=ft.colors.BLACK45,size=19)
                                                ],
                                    alignment=ft.MainAxisAlignment.END,
                                    width=330,
                                    height=20,
                                ),
                                    ],
                                    width=250,
                                    ),
                                    padding=ft.padding.all(2),
                                    margin=ft.margin.only(right=10)
                                ),
                                
                                ft.Container( #Titulo 
                                    width=350,
                                    height=50,
                                    content=ft.Row(#Descrição do titulo
                                        [   
                                            ft.Icon(name=ft.icons.MEDICAL_INFORMATION,color=ft.colors.WHITE,size=28),
                                            ft.Text(value="MYDOCTOR", color=ft.colors.WHITE,size=30,weight=ft.FontWeight.BOLD,)
                                        ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    width=250,
                                    height=40, 
                                ),
                                ),
                            ],
                            spacing=1
                            
                        ),
                        border_radius=ft.border_radius.all(10),
                        #padding=ft.padding.all(2)
                    ),
                    
                    #MINHA SAUDE
                    ft.Container(
                        width=150,
                        height=150,
                        bgcolor='#71D4D6',
                        border_radius=ft.border_radius.all(10),
                        content= ft.Column(
                            [
                                #Botão Minha Saude
                                ft.Container(
                                    width=150,
                                    height=120,
                                    content=ft.Column(
                                        [
                                            ft.Row(
                                                [
                                                ft.Container(#Container com ICON
                                                    width=100,
                                                    height=100,
                                                    bgcolor=ft.colors.BLACK45,
                                                    border_radius=ft.border_radius.all(50),
                                                    content=ft.Row(
                                                        [
                                                            ft.Icon(
                                                                name=ft.icons.MONITOR_HEART,
                                                                color=ft.colors.WHITE,
                                                                size=80
                                                            )
                                                    
                                                    
                                                    ],
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                ),
                                                margin=ft.margin.only(top=5)
                                                ),
                                                    ],
                                                width=150,
                                                alignment=ft.MainAxisAlignment.CENTER
                                            ),
                                            ft.Row( #Descriçao do BOX
                                                [
                                                    ft.Text(
                                                        value="Minha Saúde",
                                                        color=ft.colors.WHITE,
                                                        weight=ft.FontWeight.BOLD,
                                                        size=20,
                                                        )
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    )
                                    
                                )
                            ]
                        ),
                        on_click= lambda _:print("Minha Saúde") #Implantar funçao aqui
                    
                    ),
                    
                    #Meu cartao saúde
                    ft.Container(
                        width=150,
                        height=150,
                        bgcolor='#71D4D6',
                        border_radius=ft.border_radius.all(10), 
                        content=ft.Column(
                            [
                                ft.Container(
                                    width=150,
                                    height=120,
                                    content=ft.Column(
                                        [
                                            ft.Row(
                                                [
                                                ft.Container( #Botão Cartão Saude
                                                    width=100,
                                                    height=100,
                                                    bgcolor=ft.colors.BLACK45,
                                                    border_radius=ft.border_radius.all(50),
                                                    content=ft.Icon(
                                                        name=ft.icons.CREDIT_CARD,
                                                        color=ft.colors.WHITE,
                                                        size=80
                                                    )
                                                )
                                            ],
                                            width=150,
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            ),
                                            
                                            ft.Row(
                                                [
                                                    ft.Text( #Descrição do box cartão saude
                                                        value="Cartão Saúde",
                                                        color=ft.colors.WHITE,
                                                        weight=ft.FontWeight.BOLD,
                                                        size=20
                                                        )
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER
                                                
                                            ),
                                            
                                        ],
                                        
                                    ),
                                    margin=ft.margin.only(top=5)
                                ),
                            ],
                            
                            
                        ),
                        on_click= lambda _:print("Cartão saude") #Implantar função aqui
                        
                        
                    ),
                        
                    #Agendar Exames    
                    ft.Container(
                        width=150,
                        height=150,
                        bgcolor='#71D4D6',
                        border_radius=ft.border_radius.all(10),
                        content=ft.Column(
                            [
                                ft.Container(
                                    width=150,
                                    height=120,
                                    content=ft.Column(
                                        [
                                        ft.Row(
                                            [
                                                ft.Container(
                                                    width=100,
                                                    height=100,
                                                    bgcolor=ft.colors.BLACK45,
                                                    border_radius=ft.border_radius.all(50),
                                                    content=ft.Icon(
                                                                name=ft.icons.MEDICAL_INFORMATION,
                                                                color=ft.colors.WHITE,
                                                                size=75
                                                            )
                                                        
                                                    ,
                                                    margin=ft.margin.only(top=5),
                                                    
                                                    
                                                )
                                            ],alignment=ft.MainAxisAlignment.CENTER
                                        ),
                                        ft.Row(
                                            [
                                                ft.Text(value="Agendar Exames",
                                                        color=ft.colors.WHITE,
                                                        weight=ft.FontWeight.BOLD,
                                                        size=16,
                                                        
                                                        )
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER
                                        )
                                        ]
                                    )
                                    
                                    
                                    
                                
                                )
                            ]
                        ),
                        on_click= lambda _: print("Agendar Exames")
                    ),

                    #Agendar Consulta
                    ft.Container(
                        width=150,
                        height=150,
                        bgcolor='#71D4D6',
                        border_radius=ft.border_radius.all(10),
                        content=ft.Column(
                            [
                                ft.Container(
                                    width=150,
                                    height=120,
                                    content=ft.Column(
                                        [
                                        ft.Row(
                                            [
                                                ft.Container(
                                                    width=100,
                                                    height=100,
                                                    bgcolor=ft.colors.BLACK45,
                                                    border_radius=ft.border_radius.all(50),
                                                    margin=ft.margin.only(top=5),
                                                    content=ft.Icon(
                                                        name=ft.icons.LOCAL_HOSPITAL,
                                                        color=ft.colors.WHITE,
                                                        size=80
                                                    )
                                        )
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER
                                        ),
                                        ft.Row(
                                            [
                                                ft.Text(
                                                    value="Agendar Consulta",
                                                    color=ft.colors.WHITE,
                                                    size=15,
                                                    weight=ft.FontWeight.BOLD
                                                    
                                                )
                                            ],
                                            ft.MainAxisAlignment.CENTER
                                        )
                                        ],
                                    
                                    ),
                                )
                            ],
                            width=150,
                        ),
                        on_click= lambda _:print("Agendar Consulta")
                    ),
                    
                    #Meus agendamentos
                    ft.Container(
                        width=150,
                        height=150,
                        bgcolor='#71D4D6',
                        border_radius=ft.border_radius.all(10),
                        content=ft.Column(
                            [
                            ft.Container(
                                width=150,
                                height=120,
                                content=ft.Column(
                                    [
                                        ft.Row(
                                            [
                                                ft.Container(
                                                    width=100,
                                                    height=100,
                                                    bgcolor=ft.colors.BLACK45,
                                                    border_radius=ft.border_radius.all(50),
                                                    margin=ft.margin.only(top=5),
                                                    content=ft.Icon(
                                                        name=ft.icons.CONTENT_PASTE_SEARCH,
                                                        color=ft.colors.WHITE,
                                                        size=80
                                                    )
                                                    
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER
                                        ),
                                        
                                        ft.Row(
                                            [
                                                ft.Row(
                                                    [
                                                        ft.Text(
                                                                value="Meus Agendamentos",
                                                                weight=ft.FontWeight.BOLD,
                                                                color=ft.colors.WHITE,
                                                                size=13
                                                            ) 
                                                    ],
                                                    wrap=True,
        
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            
                                            
                                        )
                                    ]
                                )
                            )
                            ]
                        ),
                        on_click= lambda _: print("Meus Agendamentos")
                    ),
                    
                    #Sair do sistema
                    ft.Container(
                        width=150,
                        height=150,
                        bgcolor='#71D4D6',
                        border_radius=ft.border_radius.all(10), 
                        content=ft.Column(
                            [
                            ft.Container(
                                width=150,
                                height=120,
                                content=ft.Column(
                                    [
                                        ft.Row(
                                            [
                                                ft.Container( #Icon sair do sistema
                                                    width=100,
                                                    height=100,
                                                    bgcolor=ft.colors.BLACK45,
                                                    border_radius=ft.border_radius.all(50),
                                                    content= ft.IconButton(
                                                        icon=ft.icons.EXIT_TO_APP,
                                                        icon_color=ft.colors.WHITE,
                                                        icon_size=80,
                                                        on_click= lambda _: pagina_inicial()
                                                    ),
                                                    margin=ft.margin.only(top=5)
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER
                                        ),
                                        
                                        ft.Row( #Descrição do BOX SAIR do sistema
                                            [
                                                ft.Text( 
                                                    value="Sair",
                                                    weight=ft.FontWeight.BOLD,
                                                    color=ft.colors.WHITE,
                                                    size=20
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER
                                        )
                                    ],
                                    spacing=2
                                    
                                )
                            )
                            ]
                        )
                    ),
                ],
                wrap=True,
                alignment=ft.MainAxisAlignment.CENTER
                
            )
            
        pg_menu_central = ft.Container(
                bgcolor=ft.colors.WHITE,
                width=500,
                height=600,
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
                        ft.Container(
                            width=500,
                            height=500,
                            margin=ft.margin.only(top=2),
                            content=ft.Row(
                                    [
                                        opcoes
                                    ],
                                wrap=True
                            ),
                            alignment=ft.alignment.center
                        )
                        
                    ]
                )
            )
            
        page.add(pg_menu_central)

    #Cadastrar usuario
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
                
                
                #Retorno dos dados do banco -- TRUE (Caso os dados sejam salvo) False(Caso os dados já existem)
                result = new_cadastrar_usuario(nome,email,cpf_user,user_password)
                
                #Caso o cadastro seja efetuado aparecera uma mensagem para o usuario
                if result:
                    page.snack_bar = ft.SnackBar(
                        content=ft.Text(value=f"{result}",color=ft.colors.WHITE),
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

    #Reset de senha
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
    
    #Pagina inicial
    def pagina_inicial():
            page.clean()
                
        
            
            # Título - LOGIN
            titulo = ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(
                                name=ft.icons.MEDICAL_SERVICES,
                                size=100,
                                color="#71D4D6",
                                
                                )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [
                            ft.Text(
                                value="MYDOCTOR",
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
                        nm_user
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [
                            password
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
                            on_click=lambda e: acessar(e,nm_user.value,password.value)
                            
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
