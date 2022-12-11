from pyrogram import Client, filters 
from helper.database import db

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**__എനിക്ക് ഒരു ക്യാപ്ക്ഷൻ അയക്ക് ഞാൻ അത് സെറ്റ് ആക്കാം....__\n\n𝙴𝚡𝚊𝚖𝚙𝚕𝚎:- `/set_caption {filename}\n\n💾 Size: {filesize}\n\n⏰ Duration: {duration}`**")
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("__**തന്ന ക്യാപ്ഷൻ ഞാൻ സേവ് ആക്കിട്ടുണ്ട്..👍🏻**__")

    
@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("__**😔 നിങ്ങൾ ഒരു ക്യാപ്ഷനും തന്നിട്ടില്ല..**__")
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text("__**അയ്യോ തന്ന ക്യാപ്ഷൻ ഡിലീറ്റ് ആയി..👍🏻**__")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**നിങ്ങൾ ഇട്ട ക്യാപ്ഷൻ:-**\n\n`{caption}`")
    else:
       await message.reply_text("__**😔 നിങ്ങൾ ഒരു ക്യാപ്ഷനും തന്നിട്ടില്ല..**__")
