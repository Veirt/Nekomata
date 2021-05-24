import Version from "@entity/Version"
import { getConnection } from "typeorm"

export default (server: string, url: string): Promise<any> => {
	return new Promise(async (resolve, reject) => {
		try {
			await getConnection().getRepository(Version).save({ server, url })
			resolve(true)
		} catch (err) {
			reject(err)
		}
	})
}
