import Channel from "@entity/Channel"
import addPatchInfo from "@helpers/addPatchInfo"
import Discord from "discord.js"
import { getConnection } from "typeorm"

export default (client: Discord.Client, prefix: string): void => {
	client.on("message", async msg => {
		if (msg.channel.type === "dm" || !msg.content.startsWith(prefix)) return

		const args = msg.content.slice(prefix.length).trim().split(" ")
		const command = args.shift()

		if (command === "init") {
			try {
				await getConnection()
					.getRepository(Channel)
					.save({ server: msg.guild!.id, channel: msg.channel.id })
				msg.channel.send("Initialize")
			} catch (err) {
				if (err.name === "QueryFailedError")
					await getConnection()
						.getRepository(Channel)
						.update({ server: msg.guild!.id }, { channel: msg.channel.id })

				msg.channel.send("Reinitialize")
			}
		}

		if (command === "uninit") {
			try {
				await getConnection()
					.getRepository(Channel)
					.findOneOrFail({ server: msg.guild!.id })

				await getConnection()
					.getRepository(Channel)
					.delete({ server: msg.guild!.id })
				msg.channel.send("Uninitialized")
			} catch (err) {
				if (err.name === "EntityNotFound") msg.channel.send("Not initialized")
			}
		}

		if (command === "add") {
			const [server, url] = [...args]
			if (!server || !url || args.length !== 2)
				msg.channel.send("Invalid arguments")
			else {
				try {
					await addPatchInfo(server, url)
					msg.channel.send("Success added patch info")
				} catch (err) {
					console.error(`Error when adding patch info: ${err}`)
					msg.channel.send("Failed adding patch info")
				}
			}
		}
	})
}
