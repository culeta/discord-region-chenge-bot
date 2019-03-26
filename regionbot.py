import discord

client = discord.Client()

region_sg = "シンガポール"
region_ja = "日本"
region_hg = "香港"

change_bef = "に変更します。"
change_aft = "に変更しました。"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

    if message.content.startswith("!region sg"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージ・リージョンの変更
            await message.channel.send(region_sg+change_bef)
            await message.guild.edit(region="singapore")
            await message.channel.send(region_sg + change_aft)
    elif message.content.startswith("!region ja"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージ・リージョンの変更
            await message.channel.send(region_ja + change_bef)
            await message.guild.edit(region="japan")
            await message.channel.send(region_ja + change_aft)
    elif message.content.startswith("!region hg"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージ・リージョンの変更
            await message.channel.send(region_hg + change_bef)
            await message.guild.edit(region="hongkong")
            await message.channel.send(region_hg + change_aft)
    elif message.content.startswith("!region"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # 現在のリージョン確認
            await message.channel.send("現在のリージョンは" + message.guild.region.name + "です。")

# ここにBotのトークンを入力
client.run("token")