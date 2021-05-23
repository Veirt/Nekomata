import Channel from "@entity/Channel"
import addPatchInfo from "@helpers/addPatchInfo"
import Discord from "discord.js"
import { getConnection } from "typeorm"

export default (client: Discord.Client, prefix: string) => {
	client.on("message", async msg => {
		if (msg.channel.type === "dm") return

		if (msg.content === prefix + "init") {
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

		if (msg.content === prefix + "remove") {
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

		const message = msg.content.split(" ")
		const command = message[1]

		if (command === "add") {
			const [server, url] = [message[2], message[3]]
			if (!server || !url) msg.channel.send("Invalid arguments")
			else {
				addPatchInfo(server, url)
				msg.channel.send("Success added patch info")
			}
		}
	})
}
