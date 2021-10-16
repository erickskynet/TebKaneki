from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import authorized_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>⛄ **Welcome {message.from_user.first_name}** \n
✨ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ᴀᴅᴀʟᴀʜ ʙᴏᴛ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴍᴇᴍᴜᴛᴀʀ ᴍᴜꜱɪᴄ ᴅɪ ɢʀᴏᴜᴘ ꜱᴀʟᴜʀᴀɴ ᴛᴇʟᴇɢʀᴀᴍ ᴀɴᴅᴀ !**

📚 **Tambahkan saya ke grup Anda sekarang untuk memulai musik**

🌹 **ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ꜱᴀʏᴀ ᴋᴇᴛɪᴋ /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "ᴅᴇᴘᴇʟᴏᴠᴇʀ", url=f"https://t.me/{OWNER_NAME}"
                    ),
                    InlineKeyboardButton(
                        "ᴏꜰꜰɪᴄɪᴀʟ ɢʀᴏᴜᴘ", url=f"https://t.me/{GROUP_SUPPORT}")
                ],[
                    InlineKeyboardButton(
                        "ᴏꜰꜰɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}" 
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✅ **bot is running**\n<b>🌈 **uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ɢʀᴏᴜᴘ", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>🙋 Hello tod {message.from_user.mention()}, silakan ketuk tombol di bawah ini untuk melihat pesan bantuan yang dapat Anda baca untuk menggunakan bot ini</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="ʙᴀɢᴀɪᴍᴀɴᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ꜱᴀʏᴀ", url=f"https://t.me/{BOT_USERNAME}?start=help"
                    )
                ]
            ]
        )
    )

@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hello {message.from_user.mention()}, welcome to help menu ✨
\n☢️ ʙᴀɢᴀɪᴍᴀɴᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ꜱᴀʏᴀ ?
\n1. pertama tambahkan saya ke grup Anda.
2. promosikan saya sebagai admin dan berikan semua izin.
3. kemudian, Tambahkan @{ASSISTANT_NAME} ke grup anda atau ketik /userbotjoin.
3. pastikan Anda mengaktifkan obrolan suara terlebih dahulu sebelum mulai memutar musik.
\n☢️ **perintah untuk semua pengguna:**
\\n/play (nama lagu) - putar lagu dari youtube
/stream (membalas audio) - memutar lagu menggunakan file audio
/playlist - tampilkan daftar lagu dalam antrian
/current - tampilkan lagu dalam streaming
/song (nama lagu) - unduh lagu dari youtube
/search (nama video) - cari video dari youtube secara mendetail
/vsong (nama video) - download video dari youtube secara mendetail
/vk (nama lagu) - unduh lagu dari mode inline
\n☢️ **perintah untuk admin:**
\n/player - buka panel pengaturan pemutar musik
/pause - menjeda streaming musik
/resume - melanjutkan musik yang dijeda
/skip - lompat ke lagu berikutnya
/end - hentikan streaming musik
/userbotjoin - undang asisten bergabung ke grup Anda
/reload - untuk menyegarkan daftar admin
/cache - untuk menghapus cache admin
/auth - pengguna resmi untuk menggunakan bot musik
/deauth - tidak sah untuk menggunakan bot musik
/musicplayer (on / off) - nonaktifkan / aktifkan pemutar musik di grup Anda
\n☢️ perintah streaming saluran:
\n/cplay - streaming musik di obrolan suara saluran
/cplayer - tampilkan lagu dalam streaming
/cpause - jeda musik streaming
/cresume - melanjutkan streaming yang dijeda
/cskip - lewati streaming ke lagu berikutnya
/cend - mengakhiri streaming musik
/admincache - menyegarkan cache admin
\n☢️ perintah untuk pengguna sudo:
\n/userbotleaveall - perintahkan asisten untuk keluar dari semua grup
/gcast - mengirim pesan siaran melalui asisten
/rebootmusic - restart teb kaneki music
\n☢️ **perintah untuk bersenang-senang:**
\n/lyric - (nama lagu) lirik scrapper
/chika - periksa sendiri
/wibu - cek sendiri
/asupan - cek sendiri
/truth - periksa sendiri
/dare - periksa sendiri
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ɢʀᴏᴜᴘ", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ᴅᴇᴘᴇʟᴏᴠᴇʀ", url=f"https://t.me/{OWNER_NAME}"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "🏓 `Nih ping nya!!`\n"
        f"🔥 `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@authorized_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🌈 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
