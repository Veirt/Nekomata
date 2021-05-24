import Version from "@entity/Version"
import { getConnection } from "typeorm"

export default async (server: string, url: string): Promise<void> => {
	try {
		await getConnection().getRepository(Version).save({ server, url })
	} catch (err) {
		console.error(`Error when adding patch info: ${err}`)
	}
}
