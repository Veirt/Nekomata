import Version from "@entity/Version"
import { getConnection } from "typeorm"

export default async (server: string, url: string) => {
	await getConnection().getRepository(Version).save({ server, url })
}
