import "reflect-metadata"
import config from "./config/typeorm"
import dotenv from "dotenv"
import Discord from "discord.js"
import { createConnection } from "typeorm"
dotenv.config()

createConnection(config).then(connection => {
  const client = new Discord.Client()

  const prefix = process.env.PREFIX

  client.on('ready', () => {
    console.log(`Logged in as ${(client.user as Discord.ClientUser).tag}!`)
  });

  client.on('message', msg => {
    if (msg.content === prefix + 'init') {
      msg.channel.send("Setup channel here")
    }
  });


  client.login(process.env.TOKEN);
})
