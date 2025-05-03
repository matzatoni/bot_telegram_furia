import telebot
import random

bot = telebot.TeleBot('SUA_CHAVE_AQUI')

# Dicionário com os dados dos jogadores
jogadores = {
    "falleN": {
        "nome": "FalleN",
        "posição": "AWP / IGL",
        "kd": "1.03",
        "rating": "1.01",
        "nacionalidade": "🇧🇷 Brasil",
        "idade": "32 anos",
        "hltv": "https://www.hltv.org/player/2023/fallen"
    },
    "yuurih": {
        "nome": "yuurih",
        "posição": "Rifler",
        "kd": "1.18",
        "rating": "1.17",
        "nacionalidade": "🇧🇷 Brasil",
        "idade": "24 anos",
        "hltv": "https://www.hltv.org/player/12553/yuurih"
    },
    "yekindar": {
        "nome": "YEKINDAR",
        "posição": "Entry Fragger",
        "kd": "1.10",
        "rating": "1.09",
        "nacionalidade": "🇱🇻 Letônia",
        "idade": "24 anos",
        "hltv": "https://www.hltv.org/player/13915/yekindar"
    },
    "kscerato": {
        "nome": "KSCERATO",
        "posição": "Rifler (Lurker)",
        "kd": "1.21",
        "rating": "1.20",
        "nacionalidade": "🇧🇷 Brasil",
        "idade": "25 anos",
        "hltv": "https://www.hltv.org/player/15631/kscerato"
    },
    "molodoy": {
        "nome": "molodoy",
        "posição": "Suporte",
        "kd": "1.02",
        "rating": "1.00",
        "nacionalidade": "🇷🇺 Rússia",
        "idade": "22 anos",
        "hltv": "https://www.hltv.org/player/24144/molodoy"
    }
}

# Lista de Mensagens de torcida
mensagens_torcida = [
    "🔥 VAMOOOO FURIAAAAA!!!",
    "🐆 A selva é nossa! Vai pra cima, FURIA!",
    "💥 É bala, é tática, é FURIA dominando!",
    "🎯 Confia no processoooo! FURIA neles!",
    "🇧🇷 Representando o Brasil com garra!",
    "🧠 O professor comanda e a tropa destrói!",
    "📢 A torcida tá com vocês, FURIA!",
    "🎉 Vamos comemorar essa vitória antecipada!",
    "👊 Aqui é FURIA, aqui é raça!",
    "🌪️ Passando o carro como sempre, VAI FURIA!"
]

# Lista de curiosidades
curiosidades = [
    "A FURIA foi fundada em 2017 e rapidamente se tornou uma das principais organizações de eSports do Brasil.",
    "FalleN é conhecido como 'Professor' por seu papel de liderança e influência no cenário.",
    "KSCERATO está na FURIA desde 2018, sendo um dos pilares da equipe.",
    "A FURIA já representou o Brasil em diversos Majors de CS:GO ao redor do mundo.",
    "yuurih é considerado um dos riflers mais consistentes da América do Sul.",
    "A equipe já treinou na Europa por longos períodos para se adaptar ao cenário internacional.",
    "A FURIA é famosa por seu estilo de jogo agressivo e estratégias ousadas.",
    "YEKINDAR já jogou por grandes times como Virtus.pro e Liquid antes de atuar pela FURIA.",
    "FURIA também compete em outros jogos como League of Legends e Valorant.",
    "A torcida da FURIA é uma das mais engajadas no cenário brasileiro de eSports."
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "🐆 **Bem-vindo ao FURIA Bot!** 🔥\n\n"
        "Aqui você acompanha tudo sobre o time de CS da *FURIA* em tempo real:\n\n"
        "📊 Último e próximo jogo\n"
        "🧠 Curiosidades do time\n"
        "👥 Estatísticas dos jogadores\n"
        "📰 Últimas notícias\n"
        "🎉 Simulador de torcida\n\n"
        "Escolha uma opção abaixo para começar 👇"
    )

    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        telebot.types.InlineKeyboardButton("📊 Último Jogo", callback_data="ultimojogo"),
        telebot.types.InlineKeyboardButton("🗓️ Próximo Jogo", callback_data="proximojogo"),
        telebot.types.InlineKeyboardButton("👥 Jogadores", callback_data="players"),
        telebot.types.InlineKeyboardButton("📰 Notícias", callback_data="noticias"),
        telebot.types.InlineKeyboardButton("🎉 Torcida", callback_data="torcica"),
        telebot.types.InlineKeyboardButton("🧠 Curiosidade", callback_data="curiosidades"),
        telebot.types.InlineKeyboardButton("🛒 Loja", url="https://www.furia.gg/")
    )

    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')

