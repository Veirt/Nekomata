import fs from "fs"
import path from "path"
import Version from "@entity/Version"
import Channel from "@entity/Channel"
import axios from "axios"
import { getConnection } from "typeorm"
import Discord from "discord.js"

export default (client: Discord.Client, channels: Channel[]) => {
	fs.readFile(path.join(__dirname, "../../PatchInfo.json"), (err, data) => {
		if (err) throw err
		const patchInfos: Array<PatchURL> = JSON.parse(data.toString())

		patchInfos.forEach(async patchInfo => {
			const res = await axios.get(patchInfo.url)
			const versionPattern = /\d+/
			const nextVersion = parseInt(res.data.match(versionPattern))

			const prev = await getConnection()
				.getRepository(Version)
				.findOne({ server: patchInfo.server })

			if (prev?.version !== nextVersion) {
				if (prev?.version) {
					channels.forEach(channel => {
						;(
							client.channels.cache.get(channel.channel) as Discord.TextChannel
						).send(`${prev?.version} to ${nextVersion}`)
					})
				}
			}

			if (prev) {
				await getConnection()
					.getRepository(Version)
					.update({ server: patchInfo.server }, { version: nextVersion })
			} else {
				await getConnection()
					.getRepository(Version)
					.save({ server: patchInfo.server, version: nextVersion })
			}
		})
	})
}
