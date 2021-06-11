import Discord from "discord.js"
export default (title: string, description?: string): Discord.MessageEmbed => {
  return new Discord.MessageEmbed()
    .setTitle(title)
    .setColor("#e5c7ef")
    .setDescription(description ? description : "")
    .setTimestamp()
}
