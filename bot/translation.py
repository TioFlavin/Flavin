#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

class Translation(object):
    
    START_TEXT = """<b>Hey {}!!</b>
<i>Sou apenas um bot de filtro automático avançado....😉

Basta me adicionar ao seu grupo e canal e conectá-los e ver meus amigos 🔥🔥😝

Para mais detalhes, clique no botão de ajuda abaixo.
@VoiceChatBrazil
</i>"""    
    
    HELP_TEXT = """
<b><i><u>Como me usar!?</u></i></b>

<i>
-> Adicione-me a qualquer grupo e torne-me administrador
-> Adicione-me ao seu canal desejado
</i>

<b>Bot Comandos (Funciona Apenas em Grupos) :</b>

    -> <code>/add chat_id</code>
                OU - Para conectar um grupo com um canal (o bot deve ser administrador com privilégios totais no grupo e no canal)
     <code>/add @Username</code>
     
    -> <code>/del chat_id</code>
                OU                  - Para desconectar um grupo com um canal
     <code>/del @Username</code>
     
    -> <code>/delall</code>  - Este comando desconectará todos os canais conectados ao grupo e excluirá todos os arquivos do banco de dados
    
    -> <code>/settings</code> -  Este comando exibirá uma instância do painel de configurações que pode ser usada para ajustar as configurações do bot de acordo

            -> <code>Channel</code> - O botão mostrará todos os bate-papos conectados com o grupo e mostrará os botões correspondentes à sua ordem para controles adicionais
            
            -> <code>Filter Types</code> - O botão mostrará a você as 3 opções de filtro disponíveis no bot... Pressionar cada botão irá habilitá-los ou desabilitá-los e isso entrará em ação assim que você usá-los sem a necessidade de um descanso

            -> <code>Configure</code> - O botão ajudará você a alterar o número de páginas / botões por página / resultado total sem realmente comer o repositório ... Também oferece a opção de ativar / desativar a exibição do link de convite em cada resultado
            
            -> <code>Status</code> - O botão mostrará as estatísticas do seu canal
            
@VoiceChatBrazil
"""
    
    ABOUT_TEXT = """<b>➥ Name</b> : <code> Bot de filtro automático</code>
    
<b>➥ Creator</b> : <b><i><a href="https://t.me/TioFlavin_Fx">Tio Flavim</a></i></b>

<b>➥ Language</b> : <code>Python3</code>

<b>➥ Library</b> : <i><a href="https://docs.pyrogram.org">Pyrogram Asyncio 1.13.0 </a></i>

<b>➥ Source Code</b> : <i><a href="https://github.com/TioFlavin/Adv-Auto-Filter-Bot">Click Me</a></i>
"""