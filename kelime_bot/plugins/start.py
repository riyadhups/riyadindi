from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕ Grubuna Ekle", url=f"http://t.me/SozTapBot?startgroup=new")
    ],
    [
        InlineKeyboardButton("🇦🇿🐊 Sahibim", url="https://t.me/Thagiyevvvv"),
        InlineKeyboardButton("🌐 Söhbət Qrupu", url="https://t.me/KarabakhTeamm"),
    ]
])


START = """
**🐊✨ Salam, Qarışıq sözləri tapma oyununa xoş gəldin..**

➤ Məlumat üçün 👉 /help Vurum. Ayarlar asand və sadədir. 
"""

HELP = """
**✨ Ayarlar Menyusuna Xoşəgldiniz.**
/oyun - Oyunu başlatmaq üçün..
/kec - Üç ədəd keçmə haqqınız mövcud, oyunu keçmək üçün.. 
/qreytinq -Qlobal Qrup Reytinqləri (Qrupda Userlərin Rəqabət Sayı)..
/cancel - Oyunu dayandırmaq üçün.. 
"""

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://images.app.goo.gl/rxNaeK9dtMEMpKoa9",caption=START,reply_markup=keyboard)

@Client.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://images.app.goo.gl/rxNaeK9dtMEMpKoa9",caption=HELP) 

# Oyunu başlat. 
@Client.on_message(filters.command("oyun")) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**❗ Oyun Onsuzda Qrupnuzda Davam edir ✍🏻 \n Oyunu dayandırmaq üçün /cancel yazabilərsiniz")
    else:
        await m.reply(f"**{m.from_user.mention}** Tarafından! \nKelime Bulma Oyunu Başladı .\n\nHər birinizə uğurlar ❤️✨ !",reply_markup=RiyaddBlog) 
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["kec"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/20 
📝 Tapılacaq Söz :   <code>{kelime_list}</code>
💰 Yığdınız Xal: 1
🔎 İlk Hərf: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {int(len(kelime_list)/2)} 

✏️ Qarışıq Həriflərdən düzgün sözü tapın.
        """
        await c.send_message(m.chat.id, text)
        