# Menu dos jogadores
@bot.callback_query_handler(func=lambda call: call.data == "players")
def show_players_menu(call):
    players_markup = telebot.types.InlineKeyboardMarkup()
    players_markup.add(
        telebot.types.InlineKeyboardButton("FalleN", callback_data="falleN"),
        telebot.types.InlineKeyboardButton("yuurih", callback_data="yuurih"),
        telebot.types.InlineKeyboardButton("YEKINDAR", callback_data="yekindar"),
        telebot.types.InlineKeyboardButton("KSCERATO", callback_data="kscerato"),
        telebot.types.InlineKeyboardButton("molodoy", callback_data="molodoy")
    )
    bot.send_message(call.message.chat.id, "Escolha um jogador para ver as estatísticas:", reply_markup=players_markup)

# Handler para as notícias
@bot.callback_query_handler(func=lambda call: call.data == "noticias")
def show_news(call):
    news_text = (
        "📰 *Últimas Notícias sobre a FURIA*:\n\n"
        "1. **FURIA vence a grande final da ESL Pro League!** 🔥\n"
        "   A FURIA CS:GO acaba de conquistar a vitória na ESL Pro League, garantindo mais um título importante para a sua trajetória. Saiba mais sobre esse grande feito [aqui](https://www.hltv.org/news/2023/12/10/furia-vencendo-esl-pro-league).\n\n"
        "2. **Novos jogadores na FURIA!** 🚨\n"
        "   A FURIA anunciou recentemente a contratação de dois novos talentos para sua line-up. Fique por dentro dessa movimentação [aqui](https://www.furia.gg/noticias/novos-jogadores).\n\n"
        "3. **FURIA vai para o Major!** 🎯\n"
        "   A equipe garantiu sua vaga no próximo Major após uma série de vitórias decisivas. Confira todos os detalhes dessa conquista [aqui](https://www.hltv.org/news/2023/11/22/furia-major-qualification).\n"
    )
    bot.send_message(call.message.chat.id, news_text, parse_mode='Markdown')

# Handler para curiosidades
@bot.callback_query_handler(func=lambda call: call.data == "curiosidades")
def mostrar_curiosidade(call):
    curiosidade = random.choice(curiosidades)
    bot.send_message(call.message.chat.id, f"🧠 *Curiosidade sobre a FURIA:*\n\n_{curiosidade}_", parse_mode='Markdown')

# Handler único para todos os jogadores (Deve ser colocado manualmente, HLTV não possui API para atualizações automaticas).
@bot.callback_query_handler(func=lambda call: call.data in jogadores)
def mostrar_estatisticas(call):
    j = jogadores[call.data]
    texto = (
        f"📊 *Estatísticas do jogador {j['nome']}*:\n\n"
        f"- Posição: {j['posição']}\n"
        f"- KD: {j['kd']}\n"
        f"- Rating HLTV: {j['rating']}\n"
        f"- Nacionalidade: {j['nacionalidade']}\n"
        f"- Idade: {j['idade']}\n"
        f"- Perfil HLTV: [Acesse aqui]({j['hltv']})"
    )
    bot.send_message(call.message.chat.id, texto, parse_mode='Markdown')

# Último Jogo (Deve ser colocado manualmente, HLTV não possui API para atualizações automaticas).
@bot.callback_query_handler(func=lambda call: call.data == "ultimojogo")
def mostrar_ultimo_jogo(call):
    texto = (
        "📊 *Último Jogo da FURIA:*\n\n"
        "🆚 Adversário: *NAVI*\n"
        "📅 Data: *30 de abril de 2025*\n"
        "🕒 Horário: *18:00 BRT*\n"
        "📍 Evento: *ESL Pro League - Quartas de Final*\n"
        "🔚 Resultado: *FURIA 2 x 1 NAVI*\n"
        "🧨 Destaque: *KSCERATO - 1.35 rating*\n"
        "🔗 [Ver na HLTV](https://www.hltv.org/matches)"
    )
    bot.send_message(call.message.chat.id, texto, parse_mode='Markdown')

# Handler para Próximo Jogo
@bot.callback_query_handler(func=lambda call: call.data == "proximojogo")
def mostrar_proximo_jogo(call):
    texto = (
        "🗓️ *Próximo Jogo da FURIA:*\n\n"
        "🆚 Adversário: *Vitality*\n"
        "📅 Data: *3 de maio de 2025*\n"
        "🕒 Horário: *16:00 BRT*\n"
        "📍 Evento: *ESL Pro League - Semifinal*\n"
        "🔗 [Detalhes do confronto](https://www.hltv.org/matches)"
    )
    bot.send_message(call.message.chat.id, texto, parse_mode='Markdown')

# Handler para Simulador de torcida
@bot.callback_query_handler(func=lambda call: call.data == "torcica")
def simular_torcida(call):
    torcida = random.choice(mensagens_torcida)
    bot.send_message(call.message.chat.id, f"🎉 *Simulador de Torcida FURIA:*\n\n_{torcida}_", parse_mode='Markdown')



bot.infinity_polling()
