class script(object):
    START_TXT = """đˇđ´đťđž {},
đźđ đ˝đ°đźđ´ đ¸đ <a href=https://t.me/{}>{}</a>, đ¸ đ˛đ°đ˝ đżđđžđđ¸đłđ´ đźđžđđ¸đ´đ, đšđđđ đ°đłđł đźđ´ đđž đđžđđ đśđđžđđż đ°đ˝đł đ´đ˝đšđžđ đ"""
    HELP_TXT = """đˇđ´đ {}
đˇđ´đđ´ đ¸đ đđˇđ´ đˇđ´đťđż đľđžđ đźđ đ˛đžđźđźđ°đ˝đłđ."""
    ABOUT_TXT = """âŻ đźđ đ˝đ°đźđ´: {}
âŻ đ˛đđ´đ°đđžđ: <a href=https://t.me/MichaelAnjoottiTG<b>đŽđł đđ˘đđĄđđđĽ đđ§đŁđ¨đ¨đ­đ­đ˘ đđ</a>
âŻ đťđ¸đąđđ°đđ: đżđđđžđśđđ°đź
âŻ đťđ°đ˝đśđđ°đśđ´: đżđđđˇđžđ˝ đš
âŻ đłđ°đđ° đąđ°đđ´: đźđžđ˝đśđž đłđą
âŻ đąđžđ đđ´đđđ´đ: đˇđ´đđžđşđ
âŻ đđˇđ°đ˝đşđ đľđžđ đđđżđżđžđđ: <a href=https://t.me/humen_tg><b>Há´á´á´É´ â</a>
âŻ đąđđ¸đťđł đđđ°đđđ: v1.0.1 [ đąđ´đđ° ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- This Is A Closed Source Project. 
- Base Repo - https://github.com/EvamariaTG/EvaMaria  

<b>DEVS:</b>
- <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
â˘ /filter - <code>add a filter in chat</code>
â˘ /filters - <code>list all the filters of a chat</code>
â˘ /del - <code>delete a specific filter in chat</code>
â˘ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
â˘ /connect  - <code>connect a particular chat to your PM</code>
â˘ /disconnect  - <code>disconnect from a chat</code>
â˘ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
â˘ /id - <code>get id of a specified user.</code>
â˘ /info  - <code>get information about a user.</code>
â˘ /imdb  - <code>get the film information from IMDb source.</code>
â˘ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
â˘ /logs - <code>to get the rescent errors</code>
â˘ /stats - <code>to get status of files in db.</code>
â˘ /delete - <code>to delete a specific file from db.</code>
â˘ /users - <code>to get list of my users and ids.</code>
â˘ /chats - <code>to get list of the my chats and ids </code>
â˘ /leave  - <code>to leave from a chat.</code>
â˘ /disable  -  <code>do disable a chat.</code>
â˘ /ban  - <code>to ban a user.</code>
â˘ /unban  - <code>to unban a user.</code>
â˘ /channel - <code>to get list of total connected channels</code>
â˘ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """â đđžđđ°đť đľđ¸đťđ´đ: <code>{}</code>
â đđžđđ°đť đđđ´đđ: <code>{}</code>
â đđžđđ°đť đ˛đˇđ°đđ: <code>{}</code>
â đđđ´đł đđđžđđ°đśđ´: <code>{}</code> đźđđą
â đľđđ´đ´ đđđžđđ°đśđ´: <code>{}</code> đźđđą"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
