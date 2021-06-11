import Version from "@entity/Version"
import Channel from "@entity/Channel"
import axios from "axios"
import { getConnection } from "typeorm"
import Discord from "discord.js"

export default async (
  client: Discord.Client,
  channels: Channel[],
  channelsCount: number
): Promise<void> => {
  const patchInfos = await getConnection().getRepository(Version).find()

  patchInfos.forEach(async patchInfo => {
    try {
      const res = await axios.get(patchInfo.url)
      if (res.status !== 200)
        throw Error(`${patchInfo.server}'s version cannot be accessed`)
      const versionPattern = /\d+/
      const nextVersion = parseInt(res.data.match(versionPattern))

      if (patchInfo.version !== nextVersion) {
        if (patchInfo.version) {
          console.log(
            `Sending update of ${patchInfo.server} to ${channelsCount} server(s)`
          )
          const updateEmbed = new Discord.MessageEmbed()
            .setColor("#e5c7ef")
            .setTitle("Update Notice")
            .setDescription(
              `Mogu mogu! ${patchInfo.server} patched from ${patchInfo.version} to ${nextVersion}`
            )
            .setTimestamp()
          channels.forEach(channel => {
            (
              client.channels.cache.get(channel.channel) as Discord.TextChannel
            ).send(updateEmbed)
          })
        }
      }

      try {
        await getConnection()
          .getRepository(Version)
          .update({ server: patchInfo.server }, { version: nextVersion })
      } catch (err) {
        throw new Error(err)
      }
    } catch (err) {
      console.error(
        `Error when checking version of ${patchInfo.server}: ${err}`
      )
    }
  })
}
