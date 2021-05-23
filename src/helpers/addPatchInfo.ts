import path from "path"
import fs from "fs"

export default (server: string, url: string) => {
	fs.readFile(path.join(__dirname, "../../PatchInfo.json"), (err, data) => {
		if (err) throw err
		const patchInfos: Array<PatchURL> = JSON.parse(data.toString())
		patchInfos.push({ server, url })

		fs.writeFile(
			path.join(__dirname, "../../PatchInfo.json"),
			JSON.stringify(patchInfos),
			err => {
				if (err) throw err
			}
		)
	})
}
