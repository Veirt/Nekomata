import Channel from "../entity/Channel"
import addPatchInfo from "../helpers/addPatchInfo";
import Discord from "discord.js";
import { getConnection } from "typeorm";

export default (client: Discord.Client, prefix: string) => {
  client.on('message', async msg => {
    if (msg.content === prefix + 'init') {
      try {
        await getConnection().getRepository(Channel).save({ server: msg.guild!.id, channel: msg.channel.id })
        msg.channel.send("Setup channel here")

      } catch (err) {
        if (err.name === "QueryFailedError")
          await getConnection().getRepository(Channel).update({ server: msg.guild!.id },
            { channel: msg.channel.id })

        msg.channel.send("Success update channel")
      }
    }

    const message = msg.content.split(' ')
    const command = message[1]

    if (command === 'add') {
      const [server, url] = [message[2], message[3]]
      if (!server || !url) msg.channel.send("Invalid arguments")
      else {
        addPatchInfo(server, url)
        msg.channel.send("Success added patch info")
      }
    }

  });
}