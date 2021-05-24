import "reflect-metadata"
import "@config/index"
import config from "@config/typeorm"
import Channel from "@entity/Channel"
import checkVersion from "@helpers/checkVersion"
import setup from "./commands/setup"
import Discord from "discord.js"
import { createConnection, getRepository } from "typeorm"

createConnection(config).then(() => {
	const client = new Discord.Client()

	const prefix = process.env.PREFIX as string

	client.on("ready", async () => {
		console.log(`Logged in as ${(client.user as Discord.ClientUser).tag}!`)
		setInterval(async () => {
			const channels = await getRepository(Channel).find()
			checkVersion(client, channels)
		}, 10000)
	})

	setup(client, prefix)

	client.login(process.env.TOKEN)
})
