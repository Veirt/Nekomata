import Version from "@entity/Version"
import { getConnection } from "typeorm"

export const addPatchInfo = (server: string, url: string): Promise<any> => {
	return new Promise(async (resolve, reject) => {
		try {
			await getConnection().getRepository(Version).save({ server, url })
			resolve(true)
		} catch (err) {
			reject(err)
		}
	})
}

export const removePatchInfo = (server: string): Promise<any> => {
	return new Promise(async (resolve, reject) => {
		try {
			await getConnection().getRepository(Version).findOneOrFail({ server })
			await getConnection().getRepository(Version).delete({ server })
			resolve(true)
		} catch (err) {
			reject(err)
		}
	})
}
