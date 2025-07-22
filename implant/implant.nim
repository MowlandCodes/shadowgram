import std/[strutils, os, osproc, strformat, asyncdispatch]
import telebot
import dotenv

let
    env_path: string = &"{getCurrentDir()}/../"

load(env_path)

let API_KEY: string = strip(getEnv("ALPHA_BOT_TOKEN"))
var victimId: string

#[ TODO List

1. Automaticaly receive new ID from Master Bot

]#

proc updateHandler(bot: TeleBot, update: Update): Future[bool] {.async.} =
    # Only handle channel posts
    if not update.channelPost.isNil():
        let message: string = update.channelPost.text
    return true

when isMainModule:
    # Initialize the TeleBot
    let bot = newTeleBot(API_KEY)

    bot.onUpdate(updateHandler)
    bot.poll(offset = -1, limit = 1)
