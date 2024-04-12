# Bitcoin-Price-Monitor
Bitcoin Price Monitor: Mantenha-se atualizado com o preço do Bitcoin em tempo real diretamente no seu Telegram.

# Monitor de Preço do Bitcoin

Este é um script Python que monitora o preço do Bitcoin em relação ao Real (BRL) utilizando a API do CoinGecko. O script envia atualizações de preço para um canal no Telegram e também armazena os registros em um arquivo JSON.

## Pré-requisitos

- Python 
- Bibliotecas Python: `pycoingecko`, `python-telegram-bot`

## Configuração

1. Instale as bibliotecas Python necessárias executando o seguinte comando:

    ```
    pip install pycoingecko python-telegram-bot
    ```

2. Crie um bot no Telegram e obtenha o token do bot.

3. Obtenha o ID do chat onde deseja enviar as atualizações de preço.

4. Substitua `'SEU_TOKEN_DO_BOT_DO_TELEGRAM'` pelo token do seu bot do Telegram e `'SEU_CHAT_ID'` pelo ID do chat no script `monitor_preco_bitcoin.py`.

## Utilização

Execute o script `monitor_preco_bitcoin.py`. Ele irá iniciar o monitoramento do preço do Bitcoin e enviará atualizações para o canal configurado no Telegram sempre que houver uma mudança de preço.
