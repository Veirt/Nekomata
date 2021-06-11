import Channel from "@entity/Channel"
import embed from "../helpers/embed"
import {
  addPatchInfo,
  findPatchInfo,
  removePatchInfo,
} from "@helpers/patchInfo"
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
          .save({ server: msg.guild?.id, channel: msg.channel.id })

        const initEmbed = embed(
          "Initialize",
          "Initialize update notice in this channel"
        )
        msg.channel.send(initEmbed)
      } catch (err) {
        if (err.name === "QueryFailedError")
          await getConnection()
            .getRepository(Channel)
            .update({ server: msg.guild?.id }, { channel: msg.channel.id })

        const reinitEmbed = embed(
          "Reinitialize",
          "Reinitialize update notice on this channel"
        )
        msg.channel.send(reinitEmbed)
      }
    }

    if (command === "uninit") {
      try {
        await getConnection()
          .getRepository(Channel)
          .findOneOrFail({ server: msg.guild?.id })

        await getConnection()
          .getRepository(Channel)
          .delete({ server: msg.guild?.id })

        const uninitEmbed = embed(
          "Uninitialized",
          "Uninitialized update notice in this channel"
        )
        msg.channel.send(uninitEmbed)
      } catch (err) {
        const uninitFailedEmbed = embed(
          "Not Initialized",
          "Please initialize the channel first"
        )
        if (err.name === "EntityNotFound") msg.channel.send(uninitFailedEmbed)
      }
    }

    if (command === "list") {
      try {
        const patchInfoEmbed = embed("Version List")

        const patchInfos = await findPatchInfo()
        patchInfos.forEach(patchInfo =>
          patchInfoEmbed.addField(
            patchInfo.server,
            `Version **${patchInfo.version}**\n${patchInfo.url}`
          )
        )
        msg.channel.send(patchInfoEmbed)
      } catch (err) {
        console.error(`Error when finding patch info ${err}`)
      }
    }

    if (command === "add") {
      const [server, url] = [...args]
      if (!server || !url || args.length !== 2)
        msg.channel.send("Invalid arguments")
      else {
        try {
          await addPatchInfo(server, url)
          const addPatchEmbed = embed(
            "Patch Info",
            `Success added patch info for server ${server}`
          )
          msg.channel.send(addPatchEmbed)
        } catch (err) {
          console.error(`Error when adding patch info: ${err}`)
          const addPatchFailedEmbed = embed(
            "Patch Info",
            "Failed adding patch info"
          )
          msg.channel.send(addPatchFailedEmbed)
        }
      }
    }

    if (command === "remove") {
      const [server] = [...args]
      if (!server || args.length !== 1) msg.channel.send("Invalid arguments")
      else {
        try {
          await removePatchInfo(server)
          const removePatchEmbed = embed(
            "Patch Info",
            "Success removed patch info"
          )
          msg.channel.send(removePatchEmbed)
        } catch (err) {
          console.error(`Error when removing patch info: ${err}`)
          if (err.name === "EntityNotFound") {
            const removeFailedEmbed = embed(
              "Patch Info",
              "Patch info doesn't exist"
            )
            msg.channel.send(removeFailedEmbed)
          } else {
            const removeFailedEmbed = embed(
              "Patch Info",
              "Failed removing patch info"
            )
            msg.channel.send(removeFailedEmbed)
          }
        }
      }
    }
  })
}
